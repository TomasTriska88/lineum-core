"""Independently check retained Q2-M2-RWC1 evidence without rerunning it.

The checker is intentionally isolated from the primary implementation.  It reads
only the frozen preregistration and the public retained schemas, consumes its
one-shot authority before opening retained primary evidence, and derives every
reported decision from retained primitives.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, BinaryIO, Iterable, Iterator, Mapping, NoReturn, Sequence

import numpy as np


PROTOCOL_PATH = "research/lineum-public-tolog-b4/q2-m2-rwc1-preregistration.json"
PRIMARY_PATH = "research/lineum-public-tolog-b4/q2-m2-rwc1-local-reciprocal-work.json"
CHECKER_PATH = "research/runners/lineum_b4_q2_m2_rwc1_local_reciprocal_work_checker.py"
CHECKER_TEST_PATH = "tests/research/test_lineum_b4_q2_m2_rwc1_local_reciprocal_work_checker.py"
REPORT_PATH = "research/lineum-public-tolog-galactic-shape-b4.md"
MANIFEST_PATH = "research/lineum-public-tolog-b4/artifact-manifest.json"
CHECKER_RECEIPT_PATH = (
    "research/lineum-public-tolog-b4/q2-m2-rwc1-checker-execution-attempt-1.json"
)
CHECKER_OUTPUT_PATH = "research/lineum-public-tolog-b4/q2-m2-rwc1-independent-check.json"

FROZEN_PROTOCOL_SCHEMA = "lineum.q2-m2-rwc1-preregistration.v3"
FROZEN_PROTOCOL_BYTES = 37448
FROZEN_PROTOCOL_SHA256 = "55917a01e0ab5a04e97515010c70359494769239c5c420ddc4513352a30486fd"
FROZEN_PROTOCOL_GIT_BLOB = "b6aea98ea752460f5283a40e7e68dea05a9c564a"
FROZEN_PROTOCOL_REMOTE_COMMIT = "9b340097dd4d2aa8cc1c661e40e60811120ca22b"
FROZEN_PRIMARY_RESULT_COMMIT = "7db2b781260e70b214cb9a2bb8b52cfd34f5f602"
FROZEN_REMOTE_REF = "refs/remotes/origin/codex/q2-m30-endogenous-balance-20260830"

CHECKER_SCHEMA = "lineum.q2-m2-rwc1-independent-check.v1"
RECEIPT_SCHEMA = "lineum.q2-m2-rwc1-execution-receipt.v1"
PRIMARY_SCHEMA = "lineum.q2-m2-rwc1-primary.v1"
MANIFEST_SCHEMA = "lineum-public-tolog-b4-readable-artifacts/4"

LOWERCASE_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
LOWERCASE_GIT_BLOB = re.compile(r"[0-9a-f]{40}\Z")
LOWERCASE_COMMIT = re.compile(r"[0-9a-f]{40}\Z")


class CheckerError(RuntimeError):
    """Raised when an independent check cannot safely produce a complete output."""


class ContractError(CheckerError):
    """Raised when retained input violates the frozen public contract."""


@dataclass(frozen=True)
class FileIdentity:
    """Content identity for one retained file."""

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
class ShardIdentity(FileIdentity):
    """Content and index identity for one retained JSONL shard."""

    record_count: int
    first_record_index: int
    last_record_index: int

    def as_dict(self) -> dict[str, Any]:
        result = super().as_dict()
        result.update(
            {
                "record_count": self.record_count,
                "first_record_index": self.first_record_index,
                "last_record_index": self.last_record_index,
            }
        )
        return result


@dataclass(frozen=True)
class ProgramGate:
    """Clean-checkpoint facts established without opening retained evidence."""

    expected_execution_commit: str
    actual_head_commit: str
    remote_readback_commit: str
    head_equals_remote_readback_commit: bool
    worktree_clean: bool
    expected_checker_git_blob: str
    actual_checker_filtered_git_blob: str
    actual_checker_head_git_blob: str
    expected_checker_test_git_blob: str
    actual_checker_test_filtered_git_blob: str
    actual_checker_test_head_git_blob: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "expected_execution_commit": self.expected_execution_commit,
            "actual_head_commit": self.actual_head_commit,
            "remote_readback_commit": self.remote_readback_commit,
            "head_equals_remote_readback_commit": self.head_equals_remote_readback_commit,
            "worktree_clean": self.worktree_clean,
            "path": CHECKER_PATH,
            "expected_git_blob": self.expected_checker_git_blob,
            "actual_filtered_git_blob": self.actual_checker_filtered_git_blob,
            "actual_head_git_blob": self.actual_checker_head_git_blob,
            "test_path": CHECKER_TEST_PATH,
            "expected_test_git_blob": self.expected_checker_test_git_blob,
            "actual_test_filtered_git_blob": self.actual_checker_test_filtered_git_blob,
            "actual_test_head_git_blob": self.actual_checker_test_head_git_blob,
        }


@dataclass(frozen=True)
class InvocationBindings:
    """Identity-only inputs frozen by the checker checkpoint."""

    execution_commit: str
    remote_readback_commit: str
    checker_git_blob: str
    checker_test_git_blob: str
    report_git_blob: str
    manifest_git_blob: str
    primary: FileIdentity
    shards: tuple[ShardIdentity, ...]


@dataclass
class Audit:
    """Count independently observed disagreements without retaining raw evidence."""

    mismatch_count: int = 0
    checkpoint_metrics_match: bool = True
    trajectory_energy_summaries_match: bool = True
    technical_gate_conditionally_applied: bool = True
    aggregate_receipt_arithmetic_passed: bool = True
    retained_witness_arithmetic_passed: bool = True
    comparison_rows_match: bool = True
    gate_map_match: bool = True

    def mismatch(self, category: str) -> None:
        self.mismatch_count += 1
        if category == "checkpoint":
            self.checkpoint_metrics_match = False
        elif category == "energy":
            self.trajectory_energy_summaries_match = False
        elif category == "technical":
            self.technical_gate_conditionally_applied = False
        elif category == "aggregate_receipt":
            self.aggregate_receipt_arithmetic_passed = False
        elif category == "witness":
            self.retained_witness_arithmetic_passed = False
        elif category == "comparison":
            self.comparison_rows_match = False
        elif category == "gate":
            self.gate_map_match = False
        else:
            raise AssertionError(f"unknown audit category: {category}")


@dataclass
class EnergyAccumulator:
    """Bounded state for one per-step energy envelope."""

    pre_total: float
    count: int = 0
    minimum: float = math.inf
    maximum: float = -math.inf
    first_lower: int | None = None
    first_upper: int | None = None

    def add(self, step: int, value: float, lower_ratio: float, upper_ratio: float) -> None:
        self.count += 1
        self.minimum = min(self.minimum, value)
        self.maximum = max(self.maximum, value)
        ratio = value / self.pre_total
        if self.first_lower is None and ratio < lower_ratio:
            self.first_lower = step
        if self.first_upper is None and ratio > upper_ratio:
            self.first_upper = step


@dataclass
class TelemetryAccumulator:
    """Bounded event counts for one stencil and branch."""

    record_count: int = 0
    psi_cap_contact_count: int = 0
    phi_cap_contact_count: int = 0
    destructive_reset_count: int = 0
    nonfinite_detected_count: int = 0
    negative_phi_input_detected_count: int = 0
    undeclared_source_detected_count: int = 0

    def add(self, record: Mapping[str, Any]) -> None:
        self.record_count += 1
        for field_name in (
            "psi_cap_contact",
            "phi_cap_contact",
            "destructive_reset",
            "nonfinite_detected",
            "negative_phi_input_detected",
            "undeclared_source_detected",
        ):
            if record[field_name]:
                count_name = f"{field_name}_count"
                setattr(self, count_name, getattr(self, count_name) + 1)

    def as_row(self, stencil_index: int, branch_index: int) -> dict[str, Any]:
        return {
            "stencil_index": stencil_index,
            "branch_index": branch_index,
            "record_count": self.record_count,
            "psi_cap_contact_count": self.psi_cap_contact_count,
            "phi_cap_contact_count": self.phi_cap_contact_count,
            "destructive_reset_count": self.destructive_reset_count,
            "nonfinite_detected_count": self.nonfinite_detected_count,
            "negative_phi_input_detected_count": self.negative_phi_input_detected_count,
            "undeclared_source_detected_count": self.undeclared_source_detected_count,
        }


@dataclass
class EvidenceState:
    """Small retained summaries needed after a one-pass shard stream."""

    protocol: Mapping[str, Any]
    primary: Mapping[str, Any]
    audit: Audit
    prepared: dict[int, tuple[np.ndarray, np.ndarray]] = field(default_factory=dict)
    prepared_metrics: dict[int, dict[str, Any]] = field(default_factory=dict)
    control_states: dict[tuple[int, int], tuple[np.ndarray, np.ndarray]] = field(
        default_factory=dict
    )
    recomputed_checkpoint_rows: list[dict[str, Any]] = field(default_factory=list)
    checkpoint_by_key: dict[tuple[int, int, int], dict[str, Any]] = field(
        default_factory=dict
    )
    starting_clones: bool = True
    receipt_only_control: bool = True
    energy: dict[tuple[int, int], EnergyAccumulator] = field(default_factory=dict)
    telemetry: dict[tuple[int, int], TelemetryAccumulator] = field(default_factory=dict)
    local_receipts: bool = True
    global_receipts: bool = True
    proposal_fidelity: bool = True
    zero_energy_technical_failure: bool = False
    local_receipt_count: int = 0
    global_receipt_count: int = 0


def _fail(message: str) -> NoReturn:
    raise ContractError(message)


def _strict_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            _fail("duplicate JSON object key")
        result[key] = value
    return result


def _reject_json_constant(_: str) -> NoReturn:
    _fail("non-finite JSON token")


def strict_json_loads(data: bytes) -> Any:
    """Parse UTF-8 JSON while rejecting duplicate keys and non-finite tokens."""

    try:
        text = data.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ContractError("input is not strict UTF-8") from exc
    try:
        return json.loads(
            text,
            object_pairs_hook=_strict_pairs,
            parse_constant=_reject_json_constant,
        )
    except ContractError:
        raise
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise ContractError("malformed JSON input") from exc


def canonical_payload_bytes(payload: Mapping[str, Any]) -> bytes:
    """Return the frozen compact canonical encoding without a trailing LF."""

    try:
        return json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ContractError("payload cannot be canonically encoded") from exc


def payload_with_self_hash(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Attach the contract hash over the canonical object with that field omitted."""

    result = dict(payload)
    result.pop("canonical_payload_sha256_without_self", None)
    digest = hashlib.sha256(canonical_payload_bytes(result)).hexdigest()
    result["canonical_payload_sha256_without_self"] = digest
    return result


def canonical_file_bytes(payload: Mapping[str, Any]) -> bytes:
    return canonical_payload_bytes(payload) + b"\n"


def git_blob_digest(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    digest = hashlib.sha1(usedforsecurity=False)
    digest.update(header)
    digest.update(data)
    return digest.hexdigest()


def file_identity(path: Path, relative_path: str) -> FileIdentity:
    """Hash a bounded regular file and return both SHA-256 and Git identity."""

    size = path.stat().st_size
    sha256 = hashlib.sha256()
    git_hash = hashlib.sha1(usedforsecurity=False)
    git_hash.update(f"blob {size}\0".encode("ascii"))
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            sha256.update(chunk)
            git_hash.update(chunk)
    return FileIdentity(relative_path, size, sha256.hexdigest(), git_hash.hexdigest())


def require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        _fail(f"{label} must be an object")
    return value


def require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        _fail(f"{label} must be an array")
    return value


def require_exact_fields(value: Mapping[str, Any], fields: Sequence[str], label: str) -> None:
    if set(value) != set(fields):
        _fail(f"{label} has a non-contract field set")


def require_bool(value: Any, label: str) -> bool:
    if type(value) is not bool:
        _fail(f"{label} must be a JSON boolean")
    return value


def require_int(value: Any, label: str, *, nonnegative: bool = False) -> int:
    if type(value) is not int:
        _fail(f"{label} must be a JSON integer")
    if nonnegative and value < 0:
        _fail(f"{label} must be nonnegative")
    return value


def require_float(value: Any, label: str) -> float:
    if type(value) is not float or not math.isfinite(value):
        _fail(f"{label} must be a finite binary64 JSON number")
    return value


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str):
        _fail(f"{label} must be a string")
    return value


