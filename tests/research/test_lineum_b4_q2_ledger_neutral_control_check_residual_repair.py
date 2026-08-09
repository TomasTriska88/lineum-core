from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECKER_PATH = ROOT / "research" / "runners" / "lineum_b4_q2_ledger_neutral_control_check.py"
SPEC = importlib.util.spec_from_file_location("lineum_b4_q2_pv1b_check_residual_regression", CHECKER_PATH)
assert SPEC is not None and SPEC.loader is not None
check = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = check
SPEC.loader.exec_module(check)


def branch(case_key: str) -> dict:
    stencil, lane, phi0 = case_key.split("|")
    return {
        "case_key": case_key,
        "center_displacement": 0.0,
        "energy_error": 0.0,
        "energy_profile_error": 0.0,
        "finite": True,
        "full_recovery": False,
        "half_energy_radius_error": 0.0,
        "lane": lane,
        "phi0": float(phi0.split("=")[1]),
        "phi_one_sided_stationary": True,
        "phi_profile_error": 0.0,
        "primary_phi_cap_hits": 0,
        "primary_psi_cap_hits": 0,
        "primary_resets": 0,
        "psi_recovery": False,
        "recovery_phi_cap_hits": 0,
        "recovery_psi_cap_hits": 0,
        "recovery_resets": 0,
        "recovery_steps_completed": 1000,
        "reset_free": True,
        "stencil": stencil,
    }


def case(case_key: str, *, delta_ledger: float, ledger_tolerance: float) -> dict:
    ledger = {
        "delta_ledger": delta_ledger,
        "epsi_after": 100.0,
        "epsi_before": 100.0,
        "ledger_after": 1000.0 + delta_ledger,
        "ledger_before": 1000.0,
        "ledger_tolerance": ledger_tolerance,
        "neutral_within_numeric_tolerance": abs(delta_ledger) <= ledger_tolerance,
        "pphi_unchanged": 900.0,
    }
    return {
        "active_before_perturbation": True,
        "balanced": branch(case_key),
        "balanced_annulus_factor": 0.9,
        "canonical": branch(case_key),
        "case_key": case_key,
        "comparison": "both_q2_negative",
        "control_available": True,
        "perturbation_ledger": ledger,
    }


def test_raw_delta_difference_is_allowed_only_when_both_sides_are_within_frozen_tolerance():
    key = "LAP4|no_explicit_tanh|phi0=1.0"
    checker = case(key, delta_ledger=-4.76837158203125e-07, ledger_tolerance=0.4282901062646145)
    primary = case(key, delta_ledger=0.0, ledger_tolerance=0.4282901062646145)

    numeric, categorical, residual_failures = check.compare_case(checker, primary)

    assert numeric == []
    assert categorical == []
    assert residual_failures == []


def test_raw_delta_comparison_fails_closed_when_either_side_exceeds_its_frozen_tolerance():
    key = "LAP4|no_linear_dissipation|phi0=0.0"
    checker = case(key, delta_ledger=1.000001, ledger_tolerance=1.0)
    primary = case(key, delta_ledger=0.0, ledger_tolerance=1.0)

    numeric, categorical, residual_failures = check.compare_case(checker, primary)

    assert numeric == []
    assert categorical == []
    assert len(residual_failures) == 1
    assert residual_failures[0]["case_key"] == key
    assert residual_failures[0]["side"] == "checker"
    assert residual_failures[0]["delta_ledger"] == 1.000001
    assert residual_failures[0]["ledger_tolerance"] == 1.0
