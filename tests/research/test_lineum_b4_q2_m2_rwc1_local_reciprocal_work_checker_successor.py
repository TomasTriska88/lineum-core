from __future__ import annotations

import ast
import hashlib
import importlib.util
import inspect
import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


ROOT = Path(__file__).resolve().parents[2]
SOURCE_PATH = (
    ROOT
    / "research/runners/"
    "lineum_b4_q2_m2_rwc1_local_reciprocal_work_checker_successor.py"
)


def _load_successor():
    spec = importlib.util.spec_from_file_location("rwc1_successor_under_test", SOURCE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


successor = _load_successor()


def _git(root: Path, *arguments: str, input_bytes: bytes | None = None) -> bytes:
    completed = subprocess.run(
        ["git", *arguments],
        cwd=root,
        input=input_bytes,
        check=True,
        capture_output=True,
    )
    return completed.stdout


def _temporary_repo(tmp_path: Path, data: bytes) -> tuple[Path, str, bytes]:
    root = tmp_path / "repo"
    root.mkdir()
    _git(root, "init", "-q")
    _git(root, "config", "user.email", "synthetic@example.invalid")
    _git(root, "config", "user.name", "Synthetic Test")
    _git(root, "config", "core.autocrlf", "true")
    relative = "tracked/metadata.json"
    path = root / relative
    path.parent.mkdir()
    path.write_bytes(data)
    _git(root, "add", "--", relative)
    _git(root, "commit", "-q", "-m", "synthetic metadata")
    blob = _git(root, "rev-parse", f"HEAD:{relative}").decode("ascii").strip()
    committed = _git(root, "cat-file", "blob", blob)
    return root, blob, committed


def test_successor_paths_and_authority_are_disjoint() -> None:
    terminals = {
        successor.PREDECESSOR_RECEIPT_PATH,
        successor.PREDECESSOR_OUTPUT_PATH,
        successor.SUCCESSOR_RECEIPT_PATH,
        successor.SUCCESSOR_OUTPUT_PATH,
    }
    assert len(terminals) == 4
    assert successor.RECEIPT_SCHEMA.endswith("successor-execution-receipt.v1")
    assert successor.V4_SCHEMA.endswith("preregistration.v4")
    assert successor.BASE_CHECKER_GIT_BLOB == (
        "25120ff1185e53a5ccc2ed3de01cfa43531eb21f"
    )


def test_source_has_no_static_science_import_or_forbidden_orchestration_call() -> None:
    source = SOURCE_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported.update(
        node.module or ""
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    )
    assert not any("local_reciprocal_work_checker" in name for name in imported)
    assert not any("local_reciprocal_work" in name for name in imported)
    assert not any("primary" in name.lower() for name in imported)
    assert not any(
        name in {"lineum_core", "lineum.core"}
        or name.startswith("lineum_core.")
        or name.startswith("lineum.core.")
        for name in imported
    )

    forbidden = {
        "clean_preflight",
        "validate_manifest_after_latch",
        "create_attempt_latch",
        "execute_checker_once",
        "publish_checker_output",
        "main",
    }
    base_calls = {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "base"
    }
    assert forbidden.isdisjoint(base_calls)
    assert "expected_outcome" not in source.lower()


def test_delayed_import_is_after_predecessor_verification_loop() -> None:
    source = inspect.getsource(successor.clean_preflight)
    tree = ast.parse(source)
    load_line = min(
        node.lineno
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "_load_frozen_base"
    )
    verify_lines = [
        node.lineno
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "_verify_tracked_path"
    ]
    assert verify_lines and max(verify_lines) < load_line
    assert source.index("BASE_CHECKER_PATH") < source.index("_load_frozen_base")
    assert source.index("BASE_CHECKER_TEST_PATH") < source.index("_load_frozen_base")


def test_frozen_engine_executes_verified_snapshot_without_reopening_path(
    tmp_path: Path,
) -> None:
    required = [
        "clean_preflight",
        "validate_manifest_after_latch",
        "create_attempt_latch",
        "execute_checker_once",
        "publish_checker_output",
        "main",
        "load_primary_after_latch",
        "stream_evidence_after_latch",
        "build_checker_output",
        "strict_json_loads",
        "require_object",
        "_validate_manifest_file_entry",
        "validate_frozen_protocol",
        "validate_checker_runtime",
        "canonical_file_bytes",
    ]
    lines = ["MARKER = 'verified-snapshot'", "class Audit: pass"]
    lines.extend(["class FileIdentity: pass", "class ShardIdentity: pass", "class ProgramGate: pass"])
    lines.extend(f"def {name}(*args, **kwargs): pass" for name in required)
    snapshot = ("\n".join(lines) + "\n").encode("utf-8")
    source = inspect.getsource(successor._load_frozen_base)
    assert "read_bytes" not in source
    module = successor._load_frozen_base(tmp_path, snapshot)
    assert module.MARKER == "verified-snapshot"


def test_mixed_eol_snapshot_uses_git_clean_identity(tmp_path: Path) -> None:
    canonical = b'{\n  "alpha": 1,\n  "beta": 2\n}\n'
    root, expected, committed = _temporary_repo(tmp_path, canonical)
    assert committed == canonical
    mixed = b'{\r\n  "alpha": 1,\n  "beta": 2\r\n}\n'
    path = root / "tracked/metadata.json"
    path.write_bytes(mixed)
    assert successor._git_blob_digest(mixed) != expected

    filtered, captured = successor._verify_tracked_path(
        root,
        "tracked/metadata.json",
        expected,
        require_index=True,
    )
    assert captured == mixed
    assert filtered == expected


def test_semantic_worktree_mutation_is_rejected(tmp_path: Path) -> None:
    canonical = b'{\n  "alpha": 1\n}\n'
    root, expected, _ = _temporary_repo(tmp_path, canonical)
    (root / "tracked/metadata.json").write_bytes(b'{\r\n  "alpha": 9\r\n}\r\n')
    with pytest.raises(successor.SuccessorError, match="worktree identity"):
        successor._verify_tracked_path(
            root,
            "tracked/metadata.json",
            expected,
            require_index=True,
        )


def test_preflight_identity_rejects_index_drift(tmp_path: Path) -> None:
    canonical = b'{\n  "alpha": 1\n}\n'
    root, expected, _ = _temporary_repo(tmp_path, canonical)
    path = root / "tracked/metadata.json"
    path.write_bytes(b'{\n  "alpha": 2\n}\n')
    _git(root, "add", "--", "tracked/metadata.json")
    path.write_bytes(canonical)
    with pytest.raises(successor.SuccessorError, match="index identity"):
        successor._verify_tracked_path(
            root,
            "tracked/metadata.json",
            expected,
            require_index=True,
        )


def test_preflight_identity_rejects_head_drift(tmp_path: Path) -> None:
    canonical = b'{\n  "alpha": 1\n}\n'
    root, expected, _ = _temporary_repo(tmp_path, canonical)
    path = root / "tracked/metadata.json"
    path.write_bytes(b'{\n  "alpha": 2\n}\n')
    _git(root, "add", "--", "tracked/metadata.json")
    _git(root, "commit", "-q", "-m", "changed head")
    path.write_bytes(canonical)
    with pytest.raises(successor.SuccessorError, match="HEAD identity"):
        successor._verify_tracked_path(
            root,
            "tracked/metadata.json",
            expected,
            require_index=True,
        )


def test_committed_identity_uses_cat_file_not_smudged_worktree(tmp_path: Path) -> None:
    canonical = b'{\n  "alpha": 1,\n  "beta": 2\n}\n'
    root, expected, committed = _temporary_repo(tmp_path, canonical)
    mixed = b'{\r\n  "alpha": 1,\n  "beta": 2\r\n}\n'
    (root / "tracked/metadata.json").write_bytes(mixed)
    identity = successor._committed_identity(
        root, "tracked/metadata.json", expected
    )
    assert identity.bytes == len(committed)
    assert identity.sha256 == hashlib.sha256(committed).hexdigest()
    assert identity.git_blob == expected
    assert identity.bytes != len(mixed)


def test_binary_cat_file_preserves_arbitrary_committed_bytes(tmp_path: Path) -> None:
    canonical = b"\x00\xff\r\nopaque\n"
    root, expected, committed = _temporary_repo(tmp_path, canonical)
    assert successor._cat_blob(root, expected) == committed
    assert successor._git_blob_digest(committed) == expected


def test_missing_git_repository_fails_closed(tmp_path: Path) -> None:
    with pytest.raises(successor.SuccessorError, match="Git identity command failed"):
        successor._head_blob(tmp_path, "missing.txt")


def test_exclusive_successor_latch_cannot_be_created_twice(tmp_path: Path) -> None:
    path = tmp_path / "receipt.json"
    payload = {"schema": "synthetic", "authority_consumed": True}
    successor._exclusive_create(path, payload)
    original = path.read_bytes()
    with pytest.raises(FileExistsError):
        successor._exclusive_create(path, payload)
    assert path.read_bytes() == original


def test_failure_receipt_is_successor_only_and_non_retryable() -> None:
    gate = successor.SuccessorGate(
        expected_execution_commit="a" * 40,
        actual_head_commit="a" * 40,
        remote_readback_commit="a" * 40,
        head_equals_remote_readback_commit=True,
        worktree_clean=True,
        expected_checker_git_blob="b" * 40,
        actual_checker_filtered_git_blob="b" * 40,
        actual_checker_head_git_blob="b" * 40,
        expected_checker_test_git_blob="c" * 40,
        actual_checker_test_filtered_git_blob="c" * 40,
        actual_checker_test_head_git_blob="c" * 40,
    )
    identity = successor.FileIdentity("synthetic.json", 3, "d" * 64, "e" * 40)
    context = successor.Context(
        v4={},
        v4_identity=identity,
        protocol={},
        protocol_identity=identity,
        primary=identity,
        shards=(),
        base=SimpleNamespace(),
    )
    receipt = successor._receipt(
        status="technical_non_result",
        started_at="2026-08-30T00:00:00Z",
        ended_at="2026-08-30T00:00:01Z",
        elapsed_seconds=1.0,
        gate=gate,
        context=context,
        output_identity=None,
        failure={"phase": "synthetic", "code": "Synthetic", "sanitized_message": "x"},
    )
    assert receipt["lane"] == "checker_successor"
    assert receipt["authority_consumed"] is True
    assert receipt["retry_authorized"] is False
    assert receipt["predecessor_retry_authorized"] is False
    assert receipt["predecessor_receipt_path"] == successor.PREDECESSOR_RECEIPT_PATH
    assert receipt["output_identity"] is None
    assert "canonical_payload_sha256_without_self" in receipt


def test_frozen_output_builder_receives_truthful_successor_path_identity() -> None:
    _, gate, _ = _synthetic_execution_objects()
    adapted = successor._base_gate(SimpleNamespace(ProgramGate=pytest.fail), gate)
    payload = adapted.as_dict()
    assert adapted is gate
    assert payload["path"] == successor.SUCCESSOR_PATH
    assert payload["test_path"] == successor.SUCCESSOR_TEST_PATH
    assert payload["expected_git_blob"] == gate.expected_checker_git_blob
    assert payload["expected_test_git_blob"] == gate.expected_checker_test_git_blob
    assert "expected_checker_git_blob" not in payload


def test_clean_preflight_has_no_direct_retained_file_reads() -> None:
    source = inspect.getsource(successor.clean_preflight)
    tree = ast.parse(source)
    path_reads = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in {"read_bytes", "open"}
    ]
    assert path_reads == []
    assert "_revision_blob" in source
    assert "context.primary" in source
    assert "context.shards" in source


