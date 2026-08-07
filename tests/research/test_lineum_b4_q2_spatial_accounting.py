from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CANONICAL = ROOT / "research" / "runners" / "lineum_b4_saturation_localized_l1.py"
ACCOUNTING = ROOT / "research" / "runners" / "lineum_b4_q2_spatial_accounting.py"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


l1 = _load("lineum_b4_l1_equivalence", CANONICAL)
sa = _load("lineum_b4_sa_equivalence", ACCOUNTING)


def _lane_arrays(count: int):
    specs = [(l1.LANES[0], 1.0) for _ in range(count)]
    arrays = l1.build_lane_arrays(specs)
    arrays["use_phi_cap"][:] = False
    return arrays


def test_instrumented_l0_is_bitwise_equal_for_one_step_both_stencils():
    rng = np.random.default_rng(20260807)
    count = 3
    psi = (
        rng.normal(scale=0.1, size=(count, 32, 32))
        + 1j * rng.normal(scale=0.1, size=(count, 32, 32))
    ).astype(np.complex128)
    phi = rng.uniform(0.2, 2.0, size=(count, 32, 32))
    kappa = np.ones((count, 32, 32), dtype=float)
    mu = np.zeros_like(kappa)
    active = np.ones(count, dtype=bool)
    spatial = sa._spatial_arrays(
        tuple(sa.SpatialLane(f"L0-{i}", True, True, True) for i in range(count))
    )
    lanes = _lane_arrays(count)
    for stencil in ("LAP4", "LAP8"):
        expected = l1.advance_batch_one_step(
            psi.copy(), phi.copy(), kappa, mu, stencil, lanes, active.copy()
        )
        observed = sa.instrumented_step(
            psi.copy(),
            phi.copy(),
            kappa,
            mu,
            stencil,
            lanes,
            spatial,
            active.copy(),
            region=None,
        )
        assert np.array_equal(observed[0], expected[0])
        assert np.array_equal(observed[1], expected[1])
        assert np.array_equal(observed[2], expected[2])
        assert np.array_equal(observed[3], expected[3])
        assert np.array_equal(observed[4], expected[4])


def test_instrumented_l0_is_bitwise_equal_for_256_steps_both_stencils():
    count = 1
    initial_psi = l1.GAUSSIAN[None, ...].copy()
    initial_phi = np.ones((count, 32, 32), dtype=float)
    kappa = np.ones((count, 32, 32), dtype=float)
    mu = np.zeros_like(kappa)
    lanes = _lane_arrays(count)
    spatial = sa._spatial_arrays((sa.SpatialLane("L0", True, True, True),))
    for stencil in ("LAP4", "LAP8"):
        expected_psi = initial_psi.copy()
        expected_phi = initial_phi.copy()
        observed_psi = initial_psi.copy()
        observed_phi = initial_phi.copy()
        active_expected = np.ones(count, dtype=bool)
        active_observed = np.ones(count, dtype=bool)
        for _ in range(256):
            expected = l1.advance_batch_one_step(
                expected_psi,
                expected_phi,
                kappa,
                mu,
                stencil,
                lanes,
                active_expected,
            )
            expected_psi, expected_phi = expected[:2]
            observed = sa.instrumented_step(
                observed_psi,
                observed_phi,
                kappa,
                mu,
                stencil,
                lanes,
                spatial,
                active_observed,
                region=None,
            )
            observed_psi, observed_phi = observed[:2]
            assert np.array_equal(observed_psi, expected_psi)
            assert np.array_equal(observed_phi, expected_phi)
            assert np.array_equal(observed[2], expected[2])
            assert np.array_equal(observed[3], expected[3])
            assert np.array_equal(observed[4], expected[4])


def test_stage_deltas_telescope_to_full_step_with_fixed_region():
    count = 1
    psi = l1.GAUSSIAN[None, ...].copy()
    phi = np.ones((count, 32, 32), dtype=float)
    kappa = np.ones((count, 32, 32), dtype=float)
    mu = np.zeros_like(kappa)
    lanes = _lane_arrays(count)
    spatial = sa._spatial_arrays((sa.SpatialLane("L0", True, True, True),))
    region = (l1.RADIUS <= 4.0)[None, ...].astype(float)
    observed = sa.instrumented_step(
        psi, phi, kappa, mu, "LAP8", lanes, spatial, region=region
    )
    residual = observed[6]
    for key, values in residual.items():
        np.testing.assert_allclose(values, 0.0, rtol=0.0, atol=5e-13, err_msg=key)


def test_spatial_lane_mapping_is_exactly_the_preregistered_one_at_a_time_set():
    assert [(x.name, x.flow, x.psi_diffusion, x.phi_diffusion) for x in sa.SPATIAL_LANES] == [
        ("L0", True, True, True),
        ("S1", False, True, False),
        ("S2", False, False, True),
        ("S3", True, False, False),
    ]