def require_sha256(value: Any, label: str) -> str:
    text = require_string(value, label)
    if LOWERCASE_SHA256.fullmatch(text) is None:
        _fail(f"{label} must be a lowercase SHA-256")
    return text


def require_git_blob(value: Any, label: str) -> str:
    text = require_string(value, label)
    if LOWERCASE_GIT_BLOB.fullmatch(text) is None:
        _fail(f"{label} must be a lowercase Git blob")
    return text


def require_commit(value: Any, label: str) -> str:
    text = require_string(value, label)
    if LOWERCASE_COMMIT.fullmatch(text) is None:
        _fail(f"{label} must be a lowercase Git commit")
    return text


def require_finite_array(value: Any, shape: tuple[int, ...], label: str) -> np.ndarray:
    """Validate exact nested-list shape and float leaves before NumPy conversion."""

    def walk(node: Any, remaining: tuple[int, ...], path_label: str) -> None:
        if not remaining:
            require_float(node, path_label)
            return
        items = require_list(node, path_label)
        if len(items) != remaining[0]:
            _fail(f"{path_label} has the wrong array length")
        for index, item in enumerate(items):
            walk(item, remaining[1:], f"{path_label}[{index}]")

    walk(value, shape, label)
    array = np.asarray(value, dtype=np.float64)
    if array.shape != shape or not np.isfinite(array).all():
        _fail(f"{label} is not a finite binary64 array")
    return array


def exact_value_equal(left: Any, right: Any) -> bool:
    """Compare retained JSON values without adding an unfrozen numeric tolerance."""

    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(
            exact_value_equal(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            exact_value_equal(a, b) for a, b in zip(left, right, strict=True)
        )
    return bool(left == right)


def compare_exact(actual: Any, claimed: Any, audit: Audit, category: str) -> bool:
    matched = exact_value_equal(actual, claimed)
    if not matched:
        audit.mismatch(category)
    return matched


def _run_git(repository_root: Path, *arguments: str) -> str:
    completed = subprocess.run(
        ["git", *arguments],
        cwd=repository_root,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="strict",
    )
    if completed.returncode != 0:
        raise CheckerError("Git identity command failed")
    return completed.stdout.strip()


def _git_blob_at(repository_root: Path, revision: str, relative_path: str) -> str:
    value = _run_git(repository_root, "rev-parse", f"{revision}:{relative_path}")
    return require_git_blob(value, "Git tree blob")


def _git_filtered_blob(repository_root: Path, relative_path: str) -> str:
    value = _run_git(repository_root, "hash-object", "--", relative_path)
    return require_git_blob(value, "filtered Git blob")


def _require_path_blob(
    repository_root: Path,
    relative_path: str,
    expected_blob: str,
    *,
    filtered: bool,
) -> tuple[str, str]:
    head_blob = _git_blob_at(repository_root, "HEAD", relative_path)
    filtered_blob = _git_filtered_blob(repository_root, relative_path) if filtered else head_blob
    if head_blob != expected_blob or filtered_blob != expected_blob:
        raise CheckerError("frozen path identity mismatch")
    return filtered_blob, head_blob


def validate_frozen_protocol(protocol: Mapping[str, Any]) -> None:
    """Validate critical schema surfaces before any retained evidence is opened."""

    if protocol.get("schema") != FROZEN_PROTOCOL_SCHEMA:
        _fail("protocol schema mismatch")
    planned = require_object(protocol.get("planned_paths"), "protocol planned_paths")
    exact_paths = {
        "checker": CHECKER_PATH,
        "checker_execution_receipt": CHECKER_RECEIPT_PATH,
        "checker_output": CHECKER_OUTPUT_PATH,
        "checker_test": CHECKER_TEST_PATH,
        "primary_output": PRIMARY_PATH,
    }
    for key, expected in exact_paths.items():
        if planned.get(key) != expected:
            _fail("protocol planned path mismatch")
    retention = require_object(protocol.get("retention"), "protocol retention")
    shards = require_list(retention.get("evidence_shards"), "protocol evidence shards")
    planned_shards = require_list(
        planned.get("primary_evidence_shards"), "protocol planned shard paths"
    )
    if len(shards) != 6 or [row.get("path") for row in shards] != planned_shards:
        _fail("protocol shard order mismatch")
    outcome_map = require_list(protocol.get("outcome_map"), "protocol outcome map")
    if len(outcome_map) != 5 or any(not isinstance(item, str) for item in outcome_map):
        _fail("protocol outcome map mismatch")
    if len(set(outcome_map)) != len(outcome_map):
        _fail("protocol outcome map contains duplicates")


def read_frozen_protocol(repository_root: Path) -> tuple[dict[str, Any], FileIdentity]:
    path = repository_root / PROTOCOL_PATH
    identity = file_identity(path, PROTOCOL_PATH)
    if (
        identity.bytes != FROZEN_PROTOCOL_BYTES
        or identity.sha256 != FROZEN_PROTOCOL_SHA256
        or identity.git_blob != FROZEN_PROTOCOL_GIT_BLOB
    ):
        raise CheckerError("frozen preregistration byte identity mismatch")
    protocol = require_object(strict_json_loads(path.read_bytes()), "protocol")
    validate_frozen_protocol(protocol)
    return protocol, identity


def validate_checker_runtime(protocol: Mapping[str, Any]) -> None:
    """Fail closed unless the checker itself uses the frozen CPU/NumPy runtime."""

    runtime = require_object(protocol.get("runtime"), "protocol runtime")
    if runtime.get("backend") != "cpu_numpy_deterministic":
        raise CheckerError("checker backend contract mismatch")
    if platform.python_version() != runtime.get("python"):
        raise CheckerError("checker Python runtime mismatch")
    if np.__version__ != runtime.get("numpy"):
        raise CheckerError("checker NumPy runtime mismatch")


def parse_shard_binding(text: str, spec: Mapping[str, Any]) -> ShardIdentity:
    """Parse one identity-only CLI binding in frozen protocol order."""

    parts = text.split(":")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("shard identity must be BYTES:SHA256:GIT_BLOB")
    try:
        byte_count = int(parts[0])
    except ValueError as exc:
        raise argparse.ArgumentTypeError("shard byte count must be an integer") from exc
    if byte_count <= 0:
        raise argparse.ArgumentTypeError("shard byte count must be positive")
    if LOWERCASE_SHA256.fullmatch(parts[1]) is None:
        raise argparse.ArgumentTypeError("shard SHA-256 is invalid")
    if LOWERCASE_GIT_BLOB.fullmatch(parts[2]) is None:
        raise argparse.ArgumentTypeError("shard Git blob is invalid")
    return ShardIdentity(
        path=require_string(spec.get("path"), "protocol shard path"),
        bytes=byte_count,
        sha256=parts[1],
        git_blob=parts[2],
        record_count=require_int(spec.get("count"), "protocol shard count"),
        first_record_index=require_int(
            spec.get("first_record_index"), "protocol shard first index"
        ),
        last_record_index=require_int(
            spec.get("last_record_index"), "protocol shard last index"
        ),
    )


def build_invocation_bindings(
    arguments: argparse.Namespace, protocol: Mapping[str, Any]
) -> InvocationBindings:
    """Convert validated identity arguments into immutable invocation bindings."""

    execution_commit = require_commit(arguments.expected_execution_commit, "execution commit")
    remote_commit = require_commit(arguments.remote_readback_commit, "remote commit")
    blobs = {
        name: require_git_blob(getattr(arguments, name), name)
        for name in (
            "expected_checker_git_blob",
            "expected_checker_test_git_blob",
            "expected_report_git_blob",
            "expected_manifest_git_blob",
            "expected_primary_git_blob",
        )
    }
    primary_bytes = require_int(arguments.expected_primary_bytes, "primary bytes")
    if primary_bytes <= 0:
        raise CheckerError("primary byte count must be positive")
    primary_sha256 = require_sha256(arguments.expected_primary_sha256, "primary sha256")
    shard_specs = require_list(
        require_object(protocol["retention"], "protocol retention")["evidence_shards"],
        "protocol evidence shards",
    )
    if len(arguments.expected_shard_identity) != len(shard_specs):
        raise CheckerError("exactly six shard identities are required")
    shards = tuple(
        parse_shard_binding(text, spec)
        for text, spec in zip(arguments.expected_shard_identity, shard_specs, strict=True)
    )
    return InvocationBindings(
        execution_commit=execution_commit,
        remote_readback_commit=remote_commit,
        checker_git_blob=blobs["expected_checker_git_blob"],
        checker_test_git_blob=blobs["expected_checker_test_git_blob"],
        report_git_blob=blobs["expected_report_git_blob"],
        manifest_git_blob=blobs["expected_manifest_git_blob"],
        primary=FileIdentity(
            PRIMARY_PATH,
            primary_bytes,
            primary_sha256,
            blobs["expected_primary_git_blob"],
        ),
        shards=shards,
    )


def clean_preflight(
    repository_root: Path,
    bindings: InvocationBindings,
    protocol: Mapping[str, Any],
    protocol_identity: FileIdentity,
) -> ProgramGate:
    """Verify the clean fetched checkpoint without opening primary or shard files."""

    validate_checker_runtime(protocol)
    for terminal_path in (CHECKER_RECEIPT_PATH, CHECKER_OUTPUT_PATH):
        if (repository_root / terminal_path).exists():
            raise CheckerError("checker one-shot terminal path already exists")
    status = _run_git(repository_root, "status", "--porcelain", "--untracked-files=all")
    worktree_clean = status == ""
    if not worktree_clean:
        raise CheckerError("checker worktree is not clean")
    head_commit = require_commit(_run_git(repository_root, "rev-parse", "HEAD"), "HEAD")
    remote_commit = require_commit(
        _run_git(repository_root, "rev-parse", "--verify", FROZEN_REMOTE_REF),
        "fetched remote ref",
    )
    if (
        head_commit != bindings.execution_commit
        or remote_commit != bindings.remote_readback_commit
        or head_commit != remote_commit
    ):
        raise CheckerError("clean HEAD does not equal the exact fetched remote readback")
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FROZEN_PRIMARY_RESULT_COMMIT, head_commit],
        cwd=repository_root,
        check=False,
        capture_output=True,
    )
    if ancestor.returncode != 0:
        raise CheckerError("primary-result checkpoint is not an ancestor of checker HEAD")
    protocol_commit_ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FROZEN_PROTOCOL_REMOTE_COMMIT, head_commit],
        cwd=repository_root,
        check=False,
        capture_output=True,
    )
    if protocol_commit_ancestor.returncode != 0:
        raise CheckerError("frozen protocol checkpoint is not an ancestor of checker HEAD")

    checker_filtered, checker_head = _require_path_blob(
        repository_root, CHECKER_PATH, bindings.checker_git_blob, filtered=True
    )
    test_filtered, test_head = _require_path_blob(
        repository_root, CHECKER_TEST_PATH, bindings.checker_test_git_blob, filtered=True
    )
    _require_path_blob(repository_root, REPORT_PATH, bindings.report_git_blob, filtered=True)
    _require_path_blob(repository_root, MANIFEST_PATH, bindings.manifest_git_blob, filtered=True)
    _require_path_blob(
        repository_root, PROTOCOL_PATH, protocol_identity.git_blob, filtered=True
    )

    for expected in (bindings.primary, *bindings.shards):
        head_blob = _git_blob_at(repository_root, "HEAD", expected.path)
        retained_blob = _git_blob_at(
            repository_root, FROZEN_PRIMARY_RESULT_COMMIT, expected.path
        )
        if head_blob != expected.git_blob or retained_blob != expected.git_blob:
            raise CheckerError("retained input Git identity mismatch before latch")

    return ProgramGate(
        expected_execution_commit=bindings.execution_commit,
        actual_head_commit=head_commit,
        remote_readback_commit=bindings.remote_readback_commit,
        head_equals_remote_readback_commit=head_commit == bindings.remote_readback_commit,
        worktree_clean=worktree_clean,
        expected_checker_git_blob=bindings.checker_git_blob,
        actual_checker_filtered_git_blob=checker_filtered,
        actual_checker_head_git_blob=checker_head,
        expected_checker_test_git_blob=bindings.checker_test_git_blob,
        actual_checker_test_filtered_git_blob=test_filtered,
        actual_checker_test_head_git_blob=test_head,
    )


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _atomic_replace_json(
    path: Path, payload: Mapping[str, Any], *, replace_existing: bool = False
) -> None:
    """Publish canonical JSON via a same-directory fsynced temporary file."""

    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    data = canonical_file_bytes(payload)
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        if replace_existing:
            os.replace(temporary, path)
        else:
            try:
                os.link(temporary, path)
            except FileExistsError as exc:
                raise CheckerError("refusing to overwrite fixed checker artifact") from exc
            temporary.unlink()
    finally:
        if temporary.exists():
            temporary.unlink()


