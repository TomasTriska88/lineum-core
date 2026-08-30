from __future__ import annotations

import copy
import importlib.util
import inspect
import json
import math
from pathlib import Path
import sys
from typing import Any

import numpy as np
import pytest


ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = (
    ROOT / "research" / "runners" / "lineum_b4_q2_m2_rwc1_local_reciprocal_work.py"
)
PROTOCOL_PATH = (
    ROOT / "research" / "lineum-public-tolog-b4" / "q2-m2-rwc1-preregistration.json"
)


def _load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


runner = _load_module(RUNNER_PATH, "lineum_b4_q2_m2_rwc1_test_subject")


@pytest.fixture
def protocol() -> dict[str, Any]:
    return json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))


def test_local_law_negative_zero_full_and_zero_stock_branches() -> None:
    psi, phi, receipt = runner.local_reciprocal_work(
        np.array([[1.0 + 0.0j]]),
        np.array([[0.25]]),
        np.array([[-0.5 + 0.0j]]),
    )
    assert psi[0, 0] == 0.5 + 0.0j
    assert phi[0, 0] == pytest.approx(1.0)
    assert receipt["negative_cell_count"] == 1
    assert receipt["aggregate_residual"] == pytest.approx(0.0, abs=1e-15)

    psi, phi, receipt = runner.local_reciprocal_work(
        np.array([[1.0 + 0.0j]]), np.array([[0.4]]), np.array([[-2.0 + 0.0j]])
    )
    assert psi[0, 0] == -1.0 + 0.0j
    assert phi[0, 0] == 0.4
    assert receipt["zero_cell_count"] == 1

    psi, phi, _ = runner.local_reciprocal_work(
        np.array([[1.0 + 0.0j]]), np.array([[4.0]]), np.array([[1.0 + 0.0j]])
    )
    assert psi[0, 0] == pytest.approx(2.0 + 0.0j)
    assert phi[0, 0] == pytest.approx(1.0)

    psi, phi, receipt = runner.local_reciprocal_work(
        np.array([[1.0 + 0.0j]]), np.array([[0.0]]), np.array([[1.0 + 0.0j]])
    )
    assert psi[0, 0] == 1.0 + 0.0j
    assert phi[0, 0] == 0.0
    assert receipt["rejected_positive_work_sum"] == pytest.approx(3.0)


def test_local_law_partial_phase_zero_psi_and_antipodal_tie() -> None:
    p = np.array([[1.0 + 0.0j]])
    psi, phi, _ = runner.local_reciprocal_work(
        p, np.array([[0.25]]), np.array([[0.0 + 1.0j]])
    )
    assert abs(psi[0, 0]) == pytest.approx(math.sqrt(1.25))
    assert 0.0 < np.angle(psi[0, 0]) < np.angle(1.0 + 1.0j)
    assert psi[0, 0] != 1.0 + 1.0j
    assert phi[0, 0] == pytest.approx(0.0)

    psi, phi, _ = runner.local_reciprocal_work(
        np.array([[0.0 + 0.0j]]), np.array([[1.0]]), np.array([[0.0 + 1.0j]])
    )
    assert psi[0, 0] == pytest.approx(0.0 + 1.0j)
    assert phi[0, 0] == pytest.approx(0.0)

    z = complex(-2.0, -0.0)
    psi, _, _ = runner.local_reciprocal_work(
        np.array([[1.0 + 0.0j]]),
        np.array([[1.5]]),
        np.array([[z - 1.0]]),
    )
    assert np.angle(psi[0, 0]) > 0.0
    assert np.angle(psi[0, 0]) == pytest.approx(math.pi / 2.0)


def test_local_law_receipt_closes_full_array_and_preconditions_fail_closed() -> None:
    p = np.array([[1.0 + 0.2j, 0.4 - 0.3j], [0.0 + 0.0j, -0.6 + 0.1j]])
    b = np.array([[0.1, 0.0], [0.8, 0.3]])
    increment = np.array([[0.2 + 0.4j, -0.1 + 0.1j], [0.4j, 0.5 - 0.2j]])
    psi, phi, receipt = runner.local_reciprocal_work(p, b, increment)
    assert np.max(np.abs((np.abs(psi) ** 2 + phi) - (np.abs(p) ** 2 + b))) <= 1e-14
    assert receipt["max_cellwise_normalized_residual_ratio"] <= 1.0
    assert receipt["positive_cell_count"] + receipt["negative_cell_count"] + receipt["zero_cell_count"] == 4
    with pytest.raises(runner.CandidatePreconditionError):
        runner.local_reciprocal_work(p, np.array([[-1.0, 0.0], [0.0, 0.0]]), increment)
    with pytest.raises(runner.CandidatePreconditionError):
        runner.local_reciprocal_work(p, b, np.full_like(p, np.nan + 0.0j))
    with pytest.raises(runner.CandidatePreconditionError):
        runner.local_reciprocal_work(p, b[:1], increment)


def test_global_pool_allocation_boundaries_and_aggregate_closure() -> None:
    p = np.ones((1, 2), dtype=np.complex128)
    psi, phi, receipt = runner.global_pool_reciprocal_work(
        p, np.zeros((1, 2)), np.ones((1, 2), dtype=np.complex128)
    )
    assert receipt["A"] == 0.0 and receipt["P"] == 6.0
    assert receipt["D"] == 0.0 and receipt["q"] == 0.0
    assert np.array_equal(psi, p) and np.array_equal(phi, np.zeros((1, 2)))

    _, _, full = runner.global_pool_reciprocal_work(
        p, np.full((1, 2), 4.0), np.ones((1, 2), dtype=np.complex128)
    )
    assert full["q"] == pytest.approx(1.0)
    assert full["remaining"] == pytest.approx(2.0)

    psi, phi, partial = runner.global_pool_reciprocal_work(
        p, np.array([[1.0, 0.0]]), np.ones((1, 2), dtype=np.complex128)
    )
    assert partial["q"] == pytest.approx(1.0 / 6.0)
    assert partial["aggregate_residual"] == pytest.approx(0.0, abs=1e-14)
    assert np.sum(np.abs(psi) ** 2 + phi) == pytest.approx(np.sum(np.abs(p) ** 2 + np.array([[1.0, 0.0]])))

    _, _, no_positive = runner.global_pool_reciprocal_work(
        p, np.zeros((1, 2)), -0.5 * np.ones((1, 2), dtype=np.complex128)
    )
    assert no_positive["P"] == 0.0 and no_positive["q"] == 1.0


