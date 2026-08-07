from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECKER_PATH = ROOT / "research" / "runners" / "lineum_b4_q2_perturbation_ledger_check.py"
SPEC = importlib.util.spec_from_file_location("lineum_b4_q2_pv1_check", CHECKER_PATH)
assert SPEC is not None and SPEC.loader is not None
check = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = check
SPEC.loader.exec_module(check)

LANES = [
    "baseline",
    "no_hard_guards",
    "no_linear_dissipation",
    "no_explicit_tanh",
    "no_interaction_denominator",
    "no_mode_coupling",
    "no_phi_cap",
]
STENCILS = ["LAP4", "LAP8"]
PHI0 = [0.0, 1.0]
COLUMNS = [
    "case_key",
    "finite",
    "active_before_perturbation",
    "resets",
    "psi_cap_hits",
    "phi_cap_hits",
    "applicability",
    "e_inner",
    "e_annulus",
    "e_outer",
    "epsi_before",
    "pphi_before",
    "epsi_after",
    "direct_delta_epsi",
    "direct_delta_phi",
    "direct_delta_ledger",
    "relative_delta_epsi",
    "relative_delta_ledger",
    "analytic_delta_epsi",
    "analytic_direct_discrepancy",
    "absolute_relative_epsi_shift_over_frozen_5pct_tolerance",
    "ledger_neutral_within_numeric_tolerance",
]


def synthetic_payload() -> dict:
    rows = []
    neutral = 0
    non_neutral = 0
    active_count = 0
    inactive_count = 0
    for stencil_i, stencil in enumerate(STENCILS):
        for lane_i, lane in enumerate(LANES):
            for phi0 in PHI0:
                active = not (lane == "no_interaction_denominator" and phi0 == 1.0)
                e_inner = 2.0 + lane_i * 0.1 + stencil_i * 0.05
                e_annulus = 8.0 + phi0
                e_outer = 3.0
                pphi = 10.0 + phi0
                epsi_before = e_inner + e_annulus + e_outer
                if active:
                    epsi_after = 2.25 * e_inner + 0.25 * e_annulus + e_outer
                    analytic = 1.25 * e_inner - 0.75 * e_annulus
                    applicability = "perturbed_active"
                    active_count += 1
                else:
                    epsi_after = epsi_before
                    analytic = 0.0
                    applicability = "not_applicable_inactive"
                    inactive_count += 1
                direct = epsi_after - epsi_before
                delta_ledger = direct
                rel_epsi = direct / max(abs(epsi_before), 1e-30)
                ledger_before = epsi_before + pphi
                rel_ledger = direct / max(abs(ledger_before), 1e-30)
                neutral_label = None
                if active:
                    neutral_label = abs(delta_ledger) <= 1e-10 * max(1.0, abs(ledger_before))
                    if neutral_label:
                        neutral += 1
                    else:
                        non_neutral += 1
                rows.append([
                    f"{stencil}|{lane}|phi0={phi0:.1f}",
                    True,
                    active,
                    0,
                    0,
                    0,
                    applicability,
                    e_inner,
                    e_annulus,
                    e_outer,
                    epsi_before,
                    pphi,
                    epsi_after,
                    direct,
                    0.0,
                    delta_ledger,
                    rel_epsi,
                    rel_ledger,
                    analytic,
                    direct - analytic,
                    abs(rel_epsi) / 0.05,
                    neutral_label,
                ])
    return {
        "schema": "lineum-b4-q2-perturbation-ledger/1-retained-table",
        "stage": "Q2-PV1-A",
        "status": "primary_pending_independent_check",
        "columns": COLUMNS,
        "protocol": {
            "grid_size": 32,
            "primary_steps": 5000,
            "recovery_steps": 0,
            "stencils": STENCILS,
            "phi0_values": PHI0,
            "inner_factor": 1.5,
            "annulus_factor": 0.5,
            "numeric_rtol": 1e-10,
            "frozen_recovery_energy_tolerance": 0.05,
        },
        "pre_execution_gate": {
            "source_identity_checks_passed": True,
            "tests_passed": 16,
            "tests_failed": 0,
        },
        "source_execution": {
            "canonical_localized_runner_git_blob": check.EXPECTED_CANONICAL_RUNNER_BLOB,
            "q2_pv1_runner_git_blob": check.EXPECTED_PRIMARY_RUNNER_BLOB,
            "q2_pv1_test_git_blob": check.EXPECTED_PRIMARY_TEST_BLOB,
            "full_runtime_payload_sha256_without_self": "a" * 64,
            "runtime_output_file_sha256": "b" * 64,
            "workflow_run_id": 1,
            "workflow_job_id": 2,
            "workflow_source_commit": "c" * 40,
        },
        "summary": {
            "case_count": 28,
            "key_set_pass": True,
            "applicable_active_case_count": active_count,
            "inactive_not_applicable_case_count": inactive_count,
            "analytic_direct_all_pass": True,
            "ledger_neutral_applicable_count": neutral,
            "ledger_non_neutral_applicable_count": non_neutral,
            "all_applicable_cases_neutral": non_neutral == 0,
            "outcome": "non_neutral_detected" if non_neutral else "all_applicable_cases_neutral",
        },
        "rows": rows,
    }


def test_known_synthetic_payload_passes():
    result = check.check_payload(synthetic_payload())
    assert result["passed"] is True
    assert result["numeric_mismatch_count"] == 0
    assert result["categorical_mismatch_count"] == 0
    assert result["key_set_pass"] is True


def test_missing_case_fails_closed():
    payload = synthetic_payload()
    payload["rows"].pop()
    result = check.check_payload(payload)
    assert result["passed"] is False
    assert result["key_set_pass"] is False


def test_numeric_tamper_fails_closed():
    payload = synthetic_payload()
    payload["rows"][0][12] += 0.01
    result = check.check_payload(payload)
    assert result["passed"] is False
    assert result["numeric_mismatch_count"] >= 1


def test_category_tamper_fails_closed():
    payload = synthetic_payload()
    payload["rows"][0][21] = not payload["rows"][0][21]
    result = check.check_payload(payload)
    assert result["passed"] is False
    assert result["categorical_mismatch_count"] >= 1


def test_checker_has_no_primary_runner_import():
    source = CHECKER_PATH.read_text(encoding="utf-8")
    assert "import numpy" not in source
    assert "importlib" not in source
    assert "lineum_b4_q2_perturbation_ledger import" not in source
    assert "from lineum_b4_q2_perturbation_ledger" not in source


def test_roundoff_residual_difference_passes_when_both_paths_meet_frozen_analytic_gate():
    payload = synthetic_payload()
    row = payload["rows"][0]
    direct = abs(float(row[13]))
    analytic = abs(float(row[18]))
    tolerance = check.NUMERIC_RTOL * max(1.0, direct, analytic)
    row[19] = 0.5 * tolerance
    result = check.check_payload(payload)
    assert result["passed"] is True
    assert result["numeric_mismatch_count"] == 0
    assert result["analytic_agreement_failure_count"] == 0


def test_excessive_stored_analytic_residual_fails_closed():
    payload = synthetic_payload()
    row = payload["rows"][0]
    direct = abs(float(row[13]))
    analytic = abs(float(row[18]))
    tolerance = check.NUMERIC_RTOL * max(1.0, direct, analytic)
    row[19] = 2.0 * tolerance
    result = check.check_payload(payload)
    assert result["passed"] is False
    assert result["analytic_agreement_failure_count"] == 1
