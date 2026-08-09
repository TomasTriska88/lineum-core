from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CHECKER_PATH = (
    ROOT / "research" / "runners" / "lineum_b4_q2_ledger_neutral_control_check.py"
)
SPEC = importlib.util.spec_from_file_location("lineum_b4_q2_pv1b_check", CHECKER_PATH)
assert SPEC is not None and SPEC.loader is not None
check = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = check
SPEC.loader.exec_module(check)


def recovery_row(**updates):
    row = {
        "full_recovery": False,
        "finite": True,
        "reset_free": True,
        "primary_psi_cap_hits": 0,
        "recovery_psi_cap_hits": 0,
        "primary_phi_cap_hits": 0,
        "recovery_phi_cap_hits": 0,
    }
    row.update(updates)
    return row


def test_laplacians_annihilate_constant_field():
    field = np.ones((2, 7, 7), dtype=float)
    np.testing.assert_allclose(check.raw_laplacian(field, "LAP4"), 0.0)
    np.testing.assert_allclose(check.raw_laplacian(field, "LAP8"), 0.0)


def test_lap4_impulse_known_answer():
    field = np.zeros((1, 7, 7), dtype=float)
    field[0, 3, 3] = 1.0
    lap = check.raw_laplacian(field, "LAP4")
    assert lap[0, 3, 3] == -4.0
    assert lap[0, 2, 3] == 1.0
    assert lap[0, 4, 3] == 1.0
    assert lap[0, 3, 2] == 1.0
    assert lap[0, 3, 4] == 1.0
    np.testing.assert_allclose(np.sum(lap), 0.0)


def test_lap8_impulse_known_answer():
    field = np.zeros((1, 7, 7), dtype=float)
    field[0, 3, 3] = 1.0
    lap = check.raw_laplacian(field, "LAP8")
    assert lap[0, 3, 3] == -5.0
    assert lap[0, 2, 3] == 1.0
    assert lap[0, 2, 2] == 0.25
    np.testing.assert_allclose(np.sum(lap), 0.0)


def test_balanced_factor_known_answer_and_fail_closed():
    assert np.isclose(check.balanced_factor(2.0, 10.0), np.sqrt(0.75))
    assert check.balanced_factor(1.0, 0.0) is None
    assert check.balanced_factor(10.0, 1.0) is None


def test_perturbation_receipt_accepts_exact_balanced_control():
    psi = np.ones((9, 9), dtype=np.complex128)
    phi = np.full((9, 9), 2.0)
    radius = np.hypot(*(np.indices((9, 9), dtype=float) - 4.0))
    inner = radius <= 2.0
    annulus = (radius >= 3.0) & (radius <= 5.0)
    energy = np.abs(psi) ** 2
    factor = check.balanced_factor(
        float(np.sum(energy[inner])), float(np.sum(energy[annulus]))
    )
    assert factor is not None
    perturbed = psi.copy()
    perturbed[inner] *= 1.5
    perturbed[annulus] *= factor
    receipt = check.perturbation_receipt(psi, phi, perturbed)
    assert receipt["neutral_within_numeric_tolerance"] is True


def test_q2_admissibility_includes_caps_and_resets():
    assert check.q2_positive(recovery_row(full_recovery=True))
    assert not check.q2_positive(
        recovery_row(full_recovery=True, recovery_phi_cap_hits=1)
    )
    assert not check.q2_positive(
        recovery_row(full_recovery=True, primary_psi_cap_hits=1)
    )
    assert not check.q2_positive(recovery_row(full_recovery=True, reset_free=False))


def test_comparison_labels_are_frozen():
    negative = recovery_row()
    positive = recovery_row(full_recovery=True)
    assert check.comparison_label(negative, None) == "control_unavailable"
    assert (
        check.comparison_label(negative, positive)
        == "balanced_rescues_q2_classification"
    )
    assert check.comparison_label(negative, negative) == "both_q2_negative"
    assert check.comparison_label(positive, positive) == "both_q2_positive"
    assert (
        check.comparison_label(positive, negative)
        == "balanced_breaks_q2_classification"
    )


def test_numeric_comparison_tolerance_is_frozen():
    assert check.numeric_match(1.0, 1.0 + 0.5e-8)
    assert check.numeric_match(1.0e9, 1.0e9 + 5.0e-4)
    assert not check.numeric_match(1.0, 1.0 + 2.0e-8)
    assert check.COMPARE_ATOL == 1e-8
    assert check.COMPARE_RTOL == 1e-12


def test_exact_case_key_contract_is_28():
    keys = check.expected_keys()
    assert len(keys) == 28
    assert len(set(keys)) == 28
    assert keys[0] == "LAP4|baseline|phi0=0.0"
    assert keys[-1] == "LAP8|no_phi_cap|phi0=1.0"


def test_checker_has_no_import_or_dynamic_load_of_primary_pv1b_runner():
    source = CHECKER_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    assert not any("lineum_b4_q2_ledger_neutral_control" in name for name in imported)
    assert "importlib" not in imported
    assert "spec_from_file_location" not in source


def test_source_bindings_freeze_primary_and_report():
    assert check.EXPECTED_PRIMARY_BLOB == "50d3f15d881e0665a450982053a9216f9cf5739c"
    assert check.EXPECTED_REPORT_BLOB == "bab3f46f7dffa6f1242bcb27da1c6585fcb379b3"
    assert (
        check.EXPECTED_CANONICAL_RUNNER_BLOB
        == "1598faf0f39e056c1684f767c2554edc63283ca4"
    )


def test_sanitize_converts_nonfinite_diagnostics_to_null_representation():
    value = {"a": float("inf"), "b": [float("nan"), 1.0]}
    assert check.sanitize(value) == {"a": None, "b": [None, 1.0]}