def test_global_pool_zero_work_cell_keeps_z_and_joins_redistribution() -> None:
    psi_before = np.ones((1, 3), dtype=np.complex128)
    phi_before = np.array([[0.5, 1.0, 1.5]], dtype=np.float64)
    increment = np.array([[1.0, -0.5, -2.0]], dtype=np.complex128)
    psi_after, phi_after, receipt = runner.global_pool_reciprocal_work(
        psi_before, phi_before, increment
    )

    assert psi_after[0, 0] == pytest.approx(2.0 + 0.0j)
    assert psi_after[0, 1] == pytest.approx(0.5 + 0.0j)
    assert psi_after[0, 2] == pytest.approx(-1.0 + 0.0j)
    assert phi_after == pytest.approx(np.array([[0.1, 0.35, 0.3]]))
    assert receipt["positive_cell_count"] == 1
    assert receipt["negative_cell_count"] == 1
    assert receipt["zero_cell_count"] == 1
    assert receipt["A"] == pytest.approx(3.75)
    assert receipt["P"] == pytest.approx(3.0)
    assert receipt["D"] == pytest.approx(3.0)
    assert receipt["q"] == pytest.approx(1.0)
    assert receipt["remaining"] == pytest.approx(0.75)
    assert receipt["accepted_signed_work_sum"] == pytest.approx(2.25)
    assert receipt["sum_proxy_before"] == pytest.approx(6.0)
    assert receipt["sum_proxy_after"] == pytest.approx(6.0)
    assert receipt["aggregate_residual"] == pytest.approx(0.0, abs=1e-15)


def test_candidate_signature_has_no_reference_target_or_protocol_input() -> None:
    assert tuple(inspect.signature(runner.local_reciprocal_work).parameters) == (
        "psi_before", "phi_before", "increment"
    )
    source = inspect.getsource(runner.local_reciprocal_work)
    for forbidden in ("prepared", "expected", "target", "observer", "fixture", "protocol"):
        assert forbidden not in source.lower()


def test_historical_proposals_and_control_step_match_reference_for_both_stencils(protocol: dict[str, Any]) -> None:
    reference = runner._load_reference_runner(ROOT)
    size = int(protocol["baseline"]["grid_size"])
    row, column = np.indices((size, size), dtype=float)
    psi = np.exp(-((row - 15.5) ** 2 + (column - 15.5) ** 2) / 18.0).astype(np.complex128)
    phi = 0.2 + 0.01 * row + 0.02 * column
    kappa = np.ones((size, size))
    mu = np.zeros((size, size))
    token = object()
    flow, interaction = runner.historical_proposals(psi, phi, kappa, mu, 1.0, token)
    clipped = np.clip(phi, 0.0, 10.0)
    raw = 0.04 * clipped
    expected_interaction = 0.1 * np.tanh(raw / 0.1) * psi
    expected_interaction /= 1.0 + np.abs(expected_interaction) / 10.0
    gx, gy = np.gradient(phi, axis=(0, 1))
    expected_flow = -0.004 * (gx + 1j * gy)
    expected_flow /= 1.0 + np.abs(expected_flow) / 10.0
    assert np.array_equal(flow.increment, expected_flow)
    assert np.array_equal(interaction.increment, expected_interaction)

    lane_arrays = reference.build_lane_arrays([(reference.LANES[0], 0.0)])
    for stencil in runner.STENCILS:
        expected_psi, expected_phi, *_ = reference.advance_batch_one_step(
            psi[None, ...].copy(), phi[None, ...].copy(), kappa[None, ...], mu[None, ...], stencil, lane_arrays
        )
        psi2, phi2, cap, receipts, source_valid = runner._apply_branch_stages(
            0, psi, phi, flow, interaction, token, 1e6
        )
        actual_psi, actual_phi, phi_cap, reset, nonfinite = runner._common_tail(
            reference, psi2, phi2, kappa, stencil, 1.0, 1e6, 1e6, 0.99
        )
        assert source_valid and not cap and not receipts
        assert not phi_cap and not reset and not nonfinite
        assert np.array_equal(actual_psi, expected_psi[0])
        assert np.array_equal(actual_phi, expected_phi[0])


def test_all_six_stage_orders_and_receipt_only_identity() -> None:
    p = np.array([[1.0 + 0.0j, 0.5 + 0.0j]])
    b = np.array([[0.5, 0.5]])
    token = object()
    flow = runner.Proposal(np.array([[0.2 + 0.0j, -0.1 + 0.0j]]), token, "flow")
    interaction = runner.Proposal(np.array([[0.0 + 0.2j, 0.1 + 0.0j]]), token, "interaction")
    states = {}
    receipts = {}
    for branch in range(6):
        psi, phi, cap, rows, source_valid = runner._apply_branch_stages(
            branch, p, b, flow, interaction, token, 1e6
        )
        assert source_valid and not cap
        states[branch] = (psi, phi)
        receipts[branch] = [stage for stage, _ in rows]
    assert np.array_equal(states[0][0], states[1][0])
    assert np.array_equal(states[0][1], states[1][1])
    assert receipts == {0: [], 1: [0, 1], 2: [1], 3: [0], 4: [0, 1], 5: []}
    assert not np.array_equal(states[2][0], states[3][0])
    assert np.all(states[4][1] >= 0.0) and np.all(states[5][1] >= 0.0)
    wrong = runner.Proposal(flow.increment, object(), "flow")
    with pytest.raises(runner.TechnicalTrajectoryError):
        runner._apply_branch_stages(0, p, b, wrong, interaction, token, 1e6)