def _exclusive_create_json(path: Path, payload: Mapping[str, Any]) -> None:
    """Create a fixed one-shot receipt without overwrite or delete semantics."""

    path.parent.mkdir(parents=True, exist_ok=True)
    data = canonical_file_bytes(payload)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "wb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def build_receipt(
    *,
    status: str,
    started_at: str,
    ended_at: str | None,
    elapsed_seconds: float | None,
    execution_commit: str,
    program_identity: Mapping[str, Any],
    input_identity: Mapping[str, Any],
    output_identity: Mapping[str, Any] | None,
    stderr_identity: Mapping[str, Any] | None,
    failure: Mapping[str, Any] | None,
) -> dict[str, Any]:
    payload = {
        "schema": RECEIPT_SCHEMA,
        "protocol_id": FROZEN_PROTOCOL_SCHEMA,
        "lane": "checker",
        "attempt": 1,
        "invocation_limit": 1,
        "authority_consumed": True,
        "retry_authorized": False,
        "status": status,
        "started_at": started_at,
        "ended_at": ended_at,
        "elapsed_seconds": elapsed_seconds,
        "execution_commit": execution_commit,
        "program_identity": dict(program_identity),
        "input_identity": dict(input_identity),
        "output_identity": output_identity,
        "stderr_identity": stderr_identity,
        "failure": failure,
    }
    return payload_with_self_hash(payload)


def _sanitize_failure_message(message: str, repository_root: Path) -> str:
    sanitized = message.replace(str(repository_root), "<repository>")
    sanitized = sanitized.replace(str(Path.home()), "<home>")
    sanitized = re.sub(
        r"\\\\[^\\/\s]+[\\/][^\\/\s]+(?:[\\/][^\s]*)?",
        "<path>",
        sanitized,
    )
    sanitized = re.sub(r"(?i)[a-z]:[\\/][^\s]+", "<path>", sanitized)
    sanitized = re.sub(r"(?<![A-Za-z0-9_])\\[^\s]+", "<path>", sanitized)
    sanitized = re.sub(r"(?<![A-Za-z0-9_])(?:/[^\s]+)+", "<path>", sanitized)
    return sanitized[:240]


def initial_receipt_inputs(
    protocol_identity: FileIdentity, bindings: InvocationBindings
) -> dict[str, Any]:
    return {
        "protocol": protocol_identity.as_dict(),
        "primary": bindings.primary.as_dict(),
        "shards": [identity.as_dict() for identity in bindings.shards],
    }


def program_identity(gate: ProgramGate) -> dict[str, Any]:
    return {
        "path": CHECKER_PATH,
        "git_blob": gate.actual_checker_head_git_blob,
        "test_path": CHECKER_TEST_PATH,
        "test_git_blob": gate.actual_checker_test_head_git_blob,
    }


def create_attempt_latch(
    repository_root: Path,
    gate: ProgramGate,
    protocol_identity: FileIdentity,
    bindings: InvocationBindings,
) -> tuple[str, float, dict[str, Any], dict[str, Any]]:
    """Consume checker authority before any retained primary or shard read."""

    started_at = _utc_now()
    start = time.monotonic()
    program = program_identity(gate)
    inputs = initial_receipt_inputs(protocol_identity, bindings)
    receipt = build_receipt(
        status="attempt_started_authority_consumed",
        started_at=started_at,
        ended_at=None,
        elapsed_seconds=None,
        execution_commit=gate.actual_head_commit,
        program_identity=program,
        input_identity=inputs,
        output_identity=None,
        stderr_identity=None,
        failure=None,
    )
    _exclusive_create_json(repository_root / CHECKER_RECEIPT_PATH, receipt)
    return started_at, start, program, inputs


def _validate_file_identity_object(
    value: Any, label: str, *, protocol_schema: bool = False
) -> dict[str, Any]:
    row = require_object(value, label)
    fields = ["path", "bytes", "sha256", "git_blob"]
    if protocol_schema:
        fields.insert(1, "schema")
    require_exact_fields(row, fields, label)
    require_string(row["path"], f"{label}.path")
    if protocol_schema:
        require_string(row["schema"], f"{label}.schema")
    require_int(row["bytes"], f"{label}.bytes", nonnegative=True)
    require_sha256(row["sha256"], f"{label}.sha256")
    require_git_blob(row["git_blob"], f"{label}.git_blob")
    return row


def _validate_primary_source_gate(
    repository_root: Path,
    gate: Mapping[str, Any],
    protocol: Mapping[str, Any],
) -> bool:
    contract = require_object(
        require_object(protocol["retention"], "retention")["primary_output_contract"],
        "primary output contract",
    )
    fields = require_list(
        contract["source_identity_gate_fields"], "source identity gate fields"
    )
    require_exact_fields(gate, fields, "primary source_identity_gate")
    require_bool(gate["passed"], "source_identity_gate.passed")
    execution_commit = require_commit(
        gate["expected_execution_commit"], "source expected execution commit"
    )
    actual_commit = require_commit(gate["actual_head_commit"], "source actual commit")
    remote_commit = require_commit(gate["remote_readback_commit"], "source remote commit")
    head_remote = require_bool(
        gate["head_equals_remote_readback_commit"], "source head remote equality"
    )
    clean = require_bool(gate["worktree_clean"], "source worktree clean")

    identity_triplets = (
        (
            "expected_runner_git_blob",
            "actual_runner_filtered_git_blob",
            "actual_runner_head_git_blob",
            require_object(protocol["planned_paths"], "planned paths")["runner"],
        ),
        (
            "expected_runner_test_git_blob",
            "actual_runner_test_filtered_git_blob",
            "actual_runner_test_head_git_blob",
            require_object(protocol["planned_paths"], "planned paths")["runner_test"],
        ),
        (
            "expected_report_git_blob",
            "actual_report_filtered_git_blob",
            "actual_report_head_git_blob",
            REPORT_PATH,
        ),
        (
            "expected_manifest_git_blob",
            "actual_manifest_filtered_git_blob",
            "actual_manifest_head_git_blob",
            MANIFEST_PATH,
        ),
    )
    exact = (
        execution_commit == actual_commit == remote_commit
        and head_remote
        and clean
    )
    for expected_name, filtered_name, head_name, path in identity_triplets:
        expected = require_git_blob(gate[expected_name], expected_name)
        filtered = require_git_blob(gate[filtered_name], filtered_name)
        head = require_git_blob(gate[head_name], head_name)
        try:
            committed = _git_blob_at(repository_root, execution_commit, path)
        except CheckerError:
            committed = ""
        exact = exact and expected == filtered == head == committed

    expected_sources = require_object(gate["expected"], "source expected map")
    actual_sources = require_object(gate["actual"], "source actual map")
    source_fields = require_list(
        contract["source_identity_expected_actual_fields"], "source identity fields"
    )
    require_exact_fields(expected_sources, source_fields, "source expected map")
    require_exact_fields(actual_sources, source_fields, "source actual map")
    source_bindings = require_object(protocol["source_bindings"], "protocol source bindings")
    source_paths = {
        "core_math_git_blob": "lineum_core/math.py",
        "localized_reference_runner_git_blob": (
            "research/runners/lineum_b4_saturation_localized_l1.py"
        ),
        "requirements_git_blob": "requirements.txt",
        "requirements_dev_git_blob": "requirements-dev.txt",
    }
    for field_name in source_fields:
        expected = require_git_blob(expected_sources[field_name], f"expected.{field_name}")
        actual = require_git_blob(actual_sources[field_name], f"actual.{field_name}")
        frozen = require_git_blob(source_bindings[field_name], f"protocol.{field_name}")
        try:
            committed = _git_blob_at(
                repository_root, execution_commit, source_paths[field_name]
            )
        except CheckerError:
            committed = ""
        exact = exact and expected == actual == frozen == committed
    return require_bool(gate["passed"], "source gate passed") == exact and exact


