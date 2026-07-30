import numpy as np
import pytest

from lineum_core.developmental_baseline import (
    GaussianDevelopmentalBaseline,
    build_baseline_state,
    build_blank_state,
)
from scripts.run_core_baseline_state_matrix import run_matrix


def test_baseline_record_round_trip_rebuilds_identical_state():
    baseline = GaussianDevelopmentalBaseline()
    restored = GaussianDevelopmentalBaseline.from_record(baseline.to_record())
    left = build_baseline_state(baseline)
    right = build_baseline_state(restored)

    assert baseline == restored
    for key in ("psi", "phi", "kappa", "mu"):
        assert np.array_equal(left[key], right[key])


def test_blank_state_is_zero_except_for_uniform_kappa():
    state = build_blank_state(8, kappa_value=0.4)

    assert np.count_nonzero(state["psi"]) == 0
    assert np.count_nonzero(state["phi"]) == 0
    assert np.count_nonzero(state["mu"]) == 0
    assert np.array_equal(state["kappa"], np.full((8, 8), 0.4))


def test_invalid_baseline_is_rejected():
    with pytest.raises(ValueError):
        GaussianDevelopmentalBaseline(grid_size=2)


def test_same_baseline_and_history_replay_donor_bitwise():
    result = run_matrix()

    for key in ("psi", "phi", "kappa", "mu"):
        assert result["same_history_replay"][key]["bitwise_equal"]


def test_independent_developmental_history_breaks_exact_reconstruction():
    result = run_matrix()

    assert not result["independent_history_at_transplant"]["psi"][
        "bitwise_equal"
    ]
    assert result["independent_history_at_transplant"]["psi"]["nrmse"] > 0.0


def test_live_state_only_and_baseline_plus_live_state_are_identical():
    result = run_matrix()
    lanes = result["lanes_after_common_challenge"]

    for lane in ("X1_live_state_only", "BX_baseline_plus_live_state"):
        for key in ("psi", "phi", "kappa", "mu"):
            assert lanes[lane][key]["bitwise_equal"]
    assert not result["baseline_runtime_causal_input"]


def test_baseline_only_and_blank_do_not_match_donor_reference():
    result = run_matrix()
    lanes = result["lanes_after_common_challenge"]

    for lane in ("N0_blank", "B1_baseline_independent_history"):
        assert not lanes[lane]["psi"]["bitwise_equal"]
        assert lanes[lane]["psi"]["nrmse"] > 0.0
