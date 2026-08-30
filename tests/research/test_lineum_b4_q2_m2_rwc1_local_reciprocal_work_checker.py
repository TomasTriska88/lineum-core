from __future__ import annotations

import ast
import hashlib
import importlib.util
import io
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pytest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
CHECKER_FILE = (
    REPOSITORY_ROOT
    / "research"
    / "runners"
    / "lineum_b4_q2_m2_rwc1_local_reciprocal_work_checker.py"
)
SPEC = importlib.util.spec_from_file_location("rwc1_independent_checker", CHECKER_FILE)
assert SPEC is not None and SPEC.loader is not None
checker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = checker
SPEC.loader.exec_module(checker)


BRANCHES = [
    "CONTROL",
    "RECEIPT_ONLY",
    "PAIR_INTERACTION",
    "PAIR_FLOW",
    "PAIR_BOTH",
    "GLOBAL_POOL_PAIR_BOTH",
]
STENCILS = ["LAP4", "LAP8"]
STAGES = ["flow", "interaction"]


def synthetic_protocol() -> dict[str, Any]:
    prepared_fields = [
        "record_index",
        "record_type",
        "stencil_index",
        "psi_real",
        "psi_imag",
        "phi",
    ]
    checkpoint_fields = [
        "record_index",
        "record_type",
        "stencil_index",
        "branch_index",
        "checkpoint_index",
        "step",
        "psi_real",
        "psi_imag",
        "phi",
    ]
    local_fields = [
        "record_index",
        "record_type",
        "stencil_index",
        "branch_index",
        "step",
        "stage_index",
        "precondition_passed",
        "positive_cell_count",
        "negative_cell_count",
        "zero_cell_count",
        "accepted_signed_work_sum",
        "rejected_positive_work_sum",
        "sum_abs_accepted_signed_work",
        "sum_proxy_before",
        "sum_proxy_after",
        "aggregate_residual",
        "aggregate_scale",
        "max_cellwise_normalized_residual_ratio",
        "argmax_flat_index",
        "argmax_row",
        "argmax_column",
        "argmax_proxy_before",
        "argmax_proxy_after",
        "argmax_accepted_signed_work",
        "argmax_residual",
        "argmax_scale",
    ]
    global_fields = [
        "record_index",
        "record_type",
        "stencil_index",
        "branch_index",
        "step",
        "stage_index",
        "precondition_passed",
        "positive_cell_count",
        "negative_cell_count",
        "zero_cell_count",
        "accepted_signed_work_sum",
        "rejected_positive_work_sum",
        "sum_abs_accepted_signed_work",
        "sum_proxy_before",
        "sum_proxy_after",
        "aggregate_residual",
        "aggregate_scale",
        "P",
        "A",
        "D",
        "q",
        "remaining",
        "max_abs_cellwise_residual",
        "sum_abs_cellwise_residuals",
    ]
    shard_specs = [
        ("synthetic/000.jsonl", 26, 0, 25),
        ("synthetic/001.jsonl", 12, 26, 37),
        ("synthetic/002.jsonl", 12, 38, 49),
        ("synthetic/003.jsonl", 6, 50, 55),
        ("synthetic/004.jsonl", 6, 56, 61),
        ("synthetic/005.jsonl", 4, 62, 65),
    ]
    checkpoint_metric_fields = [
        "stencil_index",
        "branch_index",
        "checkpoint_index",
        "step",
        "total_psi_energy",
        "psi_energy_relative_error",
        "psi_radial_profile",
        "psi_radial_profile_relative_l2_error",
        "phi_radial_profile",
        "phi_radial_profile_relative_l2_error",
        "half_energy_radius",
        "half_energy_radius_absolute_change",
        "centroid_row",
        "centroid_column",
        "fixed_center_displacement",
        "centroid_shift_from_pre",
        "energy_fraction_radius_3",
        "energy_fraction_radius_6",
        "energy_fraction_radius_10",
        "phi_min",
        "phi_mean",
        "phi_max",
        "phi_total",
        "max_abs_psi",
        "finite",
    ]
    return {
        "schema": "synthetic.protocol.v1",
        "baseline": {"grid_size": 2, "continuation_steps": 1},
        "runtime": {
            "backend": "cpu_numpy_deterministic",
            "python": checker.platform.python_version(),
            "numpy": np.__version__,
        },
        "metrics": {
            "energy_relative_error_denominator": "abs(pre_total) + 1e-30",
            "profile_relative_l2_denominator": "l2(pre_profile) + 1e-30",
        },
        "thresholds": {
            "absolute_clean_gate_checkpoints": [1],
            "center_displacement_from_fixed_grid_center_max_cells": 0.5,
            "comparison_absolute": 1e-8,
            "comparison_horizons": [1, 1],
            "comparison_relative": 1e-12,
            "energy_fraction_within_radius_6_min": 0.5,
            "half_energy_radius_change_max_cells": 1.0,
            "local_and_global_aggregate_receipt_multiplier": 1e-10,
            "local_cellwise_normalized_residual_ratio_max": 1.0,
            "phi_radial_profile_relative_l2_max": 0.1,
            "psi_energy_relative_error_max": 0.05,
            "psi_radial_profile_relative_l2_max": 0.1,
            "whole_trajectory_psi_energy_lower_ratio": 0.95,
            "whole_trajectory_psi_energy_upper_ratio": 1.05,
        },
        "outcome_map": [
            "synthetic_technical",
            "synthetic_local",
            "synthetic_clean",
            "synthetic_mixed",
            "synthetic_negative",
        ],
        "claim_boundary": {"synthetic_claim": False},
        "retention": {
            "checker_limitations": ["synthetic_limited_check"],
            "evidence_max_shard_bytes": 1_000_000,
            "evidence_total_records": 66,
            "evidence_index_maps": {
                "branch_index": BRANCHES,
                "checkpoint_index": [0, 1],
                "stage_index": STAGES,
                "stencil_index": STENCILS,
            },
            "evidence_shards": [
                {
                    "path": path,
                    "count": count,
                    "first_record_index": first,
                    "last_record_index": last,
                }
                for path, count, first, last in shard_specs
            ],
            "evidence_record_schemas": {
                "prepared_state": {
                    "array_shape": [2, 2],
                    "count": 2,
                    "fields": prepared_fields,
                },
                "checkpoint_state": {
                    "array_shape": [2, 2],
                    "count": 24,
                    "fields": checkpoint_fields,
                },
                "step_energy": {
                    "count": 12,
                    "fields": [
                        "record_index",
                        "record_type",
                        "stencil_index",
                        "branch_index",
                        "step",
                        "total_psi_energy",
                    ],
                },
                "step_telemetry": {
                    "count": 12,
                    "fields": [
                        "record_index",
                        "record_type",
                        "stencil_index",
                        "branch_index",
                        "step",
                        "psi_cap_contact",
                        "phi_cap_contact",
                        "destructive_reset",
                        "nonfinite_detected",
                        "negative_phi_input_detected",
                        "undeclared_source_detected",
                    ],
                },
                "local_stage_receipt": {"count": 12, "fields": local_fields},
                "global_stage_receipt": {"count": 4, "fields": global_fields},
            },
            "primary_output_contract": {
                "checkpoint_metric_count": 24,
                "checkpoint_metric_fields": checkpoint_metric_fields,
                "checkpoint_profile_length": 1,
                "comparison_count": 12,
            },
        },
    }


