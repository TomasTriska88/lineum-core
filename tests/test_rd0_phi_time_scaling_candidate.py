"""Regression tests for the opt-in RD-0-C1 phi time-scaling candidate."""

from __future__ import annotations

import numpy as np
import pytest

from lineum_core import math as lineum_math


SIZE = 32
PHYSICAL_TIME = 10.0
TIME_STEPS = (0.2, 0.1, 0.05, 0.025)


def _config(
    dt: float, *, scaled: bool, isolated: bool = False
) -> lineum_math.CoreConfig:
    return lineum_math.CoreConfig(
        dt=dt,
        physics_mode_psi="diffusion",
        disable_quantum_noise=True,
        phi_diffusion_scales_with_dt=scaled,
        use_mode_coupling=False,
        use_mu=False,
        disable_pml=True,
        stencil_type="LAP4",
        reaction_strength=0.0 if isolated else 0.0007,
        drift_strength=0.0 if isolated else -0.004,
    )


def _make_phi_mode() -> tuple[dict[str, np.ndarray], np.ndarray]:
    y, x = np.mgrid[:SIZE, :SIZE]
    mode = np.cos(2 * np.pi * x / SIZE) * np.cos(2 * np.pi * y / SIZE)
    phi = 0.5 + 0.1 * mode
    state = {
        "psi": np.zeros((SIZE, SIZE), dtype=np.complex128),
        "phi": phi.astype(np.float64),
        "kappa": np.ones((SIZE, SIZE), dtype=np.float64),
        "delta": np.zeros((SIZE, SIZE), dtype=np.float64),
    }
    return state, mode


def _mode_amplitude(phi: np.ndarray, mode: np.ndarray) -> float:
    centered = phi - np.mean(phi)
    return float(np.sum(centered * mode) / np.sum(mode**2))


def _run_phi_mode(dt: float, *, scaled: bool) -> float:
    state, mode = _make_phi_mode()
    initial_amplitude = _mode_amplitude(state["phi"], mode)
    config = _config(dt, scaled=scaled, isolated=True)
    for _ in range(round(PHYSICAL_TIME / dt)):
        state = lineum_math._step_numpy(state, config)
    return _mode_amplitude(state["phi"], mode) / initial_amplitude


def _analytic_phi_mode_ratio(dt: float, *, scaled: bool) -> float:
    lap4_eigenvalue = 4 * np.cos(2 * np.pi / SIZE) - 4
    effective_alpha = 0.05 * 0.05
    step_scale = dt if scaled else 1.0
    per_step_factor = 1 + effective_alpha * lap4_eigenvalue * step_scale
    return float(per_step_factor ** round(PHYSICAL_TIME / dt))


def _make_coupled_state() -> dict[str, np.ndarray]:
    y, x = np.mgrid[:SIZE, :SIZE]
    center = (SIZE - 1) / 2
    radius_squared = (x - center) ** 2 + (y - center) ** 2
    envelope = np.exp(-radius_squared / (2 * 3.5**2))
    phase = 0.17 * x - 0.11 * y
    return {
        "psi": (envelope * np.exp(1j * phase)).astype(np.complex128),
        "phi": (
            0.25
            + 0.08
            * np.cos(2 * np.pi * x / SIZE)
            * np.cos(2 * np.pi * y / SIZE)
        ).astype(np.float64),
        "kappa": np.ones((SIZE, SIZE), dtype=np.float64),
        "delta": np.zeros((SIZE, SIZE), dtype=np.float64),
    }


def _run_numpy_coupled(dt: float) -> dict[str, np.ndarray]:
    state = _make_coupled_state()
    config = _config(dt, scaled=True)
    for _ in range(round(PHYSICAL_TIME / dt)):
        state = lineum_math._step_numpy(state, config)
    return state


def _relative_to_reference(estimate: np.ndarray, reference: np.ndarray) -> float:
    return float(
        np.linalg.norm(estimate - reference)
        / (np.linalg.norm(reference) + 1e-30)
    )


def _run_torch_coupled(dt: float) -> dict[str, np.ndarray]:
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
        state = _make_coupled_state()
        config = _config(dt, scaled=True)
        for _ in range(round(PHYSICAL_TIME / dt)):
            state = lineum_math._step_pytorch(state, config)
        return state
    finally:
        policy._device = original_device
        if hasattr(policy, "_backend"):
            policy._backend = original_backend


def test_candidate_is_opt_in_and_legacy_remains_default():
    assert lineum_math.CoreConfig().phi_diffusion_scales_with_dt is False


def test_candidate_phi_mode_matches_analytic_refinement():
    current_ratios = [_run_phi_mode(dt, scaled=False) for dt in TIME_STEPS]
    candidate_ratios = [_run_phi_mode(dt, scaled=True) for dt in TIME_STEPS]
    analytic_ratios = [
        _analytic_phi_mode_ratio(dt, scaled=True) for dt in TIME_STEPS
    ]

    np.testing.assert_allclose(candidate_ratios, analytic_ratios, atol=1e-14)
    assert max(current_ratios) - min(current_ratios) > 0.06
    assert max(candidate_ratios) - min(candidate_ratios) < 4e-8


def test_candidate_coupled_refinement_is_first_order():
    states = {dt: _run_numpy_coupled(dt) for dt in TIME_STEPS}
    phi_errors = []
    psi_errors = []
    for coarse, fine in zip(TIME_STEPS, TIME_STEPS[1:]):
        phi_errors.append(
            _relative_to_reference(states[coarse]["phi"], states[fine]["phi"])
        )
        psi_errors.append(
            _relative_to_reference(states[coarse]["psi"], states[fine]["psi"])
        )

    assert 1.99 < phi_errors[0] / phi_errors[1] < 2.01
    assert 1.99 < phi_errors[1] / phi_errors[2] < 2.01
    assert 1.99 < psi_errors[0] / psi_errors[1] < 2.01
    assert 1.99 < psi_errors[1] / psi_errors[2] < 2.01


def test_candidate_numpy_matches_pytorch_cpu_for_complete_state():
    numpy_state = _run_numpy_coupled(0.1)
    torch_state = _run_torch_coupled(0.1)

    np.testing.assert_allclose(
        numpy_state["psi"], torch_state["psi"], rtol=1e-12, atol=1e-13
    )
    np.testing.assert_allclose(
        numpy_state["phi"], torch_state["phi"], rtol=1e-12, atol=1e-13
    )
    assert numpy_state["telemetry"]["cap_triggers"] == 0
    assert torch_state["telemetry"]["cap_triggers"] == 0
