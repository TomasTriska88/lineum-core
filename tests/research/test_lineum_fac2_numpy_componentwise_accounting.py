from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

EXPECTED_MATH_BLOB = "bb877021810691223a0eb960a45493a2e351112a"
RUNNER = Path("research/runners/lineum_fac2_numpy_componentwise_accounting.py")


def _git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def _run() -> dict:
    proc = subprocess.run(
        [sys.executable, str(RUNNER)],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(proc.stdout)


def test_fac2_r1_frozen_source_identity():
    assert _git_blob_sha(Path("lineum_core/math.py")) == EXPECTED_MATH_BLOB


def test_fac2_r1_runner_reports_full_pass():
    out = _run()
    assert out["math_blob"] == EXPECTED_MATH_BLOB
    assert out["scope"] == "current_numpy_diffusion_step_only"
    assert out["overall_pass"] is True
    assert all(branch["pass"] is True for branch in out["branches"].values())
    assert all(value is True for value in out["specific_checks"].values())


def test_fac2_r1_claims_remain_bounded():
    out = _run()
    assert out["physical_energy_claim"] == "not_established"
    assert out["new_state_required"] == "not_established"
    assert out["real_world_correspondence"] == "not_tested"
    assert out["ancient_physics_correspondence"] == "not_established"
    classes = out["classifications_if_passed"]
    assert classes["fac2_full_cross_backend_status"] == "not_complete_requires_separate_pytorch_wave_pml_fold_decision"
    assert classes["pml_in_numpy_diffusion_path"] == "not_implemented_flag_has_no_state_effect"
    assert classes["fold_in_numpy_diffusion_path"] == "not_implemented_flags_have_no_state_effect"


def test_fac2_r1_guard_and_source_controls_are_exercised():
    out = _run()
    guard = out["branches"]["guard_stress"]
    counts = guard["diagnostics"]["guard_counts"]
    assert counts["psi_cap_after_drift"] > 0
    assert counts["phi_clip"] > 0
    assert counts["mu_clip"] > 0
    assert counts["psi_fail_safe_reset"] is True
    source = out["branches"]["stochastic_paired"]["diagnostics"]["receipts"]["psi_source_plus_interaction"]
    assert source["source_increment_l2"] >= out["thresholds"]["minimum_signal"]
    assert source["linon_count"] > 0
