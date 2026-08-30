#!/usr/bin/env python3
"""Run the additive RWC1 retained-output checker successor exactly once.

This module repairs only the predecessor's tracked-text identity boundary.  It
verifies and then dynamically imports the frozen predecessor checker as the
scientific computation engine.  The predecessor's orchestration and terminal
paths are never used.
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
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType
from typing import Any, Mapping, NoReturn, Sequence


V4_PATH = (
    "research/lineum-public-tolog-b4/"
    "q2-m2-rwc1-checker-successor-preregistration.json"
)
V3_PATH = "research/lineum-public-tolog-b4/q2-m2-rwc1-preregistration.json"
PRIMARY_PATH = (
    "research/lineum-public-tolog-b4/q2-m2-rwc1-local-reciprocal-work.json"
)
BASE_CHECKER_PATH = (
    "research/runners/lineum_b4_q2_m2_rwc1_local_reciprocal_work_checker.py"
)
BASE_CHECKER_TEST_PATH = (
    "tests/research/test_lineum_b4_q2_m2_rwc1_local_reciprocal_work_checker.py"
)
SUCCESSOR_PATH = (
    "research/runners/"
    "lineum_b4_q2_m2_rwc1_local_reciprocal_work_checker_successor.py"
)
SUCCESSOR_TEST_PATH = (
    "tests/research/"
    "test_lineum_b4_q2_m2_rwc1_local_reciprocal_work_checker_successor.py"
)
REPORT_PATH = "research/lineum-public-tolog-galactic-shape-b4.md"
MANIFEST_PATH = "research/lineum-public-tolog-b4/artifact-manifest.json"
PREDECESSOR_RECEIPT_PATH = (
    "research/lineum-public-tolog-b4/q2-m2-rwc1-checker-execution-attempt-1.json"
)
PREDECESSOR_OUTPUT_PATH = (
    "research/lineum-public-tolog-b4/q2-m2-rwc1-independent-check.json"
)
SUCCESSOR_RECEIPT_PATH = (
    "research/lineum-public-tolog-b4/"
    "q2-m2-rwc1-checker-successor-execution-attempt-1.json"
)
SUCCESSOR_OUTPUT_PATH = (
    "research/lineum-public-tolog-b4/"
    "q2-m2-rwc1-independent-check-successor.json"
)

V4_SCHEMA = "lineum.q2-m2-rwc1-preregistration.v4"
V4_BYTES = 9149
V4_SHA256 = "a8a294d661c98d44c42822645fd85f592fd23eb972812d89f8ed5e67ecde0e09"
V4_GIT_BLOB = "44c170aac5c1d7b218bdfb70d2e4adf3f1382c40"
V4_REMOTE_COMMIT = "3bf120bc953cffdf535a8d03d38db89fb2d9b920"
V3_GIT_BLOB = "b6aea98ea752460f5283a40e7e68dea05a9c564a"
V3_REMOTE_COMMIT = "9b340097dd4d2aa8cc1c661e40e60811120ca22b"
PRIMARY_RESULT_COMMIT = "7db2b781260e70b214cb9a2bb8b52cfd34f5f602"
PREDECESSOR_RETENTION_COMMIT = "91a36a844d1000fcdbe9e7f3eb12a347fe75fecf"
BASE_CHECKER_GIT_BLOB = "25120ff1185e53a5ccc2ed3de01cfa43531eb21f"
BASE_CHECKER_TEST_GIT_BLOB = "b37252605666bc8eb008df530c4dcd5cbc08db2c"
PREDECESSOR_RECEIPT_GIT_BLOB = "5829d50dccbec53947cf422a943a153728d6713e"
REMOTE_REF = "refs/remotes/origin/codex/q2-m30-endogenous-balance-20260830"
MANIFEST_SCHEMA = "lineum-public-tolog-b4-readable-artifacts/4"
RECEIPT_SCHEMA = "lineum.q2-m2-rwc1-checker-successor-execution-receipt.v1"
LOWERCASE_GIT_BLOB = re.compile(r"[0-9a-f]{40}\Z")
LOWERCASE_COMMIT = re.compile(r"[0-9a-f]{40}\Z")


class SuccessorError(RuntimeError):
    """Raised when the successor cannot safely complete its frozen contract."""


class SuccessorContractError(SuccessorError):
    """Raised when an input violates the additive successor contract."""


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
class ShardIdentity(FileIdentity):
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
class InvocationBindings:
    execution_commit: str
    remote_readback_commit: str
    successor_git_blob: str
    successor_test_git_blob: str
    report_git_blob: str
    manifest_git_blob: str


@dataclass(frozen=True)
class SuccessorGate:
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
            "path": SUCCESSOR_PATH,
            "expected_git_blob": self.expected_checker_git_blob,
            "actual_filtered_git_blob": self.actual_checker_filtered_git_blob,
            "actual_head_git_blob": self.actual_checker_head_git_blob,
            "test_path": SUCCESSOR_TEST_PATH,
            "expected_test_git_blob": self.expected_checker_test_git_blob,
            "actual_test_filtered_git_blob": self.actual_checker_test_filtered_git_blob,
            "actual_test_head_git_blob": self.actual_checker_test_head_git_blob,
        }


@dataclass(frozen=True)
class Context:
    v4: dict[str, Any]
    v4_identity: FileIdentity
    protocol: dict[str, Any]
    protocol_identity: FileIdentity
    primary: FileIdentity
    shards: tuple[ShardIdentity, ...]
    base: ModuleType


def _fail(message: str) -> NoReturn:
    raise SuccessorContractError(message)


def _strict_json_loads(data: bytes) -> Any:
    def reject_constant(token: str) -> NoReturn:
        raise SuccessorContractError(f"non-finite JSON token {token}")

    def reject_duplicate(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise SuccessorContractError("duplicate JSON key")
            result[key] = value
        return result

    try:
        return json.loads(
            data,
            parse_constant=reject_constant,
            object_pairs_hook=reject_duplicate,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SuccessorContractError("invalid strict JSON") from exc


def _require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        _fail(f"{label} must be an object")
    return value


def _require_commit(value: str, label: str) -> str:
    if LOWERCASE_COMMIT.fullmatch(value) is None:
        _fail(f"{label} must be a lowercase commit")
    return value


def _require_git_blob(value: str, label: str) -> str:
    if LOWERCASE_GIT_BLOB.fullmatch(value) is None:
        _fail(f"{label} must be a lowercase Git blob")
    return value


def _git_blob_digest(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    digest = hashlib.sha1(usedforsecurity=False)
    digest.update(header)
    digest.update(data)
    return digest.hexdigest()


def _identity(path: str, data: bytes) -> FileIdentity:
    return FileIdentity(
        path=path,
        bytes=len(data),
        sha256=hashlib.sha256(data).hexdigest(),
        git_blob=_git_blob_digest(data),
    )


def _run_git_bytes(
    repository_root: Path,
    *arguments: str,
    input_bytes: bytes | None = None,
) -> bytes:
    try:
        completed = subprocess.run(
            ["git", *arguments],
            cwd=repository_root,
            input=input_bytes,
            check=False,
            capture_output=True,
        )
    except OSError as exc:
        raise SuccessorError("Git identity command could not start") from exc
    if completed.returncode != 0:
        raise SuccessorError("Git identity command failed")
    return completed.stdout


def _run_git_ascii(repository_root: Path, *arguments: str) -> str:
    try:
        value = _run_git_bytes(repository_root, *arguments).decode("ascii").strip()
    except UnicodeDecodeError as exc:
        raise SuccessorError("Git identity output is not ASCII") from exc
    return value


def _head_blob(repository_root: Path, relative_path: str) -> str:
    return _require_git_blob(
        _run_git_ascii(repository_root, "rev-parse", f"HEAD:{relative_path}"),
        "HEAD blob",
    )


def _index_blob(repository_root: Path, relative_path: str) -> str:
    return _require_git_blob(
        _run_git_ascii(repository_root, "rev-parse", f":{relative_path}"),
        "index blob",
    )


def _revision_blob(repository_root: Path, revision: str, relative_path: str) -> str:
    return _require_git_blob(
        _run_git_ascii(repository_root, "rev-parse", f"{revision}:{relative_path}"),
        "revision blob",
    )


def _filtered_blob_from_snapshot(
    repository_root: Path, relative_path: str, snapshot: bytes
) -> str:
    value = _run_git_ascii_with_input(
        repository_root,
        "hash-object",
        f"--path={relative_path}",
        "--stdin",
        input_bytes=snapshot,
    )
    return _require_git_blob(value, "Git-clean-filtered worktree blob")


def _run_git_ascii_with_input(
    repository_root: Path,
    *arguments: str,
    input_bytes: bytes,
) -> str:
    try:
        value = _run_git_bytes(
            repository_root, *arguments, input_bytes=input_bytes
        ).decode("ascii").strip()
    except UnicodeDecodeError as exc:
        raise SuccessorError("Git identity output is not ASCII") from exc
    return value


def _cat_blob(repository_root: Path, blob: str) -> bytes:
    _require_git_blob(blob, "committed blob")
    data = _run_git_bytes(repository_root, "cat-file", "blob", blob)
    if _git_blob_digest(data) != blob:
        raise SuccessorError("Git cat-file byte identity mismatch")
    return data


def _verify_tracked_path(
    repository_root: Path,
    relative_path: str,
    expected_blob: str,
    *,
    require_index: bool,
    snapshot: bytes | None = None,
) -> tuple[str, bytes]:
    expected = _require_git_blob(expected_blob, "expected tracked blob")
    head = _head_blob(repository_root, relative_path)
    if head != expected:
        raise SuccessorError("tracked HEAD identity mismatch")
    if require_index and _index_blob(repository_root, relative_path) != expected:
        raise SuccessorError("tracked index identity mismatch")
    data = (
        (repository_root / relative_path).read_bytes()
        if snapshot is None
        else snapshot
    )
    filtered = _filtered_blob_from_snapshot(repository_root, relative_path, data)
    if filtered != expected:
        raise SuccessorError("tracked worktree identity mismatch")
    return filtered, data


def _committed_identity(
    repository_root: Path, relative_path: str, expected_blob: str
) -> FileIdentity:
    data = _cat_blob(repository_root, expected_blob)
    result = _identity(relative_path, data)
    if result.git_blob != expected_blob:
        raise SuccessorError("committed identity mismatch")
    return result


def _validate_v4(v4: Mapping[str, Any]) -> None:
    if v4.get("schema") != V4_SCHEMA:
        _fail("successor protocol schema mismatch")
    if v4.get("role") != "successor_checker_authority_and_identity_domain_repair_only":
        _fail("successor protocol role mismatch")
    authority = _require_object(v4.get("authority"), "successor authority")
    exact_authority = {
        "predecessor_checker_authority_consumed": True,
        "predecessor_checker_retry_authorized": False,
        "successor_implementation_authorized": True,
        "successor_synthetic_tests_authorized": True,
        "successor_invocations_authorized": 1,
        "primary_invocations_authorized": 0,
        "trajectory_invocations_authorized": 0,
        "partner_message_authorized": False,
        "tolog_implementation_authorized": False,
    }
    for key, expected in exact_authority.items():
        if authority.get(key) != expected or type(authority.get(key)) is not type(expected):
            _fail("successor authority contract mismatch")
    planned = _require_object(v4.get("planned_paths"), "successor planned paths")
    if planned != {
        "successor_checker": SUCCESSOR_PATH,
        "successor_checker_test": SUCCESSOR_TEST_PATH,
        "successor_output": SUCCESSOR_OUTPUT_PATH,
        "successor_receipt": SUCCESSOR_RECEIPT_PATH,
    }:
        _fail("successor planned path mismatch")
    scientific = _require_object(v4.get("scientific_contract"), "scientific contract")
    if (
        scientific.get("computation_engine_git_blob") != BASE_CHECKER_GIT_BLOB
        or scientific.get("primary_or_trajectory_execution_permitted") is not False
        or scientific.get("monkeypatch_frozen_scientific_functions_permitted") is not False
    ):
        _fail("successor scientific contract mismatch")
    failures = _require_object(v4.get("failure_semantics"), "failure semantics")
    if (
        failures.get("exclusive_successor_latch_before_primary_or_shard_read") is not True
        or failures.get("successor_invocation_limit") != 1
        or failures.get("retry_authorized") is not False
    ):
        _fail("successor failure contract mismatch")


def _read_v4_from_committed_blob(repository_root: Path) -> tuple[dict[str, Any], FileIdentity]:
    data = _cat_blob(repository_root, V4_GIT_BLOB)
    identity = _identity(V4_PATH, data)
    if (
        identity.bytes != V4_BYTES
        or identity.sha256 != V4_SHA256
        or identity.git_blob != V4_GIT_BLOB
    ):
        raise SuccessorError("successor protocol identity mismatch")
    v4 = _require_object(_strict_json_loads(data), "successor protocol")
    _validate_v4(v4)
    return v4, identity


def _load_frozen_base(repository_root: Path, verified_source: bytes) -> ModuleType:
    """Execute the exact predecessor snapshot already verified by the caller."""

    path = repository_root / BASE_CHECKER_PATH
    module_name = "rwc1_frozen_checker_engine"
    module = ModuleType(module_name)
    module.__file__ = str(path)
    module.__package__ = ""
    sys.modules[module_name] = module
    try:
        code = compile(verified_source, str(path), "exec", dont_inherit=True)
        exec(code, module.__dict__)
    except BaseException:
        sys.modules.pop(module_name, None)
        raise
    forbidden = (
        "clean_preflight",
        "validate_manifest_after_latch",
        "create_attempt_latch",
        "execute_checker_once",
        "publish_checker_output",
        "main",
    )
    if any(not hasattr(module, name) for name in forbidden):
        raise SuccessorError("frozen checker surface mismatch")
    for required in (
        "load_primary_after_latch",
        "stream_evidence_after_latch",
        "build_checker_output",
        "Audit",
        "FileIdentity",
        "ShardIdentity",
        "ProgramGate",
        "strict_json_loads",
        "require_object",
        "_validate_manifest_file_entry",
        "validate_frozen_protocol",
        "validate_checker_runtime",
        "canonical_file_bytes",
    ):
        if not hasattr(module, required):
            raise SuccessorError("frozen checker engine lacks a required surface")
    return module


def _parse_context(repository_root: Path, base: ModuleType) -> Context:
    v4, v4_identity = _read_v4_from_committed_blob(repository_root)
    v3_data = _cat_blob(repository_root, V3_GIT_BLOB)
    protocol = base.require_object(base.strict_json_loads(v3_data), "protocol")
    base.validate_frozen_protocol(protocol)
    protocol_identity_local = _identity(V3_PATH, v3_data)
    protocol_identity = base.FileIdentity(
        protocol_identity_local.path,
        protocol_identity_local.bytes,
        protocol_identity_local.sha256,
        protocol_identity_local.git_blob,
    )
    retained = _require_object(v4.get("immutable_retained_inputs"), "retained inputs")
    primary_raw = _require_object(retained.get("primary"), "retained primary")
    primary = FileIdentity(
        path=str(primary_raw["path"]),
        bytes=int(primary_raw["bytes"]),
        sha256=str(primary_raw["sha256"]),
        git_blob=str(primary_raw["git_blob"]),
    )
    shards_raw = retained.get("shards")
    if not isinstance(shards_raw, list) or len(shards_raw) != 6:
        _fail("successor shard contract mismatch")
    shards = tuple(
        ShardIdentity(
            path=str(row["path"]),
            bytes=int(row["bytes"]),
            sha256=str(row["sha256"]),
            git_blob=str(row["git_blob"]),
            record_count=int(row["record_count"]),
            first_record_index=int(row["first_record_index"]),
            last_record_index=int(row["last_record_index"]),
        )
        for row in shards_raw
    )
    return Context(
        v4=v4,
        v4_identity=v4_identity,
        protocol=protocol,
        protocol_identity=protocol_identity,
        primary=primary,
        shards=shards,
        base=base,
    )


def _clean_status(repository_root: Path) -> str:
    return _run_git_ascii(
        repository_root, "status", "--porcelain", "--untracked-files=all"
    )


def clean_preflight(
    repository_root: Path, bindings: InvocationBindings
) -> tuple[SuccessorGate, Context]:
    for terminal in (SUCCESSOR_RECEIPT_PATH, SUCCESSOR_OUTPUT_PATH):
        if (repository_root / terminal).exists():
            raise SuccessorError("successor one-shot terminal path already exists")
    if (repository_root / PREDECESSOR_OUTPUT_PATH).exists():
        raise SuccessorError("predecessor output absence contract violated")
    if _clean_status(repository_root) != "":
        raise SuccessorError("successor worktree is not clean")

    head = _require_commit(_run_git_ascii(repository_root, "rev-parse", "HEAD"), "HEAD")
    remote = _require_commit(
        _run_git_ascii(repository_root, "rev-parse", "--verify", REMOTE_REF),
        "remote readback",
    )
    if (
        head != bindings.execution_commit
        or remote != bindings.remote_readback_commit
        or head != remote
    ):
        raise SuccessorError("clean HEAD does not equal fetched remote readback")
    for ancestor in (
        V4_REMOTE_COMMIT,
        V3_REMOTE_COMMIT,
        PRIMARY_RESULT_COMMIT,
        PREDECESSOR_RETENTION_COMMIT,
    ):
        completed = subprocess.run(
            ["git", "merge-base", "--is-ancestor", ancestor, head],
            cwd=repository_root,
            check=False,
            capture_output=True,
        )
        if completed.returncode != 0:
            raise SuccessorError("required frozen checkpoint is not an ancestor")

    expected_tracked = {
        SUCCESSOR_PATH: bindings.successor_git_blob,
        SUCCESSOR_TEST_PATH: bindings.successor_test_git_blob,
        REPORT_PATH: bindings.report_git_blob,
        MANIFEST_PATH: bindings.manifest_git_blob,
        V4_PATH: V4_GIT_BLOB,
        V3_PATH: V3_GIT_BLOB,
        BASE_CHECKER_PATH: BASE_CHECKER_GIT_BLOB,
        BASE_CHECKER_TEST_PATH: BASE_CHECKER_TEST_GIT_BLOB,
        PREDECESSOR_RECEIPT_PATH: PREDECESSOR_RECEIPT_GIT_BLOB,
    }
    filtered: dict[str, str] = {}
    snapshots: dict[str, bytes] = {}
    for path, expected in expected_tracked.items():
        filtered[path], snapshots[path] = _verify_tracked_path(
            repository_root, path, expected, require_index=True
        )

    # Delayed import occurs only after predecessor source and test are verified.
    base = _load_frozen_base(repository_root, snapshots[BASE_CHECKER_PATH])
    context = _parse_context(repository_root, base)
    base.validate_checker_runtime(context.protocol)

    for expected in (context.primary, *context.shards):
        if (
            _revision_blob(repository_root, "HEAD", expected.path) != expected.git_blob
            or _revision_blob(repository_root, PRIMARY_RESULT_COMMIT, expected.path)
            != expected.git_blob
        ):
            raise SuccessorError("retained input Git identity mismatch before latch")

    gate = SuccessorGate(
        expected_execution_commit=bindings.execution_commit,
        actual_head_commit=head,
        remote_readback_commit=remote,
        head_equals_remote_readback_commit=head == remote,
        worktree_clean=True,
        expected_checker_git_blob=bindings.successor_git_blob,
        actual_checker_filtered_git_blob=filtered[SUCCESSOR_PATH],
        actual_checker_head_git_blob=_head_blob(repository_root, SUCCESSOR_PATH),
        expected_checker_test_git_blob=bindings.successor_test_git_blob,
        actual_checker_test_filtered_git_blob=filtered[SUCCESSOR_TEST_PATH],
        actual_checker_test_head_git_blob=_head_blob(
            repository_root, SUCCESSOR_TEST_PATH
        ),
    )
    return gate, context


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _canonical_payload_bytes(payload: Mapping[str, Any]) -> bytes:
    try:
        return json.dumps(
            payload,
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise SuccessorError("payload cannot be canonically encoded") from exc


def _with_self_hash(payload: Mapping[str, Any]) -> dict[str, Any]:
    result = dict(payload)
    result.pop("canonical_payload_sha256_without_self", None)
    result["canonical_payload_sha256_without_self"] = hashlib.sha256(
        _canonical_payload_bytes(result)
    ).hexdigest()
    return result


def _canonical_file_bytes(payload: Mapping[str, Any]) -> bytes:
    return _canonical_payload_bytes(payload) + b"\n"


def _exclusive_create(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "wb") as handle:
        handle.write(_canonical_file_bytes(payload))
        handle.flush()
        os.fsync(handle.fileno())


def _atomic_replace(path: Path, payload: Mapping[str, Any]) -> None:
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(_canonical_file_bytes(payload))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _program_identity(gate: SuccessorGate) -> dict[str, Any]:
    return {
        "successor": {
            "path": SUCCESSOR_PATH,
            "git_blob": gate.expected_checker_git_blob,
            "test_path": SUCCESSOR_TEST_PATH,
            "test_git_blob": gate.expected_checker_test_git_blob,
        },
        "delegated_frozen_engine": {
            "path": BASE_CHECKER_PATH,
            "git_blob": BASE_CHECKER_GIT_BLOB,
            "test_path": BASE_CHECKER_TEST_PATH,
            "test_git_blob": BASE_CHECKER_TEST_GIT_BLOB,
        },
    }


def _input_identity(context: Context) -> dict[str, Any]:
    return {
        "successor_protocol": context.v4_identity.as_dict(),
        "scientific_protocol": context.protocol_identity.as_dict(),
        "primary": context.primary.as_dict(),
        "shards": [item.as_dict() for item in context.shards],
        "predecessor_receipt": {
            "path": PREDECESSOR_RECEIPT_PATH,
            "git_blob": PREDECESSOR_RECEIPT_GIT_BLOB,
            "status": "technical_non_result",
            "retry_authorized": False,
        },
    }


def _receipt(
    *,
    status: str,
    started_at: str,
    ended_at: str | None,
    elapsed_seconds: float | None,
    gate: SuccessorGate,
    context: Context,
    output_identity: Mapping[str, Any] | None,
    failure: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _with_self_hash(
        {
            "schema": RECEIPT_SCHEMA,
            "protocol_id": V4_SCHEMA,
            "lane": "checker_successor",
            "attempt": 1,
            "invocation_limit": 1,
            "authority_consumed": True,
            "retry_authorized": False,
            "predecessor_authority_consumed": True,
            "predecessor_retry_authorized": False,
            "predecessor_receipt_path": PREDECESSOR_RECEIPT_PATH,
            "status": status,
            "started_at": started_at,
            "ended_at": ended_at,
            "elapsed_seconds": elapsed_seconds,
            "execution_commit": gate.actual_head_commit,
            "program_identity": _program_identity(gate),
            "input_identity": _input_identity(context),
            "output_identity": output_identity,
            "failure": failure,
        }
    )


def create_successor_latch(
    repository_root: Path, gate: SuccessorGate, context: Context
) -> tuple[str, float]:
    started_at = _utc_now()
    start = time.monotonic()
    latch = _receipt(
        status="started",
        started_at=started_at,
        ended_at=None,
        elapsed_seconds=None,
        gate=gate,
        context=context,
        output_identity=None,
        failure=None,
    )
    _exclusive_create(repository_root / SUCCESSOR_RECEIPT_PATH, latch)
    return started_at, start


def _post_latch_status_is_allowed(status: str) -> bool:
    """Allow the latch plus a representation-only manifest worktree marker.

    Git may report a tracked JSON file as modified when its raw checkout uses
    mixed line endings even though the path-aware clean-filtered blob is still
    identical to HEAD.  The filtered identity is verified immediately below;
    staged manifest changes and every other worktree change remain forbidden.
    """

    rows = status.replace("\\", "/").splitlines()
    required = f"?? {SUCCESSOR_RECEIPT_PATH}"
    allowed = {required, f" M {MANIFEST_PATH}"}
    return required in rows and len(rows) == len(set(rows)) and set(rows) <= allowed


def _verify_post_latch_repository(
    repository_root: Path,
    bindings: InvocationBindings,
    gate: SuccessorGate,
    manifest_snapshot: bytes,
) -> None:
    head = _require_commit(_run_git_ascii(repository_root, "rev-parse", "HEAD"), "HEAD")
    remote = _require_commit(
        _run_git_ascii(repository_root, "rev-parse", "--verify", REMOTE_REF),
        "remote readback",
    )
    if head != gate.actual_head_commit or remote != gate.remote_readback_commit:
        raise SuccessorError("repository commit changed after latch")
    status = _run_git_bytes(
        repository_root, "status", "--porcelain", "--untracked-files=all"
    ).decode("utf-8")
    if not _post_latch_status_is_allowed(status):
        raise SuccessorError("unexpected repository state after latch")
    expected_tracked = {
        SUCCESSOR_PATH: bindings.successor_git_blob,
        SUCCESSOR_TEST_PATH: bindings.successor_test_git_blob,
        REPORT_PATH: bindings.report_git_blob,
        MANIFEST_PATH: bindings.manifest_git_blob,
        V4_PATH: V4_GIT_BLOB,
        V3_PATH: V3_GIT_BLOB,
        BASE_CHECKER_PATH: BASE_CHECKER_GIT_BLOB,
        BASE_CHECKER_TEST_PATH: BASE_CHECKER_TEST_GIT_BLOB,
        PREDECESSOR_RECEIPT_PATH: PREDECESSOR_RECEIPT_GIT_BLOB,
    }
    for path, expected in expected_tracked.items():
        snapshot = manifest_snapshot if path == MANIFEST_PATH else None
        _verify_tracked_path(
            repository_root,
            path,
            expected,
            require_index=False,
            snapshot=snapshot,
        )


def validate_manifest_after_latch(
    repository_root: Path,
    bindings: InvocationBindings,
    gate: SuccessorGate,
    context: Context,
) -> None:
    # Read once. The exact same bytes are filtered and parsed.
    manifest_snapshot = (repository_root / MANIFEST_PATH).read_bytes()
    _verify_post_latch_repository(
        repository_root, bindings, gate, manifest_snapshot
    )
    base = context.base
    manifest = base.require_object(
        base.strict_json_loads(manifest_snapshot), "manifest"
    )
    if manifest.get("schema") != MANIFEST_SCHEMA:
        _fail("manifest schema mismatch")
    if manifest.get("source_report") != REPORT_PATH:
        _fail("manifest source report path mismatch")
    q2 = base.require_object(manifest.get("q2_m2_rwc1"), "manifest q2_m2_rwc1")
    if q2.get("continuity_report_git_blob") != bindings.report_git_blob:
        _fail("manifest continuity report identity mismatch")
    if (
        q2.get("successor_checker_preregistration_path") != V4_PATH
        or q2.get("successor_checker_preregistration_schema") != V4_SCHEMA
        or q2.get("successor_checker_source_path") != SUCCESSOR_PATH
        or q2.get("successor_checker_test_path") != SUCCESSOR_TEST_PATH
        or q2.get("successor_checker_receipt_path") != SUCCESSOR_RECEIPT_PATH
        or q2.get("successor_checker_output_path") != SUCCESSOR_OUTPUT_PATH
    ):
        _fail("manifest successor routing mismatch")
    if (
        q2.get("successor_checker_invocations_authorized") != 1
        or q2.get("successor_checker_invocations_consumed") != 0
        or q2.get("successor_checker_retry_authorized") is not False
        or q2.get("successor_primary_invocations_authorized") != 0
        or q2.get("successor_trajectory_invocations_authorized") != 0
    ):
        _fail("manifest successor authority mismatch")
    if q2.get("protocol_path") != V3_PATH:
        _fail("manifest scientific protocol routing mismatch")
    if q2.get("primary_output_path") != PRIMARY_PATH:
        _fail("manifest primary routing mismatch")
    if q2.get("evidence_shards") != len(context.shards):
        _fail("manifest evidence shard count mismatch")

    files = base.require_object(manifest.get("files"), "manifest files")
    tracked_rows = {
        V4_PATH: V4_GIT_BLOB,
        V3_PATH: V3_GIT_BLOB,
        BASE_CHECKER_PATH: BASE_CHECKER_GIT_BLOB,
        BASE_CHECKER_TEST_PATH: BASE_CHECKER_TEST_GIT_BLOB,
        SUCCESSOR_PATH: bindings.successor_git_blob,
        SUCCESSOR_TEST_PATH: bindings.successor_test_git_blob,
    }
    for path, expected in tracked_rows.items():
        local = _committed_identity(repository_root, path, expected)
        identity = base.FileIdentity(
            local.path, local.bytes, local.sha256, local.git_blob
        )
        schema = V4_SCHEMA if path == V4_PATH else None
        base._validate_manifest_file_entry(files, identity, schema=schema)

    primary = base.FileIdentity(
        context.primary.path,
        context.primary.bytes,
        context.primary.sha256,
        context.primary.git_blob,
    )
    base._validate_manifest_file_entry(files, primary, schema=base.PRIMARY_SCHEMA)
    for item in context.shards:
        shard = base.ShardIdentity(
            item.path,
            item.bytes,
            item.sha256,
            item.git_blob,
            item.record_count,
            item.first_record_index,
            item.last_record_index,
        )
        base._validate_manifest_file_entry(files, shard, shard=shard)


def _base_file_identity(base: ModuleType, identity: FileIdentity) -> Any:
    return base.FileIdentity(
        identity.path, identity.bytes, identity.sha256, identity.git_blob
    )


def _base_shard_identity(base: ModuleType, identity: ShardIdentity) -> Any:
    return base.ShardIdentity(
        identity.path,
        identity.bytes,
        identity.sha256,
        identity.git_blob,
        identity.record_count,
        identity.first_record_index,
        identity.last_record_index,
    )


def _base_gate(base: ModuleType, gate: SuccessorGate) -> SuccessorGate:
    """Duck-type the frozen builder while preserving successor path provenance."""

    del base
    return gate


def _publish_output(
    repository_root: Path, base: ModuleType, output: Mapping[str, Any]
) -> FileIdentity:
    data = base.canonical_file_bytes(output)
    expected = _identity(SUCCESSOR_OUTPUT_PATH, data)
    path = repository_root / SUCCESSOR_OUTPUT_PATH
    if path.exists():
        raise SuccessorError("refusing to overwrite successor output")
    _exclusive_create(path, output)
    actual = _identity(SUCCESSOR_OUTPUT_PATH, path.read_bytes())
    if actual != expected:
        raise SuccessorError("successor output readback identity mismatch")
    return actual


def _sanitize_failure(message: str, repository_root: Path) -> str:
    text = message.replace(str(repository_root), "<repository-root>")
    text = text.replace("\r", " ").replace("\n", " ").strip()
    return text[:500] or "successor checker failed"


def execute_successor_once(
    repository_root: Path,
    bindings: InvocationBindings,
    gate: SuccessorGate,
    context: Context,
) -> dict[str, Any]:
    started_at, start = create_successor_latch(repository_root, gate, context)
    receipt_path = repository_root / SUCCESSOR_RECEIPT_PATH
    phase = "open_retained_primary"
    try:
        base = context.base
        primary, primary_identity, source_truth, runtime_truth = (
            base.load_primary_after_latch(
                repository_root,
                _base_file_identity(base, context.primary),
                context.protocol,
                context.protocol_identity,
            )
        )
        phase = "validate_manifest_bindings"
        validate_manifest_after_latch(
            repository_root, bindings, gate, context
        )
        phase = "stream_retained_evidence"
        audit = base.Audit()
        state, shard_identities = base.stream_evidence_after_latch(
            repository_root,
            context.protocol,
            primary,
            tuple(_base_shard_identity(base, item) for item in context.shards),
            audit,
        )
        phase = "recompute_and_classify"
        output = base.build_checker_output(
            protocol=context.protocol,
            protocol_identity=context.protocol_identity,
            primary_identity=primary_identity,
            shard_identities=shard_identities,
            gate=_base_gate(base, gate),
            state=state,
            source_identity_truth=source_truth,
            runtime_truth=runtime_truth,
        )
        phase = "publish_successor_output"
        output_identity = _publish_output(repository_root, base, output)
        final = _receipt(
            status="complete_output_retained",
            started_at=started_at,
            ended_at=_utc_now(),
            elapsed_seconds=float(time.monotonic() - start),
            gate=gate,
            context=context,
            output_identity={"successor_output": output_identity.as_dict()},
            failure=None,
        )
        _atomic_replace(receipt_path, final)
        return output
    except BaseException as exc:
        failure = {
            "phase": phase,
            "code": type(exc).__name__,
            "sanitized_message": _sanitize_failure(
                str(exc) or type(exc).__name__, repository_root
            ),
        }
        failed = _receipt(
            status="technical_non_result",
            started_at=started_at,
            ended_at=_utc_now(),
            elapsed_seconds=float(time.monotonic() - start),
            gate=gate,
            context=context,
            output_identity=None,
            failure=failure,
        )
        try:
            _atomic_replace(receipt_path, failed)
        except BaseException:
            pass
        raise


def argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run the additive one-shot RWC1 retained-output checker successor "
            "without rerunning a trajectory."
        )
    )
    parser.add_argument("--repository-root", type=Path, default=None)
    parser.add_argument("--expected-execution-commit", required=True)
    parser.add_argument("--remote-readback-commit", required=True)
    parser.add_argument("--expected-successor-git-blob", required=True)
    parser.add_argument("--expected-successor-test-git-blob", required=True)
    parser.add_argument("--expected-report-git-blob", required=True)
    parser.add_argument("--expected-manifest-git-blob", required=True)
    return parser


def build_bindings(arguments: argparse.Namespace) -> InvocationBindings:
    return InvocationBindings(
        execution_commit=_require_commit(
            arguments.expected_execution_commit, "execution commit"
        ),
        remote_readback_commit=_require_commit(
            arguments.remote_readback_commit, "remote readback commit"
        ),
        successor_git_blob=_require_git_blob(
            arguments.expected_successor_git_blob, "successor blob"
        ),
        successor_test_git_blob=_require_git_blob(
            arguments.expected_successor_test_git_blob, "successor test blob"
        ),
        report_git_blob=_require_git_blob(
            arguments.expected_report_git_blob, "report blob"
        ),
        manifest_git_blob=_require_git_blob(
            arguments.expected_manifest_git_blob, "manifest blob"
        ),
    )


def main(argv: Sequence[str] | None = None) -> int:
    arguments = argument_parser().parse_args(argv)
    default_root = Path(__file__).resolve().parents[2]
    repository_root = (
        arguments.repository_root.resolve()
        if arguments.repository_root is not None
        else default_root
    )
    try:
        bindings = build_bindings(arguments)
        gate, context = clean_preflight(repository_root, bindings)
        execute_successor_once(repository_root, bindings, gate, context)
    except BaseException as exc:
        message = _sanitize_failure(
            str(exc) or type(exc).__name__, repository_root
        )
        sys.stderr.write(message + "\n")
        sys.stderr.flush()
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
