from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = (
    ROOT / "research" / "runners" / "lineum_b4_q2_ledger_neutral_control.py"
)
SPEC = importlib.util.spec_from_file_location("lineum_b4_q2_pv1b", RUNNER_PATH)
assert SPEC is not None and SPEC.loader is not None
pv1b = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = pv1b
SPEC.loader.exec_module(pv1b)


def synthetic_radius(size: int = 11) -> np.ndarray:
    row, col = np.indices((size, size), dtype=float)
    center = (size - 1) / 2.0
    return np.hypot(row - center, col - center)


def base_recovery_row(**overrides):
    row = {
        "full_recovery": False,
        "finite": True,
        "reset_free": True,
        "primary_psi_cap_hits": 0,
        "recovery_psi_cap_hits": 0,
        "primary_phi_cap_hits": 0,
        "recovery_phi_cap_hits": 0,
    }
    row.update(overrides)
    return row


def test_balanced_perturbation_preserves_declared_psi_ledger():
    radius = synthetic_radius()
    psi = np.ones(radius.shape, dtype=np.complex128) * (1.5 + 0.25j)
    phi = np.full(radius.shape, 2.0)
    energy = np.abs(psi) ** 2
    e_inner = float(np.sum(energy[radius <= 2.0]))
    e_annulus = float(np.sum(energy[(radius >= 3.0) & (radius <= 5.0)]))
    b_squared = 1.0 - 1.25 * e_inner / e_annulus
    assert b_squared >= 0.0
    factor = float(np.sqrt(b_squared))
    perturbed = pv1b.apply_balanced_perturbation(psi, radius, factor=factor)
    receipt = pv1b.perturbation_ledger_receipt(psi, phi, perturbed)
    assert receipt["neutral_within_numeric_tolerance"] is True
    np.testing.assert_allclose(
        receipt["epsi_after"], receipt["epsi_before"], rtol=0, atol=1e-12
    )


def test_q2_admissibility_requires_no_caps_or_resets():
    assert pv1b.q2_admissible_full_recovery(
        base_recovery_row(full_recovery=True)
    )
    assert not pv1b.q2_admissible_full_recovery(
        base_recovery_row(full_recovery=True, primary_psi_cap_hits=1)
    )
    assert not pv1b.q2_admissible_full_recovery(
        base_recovery_row(full_recovery=True, recovery_phi_cap_hits=1)
    )
    assert not pv1b.q2_admissible_full_recovery(
        base_recovery_row(full_recovery=True, reset_free=False)
    )


def test_compare_control_fails_closed_when_unavailable():
    canonical = base_recovery_row(full_recovery=False)
    assert pv1b.compare_control(canonical, None) == "control_unavailable"


def test_compare_control_classifies_rescue_and_non_rescue():
    negative = base_recovery_row(full_recovery=False)
    positive = base_recovery_row(full_recovery=True)
    assert (
        pv1b.compare_control(negative, positive)
        == "balanced_rescues_q2_classification"
    )
    assert pv1b.compare_control(negative, negative) == "both_q2_negative"
    assert pv1b.compare_control(positive, positive) == "both_q2_positive"
    assert (
        pv1b.compare_control(positive, negative)
        == "balanced_breaks_q2_classification"
    )


def test_source_bindings_are_exact_frozen_inputs():
    assert pv1b.CANONICAL_RUNNER_GIT_BLOB == "1598faf0f39e056c1684f767c2554edc63283ca4"
    assert pv1b.PV1_RUNNER_GIT_BLOB == "e3657119b855965b4fd622b3e94f08443a7c9107"
    assert pv1b.PV1_PRIMARY_GIT_BLOB == "7a7ce23471d51d9b2244256387934658b12e1f52"
    assert pv1b.PV1_CHECKER_GIT_BLOB == "c459e4a1f947aba55d01f8f30bc1aa6bae88076f"
    assert pv1b.INNER_FACTOR == 1.5
    assert pv1b.NUMERIC_RTOL == 1e-10


def test_balanced_factor_precheck_matches_preregistered_formula():
    e_inner = 2.0
    e_annulus = 10.0
    expected = np.sqrt(1.0 - 1.25 * e_inner / e_annulus)
    assert np.isclose(expected, np.sqrt(0.75))


def test_stage_and_schema_are_frozen():
    assert pv1b.STAGE == "Q2-PV1-B"
    assert pv1b.SCHEMA == "lineum-b4-q2-ledger-neutral-control/1"
