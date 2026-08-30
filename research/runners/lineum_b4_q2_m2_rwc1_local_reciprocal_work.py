#!/usr/bin/env python3
"""Execute the frozen Q2-M2-RWC1 primary exactly once.

The module deliberately keeps reusable deterministic helpers import-safe so
the permanent test suite can exercise the complete contract without running a
scientific trajectory.  Only :func:`main` performs the one-shot workflow.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time
from typing import Any, BinaryIO, TextIO

import numpy as np


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PROTOCOL_RELATIVE_PATH = (
    "research/lineum-public-tolog-b4/q2-m2-rwc1-preregistration.json"
)
MANIFEST_RELATIVE_PATH = "research/lineum-public-tolog-b4/artifact-manifest.json"
REPORT_RELATIVE_PATH = "research/lineum-public-tolog-galactic-shape-b4.md"
REFERENCE_RUNNER_RELATIVE_PATH = (
    "research/runners/lineum_b4_saturation_localized_l1.py"
)
PRIMARY_RUNNER_RELATIVE_PATH = (
    "research/runners/lineum_b4_q2_m2_rwc1_local_reciprocal_work.py"
)
PRIMARY_TEST_RELATIVE_PATH = (
    "tests/research/test_lineum_b4_q2_m2_rwc1_local_reciprocal_work.py"
)
PROTOCOL_ID = "Q2-M2-RWC1"
PRIMARY_SCHEMA = "lineum.q2-m2-rwc1-primary.v1"
EXECUTION_RECEIPT_SCHEMA = "lineum.q2-m2-rwc1-execution-receipt.v1"
PROTOCOL_SCHEMA = "lineum.q2-m2-rwc1-preregistration.v3"
PRIMARY_CLAIM_ONLY = True
PROTOCOL_EXPECTED_BYTES = 37448
PROTOCOL_EXPECTED_SHA256 = "55917a01e0ab5a04e97515010c70359494769239c5c420ddc4513352a30486fd"
PROTOCOL_EXPECTED_GIT_BLOB = "b6aea98ea752460f5283a40e7e68dea05a9c564a"
PROTOCOL_REMOTE_CHECKPOINT_COMMIT = "9b340097dd4d2aa8cc1c661e40e60811120ca22b"
FROZEN_REMOTE_REF = "refs/remotes/origin/codex/q2-m30-endogenous-balance-20260830"
IMPLEMENTATION_CHECKPOINT_PATHS = frozenset(
    {
        PRIMARY_RUNNER_RELATIVE_PATH,
        PRIMARY_TEST_RELATIVE_PATH,
        REPORT_RELATIVE_PATH,
        MANIFEST_RELATIVE_PATH,
    }
)
PROGRESS_INTERVAL = 500
_STDERR_DIGEST = hashlib.sha256()
_STDERR_BYTE_COUNT = 0

BRANCHES = (
    "CONTROL",
    "RECEIPT_ONLY",
    "PAIR_INTERACTION",
    "PAIR_FLOW",
    "PAIR_BOTH",
    "GLOBAL_POOL_PAIR_BOTH",
)
STENCILS = ("LAP4", "LAP8")
STAGES = ("flow", "interaction")
LOCAL_STAGE_MAP = {
    1: (0, 1),
    2: (1,),
    3: (0,),
    4: (0, 1),
}
TELEMETRY_FIELDS = (
    "psi_cap_contact",
    "phi_cap_contact",
    "destructive_reset",
    "nonfinite_detected",
    "negative_phi_input_detected",
    "undeclared_source_detected",
)


class ContractError(RuntimeError):
    """Raised when a frozen structural or identity contract fails."""


class CandidatePreconditionError(ContractError):
    """Raised before RWC1 arithmetic when a declared precondition fails."""


class TechnicalTrajectoryError(ContractError):
    """Raised when a consumed trajectory cannot publish a complete primary."""


@dataclass(frozen=True)
class FileIdentity:
    path: str
    bytes: int
    sha256: str
    git_blob: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "bytes": self.bytes,
            "sha256": self.sha256,
            "git_blob": self.git_blob,
        }


@dataclass(frozen=True)
class ShardIdentity:
    path: str
    bytes: int
    sha256: str
    git_blob: str
    record_count: int
    first_record_index: int
    last_record_index: int

    def primary_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "bytes": self.bytes,
            "sha256": self.sha256,
            "record_count": self.record_count,
            "first_record_index": self.first_record_index,
            "last_record_index": self.last_record_index,
        }

    def receipt_dict(self) -> dict[str, Any]:
        value = self.primary_dict()
        value["git_blob"] = self.git_blob
        return value


@dataclass(frozen=True)
class PreflightExpectations:
    execution_commit: str
    remote_readback_commit: str
    runner_git_blob: str
    runner_test_git_blob: str
    report_git_blob: str
    manifest_git_blob: str


@dataclass(frozen=True)
class Proposal:
    increment: np.ndarray
    snapshot_token: object
    stage: str


@dataclass
class StencilResult:
    stencil_index: int
    prepared_psi: np.ndarray
    prepared_phi: np.ndarray
    checkpoints: dict[tuple[int, int], tuple[np.ndarray, np.ndarray]]
    energies: np.ndarray
    telemetry: np.ndarray
    local_spools: dict[int, Path]
    global_spool: Path
    proposal_fidelity_passed: bool


def _is_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _is_finite_float(value: Any) -> bool:
    return (
        isinstance(value, (float, np.floating))
        and not isinstance(value, (bool, np.bool_))
        and math.isfinite(float(value))
    )


def _all_nested_finite_floats(value: Any) -> bool:
    if isinstance(value, list):
        return all(_all_nested_finite_floats(item) for item in value)
    return _is_finite_float(value)


def _json_default(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        numeric = float(value)
        if not math.isfinite(numeric):
            raise ValueError("Non-finite NumPy value is not canonical JSON")
        return numeric
    raise TypeError(f"Unsupported canonical JSON type: {type(value).__name__}")


def canonical_json_bytes(value: Any, *, final_lf: bool) -> bytes:
    """Serialize one strict, compact, sorted-key canonical JSON value."""
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
        default=_json_default,
    ).encode("utf-8")
    return encoded + (b"\n" if final_lf else b"")


def canonical_payload_sha256_without_self(payload: Mapping[str, Any]) -> str:
    without_self = dict(payload)
    without_self.pop("canonical_payload_sha256_without_self", None)
    return hashlib.sha256(
        canonical_json_bytes(without_self, final_lf=False)
    ).hexdigest()


def _git_blob_bytes(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def _stream_file_hashes(path: Path, expected_bytes: int) -> tuple[str, str, int, bytes, bytes]:
    sha256 = hashlib.sha256()
    git_blob = hashlib.sha1(f"blob {expected_bytes}\0".encode("ascii"))
    count = 0
    first = b""
    last = b""
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            if not first:
                first = chunk[:3]
            last = chunk[-2:]
            count += len(chunk)
            sha256.update(chunk)
            git_blob.update(chunk)
    return sha256.hexdigest(), git_blob.hexdigest(), count, first, last


def _validate_hex(value: str, length: int, label: str) -> str:
    lowered = value.lower()
    if len(lowered) != length or any(c not in "0123456789abcdef" for c in lowered):
        raise ContractError(f"{label} must be a lowercase {length}-character hex value")
    if value != lowered:
        raise ContractError(f"{label} must be lowercase")
    return value


def repository_path(root: Path, relative_path: str) -> Path:
    candidate = Path(relative_path)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ContractError(f"Repository path is not a safe relative path: {relative_path}")
    resolved_root = root.resolve()
    resolved = (root / candidate).resolve()
    if resolved != resolved_root and resolved_root not in resolved.parents:
        raise ContractError(f"Repository path escapes the checkout: {relative_path}")
    return resolved


def load_json_object(path: Path) -> dict[str, Any]:
    value = strict_json_loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError(f"Expected a JSON object at {path.name}")
    return value


def _reject_duplicate_object_pairs(pairs: Sequence[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ContractError(f"Duplicate JSON object key: {key}")
        result[key] = value
    return result


def _reject_nonfinite_json_constant(value: str) -> Any:
    raise ContractError(f"Non-finite JSON constant is forbidden: {value}")


def strict_json_loads(text: str) -> Any:
    return json.loads(
        text,
        object_pairs_hook=_reject_duplicate_object_pairs,
        parse_constant=_reject_nonfinite_json_constant,
    )


def file_identity(root: Path, relative_path: str) -> FileIdentity:
    data = repository_path(root, relative_path).read_bytes()
    return FileIdentity(
        path=relative_path,
        bytes=len(data),
        sha256=hashlib.sha256(data).hexdigest(),
        git_blob=_git_blob_bytes(data),
    )


def validate_protocol(protocol: Mapping[str, Any]) -> None:
    if protocol.get("schema") != PROTOCOL_SCHEMA:
        raise ContractError("Unexpected RWC1 preregistration schema")
    baseline = protocol.get("baseline")
    retention = protocol.get("retention")
    planned = protocol.get("planned_paths")
    if not isinstance(baseline, dict) or not isinstance(retention, dict) or not isinstance(planned, dict):
        raise ContractError("RWC1 protocol is missing required contract objects")
    if tuple(baseline.get("branches", ())) != BRANCHES:
        raise ContractError("Frozen RWC1 branch order mismatch")
    if tuple(baseline.get("stencils", ())) != STENCILS:
        raise ContractError("Frozen RWC1 stencil order mismatch")
    maps = retention.get("evidence_index_maps", {})
    if tuple(maps.get("branch_index", ())) != BRANCHES:
        raise ContractError("Evidence branch map mismatch")
    if tuple(maps.get("stencil_index", ())) != STENCILS:
        raise ContractError("Evidence stencil map mismatch")
    if tuple(maps.get("stage_index", ())) != STAGES:
        raise ContractError("Evidence stage map mismatch")
    shards = retention.get("evidence_shards")
    planned_shards = planned.get("primary_evidence_shards")
    if not isinstance(shards, list) or len(shards) != 6:
        raise ContractError("Exactly six evidence shards are required")
    if [item.get("path") for item in shards] != planned_shards:
        raise ContractError("Planned evidence shard order mismatch")
    expected_first = 0
    count_total = 0
    for shard in shards:
        count = shard.get("count")
        first = shard.get("first_record_index")
        last = shard.get("last_record_index")
        if not all(_is_int(value) for value in (count, first, last)):
            raise ContractError("Evidence shard indices and counts must be integers")
        if count <= 0 or first != expected_first or last != first + count - 1:
            raise ContractError("Evidence shard ranges must be contiguous and exact")
        expected_first = last + 1
        count_total += count
    if count_total != retention.get("evidence_total_records"):
        raise ContractError("Evidence record total mismatch")


def validate_protocol_identity(root: Path, protocol: Mapping[str, Any], manifest: Mapping[str, Any]) -> FileIdentity:
    validate_protocol(protocol)
    identity = file_identity(root, PROTOCOL_RELATIVE_PATH)
    if (
        identity.bytes != PROTOCOL_EXPECTED_BYTES
        or identity.sha256 != PROTOCOL_EXPECTED_SHA256
        or identity.git_blob != PROTOCOL_EXPECTED_GIT_BLOB
    ):
        raise ContractError("Live RWC1 protocol bytes differ from the remote frozen v3 identity")
    if git_filtered_blob(root, PROTOCOL_RELATIVE_PATH) != PROTOCOL_EXPECTED_GIT_BLOB:
        raise ContractError("Filtered RWC1 protocol blob differs from the remote frozen v3 identity")
    if git_head_blob(root, PROTOCOL_RELATIVE_PATH) != PROTOCOL_EXPECTED_GIT_BLOB:
        raise ContractError("HEAD RWC1 protocol blob differs from the remote frozen v3 identity")
    if not git_is_ancestor(root, PROTOCOL_REMOTE_CHECKPOINT_COMMIT, "HEAD"):
        raise ContractError("Remote frozen v3 checkpoint is not an ancestor of execution HEAD")
    entry = manifest.get("files", {}).get(PROTOCOL_RELATIVE_PATH)
    if not isinstance(entry, dict):
        raise ContractError("Manifest lacks the frozen RWC1 protocol identity")
    expected = {
        "bytes": PROTOCOL_EXPECTED_BYTES,
        "sha256": PROTOCOL_EXPECTED_SHA256,
        "git_blob_sha": PROTOCOL_EXPECTED_GIT_BLOB,
    }
    for key, actual in expected.items():
        if entry.get(key) != actual:
            raise ContractError(f"Frozen protocol identity mismatch for {key}")
    return identity


def _require_candidate_inputs(
    psi_before: np.ndarray,
    phi_before: np.ndarray,
    increment: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    p = np.asarray(psi_before, dtype=np.complex128)
    b = np.asarray(phi_before, dtype=np.float64)
    delta = np.asarray(increment, dtype=np.complex128)
    if p.shape != b.shape or p.shape != delta.shape:
        raise CandidatePreconditionError("RWC1 arrays must have identical shapes")
    z = p + delta
    e0 = np.abs(p) ** 2
    e1 = np.abs(z) ** 2
    w = e1 - e0
    finite = (
        np.isfinite(p)
        & np.isfinite(z)
        & np.isfinite(e0)
        & np.isfinite(e1)
        & np.isfinite(w)
        & np.isfinite(b)
    )
    if not bool(np.all(finite)):
        raise CandidatePreconditionError("RWC1 input or derived work is non-finite")
    if bool(np.any(b < 0.0)):
        raise CandidatePreconditionError("RWC1 phi input is negative")
    return p, b, z, e0, w


def _accepted_phase_projection(
    p: np.ndarray,
    z: np.ndarray,
    e0: np.ndarray,
    w: np.ndarray,
    accepted: np.ndarray,
) -> np.ndarray:
    result = p.copy()
    positive_accepted = accepted > 0.0
    if not bool(np.any(positive_accepted)):
        return result
    rho = np.sqrt(e0 + accepted)
    p_magnitude = np.abs(p)
    z_magnitude = np.abs(z)
    p_zero = positive_accepted & (p_magnitude == 0.0)
    if bool(np.any(p_zero)):
        result[p_zero] = rho[p_zero] * z[p_zero] / z_magnitude[p_zero]
    ordinary = positive_accepted & ~p_zero
    if bool(np.any(ordinary)):
        cross = z[ordinary] * np.conjugate(p[ordinary])
        theta = np.arctan2(np.imag(cross), np.real(cross))
        theta = np.where(theta == -np.pi, np.pi, theta)
        fraction = accepted[ordinary] / w[ordinary]
        base = p[ordinary] / p_magnitude[ordinary]
        result[ordinary] = rho[ordinary] * base * np.exp(1j * fraction * theta)
    return result


def _local_receipt(
    p: np.ndarray,
    b: np.ndarray,
    z: np.ndarray,
    w: np.ndarray,
    psi_after: np.ndarray,
    phi_after: np.ndarray,
    accepted_positive: np.ndarray,
) -> dict[str, Any]:
    positive = w > 0.0
    negative = w < 0.0
    zero = w == 0.0
    accepted_signed = np.where(positive, accepted_positive, w)
    rejected = np.where(positive, np.maximum(w - accepted_positive, 0.0), 0.0)
    proxy_before = np.abs(p) ** 2 + b
    proxy_after = np.abs(psi_after) ** 2 + phi_after
    residual = proxy_after - proxy_before
    scale = np.maximum.reduce(
        (
            np.ones_like(proxy_before),
            np.abs(proxy_before),
            np.abs(proxy_after),
            np.abs(accepted_signed),
        )
    )
    ratio = np.abs(residual) / (1e-10 * scale)
    flat_index = int(np.argmax(ratio.ravel()))
    row, column = np.unravel_index(flat_index, ratio.shape)
    sum_before = float(np.sum(proxy_before))
    sum_after = float(np.sum(proxy_after))
    sum_abs = float(np.sum(np.abs(accepted_signed)))
    aggregate_scale = max(1.0, abs(sum_before), abs(sum_after), sum_abs)
    return {
        "precondition_passed": True,
        "positive_cell_count": int(np.count_nonzero(positive)),
        "negative_cell_count": int(np.count_nonzero(negative)),
        "zero_cell_count": int(np.count_nonzero(zero)),
        "accepted_signed_work_sum": float(np.sum(accepted_signed)),
        "rejected_positive_work_sum": float(np.sum(rejected)),
        "sum_abs_accepted_signed_work": sum_abs,
        "sum_proxy_before": sum_before,
        "sum_proxy_after": sum_after,
        "aggregate_residual": float(sum_after - sum_before),
        "aggregate_scale": float(aggregate_scale),
        "max_cellwise_normalized_residual_ratio": float(ratio.ravel()[flat_index]),
        "argmax_flat_index": flat_index,
        "argmax_row": int(row),
        "argmax_column": int(column),
        "argmax_proxy_before": float(proxy_before.ravel()[flat_index]),
        "argmax_proxy_after": float(proxy_after.ravel()[flat_index]),
        "argmax_accepted_signed_work": float(accepted_signed.ravel()[flat_index]),
        "argmax_residual": float(residual.ravel()[flat_index]),
        "argmax_scale": float(scale.ravel()[flat_index]),
    }


def local_reciprocal_work(
    psi_before: np.ndarray,
    phi_before: np.ndarray,
    increment: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, dict[str, Any]]:
    """Apply the frozen cell-local RWC1 stage without external state access."""
    p, b, z, e0, w = _require_candidate_inputs(psi_before, phi_before, increment)
    positive = w > 0.0
    negative = w < 0.0
    zero = w == 0.0
    accepted = np.where(positive, np.minimum(w, b), 0.0)
    psi_after = p.copy()
    phi_after = b.copy()
    psi_after[negative | zero] = z[negative | zero]
    phi_after[negative] = b[negative] - w[negative]
    if bool(np.any(positive)):
        projected = _accepted_phase_projection(p, z, e0, w, accepted)
        psi_after[positive] = projected[positive]
        phi_after[positive] = b[positive] - accepted[positive]
    if not bool(np.all(np.isfinite(psi_after))) or not bool(np.all(np.isfinite(phi_after))):
        raise CandidatePreconditionError("RWC1 produced a non-finite output")
    receipt = _local_receipt(p, b, z, w, psi_after, phi_after, accepted)
    return psi_after, phi_after, receipt


def global_pool_reciprocal_work(
    psi_before: np.ndarray,
    phi_before: np.ndarray,
    increment: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, dict[str, Any]]:
    """Apply the frozen whole-grid pool control for one selected stage."""
    p, b, z, e0, w = _require_candidate_inputs(psi_before, phi_before, increment)
    positive = w > 0.0
    negative = w < 0.0
    zero = w == 0.0
    credit = b + np.maximum(-w, 0.0)
    positive_work = float(np.sum(np.maximum(w, 0.0)))
    available = float(np.sum(credit))
    debit = min(available, positive_work)
    q = 1.0 if positive_work == 0.0 else debit / positive_work
    remaining = available - debit
    accepted = np.where(positive, q * w, 0.0)
    psi_after = p.copy()
    psi_after[negative | zero] = z[negative | zero]
    if bool(np.any(positive)):
        projected = _accepted_phase_projection(p, z, e0, w, accepted)
        psi_after[positive] = projected[positive]
    phi_after = np.zeros_like(b) if available == 0.0 else credit * (remaining / available)
    if not bool(np.all(np.isfinite(psi_after))) or not bool(np.all(np.isfinite(phi_after))):
        raise CandidatePreconditionError("Global-pool RWC1 produced a non-finite output")
    accepted_signed = np.where(positive, accepted, w)
    rejected = np.where(positive, np.maximum(w - accepted, 0.0), 0.0)
    proxy_before = np.abs(p) ** 2 + b
    proxy_after = np.abs(psi_after) ** 2 + phi_after
    residual = proxy_after - proxy_before
    sum_before = float(np.sum(proxy_before))
    sum_after = float(np.sum(proxy_after))
    sum_abs = float(np.sum(np.abs(accepted_signed)))
    receipt = {
        "precondition_passed": True,
        "positive_cell_count": int(np.count_nonzero(positive)),
        "negative_cell_count": int(np.count_nonzero(negative)),
        "zero_cell_count": int(np.count_nonzero(zero)),
        "accepted_signed_work_sum": float(np.sum(accepted_signed)),
        "rejected_positive_work_sum": float(np.sum(rejected)),
        "sum_abs_accepted_signed_work": sum_abs,
        "sum_proxy_before": sum_before,
        "sum_proxy_after": sum_after,
        "aggregate_residual": float(sum_after - sum_before),
        "aggregate_scale": float(max(1.0, abs(sum_before), abs(sum_after), sum_abs)),
        "P": positive_work,
        "A": available,
        "D": float(debit),
        "q": float(q),
        "remaining": float(remaining),
        "max_abs_cellwise_residual": float(np.max(np.abs(residual))),
        "sum_abs_cellwise_residuals": float(np.sum(np.abs(residual))),
    }
    return psi_after, phi_after, receipt


def _run_git(root: Path, arguments: Sequence[str]) -> str:
    try:
        completed = subprocess.run(
            ["git", *arguments],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        detail = (getattr(exc, "stderr", "") or "").strip() or exc.__class__.__name__
        raise ContractError(f"Git identity query failed: {detail}") from exc
    return completed.stdout.strip()


def git_is_ancestor(root: Path, ancestor: str, descendant: str) -> bool:
    _validate_hex(ancestor, 40, "ancestor commit")
    try:
        completed = subprocess.run(
            ["git", "merge-base", "--is-ancestor", ancestor, descendant],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except OSError as exc:
        raise ContractError("Git ancestry query could not be executed") from exc
    if completed.returncode == 0:
        return True
    if completed.returncode == 1:
        return False
    detail = completed.stderr.strip() or f"exit {completed.returncode}"
    raise ContractError(f"Git ancestry query failed: {detail}")


def git_head(root: Path) -> str:
    return _validate_hex(_run_git(root, ["rev-parse", "HEAD"]), 40, "HEAD commit")


def git_remote_ref_commit(root: Path) -> str:
    return _validate_hex(
        _run_git(root, ["rev-parse", FROZEN_REMOTE_REF]),
        40,
        "frozen remote readback commit",
    )


def git_filtered_blob(root: Path, relative_path: str) -> str:
    value = _run_git(
        root,
        ["hash-object", f"--path={relative_path}", "--", relative_path],
    )
    return _validate_hex(value, 40, f"filtered blob for {relative_path}")


def git_head_blob(root: Path, relative_path: str) -> str:
    return _validate_hex(
        _run_git(root, ["rev-parse", f"HEAD:{relative_path}"]),
        40,
        f"HEAD blob for {relative_path}",
    )


def git_worktree_clean(root: Path) -> bool:
    return _run_git(root, ["status", "--porcelain", "--untracked-files=all"]) == ""


def git_implementation_checkpoint_paths(root: Path, head: str) -> frozenset[str]:
    """Return paths changed from the immutable v3 checkpoint to execution HEAD."""
    _validate_hex(head, 40, "execution HEAD commit")
    output = _run_git(
        root,
        [
            "diff",
            "--name-only",
            "--no-renames",
            PROTOCOL_REMOTE_CHECKPOINT_COMMIT,
            head,
            "--",
        ],
    )
    paths = [line.strip().replace("\\", "/") for line in output.splitlines() if line.strip()]
    if len(paths) != len(set(paths)):
        raise ContractError("Implementation checkpoint diff contains duplicate paths")
    return frozenset(paths)


def strict_runtime_gate(protocol: Mapping[str, Any]) -> dict[str, Any]:
    expected = protocol["runtime"]
    actual_python = platform.python_version()
    actual_numpy = np.__version__
    backend = "cpu_numpy_deterministic"
    return {
        "passed": bool(
            actual_python == expected["python"]
            and actual_numpy == expected["numpy"]
            and backend == expected["backend"]
        ),
        "backend": backend,
        "python": actual_python,
        "numpy": actual_numpy,
    }


def _manifest_expected_blob(
    manifest: Mapping[str, Any],
    relative_path: str,
    fallback: str,
) -> str:
    entry = manifest.get("files", {}).get(relative_path)
    if not isinstance(entry, dict):
        raise ContractError(f"Manifest lacks implementation identity for {relative_path}")
    manifest_blob = entry.get("git_blob_sha")
    if manifest_blob != fallback:
        raise ContractError(f"Explicit and manifest identities disagree for {relative_path}")
    return _validate_hex(fallback, 40, f"expected blob for {relative_path}")


def verify_primary_preflight(
    root: Path,
    protocol: Mapping[str, Any],
    manifest: Mapping[str, Any],
    expectations: PreflightExpectations,
    *,
    require_clean: bool,
    allow_existing_receipt: bool,
) -> dict[str, Any]:
    """Verify the frozen clean/read-back identities and output absence."""
    validate_protocol(protocol)
    planned = protocol["planned_paths"]
    runner_path = planned["runner"]
    runner_test_path = planned["runner_test"]
    _manifest_expected_blob(manifest, runner_path, expectations.runner_git_blob)
    _manifest_expected_blob(manifest, runner_test_path, expectations.runner_test_git_blob)
    if manifest.get("source_report") != REPORT_RELATIVE_PATH:
        raise ContractError("Manifest source_report path is not the canonical report")
    q2_manifest = manifest.get("q2_m2_rwc1")
    if not isinstance(q2_manifest, dict):
        raise ContractError("Manifest lacks the Q2-M2-RWC1 checkpoint object")
    if q2_manifest.get("continuity_report_git_blob") != expectations.report_git_blob:
        raise ContractError("Explicit and manifest report identities disagree")

    head = git_head(root)
    remote_ref_commit = git_remote_ref_commit(root)
    implementation_paths = git_implementation_checkpoint_paths(root, head)
    implementation_scope_exact = implementation_paths == IMPLEMENTATION_CHECKPOINT_PATHS
    status_text = _run_git(root, ["status", "--porcelain", "--untracked-files=all"])
    if allow_existing_receipt:
        receipt_status = f"?? {planned['primary_execution_receipt']}"
        status_lines = [line for line in status_text.splitlines() if line]
        clean = status_lines == [receipt_status]
    else:
        clean = status_text == ""
    path_expectations = {
        runner_path: expectations.runner_git_blob,
        runner_test_path: expectations.runner_test_git_blob,
        REPORT_RELATIVE_PATH: expectations.report_git_blob,
        MANIFEST_RELATIVE_PATH: expectations.manifest_git_blob,
    }
    path_rows: dict[str, dict[str, Any]] = {}
    paths_pass = True
    for relative_path, expected_blob in path_expectations.items():
        filtered = git_filtered_blob(root, relative_path)
        head_blob = git_head_blob(root, relative_path)
        path_pass = filtered == expected_blob and head_blob == expected_blob
        paths_pass = paths_pass and path_pass
        path_rows[relative_path] = {
            "expected": expected_blob,
            "filtered": filtered,
            "head": head_blob,
            "passed": path_pass,
        }

    source_expected = {
        "lineum_core/math.py": protocol["source_bindings"]["core_math_git_blob"],
        REFERENCE_RUNNER_RELATIVE_PATH: protocol["source_bindings"][
            "localized_reference_runner_git_blob"
        ],
        "requirements.txt": protocol["source_bindings"]["requirements_git_blob"],
        "requirements-dev.txt": protocol["source_bindings"]["requirements_dev_git_blob"],
    }
    source_actual: dict[str, str] = {}
    source_head: dict[str, str] = {}
    sources_pass = True
    for relative_path, expected_blob in source_expected.items():
        filtered = git_filtered_blob(root, relative_path)
        head_blob = git_head_blob(root, relative_path)
        source_actual[relative_path] = filtered
        source_head[relative_path] = head_blob
        sources_pass = sources_pass and filtered == expected_blob and head_blob == expected_blob

    output_paths = [
        planned["primary_output"],
        *planned["primary_evidence_shards"],
        planned["checker"],
        planned["checker_test"],
        planned["checker_output"],
        planned["checker_execution_receipt"],
    ]
    if not allow_existing_receipt:
        output_paths.append(planned["primary_execution_receipt"])
    outputs_absent = all(not repository_path(root, value).exists() for value in output_paths)
    runtime = strict_runtime_gate(protocol)
    passed = bool(
        head == expectations.execution_commit
        and head == remote_ref_commit
        and remote_ref_commit == expectations.remote_readback_commit
        and implementation_scope_exact
        and (clean or not require_clean)
        and paths_pass
        and sources_pass
        and outputs_absent
        and runtime["passed"]
    )
    return {
        "passed": passed,
        "expected_execution_commit": expectations.execution_commit,
        "actual_head_commit": head,
        "remote_readback_commit": remote_ref_commit,
        "head_equals_remote_readback_commit": head == remote_ref_commit,
        "implementation_checkpoint_paths": sorted(implementation_paths),
        "implementation_scope_exact": implementation_scope_exact,
        "worktree_clean": clean,
        "expected_runner_git_blob": expectations.runner_git_blob,
        "actual_runner_filtered_git_blob": path_rows[runner_path]["filtered"],
        "actual_runner_head_git_blob": path_rows[runner_path]["head"],
        "expected_runner_test_git_blob": expectations.runner_test_git_blob,
        "actual_runner_test_filtered_git_blob": path_rows[runner_test_path]["filtered"],
        "actual_runner_test_head_git_blob": path_rows[runner_test_path]["head"],
        "expected_report_git_blob": expectations.report_git_blob,
        "actual_report_filtered_git_blob": path_rows[REPORT_RELATIVE_PATH]["filtered"],
        "actual_report_head_git_blob": path_rows[REPORT_RELATIVE_PATH]["head"],
        "expected_manifest_git_blob": expectations.manifest_git_blob,
        "actual_manifest_filtered_git_blob": path_rows[MANIFEST_RELATIVE_PATH]["filtered"],
        "actual_manifest_head_git_blob": path_rows[MANIFEST_RELATIVE_PATH]["head"],
        "expected": {
            "core_math_git_blob": source_expected["lineum_core/math.py"],
            "localized_reference_runner_git_blob": source_expected[
                REFERENCE_RUNNER_RELATIVE_PATH
            ],
            "requirements_git_blob": source_expected["requirements.txt"],
            "requirements_dev_git_blob": source_expected["requirements-dev.txt"],
        },
        "actual": {
            "core_math_git_blob": source_actual["lineum_core/math.py"],
            "localized_reference_runner_git_blob": source_actual[
                REFERENCE_RUNNER_RELATIVE_PATH
            ],
            "requirements_git_blob": source_actual["requirements.txt"],
            "requirements_dev_git_blob": source_actual["requirements-dev.txt"],
        },
        "head_source_blobs": source_head,
        "outputs_absent": outputs_absent,
        "runtime_gate": runtime,
    }


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _receipt_with_hash(payload: Mapping[str, Any]) -> dict[str, Any]:
    result = dict(payload)
    result["canonical_payload_sha256_without_self"] = canonical_payload_sha256_without_self(result)
    return result


def create_primary_latch(
    root: Path,
    protocol: Mapping[str, Any],
    protocol_identity: FileIdentity,
    preflight: Mapping[str, Any],
) -> Path:
    """Exclusively create the durable consumed-authority receipt."""
    planned = protocol["planned_paths"]
    receipt_path = repository_path(root, planned["primary_execution_receipt"])
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    payload = _receipt_with_hash(
        {
            "schema": EXECUTION_RECEIPT_SCHEMA,
            "protocol_id": PROTOCOL_ID,
            "lane": "primary",
            "attempt": 1,
            "invocation_limit": 1,
            "authority_consumed": True,
            "retry_authorized": False,
            "status": "attempt_started_authority_consumed",
            "started_at": _utc_now(),
            "ended_at": None,
            "elapsed_seconds": None,
            "execution_commit": preflight["actual_head_commit"],
            "program_identity": {
                "path": planned["runner"],
                "git_blob": preflight["actual_runner_filtered_git_blob"],
                "test_path": planned["runner_test"],
                "test_git_blob": preflight["actual_runner_test_filtered_git_blob"],
            },
            "input_identity": {
                "protocol": protocol_identity.as_dict(),
                "source_bindings": dict(preflight["actual"]),
                "runtime": dict(preflight["runtime_gate"]),
            },
            "output_identity": None,
            "stderr_identity": None,
            "failure": None,
        }
    )
    data = canonical_json_bytes(payload, final_lf=True)
    descriptor = os.open(receipt_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, "wb", closefd=True) as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        raise
    return receipt_path


def update_primary_receipt(
    receipt_path: Path,
    *,
    status: str,
    elapsed_seconds: float,
    output_identity: Mapping[str, Any] | None,
    stderr_identity: Mapping[str, Any] | None,
    failure: Mapping[str, str] | None,
) -> None:
    """Finalize the existing non-deletable latch without creating a new path."""
    if status not in {"complete_output_retained", "technical_non_result"}:
        raise ContractError("Invalid terminal receipt status")
    current = load_json_object(receipt_path)
    if current.get("status") != "attempt_started_authority_consumed":
        raise ContractError("Primary receipt is not in the started state")
    current.update(
        {
            "status": status,
            "ended_at": _utc_now(),
            "elapsed_seconds": float(elapsed_seconds),
            "output_identity": None if output_identity is None else dict(output_identity),
            "stderr_identity": None if stderr_identity is None else dict(stderr_identity),
            "failure": None if failure is None else dict(failure),
        }
    )
    current = _receipt_with_hash(current)
    data = canonical_json_bytes(current, final_lf=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=receipt_path.parent,
            prefix=f".{receipt_path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_path = Path(handle.name)
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, receipt_path)
        temporary_path = None
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


def _load_reference_runner(root: Path) -> Any:
    path = repository_path(root, REFERENCE_RUNNER_RELATIVE_PATH)
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("rwc1_frozen_localized_reference", path)
    if spec is None or spec.loader is None:
        raise ContractError("Unable to load the frozen localized reference runner")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def historical_proposals(
    psi: np.ndarray,
    phi: np.ndarray,
    kappa: np.ndarray,
    mu: np.ndarray,
    dt: float,
    snapshot_token: object,
) -> tuple[Proposal, Proposal]:
    """Compute both unchanged historical stage increments once from S0."""
    drift_multiplier = 1.0 + mu
    clipped_phi = np.clip(phi, 0.0, 10.0)
    raw_interaction = 0.04 * clipped_phi * kappa * drift_multiplier
    interaction_factor = 0.1 * np.tanh(raw_interaction / 0.1)
    interaction = interaction_factor * psi
    interaction = interaction / (1.0 + np.abs(interaction) / 10.0)
    gradient_phi_x, gradient_phi_y = np.gradient(phi, axis=(0, 1))
    flow = -0.004 * (gradient_phi_x + 1j * gradient_phi_y) * kappa * drift_multiplier
    flow = flow / (1.0 + np.abs(flow) / 10.0)
    return (
        Proposal(flow * dt, snapshot_token, "flow"),
        Proposal(interaction * dt, snapshot_token, "interaction"),
    )


def validate_proposal(proposal: Proposal, snapshot_token: object, stage: str) -> bool:
    return proposal.snapshot_token is snapshot_token and proposal.stage == stage


def _flow_guard(psi: np.ndarray, cap: float) -> tuple[np.ndarray, bool]:
    magnitude = np.abs(psi)
    mask = magnitude > cap
    if not bool(np.any(mask)):
        return psi, False
    scale = np.ones_like(magnitude)
    scale[mask] = cap / (magnitude[mask] + 1e-30)
    return psi * scale, True


def _common_tail(
    reference: Any,
    psi: np.ndarray,
    phi: np.ndarray,
    kappa: np.ndarray,
    stencil: str,
    dt: float,
    psi_cap: float,
    phi_cap: float,
    reset_ratio: float,
) -> tuple[np.ndarray, np.ndarray, bool, bool, bool]:
    psi = psi - 0.005 * psi * dt
    psi = psi + reference.diffuse(psi[None, ...], kappa[None, ...], 0.05, stencil)[0] * kappa * dt
    energy = np.abs(psi) ** 2
    transferred = 0.001 * energy * kappa * dt
    phi = phi + transferred
    new_magnitude = np.sqrt(np.maximum(energy - transferred, 0.0))
    psi = psi / (np.sqrt(energy) + 1e-12) * new_magnitude
    phi = phi + 0.05 * reference.diffuse(phi[None, ...], kappa[None, ...], 0.05, stencil)[0]
    phi_contact = bool(np.any((phi < 0.0) | (phi > phi_cap)))
    phi = np.clip(phi, 0.0, phi_cap)
    nonfinite = not bool(np.all(np.isfinite(psi)) and np.all(np.isfinite(phi)))
    finite_max = float(np.max(np.where(np.isfinite(np.abs(psi)), np.abs(psi), 0.0)))
    destructive_reset = bool(nonfinite or finite_max >= psi_cap * reset_ratio)
    if destructive_reset:
        psi = np.zeros_like(psi)
    return psi, phi, phi_contact, destructive_reset, nonfinite


def local_record_index(stencil_index: int, branch_index: int, step: int, stage_index: int) -> int:
    if stencil_index not in (0, 1) or branch_index not in LOCAL_STAGE_MAP:
        raise ContractError("Invalid local receipt index coordinate")
    if stage_index not in LOCAL_STAGE_MAP[branch_index] or not 1 <= step <= 10000:
        raise ContractError("Invalid local receipt stage or step")
    branch_offsets = {1: 0, 2: 20000, 3: 30000, 4: 40000}
    within_step = (
        (step - 1) * 2 + stage_index
        if len(LOCAL_STAGE_MAP[branch_index]) == 2
        else step - 1
    )
    return 240110 + stencil_index * 60000 + branch_offsets[branch_index] + within_step


def global_record_index(stencil_index: int, step: int, stage_index: int) -> int:
    if stencil_index not in (0, 1) or stage_index not in (0, 1) or not 1 <= step <= 10000:
        raise ContractError("Invalid global receipt index coordinate")
    return 360110 + stencil_index * 20000 + (step - 1) * 2 + stage_index


def _receipt_record(
    receipt: Mapping[str, Any],
    *,
    record_index: int,
    record_type: str,
    stencil_index: int,
    branch_index: int,
    step: int,
    stage_index: int,
) -> dict[str, Any]:
    return {
        "record_index": record_index,
        "record_type": record_type,
        "stencil_index": stencil_index,
        "branch_index": branch_index,
        "step": step,
        "stage_index": stage_index,
        **dict(receipt),
    }


def _write_spool_line(handle: BinaryIO, record: Mapping[str, Any]) -> None:
    handle.write(canonical_json_bytes(record, final_lf=True))


def _progress(stencil: str, completed: int, total: int, started: float) -> None:
    if completed != total and completed % PROGRESS_INTERVAL != 0:
        return
    elapsed = time.monotonic() - started
    _emit_stderr_line(
        json.dumps(
            {
                "phase": "rwc1_continuation",
                "stencil": stencil,
                "completed": completed,
                "total": total,
                "elapsed_seconds": round(elapsed, 3),
            },
            sort_keys=True,
        )
    )


def _reset_stderr_identity() -> None:
    global _STDERR_DIGEST, _STDERR_BYTE_COUNT
    _STDERR_DIGEST = hashlib.sha256()
    _STDERR_BYTE_COUNT = 0


def _emit_stderr_line(message: str) -> None:
    global _STDERR_BYTE_COUNT
    data = (message + "\n").encode("utf-8")
    _STDERR_DIGEST.update(data)
    _STDERR_BYTE_COUNT += len(data)
    sys.stderr.write(message + "\n")
    sys.stderr.flush()


def _stderr_identity(status_summary: str) -> dict[str, Any]:
    return {
        "bytes": int(_STDERR_BYTE_COUNT),
        "sha256": _STDERR_DIGEST.hexdigest(),
        "status_summary": status_summary,
    }


def prepare_baseline(reference: Any, protocol: Mapping[str, Any], stencil: str) -> tuple[np.ndarray, np.ndarray]:
    baseline = protocol["baseline"]
    size = int(baseline["grid_size"])
    psi = np.asarray(reference.GAUSSIAN, dtype=np.complex128)[None, ...].copy()
    if psi.shape != (1, size, size):
        raise TechnicalTrajectoryError("Frozen initial Gaussian shape mismatch")
    phi = np.full((1, size, size), float(baseline["initial_phi"]), dtype=np.float64)
    kappa = np.full_like(phi, float(baseline["kappa"]), dtype=np.float64)
    mu = np.full_like(phi, float(baseline["mu"]), dtype=np.float64)
    specs = [(reference.LANES[0], float(baseline["initial_phi"]))]
    lane_arrays = reference.build_lane_arrays(specs)
    with np.errstate(all="ignore"):
        for _ in range(int(baseline["preparation_steps"])):
            psi, phi, reset, psi_cap, phi_cap = reference.advance_batch_one_step(
                psi, phi, kappa, mu, stencil, lane_arrays
            )
            if bool(reset[0] or psi_cap[0] or phi_cap[0]):
                raise TechnicalTrajectoryError("Historical preparation touched a frozen guard")
            if not bool(np.all(np.isfinite(psi)) and np.all(np.isfinite(phi))):
                raise TechnicalTrajectoryError("Historical preparation became non-finite")
    return psi[0].copy(), phi[0].copy()


def _apply_branch_stages(
    branch_index: int,
    psi0: np.ndarray,
    phi0: np.ndarray,
    flow: Proposal,
    interaction: Proposal,
    snapshot_token: object,
    psi_cap: float,
) -> tuple[np.ndarray, np.ndarray, bool, list[tuple[int, dict[str, Any]]], bool]:
    source_valid = validate_proposal(flow, snapshot_token, "flow") and validate_proposal(
        interaction, snapshot_token, "interaction"
    )
    if not source_valid:
        raise TechnicalTrajectoryError("Proposal provenance guard failed")
    local_receipts: list[tuple[int, dict[str, Any]]] = []

    if branch_index == 0:
        psi1 = psi0 + flow.increment
        phi1 = phi0
    elif branch_index == 1:
        _, _, flow_receipt = local_reciprocal_work(psi0, phi0, flow.increment)
        local_receipts.append((0, flow_receipt))
        psi1 = psi0 + flow.increment
        phi1 = phi0
    elif branch_index in (2,):
        psi1 = psi0 + flow.increment
        phi1 = phi0
    elif branch_index in (3, 4):
        psi1, phi1, flow_receipt = local_reciprocal_work(psi0, phi0, flow.increment)
        local_receipts.append((0, flow_receipt))
    elif branch_index == 5:
        psi1, phi1, _ = global_pool_reciprocal_work(psi0, phi0, flow.increment)
    else:
        raise ContractError("Unknown RWC1 branch index")

    psi1, cap_contact = _flow_guard(psi1, psi_cap)
    if branch_index == 0:
        psi2 = psi1 + interaction.increment
        phi2 = phi1
    elif branch_index == 1:
        _, _, interaction_receipt = local_reciprocal_work(
            psi1, phi1, interaction.increment
        )
        local_receipts.append((1, interaction_receipt))
        psi2 = psi1 + interaction.increment
        phi2 = phi1
    elif branch_index == 2:
        psi2, phi2, interaction_receipt = local_reciprocal_work(
            psi1, phi1, interaction.increment
        )
        local_receipts.append((1, interaction_receipt))
    elif branch_index == 3:
        psi2 = psi1 + interaction.increment
        phi2 = phi1
    elif branch_index == 4:
        psi2, phi2, interaction_receipt = local_reciprocal_work(
            psi1, phi1, interaction.increment
        )
        local_receipts.append((1, interaction_receipt))
    else:
        psi2, phi2, _ = global_pool_reciprocal_work(
            psi1, phi1, interaction.increment
        )
    return psi2, phi2, cap_contact, local_receipts, source_valid


def simulate_stencil(
    stencil: str,
    stencil_index: int,
    protocol: Mapping[str, Any],
    reference: Any,
    spool_directory: Path,
) -> StencilResult:
    """Run one frozen stencil; callers must never use this in unit tests."""
    baseline = protocol["baseline"]
    thresholds = protocol["thresholds"]
    continuation_steps = int(baseline["continuation_steps"])
    if continuation_steps != 10000:
        raise ContractError("RWC1 continuation length differs from the frozen index map")
    prepared_psi, prepared_phi = prepare_baseline(reference, protocol, stencil)
    size = int(baseline["grid_size"])
    psi = np.stack([prepared_psi.copy() for _ in BRANCHES])
    phi = np.stack([prepared_phi.copy() for _ in BRANCHES])
    kappa = np.full((size, size), float(baseline["kappa"]), dtype=np.float64)
    mu = np.full((size, size), float(baseline["mu"]), dtype=np.float64)
    dt = float(baseline["dt"])
    psi_cap = float(thresholds["historical_psi_cap"])
    phi_cap = float(thresholds["historical_phi_cap"])
    reset_ratio = float(thresholds["historical_psi_destructive_reset_ratio"])
    checkpoints: dict[tuple[int, int], tuple[np.ndarray, np.ndarray]] = {
        (branch_index, 0): (psi[branch_index].copy(), phi[branch_index].copy())
        for branch_index in range(len(BRANCHES))
    }
    checkpoint_steps = set(int(value) for value in baseline["checkpoints"])
    energies = np.empty((len(BRANCHES), continuation_steps), dtype=np.float64)
    telemetry = np.zeros(
        (len(BRANCHES), continuation_steps, len(TELEMETRY_FIELDS)), dtype=np.bool_
    )
    local_paths = {
        branch_index: spool_directory / f"local-{stencil_index}-{branch_index}.jsonl"
        for branch_index in LOCAL_STAGE_MAP
    }
    global_path = spool_directory / f"global-{stencil_index}.jsonl"
    local_handles = {key: path.open("xb") for key, path in local_paths.items()}
    global_handle = global_path.open("xb")
    started = time.monotonic()
    try:
        for step in range(1, continuation_steps + 1):
            next_psi = np.empty_like(psi)
            next_phi = np.empty_like(phi)
            for branch_index in range(len(BRANCHES)):
                psi0 = psi[branch_index].copy()
                phi0 = phi[branch_index].copy()
                if not bool(np.all(np.isfinite(psi0)) and np.all(np.isfinite(phi0))):
                    raise TechnicalTrajectoryError("Non-finite branch state before a declared stage")
                token = object()
                flow, interaction = historical_proposals(psi0, phi0, kappa, mu, dt, token)
                psi2, phi2, psi_cap_contact, receipts, source_valid = _apply_branch_stages(
                    branch_index,
                    psi0,
                    phi0,
                    flow,
                    interaction,
                    token,
                    psi_cap,
                )
                global_receipts: list[tuple[int, dict[str, Any]]] = []
                if branch_index == 5:
                    _, _, flow_receipt = global_pool_reciprocal_work(
                        psi0, phi0, flow.increment
                    )
                    psi1, phi1, _ = global_pool_reciprocal_work(
                        psi0, phi0, flow.increment
                    )
                    psi1, _ = _flow_guard(psi1, psi_cap)
                    _, _, interaction_receipt = global_pool_reciprocal_work(
                        psi1, phi1, interaction.increment
                    )
                    global_receipts = [(0, flow_receipt), (1, interaction_receipt)]

                psi3, phi3, phi_cap_contact, destructive_reset, nonfinite = _common_tail(
                    reference,
                    psi2,
                    phi2,
                    kappa,
                    stencil,
                    dt,
                    psi_cap,
                    phi_cap,
                    reset_ratio,
                )
                negative_input = bool(
                    branch_index in LOCAL_STAGE_MAP or branch_index == 5
                ) and bool(np.any(phi0 < 0.0))
                flags = (
                    psi_cap_contact,
                    phi_cap_contact,
                    destructive_reset,
                    nonfinite,
                    negative_input,
                    not source_valid,
                )
                telemetry[branch_index, step - 1, :] = flags
                if any(flags):
                    raise TechnicalTrajectoryError(
                        f"Frozen technical telemetry failed at {stencil} step {step} branch {branch_index}"
                    )
                next_psi[branch_index] = psi3
                next_phi[branch_index] = phi3
                energies[branch_index, step - 1] = float(np.sum(np.abs(psi3) ** 2))
                for stage_index, receipt in receipts:
                    record = _receipt_record(
                        receipt,
                        record_index=local_record_index(
                            stencil_index, branch_index, step, stage_index
                        ),
                        record_type="local_stage_receipt",
                        stencil_index=stencil_index,
                        branch_index=branch_index,
                        step=step,
                        stage_index=stage_index,
                    )
                    _write_spool_line(local_handles[branch_index], record)
                for stage_index, receipt in global_receipts:
                    record = _receipt_record(
                        receipt,
                        record_index=global_record_index(stencil_index, step, stage_index),
                        record_type="global_stage_receipt",
                        stencil_index=stencil_index,
                        branch_index=5,
                        step=step,
                        stage_index=stage_index,
                    )
                    _write_spool_line(global_handle, record)
            psi = next_psi
            phi = next_phi
            if step in checkpoint_steps:
                for branch_index in range(len(BRANCHES)):
                    checkpoints[(branch_index, step)] = (
                        psi[branch_index].copy(),
                        phi[branch_index].copy(),
                    )
            _progress(stencil, step, continuation_steps, started)
    finally:
        for handle in local_handles.values():
            handle.close()
        global_handle.close()
    return StencilResult(
        stencil_index=stencil_index,
        prepared_psi=prepared_psi,
        prepared_phi=prepared_phi,
        checkpoints=checkpoints,
        energies=energies,
        telemetry=telemetry,
        local_spools=local_paths,
        global_spool=global_path,
        proposal_fidelity_passed=True,
    )


def orchestrate_stencils(
    protocol: Mapping[str, Any],
    runner: Callable[[str, int], StencilResult],
) -> list[StencilResult]:
    """Invoke exactly one LAP4 payload followed by exactly one LAP8 payload."""
    stencils = tuple(protocol["baseline"]["stencils"])
    if stencils != STENCILS:
        raise ContractError("Scientific orchestration requires the frozen two-stencil order")
    return [runner(stencil, index) for index, stencil in enumerate(stencils)]


def _all_finite_json(value: Any) -> bool:
    if isinstance(value, dict):
        return all(isinstance(key, str) and _all_finite_json(item) for key, item in value.items())
    if isinstance(value, (list, tuple)):
        return all(_all_finite_json(item) for item in value)
    if isinstance(value, (float, np.floating)):
        return math.isfinite(float(value))
    if isinstance(value, (str, int, bool, np.integer, np.bool_)):
        return True
    return False


def validate_evidence_record(record: Mapping[str, Any], protocol: Mapping[str, Any]) -> None:
    schemas = protocol["retention"]["evidence_record_schemas"]
    record_type = record.get("record_type")
    if record_type not in schemas:
        raise ContractError("Evidence record_type is not a frozen schema name")
    expected_fields = set(schemas[record_type]["fields"])
    if set(record) != expected_fields:
        raise ContractError(f"Evidence {record_type} key set mismatch")
    integer_fields = {
        "record_index", "stencil_index", "branch_index", "checkpoint_index",
        "step", "stage_index", "positive_cell_count", "negative_cell_count",
        "zero_cell_count", "argmax_flat_index", "argmax_row", "argmax_column",
    }
    boolean_fields = set(TELEMETRY_FIELDS) | {"precondition_passed"}
    array_fields = {"psi_real", "psi_imag", "phi"}
    for name in integer_fields & set(record):
        if not _is_int(record[name]):
            raise ContractError(f"Evidence field {name} must be an integer, not Boolean")
    for name in boolean_fields & set(record):
        if not isinstance(record[name], bool):
            raise ContractError(f"Evidence field {name} must be a Boolean")
    numeric_fields = (
        set(record)
        - integer_fields
        - boolean_fields
        - array_fields
        - {"record_type"}
    )
    for name in numeric_fields:
        if not _is_finite_float(record[name]):
            raise ContractError(f"Evidence field {name} must be a finite binary64 number")
    if not _all_finite_json(record):
        raise ContractError("Evidence record contains an unsupported or non-finite value")
    index = record["record_index"]
    stencil_index = record["stencil_index"]
    if stencil_index not in (0, 1):
        raise ContractError("Evidence stencil index is outside the frozen map")
    if record_type == "prepared_state":
        expected_index = stencil_index
    elif record_type == "checkpoint_state":
        branch_index = record["branch_index"]
        checkpoint_index = record["checkpoint_index"]
        checkpoints = protocol["baseline"]["checkpoints"]
        if branch_index not in range(6) or checkpoint_index not in range(9):
            raise ContractError("Checkpoint evidence coordinate is outside the frozen map")
        if record["step"] != checkpoints[checkpoint_index]:
            raise ContractError("Checkpoint evidence step and checkpoint index disagree")
        expected_index = 2 + stencil_index * 54 + branch_index * 9 + checkpoint_index
    elif record_type in {"step_energy", "step_telemetry"}:
        branch_index = record["branch_index"]
        step = record["step"]
        if branch_index not in range(6) or not 1 <= step <= 10000:
            raise ContractError("Per-step evidence coordinate is outside the frozen map")
        start = 110 if record_type == "step_energy" else 120110
        expected_index = start + stencil_index * 60000 + branch_index * 10000 + step - 1
    elif record_type == "local_stage_receipt":
        expected_index = local_record_index(
            stencil_index,
            record["branch_index"],
            record["step"],
            record["stage_index"],
        )
    else:
        if record["branch_index"] != 5:
            raise ContractError("Global receipt must use the global-pool branch index")
        expected_index = global_record_index(
            stencil_index, record["step"], record["stage_index"]
        )
    if index != expected_index:
        raise ContractError("Evidence record index disagrees with its frozen coordinates")
    if record_type in {"prepared_state", "checkpoint_state"}:
        shape = tuple(schemas[record_type]["array_shape"])
        for name in ("psi_real", "psi_imag", "phi"):
            array = np.asarray(record[name])
            if (
                array.shape != shape
                or array.dtype.kind != "f"
                or not _all_nested_finite_floats(record[name])
                or not bool(np.all(np.isfinite(array)))
            ):
                raise ContractError(f"Evidence array {name} has wrong shape or non-finite values")


def write_jsonl_shard(
    path: Path,
    records: Iterable[Mapping[str, Any]],
    shard_spec: Mapping[str, Any],
    protocol: Mapping[str, Any],
) -> ShardIdentity:
    """Exclusively write and validate one canonical physical evidence shard."""
    expected_count = int(shard_spec["count"])
    expected_first = int(shard_spec["first_record_index"])
    expected_last = int(shard_spec["last_record_index"])
    maximum_bytes = int(protocol["retention"]["evidence_max_shard_bytes"])
    path.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    count = 0
    byte_count = 0
    first_seen: int | None = None
    last_seen: int | None = None
    with path.open("xb") as handle:
        for record in records:
            validate_evidence_record(record, protocol)
            index = record["record_index"]
            expected_index = expected_first + count
            if index != expected_index:
                raise ContractError("Evidence record indices are missing, duplicated, or reordered")
            encoded = canonical_json_bytes(record, final_lf=True)
            if b"\r" in encoded or encoded.startswith(b"\xef\xbb\xbf"):
                raise ContractError("Evidence line encoding is not canonical UTF-8/LF")
            if byte_count + len(encoded) > maximum_bytes:
                raise ContractError("Evidence shard exceeds the frozen byte cap")
            handle.write(encoded)
            digest.update(encoded)
            byte_count += len(encoded)
            first_seen = index if first_seen is None else first_seen
            last_seen = index
            count += 1
        handle.flush()
        os.fsync(handle.fileno())
    if count != expected_count or first_seen != expected_first or last_seen != expected_last:
        raise ContractError("Evidence shard count or range mismatch")
    read_sha256, read_git_blob, read_bytes, first_bytes, last_bytes = _stream_file_hashes(
        path, byte_count
    )
    if (
        read_bytes != byte_count
        or read_sha256 != digest.hexdigest()
        or last_bytes[-1:] != b"\n"
        or first_bytes == b"\xef\xbb\xbf"
    ):
        raise ContractError("Evidence shard final encoding check failed")
    return ShardIdentity(
        path=str(shard_spec["path"]),
        bytes=byte_count,
        sha256=digest.hexdigest(),
        git_blob=read_git_blob,
        record_count=count,
        first_record_index=expected_first,
        last_record_index=expected_last,
    )


def _read_spool(path: Path) -> Iterator[dict[str, Any]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        for line in handle:
            if not line.endswith("\n") or "\r" in line or not line.strip():
                raise ContractError("Receipt spool is not canonical line-delimited JSON")
            value = strict_json_loads(line)
            if not isinstance(value, dict):
                raise ContractError("Receipt spool line is not a JSON object")
            yield value


def _geometry(size: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int]:
    center = (size - 1) / 2.0
    row, column = np.indices((size, size), dtype=np.float64)
    radius = np.hypot(row - center, column - center)
    bins = np.floor(radius).astype(np.int64)
    return row, column, radius, bins, int(np.max(bins)) + 1


def _radial_profile(values: np.ndarray, bins: np.ndarray, count: int) -> np.ndarray:
    sums = np.bincount(bins.ravel(), weights=values.ravel(), minlength=count)
    populations = np.bincount(bins.ravel(), minlength=count)
    return sums / np.maximum(populations, 1)


def state_metrics(
    psi: np.ndarray,
    phi: np.ndarray,
    prepared_psi: np.ndarray,
    prepared_phi: np.ndarray,
) -> dict[str, Any]:
    size = psi.shape[0]
    row, column, radius, bins, bin_count = _geometry(size)
    energy = np.abs(psi) ** 2
    prepared_energy = np.abs(prepared_psi) ** 2
    total = float(np.sum(energy))
    prepared_total = float(np.sum(prepared_energy))
    if not math.isfinite(total) or total <= 0.0:
        raise TechnicalTrajectoryError("Checkpoint psi energy is non-positive or non-finite")
    prepared_profile = _radial_profile(prepared_energy, bins, bin_count)
    psi_profile = _radial_profile(energy, bins, bin_count)
    prepared_phi_profile = _radial_profile(prepared_phi, bins, bin_count)
    phi_profile = _radial_profile(phi, bins, bin_count)
    center = (size - 1) / 2.0
    centroid_row = float(np.sum(energy * row) / total)
    centroid_column = float(np.sum(energy * column) / total)
    prepared_centroid_row = float(np.sum(prepared_energy * row) / prepared_total)
    prepared_centroid_column = float(np.sum(prepared_energy * column) / prepared_total)
    order = np.argsort(radius.ravel())
    cumulative = np.cumsum(energy.ravel()[order])
    prepared_cumulative = np.cumsum(prepared_energy.ravel()[order])
    index = min(int(np.searchsorted(cumulative, 0.5 * total)), order.size - 1)
    prepared_index = min(
        int(np.searchsorted(prepared_cumulative, 0.5 * prepared_total)),
        order.size - 1,
    )
    half_radius = float(radius.ravel()[order[index]])
    prepared_half_radius = float(radius.ravel()[order[prepared_index]])
    return {
        "total_psi_energy": total,
        "psi_energy_relative_error": float(
            abs(total - prepared_total) / (abs(prepared_total) + 1e-30)
        ),
        "psi_radial_profile": psi_profile.tolist(),
        "psi_radial_profile_relative_l2_error": float(
            np.linalg.norm(psi_profile - prepared_profile)
            / (np.linalg.norm(prepared_profile) + 1e-30)
        ),
        "phi_radial_profile": phi_profile.tolist(),
        "phi_radial_profile_relative_l2_error": float(
            np.linalg.norm(phi_profile - prepared_phi_profile)
            / (np.linalg.norm(prepared_phi_profile) + 1e-30)
        ),
        "half_energy_radius": half_radius,
        "half_energy_radius_absolute_change": float(abs(half_radius - prepared_half_radius)),
        "centroid_row": centroid_row,
        "centroid_column": centroid_column,
        "fixed_center_displacement": float(math.hypot(centroid_row - center, centroid_column - center)),
        "centroid_shift_from_pre": float(
            math.hypot(
                centroid_row - prepared_centroid_row,
                centroid_column - prepared_centroid_column,
            )
        ),
        "energy_fraction_radius_3": float(np.sum(energy[radius <= 3.0]) / total),
        "energy_fraction_radius_6": float(np.sum(energy[radius <= 6.0]) / total),
        "energy_fraction_radius_10": float(np.sum(energy[radius <= 10.0]) / total),
        "phi_min": float(np.min(phi)),
        "phi_mean": float(np.mean(phi)),
        "phi_max": float(np.max(phi)),
        "phi_total": float(np.sum(phi)),
        "max_abs_psi": float(np.max(np.abs(psi))),
        "finite": bool(np.all(np.isfinite(psi)) and np.all(np.isfinite(phi))),
    }


def checkpoint_rows(results: Sequence[StencilResult], protocol: Mapping[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    checkpoints = [int(value) for value in protocol["baseline"]["checkpoints"]]
    for result in results:
        for branch_index in range(len(BRANCHES)):
            for checkpoint_index, step in enumerate(checkpoints):
                psi, phi = result.checkpoints[(branch_index, step)]
                rows.append(
                    {
                        "stencil_index": result.stencil_index,
                        "branch_index": branch_index,
                        "checkpoint_index": checkpoint_index,
                        "step": step,
                        **state_metrics(
                            psi,
                            phi,
                            result.prepared_psi,
                            result.prepared_phi,
                        ),
                    }
                )
    return rows


def _checkpoint_lookup(rows: Sequence[Mapping[str, Any]]) -> dict[tuple[int, int, int], Mapping[str, Any]]:
    return {
        (int(row["stencil_index"]), int(row["branch_index"]), int(row["step"])): row
        for row in rows
    }


def _absolute_checkpoint_pass(row: Mapping[str, Any], thresholds: Mapping[str, Any]) -> bool:
    return bool(
        row["finite"]
        and row["psi_energy_relative_error"] <= thresholds["psi_energy_relative_error_max"]
        and row["psi_radial_profile_relative_l2_error"]
        <= thresholds["psi_radial_profile_relative_l2_max"]
        and row["phi_radial_profile_relative_l2_error"]
        <= thresholds["phi_radial_profile_relative_l2_max"]
        and row["half_energy_radius_absolute_change"]
        <= thresholds["half_energy_radius_change_max_cells"]
        and row["fixed_center_displacement"]
        <= thresholds["center_displacement_from_fixed_grid_center_max_cells"]
        and row["energy_fraction_radius_6"]
        >= thresholds["energy_fraction_within_radius_6_min"]
    )


def absolute_clean_branch(
    rows: Sequence[Mapping[str, Any]],
    results: Sequence[StencilResult],
    protocol: Mapping[str, Any],
    branch_index: int,
) -> bool:
    thresholds = protocol["thresholds"]
    required_steps = set(int(value) for value in thresholds["absolute_clean_gate_checkpoints"])
    relevant = [row for row in rows if row["branch_index"] == branch_index and row["step"] in required_steps]
    checkpoints_pass = len(relevant) == len(STENCILS) * len(required_steps) and all(
        _absolute_checkpoint_pass(row, thresholds) for row in relevant
    )
    trajectory_pass = True
    for result in results:
        pre_total = float(np.sum(np.abs(result.prepared_psi) ** 2))
        ratios = result.energies[branch_index] / pre_total
        trajectory_pass = trajectory_pass and bool(
            np.all(ratios >= thresholds["whole_trajectory_psi_energy_lower_ratio"])
            and np.all(ratios <= thresholds["whole_trajectory_psi_energy_upper_ratio"])
        )
    return checkpoints_pass and trajectory_pass


def comparison_rows(rows: Sequence[Mapping[str, Any]], protocol: Mapping[str, Any]) -> list[dict[str, Any]]:
    lookup = _checkpoint_lookup(rows)
    thresholds = protocol["thresholds"]
    result: list[dict[str, Any]] = []

    def append(
        kind: str,
        stencil_index: int,
        step: int,
        metric: str,
        reference_branch: int,
        candidate_branch: int,
    ) -> None:
        reference = float(lookup[(stencil_index, reference_branch, step)][metric])
        candidate = float(lookup[(stencil_index, candidate_branch, step)][metric])
        tolerance = float(
            thresholds["comparison_absolute"]
            + thresholds["comparison_relative"] * max(abs(reference), abs(candidate))
        )
        improvement = reference - candidate
        result.append(
            {
                "comparison_index": len(result),
                "comparison_kind": kind,
                "stencil_index": stencil_index,
                "step": step,
                "metric": metric,
                "reference_branch_index": reference_branch,
                "candidate_branch_index": candidate_branch,
                "reference_value": reference,
                "candidate_value": candidate,
                "tolerance": tolerance,
                "improvement": improvement,
                "passed": bool(improvement > tolerance),
            }
        )

    for stencil_index in range(len(STENCILS)):
        for step in thresholds["comparison_horizons"]:
            for metric in (
                "psi_energy_relative_error",
                "psi_radial_profile_relative_l2_error",
            ):
                append("pair_both_vs_control", stencil_index, int(step), metric, 0, 4)
    for stencil_index in range(len(STENCILS)):
        for step in thresholds["comparison_horizons"]:
            append(
                "pair_both_vs_global_pool",
                stencil_index,
                int(step),
                "psi_radial_profile_relative_l2_error",
                5,
                4,
            )
    return result


def trajectory_energy_summaries(results: Sequence[StencilResult], protocol: Mapping[str, Any]) -> list[dict[str, Any]]:
    thresholds = protocol["thresholds"]
    rows: list[dict[str, Any]] = []
    for result in results:
        pre_total = float(np.sum(np.abs(result.prepared_psi) ** 2))
        for branch_index in range(len(BRANCHES)):
            values = result.energies[branch_index]
            ratios = values / pre_total
            lower = np.flatnonzero(ratios < thresholds["whole_trajectory_psi_energy_lower_ratio"])
            upper = np.flatnonzero(ratios > thresholds["whole_trajectory_psi_energy_upper_ratio"])
            rows.append(
                {
                    "stencil_index": result.stencil_index,
                    "branch_index": branch_index,
                    "record_count": int(values.size),
                    "pre_total_psi_energy": pre_total,
                    "minimum_total_psi_energy": float(np.min(values)),
                    "maximum_total_psi_energy": float(np.max(values)),
                    "minimum_energy_ratio": float(np.min(ratios)),
                    "maximum_energy_ratio": float(np.max(ratios)),
                    "first_lower_bound_violation_step": None if lower.size == 0 else int(lower[0] + 1),
                    "first_upper_bound_violation_step": None if upper.size == 0 else int(upper[0] + 1),
                }
            )
    return rows


def technical_telemetry_summaries(results: Sequence[StencilResult]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for result in results:
        for branch_index in range(len(BRANCHES)):
            values = result.telemetry[branch_index]
            rows.append(
                {
                    "stencil_index": result.stencil_index,
                    "branch_index": branch_index,
                    "record_count": int(values.shape[0]),
                    **{
                        f"{name}_count": int(np.count_nonzero(values[:, index]))
                        for index, name in enumerate(TELEMETRY_FIELDS)
                    },
                }
            )
    return rows


def receipt_only_equals_control(results: Sequence[StencilResult], rows: Sequence[Mapping[str, Any]]) -> bool:
    for result in results:
        if not np.array_equal(result.energies[0], result.energies[1]):
            return False
        if not np.array_equal(result.telemetry[0], result.telemetry[1]):
            return False
        for step in sorted(step for branch, step in result.checkpoints if branch == 0):
            control = result.checkpoints[(0, step)]
            receipt = result.checkpoints[(1, step)]
            if not np.array_equal(control[0], receipt[0]) or not np.array_equal(control[1], receipt[1]):
                return False
    lookup = _checkpoint_lookup(rows)
    scalar_fields = set(rows[0]) - {"stencil_index", "branch_index", "checkpoint_index"}
    for stencil_index in range(len(STENCILS)):
        for step in sorted({int(row["step"]) for row in rows}):
            a = lookup[(stencil_index, 0, step)]
            b = lookup[(stencil_index, 1, step)]
            if any(a[field] != b[field] for field in scalar_fields):
                return False
    return True


def classify_outcome(gates: Mapping[str, bool], comparisons: Sequence[Mapping[str, Any]]) -> str:
    technical_keys = (
        "identity", "runtime", "serialization", "starting_clones",
        "receipt_only_control", "proposal_fidelity", "technical_telemetry",
        "local_receipts", "global_receipts", "control_phenotype",
    )
    if not all(gates[key] for key in technical_keys):
        return "rwc1_technical_non_result"
    if gates["pair_both_absolute_clean"] and gates["pair_both_causal_improvement"]:
        if gates["local_advantage"]:
            return "rwc1_local_advantage_clean_gate_passed"
        return "rwc1_clean_gate_passed_locality_not_identified"
    if any(row["passed"] for row in comparisons[:8]):
        return "rwc1_mixed_or_partial_only"
    return "rwc1_unsupported_under_tested_conditions"


def receipt_gates(results: Sequence[StencilResult], protocol: Mapping[str, Any]) -> tuple[bool, bool]:
    multiplier = float(protocol["thresholds"]["local_and_global_aggregate_receipt_multiplier"])
    local_pass = True
    global_pass = True
    for result in results:
        for branch_index in LOCAL_STAGE_MAP:
            local_count = 0
            for record in _read_spool(result.local_spools[branch_index]):
                local_count += 1
                local_pass = local_pass and bool(
                    record["precondition_passed"]
                    and record["max_cellwise_normalized_residual_ratio"]
                    <= protocol["thresholds"]["local_cellwise_normalized_residual_ratio_max"]
                    and abs(record["aggregate_residual"])
                    <= multiplier * record["aggregate_scale"]
                )
            expected_count = 10000 * len(LOCAL_STAGE_MAP[branch_index])
            local_pass = local_pass and local_count == expected_count
        global_count = 0
        for record in _read_spool(result.global_spool):
            global_count += 1
            global_pass = global_pass and bool(
                record["precondition_passed"]
                and abs(record["aggregate_residual"])
                <= multiplier * record["aggregate_scale"]
            )
        global_pass = global_pass and global_count == 20000
    return local_pass, global_pass


def _prepared_records(results: Sequence[StencilResult]) -> Iterator[dict[str, Any]]:
    for result in results:
        yield {
            "record_index": result.stencil_index,
            "record_type": "prepared_state",
            "stencil_index": result.stencil_index,
            "psi_real": np.real(result.prepared_psi).tolist(),
            "psi_imag": np.imag(result.prepared_psi).tolist(),
            "phi": result.prepared_phi.tolist(),
        }


def _checkpoint_records(results: Sequence[StencilResult], protocol: Mapping[str, Any]) -> Iterator[dict[str, Any]]:
    checkpoints = [int(value) for value in protocol["baseline"]["checkpoints"]]
    for result in results:
        for branch_index in range(len(BRANCHES)):
            for checkpoint_index, step in enumerate(checkpoints):
                psi, phi = result.checkpoints[(branch_index, step)]
                yield {
                    "record_index": 2 + result.stencil_index * 54 + branch_index * 9 + checkpoint_index,
                    "record_type": "checkpoint_state",
                    "stencil_index": result.stencil_index,
                    "branch_index": branch_index,
                    "checkpoint_index": checkpoint_index,
                    "step": step,
                    "psi_real": np.real(psi).tolist(),
                    "psi_imag": np.imag(psi).tolist(),
                    "phi": phi.tolist(),
                }


def _step_energy_records(results: Sequence[StencilResult]) -> Iterator[dict[str, Any]]:
    for result in results:
        for branch_index in range(len(BRANCHES)):
            for step, value in enumerate(result.energies[branch_index], start=1):
                yield {
                    "record_index": 110 + result.stencil_index * 60000 + branch_index * 10000 + step - 1,
                    "record_type": "step_energy",
                    "stencil_index": result.stencil_index,
                    "branch_index": branch_index,
                    "step": step,
                    "total_psi_energy": float(value),
                }


def _step_telemetry_records(results: Sequence[StencilResult]) -> Iterator[dict[str, Any]]:
    for result in results:
        for branch_index in range(len(BRANCHES)):
            for step, values in enumerate(result.telemetry[branch_index], start=1):
                yield {
                    "record_index": 120110 + result.stencil_index * 60000 + branch_index * 10000 + step - 1,
                    "record_type": "step_telemetry",
                    "stencil_index": result.stencil_index,
                    "branch_index": branch_index,
                    "step": step,
                    **{
                        name: bool(values[index])
                        for index, name in enumerate(TELEMETRY_FIELDS)
                    },
                }


def _local_records(result: StencilResult) -> Iterator[dict[str, Any]]:
    for branch_index in LOCAL_STAGE_MAP:
        yield from _read_spool(result.local_spools[branch_index])


def stage_evidence_shards(
    staging_directory: Path,
    results: Sequence[StencilResult],
    protocol: Mapping[str, Any],
) -> tuple[list[Path], list[ShardIdentity]]:
    shard_specs = protocol["retention"]["evidence_shards"]
    iterators: list[Iterable[Mapping[str, Any]]] = [
        (*_prepared_records(results), *_checkpoint_records(results, protocol)),
        _step_energy_records(results),
        _step_telemetry_records(results),
        _local_records(results[0]),
        _local_records(results[1]),
        (record for result in results for record in _read_spool(result.global_spool)),
    ]
    paths: list[Path] = []
    identities: list[ShardIdentity] = []
    for index, (spec, records) in enumerate(zip(shard_specs, iterators, strict=True)):
        path = staging_directory / f"evidence-{index}.jsonl"
        identity = write_jsonl_shard(path, records, spec, protocol)
        paths.append(path)
        identities.append(identity)
    return paths, identities


def _starting_clones_equal(results: Sequence[StencilResult]) -> bool:
    for result in results:
        reference_psi, reference_phi = result.checkpoints[(0, 0)]
        for branch_index in range(1, len(BRANCHES)):
            psi, phi = result.checkpoints[(branch_index, 0)]
            if not np.array_equal(reference_psi, psi) or not np.array_equal(reference_phi, phi):
                return False
    return True


def _control_phenotype(rows: Sequence[Mapping[str, Any]], protocol: Mapping[str, Any]) -> bool:
    lookup = _checkpoint_lookup(rows)
    thresholds = protocol["thresholds"]
    return all(
        not _absolute_checkpoint_pass(lookup[(stencil_index, 0, 10000)], thresholds)
        for stencil_index in range(len(STENCILS))
    )


def build_primary_payload(
    protocol: Mapping[str, Any],
    protocol_identity: FileIdentity,
    preflight: Mapping[str, Any],
    results: Sequence[StencilResult],
    shard_identities: Sequence[ShardIdentity],
) -> dict[str, Any]:
    checkpoints = checkpoint_rows(results, protocol)
    comparisons = comparison_rows(checkpoints, protocol)
    local_receipts, global_receipts = receipt_gates(results, protocol)
    telemetry_rows = technical_telemetry_summaries(results)
    technical_pass = all(
        row[f"{name}_count"] == 0
        for row in telemetry_rows
        for name in TELEMETRY_FIELDS
    )
    pair_absolute = absolute_clean_branch(checkpoints, results, protocol, 4)
    global_absolute = absolute_clean_branch(checkpoints, results, protocol, 5)
    gates = {
        "identity": bool(preflight["passed"]),
        "runtime": bool(preflight["runtime_gate"]["passed"]),
        "serialization": True,
        "starting_clones": _starting_clones_equal(results),
        "receipt_only_control": receipt_only_equals_control(results, checkpoints),
        "proposal_fidelity": all(result.proposal_fidelity_passed for result in results),
        "technical_telemetry": technical_pass,
        "local_receipts": local_receipts,
        "global_receipts": global_receipts,
        "control_phenotype": _control_phenotype(checkpoints, protocol),
        "pair_both_absolute_clean": pair_absolute,
        "pair_both_causal_improvement": all(row["passed"] for row in comparisons[:8]),
        "local_advantage": all(row["passed"] for row in comparisons[8:]),
        "global_pool_absolute_clean": global_absolute,
    }
    outcome = classify_outcome(gates, comparisons)
    source_gate_fields = protocol["retention"]["primary_output_contract"][
        "source_identity_gate_fields"
    ]
    source_gate = {name: preflight[name] for name in source_gate_fields}
    payload: dict[str, Any] = {
        "schema": PRIMARY_SCHEMA,
        "protocol_identity": {
            **protocol_identity.as_dict(),
            "schema": protocol["schema"],
        },
        "source_identity_gate": source_gate,
        "runtime_gate": dict(preflight["runtime_gate"]),
        "execution_identity": {
            "attempt": 1,
            "trajectory_execution_count": 1,
            "stencil_count": 2,
            "branch_count": 6,
            "continuation_steps": int(protocol["baseline"]["continuation_steps"]),
        },
        "index_maps": dict(protocol["retention"]["evidence_index_maps"]),
        "checkpoint_metrics": checkpoints,
        "trajectory_energy_summaries": trajectory_energy_summaries(results, protocol),
        "technical_telemetry_summaries": telemetry_rows,
        "comparisons": comparisons,
        "gates": gates,
        "classification": {
            "outcome": outcome,
            "primary_claim_only": PRIMARY_CLAIM_ONLY,
        },
        "evidence_identity": {
            "shard_count": len(shard_identities),
            "total_record_count": sum(item.record_count for item in shard_identities),
            "shards": [item.primary_dict() for item in shard_identities],
        },
        "claim_boundary": dict(protocol["claim_boundary"]),
    }
    payload["canonical_payload_sha256_without_self"] = canonical_payload_sha256_without_self(payload)
    validate_primary_payload(payload, protocol)
    return payload


def validate_primary_payload(payload: Mapping[str, Any], protocol: Mapping[str, Any]) -> None:
    """Fail closed on every frozen primary schema, order, type, and hash surface."""
    contract = protocol["retention"]["primary_output_contract"]
    if set(payload) != set(contract["top_level_fields"]):
        raise ContractError("Primary top-level schema mismatch")
    exact_objects = {
        "protocol_identity": contract["protocol_identity_fields"],
        "source_identity_gate": contract["source_identity_gate_fields"],
        "runtime_gate": contract["runtime_gate_fields"],
        "execution_identity": contract["execution_identity_fields"],
        "evidence_identity": contract["evidence_identity_fields"],
        "classification": contract["classification_fields"],
        "gates": contract["gates_fields"],
        "claim_boundary": contract["claim_boundary_fields"],
    }
    for name, fields in exact_objects.items():
        value = payload.get(name)
        if not isinstance(value, dict) or set(value) != set(fields):
            raise ContractError(f"Primary {name} field set mismatch")
    if payload["schema"] != contract["primary_schema"]:
        raise ContractError("Primary schema label mismatch")
    if (
        payload["protocol_identity"]["path"] != PROTOCOL_RELATIVE_PATH
        or payload["protocol_identity"]["schema"] != protocol["schema"]
    ):
        raise ContractError("Primary protocol identity path or schema mismatch")
    if payload["classification"]["outcome"] not in protocol["outcome_map"]:
        raise ContractError("Primary outcome is outside the frozen map")
    if payload["classification"]["primary_claim_only"] is not True:
        raise ContractError("Primary claim-only boundary must be Boolean true")
    if payload["claim_boundary"] != protocol["claim_boundary"]:
        raise ContractError("Primary claim boundary differs from preregistration")
    index_maps = payload["index_maps"]
    expected_index_maps = protocol["retention"]["evidence_index_maps"]
    if not isinstance(index_maps, dict) or set(index_maps) != set(expected_index_maps):
        raise ContractError("Primary evidence index-map shape mismatch")
    if (
        not isinstance(index_maps["checkpoint_index"], list)
        or any(not _is_int(value) for value in index_maps["checkpoint_index"])
        or any(
            not isinstance(index_maps[name], list)
            or any(not isinstance(value, str) for value in index_maps[name])
            for name in ("branch_index", "stage_index", "stencil_index")
        )
    ):
        raise ContractError("Primary evidence index-map types mismatch")
    if index_maps != expected_index_maps:
        raise ContractError("Primary evidence index maps differ from preregistration")
    for name in contract["gates_fields"]:
        if not isinstance(payload["gates"][name], bool):
            raise ContractError("Primary gate values must be Booleans")
    if any(not isinstance(payload["claim_boundary"][name], bool) for name in contract["claim_boundary_fields"]):
        raise ContractError("Primary claim boundary values must be Booleans")
    runtime_gate = payload["runtime_gate"]
    if not isinstance(runtime_gate["passed"], bool) or any(
        not isinstance(runtime_gate[name], str) for name in ("backend", "python", "numpy")
    ):
        raise ContractError("Primary runtime gate types mismatch")
    execution = payload["execution_identity"]
    if any(not _is_int(execution[name]) for name in contract["execution_identity_fields"]):
        raise ContractError("Primary execution identity values must be integers")
    if (
        execution["attempt"] != 1
        or execution["trajectory_execution_count"] != 1
        or execution["stencil_count"] != 2
        or execution["branch_count"] != 6
        or execution["continuation_steps"] != 10000
    ):
        raise ContractError("Primary execution identity values mismatch")
    protocol_identity = payload["protocol_identity"]
    if (
        not _is_int(protocol_identity["bytes"])
        or protocol_identity["bytes"] != PROTOCOL_EXPECTED_BYTES
        or protocol_identity["sha256"] != PROTOCOL_EXPECTED_SHA256
        or protocol_identity["git_blob"] != PROTOCOL_EXPECTED_GIT_BLOB
    ):
        raise ContractError("Primary protocol identity differs from the immutable v3 checkpoint")
    _validate_hex(protocol_identity["sha256"], 64, "primary protocol SHA-256")
    _validate_hex(protocol_identity["git_blob"], 40, "primary protocol Git blob")
    source_gate = payload["source_identity_gate"]
    for name in ("passed", "head_equals_remote_readback_commit", "worktree_clean"):
        if not isinstance(source_gate[name], bool):
            raise ContractError("Primary source identity flags must be Booleans")
    source_hash_fields = (
        "expected_execution_commit", "actual_head_commit", "remote_readback_commit",
        "expected_runner_git_blob", "actual_runner_filtered_git_blob", "actual_runner_head_git_blob",
        "expected_runner_test_git_blob", "actual_runner_test_filtered_git_blob", "actual_runner_test_head_git_blob",
        "expected_report_git_blob", "actual_report_filtered_git_blob", "actual_report_head_git_blob",
        "expected_manifest_git_blob", "actual_manifest_filtered_git_blob", "actual_manifest_head_git_blob",
    )
    for name in source_hash_fields:
        _validate_hex(source_gate[name], 40, f"primary source identity {name}")
    for name in ("expected", "actual"):
        value = source_gate[name]
        if not isinstance(value, dict) or set(value) != {
            "core_math_git_blob", "localized_reference_runner_git_blob",
            "requirements_git_blob", "requirements_dev_git_blob",
        }:
            raise ContractError("Primary frozen source binding fields mismatch")
        for key, blob in value.items():
            _validate_hex(blob, 40, f"primary source binding {name}.{key}")
    expected_source_bindings = {
        "core_math_git_blob": protocol["source_bindings"]["core_math_git_blob"],
        "localized_reference_runner_git_blob": protocol["source_bindings"][
            "localized_reference_runner_git_blob"
        ],
        "requirements_git_blob": protocol["source_bindings"]["requirements_git_blob"],
        "requirements_dev_git_blob": protocol["source_bindings"][
            "requirements_dev_git_blob"
        ],
    }
    if source_gate["expected"] != expected_source_bindings:
        raise ContractError("Primary expected source bindings differ from preregistration")
    head_equals_remote = (
        source_gate["actual_head_commit"] == source_gate["remote_readback_commit"]
    )
    if source_gate["head_equals_remote_readback_commit"] is not head_equals_remote:
        raise ContractError("Primary remote-readback comparison flag is incoherent")
    identity_conjunction = bool(
        source_gate["worktree_clean"]
        and head_equals_remote
        and source_gate["expected_execution_commit"] == source_gate["actual_head_commit"]
        and source_gate["expected_runner_git_blob"]
        == source_gate["actual_runner_filtered_git_blob"]
        == source_gate["actual_runner_head_git_blob"]
        and source_gate["expected_runner_test_git_blob"]
        == source_gate["actual_runner_test_filtered_git_blob"]
        == source_gate["actual_runner_test_head_git_blob"]
        and source_gate["expected_report_git_blob"]
        == source_gate["actual_report_filtered_git_blob"]
        == source_gate["actual_report_head_git_blob"]
        and source_gate["expected_manifest_git_blob"]
        == source_gate["actual_manifest_filtered_git_blob"]
        == source_gate["actual_manifest_head_git_blob"]
        and source_gate["expected"] == source_gate["actual"]
    )
    if source_gate["passed"] is not identity_conjunction:
        raise ContractError("Primary source identity passed flag is incoherent")
    runtime_conjunction = bool(
        runtime_gate["backend"] == protocol["runtime"]["backend"]
        and runtime_gate["python"] == protocol["runtime"]["python"]
        and runtime_gate["numpy"] == protocol["runtime"]["numpy"]
    )
    if runtime_gate["passed"] is not runtime_conjunction:
        raise ContractError("Primary runtime passed flag is incoherent")
    if payload["gates"]["identity"] is not source_gate["passed"]:
        raise ContractError("Primary identity gate disagrees with source identity")
    if payload["gates"]["runtime"] is not runtime_gate["passed"]:
        raise ContractError("Primary runtime gate disagrees with runtime identity")

    list_contracts = (
        ("checkpoint_metrics", contract["checkpoint_metric_count"], contract["checkpoint_metric_fields"]),
        ("trajectory_energy_summaries", contract["trajectory_energy_summary_count"], contract["trajectory_energy_summary_fields"]),
        ("technical_telemetry_summaries", contract["technical_telemetry_summary_count"], contract["technical_telemetry_summary_fields"]),
        ("comparisons", contract["comparison_count"], contract["comparison_fields"]),
    )
    for name, count, fields in list_contracts:
        rows = payload.get(name)
        if not isinstance(rows, list) or len(rows) != count:
            raise ContractError(f"Primary {name} count mismatch")
        if any(not isinstance(row, dict) or set(row) != set(fields) for row in rows):
            raise ContractError(f"Primary {name} row field mismatch")

    checkpoint_integer_fields = {"stencil_index", "branch_index", "checkpoint_index", "step"}
    checkpoint_boolean_fields = {"finite"}
    checkpoint_profile_fields = {"psi_radial_profile", "phi_radial_profile"}
    for row in payload["checkpoint_metrics"]:
        if any(not _is_int(row[name]) for name in checkpoint_integer_fields):
            raise ContractError("Primary checkpoint indices must be integers")
        if any(not isinstance(row[name], bool) for name in checkpoint_boolean_fields):
            raise ContractError("Primary checkpoint flags must be Booleans")
        for name in checkpoint_profile_fields:
            if not isinstance(row[name], list) or any(not _is_finite_float(value) for value in row[name]):
                raise ContractError("Primary checkpoint profiles must contain finite binary64 values")
        for name in set(contract["checkpoint_metric_fields"]) - checkpoint_integer_fields - checkpoint_boolean_fields - checkpoint_profile_fields:
            if not _is_finite_float(row[name]):
                raise ContractError("Primary checkpoint scalar must be a finite binary64 value")

    for row in payload["trajectory_energy_summaries"]:
        if any(not _is_int(row[name]) for name in ("stencil_index", "branch_index", "record_count")):
            raise ContractError("Primary trajectory summary counts must be integers")
        for name in (
            "pre_total_psi_energy", "minimum_total_psi_energy", "maximum_total_psi_energy",
            "minimum_energy_ratio", "maximum_energy_ratio",
        ):
            if not _is_finite_float(row[name]):
                raise ContractError("Primary trajectory summary scalar must be finite binary64")
        for name in ("first_lower_bound_violation_step", "first_upper_bound_violation_step"):
            if row[name] is not None and not _is_int(row[name]):
                raise ContractError("Primary violation steps must be integer or null")
    for row in payload["technical_telemetry_summaries"]:
        if any(not _is_int(value) for value in row.values()):
            raise ContractError("Primary technical telemetry summaries must be integer counts")
        if row["record_count"] != 10000 or any(
            row[f"{name}_count"] < 0 for name in TELEMETRY_FIELDS
        ):
            raise ContractError("Primary technical telemetry count value mismatch")
    for row in payload["comparisons"]:
        if any(
            not _is_int(row[name])
            for name in (
                "comparison_index", "stencil_index", "step",
                "reference_branch_index", "candidate_branch_index",
            )
        ):
            raise ContractError("Primary comparison indices must be integers")
        if not isinstance(row["passed"], bool):
            raise ContractError("Primary comparison passed must be Boolean")
        if any(not isinstance(row[name], str) for name in ("comparison_kind", "metric")):
            raise ContractError("Primary comparison labels must be strings")
        if any(
            not _is_finite_float(row[name])
            for name in ("reference_value", "candidate_value", "tolerance", "improvement")
        ):
            raise ContractError("Primary comparison values must be finite numbers")

    checkpoints = payload["checkpoint_metrics"]
    expected_checkpoint_coordinates = [
        (stencil, branch, checkpoint, int(step))
        for stencil in range(2)
        for branch in range(6)
        for checkpoint, step in enumerate(protocol["baseline"]["checkpoints"])
    ]
    actual_checkpoint_coordinates = [
        (row["stencil_index"], row["branch_index"], row["checkpoint_index"], row["step"])
        for row in checkpoints
    ]
    if actual_checkpoint_coordinates != expected_checkpoint_coordinates:
        raise ContractError("Primary checkpoint row order mismatch")
    if any(len(row["psi_radial_profile"]) != contract["checkpoint_profile_length"] for row in checkpoints):
        raise ContractError("Primary psi profile length mismatch")
    if any(len(row["phi_radial_profile"]) != contract["checkpoint_profile_length"] for row in checkpoints):
        raise ContractError("Primary phi profile length mismatch")

    expected_summary_coordinates = [(stencil, branch) for stencil in range(2) for branch in range(6)]
    for name in ("trajectory_energy_summaries", "technical_telemetry_summaries"):
        actual = [(row["stencil_index"], row["branch_index"]) for row in payload[name]]
        if actual != expected_summary_coordinates:
            raise ContractError(f"Primary {name} row order mismatch")
    if [row["comparison_index"] for row in payload["comparisons"]] != list(range(12)):
        raise ContractError("Primary comparison indices are not contiguous")
    expected_comparisons: list[tuple[str, int, int, str, int, int]] = []
    for stencil_index in range(2):
        for step in protocol["thresholds"]["comparison_horizons"]:
            for metric in (
                "psi_energy_relative_error",
                "psi_radial_profile_relative_l2_error",
            ):
                expected_comparisons.append(
                    ("pair_both_vs_control", stencil_index, int(step), metric, 0, 4)
                )
    for stencil_index in range(2):
        for step in protocol["thresholds"]["comparison_horizons"]:
            expected_comparisons.append(
                (
                    "pair_both_vs_global_pool",
                    stencil_index,
                    int(step),
                    "psi_radial_profile_relative_l2_error",
                    5,
                    4,
                )
            )
    actual_comparisons = [
        (
            row["comparison_kind"], row["stencil_index"], row["step"], row["metric"],
            row["reference_branch_index"], row["candidate_branch_index"],
        )
        for row in payload["comparisons"]
    ]
    if actual_comparisons != expected_comparisons:
        raise ContractError("Primary comparison row order mismatch")
    for row in payload["comparisons"]:
        expected_tolerance = (
            protocol["thresholds"]["comparison_absolute"]
            + protocol["thresholds"]["comparison_relative"]
            * max(abs(row["reference_value"]), abs(row["candidate_value"]))
        )
        expected_improvement = row["reference_value"] - row["candidate_value"]
        if (
            row["tolerance"] != expected_tolerance
            or row["improvement"] != expected_improvement
            or row["passed"] is not (expected_improvement > expected_tolerance)
        ):
            raise ContractError("Primary comparison arithmetic mismatch")

    evidence = payload["evidence_identity"]
    if evidence["shard_count"] != 6 or evidence["total_record_count"] != 400110:
        raise ContractError("Primary evidence identity total mismatch")
    shards = evidence["shards"]
    if not isinstance(shards, list) or len(shards) != 6:
        raise ContractError("Primary evidence shard identity count mismatch")
    for actual, expected in zip(shards, protocol["retention"]["evidence_shards"], strict=True):
        if set(actual) != set(contract["evidence_shard_identity_fields"]):
            raise ContractError("Primary evidence shard identity fields mismatch")
        if (
            actual["path"] != expected["path"]
            or not _is_int(actual["record_count"])
            or not _is_int(actual["first_record_index"])
            or not _is_int(actual["last_record_index"])
            or actual["record_count"] != expected["count"]
            or actual["first_record_index"] != expected["first_record_index"]
            or actual["last_record_index"] != expected["last_record_index"]
            or not _is_int(actual["bytes"])
            or actual["bytes"] <= 0
        ):
            raise ContractError("Primary evidence shard identity value mismatch")
        _validate_hex(actual["sha256"], 64, "evidence shard SHA-256")

    if payload["classification"]["outcome"] != classify_outcome(
        payload["gates"], payload["comparisons"]
    ):
        raise ContractError("Primary classification disagrees with the frozen outcome map")

    allowed_null_locations = {
        ("trajectory_energy_summaries", index, field)
        for index in range(12)
        for field in ("first_lower_bound_violation_step", "first_upper_bound_violation_step")
    }

    def validate_value(value: Any, path: tuple[Any, ...]) -> None:
        if value is None:
            if path not in allowed_null_locations:
                raise ContractError("Primary null appears outside the frozen violation-step fields")
            return
        if isinstance(value, dict):
            for key, item in value.items():
                validate_value(item, (*path, key))
            return
        if isinstance(value, list):
            for index, item in enumerate(value):
                validate_value(item, (*path, index))
            return
        if isinstance(value, (float, np.floating)) and not math.isfinite(float(value)):
            raise ContractError("Primary contains a non-finite value")
        if not isinstance(value, (str, int, float, bool, np.integer, np.floating, np.bool_)):
            raise ContractError("Primary contains an unsupported value type")

    validate_value(payload, ())
    claimed_hash = payload["canonical_payload_sha256_without_self"]
    _validate_hex(claimed_hash, 64, "primary canonical payload SHA-256")
    if claimed_hash != canonical_payload_sha256_without_self(payload):
        raise ContractError("Primary canonical payload hash mismatch")
    canonical_json_bytes(payload, final_lf=True)


def stage_primary(path: Path, payload: Mapping[str, Any]) -> FileIdentity:
    data = canonical_json_bytes(payload, final_lf=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    if path.read_bytes() != data:
        raise ContractError("Staged primary failed canonical read-back")
    return FileIdentity(
        path="",
        bytes=len(data),
        sha256=hashlib.sha256(data).hexdigest(),
        git_blob=_git_blob_bytes(data),
    )


def _copy_exclusive(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with source.open("rb") as input_handle, destination.open("xb") as output_handle:
        shutil.copyfileobj(input_handle, output_handle, length=1024 * 1024)
        output_handle.flush()
        os.fsync(output_handle.fileno())


def _copy_primary_to_hidden_temp(source: Path, destination: Path) -> Path:
    """Durably copy a marker beside its final path without publishing it."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=destination.parent,
        prefix=f".{destination.name}.",
        suffix=".tmp",
    )
    temporary_path = Path(temporary_name)
    try:
        with source.open("rb") as input_handle, os.fdopen(
            descriptor, "wb", closefd=True
        ) as output_handle:
            shutil.copyfileobj(input_handle, output_handle, length=1024 * 1024)
            output_handle.flush()
            os.fsync(output_handle.fileno())
        return temporary_path
    except BaseException:
        try:
            os.close(descriptor)
        except OSError:
            pass
        temporary_path.unlink(missing_ok=True)
        raise