def validate_primary_structure(
    repository_root: Path,
    primary: Mapping[str, Any],
    protocol: Mapping[str, Any],
    protocol_identity: FileIdentity,
) -> tuple[bool, bool]:
    """Validate the full public primary schema and return its identity-gate truth."""

    retention = require_object(protocol["retention"], "protocol retention")
    contract = require_object(retention["primary_output_contract"], "primary contract")
    top_fields = require_list(contract["top_level_fields"], "primary top-level fields")
    require_exact_fields(primary, top_fields, "primary")
    if primary["schema"] != PRIMARY_SCHEMA:
        _fail("primary schema mismatch")
    self_hash = require_sha256(
        primary["canonical_payload_sha256_without_self"], "primary payload hash"
    )
    without_self = dict(primary)
    without_self.pop("canonical_payload_sha256_without_self")
    if hashlib.sha256(canonical_payload_bytes(without_self)).hexdigest() != self_hash:
        _fail("primary canonical payload hash mismatch")

    protocol_row = _validate_file_identity_object(
        primary["protocol_identity"], "primary protocol identity", protocol_schema=True
    )
    expected_protocol = {
        "path": PROTOCOL_PATH,
        "schema": FROZEN_PROTOCOL_SCHEMA,
        "bytes": protocol_identity.bytes,
        "sha256": protocol_identity.sha256,
        "git_blob": protocol_identity.git_blob,
    }
    if not exact_value_equal(protocol_row, expected_protocol):
        _fail("primary protocol identity mismatch")

    execution = require_object(primary["execution_identity"], "execution identity")
    require_exact_fields(
        execution,
        require_list(contract["execution_identity_fields"], "execution identity fields"),
        "execution identity",
    )
    expected_execution = {
        "attempt": 1,
        "trajectory_execution_count": 1,
        "stencil_count": len(retention["evidence_index_maps"]["stencil_index"]),
        "branch_count": len(retention["evidence_index_maps"]["branch_index"]),
        "continuation_steps": protocol["baseline"]["continuation_steps"],
    }
    for key, expected in expected_execution.items():
        require_int(execution[key], f"execution_identity.{key}")
        if execution[key] != expected:
            _fail("primary execution identity value mismatch")

    if not exact_value_equal(primary["index_maps"], retention["evidence_index_maps"]):
        _fail("primary index maps mismatch")
    if not exact_value_equal(primary["claim_boundary"], protocol["claim_boundary"]):
        _fail("primary claim boundary mismatch")
    for key, value in require_object(primary["claim_boundary"], "claim boundary").items():
        require_bool(value, f"claim_boundary.{key}")

    runtime = require_object(primary["runtime_gate"], "runtime gate")
    require_exact_fields(
        runtime,
        require_list(contract["runtime_gate_fields"], "runtime gate fields"),
        "runtime gate",
    )
    runtime_exact = (
        require_bool(runtime["passed"], "runtime passed")
        and runtime["backend"] == protocol["runtime"]["backend"]
        and runtime["python"] == protocol["runtime"]["python"]
        and runtime["numpy"] == protocol["runtime"]["numpy"]
    )
    for key in ("backend", "python", "numpy"):
        require_string(runtime[key], f"runtime.{key}")

    source_gate = require_object(primary["source_identity_gate"], "source identity gate")
    source_exact = _validate_primary_source_gate(
        repository_root, source_gate, protocol
    )

    evidence = require_object(primary["evidence_identity"], "evidence identity")
    require_exact_fields(
        evidence,
        require_list(contract["evidence_identity_fields"], "evidence identity fields"),
        "evidence identity",
    )
    if require_int(evidence["shard_count"], "evidence shard count") != 6:
        _fail("primary evidence shard count mismatch")
    if (
        require_int(evidence["total_record_count"], "evidence total record count")
        != retention["evidence_total_records"]
    ):
        _fail("primary evidence total count mismatch")
    shard_rows = require_list(evidence["shards"], "primary evidence shards")
    shard_fields = require_list(
        contract["evidence_shard_identity_fields"], "primary evidence shard fields"
    )
    shard_specs = require_list(retention["evidence_shards"], "protocol evidence shards")
    if len(shard_rows) != len(shard_specs):
        _fail("primary evidence shard list length mismatch")
    for index, (row_value, spec) in enumerate(zip(shard_rows, shard_specs, strict=True)):
        row = require_object(row_value, f"primary evidence shard {index}")
        require_exact_fields(row, shard_fields, f"primary evidence shard {index}")
        require_string(row["path"], f"shard {index} path")
        require_int(row["bytes"], f"shard {index} bytes")
        require_sha256(row["sha256"], f"shard {index} sha256")
        for field_name, spec_name in (
            ("record_count", "count"),
            ("first_record_index", "first_record_index"),
            ("last_record_index", "last_record_index"),
        ):
            require_int(row[field_name], f"shard {index} {field_name}")
            if row[field_name] != spec[spec_name]:
                _fail("primary evidence range mismatch")
        if row["path"] != spec["path"] or row["bytes"] <= 0:
            _fail("primary evidence identity mismatch")

    checkpoint_rows = require_list(primary["checkpoint_metrics"], "checkpoint metrics")
    if len(checkpoint_rows) != contract["checkpoint_metric_count"]:
        _fail("primary checkpoint metric count mismatch")
    checkpoint_fields = require_list(
        contract["checkpoint_metric_fields"], "checkpoint metric fields"
    )
    profile_length = require_int(
        contract["checkpoint_profile_length"], "checkpoint profile length"
    )
    for index, row_value in enumerate(checkpoint_rows):
        row = require_object(row_value, f"checkpoint metric {index}")
        require_exact_fields(row, checkpoint_fields, f"checkpoint metric {index}")
        for field_name in ("stencil_index", "branch_index", "checkpoint_index", "step"):
            require_int(row[field_name], f"checkpoint metric {index}.{field_name}")
        require_bool(row["finite"], f"checkpoint metric {index}.finite")
        for field_name in checkpoint_fields:
            if field_name in {
                "stencil_index",
                "branch_index",
                "checkpoint_index",
                "step",
                "finite",
                "psi_radial_profile",
                "phi_radial_profile",
            }:
                continue
            require_float(row[field_name], f"checkpoint metric {index}.{field_name}")
        for field_name in ("psi_radial_profile", "phi_radial_profile"):
            values = require_list(row[field_name], f"checkpoint metric {index}.{field_name}")
            if len(values) != profile_length:
                _fail("primary checkpoint profile length mismatch")
            for item_index, item in enumerate(values):
                require_float(item, f"{field_name}[{item_index}]")

    energy_rows = require_list(
        primary["trajectory_energy_summaries"], "trajectory energy summaries"
    )
    if len(energy_rows) != contract["trajectory_energy_summary_count"]:
        _fail("primary trajectory energy summary count mismatch")
    energy_fields = require_list(
        contract["trajectory_energy_summary_fields"], "trajectory energy summary fields"
    )
    for index, row_value in enumerate(energy_rows):
        row = require_object(row_value, f"trajectory energy summary {index}")
        require_exact_fields(row, energy_fields, f"trajectory energy summary {index}")
        for field_name in ("stencil_index", "branch_index", "record_count"):
            require_int(row[field_name], f"energy summary {index}.{field_name}")
        for field_name in (
            "pre_total_psi_energy",
            "minimum_total_psi_energy",
            "maximum_total_psi_energy",
            "minimum_energy_ratio",
            "maximum_energy_ratio",
        ):
            require_float(row[field_name], f"energy summary {index}.{field_name}")
        for field_name in (
            "first_lower_bound_violation_step",
            "first_upper_bound_violation_step",
        ):
            value = row[field_name]
            if value is not None:
                require_int(value, f"energy summary {index}.{field_name}")

    telemetry_rows = require_list(
        primary["technical_telemetry_summaries"], "technical telemetry summaries"
    )
    if len(telemetry_rows) != contract["technical_telemetry_summary_count"]:
        _fail("primary telemetry summary count mismatch")
    telemetry_fields = require_list(
        contract["technical_telemetry_summary_fields"], "telemetry summary fields"
    )
    for index, row_value in enumerate(telemetry_rows):
        row = require_object(row_value, f"telemetry summary {index}")
        require_exact_fields(row, telemetry_fields, f"telemetry summary {index}")
        for field_name in telemetry_fields:
            require_int(row[field_name], f"telemetry summary {index}.{field_name}", nonnegative=True)

    comparisons = require_list(primary["comparisons"], "comparisons")
    if len(comparisons) != contract["comparison_count"]:
        _fail("primary comparison count mismatch")
    comparison_fields = require_list(contract["comparison_fields"], "comparison fields")
    for index, row_value in enumerate(comparisons):
        row = require_object(row_value, f"comparison {index}")
        require_exact_fields(row, comparison_fields, f"comparison {index}")
        for field_name in (
            "comparison_index",
            "stencil_index",
            "step",
            "reference_branch_index",
            "candidate_branch_index",
        ):
            require_int(row[field_name], f"comparison {index}.{field_name}")
        for field_name in ("comparison_kind", "metric"):
            require_string(row[field_name], f"comparison {index}.{field_name}")
        for field_name in (
            "reference_value",
            "candidate_value",
            "tolerance",
            "improvement",
        ):
            require_float(row[field_name], f"comparison {index}.{field_name}")
        require_bool(row["passed"], f"comparison {index}.passed")

    gates = require_object(primary["gates"], "primary gates")
    require_exact_fields(
        gates, require_list(contract["gates_fields"], "gates fields"), "primary gates"
    )
    for key, value in gates.items():
        require_bool(value, f"gates.{key}")
    classification = require_object(primary["classification"], "classification")
    require_exact_fields(
        classification,
        require_list(contract["classification_fields"], "classification fields"),
        "classification",
    )
    # The claimed outcome is deliberately not accessed until independent
    # recomputation and classification are complete.
    return source_exact, runtime_exact


def load_primary_after_latch(
    repository_root: Path,
    expected: FileIdentity,
    protocol: Mapping[str, Any],
    protocol_identity: FileIdentity,
) -> tuple[dict[str, Any], FileIdentity, bool, bool]:
    """Open the retained primary only after the caller has consumed authority."""

    path = repository_root / expected.path
    data = path.read_bytes()
    actual = FileIdentity(
        expected.path,
        len(data),
        hashlib.sha256(data).hexdigest(),
        git_blob_digest(data),
    )
    if actual != expected:
        raise ContractError("retained primary file identity mismatch")
    if not data.endswith(b"\n") or data.endswith(b"\n\n") or b"\r" in data or data.startswith(b"\xef\xbb\xbf"):
        _fail("primary file encoding is not canonical")
    primary = require_object(strict_json_loads(data), "primary")
    if canonical_file_bytes(primary) != data:
        _fail("primary file is not exact canonical JSON plus one LF")
    source_identity_truth, runtime_truth = validate_primary_structure(
        repository_root, primary, protocol, protocol_identity
    )
    return primary, actual, source_identity_truth, runtime_truth


def _validate_manifest_file_entry(
    files: Mapping[str, Any],
    identity: FileIdentity,
    *,
    schema: str | None = None,
    shard: ShardIdentity | None = None,
) -> None:
    """Cross-bind one identity entry while deliberately ignoring free-text roles."""

    if identity.path not in files:
        _fail("manifest is missing a frozen checker input entry")
    entry = require_object(files[identity.path], f"manifest file {identity.path}")
    required = {"bytes", "sha256", "git_blob_sha"}
    if not required.issubset(entry):
        _fail("manifest file entry lacks identity fields")
    if (
        require_int(entry["bytes"], "manifest file bytes") != identity.bytes
        or require_sha256(entry["sha256"], "manifest file sha256") != identity.sha256
        or require_git_blob(entry["git_blob_sha"], "manifest file git blob")
        != identity.git_blob
    ):
        _fail("manifest file identity does not match the frozen binding")
    if schema is not None and entry.get("schema") != schema:
        _fail("manifest file schema mismatch")
    if shard is not None:
        for field_name in (
            "record_count",
            "first_record_index",
            "last_record_index",
        ):
            if require_int(entry.get(field_name), f"manifest shard {field_name}") != getattr(
                shard, field_name
            ):
                _fail("manifest shard range identity mismatch")


def validate_manifest_after_latch(
    repository_root: Path,
    protocol: Mapping[str, Any],
    protocol_identity: FileIdentity,
    bindings: InvocationBindings,
) -> None:
    """Strictly cross-bind machine fields without consulting prose or outcome labels."""

    manifest_path = repository_root / MANIFEST_PATH
    manifest_identity = file_identity(manifest_path, MANIFEST_PATH)
    if manifest_identity.git_blob != bindings.manifest_git_blob:
        _fail("manifest Git identity changed after preflight")
    manifest = require_object(strict_json_loads(manifest_path.read_bytes()), "manifest")
    if manifest.get("schema") != MANIFEST_SCHEMA:
        _fail("manifest schema mismatch")
    if manifest.get("source_report") != REPORT_PATH:
        _fail("manifest source report path mismatch")
    q2 = require_object(manifest.get("q2_m2_rwc1"), "manifest q2_m2_rwc1")
    if require_git_blob(
        q2.get("continuity_report_git_blob"), "manifest continuity report blob"
    ) != bindings.report_git_blob:
        _fail("manifest continuity report identity mismatch")
    if q2.get("protocol_path") != PROTOCOL_PATH or q2.get("protocol_schema") != FROZEN_PROTOCOL_SCHEMA:
        _fail("manifest protocol routing mismatch")
    if q2.get("primary_output_path") != PRIMARY_PATH:
        _fail("manifest primary routing mismatch")
    if require_int(q2.get("evidence_shards"), "manifest evidence shard count") != len(
        bindings.shards
    ):
        _fail("manifest evidence shard count mismatch")
    if (
        require_int(q2.get("evidence_record_count"), "manifest evidence record count")
        != protocol["retention"]["evidence_total_records"]
        or require_int(q2.get("evidence_first_record_index"), "manifest first index")
        != bindings.shards[0].first_record_index
        or require_int(q2.get("evidence_last_record_index"), "manifest last index")
        != bindings.shards[-1].last_record_index
        or require_int(q2.get("evidence_max_shard_bytes"), "manifest shard byte cap")
        != protocol["retention"]["evidence_max_shard_bytes"]
    ):
        _fail("manifest aggregate evidence identity mismatch")

    files = require_object(manifest.get("files"), "manifest files")
    checker_identity = file_identity(repository_root / CHECKER_PATH, CHECKER_PATH)
    checker_test_identity = file_identity(
        repository_root / CHECKER_TEST_PATH, CHECKER_TEST_PATH
    )
    if checker_identity.git_blob != bindings.checker_git_blob:
        _fail("checker source changed after clean preflight")
    if checker_test_identity.git_blob != bindings.checker_test_git_blob:
        _fail("checker test changed after clean preflight")
    _validate_manifest_file_entry(files, protocol_identity)
    _validate_manifest_file_entry(files, checker_identity)
    _validate_manifest_file_entry(files, checker_test_identity)
    _validate_manifest_file_entry(files, bindings.primary, schema=PRIMARY_SCHEMA)
    for shard_identity in bindings.shards:
        _validate_manifest_file_entry(
            files, shard_identity, shard=shard_identity
        )


def _observer_geometry(grid_size: int, profile_length: int) -> tuple[np.ndarray, ...]:
    coordinates = np.indices((grid_size, grid_size), dtype=np.float64)
    rows, columns = coordinates[0], coordinates[1]
    center = (grid_size - 1.0) / 2.0
    radius = np.sqrt((rows - center) ** 2 + (columns - center) ** 2)
    bins = np.floor(radius).astype(np.int64)
    if int(bins.max()) >= profile_length:
        _fail("frozen checkpoint profile length cannot cover the grid")
    bin_counts = np.bincount(bins.ravel(), minlength=profile_length).astype(np.float64)
    return rows, columns, radius, bins, bin_counts


