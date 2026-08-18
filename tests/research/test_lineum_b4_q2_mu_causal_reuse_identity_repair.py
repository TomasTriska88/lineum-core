from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "research" / "runners" / "lineum_b4_q2_mu_causal_reuse.py"
SPEC = importlib.util.spec_from_file_location("lineum_b4_q2_m1_identity_repair", RUNNER_PATH)
assert SPEC is not None and SPEC.loader is not None
m1 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = m1
SPEC.loader.exec_module(m1)


FROZEN_PAYLOADS = {
    "lineum_core/math.py": b"VALUE = 1\nOTHER = 2\n",
    "requirements.txt": b"numpy==1.26.4\n",
    "requirements-dev.txt": b"pytest==9.1.1\n",
}


def _git(repository: Path, *arguments: str) -> str:
    completed = subprocess.run(
        ["git", *arguments],
        cwd=repository,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return completed.stdout.strip()


def _write(repository: Path, relative_path: str, payload: bytes) -> None:
    target = repository / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(payload)


def _crlf(payload: bytes) -> bytes:
    return payload.replace(b"\n", b"\r\n")


def _frozen_repository(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[
    Path, dict[str, str]
]:
    repository = tmp_path / "repository"
    repository.mkdir()
    _git(repository, "init", "--quiet")
    _git(repository, "config", "user.name", "Q2-M1 Repair Test")
    _git(repository, "config", "user.email", "q2-m1-repair@example.invalid")
    _git(repository, "config", "core.autocrlf", "true")
    for path, payload in FROZEN_PAYLOADS.items():
        _write(repository, path, payload)
    _git(repository, "add", "--", *FROZEN_PAYLOADS)
    _git(repository, "commit", "--quiet", "-m", "frozen sources")
    expected = {
        path: _git(repository, "rev-parse", f"HEAD:{path}")
        for path in FROZEN_PAYLOADS
    }
    monkeypatch.setattr(
        m1, "FROZEN_ENGINE_GIT_BLOB", expected["lineum_core/math.py"]
    )
    monkeypatch.setattr(
        m1, "FROZEN_REQUIREMENTS_GIT_BLOB", expected["requirements.txt"]
    )
    monkeypatch.setattr(
        m1,
        "FROZEN_REQUIREMENTS_DEV_GIT_BLOB",
        expected["requirements-dev.txt"],
    )
    return repository, expected


def test_crlf_worktree_passes_when_filtered_and_head_identities_are_frozen(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repository, expected = _frozen_repository(tmp_path, monkeypatch)
    for path, payload in FROZEN_PAYLOADS.items():
        _write(repository, path, _crlf(payload))
        assert m1.git_blob_sha1_file(repository / path) != expected[path]

    receipt = m1.verify_frozen_sources(repository)

    assert receipt["passed"] is True
    assert receipt["method"] == "git_filtered_worktree_and_head_blob"
    assert receipt["actual"] == expected
    assert receipt["head"] == expected


def test_semantic_worktree_change_fails_with_frozen_head(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repository, expected = _frozen_repository(tmp_path, monkeypatch)
    for path, payload in FROZEN_PAYLOADS.items():
        _write(repository, path, _crlf(payload))
    _write(repository, "requirements.txt", b"numpy==9.9.9\r\n")

    receipt = m1.verify_frozen_sources(repository)

    assert receipt["passed"] is False
    assert receipt["head"] == expected
    assert receipt["actual"]["requirements.txt"] != expected["requirements.txt"]


def test_committed_head_drift_fails_even_when_worktree_matches_frozen_content(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repository, expected = _frozen_repository(tmp_path, monkeypatch)
    _write(repository, "requirements.txt", b"numpy==9.9.9\n")
    _git(repository, "add", "--", "requirements.txt")
    _git(repository, "commit", "--quiet", "-m", "drift committed source")
    for path, payload in FROZEN_PAYLOADS.items():
        _write(repository, path, _crlf(payload))

    receipt = m1.verify_frozen_sources(repository)

    assert receipt["passed"] is False
    assert receipt["actual"] == expected
    assert receipt["head"]["requirements.txt"] != expected["requirements.txt"]


def test_missing_git_repository_fails_closed(
    tmp_path: Path,
) -> None:
    for path, payload in FROZEN_PAYLOADS.items():
        _write(tmp_path, path, payload)

    with pytest.raises(RuntimeError, match="Git source identity failed"):
        m1.verify_frozen_sources(tmp_path)