def test_metrics_boundaries_outcome_precedence_and_zero_energy(protocol: dict[str, Any]) -> None:
    thresholds = protocol["thresholds"]
    row = {
        "finite": True,
        "psi_energy_relative_error": thresholds["psi_energy_relative_error_max"],
        "psi_radial_profile_relative_l2_error": thresholds["psi_radial_profile_relative_l2_max"],
        "phi_radial_profile_relative_l2_error": thresholds["phi_radial_profile_relative_l2_max"],
        "half_energy_radius_absolute_change": thresholds["half_energy_radius_change_max_cells"],
        "fixed_center_displacement": thresholds["center_displacement_from_fixed_grid_center_max_cells"],
        "energy_fraction_radius_6": thresholds["energy_fraction_within_radius_6_min"],
    }
    assert runner._absolute_checkpoint_pass(row, thresholds)
    row["energy_fraction_radius_6"] = math.nextafter(
        thresholds["energy_fraction_within_radius_6_min"], 0.0
    )
    assert not runner._absolute_checkpoint_pass(row, thresholds)

    gates = {name: True for name in protocol["retention"]["primary_output_contract"]["gates_fields"]}
    comparisons = [{"passed": True}] * 12
    assert runner.classify_outcome(gates, comparisons) == "rwc1_local_advantage_clean_gate_passed"
    gates["local_advantage"] = False
    assert runner.classify_outcome(gates, comparisons) == "rwc1_clean_gate_passed_locality_not_identified"
    gates["pair_both_absolute_clean"] = False
    assert runner.classify_outcome(gates, comparisons) == "rwc1_mixed_or_partial_only"
    comparisons = [{"passed": False}] * 12
    assert runner.classify_outcome(gates, comparisons) == "rwc1_unsupported_under_tested_conditions"
    gates["runtime"] = False
    assert runner.classify_outcome(gates, comparisons) == "rwc1_technical_non_result"

    zeros = np.zeros((32, 32), dtype=np.complex128)
    with pytest.raises(runner.TechnicalTrajectoryError):
        runner.state_metrics(zeros, np.zeros((32, 32)), zeros, np.zeros((32, 32)))


def test_exact_maps_shards_indices_and_record_type_bijection(protocol: dict[str, Any]) -> None:
    runner.validate_protocol(protocol)
    retention = protocol["retention"]
    assert retention["evidence_total_records"] == 400110
    assert [(s["first_record_index"], s["last_record_index"], s["count"]) for s in retention["evidence_shards"]] == [
        (0, 109, 110), (110, 120109, 120000), (120110, 240109, 120000),
        (240110, 300109, 60000), (300110, 360109, 60000), (360110, 400109, 40000),
    ]
    assert runner.local_record_index(0, 1, 1, 0) == 240110
    assert runner.local_record_index(0, 1, 10000, 1) == 260109
    assert runner.local_record_index(0, 2, 1, 1) == 260110
    assert runner.local_record_index(1, 4, 10000, 1) == 360109
    assert runner.global_record_index(0, 1, 0) == 360110
    assert runner.global_record_index(1, 10000, 1) == 400109
    assert set(retention["evidence_record_types"]) == set(retention["evidence_record_schemas"])


def test_all_400110_frozen_record_coordinates_are_unique_contiguous_and_ordered(protocol: dict[str, Any]) -> None:
    index = 0
    for stencil_index in range(2):
        assert stencil_index == index
        index += 1
    for stencil_index in range(2):
        for branch_index in range(6):
            for checkpoint_index, _step in enumerate(protocol["baseline"]["checkpoints"]):
                calculated = 2 + stencil_index * 54 + branch_index * 9 + checkpoint_index
                assert calculated == index
                index += 1
    for start in (110, 120110):
        assert index == start
        for stencil_index in range(2):
            for branch_index in range(6):
                for step in range(1, 10001):
                    calculated = start + stencil_index * 60000 + branch_index * 10000 + step - 1
                    assert calculated == index
                    index += 1
    assert index == 240110
    for stencil_index in range(2):
        for branch_index in runner.LOCAL_STAGE_MAP:
            for step in range(1, 10001):
                for stage_index in runner.LOCAL_STAGE_MAP[branch_index]:
                    assert runner.local_record_index(
                        stencil_index, branch_index, step, stage_index
                    ) == index
                    index += 1
    assert index == 360110
    for stencil_index in range(2):
        for step in range(1, 10001):
            for stage_index in range(2):
                assert runner.global_record_index(stencil_index, step, stage_index) == index
                index += 1
    assert index == 400110


def _mini_protocol(protocol: dict[str, Any], *, byte_cap: int = 10000) -> dict[str, Any]:
    value = copy.deepcopy(protocol)
    value["retention"]["evidence_max_shard_bytes"] = byte_cap
    return value


def test_canonical_serializer_and_jsonl_writer_identity(tmp_path: Path, protocol: dict[str, Any]) -> None:
    record = {
        "record_index": 110,
        "record_type": "step_energy",
        "stencil_index": 0,
        "branch_index": 0,
        "step": 1,
        "total_psi_energy": 1.25,
    }
    spec = {"path": "evidence.jsonl", "count": 1, "first_record_index": 110, "last_record_index": 110}
    path = tmp_path / "evidence.jsonl"
    identity = runner.write_jsonl_shard(path, [record], spec, _mini_protocol(protocol))
    data = path.read_bytes()
    assert data == runner.canonical_json_bytes(record, final_lf=True)
    assert data.endswith(b"\n") and b"\r" not in data and not data.startswith(b"\xef\xbb\xbf")
    assert identity.bytes == len(data) and identity.sha256 == runner.hashlib.sha256(data).hexdigest()
    assert identity.git_blob == runner._git_blob_bytes(data)
    with pytest.raises(ValueError):
        runner.canonical_json_bytes({"bad": math.nan}, final_lf=True)

    bad_type = dict(record, step=True)
    with pytest.raises(runner.ContractError):
        runner.validate_evidence_record(bad_type, protocol)
    bad_numeric_string = dict(record, total_psi_energy="1.25")
    with pytest.raises(runner.ContractError, match="finite binary64 number"):
        runner.validate_evidence_record(bad_numeric_string, protocol)
    bad_numeric_boolean = dict(record, total_psi_energy=True)
    with pytest.raises(runner.ContractError, match="finite binary64 number"):
        runner.validate_evidence_record(bad_numeric_boolean, protocol)
    bad_numeric_integer = dict(record, total_psi_energy=1)
    with pytest.raises(runner.ContractError, match="finite binary64 number"):
        runner.validate_evidence_record(bad_numeric_integer, protocol)
    bad_key = dict(record, extra=1)
    with pytest.raises(runner.ContractError):
        runner.validate_evidence_record(bad_key, protocol)
    bad_coordinate = dict(record, branch_index=1)
    with pytest.raises(runner.ContractError, match="coordinates"):
        runner.validate_evidence_record(bad_coordinate, protocol)
    bad_order = tmp_path / "bad-order.jsonl"
    with pytest.raises(runner.ContractError):
        runner.write_jsonl_shard(bad_order, [dict(record, record_index=111)], spec, _mini_protocol(protocol))

    floating_state = {
        "record_index": 0,
        "record_type": "prepared_state",
        "stencil_index": 0,
        "psi_real": [[0.0] * 32 for _ in range(32)],
        "psi_imag": [[0.0] * 32 for _ in range(32)],
        "phi": [[0.0] * 32 for _ in range(32)],
    }
    runner.validate_evidence_record(floating_state, protocol)
    integer_state = copy.deepcopy(floating_state)
    integer_state["phi"][0][0] = 0
    with pytest.raises(runner.ContractError, match="wrong shape or non-finite"):
        runner.validate_evidence_record(integer_state, protocol)


