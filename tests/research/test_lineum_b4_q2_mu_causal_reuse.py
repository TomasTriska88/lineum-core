from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "research" / "runners" / "lineum_b4_q2_mu_causal_reuse.py"
SPEC = importlib.util.spec_from_file_location("lineum_b4_q2_m1", RUNNER_PATH)
assert SPEC is not None and SPEC.loader is not None
m1 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = m1
SPEC.loader.exec_module(m1)


def test_frozen_schedule_and_representatives_are_exact():
    schedule = m1.nuisance_schedule()
    assert len(schedule) == 30
    assert schedule[12] == (12.0, 2.5, 0, 0)
    assert schedule[17] == (12.0, 3.5, 0, 0)
    train, held = m1.split_variant_masks(len(schedule))
    assert int(np.sum(train)) == 20
    assert int(np.sum(held)) == 10
    assert all(train[index] == (index % 3 in (0, 1)) for index in range(30))


def test_orientation_pair_uses_row_column_convention_and_equal_energy():
    psi_a, psi_b = m1.make_orientation_pair(64, 12.0, 2.5, 0, 0)
    np.testing.assert_allclose(np.sum(np.abs(psi_a) ** 2), 1.0, rtol=0, atol=1e-14)
    np.testing.assert_allclose(np.sum(np.abs(psi_b) ** 2), 1.0, rtol=0, atol=1e-14)
    np.testing.assert_allclose(psi_b, psi_a.T, rtol=0, atol=1e-14)
    assert m1.quadrupole_score(m1.field_weight("psi", psi_a)) > 0.0
    assert m1.quadrupole_score(m1.field_weight("psi", psi_b)) < 0.0


def test_shift_x_moves_columns_and_shift_y_moves_rows():
    base_a, _ = m1.make_orientation_pair(64, 12.0, 2.5, 0, 0)
    shifted_x, _ = m1.make_orientation_pair(64, 12.0, 2.5, 3, 0)
    shifted_y, _ = m1.make_orientation_pair(64, 12.0, 2.5, 0, -2)
    np.testing.assert_allclose(shifted_x, np.roll(base_a, (0, 3), axis=(0, 1)))
    np.testing.assert_allclose(shifted_y, np.roll(base_a, (-2, 0), axis=(0, 1)))


def test_p0_observers_are_known_answer_on_pristine_family():
    audit = m1.p0_observer_audit(m1.nuisance_schedule())
    assert audit["passed"] is True
    assert audit["quadrupole"]["balanced_accuracy"] >= 0.95
    assert audit["pooled"]["balanced_accuracy"] >= 0.95
    assert audit["quadrupole"]["permutation_p"] <= 0.01
    assert audit["pooled"]["permutation_p"] <= 0.01
    assert audit["transpose_antisymmetry_error"] <= 1e-12


def test_observer_random_stream_contract_is_deterministic_and_independent():
    a = m1.observer_rng("mu", 2001, 20).normal(size=8)
    b = m1.observer_rng("mu", 2001, 20).normal(size=8)
    c = m1.observer_rng("mu", 2001, 21).normal(size=8)
    np.testing.assert_array_equal(a, b)
    assert not np.array_equal(a, c)


def test_analytic_mu_decay_matches_frozen_closed_form():
    mu0 = np.array([[0.25, 0.5], [1.0, 2.0]], dtype=float)
    observed = m1.analytic_mu_decay(mu0, mu_rho=0.0001, dt=0.1, steps=2000)
    expected = mu0 * (1.0 - 0.0001 * 0.1) ** 2000
    np.testing.assert_allclose(observed, expected, rtol=0, atol=1e-15)


def test_step_receipt_detects_stable_core_fail_safe_marker():
    state = m1.make_state(m1.make_common_state(8, 2.0))

    def fake_step(current, cfg):
        print("!!! LINEUM FAIL-SAFE (CPU): Numeric divergence detected. Resetting Psi. !!!")
        out = m1.clone_state(current)
        out["psi"][:] = 0.0
        return out

    out, reset_seen, captured = m1.step_with_receipt(state, object(), fake_step)
    assert reset_seen is True
    assert m1.FAIL_SAFE_MARKER in captured
    assert np.max(np.abs(out["psi"])) == 0.0