def _radial_profile(
    values: np.ndarray,
    bins: np.ndarray,
    bin_counts: np.ndarray,
    profile_length: int,
) -> np.ndarray:
    weighted = np.bincount(
        bins.ravel(), weights=values.ravel(), minlength=profile_length
    ).astype(np.float64)
    return weighted[:profile_length] / np.maximum(bin_counts[:profile_length], 1.0)


def _half_energy_radius(energy: np.ndarray, radius: np.ndarray, total: float) -> float:
    order = np.argsort(radius.ravel(), kind="stable")
    ordered_energy = energy.ravel()[order]
    cumulative = np.cumsum(ordered_energy, dtype=np.float64)
    position = int(np.searchsorted(cumulative, 0.5 * total, side="left"))
    position = min(position, order.size - 1)
    return float(radius.ravel()[order[position]])


def _base_observer_metrics(
    psi: np.ndarray,
    phi: np.ndarray,
    geometry: tuple[np.ndarray, ...],
    profile_length: int,
) -> dict[str, Any]:
    rows, columns, radius, bins, bin_counts = geometry
    energy = np.abs(psi) ** 2
    total = float(np.sum(energy, dtype=np.float64))
    finite = bool(np.isfinite(psi).all() and np.isfinite(phi).all() and math.isfinite(total))
    if not finite or total <= 0.0:
        raise ContractError("nonpositive or nonfinite checkpoint energy")
    centroid_row = float(np.sum(rows * energy, dtype=np.float64) / total)
    centroid_column = float(np.sum(columns * energy, dtype=np.float64) / total)
    center = (psi.shape[0] - 1.0) / 2.0
    return {
        "total_psi_energy": total,
        "psi_radial_profile": _radial_profile(
            energy, bins, bin_counts, profile_length
        ),
        "phi_radial_profile": _radial_profile(
            phi, bins, bin_counts, profile_length
        ),
        "half_energy_radius": _half_energy_radius(energy, radius, total),
        "centroid_row": centroid_row,
        "centroid_column": centroid_column,
        "fixed_center_displacement": float(
            math.hypot(centroid_row - center, centroid_column - center)
        ),
        "energy_fraction_radius_3": float(np.sum(energy[radius <= 3.0]) / total),
        "energy_fraction_radius_6": float(np.sum(energy[radius <= 6.0]) / total),
        "energy_fraction_radius_10": float(np.sum(energy[radius <= 10.0]) / total),
        "phi_min": float(np.min(phi)),
        "phi_mean": float(np.mean(phi, dtype=np.float64)),
        "phi_max": float(np.max(phi)),
        "phi_total": float(np.sum(phi, dtype=np.float64)),
        "max_abs_psi": float(np.max(np.abs(psi))),
        "finite": finite,
    }


def checkpoint_metrics(
    *,
    stencil_index: int,
    branch_index: int,
    checkpoint_index: int,
    step: int,
    psi: np.ndarray,
    phi: np.ndarray,
    prepared: Mapping[str, Any],
    geometry: tuple[np.ndarray, ...],
    profile_length: int,
    energy_denominator_floor: float,
    profile_denominator_floor: float,
) -> dict[str, Any]:
    current = _base_observer_metrics(psi, phi, geometry, profile_length)
    pre_total = prepared["total_psi_energy"]
    psi_profile = current["psi_radial_profile"]
    phi_profile = current["phi_radial_profile"]
    pre_psi_profile = prepared["psi_radial_profile"]
    pre_phi_profile = prepared["phi_radial_profile"]
    result = {
        "stencil_index": stencil_index,
        "branch_index": branch_index,
        "checkpoint_index": checkpoint_index,
        "step": step,
        "total_psi_energy": current["total_psi_energy"],
        "psi_energy_relative_error": float(
            abs(current["total_psi_energy"] - pre_total)
            / (abs(pre_total) + energy_denominator_floor)
        ),
        "psi_radial_profile": [float(value) for value in psi_profile],
        "psi_radial_profile_relative_l2_error": float(
            np.linalg.norm(psi_profile - pre_psi_profile)
            / (np.linalg.norm(pre_psi_profile) + profile_denominator_floor)
        ),
        "phi_radial_profile": [float(value) for value in phi_profile],
        "phi_radial_profile_relative_l2_error": float(
            np.linalg.norm(phi_profile - pre_phi_profile)
            / (np.linalg.norm(pre_phi_profile) + profile_denominator_floor)
        ),
        "half_energy_radius": current["half_energy_radius"],
        "half_energy_radius_absolute_change": float(
            abs(current["half_energy_radius"] - prepared["half_energy_radius"])
        ),
        "centroid_row": current["centroid_row"],
        "centroid_column": current["centroid_column"],
        "fixed_center_displacement": current["fixed_center_displacement"],
        "centroid_shift_from_pre": float(
            math.hypot(
                current["centroid_row"] - prepared["centroid_row"],
                current["centroid_column"] - prepared["centroid_column"],
            )
        ),
        "energy_fraction_radius_3": current["energy_fraction_radius_3"],
        "energy_fraction_radius_6": current["energy_fraction_radius_6"],
        "energy_fraction_radius_10": current["energy_fraction_radius_10"],
        "phi_min": current["phi_min"],
        "phi_mean": current["phi_mean"],
        "phi_max": current["phi_max"],
        "phi_total": current["phi_total"],
        "max_abs_psi": current["max_abs_psi"],
        "finite": current["finite"],
    }
    return result


def _denominator_floor(expression: Any, label: str) -> float:
    text = require_string(expression, label)
    match = re.search(r"\+\s*([0-9]+(?:\.[0-9]+)?(?:e[+-]?[0-9]+)?)\s*\Z", text)
    if match is None:
        _fail(f"{label} does not end in a numeric denominator floor")
    value = float(match.group(1))
    if not math.isfinite(value) or value <= 0.0:
        _fail(f"{label} denominator floor is invalid")
    return value


def _expected_record_descriptor(
    protocol: Mapping[str, Any], shard_index: int, ordinal: int
) -> tuple[str, dict[str, int]]:
    retention = require_object(protocol["retention"], "retention")
    maps = require_object(retention["evidence_index_maps"], "evidence index maps")
    stencil_count = len(require_list(maps["stencil_index"], "stencil map"))
    branch_names = require_list(maps["branch_index"], "branch map")
    branch_count = len(branch_names)
    checkpoints = require_list(maps["checkpoint_index"], "checkpoint map")
    checkpoint_count = len(checkpoints)
    stage_names = require_list(maps["stage_index"], "stage map")
    steps = require_int(protocol["baseline"]["continuation_steps"], "continuation steps")

    if shard_index == 0:
        if ordinal < stencil_count:
            return "prepared_state", {"stencil_index": ordinal}
        offset = ordinal - stencil_count
        stencil_index, remainder = divmod(offset, branch_count * checkpoint_count)
        branch_index, checkpoint_index = divmod(remainder, checkpoint_count)
        return "checkpoint_state", {
            "stencil_index": stencil_index,
            "branch_index": branch_index,
            "checkpoint_index": checkpoint_index,
            "step": require_int(checkpoints[checkpoint_index], "checkpoint step"),
        }
    if shard_index in (1, 2):
        stencil_index, remainder = divmod(ordinal, branch_count * steps)
        branch_index, step_offset = divmod(remainder, steps)
        record_type = "step_energy" if shard_index == 1 else "step_telemetry"
        return record_type, {
            "stencil_index": stencil_index,
            "branch_index": branch_index,
            "step": step_offset + 1,
        }
    if shard_index in (3, 4):
        stencil_index = shard_index - 3
        flow = stage_names.index("flow")
        interaction = stage_names.index("interaction")
        layouts = (
            (branch_names.index("RECEIPT_ONLY"), (flow, interaction)),
            (branch_names.index("PAIR_INTERACTION"), (interaction,)),
            (branch_names.index("PAIR_FLOW"), (flow,)),
            (branch_names.index("PAIR_BOTH"), (flow, interaction)),
        )
        cursor = ordinal
        for branch_index, stages in layouts:
            block_size = steps * len(stages)
            if cursor < block_size:
                step_offset, stage_offset = divmod(cursor, len(stages))
                return "local_stage_receipt", {
                    "stencil_index": stencil_index,
                    "branch_index": branch_index,
                    "step": step_offset + 1,
                    "stage_index": stages[stage_offset],
                }
            cursor -= block_size
        _fail("local receipt ordinal exceeds the frozen branch layout")
    if shard_index == 5:
        global_branch = branch_names.index("GLOBAL_POOL_PAIR_BOTH")
        stage_count = len(stage_names)
        stencil_index, remainder = divmod(ordinal, steps * stage_count)
        step_offset, stage_index = divmod(remainder, stage_count)
        return "global_stage_receipt", {
            "stencil_index": stencil_index,
            "branch_index": global_branch,
            "step": step_offset + 1,
            "stage_index": stage_index,
        }
    _fail("unknown evidence shard index")


def _validate_record(
    protocol: Mapping[str, Any],
    record: Mapping[str, Any],
    record_type: str,
    expected_descriptor: Mapping[str, int],
    expected_record_index: int,
) -> None:
    retention = require_object(protocol["retention"], "retention")
    schemas = require_object(retention["evidence_record_schemas"], "evidence schemas")
    schema = require_object(schemas[record_type], f"schema {record_type}")
    fields = require_list(schema["fields"], f"schema fields {record_type}")
    require_exact_fields(record, fields, f"evidence record {expected_record_index}")
    if record.get("record_type") != record_type:
        _fail("evidence record type mismatch")
    if require_int(record.get("record_index"), "record_index") != expected_record_index:
        _fail("evidence global record index mismatch")
    for field_name, expected in expected_descriptor.items():
        if require_int(record.get(field_name), field_name) != expected:
            _fail("evidence record ordering descriptor mismatch")

    index_fields = {
        "record_index",
        "stencil_index",
        "branch_index",
        "checkpoint_index",
        "step",
        "stage_index",
        "positive_cell_count",
        "negative_cell_count",
        "zero_cell_count",
        "argmax_flat_index",
        "argmax_row",
        "argmax_column",
    }
    boolean_fields = {
        "precondition_passed",
        "psi_cap_contact",
        "phi_cap_contact",
        "destructive_reset",
        "nonfinite_detected",
        "negative_phi_input_detected",
        "undeclared_source_detected",
    }
    array_fields = {"psi_real", "psi_imag", "phi"}
    shape = tuple(require_list(schema.get("array_shape", []), "record array shape"))
    for field_name in fields:
        if field_name in {"record_type"}:
            require_string(record[field_name], field_name)
        elif field_name in index_fields:
            require_int(record[field_name], field_name, nonnegative=True)
        elif field_name in boolean_fields:
            require_bool(record[field_name], field_name)
        elif field_name in array_fields:
            require_finite_array(record[field_name], shape, field_name)
        else:
            require_float(record[field_name], field_name)


def _state_arrays(record: Mapping[str, Any], grid_size: int) -> tuple[np.ndarray, np.ndarray]:
    shape = (grid_size, grid_size)
    real = require_finite_array(record["psi_real"], shape, "psi_real")
    imaginary = require_finite_array(record["psi_imag"], shape, "psi_imag")
    phi = require_finite_array(record["phi"], shape, "phi")
    return real + 1j * imaginary, phi


def _process_prepared_state(state: EvidenceState, record: Mapping[str, Any]) -> None:
    protocol = state.protocol
    grid_size = require_int(protocol["baseline"]["grid_size"], "grid size")
    contract = protocol["retention"]["primary_output_contract"]
    profile_length = require_int(contract["checkpoint_profile_length"], "profile length")
    stencil_index = record["stencil_index"]
    if stencil_index in state.prepared:
        _fail("duplicate prepared stencil state")
    psi, phi = _state_arrays(record, grid_size)
    geometry = _observer_geometry(grid_size, profile_length)
    metrics = _base_observer_metrics(psi, phi, geometry, profile_length)
    state.prepared[stencil_index] = (psi, phi)
    state.prepared_metrics[stencil_index] = metrics