def state_arrays() -> tuple[list[list[float]], list[list[float]], list[list[float]]]:
    real = [[1.0, 1.0], [1.0, 1.0]]
    imaginary = [[0.0, 0.0], [0.0, 0.0]]
    phi = [[0.0, 0.0], [0.0, 0.0]]
    return real, imaginary, phi


def synthetic_record(
    protocol: dict[str, Any], shard_index: int, ordinal: int
) -> dict[str, Any]:
    spec = protocol["retention"]["evidence_shards"][shard_index]
    record_type, descriptor = checker._expected_record_descriptor(
        protocol, shard_index, ordinal
    )
    record_index = spec["first_record_index"] + ordinal
    base: dict[str, Any] = {
        "record_index": record_index,
        "record_type": record_type,
        **descriptor,
    }
    if record_type in {"prepared_state", "checkpoint_state"}:
        real, imaginary, phi = state_arrays()
        base.update({"psi_real": real, "psi_imag": imaginary, "phi": phi})
    elif record_type == "step_energy":
        base["total_psi_energy"] = 4.0
    elif record_type == "step_telemetry":
        base.update(
            {
                "psi_cap_contact": False,
                "phi_cap_contact": False,
                "destructive_reset": False,
                "nonfinite_detected": False,
                "negative_phi_input_detected": False,
                "undeclared_source_detected": False,
            }
        )
    elif record_type == "local_stage_receipt":
        base.update(
            {
                "precondition_passed": True,
                "positive_cell_count": 0,
                "negative_cell_count": 0,
                "zero_cell_count": 4,
                "accepted_signed_work_sum": 0.0,
                "rejected_positive_work_sum": 0.0,
                "sum_abs_accepted_signed_work": 0.0,
                "sum_proxy_before": 4.0,
                "sum_proxy_after": 4.0,
                "aggregate_residual": 0.0,
                "aggregate_scale": 4.0,
                "max_cellwise_normalized_residual_ratio": 0.0,
                "argmax_flat_index": 0,
                "argmax_row": 0,
                "argmax_column": 0,
                "argmax_proxy_before": 1.0,
                "argmax_proxy_after": 1.0,
                "argmax_accepted_signed_work": 0.0,
                "argmax_residual": 0.0,
                "argmax_scale": 1.0,
            }
        )
    else:
        base.update(
            {
                "precondition_passed": True,
                "positive_cell_count": 0,
                "negative_cell_count": 0,
                "zero_cell_count": 4,
                "accepted_signed_work_sum": 0.0,
                "rejected_positive_work_sum": 0.0,
                "sum_abs_accepted_signed_work": 0.0,
                "sum_proxy_before": 4.0,
                "sum_proxy_after": 4.0,
                "aggregate_residual": 0.0,
                "aggregate_scale": 4.0,
                "P": 0.0,
                "A": 0.0,
                "D": 0.0,
                "q": 1.0,
                "remaining": 0.0,
                "max_abs_cellwise_residual": 0.0,
                "sum_abs_cellwise_residuals": 0.0,
            }
        )
    return base


def checkpoint_rows(protocol: dict[str, Any]) -> list[dict[str, Any]]:
    psi = np.ones((2, 2), dtype=np.complex128)
    phi = np.zeros((2, 2), dtype=np.float64)
    geometry = checker._observer_geometry(2, 1)
    prepared = checker._base_observer_metrics(psi, phi, geometry, 1)
    rows: list[dict[str, Any]] = []
    for stencil_index in range(2):
        for branch_index in range(6):
            for checkpoint_index, step in enumerate([0, 1]):
                rows.append(
                    checker.checkpoint_metrics(
                        stencil_index=stencil_index,
                        branch_index=branch_index,
                        checkpoint_index=checkpoint_index,
                        step=step,
                        psi=psi,
                        phi=phi,
                        prepared=prepared,
                        geometry=geometry,
                        profile_length=1,
                        energy_denominator_floor=1e-30,
                        profile_denominator_floor=1e-30,
                    )
                )
    return rows