def test_strict_json_reader_rejects_duplicate_keys_and_nonfinite_tokens(tmp_path: Path) -> None:
    duplicate = tmp_path / "duplicate.json"
    duplicate.write_text('{"value":1,"value":2}\n', encoding="utf-8")
    with pytest.raises(runner.ContractError, match="Duplicate"):
        runner.load_json_object(duplicate)
    nonfinite = tmp_path / "nonfinite.json"
    nonfinite.write_text('{"value":NaN}\n', encoding="utf-8")
    with pytest.raises(runner.ContractError, match="Non-finite"):
        runner.load_json_object(nonfinite)


def test_jsonl_writer_enforces_byte_cap_and_final_count(tmp_path: Path, protocol: dict[str, Any]) -> None:
    record = {
        "record_index": 110,
        "record_type": "step_energy",
        "stencil_index": 0,
        "branch_index": 0,
        "step": 1,
        "total_psi_energy": 1.0,
    }
    spec = {"path": "tiny.jsonl", "count": 1, "first_record_index": 110, "last_record_index": 110}
    with pytest.raises(runner.ContractError, match="byte cap"):
        runner.write_jsonl_shard(tmp_path / "tiny.jsonl", [record], spec, _mini_protocol(protocol, byte_cap=1))
    with pytest.raises(runner.ContractError, match="count or range"):
        runner.write_jsonl_shard(tmp_path / "empty.jsonl", [], spec, _mini_protocol(protocol))


def test_six_shards_publish_before_primary_and_partial_failure_has_no_primary(tmp_path: Path, protocol: dict[str, Any]) -> None:
    value = copy.deepcopy(protocol)
    value["planned_paths"]["primary_evidence_shards"] = [f"out/shard-{index}.jsonl" for index in range(6)]
    value["planned_paths"]["primary_output"] = "out/primary.json"
    staged = []
    for index in range(6):
        path = tmp_path / f"staged-{index}.jsonl"
        path.write_bytes(f"{index}\n".encode("ascii"))
        staged.append(path)
    primary = tmp_path / "staged-primary.json"
    primary.write_bytes(b"{}\n")
    shard_identities = [
        runner.ShardIdentity(
            path=value["planned_paths"]["primary_evidence_shards"][index],
            bytes=len(path.read_bytes()),
            sha256=runner.hashlib.sha256(path.read_bytes()).hexdigest(),
            git_blob=runner._git_blob_bytes(path.read_bytes()),
            record_count=1,
            first_record_index=index,
            last_record_index=index,
        )
        for index, path in enumerate(staged)
    ]
    primary_identity = runner.FileIdentity(
        path=value["planned_paths"]["primary_output"],
        bytes=len(primary.read_bytes()),
        sha256=runner.hashlib.sha256(primary.read_bytes()).hexdigest(),
        git_blob=runner._git_blob_bytes(primary.read_bytes()),
    )
    order: list[int] = []
    runner.publish_staged_artifacts(
        tmp_path,
        value,
        staged,
        shard_identities,
        primary,
        primary_identity,
        before_copy=lambda index, *_: order.append(index),
    )
    assert order == [0, 1, 2, 3, 4, 5, 6]
    assert (tmp_path / "out" / "primary.json").read_bytes() == b"{}\n"
    with pytest.raises(runner.ContractError):
        runner.publish_staged_artifacts(
            tmp_path, value, staged, shard_identities, primary, primary_identity
        )

    failed_root = tmp_path / "failed"
    failed_root.mkdir()
    def fail_on_fourth(index: int, *_: Any) -> None:
        if index == 3:
            raise OSError("synthetic copy failure")
    with pytest.raises(OSError):
        runner.publish_staged_artifacts(
            failed_root,
            value,
            staged,
            shard_identities,
            primary,
            primary_identity,
            before_copy=fail_on_fourth,
        )
    assert not (failed_root / "out" / "primary.json").exists()


def test_publish_readback_rejects_short_or_changed_shard_before_primary(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    protocol: dict[str, Any],
) -> None:
    value = copy.deepcopy(protocol)
    value["planned_paths"]["primary_evidence_shards"] = [f"out/shard-{index}.jsonl" for index in range(6)]
    value["planned_paths"]["primary_output"] = "out/primary.json"
    staged = []
    identities = []
    for index in range(6):
        path = tmp_path / f"source-{index}.jsonl"
        data = f"record-{index}\n".encode("ascii")
        path.write_bytes(data)
        staged.append(path)
        identities.append(
            runner.ShardIdentity(
                path=value["planned_paths"]["primary_evidence_shards"][index],
                bytes=len(data),
                sha256=runner.hashlib.sha256(data).hexdigest(),
                git_blob=runner._git_blob_bytes(data),
                record_count=1,
                first_record_index=index,
                last_record_index=index,
            )
        )
    primary = tmp_path / "source-primary.json"
    primary.write_bytes(b"{}\n")
    primary_identity = runner.FileIdentity(
        value["planned_paths"]["primary_output"],
        3,
        runner.hashlib.sha256(b"{}\n").hexdigest(),
        runner._git_blob_bytes(b"{}\n"),
    )
    original_copy = runner._copy_exclusive
    def short_copy(source: Path, destination: Path) -> None:
        if destination.name == "shard-0.jsonl":
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(source.read_bytes()[:-1])
        else:
            original_copy(source, destination)
    monkeypatch.setattr(runner, "_copy_exclusive", short_copy)
    with pytest.raises(runner.ContractError, match="read-back"):
        runner.publish_staged_artifacts(
            tmp_path, value, staged, identities, primary, primary_identity
        )
    assert not (tmp_path / "out" / "primary.json").exists()

    changed_root = tmp_path / "changed"
    changed_root.mkdir()
    staged[0].write_bytes(b"changed-after-identity\n")
    monkeypatch.setattr(runner, "_copy_exclusive", original_copy)
    with pytest.raises(runner.ContractError, match="changed before"):
        runner.publish_staged_artifacts(
            changed_root, value, staged, identities, primary, primary_identity
        )
    assert not (changed_root / "out" / "primary.json").exists()