def _process_checkpoint_state(state: EvidenceState, record: Mapping[str, Any]) -> None:
    protocol = state.protocol
    contract = protocol["retention"]["primary_output_contract"]
    grid_size = require_int(protocol["baseline"]["grid_size"], "grid size")
    profile_length = require_int(contract["checkpoint_profile_length"], "profile length")
    stencil_index = record["stencil_index"]
    branch_index = record["branch_index"]
    checkpoint_index = record["checkpoint_index"]
    maps = protocol["retention"]["evidence_index_maps"]
    branch_names = maps["branch_index"]
    control_index = branch_names.index("CONTROL")
    receipt_only_index = branch_names.index("RECEIPT_ONLY")
    if stencil_index not in state.prepared:
        _fail("checkpoint precedes its prepared state")
    psi, phi = _state_arrays(record, grid_size)
    prepared_psi, prepared_phi = state.prepared[stencil_index]
    if checkpoint_index == 0 and not (
        np.array_equal(psi, prepared_psi) and np.array_equal(phi, prepared_phi)
    ):
        state.starting_clones = False
    if branch_index == control_index:
        state.control_states[(stencil_index, checkpoint_index)] = (psi.copy(), phi.copy())
    elif branch_index == receipt_only_index:
        control = state.control_states.get((stencil_index, checkpoint_index))
        if control is None or not (
            np.array_equal(psi, control[0]) and np.array_equal(phi, control[1])
        ):
            state.receipt_only_control = False

    metrics_contract = require_object(protocol["metrics"], "metrics")
    row = checkpoint_metrics(
        stencil_index=stencil_index,
        branch_index=branch_index,
        checkpoint_index=checkpoint_index,
        step=record["step"],
        psi=psi,
        phi=phi,
        prepared=state.prepared_metrics[stencil_index],
        geometry=_observer_geometry(grid_size, profile_length),
        profile_length=profile_length,
        energy_denominator_floor=_denominator_floor(
            metrics_contract["energy_relative_error_denominator"],
            "energy denominator",
        ),
        profile_denominator_floor=_denominator_floor(
            metrics_contract["profile_relative_l2_denominator"],
            "profile denominator",
        ),
    )
    primary_rows = state.primary["checkpoint_metrics"]
    primary_row = primary_rows[len(state.recomputed_checkpoint_rows)]
    compare_exact(row, primary_row, state.audit, "checkpoint")
    state.recomputed_checkpoint_rows.append(row)
    state.checkpoint_by_key[(stencil_index, branch_index, checkpoint_index)] = row


def _process_step_energy(state: EvidenceState, record: Mapping[str, Any]) -> None:
    key = (record["stencil_index"], record["branch_index"])
    thresholds = state.protocol["thresholds"]
    if key not in state.energy:
        pre_total = state.prepared_metrics[key[0]]["total_psi_energy"]
        state.energy[key] = EnergyAccumulator(pre_total=pre_total)
    state.energy[key].add(
        record["step"],
        record["total_psi_energy"],
        require_float(thresholds["whole_trajectory_psi_energy_lower_ratio"], "lower ratio"),
        require_float(thresholds["whole_trajectory_psi_energy_upper_ratio"], "upper ratio"),
    )


def _process_step_telemetry(state: EvidenceState, record: Mapping[str, Any]) -> None:
    key = (record["stencil_index"], record["branch_index"])
    accumulator = state.telemetry.setdefault(key, TelemetryAccumulator())
    accumulator.add(record)
    if record["undeclared_source_detected"]:
        state.proposal_fidelity = False


def _compare_computed_float(
    computed: float, retained: float, state: EvidenceState, category: str
) -> bool:
    if computed != retained:
        state.audit.mismatch(category)
        return False
    return True


def _process_local_receipt(state: EvidenceState, record: Mapping[str, Any]) -> None:
    thresholds = state.protocol["thresholds"]
    multiplier = require_float(
        thresholds["local_and_global_aggregate_receipt_multiplier"], "receipt multiplier"
    )
    grid_size = require_int(state.protocol["baseline"]["grid_size"], "grid size")
    state.local_receipt_count += 1
    counts_ok = (
        record["positive_cell_count"]
        + record["negative_cell_count"]
        + record["zero_cell_count"]
        == grid_size * grid_size
    )
    aggregate_residual = record["sum_proxy_after"] - record["sum_proxy_before"]
    aggregate_scale = max(
        1.0,
        abs(record["sum_proxy_before"]),
        abs(record["sum_proxy_after"]),
        record["sum_abs_accepted_signed_work"],
    )
    residual_match = _compare_computed_float(
        aggregate_residual, record["aggregate_residual"], state, "aggregate_receipt"
    )
    scale_match = _compare_computed_float(
        aggregate_scale, record["aggregate_scale"], state, "aggregate_receipt"
    )
    aggregate_fields_match = residual_match and scale_match
    aggregate_pass = (
        record["precondition_passed"]
        and counts_ok
        and record["rejected_positive_work_sum"] >= 0.0
        and record["sum_abs_accepted_signed_work"]
        >= abs(record["accepted_signed_work_sum"])
        and abs(aggregate_residual) <= multiplier * aggregate_scale
    )
    flat_index = record["argmax_flat_index"]
    witness_residual = record["argmax_proxy_after"] - record["argmax_proxy_before"]
    witness_scale = max(
        1.0,
        abs(record["argmax_proxy_before"]),
        abs(record["argmax_proxy_after"]),
        abs(record["argmax_accepted_signed_work"]),
    )
    normalized = abs(witness_residual) / (multiplier * witness_scale)
    witness_residual_match = _compare_computed_float(
        witness_residual, record["argmax_residual"], state, "witness"
    )
    witness_scale_match = _compare_computed_float(
        witness_scale, record["argmax_scale"], state, "witness"
    )
    normalized_match = _compare_computed_float(
        normalized,
        record["max_cellwise_normalized_residual_ratio"],
        state,
        "witness",
    )
    witness_match = (
        record["argmax_row"] == flat_index // grid_size
        and record["argmax_column"] == flat_index % grid_size
        and witness_residual_match
        and witness_scale_match
        and normalized_match
    )
    witness_pass = (
        witness_match
        and 0 <= flat_index < grid_size * grid_size
        and normalized
        <= require_float(
            thresholds["local_cellwise_normalized_residual_ratio_max"],
            "local normalized residual maximum",
        )
    )
    if not (aggregate_fields_match and aggregate_pass):
        state.local_receipts = False
        if aggregate_fields_match:
            state.audit.mismatch("aggregate_receipt")
    if not witness_pass:
        state.local_receipts = False
        if witness_match:
            state.audit.mismatch("witness")


def _process_global_receipt(state: EvidenceState, record: Mapping[str, Any]) -> None:
    thresholds = state.protocol["thresholds"]
    multiplier = require_float(
        thresholds["local_and_global_aggregate_receipt_multiplier"], "receipt multiplier"
    )
    grid_size = require_int(state.protocol["baseline"]["grid_size"], "grid size")
    state.global_receipt_count += 1
    counts_ok = (
        record["positive_cell_count"]
        + record["negative_cell_count"]
        + record["zero_cell_count"]
        == grid_size * grid_size
    )
    residual = record["sum_proxy_after"] - record["sum_proxy_before"]
    scale = max(
        1.0,
        abs(record["sum_proxy_before"]),
        abs(record["sum_proxy_after"]),
        record["sum_abs_accepted_signed_work"],
    )
    expected_d = min(record["A"], record["P"])
    expected_q = 1.0 if record["P"] == 0.0 else expected_d / record["P"]
    expected_remaining = record["A"] - expected_d
    accepted_positive_total = 0.5 * (
        record["sum_abs_accepted_signed_work"]
        + record["accepted_signed_work_sum"]
    )
    calculated = (
        (residual, record["aggregate_residual"]),
        (scale, record["aggregate_scale"]),
        (expected_d, record["D"]),
        (expected_q, record["q"]),
        (expected_remaining, record["remaining"]),
        (record["P"] - expected_d, record["rejected_positive_work_sum"]),
    )
    arithmetic_match = True
    for computed, retained in calculated:
        arithmetic_match = (
            _compare_computed_float(
                computed, retained, state, "aggregate_receipt"
            )
            and arithmetic_match
        )
    arithmetic_pass = (
        record["precondition_passed"]
        and counts_ok
        and record["P"] >= 0.0
        and record["A"] >= 0.0
        and 0.0 <= record["D"] <= record["P"]
        and 0.0 <= record["q"] <= 1.0
        and record["remaining"] >= 0.0
        and record["sum_abs_accepted_signed_work"]
        >= abs(record["accepted_signed_work_sum"])
        and accepted_positive_total >= 0.0
        and abs(accepted_positive_total - record["D"]) <= multiplier * scale
        and (record["P"] == 0.0) == (record["positive_cell_count"] == 0)
        and (
            record["P"] != 0.0
            or (
                record["D"] == 0.0
                and record["rejected_positive_work_sum"] == 0.0
                and record["q"] == 1.0
            )
        )
        and abs(residual) <= multiplier * scale
        and record["max_abs_cellwise_residual"] >= 0.0
        and record["sum_abs_cellwise_residuals"] >= 0.0
        and record["sum_abs_cellwise_residuals"]
        >= record["max_abs_cellwise_residual"]
    )
    if not (arithmetic_match and arithmetic_pass):
        state.global_receipts = False
        if arithmetic_match:
            state.audit.mismatch("aggregate_receipt")


def _process_record(state: EvidenceState, record_type: str, record: Mapping[str, Any]) -> None:
    if record_type == "prepared_state":
        _process_prepared_state(state, record)
    elif record_type == "checkpoint_state":
        _process_checkpoint_state(state, record)
    elif record_type == "step_energy":
        _process_step_energy(state, record)
    elif record_type == "step_telemetry":
        _process_step_telemetry(state, record)
    elif record_type == "local_stage_receipt":
        _process_local_receipt(state, record)
    elif record_type == "global_stage_receipt":
        _process_global_receipt(state, record)
    else:
        _fail("unknown evidence record type")


def _stream_one_shard(
    repository_root: Path,
    protocol: Mapping[str, Any],
    primary: Mapping[str, Any],
    expected: ShardIdentity,
    shard_index: int,
    state: EvidenceState,
) -> ShardIdentity:
    """Validate, hash, and recompute one shard in one bounded-memory pass."""

    path = repository_root / expected.path
    size = path.stat().st_size
    byte_cap = require_int(
        protocol["retention"]["evidence_max_shard_bytes"], "evidence byte cap"
    )
    if size >= byte_cap:
        _fail("retained evidence shard is not below the frozen byte cap")
    sha256 = hashlib.sha256()
    git_hash = hashlib.sha1(usedforsecurity=False)
    git_hash.update(f"blob {size}\0".encode("ascii"))
    count = 0
    first_index: int | None = None
    last_index: int | None = None
    with path.open("rb") as handle:
        for line in handle:
            sha256.update(line)
            git_hash.update(line)
            if not line.endswith(b"\n") or line == b"\n" or b"\r" in line:
                _fail("evidence JSONL line ending or blank-line violation")
            if count == 0 and line.startswith(b"\xef\xbb\xbf"):
                _fail("evidence JSONL BOM is forbidden")
            record = require_object(strict_json_loads(line[:-1]), "evidence record")
            if canonical_payload_bytes(record) + b"\n" != line:
                _fail("evidence JSONL record is not exact canonical JSON")
            record_type, descriptor = _expected_record_descriptor(
                protocol, shard_index, count
            )
            global_index = expected.first_record_index + count
            _validate_record(protocol, record, record_type, descriptor, global_index)
            if first_index is None:
                first_index = global_index
            last_index = global_index
            _process_record(state, record_type, record)
            count += 1
    if count != expected.record_count or first_index != expected.first_record_index:
        _fail("evidence shard record count or first index mismatch")
    if last_index != expected.last_record_index:
        _fail("evidence shard last index mismatch")
    actual = ShardIdentity(
        path=expected.path,
        bytes=size,
        sha256=sha256.hexdigest(),
        git_blob=git_hash.hexdigest(),
        record_count=count,
        first_record_index=first_index,
        last_record_index=last_index,
    )
    if actual != expected:
        _fail("retained evidence shard identity mismatch")
    primary_identity = primary["evidence_identity"]["shards"][shard_index]
    primary_expected = {
        "path": actual.path,
        "bytes": actual.bytes,
        "sha256": actual.sha256,
        "record_count": actual.record_count,
        "first_record_index": actual.first_record_index,
        "last_record_index": actual.last_record_index,
    }
    if not exact_value_equal(primary_identity, primary_expected):
        _fail("primary-recorded evidence shard identity mismatch")
    return actual