def test_interventions_use_source_off_state_and_equal_common_psi():
    common = m1.make_common_state(8, 2.0)
    source = m1.make_state(common)
    source["phi"][:] = np.arange(64).reshape(8, 8)
    source["mu"][:] = np.arange(64).reshape(8, 8) / 100.0
    source["psi"][:] = 0.0

    c0 = m1.apply_intervention(source, "C0", common)
    c1 = m1.apply_intervention(source, "C1", common)
    c2 = m1.apply_intervention(source, "C2", common)
    c3 = m1.apply_intervention(source, "C3", common)

    for lane in (c0, c1, c2, c3):
        np.testing.assert_array_equal(lane["psi"], common)
    assert np.count_nonzero(c0["phi"]) == 0
    assert np.count_nonzero(c0["mu"]) == 0
    np.testing.assert_array_equal(c1["phi"], source["phi"])
    np.testing.assert_array_equal(c1["mu"], source["mu"])
    np.testing.assert_array_equal(c2["phi"], source["phi"])
    assert np.count_nonzero(c2["mu"]) == 0
    assert np.count_nonzero(c3["phi"]) == 0
    np.testing.assert_array_equal(c3["mu"], source["mu"])


def test_quarter_turn_rotates_spatial_channels_and_preserves_metadata():
    state = {
        "psi": np.arange(9).reshape(3, 3).astype(complex),
        "phi": np.arange(9).reshape(3, 3).astype(float) + 10,
        "mu": np.arange(9).reshape(3, 3).astype(float) + 20,
        "kappa": np.ones((3, 3)),
        "telemetry": {
            "N_t": 1.25,
            "is_nan": False,
            "guards": {"cap_triggers": 0, "fold_triggers": 0},
        },
    }
    cloned = m1.clone_state(state)
    rotated = m1.rotate_state_quarter_turn(cloned)

    for channel in ("psi", "phi", "mu", "kappa"):
        np.testing.assert_array_equal(rotated[channel], np.rot90(state[channel]))

    assert isinstance(rotated["telemetry"], dict)
    assert rotated["telemetry"] == state["telemetry"]
    assert rotated["telemetry"] is not state["telemetry"]
    assert rotated["telemetry"]["guards"] is not state["telemetry"]["guards"]
    rotated["telemetry"]["guards"]["cap_triggers"] = 1
    assert state["telemetry"]["guards"]["cap_triggers"] == 0


def test_causal_floors_and_zeroing_reduction_are_frozen():
    assert m1.full_history_floor(0.0) == 1e-4
    assert m1.single_channel_floor(0.0) == 5e-5
    assert m1.full_history_floor(2e-5) == 2e-4
    assert m1.single_channel_floor(2e-5) == 1e-4
    assert m1.zeroing_reduction(1.0, 0.5) == 0.5
    assert m1.zeroing_reduction(1.0, 0.25) == 0.75


def test_c3_cap_control_requires_matching_qualitative_status_and_ratio_when_active():
    passed = m1.c3_cap_control_pass(
        primary_value=2e-4,
        cap_value=2.2e-4,
        primary_d_null=0.0,
        cap_d_null=0.0,
        primary_valid=True,
        cap_valid=True,
    )
    assert passed["passed"] is True

    mismatch = m1.c3_cap_control_pass(
        primary_value=2e-4,
        cap_value=1e-6,
        primary_d_null=0.0,
        cap_d_null=0.0,
        primary_valid=True,
        cap_valid=True,
    )
    assert mismatch["passed"] is False

    ratio_fail = m1.c3_cap_control_pass(
        primary_value=1e-4,
        cap_value=3e-4,
        primary_d_null=0.0,
        cap_d_null=0.0,
        primary_valid=True,
        cap_valid=True,
    )
    assert ratio_fail["passed"] is False


def test_scale_control_freezes_c0_c3_signature_and_active_ratios():
    primary = {"C0": 0.0, "C1": 2e-4, "C2": 2e-5, "C3": 1e-4}
    control = {"C0": 0.0, "C1": 2.5e-4, "C2": 1e-5, "C3": 1.2e-4}
    receipt = m1.scale_control_pass(primary, control, primary_valid=True, control_valid=True)
    assert receipt["passed"] is True
    assert receipt["primary_signature"] == receipt["control_signature"]

    signature_fail = dict(control)
    signature_fail["C2"] = 1e-4
    receipt = m1.scale_control_pass(
        primary, signature_fail, primary_valid=True, control_valid=True
    )
    assert receipt["passed"] is False


