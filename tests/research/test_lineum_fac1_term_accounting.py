from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

EXPECTED_MATH_BLOB = "bb877021810691223a0eb960a45493a2e351112a"
RUNNER = Path("research/runners/lineum_fac1_term_accounting.py")


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


def test_fac1_frozen_source_identity():
    assert _git_blob_sha(Path("lineum_core/math.py")) == EXPECTED_MATH_BLOB


def test_fac1_runner_reports_full_pass():
    out = _run()
    assert out["math_blob"] == EXPECTED_MATH_BLOB
    assert out["paired_mode"]["pass"] is True
    assert out["fallback_mode"]["pass"] is True
    assert out["overall_pass"] is True


def test_fac1_accounting_classifications_are_bounded():
    out = _run()
    assert out["physical_energy_claim"] == "not_established"
    assert out["new_state_required"] == "not_established"
    assert out["real_world_correspondence"] == "not_tested"
    assert out["ancient_physics_correspondence"] == "not_established"
    mode = out["paired_mode"]["terms"]["mode_coupling"]
    assert mode["qphi_credit"] > 0
    assert mode["qpsi_debit"] > 0
    assert mode["relative_abs_residual"] <= out["thresholds"]["paired_relative_residual_tolerance"]
    assert mode["residual_prediction_abs_error"] <= out["thresholds"]["pair_prediction_tolerance"]
