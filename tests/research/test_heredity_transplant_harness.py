import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pytest

from lineum_core.math import CoreConfig, ExecutionPolicy

HARNESS_PATH = (
    Path(__file__).resolve().parents[2]
    / "scripts"
    / "research"
    / "heredity_transplant_harness.py"
)
SPEC = importlib.util.spec_from_file_location("heredity_transplant_harness", HARNESS_PATH)
assert SPEC is not None and SPEC.loader is not None
harness = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = harness
SPEC.loader.exec_module(harness)


def assert_state_equal(left, right):
    for key in ("psi", "phi", "kappa", "mu"):
        assert np.array_equal(left[key], right[key]), key


def test_baseline_record_round_trip_rebuilds_identical_state():
    baseline = harness.GaussianDevelopmentalBaseline()
    restored = harness.GaussianDevelopmentalBaseline.from_record(
        baseline.to_record()
    )
    left = harness.build_baseline_state(baseline)
    right = harness.build_baseline_state(restored)
    assert baseline == restored
    assert_state_equal(left, right)


def test_blank_state_is_zero_except_for_uniform_kappa():
    state = harness.build_blank_state(8, kappa_value=0.4)
    assert np.count_nonzero(state["psi"]) == 0
    assert np.count_nonzero(state["phi"]) == 0
    assert np.count_nonzero(state["mu"]) == 0
    assert np.array_equal(state["kappa"], np.full((8, 8), 0.4))


def test_invalid_baseline_is_rejected():
    with pytest.raises(ValueError):
        harness.GaussianDevelopmentalBaseline(grid_size=2)


def test_checkpoint_round_trip_preserves_arrays_config_and_hash():
    ExecutionPolicy.init_core_determinism(seed=1729, device_mode="numpy")
    config = CoreConfig(use_mu=True, noise_strength=0.003)
    state = harness.run_steps(
        harness.build_baseline_state(harness.GaussianDevelopmentalBaseline()),
        config,
        3,
    )
    checkpoint = harness.create_checkpoint(state, config, step_index=3)
    serialized = harness.serialize_checkpoint(checkpoint)
    restored_state, restored_config, restored_step = harness.load_checkpoint(serialized)
    assert restored_step == 3
    assert restored_config == config
    assert_state_equal(state, restored_state)
    assert hashlib.sha256(serialized).hexdigest() == hashlib.sha256(
        harness.serialize_checkpoint(checkpoint)
    ).hexdigest()


def test_restored_checkpoint_continues_bitwise_when_rng_state_is_transferred():
    ExecutionPolicy.init_core_determinism(seed=314159, device_mode="numpy")
    config = CoreConfig(use_mu=True, noise_strength=0.004)
    donor = harness.run_steps(
        harness.build_baseline_state(harness.GaussianDevelopmentalBaseline()),
        config,
        5,
    )
    serialized = harness.serialize_checkpoint(
        harness.create_checkpoint(donor, config, step_index=5)
    )
    uninterrupted = harness.run_steps(donor, config, 7)
    recipient_state, recipient_config, recipient_step = harness.load_checkpoint(
        serialized
    )
    restored = harness.run_steps(recipient_state, recipient_config, 7)
    assert recipient_step == 5
    assert_state_equal(uninterrupted, restored)


def test_reset_rng_breaks_exact_continuation_when_noise_is_active():
    ExecutionPolicy.init_core_determinism(seed=271828, device_mode="numpy")
    config = CoreConfig(use_mu=True, noise_strength=0.004)
    donor = harness.run_steps(
        harness.build_baseline_state(harness.GaussianDevelopmentalBaseline()),
        config,
        5,
    )
    serialized = harness.serialize_checkpoint(
        harness.create_checkpoint(donor, config, step_index=5)
    )
    uninterrupted = harness.run_steps(donor, config, 7)
    recipient_state, recipient_config, _ = harness.load_checkpoint(
        serialized, restore_rng=False
    )
    np.random.seed(999)
    reset_history = harness.run_steps(recipient_state, recipient_config, 7)
    assert not np.array_equal(uninterrupted["psi"], reset_history["psi"])


def test_integrity_hash_rejects_modified_checkpoint():
    ExecutionPolicy.init_core_determinism(seed=42, device_mode="numpy")
    baseline = harness.GaussianDevelopmentalBaseline()
    checkpoint = harness.create_checkpoint(
        harness.build_baseline_state(baseline), CoreConfig(), step_index=0
    )
    modified = json.loads(harness.serialize_checkpoint(checkpoint))
    modified["step_index"] = 1
    with pytest.raises(harness.CheckpointFormatError, match="integrity hash mismatch"):
        harness.load_checkpoint(modified)


def test_same_baseline_and_history_replay_donor_bitwise():
    result = harness.run_baseline_state_matrix()
    for key in ("psi", "phi", "kappa", "mu"):
        assert result["same_history_replay"][key]["bitwise_equal"]


def test_independent_history_breaks_exact_reconstruction():
    result = harness.run_baseline_state_matrix()
    receipt = result["independent_history_at_transplant"]
    assert not receipt["psi"]["bitwise_equal"]
    assert receipt["psi"]["nrmse"] > 0.0


def test_live_state_only_and_baseline_plus_live_state_are_identical():
    result = harness.run_baseline_state_matrix()
    lanes = result["lanes_after_common_challenge"]
    for lane in ("X1_live_state_only", "BX_baseline_plus_live_state"):
        for key in ("psi", "phi", "kappa", "mu"):
            assert lanes[lane][key]["bitwise_equal"]
    assert not result["baseline_runtime_causal_input"]


def test_baseline_only_and_blank_do_not_match_donor_reference():
    result = harness.run_baseline_state_matrix()
    lanes = result["lanes_after_common_challenge"]
    for lane in ("N0_blank", "B1_baseline_independent_history"):
        assert not lanes[lane]["psi"]["bitwise_equal"]
        assert lanes[lane]["psi"]["nrmse"] > 0.0


def test_checkpoint_pilot_receipt_matches_declared_behavior():
    result = harness.run_checkpoint_pilot()
    full = result["full_transfer"]
    assert full["psi_bitwise_equal"]
    assert full["phi_bitwise_equal"]
    assert full["kappa_bitwise_equal"]
    assert full["mu_bitwise_equal"]
    assert full["max_abs_psi_difference"] == 0.0
    assert not result["reset_rng_control"]["psi_bitwise_equal"]
    assert result["reset_rng_control"]["max_abs_psi_difference"] > 0.0