def stream_evidence_after_latch(
    repository_root: Path,
    protocol: Mapping[str, Any],
    primary: Mapping[str, Any],
    expected_shards: Sequence[ShardIdentity],
    audit: Audit,
) -> tuple[EvidenceState, tuple[ShardIdentity, ...]]:
    """Consume all six shards exactly once after the fixed receipt exists."""

    state = EvidenceState(protocol=protocol, primary=primary, audit=audit)
    actual: list[ShardIdentity] = []
    for shard_index, expected in enumerate(expected_shards):
        actual.append(
            _stream_one_shard(
                repository_root,
                protocol,
                primary,
                expected,
                shard_index,
                state,
            )
        )
    if len(state.recomputed_checkpoint_rows) != protocol["retention"]["primary_output_contract"]["checkpoint_metric_count"]:
        _fail("recomputed checkpoint metric count mismatch")
    expected_local = protocol["retention"]["evidence_record_schemas"]["local_stage_receipt"]["count"]
    expected_global = protocol["retention"]["evidence_record_schemas"]["global_stage_receipt"]["count"]
    if state.local_receipt_count != expected_local or state.global_receipt_count != expected_global:
        _fail("retained receipt count mismatch")
    return state, tuple(actual)


def recompute_energy_summaries(state: EvidenceState) -> list[dict[str, Any]]:
    maps = state.protocol["retention"]["evidence_index_maps"]
    rows: list[dict[str, Any]] = []
    for stencil_index in range(len(maps["stencil_index"])):
        for branch_index in range(len(maps["branch_index"])):
            accumulator = state.energy.get((stencil_index, branch_index))
            if accumulator is None or accumulator.count == 0:
                _fail("missing trajectory energy accumulator")
            row = {
                "stencil_index": stencil_index,
                "branch_index": branch_index,
                "record_count": accumulator.count,
                "pre_total_psi_energy": accumulator.pre_total,
                "minimum_total_psi_energy": accumulator.minimum,
                "maximum_total_psi_energy": accumulator.maximum,
                "minimum_energy_ratio": accumulator.minimum / accumulator.pre_total,
                "maximum_energy_ratio": accumulator.maximum / accumulator.pre_total,
                "first_lower_bound_violation_step": accumulator.first_lower,
                "first_upper_bound_violation_step": accumulator.first_upper,
            }
            claimed = state.primary["trajectory_energy_summaries"][len(rows)]
            compare_exact(row, claimed, state.audit, "energy")
            rows.append(row)
    return rows


def recompute_telemetry_summaries(state: EvidenceState) -> list[dict[str, Any]]:
    maps = state.protocol["retention"]["evidence_index_maps"]
    rows: list[dict[str, Any]] = []
    for stencil_index in range(len(maps["stencil_index"])):
        for branch_index in range(len(maps["branch_index"])):
            accumulator = state.telemetry.get((stencil_index, branch_index))
            if accumulator is None:
                _fail("missing telemetry accumulator")
            row = accumulator.as_row(stencil_index, branch_index)
            claimed = state.primary["technical_telemetry_summaries"][len(rows)]
            compare_exact(row, claimed, state.audit, "technical")
            rows.append(row)
    control_index = maps["branch_index"].index("CONTROL")
    receipt_index = maps["branch_index"].index("RECEIPT_ONLY")
    for stencil_index in range(len(maps["stencil_index"])):
        control = rows[stencil_index * len(maps["branch_index"]) + control_index]
        receipt = rows[stencil_index * len(maps["branch_index"]) + receipt_index]
        comparable_fields = [key for key in control if key not in {"branch_index"}]
        if any(control[key] != receipt[key] for key in comparable_fields):
            state.receipt_only_control = False
    return rows


def _comparison_row(
    *,
    comparison_index: int,
    comparison_kind: str,
    stencil_index: int,
    step: int,
    metric: str,
    reference_branch_index: int,
    candidate_branch_index: int,
    reference_value: float,
    candidate_value: float,
    absolute_tolerance: float,
    relative_tolerance: float,
) -> dict[str, Any]:
    tolerance = absolute_tolerance + relative_tolerance * max(
        abs(reference_value), abs(candidate_value)
    )
    improvement = reference_value - candidate_value
    return {
        "comparison_index": comparison_index,
        "comparison_kind": comparison_kind,
        "stencil_index": stencil_index,
        "step": step,
        "metric": metric,
        "reference_branch_index": reference_branch_index,
        "candidate_branch_index": candidate_branch_index,
        "reference_value": reference_value,
        "candidate_value": candidate_value,
        "tolerance": tolerance,
        "improvement": improvement,
        "passed": improvement > tolerance,
    }


def recompute_comparisons(state: EvidenceState) -> list[dict[str, Any]]:
    protocol = state.protocol
    maps = protocol["retention"]["evidence_index_maps"]
    branches = maps["branch_index"]
    checkpoints = maps["checkpoint_index"]
    thresholds = protocol["thresholds"]
    absolute = require_float(thresholds["comparison_absolute"], "comparison absolute")
    relative = require_float(thresholds["comparison_relative"], "comparison relative")
    horizons = require_list(thresholds["comparison_horizons"], "comparison horizons")
    control = branches.index("CONTROL")
    pair_both = branches.index("PAIR_BOTH")
    global_pool = branches.index("GLOBAL_POOL_PAIR_BOTH")
    rows: list[dict[str, Any]] = []
    control_metrics = (
        "psi_energy_relative_error",
        "psi_radial_profile_relative_l2_error",
    )
    for stencil_index in range(len(maps["stencil_index"])):
        for step in horizons:
            checkpoint_index = checkpoints.index(step)
            for metric in control_metrics:
                reference = state.checkpoint_by_key[(stencil_index, control, checkpoint_index)]
                candidate = state.checkpoint_by_key[(stencil_index, pair_both, checkpoint_index)]
                rows.append(
                    _comparison_row(
                        comparison_index=len(rows),
                        comparison_kind="pair_both_vs_control",
                        stencil_index=stencil_index,
                        step=step,
                        metric=metric,
                        reference_branch_index=control,
                        candidate_branch_index=pair_both,
                        reference_value=reference[metric],
                        candidate_value=candidate[metric],
                        absolute_tolerance=absolute,
                        relative_tolerance=relative,
                    )
                )
    for stencil_index in range(len(maps["stencil_index"])):
        for step in horizons:
            checkpoint_index = checkpoints.index(step)
            metric = "psi_radial_profile_relative_l2_error"
            reference = state.checkpoint_by_key[(stencil_index, global_pool, checkpoint_index)]
            candidate = state.checkpoint_by_key[(stencil_index, pair_both, checkpoint_index)]
            rows.append(
                _comparison_row(
                    comparison_index=len(rows),
                    comparison_kind="pair_both_vs_global_pool",
                    stencil_index=stencil_index,
                    step=step,
                    metric=metric,
                    reference_branch_index=global_pool,
                    candidate_branch_index=pair_both,
                    reference_value=reference[metric],
                    candidate_value=candidate[metric],
                    absolute_tolerance=absolute,
                    relative_tolerance=relative,
                )
            )
    if len(rows) != protocol["retention"]["primary_output_contract"]["comparison_count"]:
        _fail("recomputed comparison count mismatch")
    for actual, claimed in zip(rows, state.primary["comparisons"], strict=True):
        compare_exact(actual, claimed, state.audit, "comparison")
    return rows


def _telemetry_row_map(rows: Sequence[Mapping[str, Any]]) -> dict[tuple[int, int], Mapping[str, Any]]:
    return {(row["stencil_index"], row["branch_index"]): row for row in rows}


def _telemetry_clean(row: Mapping[str, Any]) -> bool:
    return all(
        row[field_name] == 0
        for field_name in (
            "psi_cap_contact_count",
            "phi_cap_contact_count",
            "destructive_reset_count",
            "nonfinite_detected_count",
            "negative_phi_input_detected_count",
            "undeclared_source_detected_count",
        )
    )


def _checkpoint_absolute_clean(row: Mapping[str, Any], thresholds: Mapping[str, Any]) -> bool:
    return bool(
        row["finite"]
        and row["psi_energy_relative_error"]
        <= require_float(thresholds["psi_energy_relative_error_max"], "energy error max")
        and row["psi_radial_profile_relative_l2_error"]
        <= require_float(
            thresholds["psi_radial_profile_relative_l2_max"], "psi profile max"
        )
        and row["phi_radial_profile_relative_l2_error"]
        <= require_float(
            thresholds["phi_radial_profile_relative_l2_max"], "phi profile max"
        )
        and row["half_energy_radius_absolute_change"]
        <= require_float(
            thresholds["half_energy_radius_change_max_cells"], "half radius max"
        )
        and row["fixed_center_displacement"]
        <= require_float(
            thresholds["center_displacement_from_fixed_grid_center_max_cells"],
            "center displacement max",
        )
        and row["energy_fraction_radius_6"]
        >= require_float(
            thresholds["energy_fraction_within_radius_6_min"], "radius six minimum"
        )
    )


def _branch_absolute_clean(
    state: EvidenceState,
    energy_rows: Sequence[Mapping[str, Any]],
    telemetry_rows: Sequence[Mapping[str, Any]],
    branch_index: int,
) -> bool:
    protocol = state.protocol
    maps = protocol["retention"]["evidence_index_maps"]
    thresholds = protocol["thresholds"]
    lower = require_float(thresholds["whole_trajectory_psi_energy_lower_ratio"], "lower ratio")
    upper = require_float(thresholds["whole_trajectory_psi_energy_upper_ratio"], "upper ratio")
    checkpoint_steps = require_list(
        thresholds["absolute_clean_gate_checkpoints"], "absolute clean checkpoints"
    )
    telemetry_map = _telemetry_row_map(telemetry_rows)
    energy_map = {
        (row["stencil_index"], row["branch_index"]): row for row in energy_rows
    }
    for stencil_index in range(len(maps["stencil_index"])):
        envelope = energy_map[(stencil_index, branch_index)]
        if not (
            envelope["minimum_energy_ratio"] >= lower
            and envelope["maximum_energy_ratio"] <= upper
        ):
            return False
        if not _telemetry_clean(telemetry_map[(stencil_index, branch_index)]):
            return False
        for step in checkpoint_steps:
            checkpoint_index = maps["checkpoint_index"].index(step)
            row = state.checkpoint_by_key[(stencil_index, branch_index, checkpoint_index)]
            if not _checkpoint_absolute_clean(row, thresholds):
                return False
    return True


def _control_phenotype(state: EvidenceState) -> bool:
    protocol = state.protocol
    maps = protocol["retention"]["evidence_index_maps"]
    thresholds = protocol["thresholds"]
    control_index = maps["branch_index"].index("CONTROL")
    final_checkpoint = maps["checkpoint_index"].index(
        require_int(protocol["baseline"]["continuation_steps"], "continuation steps")
    )
    return all(
        not _checkpoint_absolute_clean(
            state.checkpoint_by_key[(stencil_index, control_index, final_checkpoint)],
            thresholds,
        )
        for stencil_index in range(len(maps["stencil_index"]))
    )


