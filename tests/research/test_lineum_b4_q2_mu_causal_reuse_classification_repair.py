from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "research" / "runners" / "lineum_b4_q2_mu_causal_reuse.py"
SPEC = importlib.util.spec_from_file_location("lineum_b4_q2_m1_classification_repair", RUNNER_PATH)
assert SPEC is not None and SPEC.loader is not None
m1 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = m1
SPEC.loader.exec_module(m1)


def _causal_summary(c0: float, c1: float, c2: float, c3: float) -> dict[str, dict]:
    def row(value: float) -> dict:
        return {
            "median_divergence": {"psi": value, "phi": 0.0, "mu": 0.0},
            "valid": True,
            "common_state_equal": True,
        }

    return {"C0": row(c0), "C1": row(c1), "C2": row(c2), "C3": row(c3)}


def test_failed_resolution_control_forces_inconclusive_before_passive_archive_label() -> None:
    result = m1.classify_primary(
        p0_valid=True,
        primary_histories_valid=True,
        cap_histories_valid=True,
        passive_mu_pass=True,
        cap_independence_pass=True,
        causal_summary=_causal_summary(
            0.0,
            6.308186615838749e-05,
            6.302829652263173e-05,
            3.360263121673625e-08,
        ),
        c3_cap_pass=True,
        full_grid_pass=True,
        c3_grid_pass=True,
        dt_control_pass=True,
        resolution_control_pass=False,
    )

    assert result["all_nuisance_pass"] is False
    assert result["mu_candidate_pass"] is False
    assert result["outcome"] == "inconclusive_or_confounded"