def publish_staged_artifacts(
    root: Path,
    protocol: Mapping[str, Any],
    staged_shards: Sequence[Path],
    shard_identities: Sequence[ShardIdentity],
    staged_primary: Path,
    primary_identity: FileIdentity,
    *,
    before_copy: Callable[[int, Path, Path], None] | None = None,
) -> None:
    """Publish all six shards in order and the primary completion marker last."""
    destinations = [
        repository_path(root, relative_path)
        for relative_path in protocol["planned_paths"]["primary_evidence_shards"]
    ]
    primary_destination = repository_path(root, protocol["planned_paths"]["primary_output"])
    if (
        len(staged_shards) != 6
        or len(shard_identities) != 6
        or any(path.exists() for path in [*destinations, primary_destination])
    ):
        raise ContractError("Final primary or exact six-shard destination set is not absent")
    for index, (source, expected, destination) in enumerate(
        zip(staged_shards, shard_identities, destinations, strict=True)
    ):
        staged_sha, staged_blob, staged_bytes, _, _ = _stream_file_hashes(
            source, expected.bytes
        )
        if (
            staged_bytes != expected.bytes
            or staged_sha != expected.sha256
            or staged_blob != expected.git_blob
        ):
            raise ContractError("Staged evidence identity changed before publication")
        if before_copy is not None:
            before_copy(index, source, destination)
        _copy_exclusive(source, destination)
        final_sha, final_blob, final_bytes, _, _ = _stream_file_hashes(
            destination, expected.bytes
        )
        if (
            final_bytes != expected.bytes
            or final_sha != expected.sha256
            or final_blob != expected.git_blob
        ):
            raise ContractError("Published evidence shard failed streamed identity read-back")
    staged_primary_actual = file_identity(staged_primary.parent, staged_primary.name)
    if (
        staged_primary_actual.bytes != primary_identity.bytes
        or staged_primary_actual.sha256 != primary_identity.sha256
        or staged_primary_actual.git_blob != primary_identity.git_blob
    ):
        raise ContractError("Staged primary identity changed before publication")
    if before_copy is not None:
        before_copy(6, staged_primary, primary_destination)
    hidden_primary: Path | None = None
    published_by_this_call = False
    try:
        hidden_primary = _copy_primary_to_hidden_temp(
            staged_primary, primary_destination
        )
        hidden_identity = file_identity(hidden_primary.parent, hidden_primary.name)
        if (
            hidden_identity.bytes != primary_identity.bytes
            or hidden_identity.sha256 != primary_identity.sha256
            or hidden_identity.git_blob != primary_identity.git_blob
        ):
            raise ContractError(
                "Hidden primary completion marker failed identity read-back"
            )
        if primary_destination.exists():
            raise ContractError(
                "Primary completion marker appeared before exclusive publication"
            )
        try:
            os.link(hidden_primary, primary_destination)
        except FileExistsError as exc:
            raise ContractError(
                "Primary completion marker lost its exclusive publication race"
            ) from exc
        published_by_this_call = True
        hidden_primary.unlink()
        hidden_primary = None
        final_primary = file_identity(
            root, protocol["planned_paths"]["primary_output"]
        )
        if (
            final_primary.bytes != primary_identity.bytes
            or final_primary.sha256 != primary_identity.sha256
            or final_primary.git_blob != primary_identity.git_blob
        ):
            primary_destination.unlink(missing_ok=True)
            published_by_this_call = False
            raise ContractError(
                "Published primary completion marker failed identity read-back"
            )
    finally:
        if hidden_primary is not None:
            hidden_primary.unlink(missing_ok=True)
        if published_by_this_call and not primary_destination.exists():
            raise ContractError("Published primary completion marker disappeared")