def write_synthetic_shards(
    root: Path, protocol: dict[str, Any]
) -> tuple[list[list[dict[str, Any]]], tuple[Any, ...]]:
    records_by_shard: list[list[dict[str, Any]]] = []
    identities: list[Any] = []
    for shard_index, spec in enumerate(protocol["retention"]["evidence_shards"]):
        records = [
            synthetic_record(protocol, shard_index, ordinal)
            for ordinal in range(spec["count"])
        ]
        path = root / spec["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        data = b"".join(checker.canonical_payload_bytes(row) + b"\n" for row in records)
        path.write_bytes(data)
        base = checker.file_identity(path, spec["path"])
        identities.append(
            checker.ShardIdentity(
                path=base.path,
                bytes=base.bytes,
                sha256=base.sha256,
                git_blob=base.git_blob,
                record_count=spec["count"],
                first_record_index=spec["first_record_index"],
                last_record_index=spec["last_record_index"],
            )
        )
        records_by_shard.append(records)
    return records_by_shard, tuple(identities)


def primary_for_stream(identities: tuple[Any, ...]) -> dict[str, Any]:
    return {
        "checkpoint_metrics": checkpoint_rows(synthetic_protocol()),
        "evidence_identity": {
            "shards": [
                {
                    "path": identity.path,
                    "bytes": identity.bytes,
                    "sha256": identity.sha256,
                    "record_count": identity.record_count,
                    "first_record_index": identity.first_record_index,
                    "last_record_index": identity.last_record_index,
                }
                for identity in identities
            ]
        },
    }


def complete_primary_summaries(primary: dict[str, Any], protocol: dict[str, Any]) -> None:
    primary["trajectory_energy_summaries"] = [
        {
            "stencil_index": stencil_index,
            "branch_index": branch_index,
            "record_count": 1,
            "pre_total_psi_energy": 4.0,
            "minimum_total_psi_energy": 4.0,
            "maximum_total_psi_energy": 4.0,
            "minimum_energy_ratio": 1.0,
            "maximum_energy_ratio": 1.0,
            "first_lower_bound_violation_step": None,
            "first_upper_bound_violation_step": None,
        }
        for stencil_index in range(2)
        for branch_index in range(6)
    ]
    primary["technical_telemetry_summaries"] = [
        {
            "stencil_index": stencil_index,
            "branch_index": branch_index,
            "record_count": 1,
            "psi_cap_contact_count": 0,
            "phi_cap_contact_count": 0,
            "destructive_reset_count": 0,
            "nonfinite_detected_count": 0,
            "negative_phi_input_detected_count": 0,
            "undeclared_source_detected_count": 0,
        }
        for stencil_index in range(2)
        for branch_index in range(6)
    ]
    comparisons: list[dict[str, Any]] = []
    for stencil_index in range(2):
        for step in (1, 1):
            for metric in (
                "psi_energy_relative_error",
                "psi_radial_profile_relative_l2_error",
            ):
                comparisons.append(
                    checker._comparison_row(
                        comparison_index=len(comparisons),
                        comparison_kind="pair_both_vs_control",
                        stencil_index=stencil_index,
                        step=step,
                        metric=metric,
                        reference_branch_index=0,
                        candidate_branch_index=4,
                        reference_value=0.0,
                        candidate_value=0.0,
                        absolute_tolerance=1e-8,
                        relative_tolerance=1e-12,
                    )
                )
    for stencil_index in range(2):
        for step in (1, 1):
            comparisons.append(
                checker._comparison_row(
                    comparison_index=len(comparisons),
                    comparison_kind="pair_both_vs_global_pool",
                    stencil_index=stencil_index,
                    step=step,
                    metric="psi_radial_profile_relative_l2_error",
                    reference_branch_index=5,
                    candidate_branch_index=4,
                    reference_value=0.0,
                    candidate_value=0.0,
                    absolute_tolerance=1e-8,
                    relative_tolerance=1e-12,
                )
            )
    primary["comparisons"] = comparisons
    primary["gates"] = {
        "identity": True,
        "runtime": True,
        "serialization": True,
        "starting_clones": True,
        "receipt_only_control": True,
        "proposal_fidelity": True,
        "technical_telemetry": True,
        "local_receipts": True,
        "global_receipts": True,
        "control_phenotype": False,
        "pair_both_absolute_clean": True,
        "pair_both_causal_improvement": False,
        "local_advantage": False,
        "global_pool_absolute_clean": True,
    }
    primary["classification"] = {
        "outcome": protocol["outcome_map"][0],
        "primary_claim_only": True,
    }


def fake_program_gate() -> Any:
    commit = "1" * 40
    blob = "2" * 40
    return checker.ProgramGate(
        expected_execution_commit=commit,
        actual_head_commit=commit,
        remote_readback_commit=commit,
        head_equals_remote_readback_commit=True,
        worktree_clean=True,
        expected_checker_git_blob=blob,
        actual_checker_filtered_git_blob=blob,
        actual_checker_head_git_blob=blob,
        expected_checker_test_git_blob=blob,
        actual_checker_test_filtered_git_blob=blob,
        actual_checker_test_head_git_blob=blob,
    )


def fake_bindings() -> Any:
    empty_sha = hashlib.sha256(b"").hexdigest()
    empty_blob = checker.git_blob_digest(b"")
    primary = checker.FileIdentity(checker.PRIMARY_PATH, 1, empty_sha, empty_blob)
    shards = tuple(
        checker.ShardIdentity(
            path=f"synthetic/{index}.jsonl",
            bytes=1,
            sha256=empty_sha,
            git_blob=empty_blob,
            record_count=1,
            first_record_index=index,
            last_record_index=index,
        )
        for index in range(6)
    )
    return checker.InvocationBindings(
        execution_commit="1" * 40,
        remote_readback_commit="1" * 40,
        checker_git_blob="2" * 40,
        checker_test_git_blob="2" * 40,
        report_git_blob="2" * 40,
        manifest_git_blob="2" * 40,
        primary=primary,
        shards=shards,
    )


def test_source_is_machine_verifiably_independent_and_has_no_outcome_constant() -> None:
    source = CHECKER_FILE.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert all("local_reciprocal_work" not in name for name in imports)
    classifier = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "classify_from_protocol"
    )
    classifier_strings = {
        node.value
        for node in ast.walk(classifier)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    assert not any(value.startswith("rwc1_") for value in classifier_strings)
    assert "expected_outcome" not in source.lower()


def test_strict_json_rejects_duplicate_keys_nonfinite_and_non_utf8() -> None:
    with pytest.raises(checker.ContractError):
        checker.strict_json_loads(b'{"a":1,"a":2}')
    with pytest.raises(checker.ContractError):
        checker.strict_json_loads(b'{"a":NaN}')
    with pytest.raises(checker.ContractError):
        checker.strict_json_loads(b"\xff")


def test_canonical_payload_hash_omits_self_and_file_has_one_lf() -> None:
    payload = checker.payload_with_self_hash({"z": 1, "a": True})
    without_self = dict(payload)
    digest = without_self.pop("canonical_payload_sha256_without_self")
    assert digest == hashlib.sha256(checker.canonical_payload_bytes(without_self)).hexdigest()
    data = checker.canonical_file_bytes(payload)
    assert data.endswith(b"\n")
    assert not data.endswith(b"\n\n")
    assert b" " not in data


def test_observer_uses_mean_floor_bins_exact_cell_half_radius_and_exact_circle() -> None:
    psi = np.asarray(
        [[1.0 + 0.0j, 2.0 + 0.0j, 0.0 + 0.0j], [0.0j, 3.0 + 0.0j, 0.0j], [0.0j, 0.0j, 0.0j]],
        dtype=np.complex128,
    )
    phi = np.arange(9, dtype=np.float64).reshape(3, 3)
    geometry = checker._observer_geometry(3, 2)
    metrics = checker._base_observer_metrics(psi, phi, geometry, 2)
    energy = np.abs(psi) ** 2
    bins = geometry[3]
    counts = geometry[4]
    expected_profile = np.bincount(bins.ravel(), weights=energy.ravel(), minlength=2) / np.maximum(counts, 1.0)
    assert np.array_equal(metrics["psi_radial_profile"], expected_profile)
    assert metrics["half_energy_radius"] == 0.0
    radius = geometry[2]
    assert metrics["energy_fraction_radius_3"] == float(np.sum(energy[radius <= 3.0]) / np.sum(energy))


def test_exact_value_comparison_adds_no_numeric_tolerance() -> None:
    audit = checker.Audit()
    assert not checker.compare_exact(1.0, np.nextafter(1.0, 2.0), audit, "checkpoint")
    assert audit.mismatch_count == 1
    assert not audit.checkpoint_metrics_match


def test_descriptor_enumeration_covers_every_synthetic_record_exactly() -> None:
    protocol = synthetic_protocol()
    observed: list[tuple[str, tuple[tuple[str, int], ...]]] = []
    for shard_index, spec in enumerate(protocol["retention"]["evidence_shards"]):
        for ordinal in range(spec["count"]):
            record_type, descriptor = checker._expected_record_descriptor(
                protocol, shard_index, ordinal
            )
            observed.append((record_type, tuple(sorted(descriptor.items()))))
    assert len(observed) == 66
    assert sum(record_type == "prepared_state" for record_type, _ in observed) == 2
    assert sum(record_type == "checkpoint_state" for record_type, _ in observed) == 24
    assert sum(record_type == "local_stage_receipt" for record_type, _ in observed) == 12
    assert len(set(range(66))) == 66


def test_frozen_v3_enumerates_all_400110_records_and_exact_subranges() -> None:
    protocol, identity = checker.read_frozen_protocol(REPOSITORY_ROOT)
    assert identity.bytes == checker.FROZEN_PROTOCOL_BYTES
    specs = protocol["retention"]["evidence_shards"]
    expected_type_counts = {
        "prepared_state": 2,
        "checkpoint_state": 108,
        "step_energy": 120000,
        "step_telemetry": 120000,
        "local_stage_receipt": 120000,
        "global_stage_receipt": 40000,
    }
    observed_type_counts = {name: 0 for name in expected_type_counts}
    observed_global_indices: list[tuple[int, int]] = []
    for shard_index, spec in enumerate(specs):
        observed_global_indices.append(
            (spec["first_record_index"], spec["last_record_index"])
        )
        assert spec["last_record_index"] - spec["first_record_index"] + 1 == spec["count"]
        for ordinal in range(spec["count"]):
            record_type, _ = checker._expected_record_descriptor(
                protocol, shard_index, ordinal
            )
            observed_type_counts[record_type] += 1
    assert observed_type_counts == expected_type_counts
    assert sum(observed_type_counts.values()) == 400110
    assert observed_global_indices == [
        (0, 109),
        (110, 120109),
        (120110, 240109),
        (240110, 300109),
        (300110, 360109),
        (360110, 400109),
    ]

    for shard_index, stencil_index in ((3, 0), (4, 1)):
        boundary_expectations = {
            0: (1, 1, 0),
            1: (1, 1, 1),
            19999: (1, 10000, 1),
            20000: (2, 1, 1),
            29999: (2, 10000, 1),
            30000: (3, 1, 0),
            39999: (3, 10000, 0),
            40000: (4, 1, 0),
            40001: (4, 1, 1),
            59999: (4, 10000, 1),
        }
        for ordinal, (branch_index, step, stage_index) in boundary_expectations.items():
            record_type, descriptor = checker._expected_record_descriptor(
                protocol, shard_index, ordinal
            )
            assert record_type == "local_stage_receipt"
            assert descriptor == {
                "stencil_index": stencil_index,
                "branch_index": branch_index,
                "step": step,
                "stage_index": stage_index,
            }

    global_boundaries = {
        0: (0, 1, 0),
        1: (0, 1, 1),
        19999: (0, 10000, 1),
        20000: (1, 1, 0),
        20001: (1, 1, 1),
        39999: (1, 10000, 1),
    }
    for ordinal, (stencil_index, step, stage_index) in global_boundaries.items():
        record_type, descriptor = checker._expected_record_descriptor(protocol, 5, ordinal)
        assert record_type == "global_stage_receipt"
        assert descriptor == {
            "stencil_index": stencil_index,
            "branch_index": 5,
            "step": step,
            "stage_index": stage_index,
        }


def test_one_pass_stream_recomputes_all_synthetic_record_families(tmp_path: Path) -> None:
    protocol = synthetic_protocol()
    _, identities = write_synthetic_shards(tmp_path, protocol)
    primary = primary_for_stream(identities)
    audit = checker.Audit()
    state, actual = checker.stream_evidence_after_latch(
        tmp_path, protocol, primary, identities, audit
    )
    assert actual == identities
    assert len(state.recomputed_checkpoint_rows) == 24
    assert state.local_receipt_count == 12
    assert state.global_receipt_count == 4
    assert state.local_receipts
    assert state.global_receipts
    assert state.starting_clones
    assert state.receipt_only_control
    assert audit.mismatch_count == 0


def test_stream_rejects_noncanonical_line_and_wrong_numeric_type(tmp_path: Path) -> None:
    protocol = synthetic_protocol()
    records, identities = write_synthetic_shards(tmp_path, protocol)
    path = tmp_path / identities[1].path
    records[1][0]["total_psi_energy"] = 4
    data = b"".join(checker.canonical_payload_bytes(row) + b"\n" for row in records[1])
    path.write_bytes(data)
    base = checker.file_identity(path, identities[1].path)
    bad_identity = checker.ShardIdentity(
        path=base.path,
        bytes=base.bytes,
        sha256=base.sha256,
        git_blob=base.git_blob,
        record_count=identities[1].record_count,
        first_record_index=identities[1].first_record_index,
        last_record_index=identities[1].last_record_index,
    )
    primary = primary_for_stream(identities)
    state = checker.EvidenceState(protocol=protocol, primary=primary, audit=checker.Audit())
    with pytest.raises(checker.ContractError, match="finite binary64"):
        checker._stream_one_shard(tmp_path, protocol, primary, bad_identity, 1, state)

    records[1][0]["total_psi_energy"] = 4.0
    canonical = checker.canonical_payload_bytes(records[1][0])
    path.write_bytes(canonical.replace(b":", b": ", 1) + b"\n")
    base = checker.file_identity(path, identities[1].path)
    noncanonical = checker.ShardIdentity(
        path=base.path,
        bytes=base.bytes,
        sha256=base.sha256,
        git_blob=base.git_blob,
        record_count=1,
        first_record_index=identities[1].first_record_index,
        last_record_index=identities[1].first_record_index,
    )
    state = checker.EvidenceState(protocol=protocol, primary=primary, audit=checker.Audit())
    with pytest.raises(checker.ContractError, match="canonical"):
        checker._stream_one_shard(tmp_path, protocol, primary, noncanonical, 1, state)


def test_global_cellwise_diagnostic_is_non_gating(tmp_path: Path) -> None:
    protocol = synthetic_protocol()
    record = synthetic_record(protocol, 5, 0)
    record["max_abs_cellwise_residual"] = 1000.0
    record["sum_abs_cellwise_residuals"] = 1000.0
    state = checker.EvidenceState(protocol=protocol, primary={}, audit=checker.Audit())
    checker._process_global_receipt(state, record)
    assert state.global_receipts
    assert state.audit.aggregate_receipt_arithmetic_passed


def test_global_receipt_binds_debit_to_accepted_aggregates_and_zero_boundary() -> None:
    protocol = synthetic_protocol()
    zero_record = synthetic_record(protocol, 5, 0)
    zero_state = checker.EvidenceState(protocol=protocol, primary={}, audit=checker.Audit())
    checker._process_global_receipt(zero_state, zero_record)
    assert zero_state.global_receipts

    tampered = dict(zero_record)
    tampered.update(
        {
            "positive_cell_count": 1,
            "zero_cell_count": 3,
            "P": 1.0,
            "A": 1.0,
            "D": 1.0,
            "q": 1.0,
            "remaining": 0.0,
            "rejected_positive_work_sum": 0.0,
            "accepted_signed_work_sum": 0.0,
            "sum_abs_accepted_signed_work": 0.0,
        }
    )
    tampered_state = checker.EvidenceState(
        protocol=protocol, primary={}, audit=checker.Audit()
    )
    checker._process_global_receipt(tampered_state, tampered)
    assert not tampered_state.global_receipts
    assert not tampered_state.audit.aggregate_receipt_arithmetic_passed


def test_local_retained_witness_mismatch_fails_without_unretained_claim() -> None:
    protocol = synthetic_protocol()
    record = synthetic_record(protocol, 3, 0)
    record["max_cellwise_normalized_residual_ratio"] = 0.5
    state = checker.EvidenceState(protocol=protocol, primary={}, audit=checker.Audit())
    checker._process_local_receipt(state, record)
    assert not state.local_receipts
    assert not state.audit.retained_witness_arithmetic_passed


def test_classifier_uses_only_protocol_map_and_recomputed_surfaces() -> None:
    protocol = synthetic_protocol()
    gates = {
        "identity": True,
        "runtime": True,
        "serialization": True,
        "starting_clones": True,
        "receipt_only_control": True,
        "proposal_fidelity": True,
        "technical_telemetry": True,
        "local_receipts": True,
        "global_receipts": True,
        "control_phenotype": True,
        "pair_both_absolute_clean": True,
        "pair_both_causal_improvement": True,
        "local_advantage": True,
        "global_pool_absolute_clean": False,
    }
    comparisons = [{"comparison_kind": "pair_both_vs_control", "passed": False}]
    assert checker.classify_from_protocol(protocol, gates, comparisons) == protocol["outcome_map"][1]
    gates["local_advantage"] = False
    assert checker.classify_from_protocol(protocol, gates, comparisons) == protocol["outcome_map"][2]
    gates["pair_both_causal_improvement"] = False
    comparisons[0]["passed"] = True
    assert checker.classify_from_protocol(protocol, gates, comparisons) == protocol["outcome_map"][3]
    comparisons[0]["passed"] = False
    assert checker.classify_from_protocol(protocol, gates, comparisons) == protocol["outcome_map"][4]
    gates["identity"] = False
    assert checker.classify_from_protocol(protocol, gates, comparisons) == protocol["outcome_map"][0]
    gates["identity"] = True
    gates["control_phenotype"] = False
    assert checker.classify_from_protocol(protocol, gates, comparisons) == protocol["outcome_map"][0]


def test_full_synthetic_recomputation_builds_contract_output(tmp_path: Path) -> None:
    protocol = synthetic_protocol()
    _, identities = write_synthetic_shards(tmp_path, protocol)
    primary = primary_for_stream(identities)
    complete_primary_summaries(primary, protocol)
    audit = checker.Audit()
    state, actual = checker.stream_evidence_after_latch(
        tmp_path, protocol, primary, identities, audit
    )
    empty = b"synthetic-primary\n"
    primary_identity = checker.FileIdentity(
        "synthetic/primary.json",
        len(empty),
        hashlib.sha256(empty).hexdigest(),
        checker.git_blob_digest(empty),
    )
    protocol_identity = checker.FileIdentity(
        "synthetic/protocol.json",
        len(empty),
        hashlib.sha256(empty).hexdigest(),
        checker.git_blob_digest(empty),
    )
    output = checker.build_checker_output(
        protocol=protocol,
        protocol_identity=protocol_identity,
        primary_identity=primary_identity,
        shard_identities=actual,
        gate=fake_program_gate(),
        state=state,
        source_identity_truth=True,
        runtime_truth=True,
    )
    assert output["schema"] == checker.CHECKER_SCHEMA
    assert output["agreement"] == {"passed": True, "mismatch_count": 0}
    assert output["conditional_outcome"]["agrees"]
    assert output["limitations"] == protocol["retention"]["checker_limitations"]
    without_self = dict(output)
    digest = without_self.pop("canonical_payload_sha256_without_self")
    assert digest == hashlib.sha256(checker.canonical_payload_bytes(without_self)).hexdigest()


def test_fixed_latch_is_exclusive_and_canonical(tmp_path: Path) -> None:
    protocol_identity = checker.FileIdentity(
        "synthetic/protocol.json",
        1,
        hashlib.sha256(b"x").hexdigest(),
        checker.git_blob_digest(b"x"),
    )
    gate = fake_program_gate()
    bindings = fake_bindings()
    checker.create_attempt_latch(tmp_path, gate, protocol_identity, bindings)
    receipt_path = tmp_path / checker.CHECKER_RECEIPT_PATH
    receipt_data = receipt_path.read_bytes()
    receipt = checker.strict_json_loads(receipt_data)
    assert checker.canonical_file_bytes(receipt) == receipt_data
    assert receipt["status"] == "attempt_started_authority_consumed"
    assert receipt["authority_consumed"] is True
    assert receipt["retry_authorized"] is False
    with pytest.raises(FileExistsError):
        checker.create_attempt_latch(tmp_path, gate, protocol_identity, bindings)


def test_execute_reads_primary_only_after_latch_and_retains_failure_receipt(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    protocol = synthetic_protocol()
    protocol_identity = checker.FileIdentity(
        "synthetic/protocol.json",
        1,
        hashlib.sha256(b"x").hexdigest(),
        checker.git_blob_digest(b"x"),
    )

    def guarded_load(*args: Any, **kwargs: Any) -> Any:
        assert (tmp_path / checker.CHECKER_RECEIPT_PATH).exists()
        raise checker.ContractError("synthetic retained input failure")

    monkeypatch.setattr(checker, "load_primary_after_latch", guarded_load)
    with pytest.raises(checker.ContractError, match="synthetic retained input failure"):
        checker.execute_checker_once(
            tmp_path,
            protocol,
            protocol_identity,
            fake_bindings(),
            fake_program_gate(),
        )
    receipt = checker.strict_json_loads(
        (tmp_path / checker.CHECKER_RECEIPT_PATH).read_bytes()
    )
    assert receipt["status"] == "technical_non_result"
    assert receipt["authority_consumed"] is True
    assert receipt["retry_authorized"] is False
    assert not (tmp_path / checker.CHECKER_OUTPUT_PATH).exists()
    expected_stderr = checker.canonical_failure_stderr_bytes(
        "synthetic retained input failure"
    )
    binary_stream = io.BytesIO()

    class BinaryCapture:
        buffer = binary_stream

    checker.emit_failure_stderr(expected_stderr, BinaryCapture())
    emitted = binary_stream.getvalue()
    assert emitted == expected_stderr
    assert receipt["stderr_identity"]["bytes"] == len(emitted)
    assert receipt["stderr_identity"]["sha256"] == hashlib.sha256(emitted).hexdigest()

    text_stream = io.StringIO()
    checker.emit_failure_stderr(expected_stderr, text_stream)
    assert text_stream.getvalue().encode("utf-8") == expected_stderr


def git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return completed.stdout.strip()


def test_clean_preflight_binds_exact_remote_and_primary_ancestor_without_opening_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    paths = [
        checker.CHECKER_PATH,
        checker.CHECKER_TEST_PATH,
        checker.REPORT_PATH,
        checker.MANIFEST_PATH,
        checker.PROTOCOL_PATH,
        checker.PRIMARY_PATH,
        *[f"synthetic/{index}.jsonl" for index in range(6)],
    ]
    for index, relative_path in enumerate(paths):
        path = tmp_path / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(f"fixture-{index}\n".encode("ascii"))
    git(tmp_path, "init")
    git(tmp_path, "config", "user.email", "synthetic@example.invalid")
    git(tmp_path, "config", "user.name", "Synthetic Test")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-m", "synthetic retained checkpoint")
    commit = git(tmp_path, "rev-parse", "HEAD")
    git(tmp_path, "update-ref", checker.FROZEN_REMOTE_REF, commit)
    monkeypatch.setattr(checker, "FROZEN_PRIMARY_RESULT_COMMIT", commit)
    monkeypatch.setattr(checker, "FROZEN_PROTOCOL_REMOTE_COMMIT", commit)

    identity_by_path = {
        relative_path: checker.file_identity(tmp_path / relative_path, relative_path)
        for relative_path in paths
    }
    shard_identities = tuple(
        checker.ShardIdentity(
            path=f"synthetic/{index}.jsonl",
            bytes=identity_by_path[f"synthetic/{index}.jsonl"].bytes,
            sha256=identity_by_path[f"synthetic/{index}.jsonl"].sha256,
            git_blob=identity_by_path[f"synthetic/{index}.jsonl"].git_blob,
            record_count=1,
            first_record_index=index,
            last_record_index=index,
        )
        for index in range(6)
    )
    bindings = checker.InvocationBindings(
        execution_commit=commit,
        remote_readback_commit=commit,
        checker_git_blob=identity_by_path[checker.CHECKER_PATH].git_blob,
        checker_test_git_blob=identity_by_path[checker.CHECKER_TEST_PATH].git_blob,
        report_git_blob=identity_by_path[checker.REPORT_PATH].git_blob,
        manifest_git_blob=identity_by_path[checker.MANIFEST_PATH].git_blob,
        primary=identity_by_path[checker.PRIMARY_PATH],
        shards=shard_identities,
    )
    original_open = Path.open

    def guarded_open(path: Path, *args: Any, **kwargs: Any) -> Any:
        relative = path.resolve().relative_to(tmp_path.resolve()).as_posix()
        if relative == checker.PRIMARY_PATH or relative.startswith("synthetic/"):
            raise AssertionError("preflight opened retained input")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded_open)
    gate = checker.clean_preflight(
        tmp_path, bindings, synthetic_protocol(), identity_by_path[checker.PROTOCOL_PATH]
    )
    assert gate.worktree_clean
    assert gate.actual_head_commit == commit
    assert gate.head_equals_remote_readback_commit


def test_checker_runtime_mismatch_fails_before_latch(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    protocol = synthetic_protocol()
    monkeypatch.setattr(checker.platform, "python_version", lambda: "0.0.0")
    with pytest.raises(checker.CheckerError, match="Python runtime"):
        checker.validate_checker_runtime(protocol)
    assert not (tmp_path / checker.CHECKER_RECEIPT_PATH).exists()


def test_manifest_cross_binds_only_machine_identity_fields(tmp_path: Path) -> None:
    protocol = synthetic_protocol()
    paths = [
        checker.CHECKER_PATH,
        checker.CHECKER_TEST_PATH,
        checker.PROTOCOL_PATH,
        checker.PRIMARY_PATH,
        checker.REPORT_PATH,
        *[spec["path"] for spec in protocol["retention"]["evidence_shards"]],
    ]
    for index, relative_path in enumerate(paths):
        path = tmp_path / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(f"identity-{index}\n".encode("ascii"))
    identities = {
        relative_path: checker.file_identity(tmp_path / relative_path, relative_path)
        for relative_path in paths
    }
    shards = tuple(
        checker.ShardIdentity(
            path=spec["path"],
            bytes=identities[spec["path"]].bytes,
            sha256=identities[spec["path"]].sha256,
            git_blob=identities[spec["path"]].git_blob,
            record_count=spec["count"],
            first_record_index=spec["first_record_index"],
            last_record_index=spec["last_record_index"],
        )
        for spec in protocol["retention"]["evidence_shards"]
    )
    file_rows: dict[str, Any] = {}
    for relative_path in (
        checker.PROTOCOL_PATH,
        checker.CHECKER_PATH,
        checker.CHECKER_TEST_PATH,
        checker.PRIMARY_PATH,
    ):
        identity = identities[relative_path]
        file_rows[relative_path] = {
            "bytes": identity.bytes,
            "sha256": identity.sha256,
            "git_blob_sha": identity.git_blob,
            "role": "ignored free text",
        }
    file_rows[checker.PRIMARY_PATH]["schema"] = checker.PRIMARY_SCHEMA
    for shard in shards:
        file_rows[shard.path] = {
            "bytes": shard.bytes,
            "sha256": shard.sha256,
            "git_blob_sha": shard.git_blob,
            "record_count": shard.record_count,
            "first_record_index": shard.first_record_index,
            "last_record_index": shard.last_record_index,
            "role": "ignored free text",
        }
    manifest = {
        "schema": checker.MANIFEST_SCHEMA,
        "source_report": checker.REPORT_PATH,
        "files": file_rows,
        "q2_m2_rwc1": {
            "continuity_report_git_blob": identities[checker.REPORT_PATH].git_blob,
            "protocol_path": checker.PROTOCOL_PATH,
            "protocol_schema": checker.FROZEN_PROTOCOL_SCHEMA,
            "primary_output_path": checker.PRIMARY_PATH,
            "evidence_shards": 6,
            "evidence_record_count": 66,
            "evidence_first_record_index": 0,
            "evidence_last_record_index": 65,
            "evidence_max_shard_bytes": 1_000_000,
            "primary_outcome": "ignored free text",
        },
    }
    manifest_path = tmp_path / checker.MANIFEST_PATH
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_bytes(json.dumps(manifest, indent=2).encode("utf-8") + b"\n")
    manifest_identity = checker.file_identity(manifest_path, checker.MANIFEST_PATH)
    bindings = checker.InvocationBindings(
        execution_commit="1" * 40,
        remote_readback_commit="1" * 40,
        checker_git_blob=identities[checker.CHECKER_PATH].git_blob,
        checker_test_git_blob=identities[checker.CHECKER_TEST_PATH].git_blob,
        report_git_blob=identities[checker.REPORT_PATH].git_blob,
        manifest_git_blob=manifest_identity.git_blob,
        primary=identities[checker.PRIMARY_PATH],
        shards=shards,
    )
    checker.validate_manifest_after_latch(
        tmp_path,
        protocol,
        identities[checker.PROTOCOL_PATH],
        bindings,
    )

    manifest["files"][checker.CHECKER_PATH]["sha256"] = "0" * 64
    manifest_path.write_bytes(json.dumps(manifest, indent=2).encode("utf-8") + b"\n")
    changed_manifest = checker.file_identity(manifest_path, checker.MANIFEST_PATH)
    changed_bindings = checker.InvocationBindings(
        execution_commit=bindings.execution_commit,
        remote_readback_commit=bindings.remote_readback_commit,
        checker_git_blob=bindings.checker_git_blob,
        checker_test_git_blob=bindings.checker_test_git_blob,
        report_git_blob=bindings.report_git_blob,
        manifest_git_blob=changed_manifest.git_blob,
        primary=bindings.primary,
        shards=bindings.shards,
    )
    with pytest.raises(checker.ContractError, match="manifest file identity"):
        checker.validate_manifest_after_latch(
            tmp_path,
            protocol,
            identities[checker.PROTOCOL_PATH],
            changed_bindings,
        )


def test_atomic_output_publication_never_overwrites_existing_or_racing_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    output = tmp_path / "fixed.json"
    output.write_bytes(b"existing\n")
    with pytest.raises(checker.CheckerError, match="overwrite"):
        checker._atomic_replace_json(output, {"value": 1})
    assert output.read_bytes() == b"existing\n"

    output.unlink()
    original_link = checker.os.link

    def racing_link(source: Any, destination: Any) -> None:
        Path(destination).write_bytes(b"racer\n")
        raise FileExistsError

    monkeypatch.setattr(checker.os, "link", racing_link)
    with pytest.raises(checker.CheckerError, match="overwrite"):
        checker._atomic_replace_json(output, {"value": 2})
    assert output.read_bytes() == b"racer\n"
    monkeypatch.setattr(checker.os, "link", original_link)


def test_checker_output_requires_exact_canonical_readback(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    output = checker.payload_with_self_hash({"schema": "synthetic.output", "passed": True})
    identity = checker.publish_checker_output(tmp_path, output)
    expected = checker.canonical_file_bytes(output)
    assert identity.bytes == len(expected)
    assert identity.sha256 == hashlib.sha256(expected).hexdigest()

    second_root = tmp_path / "tampered"
    original_publish = checker._atomic_replace_json

    def tampered_publish(path: Path, payload: dict[str, Any], **kwargs: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"tampered\n")

    monkeypatch.setattr(checker, "_atomic_replace_json", tampered_publish)
    with pytest.raises(checker.CheckerError, match="readback identity"):
        checker.publish_checker_output(second_root, output)
    assert (second_root / checker.CHECKER_OUTPUT_PATH).read_bytes() == b"tampered\n"
    monkeypatch.setattr(checker, "_atomic_replace_json", original_publish)


def test_failure_sanitizer_redacts_home_drive_unc_and_backslash_paths(tmp_path: Path) -> None:
    message = (
        f"{Path.home()} C:\\synthetic\\secret "
        r"\\synthetic-host\synthetic-share\private\file.json "
        r"\rooted\private\file.json"
    )
    sanitized = checker._sanitize_failure_message(message, tmp_path)
    assert str(Path.home()) not in sanitized
    assert "synthetic-host" not in sanitized
    assert "synthetic-share" not in sanitized
    assert "synthetic\\secret" not in sanitized
    assert "rooted\\private" not in sanitized


def test_argument_parser_requires_six_identity_bindings() -> None:
    protocol = synthetic_protocol()
    namespace = checker.argument_parser().parse_args(
        [
            "--expected-execution-commit",
            "1" * 40,
            "--remote-readback-commit",
            "1" * 40,
            "--expected-checker-git-blob",
            "2" * 40,
            "--expected-checker-test-git-blob",
            "2" * 40,
            "--expected-report-git-blob",
            "2" * 40,
            "--expected-manifest-git-blob",
            "2" * 40,
            "--expected-primary-bytes",
            "1",
            "--expected-primary-sha256",
            "3" * 64,
            "--expected-primary-git-blob",
            "2" * 40,
        ]
    )
    with pytest.raises(checker.CheckerError, match="six shard identities"):
        checker.build_invocation_bindings(namespace, protocol)