def _synthetic_execution_objects():
    identity = successor.FileIdentity("synthetic.json", 3, "d" * 64, "e" * 40)
    gate = successor.SuccessorGate(
        expected_execution_commit="a" * 40,
        actual_head_commit="a" * 40,
        remote_readback_commit="a" * 40,
        head_equals_remote_readback_commit=True,
        worktree_clean=True,
        expected_checker_git_blob="b" * 40,
        actual_checker_filtered_git_blob="b" * 40,
        actual_checker_head_git_blob="b" * 40,
        expected_checker_test_git_blob="c" * 40,
        actual_checker_test_filtered_git_blob="c" * 40,
        actual_checker_test_head_git_blob="c" * 40,
    )
    bindings = successor.InvocationBindings(
        execution_commit="a" * 40,
        remote_readback_commit="a" * 40,
        successor_git_blob="b" * 40,
        successor_test_git_blob="c" * 40,
        report_git_blob="f" * 40,
        manifest_git_blob="1" * 40,
    )
    return identity, gate, bindings


def test_execute_successor_latches_before_all_delegated_science(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    identity, gate, bindings = _synthetic_execution_objects()
    events: list[str] = []

    class FakeBase:
        FileIdentity = successor.FileIdentity
        ShardIdentity = successor.ShardIdentity
        ProgramGate = successor.SuccessorGate

        class Audit:
            pass

        @staticmethod
        def load_primary_after_latch(*args, **kwargs):
            assert events == ["latch"]
            events.append("load_primary")
            return {}, identity, True, True

        @staticmethod
        def stream_evidence_after_latch(*args, **kwargs):
            events.append("stream")
            return object(), ()

        @staticmethod
        def build_checker_output(**kwargs):
            events.append("build")
            return {"schema": "synthetic-independent-check"}

    context = successor.Context(
        v4={},
        v4_identity=identity,
        protocol={},
        protocol_identity=identity,
        primary=identity,
        shards=(),
        base=FakeBase(),
    )

    def latch(*args, **kwargs):
        events.append("latch")
        return "2026-08-30T00:00:00Z", 0.0

    monkeypatch.setattr(successor, "create_successor_latch", latch)
    monkeypatch.setattr(
        successor,
        "validate_manifest_after_latch",
        lambda *args, **kwargs: events.append("manifest"),
    )
    monkeypatch.setattr(
        successor,
        "_publish_output",
        lambda *args, **kwargs: (events.append("publish") or identity),
    )
    finalized: list[dict] = []
    monkeypatch.setattr(
        successor,
        "_atomic_replace",
        lambda path, payload: finalized.append(dict(payload)),
    )
    monkeypatch.setattr(successor.time, "monotonic", lambda: 1.0)

    output = successor.execute_successor_once(
        tmp_path, bindings, gate, context
    )
    assert output["schema"] == "synthetic-independent-check"
    assert events == [
        "latch",
        "load_primary",
        "manifest",
        "stream",
        "build",
        "publish",
    ]
    assert finalized[-1]["status"] == "complete_output_retained"
    assert finalized[-1]["retry_authorized"] is False


def test_post_latch_failure_retains_successor_non_result_without_publish(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    identity, gate, bindings = _synthetic_execution_objects()
    events: list[str] = []

    class FailingBase:
        FileIdentity = successor.FileIdentity
        ShardIdentity = successor.ShardIdentity
        ProgramGate = successor.SuccessorGate

        @staticmethod
        def load_primary_after_latch(*args, **kwargs):
            events.append("load_primary")
            raise successor.SuccessorContractError("synthetic post-latch failure")

    context = successor.Context(
        v4={},
        v4_identity=identity,
        protocol={},
        protocol_identity=identity,
        primary=identity,
        shards=(),
        base=FailingBase(),
    )
    monkeypatch.setattr(
        successor,
        "create_successor_latch",
        lambda *args, **kwargs: (events.append("latch") or ("start", 0.0)),
    )
    monkeypatch.setattr(
        successor,
        "_publish_output",
        lambda *args, **kwargs: pytest.fail("output must not publish after failure"),
    )
    finalized: list[dict] = []
    monkeypatch.setattr(
        successor,
        "_atomic_replace",
        lambda path, payload: finalized.append(dict(payload)),
    )
    monkeypatch.setattr(successor.time, "monotonic", lambda: 1.0)

    with pytest.raises(successor.SuccessorContractError, match="synthetic"):
        successor.execute_successor_once(tmp_path, bindings, gate, context)
    assert events == ["latch", "load_primary"]
    assert finalized[-1]["status"] == "technical_non_result"
    assert finalized[-1]["retry_authorized"] is False
    assert finalized[-1]["failure"]["phase"] == "open_retained_primary"
    assert finalized[-1]["output_identity"] is None


def _write_relative(root: Path, relative: str, data: bytes) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _index_file_identity(root: Path, relative: str) -> successor.FileIdentity:
    blob = _git(root, "rev-parse", f":{relative}").decode("ascii").strip()
    data = _git(root, "cat-file", "blob", blob)
    return successor.FileIdentity(
        relative,
        len(data),
        hashlib.sha256(data).hexdigest(),
        blob,
    )


def _manifest_integration_fixture(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    root = tmp_path / "manifest-repo"
    root.mkdir()
    _git(root, "init", "-q")
    _git(root, "config", "user.email", "synthetic@example.invalid")
    _git(root, "config", "user.name", "Synthetic Test")
    _git(root, "config", "core.autocrlf", "true")

    base_source = (ROOT / successor.BASE_CHECKER_PATH).read_bytes()
    tracked_payloads = {
        successor.V4_PATH: (ROOT / successor.V4_PATH).read_bytes(),
        successor.V3_PATH: (ROOT / successor.V3_PATH).read_bytes(),
        successor.BASE_CHECKER_PATH: base_source,
        successor.BASE_CHECKER_TEST_PATH: (
            ROOT / successor.BASE_CHECKER_TEST_PATH
        ).read_bytes(),
        successor.SUCCESSOR_PATH: (ROOT / successor.SUCCESSOR_PATH).read_bytes(),
        successor.SUCCESSOR_TEST_PATH: (
            ROOT / successor.SUCCESSOR_TEST_PATH
        ).read_bytes(),
        successor.REPORT_PATH: b"synthetic report\n",
        successor.PREDECESSOR_RECEIPT_PATH: b'{"status":"technical_non_result"}\n',
    }
    for relative, data in tracked_payloads.items():
        _write_relative(root, relative, data)
    _git(root, "add", "--", *tracked_payloads.keys())

    identities = {
        relative: _index_file_identity(root, relative)
        for relative in tracked_payloads
    }
    predecessor_blob = identities[successor.PREDECESSOR_RECEIPT_PATH].git_blob
    monkeypatch.setattr(
        successor, "PREDECESSOR_RECEIPT_GIT_BLOB", predecessor_blob
    )

    primary_data = b'{"synthetic":"primary"}\n'
    primary = successor.FileIdentity(
        successor.PRIMARY_PATH,
        len(primary_data),
        hashlib.sha256(primary_data).hexdigest(),
        successor._git_blob_digest(primary_data),
    )
    shards = []
    first = 0
    for index in range(6):
        data = f'{{"synthetic_shard":{index}}}\n'.encode("ascii")
        count = index + 1
        shards.append(
            successor.ShardIdentity(
                path=(
                    "research/lineum-public-tolog-b4/"
                    f"synthetic-shard-{index}.jsonl"
                ),
                bytes=len(data),
                sha256=hashlib.sha256(data).hexdigest(),
                git_blob=successor._git_blob_digest(data),
                record_count=count,
                first_record_index=first,
                last_record_index=first + count - 1,
            )
        )
        first += count

    def row(identity: successor.FileIdentity, *, schema: str | None = None):
        result = {
            "bytes": identity.bytes,
            "sha256": identity.sha256,
            "git_blob_sha": identity.git_blob,
            "role": "synthetic",
        }
        if schema is not None:
            result["schema"] = schema
        return result

    files = {
        successor.V4_PATH: row(identities[successor.V4_PATH], schema=successor.V4_SCHEMA),
        successor.V3_PATH: row(identities[successor.V3_PATH]),
        successor.BASE_CHECKER_PATH: row(identities[successor.BASE_CHECKER_PATH]),
        successor.BASE_CHECKER_TEST_PATH: row(
            identities[successor.BASE_CHECKER_TEST_PATH]
        ),
        successor.SUCCESSOR_PATH: row(identities[successor.SUCCESSOR_PATH]),
        successor.SUCCESSOR_TEST_PATH: row(
            identities[successor.SUCCESSOR_TEST_PATH]
        ),
        successor.PRIMARY_PATH: row(primary, schema="lineum.q2-m2-rwc1-primary.v1"),
    }
    for shard in shards:
        files[shard.path] = {
            **row(shard),
            "record_count": shard.record_count,
            "first_record_index": shard.first_record_index,
            "last_record_index": shard.last_record_index,
        }

    manifest = {
        "schema": successor.MANIFEST_SCHEMA,
        "source_report": successor.REPORT_PATH,
        "files": files,
        "q2_m2_rwc1": {
            "continuity_report_git_blob": identities[successor.REPORT_PATH].git_blob,
            "successor_checker_preregistration_path": successor.V4_PATH,
            "successor_checker_preregistration_schema": successor.V4_SCHEMA,
            "successor_checker_source_path": successor.SUCCESSOR_PATH,
            "successor_checker_test_path": successor.SUCCESSOR_TEST_PATH,
            "successor_checker_receipt_path": successor.SUCCESSOR_RECEIPT_PATH,
            "successor_checker_output_path": successor.SUCCESSOR_OUTPUT_PATH,
            "successor_checker_invocations_authorized": 1,
            "successor_checker_invocations_consumed": 0,
            "successor_checker_retry_authorized": False,
            "successor_primary_invocations_authorized": 0,
            "successor_trajectory_invocations_authorized": 0,
            "protocol_path": successor.V3_PATH,
            "primary_output_path": successor.PRIMARY_PATH,
            "evidence_shards": 6,
        },
    }
    manifest_bytes = (
        json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False).encode("utf-8")
        + b"\n"
    )
    _write_relative(root, successor.MANIFEST_PATH, manifest_bytes)
    _git(root, "add", "--", successor.MANIFEST_PATH)
    manifest_identity = _index_file_identity(root, successor.MANIFEST_PATH)
    _git(root, "commit", "-q", "-m", "synthetic execution checkpoint")
    head = _git(root, "rev-parse", "HEAD").decode("ascii").strip()
    _git(root, "update-ref", successor.REMOTE_REF, head)

    # The durable successor receipt is the only allowed post-latch worktree change.
    _write_relative(root, successor.SUCCESSOR_RECEIPT_PATH, b'{"status":"started"}\n')

    # Recreate the diagnosed checkout shape: same filtered JSON, mixed raw EOLs.
    canonical_manifest = _git(
        root, "cat-file", "blob", manifest_identity.git_blob
    )
    lines = canonical_manifest.splitlines(keepends=True)
    mixed_manifest = b"".join(
        line[:-1] + (b"\r\n" if index % 2 else b"\n")
        for index, line in enumerate(lines)
    )
    _write_relative(root, successor.MANIFEST_PATH, mixed_manifest)
    assert successor._git_blob_digest(mixed_manifest) != manifest_identity.git_blob
    assert successor._filtered_blob_from_snapshot(
        root, successor.MANIFEST_PATH, mixed_manifest
    ) == manifest_identity.git_blob

    bindings = successor.InvocationBindings(
        execution_commit=head,
        remote_readback_commit=head,
        successor_git_blob=identities[successor.SUCCESSOR_PATH].git_blob,
        successor_test_git_blob=identities[successor.SUCCESSOR_TEST_PATH].git_blob,
        report_git_blob=identities[successor.REPORT_PATH].git_blob,
        manifest_git_blob=manifest_identity.git_blob,
    )
    gate = successor.SuccessorGate(
        expected_execution_commit=head,
        actual_head_commit=head,
        remote_readback_commit=head,
        head_equals_remote_readback_commit=True,
        worktree_clean=True,
        expected_checker_git_blob=bindings.successor_git_blob,
        actual_checker_filtered_git_blob=bindings.successor_git_blob,
        actual_checker_head_git_blob=bindings.successor_git_blob,
        expected_checker_test_git_blob=bindings.successor_test_git_blob,
        actual_checker_test_filtered_git_blob=bindings.successor_test_git_blob,
        actual_checker_test_head_git_blob=bindings.successor_test_git_blob,
    )
    base = successor._load_frozen_base(root, base_source)
    v4_identity = identities[successor.V4_PATH]
    protocol_identity = identities[successor.V3_PATH]
    context = successor.Context(
        v4={},
        v4_identity=v4_identity,
        protocol={},
        protocol_identity=protocol_identity,
        primary=primary,
        shards=tuple(shards),
        base=base,
    )
    return root, bindings, gate, context


def test_real_manifest_validator_accepts_mixed_eol_and_committed_rows(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, bindings, gate, context = _manifest_integration_fixture(
        tmp_path, monkeypatch
    )
    successor.validate_manifest_after_latch(root, bindings, gate, context)


def test_post_latch_manifest_semantic_drift_fails_before_any_stream(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, bindings, gate, context = _manifest_integration_fixture(
        tmp_path, monkeypatch
    )
    path = root / successor.MANIFEST_PATH
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["q2_m2_rwc1"]["evidence_shards"] = 5
    path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")
    with pytest.raises(successor.SuccessorError, match="worktree identity"):
        successor.validate_manifest_after_latch(root, bindings, gate, context)


def test_execute_failure_persists_canonical_successor_receipt_and_old_sentinel(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    identity, gate, bindings = _synthetic_execution_objects()
    old_path = tmp_path / successor.PREDECESSOR_RECEIPT_PATH
    old_path.parent.mkdir(parents=True)
    old_path.write_bytes(b"immutable-old-receipt\n")

    class FailingBase:
        FileIdentity = successor.FileIdentity
        ShardIdentity = successor.ShardIdentity
        ProgramGate = successor.SuccessorGate

        @staticmethod
        def load_primary_after_latch(*args, **kwargs):
            receipt = tmp_path / successor.SUCCESSOR_RECEIPT_PATH
            assert receipt.exists()
            raise successor.SuccessorContractError("synthetic retained-read failure")

    context = successor.Context(
        v4={},
        v4_identity=identity,
        protocol={},
        protocol_identity=identity,
        primary=identity,
        shards=(),
        base=FailingBase(),
    )
    with pytest.raises(successor.SuccessorContractError, match="synthetic"):
        successor.execute_successor_once(tmp_path, bindings, gate, context)
    receipt_path = tmp_path / successor.SUCCESSOR_RECEIPT_PATH
    retained = json.loads(receipt_path.read_text(encoding="utf-8"))
    assert retained["status"] == "technical_non_result"
    assert retained["authority_consumed"] is True
    assert retained["retry_authorized"] is False
    assert retained["output_identity"] is None
    assert not (tmp_path / successor.SUCCESSOR_OUTPUT_PATH).exists()
    assert old_path.read_bytes() == b"immutable-old-receipt\n"


def test_v4_machine_contract_is_strict_and_contains_no_result_value() -> None:
    protocol_path = ROOT / successor.V4_PATH
    protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    successor._validate_v4(protocol)
    assert protocol["authority"]["successor_invocations_authorized"] == 1
    assert protocol["authority"]["primary_invocations_authorized"] == 0
    assert protocol["authority"]["trajectory_invocations_authorized"] == 0
    assert protocol["failure_semantics"]["retry_authorized"] is False
    assert '"expected_outcome":' not in protocol_path.read_text(
        encoding="utf-8"
    ).lower()