def _terminal_failure(exc: BaseException, phase: str) -> dict[str, str]:
    return {
        "phase": phase,
        "code": exc.__class__.__name__,
        "sanitized_message": f"technical_failure_during_{phase}",
    }


def execute_primary_once(
    root: Path,
    expectations: PreflightExpectations,
) -> dict[str, Any]:
    """Perform the dry preflight, consume the latch, recheck, and run once."""
    started = time.perf_counter()
    _reset_stderr_identity()
    protocol = load_json_object(repository_path(root, PROTOCOL_RELATIVE_PATH))
    manifest = load_json_object(repository_path(root, MANIFEST_RELATIVE_PATH))
    protocol_identity = validate_protocol_identity(root, protocol, manifest)

    dry_preflight = verify_primary_preflight(
        root,
        protocol,
        manifest,
        expectations,
        require_clean=True,
        allow_existing_receipt=False,
    )
    if not dry_preflight["passed"]:
        raise ContractError("Dry clean/read-back primary preflight failed")
    receipt_path = create_primary_latch(
        root, protocol, protocol_identity, dry_preflight
    )
    phase = "consumed_preflight"
    try:
        consumed_protocol = load_json_object(
            repository_path(root, PROTOCOL_RELATIVE_PATH)
        )
        consumed_manifest = load_json_object(
            repository_path(root, MANIFEST_RELATIVE_PATH)
        )
        consumed_protocol_identity = validate_protocol_identity(
            root, consumed_protocol, consumed_manifest
        )
        if consumed_protocol_identity != protocol_identity:
            raise ContractError("Consumed protocol identity differs from dry preflight")
        protocol = consumed_protocol
        manifest = consumed_manifest
        consumed_preflight = verify_primary_preflight(
            root,
            protocol,
            manifest,
            expectations,
            require_clean=True,
            allow_existing_receipt=True,
        )
        if not consumed_preflight["passed"]:
            raise ContractError("Consumed identity/runtime/output-absence preflight failed")

        phase = "trajectory"
        reference = _load_reference_runner(root)
        evidence_parent = repository_path(
            root, protocol["planned_paths"]["primary_evidence_shards"][0]
        ).parent
        evidence_parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=".q2-m2-rwc1-", dir=evidence_parent) as temporary:
            staging_directory = Path(temporary)
            spool_directory = staging_directory / "spool"
            spool_directory.mkdir()

            def scientific_runner(stencil: str, stencil_index: int) -> StencilResult:
                return simulate_stencil(
                    stencil,
                    stencil_index,
                    protocol,
                    reference,
                    spool_directory,
                )

            results = orchestrate_stencils(protocol, scientific_runner)
            phase = "evidence_staging"
            staged_shards, shard_identities = stage_evidence_shards(
                staging_directory, results, protocol
            )
            payload = build_primary_payload(
                protocol,
                protocol_identity,
                consumed_preflight,
                results,
                shard_identities,
            )
            staged_primary = staging_directory / "primary.json"
            primary_raw_identity = stage_primary(staged_primary, payload)
            primary_identity = FileIdentity(
                path=protocol["planned_paths"]["primary_output"],
                bytes=primary_raw_identity.bytes,
                sha256=primary_raw_identity.sha256,
                git_blob=primary_raw_identity.git_blob,
            )
            phase = "publication"
            publish_staged_artifacts(
                root,
                protocol,
                staged_shards,
                shard_identities,
                staged_primary,
                primary_identity,
            )

        elapsed = time.perf_counter() - started
        output_identity = {
            "primary": primary_identity.as_dict(),
            "shards": [item.receipt_dict() for item in shard_identities],
        }
        update_primary_receipt(
            receipt_path,
            status="complete_output_retained",
            elapsed_seconds=elapsed,
            output_identity=output_identity,
            stderr_identity=_stderr_identity("primary_completed_without_raw_stderr_retention"),
            failure=None,
        )
        return {
            "status": "complete_output_retained",
            "outcome": payload["classification"]["outcome"],
            "primary": primary_identity.as_dict(),
            "shards": [item.receipt_dict() for item in shard_identities],
            "receipt": protocol["planned_paths"]["primary_execution_receipt"],
        }
    except BaseException as exc:
        elapsed = time.perf_counter() - started
        update_primary_receipt(
            receipt_path,
            status="technical_non_result",
            elapsed_seconds=elapsed,
            output_identity=None,
            stderr_identity=None,
            failure=_terminal_failure(exc, phase),
        )
        raise


def _expectations_from_args(args: argparse.Namespace) -> PreflightExpectations:
    values = {
        "execution_commit": args.expected_execution_commit,
        "remote_readback_commit": args.remote_readback_commit,
        "runner_git_blob": args.expected_runner_git_blob,
        "runner_test_git_blob": args.expected_runner_test_git_blob,
        "report_git_blob": args.expected_report_git_blob,
        "manifest_git_blob": args.expected_manifest_git_blob,
    }
    for name, value in values.items():
        _validate_hex(value, 40, name)
    return PreflightExpectations(**values)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Execute the frozen Q2-M2-RWC1 primary once after exact clean "
            "source, runtime, remote-readback, and output-absence gates."
        )
    )
    parser.add_argument("--expected-execution-commit", required=True)
    parser.add_argument("--remote-readback-commit", required=True)
    parser.add_argument("--expected-runner-git-blob", required=True)
    parser.add_argument("--expected-runner-test-git-blob", required=True)
    parser.add_argument("--expected-report-git-blob", required=True)
    parser.add_argument("--expected-manifest-git-blob", required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = execute_primary_once(REPOSITORY_ROOT, _expectations_from_args(args))
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
