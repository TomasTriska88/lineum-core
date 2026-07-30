import hashlib
import json

import numpy as np
import pytest

from lineum_core.math import CoreConfig, ExecutionPolicy
from lineum_core.state_checkpoint import (
    CheckpointFormatError,
    create_checkpoint,
    load_checkpoint,
    run_steps,
    serialize_checkpoint,
)


def make_state(size: int = 12) -> dict[str, np.ndarray]:
    axis = np.linspace(-1.0, 1.0, size)
    y, x = np.meshgrid(axis, axis, indexing="ij")
    envelope = np.exp(-4.0 * (x**2 + y**2))
    phase = np.exp(1j * (1.7 * x - 0.8 * y))
    return {
        "psi": (0.15 * envelope * phase).astype(np.complex128),
        "phi": (0.02 * envelope).astype(np.float64),
        "kappa": (0.55 + 0.35 * envelope).astype(np.float64),
        "mu": (0.01 * (1.0 - envelope)).astype(np.float64),
    }


def assert_state_equal(left, right):
    for key in ("psi", "phi", "kappa", "mu"):
        assert np.array_equal(left[key], right[key]), key


def test_checkpoint_round_trip_preserves_arrays_config_and_hash():
    ExecutionPolicy.init_core_determinism(seed=1729, device_mode="numpy")
    config = CoreConfig(use_mu=True, noise_strength=0.003)
    state = run_steps(make_state(), config, 3)
    checkpoint = create_checkpoint(state, config, step_index=3)
    serialized = serialize_checkpoint(checkpoint)

    restored_state, restored_config, restored_step = load_checkpoint(serialized)

    assert restored_step == 3
    assert restored_config == config
    assert_state_equal(state, restored_state)
    assert hashlib.sha256(serialized).hexdigest() == hashlib.sha256(
        serialize_checkpoint(checkpoint)
    ).hexdigest()


def test_restored_checkpoint_continues_bitwise_when_rng_state_is_transferred():
    ExecutionPolicy.init_core_determinism(seed=314159, device_mode="numpy")
    config = CoreConfig(use_mu=True, noise_strength=0.004)
    donor_at_checkpoint = run_steps(make_state(), config, 5)
    serialized = serialize_checkpoint(
        create_checkpoint(donor_at_checkpoint, config, step_index=5)
    )

    uninterrupted = run_steps(donor_at_checkpoint, config, 7)
    recipient_state, recipient_config, recipient_step = load_checkpoint(serialized)
    restored = run_steps(recipient_state, recipient_config, 7)

    assert recipient_step == 5
    assert_state_equal(uninterrupted, restored)


def test_reset_rng_breaks_exact_continuation_when_noise_is_active():
    ExecutionPolicy.init_core_determinism(seed=271828, device_mode="numpy")
    config = CoreConfig(use_mu=True, noise_strength=0.004)
    donor_at_checkpoint = run_steps(make_state(), config, 5)
    serialized = serialize_checkpoint(
        create_checkpoint(donor_at_checkpoint, config, step_index=5)
    )

    uninterrupted = run_steps(donor_at_checkpoint, config, 7)
    recipient_state, recipient_config, _ = load_checkpoint(
        serialized,
        restore_rng=False,
    )
    np.random.seed(999)
    reset_history = run_steps(recipient_state, recipient_config, 7)

    assert not np.array_equal(uninterrupted["psi"], reset_history["psi"])
    assert (
        float(np.max(np.abs(uninterrupted["psi"] - reset_history["psi"])))
        > 0.0
    )


def test_integrity_hash_rejects_modified_checkpoint():
    ExecutionPolicy.init_core_determinism(seed=42, device_mode="numpy")
    checkpoint = create_checkpoint(make_state(), CoreConfig(), step_index=0)
    modified = json.loads(serialize_checkpoint(checkpoint))
    modified["step_index"] = 1

    with pytest.raises(CheckpointFormatError, match="integrity hash mismatch"):
        load_checkpoint(modified)