def recompute_gates(
    state: EvidenceState,
    *,
    source_identity_truth: bool,
    runtime_truth: bool,
    energy_rows: Sequence[Mapping[str, Any]],
    telemetry_rows: Sequence[Mapping[str, Any]],
    comparisons: Sequence[Mapping[str, Any]],
) -> dict[str, bool]:
    maps = state.protocol["retention"]["evidence_index_maps"]
    branches = maps["branch_index"]
    telemetry_clean = all(_telemetry_clean(row) for row in telemetry_rows)
    pair_both = branches.index("PAIR_BOTH")
    global_pool = branches.index("GLOBAL_POOL_PAIR_BOTH")
    control_comparisons = [
        row for row in comparisons if row["comparison_kind"] == "pair_both_vs_control"
    ]
    global_comparisons = [
        row
        for row in comparisons
        if row["comparison_kind"] == "pair_both_vs_global_pool"
    ]
    gates = {
        "identity": source_identity_truth,
        "runtime": runtime_truth,
        "serialization": True,
        "starting_clones": state.starting_clones,
        "receipt_only_control": state.receipt_only_control,
        "proposal_fidelity": state.proposal_fidelity,
        "technical_telemetry": telemetry_clean,
        "local_receipts": state.local_receipts,
        "global_receipts": state.global_receipts,
        "control_phenotype": _control_phenotype(state),
        "pair_both_absolute_clean": _branch_absolute_clean(
            state, energy_rows, telemetry_rows, pair_both
        ),
        "pair_both_causal_improvement": all(row["passed"] for row in control_comparisons),
        "local_advantage": all(row["passed"] for row in global_comparisons),
        "global_pool_absolute_clean": _branch_absolute_clean(
            state, energy_rows, telemetry_rows, global_pool
        ),
    }
    claimed = require_object(state.primary["gates"], "primary gates")
    compare_exact(gates, claimed, state.audit, "gate")
    if claimed["technical_telemetry"] != telemetry_clean:
        state.audit.mismatch("technical")
    return gates


def classify_from_protocol(
    protocol: Mapping[str, Any],
    gates: Mapping[str, bool],
    comparisons: Sequence[Mapping[str, Any]],
) -> str:
    """Derive the outcome only from the frozen ordered map and recomputed gates."""

    outcomes = require_list(protocol["outcome_map"], "outcome map")
    technical_gate_names = (
        "identity",
        "runtime",
        "serialization",
        "starting_clones",
        "receipt_only_control",
        "proposal_fidelity",
        "technical_telemetry",
        "local_receipts",
        "global_receipts",
        "control_phenotype",
    )
    if not all(gates[name] for name in technical_gate_names):
        return outcomes[0]
    clean_causal = (
        gates["control_phenotype"]
        and gates["pair_both_absolute_clean"]
        and gates["pair_both_causal_improvement"]
    )
    if clean_causal and gates["local_advantage"]:
        return outcomes[1]
    if clean_causal:
        return outcomes[2]
    control_rows = [
        row for row in comparisons if row["comparison_kind"] == "pair_both_vs_control"
    ]
    if any(row["passed"] for row in control_rows):
        return outcomes[3]
    return outcomes[4]


def build_checker_output(
    *,
    protocol: Mapping[str, Any],
    protocol_identity: FileIdentity,
    primary_identity: FileIdentity,
    shard_identities: Sequence[ShardIdentity],
    gate: ProgramGate,
    state: EvidenceState,
    source_identity_truth: bool,
    runtime_truth: bool,
) -> dict[str, Any]:
    """Finish all independent work before reading the primary's claimed outcome."""

    energy_rows = recompute_energy_summaries(state)
    telemetry_rows = recompute_telemetry_summaries(state)
    comparisons = recompute_comparisons(state)
    gates = recompute_gates(
        state,
        source_identity_truth=source_identity_truth,
        runtime_truth=runtime_truth,
        energy_rows=energy_rows,
        telemetry_rows=telemetry_rows,
        comparisons=comparisons,
    )
    recomputed_outcome = classify_from_protocol(protocol, gates, comparisons)

    classification = require_object(state.primary["classification"], "primary classification")
    primary_claimed_outcome = require_string(
        classification["outcome"], "primary claimed outcome"
    )
    if primary_claimed_outcome not in protocol["outcome_map"]:
        _fail("primary claimed outcome is outside the frozen outcome map")
    primary_claim_only = require_bool(
        classification["primary_claim_only"], "primary claim-only flag"
    )
    outcome_agrees = recomputed_outcome == primary_claimed_outcome
    if not outcome_agrees:
        state.audit.mismatch_count += 1
    if not primary_claim_only:
        state.audit.mismatch_count += 1

    limitations = require_list(
        protocol["retention"]["checker_limitations"], "checker limitations"
    )
    payload = {
        "schema": CHECKER_SCHEMA,
        "checker_id": gate.as_dict(),
        "protocol_identity": {
            "path": protocol_identity.path,
            "schema": FROZEN_PROTOCOL_SCHEMA,
            "bytes": protocol_identity.bytes,
            "sha256": protocol_identity.sha256,
            "git_blob": protocol_identity.git_blob,
        },
        "input_identity": {
            "protocol": protocol_identity.as_dict(),
            "primary": primary_identity.as_dict(),
            "shards": [identity.as_dict() for identity in shard_identities],
        },
        "structural_validation": {
            "passed": True,
            "canonical_primary": True,
            "canonical_shards": True,
            "exact_schema": True,
            "exact_record_order": True,
            "exact_counts": True,
            "hashes_match": True,
        },
        "recomputed": {
            "checkpoint_metrics_match": state.audit.checkpoint_metrics_match,
            "trajectory_energy_summaries_match": state.audit.trajectory_energy_summaries_match,
            "technical_gate_conditionally_applied": state.audit.technical_gate_conditionally_applied,
            "aggregate_receipt_arithmetic_passed": state.audit.aggregate_receipt_arithmetic_passed,
            "retained_witness_arithmetic_passed": state.audit.retained_witness_arithmetic_passed,
            "comparison_rows_match": state.audit.comparison_rows_match,
            "gate_map_match": state.audit.gate_map_match,
        },
        "agreement": {
            "passed": state.audit.mismatch_count == 0,
            "mismatch_count": state.audit.mismatch_count,
        },
        "conditional_outcome": {
            "recomputed_outcome": recomputed_outcome,
            "primary_claimed_outcome": primary_claimed_outcome,
            "agrees": outcome_agrees,
        },
        "limitations": list(limitations),
        "claim_boundary": dict(protocol["claim_boundary"]),
    }
    return payload_with_self_hash(payload)


def _empty_stderr_identity() -> dict[str, Any]:
    return {
        "bytes": 0,
        "sha256": hashlib.sha256(b"").hexdigest(),
        "status_summary": "empty",
    }


def canonical_failure_stderr_bytes(message: str) -> bytes:
    """Encode one sanitized failure line with an exact UTF-8 LF terminator."""

    return message.encode("utf-8", errors="strict") + b"\n"


def emit_failure_stderr(data: bytes, stream: Any | None = None) -> None:
    """Emit exact bytes when possible, with a deterministic text-stream fallback."""

    target = sys.stderr if stream is None else stream
    binary = getattr(target, "buffer", None)
    if binary is not None:
        binary.write(data)
        binary.flush()
        return
    target.write(data.decode("utf-8", errors="strict"))
    target.flush()


def _failure_stderr_identity(data: bytes) -> dict[str, Any]:
    return {
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "status_summary": "sanitized_failure_reported",
    }


def publish_checker_output(
    repository_root: Path, output: Mapping[str, Any]
) -> FileIdentity:
    """Publish once and require exact canonical-content readback before receipt finalization."""

    output_path = repository_root / CHECKER_OUTPUT_PATH
    expected_bytes = canonical_file_bytes(output)
    expected = FileIdentity(
        path=CHECKER_OUTPUT_PATH,
        bytes=len(expected_bytes),
        sha256=hashlib.sha256(expected_bytes).hexdigest(),
        git_blob=git_blob_digest(expected_bytes),
    )
    _atomic_replace_json(output_path, output)
    actual = file_identity(output_path, CHECKER_OUTPUT_PATH)
    if actual != expected:
        raise CheckerError("checker output readback identity mismatch")
    return actual


def execute_checker_once(
    repository_root: Path,
    protocol: Mapping[str, Any],
    protocol_identity: FileIdentity,
    bindings: InvocationBindings,
    gate: ProgramGate,
) -> dict[str, Any]:
    """Consume one-shot authority, stream retained evidence, and publish once."""

    started_at, start, program, inputs = create_attempt_latch(
        repository_root, gate, protocol_identity, bindings
    )
    receipt_path = repository_root / CHECKER_RECEIPT_PATH
    phase = "open_retained_primary"
    try:
        (
            primary,
            primary_identity_actual,
            source_identity_truth,
            runtime_truth,
        ) = load_primary_after_latch(
            repository_root,
            bindings.primary,
            protocol,
            protocol_identity,
        )
        phase = "validate_manifest_bindings"
        validate_manifest_after_latch(
            repository_root,
            protocol,
            protocol_identity,
            bindings,
        )
        audit = Audit()
        phase = "stream_retained_evidence"
        state, shard_identities = stream_evidence_after_latch(
            repository_root,
            protocol,
            primary,
            bindings.shards,
            audit,
        )
        phase = "recompute_and_classify"
        output = build_checker_output(
            protocol=protocol,
            protocol_identity=protocol_identity,
            primary_identity=primary_identity_actual,
            shard_identities=shard_identities,
            gate=gate,
            state=state,
            source_identity_truth=source_identity_truth,
            runtime_truth=runtime_truth,
        )
        phase = "publish_checker_output"
        output_identity = publish_checker_output(repository_root, output)
        phase = "finalize_receipt"
        elapsed = float(time.monotonic() - start)
        final_receipt = build_receipt(
            status="complete_output_retained",
            started_at=started_at,
            ended_at=_utc_now(),
            elapsed_seconds=elapsed,
            execution_commit=gate.actual_head_commit,
            program_identity=program,
            input_identity=inputs,
            output_identity={"checker_output": output_identity.as_dict()},
            stderr_identity=_empty_stderr_identity(),
            failure=None,
        )
        _atomic_replace_json(receipt_path, final_receipt, replace_existing=True)
        return output
    except BaseException as exc:
        sanitized = _sanitize_failure_message(str(exc) or type(exc).__name__, repository_root)
        stderr_payload = canonical_failure_stderr_bytes(sanitized)
        failure = {
            "phase": phase,
            "code": type(exc).__name__,
            "sanitized_message": sanitized,
        }
        failed_receipt = build_receipt(
            status="technical_non_result",
            started_at=started_at,
            ended_at=_utc_now(),
            elapsed_seconds=float(time.monotonic() - start),
            execution_commit=gate.actual_head_commit,
            program_identity=program,
            input_identity=inputs,
            output_identity=None,
            stderr_identity=_failure_stderr_identity(stderr_payload),
            failure=failure,
        )
        try:
            _atomic_replace_json(receipt_path, failed_receipt, replace_existing=True)
        except BaseException:
            pass
        raise


def argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Independently check one frozen Q2-M2-RWC1 retained primary and its six "
            "canonical JSONL evidence shards without rerunning a trajectory."
        )
    )
    parser.add_argument("--repository-root", type=Path, default=None)
    parser.add_argument("--expected-execution-commit", required=True)
    parser.add_argument("--remote-readback-commit", required=True)
    parser.add_argument("--expected-checker-git-blob", required=True)
    parser.add_argument("--expected-checker-test-git-blob", required=True)
    parser.add_argument("--expected-report-git-blob", required=True)
    parser.add_argument("--expected-manifest-git-blob", required=True)
    parser.add_argument("--expected-primary-bytes", type=int, required=True)
    parser.add_argument("--expected-primary-sha256", required=True)
    parser.add_argument("--expected-primary-git-blob", required=True)
    parser.add_argument(
        "--expected-shard-identity",
        action="append",
        default=[],
        metavar="BYTES:SHA256:GIT_BLOB",
        help="Repeat exactly six times in frozen protocol shard order.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = argument_parser()
    arguments = parser.parse_args(argv)
    default_root = Path(__file__).resolve().parents[2]
    repository_root = (
        arguments.repository_root.resolve()
        if arguments.repository_root is not None
        else default_root
    )
    try:
        protocol, protocol_identity = read_frozen_protocol(repository_root)
        bindings = build_invocation_bindings(arguments, protocol)
        gate = clean_preflight(repository_root, bindings, protocol, protocol_identity)
        execute_checker_once(
            repository_root,
            protocol,
            protocol_identity,
            bindings,
            gate,
        )
    except BaseException as exc:
        message = _sanitize_failure_message(str(exc) or type(exc).__name__, repository_root)
        emit_failure_stderr(canonical_failure_stderr_bytes(message))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