def test_primary_marker_short_hidden_copy_never_reaches_final_path(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    protocol: dict[str, Any],
) -> None:
    value = copy.deepcopy(protocol)
    value["planned_paths"]["primary_evidence_shards"] = [
        f"out/shard-{index}.jsonl" for index in range(6)
    ]
    value["planned_paths"]["primary_output"] = "out/primary.json"
    staged: list[Path] = []
    identities: list[Any] = []
    for index in range(6):
        source = tmp_path / f"marker-source-{index}.jsonl"
        data = f"record-{index}\n".encode("ascii")
        source.write_bytes(data)
        staged.append(source)
        identities.append(
            runner.ShardIdentity(
                path=value["planned_paths"]["primary_evidence_shards"][index],
                bytes=len(data),
                sha256=runner.hashlib.sha256(data).hexdigest(),
                git_blob=runner._git_blob_bytes(data),
                record_count=1,
                first_record_index=index,
                last_record_index=index,
            )
        )
    primary = tmp_path / "marker-source-primary.json"
    primary_data = b"{}\n"
    primary.write_bytes(primary_data)
    primary_identity = runner.FileIdentity(
        path=value["planned_paths"]["primary_output"],
        bytes=len(primary_data),
        sha256=runner.hashlib.sha256(primary_data).hexdigest(),
        git_blob=runner._git_blob_bytes(primary_data),
    )
    original_hidden_copy = runner._copy_primary_to_hidden_temp

    def short_hidden_copy(source: Path, destination: Path) -> Path:
        hidden = original_hidden_copy(source, destination)
        hidden.write_bytes(hidden.read_bytes()[:-1])
        return hidden

    monkeypatch.setattr(runner, "_copy_primary_to_hidden_temp", short_hidden_copy)
    with pytest.raises(runner.ContractError, match="Hidden primary"):
        runner.publish_staged_artifacts(
            tmp_path, value, staged, identities, primary, primary_identity
        )
    assert not (tmp_path / "out" / "primary.json").exists()
    assert not list((tmp_path / "out").glob(".primary.json.*.tmp"))


def test_primary_latch_is_exclusive_and_terminal_update_keeps_path(tmp_path: Path, protocol: dict[str, Any]) -> None:
    value = copy.deepcopy(protocol)
    value["planned_paths"]["primary_execution_receipt"] = "out/receipt.json"
    identity = runner.FileIdentity("protocol.json", 2, "0" * 64, "0" * 40)
    preflight = {
        "actual_head_commit": "1" * 40,
        "actual_runner_filtered_git_blob": "2" * 40,
        "actual_runner_test_filtered_git_blob": "3" * 40,
        "actual": {},
        "runtime_gate": {"passed": True, "backend": "cpu_numpy_deterministic", "python": "3.11.15", "numpy": "1.26.4"},
    }
    path = runner.create_primary_latch(tmp_path, value, identity, preflight)
    started = path.read_bytes()
    with pytest.raises(FileExistsError):
        runner.create_primary_latch(tmp_path, value, identity, preflight)
    runner.update_primary_receipt(
        path,
        status="technical_non_result",
        elapsed_seconds=1.0,
        output_identity=None,
        stderr_identity=None,
        failure={"phase": "synthetic", "code": "SyntheticFailure", "sanitized_message": "synthetic"},
    )
    assert path.exists() and path.read_bytes() != started
    terminal = json.loads(path.read_text(encoding="utf-8"))
    assert terminal["authority_consumed"] is True
    assert terminal["retry_authorized"] is False
    assert terminal["status"] == "technical_non_result"
    assert terminal["canonical_payload_sha256_without_self"] == runner.canonical_payload_sha256_without_self(terminal)
    assert not list(path.parent.glob(f".{path.name}.*.tmp"))


def test_failure_receipt_sanitizes_machine_local_paths_and_primary_claim_is_boolean() -> None:
    failure = runner._terminal_failure(
        RuntimeError("failed at C:\\Users\\private-user\\workspace\\secret.json"),
        "synthetic",
    )
    assert failure["sanitized_message"] == "technical_failure_during_synthetic"
    assert "private-user" not in failure["sanitized_message"]
    assert runner.PRIMARY_CLAIM_ONLY is True


