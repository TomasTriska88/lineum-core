"""Characterization contract for the provisional RD-0 software reference.

RD-0 freezes a deterministic diffusive implementation baseline. It is a
regression ruler, not a claim that this update law is fundamental physics.
"""

from __future__ import annotations

import hashlib

import numpy as np
import pytest

from lineum_core import math as lineum_math


CHECKPOINTS = (1, 10, 100)
FINGERPRINT_SCALE = 10**12
EXPECTED_STATE_FINGERPRINTS = {
    1: "b4a47af600aecced9718600330b8e618d4f6888ec2465acf2f611dcc399fd3af",
    10: "e57d5a18a8ef8dbed48fe06eccc3108251ecda1afa7f1855801374092a5faf3f",
    100: "211dda7f2230625c9f4f1d92982dc022c1f6b6c7e3ba3aadffe5d0c78719418f",
}


def _make_rd0_state(size: int = 32) -> dict[str, np.ndarray]:
    y, x = np.mgrid[:size, :size]
    center = (size - 1) / 2
    radius_squared = (x - center) ** 2 + (y - center) ** 2
    envelope = np.exp(-radius_squared / (2 * 3.5**2))
    phase = 0.17 * x - 0.11 * y
    return {
        "psi": (envelope * np.exp(1j * phase)).astype(np.complex128),
        "phi": (
            0.25
            + 0.08
            * np.cos(2 * np.pi * x / size)
            * np.cos(2 * np.pi * y / size)
        ).astype(np.float64),
        "kappa": np.ones((size, size), dtype=np.float64),
        "delta": np.zeros((size, size), dtype=np.float64),
    }


def _rd0_config() -> lineum_math.CoreConfig:
    return lineum_math.CoreConfig(
        dt=0.1,
        physics_mode_psi="diffusion",
        disable_quantum_noise=True,
        use_mode_coupling=False,
        use_mu=False,
        disable_pml=True,
        stencil_type="LAP4",
    )


def _state_fingerprint(state: dict[str, np.ndarray]) -> str:
    """Hash the complete psi/phi state after quantization to 1e-12."""
    digest = hashlib.sha256()
    components = (
        ("psi.real", np.asarray(state["psi"]).real),
        ("psi.imag", np.asarray(state["psi"]).imag),
        ("phi", np.asarray(state["phi"])),
    )
    for name, component in components:
        quantized = np.rint(component * FINGERPRINT_SCALE).astype("<i8")
        digest.update(name.encode("ascii"))
        digest.update(np.asarray(quantized.shape, dtype="<i8").tobytes())
        digest.update(np.ascontiguousarray(quantized).tobytes())
    return digest.hexdigest()


def _run_numpy() -> dict[int, dict[str, np.ndarray]]:
    state = _make_rd0_state()
    results = {}
    for step in range(1, max(CHECKPOINTS) + 1):
        state = lineum_math._step_numpy(state, _rd0_config())
        if step in CHECKPOINTS:
            results[step] = {
                "psi": state["psi"].copy(),
                "phi": state["phi"].copy(),
                "telemetry": dict(state["telemetry"]),
            }
    return results


def _run_torch_cpu() -> dict[int, dict[str, np.ndarray]]:
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
        state = _make_rd0_state()
        results = {}
        for step in range(1, max(CHECKPOINTS) + 1):
            state = lineum_math._step_pytorch(state, _rd0_config())
            if step in CHECKPOINTS:
                results[step] = {
                    "psi": state["psi"].copy(),
                    "phi": state["phi"].copy(),
                    "telemetry": dict(state["telemetry"]),
                }
        return results
    finally:
        policy._device = original_device
        if hasattr(policy, "_backend"):
            policy._backend = original_backend


def test_rd0_numpy_full_state_fingerprints():
    """Freeze the current ordered diffusive map at 1e-12 resolution."""
    results = _run_numpy()

    assert {
        step: _state_fingerprint(results[step]) for step in CHECKPOINTS
    } == EXPECTED_STATE_FINGERPRINTS
    assert all(
        results[step]["telemetry"]["cap_triggers"] == 0
        and not results[step]["telemetry"]["is_nan"]
        for step in CHECKPOINTS
    )


def test_rd0_numpy_matches_pytorch_cpu_for_complete_state():
    """Require both CPU backends to implement the same RD-0 state evolution."""
    numpy_results = _run_numpy()
    torch_results = _run_torch_cpu()

    for step in CHECKPOINTS:
        assert torch_results[step]["telemetry"]["cap_triggers"] == 0
        assert not torch_results[step]["telemetry"]["is_nan"]
        np.testing.assert_allclose(
            numpy_results[step]["psi"],
            torch_results[step]["psi"],
            rtol=1e-12,
            atol=1e-13,
        )
        np.testing.assert_allclose(
            numpy_results[step]["phi"],
            torch_results[step]["phi"],
            rtol=1e-12,
            atol=1e-13,
        )
