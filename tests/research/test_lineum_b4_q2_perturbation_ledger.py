from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "research" / "runners" / "lineum_b4_q2_perturbation_ledger.py"
SPEC = importlib.util.spec_from_file_location("lineum_b4_q2_pv1", RUNNER_PATH)
assert SPEC is not None and SPEC.loader is not None
pv1 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = pv1
SPEC.loader.exec_module(pv1)


def synthetic_radius(size: int = 9) -> np.ndarray:
    row, col = np.indices((size, size), dtype=float)
    center = (size - 1) / 2.0
    return np.hypot(row - center, col - center)


def test_analytic_delta_matches_closed_form():
    assert pv1.analytic_delta(8.0, 4.0, active=True) == 7.0
    assert pv1.analytic_delta(8.0, 4.0, active=False) == 0.0


def test_active_audit_matches_direct_array_and_analytic_identity():
    radius = synthetic_radius()
    psi = np.ones(radius.shape, dtype=np.complex128) * (2.0 + 0.5j)
    phi = np.full(radius.shape, 3.0)
    row = pv1.audit_state(psi, phi, radius, active=True)

    expected = 1.25 * row["e_inner"] - 0.75 * row["e_annulus"]
    assert row["applicability"] == "perturbed_active"
    assert row["analytic_agreement"] is True
    np.testing.assert_allclose(row["analytic_delta_epsi"], expected, rtol=0, atol=1e-12)
    np.testing.assert_allclose(row["direct_delta_epsi"], expected, rtol=0, atol=1e-12)
    np.testing.assert_allclose(row["direct_delta_ledger"], expected, rtol=0, atol=1e-12)
    assert row["direct_delta_phi"] == 0.0


def test_inactive_audit_is_exact_noop_and_not_called_neutral_evidence():
    radius = synthetic_radius()
    psi = np.ones(radius.shape, dtype=np.complex128)
    phi = np.ones(radius.shape)
    row = pv1.audit_state(psi, phi, radius, active=False)

    assert row["applicability"] == "not_applicable_inactive"
    assert row["direct_delta_epsi"] == 0.0
    assert row["analytic_delta_epsi"] == 0.0
    assert row["direct_delta_ledger"] == 0.0
    assert row["ledger_neutral_within_numeric_tolerance"] is None
    assert row["analytic_agreement"] is True


def test_ledger_neutrality_threshold_is_frozen_relative_rule():
    assert pv1.ledger_tolerance(2.0e6) == 2.0e-4
    assert pv1.ledger_tolerance(0.25) == 1.0e-10


def test_balanced_annulus_factor_preserves_psi_ledger_when_available():
    e_inner = 2.0
    e_annulus = 8.0
    factor = pv1.balanced_annulus_factor(e_inner, e_annulus)
    assert factor is not None
    before = e_inner + e_annulus
    after = (1.5**2) * e_inner + (factor**2) * e_annulus
    np.testing.assert_allclose(after, before, rtol=0, atol=1e-12)


def test_balanced_annulus_factor_fails_closed_when_unavailable():
    assert pv1.balanced_annulus_factor(1.0, 0.0) is None
    assert pv1.balanced_annulus_factor(10.0, 1.0) is None


def test_expected_case_key_count_is_28():
    names = [
        "baseline",
        "no_hard_guards",
        "no_linear_dissipation",
        "no_explicit_tanh",
        "no_interaction_denominator",
        "no_mode_coupling",
        "no_phi_cap",
    ]
    keys = pv1.expected_case_keys(names, (0.0, 1.0), ("LAP4", "LAP8"))
    assert len(keys) == 28
    assert len(set(keys)) == 28