def test_implementation_checkpoint_scope_is_literal_and_exact(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    captured: list[list[str]] = []

    def fake_git(_root: Path, arguments: list[str]) -> str:
        captured.append(arguments)
        return "\n".join(sorted(runner.IMPLEMENTATION_CHECKPOINT_PATHS))

    monkeypatch.setattr(runner, "_run_git", fake_git)
    head = "1" * 40
    assert runner.git_implementation_checkpoint_paths(
        tmp_path, head
    ) == runner.IMPLEMENTATION_CHECKPOINT_PATHS
    assert captured == [
        [
            "diff",
            "--name-only",
            "--no-renames",
            runner.PROTOCOL_REMOTE_CHECKPOINT_COMMIT,
            head,
            "--",
        ]
    ]
    assert runner.IMPLEMENTATION_CHECKPOINT_PATHS == {
        runner.PRIMARY_RUNNER_RELATIVE_PATH,
        runner.PRIMARY_TEST_RELATIVE_PATH,
        runner.REPORT_RELATIVE_PATH,
        runner.MANIFEST_RELATIVE_PATH,
    }
    assert (
        runner.FROZEN_REMOTE_REF
        == "refs/remotes/origin/codex/q2-m30-endogenous-balance-20260830"
    )


def test_primary_and_checker_style_dual_identity_preflights(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, protocol: dict[str, Any]) -> None:
    expected = runner.PreflightExpectations(
        execution_commit="1" * 40,
        remote_readback_commit="1" * 40,
        runner_git_blob="2" * 40,
        runner_test_git_blob="3" * 40,
        report_git_blob="4" * 40,
        manifest_git_blob="5" * 40,
    )
    remote_state = {"commit": expected.execution_commit}
    scope_state = {"paths": runner.IMPLEMENTATION_CHECKPOINT_PATHS}
    primary_context: tuple[dict[str, Any], dict[str, Any], dict[str, str]] | None = None
    for lane in ("primary", "checker"):
        value = copy.deepcopy(protocol)
        if lane == "checker":
            value["planned_paths"]["runner"] = value["planned_paths"]["checker"]
            value["planned_paths"]["runner_test"] = value["planned_paths"]["checker_test"]
            value["planned_paths"]["primary_output"] = value["planned_paths"]["checker_output"]
            value["planned_paths"]["primary_execution_receipt"] = value["planned_paths"]["checker_execution_receipt"]
        manifest = {
            "files": {
                runner.PROTOCOL_RELATIVE_PATH: {"bytes": 0, "sha256": "", "git_blob_sha": ""},
                value["planned_paths"]["runner"]: {"git_blob_sha": expected.runner_git_blob},
                value["planned_paths"]["runner_test"]: {"git_blob_sha": expected.runner_test_git_blob},
            },
            "source_report": runner.REPORT_RELATIVE_PATH,
            "q2_m2_rwc1": {"continuity_report_git_blob": expected.report_git_blob},
        }
        source_expected = value["source_bindings"]
        blobs = {
            value["planned_paths"]["runner"]: expected.runner_git_blob,
            value["planned_paths"]["runner_test"]: expected.runner_test_git_blob,
            runner.REPORT_RELATIVE_PATH: expected.report_git_blob,
            runner.MANIFEST_RELATIVE_PATH: expected.manifest_git_blob,
            "lineum_core/math.py": source_expected["core_math_git_blob"],
            runner.REFERENCE_RUNNER_RELATIVE_PATH: source_expected["localized_reference_runner_git_blob"],
            "requirements.txt": source_expected["requirements_git_blob"],
            "requirements-dev.txt": source_expected["requirements_dev_git_blob"],
        }
        if lane == "primary":
            primary_context = (value, manifest, blobs)
        monkeypatch.setattr(runner, "git_head", lambda _root: expected.execution_commit)
        monkeypatch.setattr(
            runner, "git_remote_ref_commit", lambda _root: remote_state["commit"]
        )
        monkeypatch.setattr(
            runner,
            "git_implementation_checkpoint_paths",
            lambda _root, _head: scope_state["paths"],
        )
        monkeypatch.setattr(runner, "git_filtered_blob", lambda _root, path: blobs[path])
        monkeypatch.setattr(runner, "git_head_blob", lambda _root, path: blobs[path])
        monkeypatch.setattr(runner, "_run_git", lambda _root, _args: "")
        monkeypatch.setattr(
            runner,
            "strict_runtime_gate",
            lambda _protocol: {"passed": True, "backend": "cpu_numpy_deterministic", "python": "3.11.15", "numpy": "1.26.4"},
        )
        result = runner.verify_primary_preflight(
            tmp_path, value, manifest, expected, require_clean=True, allow_existing_receipt=False
        )
        assert result["passed"] and result["worktree_clean"]
        assert result["implementation_scope_exact"]
        assert result["actual_runner_filtered_git_blob"] == result["actual_runner_head_git_blob"] == expected.runner_git_blob

    assert primary_context is not None
    value, manifest, blobs = primary_context
    monkeypatch.setattr(runner, "git_filtered_blob", lambda _root, path: blobs[path])
    monkeypatch.setattr(runner, "git_head_blob", lambda _root, path: blobs[path])
    mismatch = runner.PreflightExpectations(
        execution_commit=expected.execution_commit,
        remote_readback_commit="6" * 40,
        runner_git_blob=expected.runner_git_blob,
        runner_test_git_blob=expected.runner_test_git_blob,
        report_git_blob=expected.report_git_blob,
        manifest_git_blob=expected.manifest_git_blob,
    )
    result = runner.verify_primary_preflight(
        tmp_path, value, manifest, mismatch, require_clean=True, allow_existing_receipt=False
    )
    assert not result["passed"]

    remote_state["commit"] = "7" * 40
    result = runner.verify_primary_preflight(
        tmp_path, value, manifest, expected, require_clean=True, allow_existing_receipt=False
    )
    assert not result["passed"]
    assert result["remote_readback_commit"] == "7" * 40
    remote_state["commit"] = expected.execution_commit

    scope_state["paths"] = runner.IMPLEMENTATION_CHECKPOINT_PATHS - {
        runner.REPORT_RELATIVE_PATH
    }
    result = runner.verify_primary_preflight(
        tmp_path, value, manifest, expected, require_clean=True, allow_existing_receipt=False
    )
    assert not result["passed"] and not result["implementation_scope_exact"]
    scope_state["paths"] = runner.IMPLEMENTATION_CHECKPOINT_PATHS | {
        "unrelated/edited.py"
    }
    result = runner.verify_primary_preflight(
        tmp_path, value, manifest, expected, require_clean=True, allow_existing_receipt=False
    )
    assert not result["passed"] and not result["implementation_scope_exact"]
    scope_state["paths"] = runner.IMPLEMENTATION_CHECKPOINT_PATHS

    for checker_name in (
        "checker",
        "checker_test",
        "checker_output",
        "checker_execution_receipt",
    ):
        checker_path = runner.repository_path(
            tmp_path, value["planned_paths"][checker_name]
        )
        checker_path.parent.mkdir(parents=True, exist_ok=True)
        checker_path.write_text("synthetic pre-authored checker", encoding="utf-8")
        result = runner.verify_primary_preflight(
            tmp_path,
            value,
            manifest,
            expected,
            require_clean=True,
            allow_existing_receipt=False,
        )
        assert not result["passed"] and not result["outputs_absent"]
        checker_path.unlink()


def test_protocol_identity_is_rooted_in_remote_checkpoint_and_rejects_tampering(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    protocol: dict[str, Any],
) -> None:
    destination = tmp_path / runner.PROTOCOL_RELATIVE_PATH
    destination.parent.mkdir(parents=True)
    frozen_bytes = PROTOCOL_PATH.read_bytes()
    destination.write_bytes(frozen_bytes)
    manifest = {
        "files": {
            runner.PROTOCOL_RELATIVE_PATH: {
                "bytes": runner.PROTOCOL_EXPECTED_BYTES,
                "sha256": runner.PROTOCOL_EXPECTED_SHA256,
                "git_blob_sha": runner.PROTOCOL_EXPECTED_GIT_BLOB,
            }
        }
    }
    filtered = {"value": runner.PROTOCOL_EXPECTED_GIT_BLOB}
    ancestry = {"value": True}
    monkeypatch.setattr(runner, "git_filtered_blob", lambda *_: filtered["value"])
    monkeypatch.setattr(runner, "git_head_blob", lambda *_: runner.PROTOCOL_EXPECTED_GIT_BLOB)
    monkeypatch.setattr(runner, "git_is_ancestor", lambda *_: ancestry["value"])
    identity = runner.validate_protocol_identity(tmp_path, protocol, manifest)
    assert identity.bytes == 37448
    assert identity.sha256 == runner.PROTOCOL_EXPECTED_SHA256

    destination.write_bytes(frozen_bytes + b" ")
    with pytest.raises(runner.ContractError, match="bytes differ"):
        runner.validate_protocol_identity(tmp_path, protocol, manifest)
    destination.write_bytes(frozen_bytes)

    tampered_manifest = copy.deepcopy(manifest)
    tampered_manifest["files"][runner.PROTOCOL_RELATIVE_PATH]["sha256"] = "0" * 64
    with pytest.raises(runner.ContractError, match="identity mismatch"):
        runner.validate_protocol_identity(tmp_path, protocol, tampered_manifest)

    filtered["value"] = "0" * 40
    with pytest.raises(runner.ContractError, match="Filtered"):
        runner.validate_protocol_identity(tmp_path, protocol, manifest)
    filtered["value"] = runner.PROTOCOL_EXPECTED_GIT_BLOB
    ancestry["value"] = False
    with pytest.raises(runner.ContractError, match="ancestor"):
        runner.validate_protocol_identity(tmp_path, protocol, manifest)


def test_synthetic_orchestration_is_exactly_lap4_then_lap8_without_retry(protocol: dict[str, Any]) -> None:
    calls: list[tuple[str, int]] = []
    sentinels = [object(), object()]
    def fake(stencil: str, index: int) -> Any:
        calls.append((stencil, index))
        return sentinels[index]
    assert runner.orchestrate_stencils(protocol, fake) == sentinels
    assert calls == [("LAP4", 0), ("LAP8", 1)]
    parser_actions = {action.dest for action in runner.build_parser()._actions}
    assert not parser_actions & {"grid_size", "seed", "noise", "dt", "stencil", "steps", "threshold"}


def test_reference_import_disables_repository_bytecode_writes(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(sys, "dont_write_bytecode", False)
    reference = runner._load_reference_runner(ROOT)
    assert reference is not None
    assert sys.dont_write_bytecode is True


def _synthetic_primary(protocol: dict[str, Any]) -> dict[str, Any]:
    contract = protocol["retention"]["primary_output_contract"]
    source_names = {
        "core_math_git_blob", "localized_reference_runner_git_blob",
        "requirements_git_blob", "requirements_dev_git_blob",
    }
    expected_source_bindings = {
        "core_math_git_blob": protocol["source_bindings"]["core_math_git_blob"],
        "localized_reference_runner_git_blob": protocol["source_bindings"][
            "localized_reference_runner_git_blob"
        ],
        "requirements_git_blob": protocol["source_bindings"]["requirements_git_blob"],
        "requirements_dev_git_blob": protocol["source_bindings"][
            "requirements_dev_git_blob"
        ],
    }
    source_gate = {name: "1" * 40 for name in contract["source_identity_gate_fields"]}
    source_gate.update(
        {
            "passed": True,
            "head_equals_remote_readback_commit": True,
            "worktree_clean": True,
            "expected": dict(expected_source_bindings),
            "actual": dict(expected_source_bindings),
        }
    )
    checkpoints = []
    for stencil_index in range(2):
        for branch_index in range(6):
            for checkpoint_index, step in enumerate(protocol["baseline"]["checkpoints"]):
                row = {name: 0.0 for name in contract["checkpoint_metric_fields"]}
                row.update(
                    {
                        "stencil_index": stencil_index,
                        "branch_index": branch_index,
                        "checkpoint_index": checkpoint_index,
                        "step": step,
                        "total_psi_energy": 1.0,
                        "psi_radial_profile": [0.0] * 22,
                        "phi_radial_profile": [0.0] * 22,
                        "finite": True,
                    }
                )
                checkpoints.append(row)
    trajectory = []
    telemetry = []
    for stencil_index in range(2):
        for branch_index in range(6):
            trajectory.append(
                {
                    "stencil_index": stencil_index,
                    "branch_index": branch_index,
                    "record_count": 10000,
                    "pre_total_psi_energy": 1.0,
                    "minimum_total_psi_energy": 1.0,
                    "maximum_total_psi_energy": 1.0,
                    "minimum_energy_ratio": 1.0,
                    "maximum_energy_ratio": 1.0,
                    "first_lower_bound_violation_step": None,
                    "first_upper_bound_violation_step": None,
                }
            )
            telemetry.append(
                {
                    "stencil_index": stencil_index,
                    "branch_index": branch_index,
                    "record_count": 10000,
                    **{f"{name}_count": 0 for name in runner.TELEMETRY_FIELDS},
                }
            )
    comparisons = []
    descriptors = []
    for stencil_index in range(2):
        for step in protocol["thresholds"]["comparison_horizons"]:
            for metric in ("psi_energy_relative_error", "psi_radial_profile_relative_l2_error"):
                descriptors.append(("pair_both_vs_control", stencil_index, step, metric, 0, 4))
    for stencil_index in range(2):
        for step in protocol["thresholds"]["comparison_horizons"]:
            descriptors.append(("pair_both_vs_global_pool", stencil_index, step, "psi_radial_profile_relative_l2_error", 5, 4))
    for index, (kind, stencil, step, metric, reference, candidate) in enumerate(descriptors):
        tolerance = protocol["thresholds"]["comparison_absolute"]
        comparisons.append(
            {
                "comparison_index": index,
                "comparison_kind": kind,
                "stencil_index": stencil,
                "step": step,
                "metric": metric,
                "reference_branch_index": reference,
                "candidate_branch_index": candidate,
                "reference_value": 0.0,
                "candidate_value": 0.0,
                "tolerance": tolerance,
                "improvement": 0.0,
                "passed": False,
            }
        )
    gates = {name: True for name in contract["gates_fields"]}
    gates["pair_both_absolute_clean"] = False
    gates["pair_both_causal_improvement"] = False
    gates["local_advantage"] = False
    shards = [
        {
            "path": spec["path"],
            "bytes": 1,
            "sha256": f"{index + 1:064x}",
            "record_count": spec["count"],
            "first_record_index": spec["first_record_index"],
            "last_record_index": spec["last_record_index"],
        }
        for index, spec in enumerate(protocol["retention"]["evidence_shards"])
    ]
    payload = {
        "canonical_payload_sha256_without_self": "0" * 64,
        "checkpoint_metrics": checkpoints,
        "claim_boundary": copy.deepcopy(protocol["claim_boundary"]),
        "classification": {
            "outcome": "rwc1_unsupported_under_tested_conditions",
            "primary_claim_only": True,
        },
        "comparisons": comparisons,
        "evidence_identity": {"shard_count": 6, "total_record_count": 400110, "shards": shards},
        "execution_identity": {
            "attempt": 1, "trajectory_execution_count": 1, "stencil_count": 2,
            "branch_count": 6, "continuation_steps": 10000,
        },
        "gates": gates,
        "index_maps": copy.deepcopy(protocol["retention"]["evidence_index_maps"]),
        "protocol_identity": {
            "path": runner.PROTOCOL_RELATIVE_PATH,
            "schema": protocol["schema"],
            "bytes": runner.PROTOCOL_EXPECTED_BYTES,
            "sha256": runner.PROTOCOL_EXPECTED_SHA256,
            "git_blob": runner.PROTOCOL_EXPECTED_GIT_BLOB,
        },
        "runtime_gate": {
            "passed": True, "backend": "cpu_numpy_deterministic",
            "python": "3.11.15", "numpy": "1.26.4",
        },
        "schema": runner.PRIMARY_SCHEMA,
        "source_identity_gate": source_gate,
        "technical_telemetry_summaries": telemetry,
        "trajectory_energy_summaries": trajectory,
    }
    payload["canonical_payload_sha256_without_self"] = runner.canonical_payload_sha256_without_self(payload)
    return payload


def test_primary_schema_validator_freezes_exact_types_nulls_hash_and_classifier(protocol: dict[str, Any]) -> None:
    payload = _synthetic_primary(protocol)
    runner.validate_primary_payload(payload, protocol)

    wrong_claim = copy.deepcopy(payload)
    wrong_claim["classification"]["primary_claim_only"] = "true"
    with pytest.raises(runner.ContractError, match="Boolean true"):
        runner.validate_primary_payload(wrong_claim, protocol)

    wrong_integer = copy.deepcopy(payload)
    wrong_integer["execution_identity"]["attempt"] = True
    with pytest.raises(runner.ContractError, match="integers"):
        runner.validate_primary_payload(wrong_integer, protocol)

    wrong_shard_index = copy.deepcopy(payload)
    wrong_shard_index["evidence_identity"]["shards"][0][
        "first_record_index"
    ] = False
    wrong_shard_index["canonical_payload_sha256_without_self"] = (
        runner.canonical_payload_sha256_without_self(wrong_shard_index)
    )
    with pytest.raises(runner.ContractError, match="shard identity value"):
        runner.validate_primary_payload(wrong_shard_index, protocol)

    wrong_index_map = copy.deepcopy(payload)
    wrong_index_map["index_maps"]["checkpoint_index"][0] = False
    wrong_index_map["canonical_payload_sha256_without_self"] = (
        runner.canonical_payload_sha256_without_self(wrong_index_map)
    )
    with pytest.raises(runner.ContractError, match="index-map types"):
        runner.validate_primary_payload(wrong_index_map, protocol)

    wrong_null = copy.deepcopy(payload)
    wrong_null["checkpoint_metrics"][0]["phi_mean"] = None
    with pytest.raises(runner.ContractError):
        runner.validate_primary_payload(wrong_null, protocol)

    wrong_float_integer = copy.deepcopy(payload)
    wrong_float_integer["checkpoint_metrics"][0]["total_psi_energy"] = 1
    wrong_float_integer["canonical_payload_sha256_without_self"] = (
        runner.canonical_payload_sha256_without_self(wrong_float_integer)
    )
    with pytest.raises(runner.ContractError, match="finite binary64"):
        runner.validate_primary_payload(wrong_float_integer, protocol)

    wrong_profile_integer = copy.deepcopy(payload)
    wrong_profile_integer["checkpoint_metrics"][0]["psi_radial_profile"][0] = 0
    wrong_profile_integer["canonical_payload_sha256_without_self"] = (
        runner.canonical_payload_sha256_without_self(wrong_profile_integer)
    )
    with pytest.raises(runner.ContractError, match="finite binary64"):
        runner.validate_primary_payload(wrong_profile_integer, protocol)

    wrong_protocol_identity = copy.deepcopy(payload)
    wrong_protocol_identity["protocol_identity"]["sha256"] = "2" * 64
    wrong_protocol_identity["canonical_payload_sha256_without_self"] = (
        runner.canonical_payload_sha256_without_self(wrong_protocol_identity)
    )
    with pytest.raises(runner.ContractError, match="immutable v3 checkpoint"):
        runner.validate_primary_payload(wrong_protocol_identity, protocol)

    incoherent_source = copy.deepcopy(payload)
    incoherent_source["source_identity_gate"]["actual_runner_head_git_blob"] = "2" * 40
    incoherent_source["canonical_payload_sha256_without_self"] = (
        runner.canonical_payload_sha256_without_self(incoherent_source)
    )
    with pytest.raises(runner.ContractError, match="passed flag is incoherent"):
        runner.validate_primary_payload(incoherent_source, protocol)

    incoherent_remote_flag = copy.deepcopy(payload)
    incoherent_remote_flag["source_identity_gate"][
        "head_equals_remote_readback_commit"
    ] = False
    incoherent_remote_flag["canonical_payload_sha256_without_self"] = (
        runner.canonical_payload_sha256_without_self(incoherent_remote_flag)
    )
    with pytest.raises(runner.ContractError, match="comparison flag is incoherent"):
        runner.validate_primary_payload(incoherent_remote_flag, protocol)

    incoherent_top_gate = copy.deepcopy(payload)
    incoherent_top_gate["gates"]["identity"] = False
    incoherent_top_gate["canonical_payload_sha256_without_self"] = (
        runner.canonical_payload_sha256_without_self(incoherent_top_gate)
    )
    with pytest.raises(runner.ContractError, match="identity gate disagrees"):
        runner.validate_primary_payload(incoherent_top_gate, protocol)

    wrong_hash = copy.deepcopy(payload)
    wrong_hash["canonical_payload_sha256_without_self"] = "f" * 64
    with pytest.raises(runner.ContractError, match="hash mismatch"):
        runner.validate_primary_payload(wrong_hash, protocol)