def test_lane_validity_uses_fail_safe_caps_and_source_off_gate():
    good = m1.TraceReceipt(
        finite=True,
        reset_seen=False,
        max_abs_psi=1.0,
        max_phi=2.0,
        max_mu=1.0,
        source_off_psi_max=0.0,
    )
    assert m1.lane_valid(good, mu_cap=10.0, require_source_off=True)

    reset = m1.TraceReceipt(**{**good.__dict__, "reset_seen": True})
    assert not m1.lane_valid(reset, mu_cap=10.0, require_source_off=True)
    cap = m1.TraceReceipt(**{**good.__dict__, "max_mu": 2.5})
    assert not m1.lane_valid(cap, mu_cap=10.0, require_source_off=True)
    leak = m1.TraceReceipt(**{**good.__dict__, "source_off_psi_max": 2e-15})
    assert not m1.lane_valid(leak, mu_cap=10.0, require_source_off=True)


def _causal_summary(c0, c1, c2, c3, *, valid=True):
    def row(value):
        return {
            "median_divergence": {"psi": value, "phi": 0.0, "mu": 0.0},
            "valid": valid,
            "common_state_equal": True,
        }

    return {"C0": row(c0), "C1": row(c1), "C2": row(c2), "C3": row(c3)}


def test_classification_retains_mu_only_when_primary_and_all_nuisance_gates_pass():
    summary = _causal_summary(0.0, 4e-4, 1e-4, 2e-4)
    result = m1.classify_primary(
        p0_valid=True,
        primary_histories_valid=True,
        cap_histories_valid=True,
        passive_mu_pass=True,
        cap_independence_pass=True,
        causal_summary=summary,
        c3_cap_pass=True,
        full_grid_pass=True,
        c3_grid_pass=True,
        dt_control_pass=True,
        resolution_control_pass=True,
    )
    assert result["mu_candidate_pass"] is True
    assert result["outcome"] == "mu_causal_reuse_candidate_retained"

    confounded = m1.classify_primary(
        p0_valid=True,
        primary_histories_valid=True,
        cap_histories_valid=True,
        passive_mu_pass=True,
        cap_independence_pass=True,
        causal_summary=summary,
        c3_cap_pass=True,
        full_grid_pass=True,
        c3_grid_pass=False,
        dt_control_pass=True,
        resolution_control_pass=True,
    )
    assert confounded["mu_candidate_pass"] is False
    assert confounded["outcome"] == "inconclusive_or_confounded"


def test_classification_can_report_passive_mu_without_causal_reuse():
    summary = _causal_summary(0.0, 2e-4, 1e-4, 1e-6)
    result = m1.classify_primary(
        p0_valid=True,
        primary_histories_valid=True,
        cap_histories_valid=True,
        passive_mu_pass=True,
        cap_independence_pass=True,
        causal_summary=summary,
        c3_cap_pass=True,
        full_grid_pass=True,
        c3_grid_pass=True,
        dt_control_pass=True,
        resolution_control_pass=True,
    )
    assert result["c3_single_pass"] is False
    assert result["outcome"] == "mu_passive_archive_without_demonstrated_causal_reuse"


def test_git_blob_sha_helper_known_answer():
    assert m1.git_blob_sha1_bytes(b"test\n") == "9daeafb9864cf43055ae93beb0afd6c7d144bfa4"


def test_active_core_config_binds_exact_frozen_deterministic_subset():
    CoreConfig, ExecutionPolicy, _ = m1.core_bindings()
    cfg = m1.make_core_config(CoreConfig, dt=0.1)
    assert cfg.dt == 0.1
    assert cfg.stencil_type == "LAP4"
    assert cfg.drift_strength == 0.0
    assert cfg.disable_quantum_noise is True
    assert cfg.use_mode_coupling is False
    assert cfg.phi_diffusion_scales_with_dt is True
    assert cfg.use_mu is True
    assert cfg.mu_eta == 0.005
    assert cfg.mu_rho == 0.0001
    assert cfg.mu_cap == 10.0
    assert ExecutionPolicy.uses_pytorch() is False


def test_frozen_source_identity_gate_matches_branch_checkout():
    receipt = m1.verify_frozen_sources(ROOT)
    assert receipt["passed"] is True
