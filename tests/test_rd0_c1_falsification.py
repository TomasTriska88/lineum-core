"""Broader falsification controls for the opt-in RD-0-C1 candidate."""

from __future__ import annotations

import numpy as np
import pytest

from lineum_core import math as lineum_math
from lineum_core.profiles import (
    RD0_C1_CONTINUOUS_TIME_PROFILE,
    make_core_config,
)


SIZE = 32
PHYSICAL_TIME = 10.0
TIME_STEPS = (0.2, 0.1, 0.05, 0.025)
EFFECTIVE_PHI_ALPHA = 0.05 * 0.05


def _config(dt: float) -> lineum_math.CoreConfig:
    return make_core_config(
        RD0_C1_CONTINUOUS_TIME_PROFILE,
        dt=dt,
        psi_diffusion=0.0,
        phi_diffusion=0.05,
        reaction_strength=0.0,
        drift_strength=0.0,
    )


def _state(phi: np.ndarray, kappa: np.ndarray) -> dict[str, np.ndarray]:
    return {
        "psi": np.zeros_like(phi, dtype=np.complex128),
        "phi": phi.astype(np.float64),
        "kappa": kappa.astype(np.float64),
        "delta": np.zeros_like(phi, dtype=np.float64),
    }


def _mode(mode_x: int, mode_y: int) -> np.ndarray:
    y, x = np.mgrid[:SIZE, :SIZE]
    return np.cos(2 * np.pi * mode_x * x / SIZE) * np.cos(
        2 * np.pi * mode_y * y / SIZE
    )


def _mode_amplitude(phi: np.ndarray, mode: np.ndarray) -> float:
    centered = phi - np.mean(phi)
    return float(np.sum(centered * mode) / np.sum(mode**2))


def _evolve_numpy(
    phi: np.ndarray, kappa: np.ndarray, dt: float
) -> dict[str, np.ndarray]:
    state = _state(phi, kappa)
    config = _config(dt)
    for _ in range(round(PHYSICAL_TIME / dt)):
        state = lineum_math._step_numpy(state, config)
    return state


def _relative_to_reference(estimate: np.ndarray, reference: np.ndarray) -> float:
    return float(
        np.linalg.norm(estimate - reference)
        / (np.linalg.norm(reference) + 1e-30)
    )


def _evolve_torch_cpu(
    phi: np.ndarray, kappa: np.ndarray, dt: float
) -> dict[str, np.ndarray]:
    torch = getattr(lineum_math, "torch", None)
    if torch is None:
        pytest.skip("PyTorch is not installed")

    policy = lineum_math.ExecutionPolicy
    original_device = policy._device
    original_backend = getattr(policy, "_backend", None)
    policy._device = torch.device("cpu")
    if hasattr(policy, "_backend"):
        policy._backend = "pytorch"
    try:
        state = _state(phi, kappa)
        config = _config(dt)
        for _ in range(round(PHYSICAL_TIME / dt)):
            state = lineum_math._step_pytorch(state, config)
        return state
    finally:
        policy._device = original_device
        if hasattr(policy, "_backend"):
            policy._backend = original_backend


@pytest.mark.parametrize("mode_x,mode_y", [(1, 0), (1, 1), (2, 3), (8, 8)])
def test_multiple_fourier_modes_match_the_exact_lap4_solution(
    mode_x: int, mode_y: int
):
    dt = 0.1
    mode = _mode(mode_x, mode_y)
    initial_phi = 0.5 + 0.05 * mode
    result = _evolve_numpy(initial_phi, np.ones_like(initial_phi), dt)
    observed_ratio = _mode_amplitude(result["phi"], mode) / 0.05

    eigenvalue = (
        2 * np.cos(2 * np.pi * mode_x / SIZE)
        + 2 * np.cos(2 * np.pi * mode_y / SIZE)
        - 4
    )
    expected_ratio = float(
        (1 + dt * EFFECTIVE_PHI_ALPHA * eigenvalue)
        ** round(PHYSICAL_TIME / dt)
    )

    assert observed_ratio == pytest.approx(expected_ratio, abs=1e-13)


def test_one_step_phi_diffusion_wraps_periodically_at_all_edges():
    dt = 0.1
    phi = np.full((SIZE, SIZE), 0.5, dtype=np.float64)
    phi[0, 0] += 0.1
    result = lineum_math._step_numpy(_state(phi, np.ones_like(phi)), _config(dt))
    delta = result["phi"] - phi

    expected_neighbor_gain = dt * EFFECTIVE_PHI_ALPHA * 0.1
    assert delta[0, 0] == pytest.approx(-4 * expected_neighbor_gain)
    for y, x in ((1, 0), (SIZE - 1, 0), (0, 1), (0, SIZE - 1)):
        assert delta[y, x] == pytest.approx(expected_neighbor_gain)
    untouched = delta.copy()
    untouched[0, 0] = 0.0
    untouched[1, 0] = 0.0
    untouched[SIZE - 1, 0] = 0.0
    untouched[0, 1] = 0.0
    untouched[0, SIZE - 1] = 0.0
    assert np.max(np.abs(untouched)) < 1e-15


def test_nonuniform_kappa_refinement_remains_first_order():
    y, x = np.mgrid[:SIZE, :SIZE]
    phi = 0.5 + 0.08 * _mode(2, 1)
    kappa = 0.6 + 0.3 * np.cos(2 * np.pi * x / SIZE) * np.cos(
        2 * np.pi * y / SIZE
    )
    states = {dt: _evolve_numpy(phi, kappa, dt) for dt in TIME_STEPS}
    errors = [
        _relative_to_reference(states[coarse]["phi"], states[fine]["phi"])
        for coarse, fine in zip(TIME_STEPS, TIME_STEPS[1:])
    ]

    assert 1.95 < errors[0] / errors[1] < 2.05
    assert 1.95 < errors[1] / errors[2] < 2.05


def test_uniform_phi_stability_boundary_matches_lap4_prediction():
    checkerboard = _mode(SIZE // 2, SIZE // 2)
    phi = 0.5 + 0.1 * checkerboard
    kappa = np.ones_like(phi)

    def one_step_amplitude_ratio(dt: float) -> float:
        result = lineum_math._step_numpy(_state(phi.copy(), kappa), _config(dt))
        return _mode_amplitude(result["phi"], checkerboard) / 0.1

    assert one_step_amplitude_ratio(99.0) == pytest.approx(-0.98)
    assert abs(one_step_amplitude_ratio(99.0)) < 1.0
    assert one_step_amplitude_ratio(101.0) == pytest.approx(-1.02)
    assert abs(one_step_amplitude_ratio(101.0)) > 1.0


def test_nonuniform_candidate_matches_between_numpy_and_pytorch_cpu():
    y, x = np.mgrid[:SIZE, :SIZE]
    phi = 0.5 + 0.08 * _mode(3, 2)
    kappa = 0.6 + 0.3 * np.cos(2 * np.pi * x / SIZE) * np.cos(
        2 * np.pi * y / SIZE
    )
    numpy_state = _evolve_numpy(phi, kappa, 0.1)
    torch_state = _evolve_torch_cpu(phi, kappa, 0.1)

    np.testing.assert_allclose(
        numpy_state["phi"], torch_state["phi"], rtol=1e-12, atol=1e-13
    )
    np.testing.assert_allclose(
        numpy_state["psi"], torch_state["psi"], rtol=1e-12, atol=1e-13
    )
