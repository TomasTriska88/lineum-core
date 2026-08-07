from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "research" / "runners" / "lineum_b4_saturation_localized_l1.py"
CHECKER_PATH = (
    ROOT / "research" / "runners" / "lineum_b4_saturation_localized_l1_check.py"
)
SPEC = importlib.util.spec_from_file_location("lineum_b4_l1", RUNNER_PATH)
assert SPEC is not None and SPEC.loader is not None
l1 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = l1
SPEC.loader.exec_module(l1)

CHECKER_SPEC = importlib.util.spec_from_file_location("lineum_b4_l1_check", CHECKER_PATH)
assert CHECKER_SPEC is not None and CHECKER_SPEC.loader is not None
l1_check = importlib.util.module_from_spec(CHECKER_SPEC)
sys.modules[CHECKER_SPEC.name] = l1_check
CHECKER_SPEC.loader.exec_module(l1_check)


def production_diffuse(field, kappa, rate, stencil):
    k_up = np.roll(kappa, 1, axis=0)
    k_dn = np.roll(kappa, -1, axis=0)
    k_lf = np.roll(kappa, 1, axis=1)
    k_rt = np.roll(kappa, -1, axis=1)
    f_up = np.roll(field, 1, axis=0)
    f_dn = np.roll(field, -1, axis=0)
    f_lf = np.roll(field, 1, axis=1)
    f_rt = np.roll(field, -1, axis=1)
    if stencil == "LAP8":
        k_ul = np.roll(k_up, 1, axis=1)
        k_ur = np.roll(k_up, -1, axis=1)
        k_dl = np.roll(k_dn, 1, axis=1)
        k_dr = np.roll(k_dn, -1, axis=1)
        f_ul = np.roll(f_up, 1, axis=1)
        f_ur = np.roll(f_up, -1, axis=1)
        f_dl = np.roll(f_dn, 1, axis=1)
        f_dr = np.roll(f_dn, -1, axis=1)
        neighbour_sum = (
            f_up * k_up
            + f_dn * k_dn
            + f_lf * k_lf
            + f_rt * k_rt
            + 0.25
            * (
                f_ul * k_ul
                + f_ur * k_ur
                + f_dl * k_dl
                + f_dr * k_dr
            )
        )
        active = (
            k_up
            + k_dn
            + k_lf
            + k_rt
            + 0.25 * (k_ul + k_ur + k_dl + k_dr)
        )
    else:
        neighbour_sum = f_up * k_up + f_dn * k_dn + f_lf * k_lf + f_rt * k_rt
        active = k_up + k_dn + k_lf + k_rt
    return rate * (neighbour_sum - active * field)


def production_baseline_step(psi, phi, kappa, stencil):
    phi_int = np.clip(phi, 0.0, 10.0)
    interaction_factor = 0.1 * np.tanh((0.04 * phi_int * kappa) / 0.1)
    interaction = interaction_factor * psi
    interaction = interaction / (1.0 + np.abs(interaction) / 10.0)

    grad_phi_x, grad_phi_y = np.gradient(phi)
    flow = -0.004 * (grad_phi_x + 1j * grad_phi_y) * kappa
    flow = flow / (1.0 + np.abs(flow) / 10.0)
    psi = psi + flow
    magnitude = np.abs(psi)
    mask = magnitude > l1.PSI_CAP
    psi[mask] = psi[mask] * (l1.PSI_CAP / (magnitude[mask] + 1e-30))
    psi = psi + interaction
    psi = psi - 0.005 * psi
    psi = psi + production_diffuse(psi, kappa, 0.05, stencil) * kappa

    energy = np.abs(psi) ** 2
    transferred = 0.001 * energy * kappa
    phi = phi + transferred
    psi = psi / (np.sqrt(energy) + 1e-12) * np.sqrt(
        np.maximum(energy - transferred, 0.0)
    )
    phi = phi + 0.05 * production_diffuse(phi, kappa, 0.05, stencil)
    phi = np.clip(phi, 0.0, l1.PHI_CAP)
    if np.isnan(np.sum(psi)) or np.max(np.abs(psi)) >= l1.PSI_CAP * 0.99:
        psi = np.zeros_like(psi)
    return psi, phi


def test_gaussian_has_declared_peak_one():
    assert np.abs(l1.GAUSSIAN).max() == 1.0
    assert np.count_nonzero(np.isclose(np.abs(l1.GAUSSIAN), 1.0)) == 4


def test_batched_diffusion_matches_frozen_production_for_both_stencils():
    rng = np.random.default_rng(1234)
    field = rng.normal(size=(32, 32)) + 1j * rng.normal(size=(32, 32))
    kappa = rng.uniform(0.2, 1.0, size=(32, 32))
    for stencil in ("LAP4", "LAP8"):
        expected = production_diffuse(field, kappa, 0.05, stencil)
        observed = l1.diffuse(field[None, ...], kappa[None, ...], 0.05, stencil)[0]
        np.testing.assert_allclose(observed, expected, rtol=0.0, atol=0.0)


