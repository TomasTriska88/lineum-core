"""Characterization tests for the zero-kappa damping lane.

An earlier test described repeated explicit forcing as thermal-noise
amplification and true randomness. With kappa equal to zero, the current Core
map suppresses diffusion, interaction, reaction, and stochastic source
transfer. The remaining psi evolution is deterministic damping. These tests
freeze that actual behavior and prevent the forced accumulation from being
misidentified as chaos.
"""

from __future__ import annotations

import numpy as np
import pytest

from lineum_core.math import CoreConfig, _step_numpy


GRID_SIZE = 16
DAMPING_FACTOR = 1.0 - 0.005
CONFIG = CoreConfig(
    dt=1.0,
    disable_quantum_noise=True,
    use_mode_coupling=False,
    use_mu=False,
    disable_pml=True,
)


def _state(psi: np.ndarray) -> dict[str, np.ndarray]:
    zeros = np.zeros(psi.shape, dtype=np.float64)
    return {
        "psi": psi.astype(np.complex128).copy(),
        "phi": zeros.copy(),
        "kappa": zeros.copy(),
        "delta": zeros.copy(),
    }


def _evolve(state: dict[str, np.ndarray], steps: int) -> dict[str, np.ndarray]:
    for _ in range(steps):
        state = _step_numpy(state, CONFIG)
    return state


def test_zero_kappa_identical_complete_states_replay_exactly():
    initial = np.full((GRID_SIZE, GRID_SIZE), 0.5 + 0.1j)
    first = _evolve(_state(initial), 100)
    second = _evolve(_state(initial), 100)

    np.testing.assert_array_equal(first["psi"], second["psi"])
    np.testing.assert_array_equal(first["phi"], second["phi"])


def test_zero_kappa_single_perturbation_decays_instead_of_amplifying():
    steps = 1_500
    injection = 1e-5 + 1e-5j
    baseline = np.full((GRID_SIZE, GRID_SIZE), 0.5 + 0.0j)
    perturbed = baseline.copy()
    perturbed[3, 3] += injection

    baseline_final = _evolve(_state(baseline), steps)["psi"]
    perturbed_final = _evolve(_state(perturbed), steps)["psi"]
    observed = float(np.sum(np.abs(perturbed_final - baseline_final)))
    expected = abs(injection) * DAMPING_FACTOR**steps

    assert observed == pytest.approx(expected, rel=2e-7, abs=1e-15)
    assert observed < abs(injection)


def test_zero_kappa_repeated_forcing_is_a_geometric_sum_not_chaos():
    steps = 1_500
    injection = 1e-5 + 1e-5j
    baseline = _state(np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.complex128))
    forced = _state(np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.complex128))

    for _ in range(steps):
        forced["psi"][3, 3] += injection
        baseline = _step_numpy(baseline, CONFIG)
        forced = _step_numpy(forced, CONFIG)

    observed = float(np.sum(np.abs(forced["psi"] - baseline["psi"])))
    expected = (
        abs(injection)
        * DAMPING_FACTOR
        * (1.0 - DAMPING_FACTOR**steps)
        / (1.0 - DAMPING_FACTOR)
    )

    assert observed == pytest.approx(expected, rel=1e-12, abs=1e-15)
    assert observed > 0.001
