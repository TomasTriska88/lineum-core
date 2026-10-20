"""Regression tests for canonical audit profile selection and execution."""

import json
import sys
from pathlib import Path

from tools.whitepaper_contract import main, select_profile_result


def _profile_result(name: str, status: str, check_count: int) -> dict:
    return {
        "profile": name,
        "status": status,
        "checks": [{"status": status} for _ in range(check_count)],
    }


def _run_audit_fixture(tmp_path: Path, monkeypatch, *, steps: int, include_scope: bool):
    runs_root = tmp_path / "runs"
    run_dir = runs_root / f"spec6_false_s41_steps_{steps}"
    run_dir.mkdir(parents=True)

    manifest = {
        "run": {
            "run_id": 6,
            "run_tag": "spec6_false_s41",
            "seed": 41,
            "run_mode": "false",
            "param_tag": "",
            "kappa_mode": "constant",
            "low_noise_mode": False,
            "test_exhale_mode": True,
            "grid_size": 128,
            "steps": steps,
            "pixel_size_m": 1e-12,
            "time_step_s": 1e-21,
            "window_W": 256,
            "window_hop": 128,
        },
        "invariants": {"dim": "2D", "bcs": "periodic", "precision": "float64"},
        "metrics": {},
        "analysis_config": {},
        "spectral_pipeline": {},
        "logging": {},
    }
    if include_scope:
        manifest["audit_scope"] = {
            "expected_hash": "fixture-hash",
            "actual_hash": "fixture-hash",
        }

    (run_dir / "spec6_false_s41_manifest.json").write_text(
        json.dumps(manifest), encoding="utf-8"
    )
    (run_dir / "spec6_false_s41_metrics_summary.csv").write_text(
        "metric,value\n", encoding="utf-8"
    )

    contract = {
        "contract_id": "lineum-audit-profile-regression",
        "contract_version": "0.0.1",
        "constants": {},
        "profiles": [
            {
                "name": "baseline",
                "selectors": {},
                "checks": {
                    "invariants": {
                        "dim": "2D",
                        "bcs": "periodic",
                        "precision": "float64",
                    },
                    "required_artifacts": [
                        "*manifest.json",
                        "*metrics_summary.csv",
                    ],
                },
            },
            {
                "name": "canonical",
                "selectors": {"run_tag": "spec6_false_s41"},
                "checks": {
                    "identity": {
                        "seed": 41,
                        "steps": 2000,
                        "grid_size": 128,
                        "time_step_s": 1e-21,
                        "kappa_mode": "constant",
                    },
                    "required_artifacts": [
                        "*manifest.json",
                        "*metrics_summary.csv",
                    ],
                },
            },
        ],
    }
    contract_path = tmp_path / "contract.json"
    contract_path.write_text(json.dumps(contract), encoding="utf-8")

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "whitepaper_contract.py",
            "--run-dir",
            str(run_dir),
            "--runs-root",
            str(runs_root),
            "--contract",
            str(contract_path),
            "--strict",
        ],
    )

    try:
        main()
        exit_code = 0
    except SystemExit as exc:
        exit_code = int(exc.code or 0)

    suite_path = runs_root / "_whitepaper_contract" / "whitepaper_contract_suite.json"
    return exit_code, json.loads(suite_path.read_text(encoding="utf-8"))


def test_one_step_manifest_fails_canonical_even_when_baseline_passes(tmp_path, monkeypatch) -> None:
    exit_code, suite = _run_audit_fixture(
        tmp_path, monkeypatch, steps=1, include_scope=False
    )

    assert suite["summary"]["matched_canonical"] == 1
    assert suite["summary"]["canonical_pass"] == 0
    assert suite["summary"]["canonical_fail"] == 1
    assert suite["summary"]["pass"] == 0
    assert suite["summary"]["fail"] == 1
    assert exit_code == 1
    assert suite["runs"][0]["matched_profile"] == "canonical"
    assert suite["runs"][0]["status"] == "FAIL"
    assert any(
        check["id"] == "canonical.identity.steps" and check["status"] == "FAIL"
        for check in suite["runs"][0]["checks"]
    )


def test_two_thousand_step_manifest_uses_canonical_profile(tmp_path, monkeypatch) -> None:
    exit_code, suite = _run_audit_fixture(
        tmp_path, monkeypatch, steps=2000, include_scope=True
    )

    assert exit_code == 0
    assert suite["summary"]["matched_canonical"] == 1
    assert suite["summary"]["canonical_pass"] == 1
    assert suite["summary"]["canonical_fail"] == 0
    assert suite["summary"]["pass"] == 1
    assert suite["summary"]["fail"] == 0
    assert suite["runs"][0]["matched_profile"] == "canonical"
    assert suite["runs"][0]["status"] == "PASS"


def test_failed_canonical_profile_cannot_be_hidden_by_baseline_pass() -> None:
    baseline = _profile_result("baseline", "PASS", 5)
    canonical = _profile_result("canonical", "FAIL", 12)
    selected = select_profile_result([baseline, canonical])
    assert selected["profile"] == "canonical"
    assert selected["status"] == "FAIL"


def test_wave_core_pass_cannot_hide_canonical_failure() -> None:
    baseline = _profile_result("baseline", "PASS", 5)
    canonical = _profile_result("canonical", "FAIL", 12)
    wave_core = _profile_result("wave_core", "PASS", 13)
    selected = select_profile_result([baseline, canonical, wave_core])
    assert selected["profile"] == "canonical"
    assert selected["status"] == "FAIL"


def test_canonical_pass_remains_authoritative() -> None:
    baseline = _profile_result("baseline", "PASS", 5)
    canonical = _profile_result("canonical", "PASS", 12)
    wave_core = _profile_result("wave_core", "FAIL", 13)
    selected = select_profile_result([baseline, canonical, wave_core])
    assert selected["profile"] == "canonical"
    assert selected["status"] == "PASS"


def test_noncanonical_run_preserves_best_passing_profile() -> None:
    baseline = _profile_result("baseline", "PASS", 5)
    wave_core = _profile_result("wave_core", "PASS", 13)
    selected = select_profile_result([baseline, wave_core])
    assert selected["profile"] == "wave_core"
    assert selected["status"] == "PASS"


def test_noncanonical_run_falls_back_to_most_comprehensive_failure() -> None:
    baseline = _profile_result("baseline", "FAIL", 5)
    wave_core = _profile_result("wave_core", "FAIL", 13)
    selected = select_profile_result([baseline, wave_core])
    assert selected["profile"] == "wave_core"
    assert selected["status"] == "FAIL"
}