def test_one_step_preserves_production_gradient_axis_order():
    row, column = np.indices((32, 32), dtype=float)
    psi = (0.2 + 0.001 * row + 0.002j * column).astype(np.complex128)
    phi = (0.03 * row + 0.07 * column + 0.0005 * row * column).astype(float)
    kappa = np.ones((32, 32), dtype=float)
    expected_psi, expected_phi = production_baseline_step(
        psi.copy(), phi.copy(), kappa.copy(), "LAP8"
    )
    specs = [(l1.LANES[0], 0.0)]
    observed_psi, observed_phi, reset, psi_cap, phi_cap = l1.advance_batch_one_step(
        psi[None, ...],
        phi[None, ...],
        kappa[None, ...],
        np.zeros((1, 32, 32)),
        "LAP8",
        l1.build_lane_arrays(specs),
    )
    np.testing.assert_allclose(observed_psi[0], expected_psi, rtol=0.0, atol=2e-15)
    np.testing.assert_allclose(observed_phi[0], expected_phi, rtol=0.0, atol=2e-15)
    assert not reset[0]
    assert not psi_cap[0]
    assert not phi_cap[0]


def test_nonfinite_failure_preserves_last_finite_state_and_receipt():
    psi = np.ones((2, 32, 32), dtype=np.complex128)
    phi = np.ones((2, 32, 32), dtype=float)
    active = np.array([True, True])
    last_psi = psi.copy()
    last_phi = phi.copy()
    psi[1, 0, 0] = np.inf
    failure_step = np.full(2, -1, dtype=int)
    failure_stage = [None, None]
    failure_reason = [None, None]
    psi, phi, newly_bad = l1._mark_failures(
        psi,
        phi,
        active,
        last_psi,
        last_phi,
        failure_step,
        failure_stage,
        failure_reason,
        17,
        "primary",
    )
    assert newly_bad.tolist() == [False, True]
    assert np.all(psi[1] == 1.0)
    assert np.all(phi[1] == 1.0)
    assert not active[1]
    assert failure_step[1] == 17
    assert failure_stage[1] == "primary"
    assert failure_reason[1] == "nonfinite_state"


def test_stencil_comparison_status_includes_all_primary_boundedness_gates():
    row = {
        "boundedness": {
            "finite": True,
            "reset_free": False,
            "psi_cap_free": True,
            "phi_cap_free": False,
        },
        "recovery": {
            "localized_psi_recovery": True,
            "localized_full_state_recovery": False,
        },
    }
    assert l1._pair_status(row) == (True, False, True, False, True, False)


def test_checker_is_independent_of_primary_runner_import():
    executed_source = getattr(l1_check, "_CANONICAL_SOURCE", CHECKER_PATH.read_bytes())
    source = executed_source.decode("utf-8")
    assert "import lineum_b4_saturation_localized_l1" not in source
    assert "from lineum_b4_saturation_localized_l1" not in source
    assert "recomputes_all_28_runs" in source


def test_json_boundary_converts_numpy_scalars():
    assert l1.json_scalar(np.bool_(True)) is True
    assert l1.json_scalar(np.int64(7)) == 7
    assert l1_check.json_scalar(np.float64(1.25)) == 1.25
    payload = {"flag": np.bool_(False), "count": np.int64(3)}
    assert json.loads(json.dumps(payload, default=l1.json_scalar)) == {
        "flag": False,
        "count": 3,
    }


def test_strict_json_boundary_preserves_nonfinite_diagnostics():
    payload = {
        "positive": math.inf,
        "negative": -math.inf,
        "nan": math.nan,
        "nested": [np.float64(math.inf)],
    }
    ready = l1.json_ready(payload)
    assert ready == {
        "positive": "Infinity",
        "negative": "-Infinity",
        "nan": "NaN",
        "nested": ["Infinity"],
    }
    encoded = json.dumps(ready, allow_nan=False)
    restored = l1_check.restore_nonfinite(json.loads(encoded))
    assert restored["positive"] == math.inf
    assert restored["negative"] == -math.inf
    assert math.isnan(restored["nan"])
    assert restored["nested"] == [math.inf]


def test_checker_numeric_comparison_accepts_matching_nonfinite_sentinels():
    assert l1_check.numeric_values_match(math.nan, math.nan)
    assert l1_check.numeric_values_match(math.inf, math.inf)
    assert l1_check.numeric_values_match(-math.inf, -math.inf)
    assert not l1_check.numeric_values_match(math.inf, -math.inf)
    assert not l1_check.numeric_values_match(math.nan, 0.0)
    assert l1_check.numeric_values_match(1.0, 1.0 + 1e-12)
