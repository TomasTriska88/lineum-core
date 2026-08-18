from __future__ import annotations

import ast
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[2]
CHECKER_PATH = (
    ROOT
    / "research"
    / "runners"
    / "lineum_b4_q2_m1_rs1_resolution_sensitivity_checker.py"
)
SPEC = importlib.util.spec_from_file_location("lineum_b4_q2_m1_rs1_checker", CHECKER_PATH)
assert SPEC is not None and SPEC.loader is not None
checker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = checker
SPEC.loader.exec_module(checker)


def _classification_result(
    *,
    c0: float = 0.0,
    c1: float,
    c2: float,
    c3: float,
    valid: bool = True,
    c0_phi: float = 0.0,
    c0_mu: float = 0.0,
) -> dict[str, Any]:
    return {
        "valid": valid,
        "values": {"C0": c0, "C1": c1, "C2": c2, "C3": c3},
        "c0_channel_divergences": {
            "psi": c0,
            "phi": c0_phi,
            "mu": c0_mu,
        },
    }


def _size_result(label: str) -> dict[str, Any]:
    geometry = deepcopy(checker.EXPECTED_SIZE_GEOMETRY[label])
    values = deepcopy(checker.EXPECTED_VALUES[label])
    rows: dict[str, list[dict[str, Any]]] = {}
    summaries: dict[str, dict[str, Any]] = {}
    for lane in checker.LANES:
        psi = values[lane]
        divergences = {
            "psi": psi,
            "phi": 0.0 if lane == "C0" else psi * 2.0,
            "mu": 0.0 if lane == "C0" else psi * 3.0,
        }
        rows[lane] = [
            {
                "common_state_equal": True,
                "divergences": deepcopy(divergences),
                "valid": True,
                "variant_id": variant_id,
            }
            for variant_id in checker.VARIANT_IDS
        ]
        summaries[lane] = {
            "common_state_equal": True,
            "median_divergence": deepcopy(divergences),
            "valid": True,
        }
    return {
        **geometry,
        "variant_ids": list(checker.VARIANT_IDS),
        "valid": True,
        "validity": {
            "c0_null_pass": True,
            "common_state_equal": True,
            "histories_valid": True,
            "lanes_valid": True,
        },
        "causal_rows": rows,
        "causal_summary": summaries,
        "values": values,
        "c0_channel_divergences": deepcopy(summaries["C0"]["median_divergence"]),
    }


def _payload() -> dict[str, Any]:
    sizes = {"96": _size_result("96"), "128": _size_result("128")}
    independent = checker.classify_resolution_pair(
        _classification_result(**{
            "c0": sizes["96"]["values"]["C0"],
            "c1": sizes["96"]["values"]["C1"],
            "c2": sizes["96"]["values"]["C2"],
            "c3": sizes["96"]["values"]["C3"],
        }),
        _classification_result(**{
            "c0": sizes["128"]["values"]["C0"],
            "c1": sizes["128"]["values"]["C1"],
            "c2": sizes["128"]["values"]["C2"],
            "c3": sizes["128"]["values"]["C3"],
        }),
    )
    classification = {
        field: independent[field]
        for field in (
            "outcome",
            "resolution_stability_pass",
            "signatures_match",
            "signatures",
            "ratios",
            "ratios_pass",
            "mu_zeroing_reduction",
        )
    }
    payload: dict[str, Any] = {
        "protocol_id": checker.PROTOCOL_ID,
        "stage": "prospective_normalized_lattice_resolution_sensitivity",
        "empirically_connected": False,
        "protocol": deepcopy(checker.EXPECTED_PROTOCOL),
        "runtime_gate": {
            "numpy_version": "1.26.4",
            "passed": True,
            "python_version": "3.11.15",
            "required_numpy": "1.26.4",
            "required_python": "3.11.15",
        },
        "source_identity_gate": {
            "passed": True,
            "method": "git_filtered_worktree_and_head_blob",
            "expected": deepcopy(checker.EXPECTED_SOURCE_BLOBS),
            "actual": deepcopy(checker.EXPECTED_SOURCE_BLOBS),
            "head": deepcopy(checker.EXPECTED_SOURCE_BLOBS),
        },
        "environment": {
            "git_head": checker.EXPECTED_PRIMARY_HEAD,
            "runner_sha256": checker.EXPECTED_PRIMARY_RUNNER_SHA256,
            "numpy": "1.26.4",
            "python": "3.11.15 (synthetic non-scientific fixture)",
        },
        "evidence_boundary": {
            "normalized_lattice_sensitivity_only": True,
            "continuum_convergence_established": False,
            "retained_q2_m1_primary_reclassified": False,
            "independent_checker_run": False,
            "q2_rescue_tested": False,
            "physical_memory_field_established": False,
            "gravity_established": False,
            "quantum_memory_established": False,
            "consciousness_established": False,
            "cosmology_established": False,
        },
        "size_results": sizes,
        "classification": classification,
    }
    payload["canonical_payload_sha256_without_self"] = (
        checker.canonical_payload_sha256_without_self(payload)
    )
    return payload


def test_checker_source_is_retained_output_only_and_stdlib_independent() -> None:
    source = CHECKER_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imports = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported_from = {
        node.module
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module is not None
    }
    assert "numpy" not in imports
    assert "numpy" not in imported_from
    assert "lineum_b4_q2_m1_rs1_resolution_sensitivity.py" not in source
    assert "run_size" not in source
    assert checker.PRIMARY_RELATIVE_PATH.endswith("resolution-sensitivity.json")


def test_checker_freezes_exact_retained_primary_identity() -> None:
    assert checker.EXPECTED_PRIMARY_CHECKOUT_BYTES == 13155
    assert checker.EXPECTED_PRIMARY_CHECKOUT_SHA256 == (
        "f1f43968bbd84de63568365371d9e1587a4feb9107020c4e143c466a77b78f2a"
    )
    assert checker.EXPECTED_PRIMARY_GIT_BLOB == (
        "d7f8b714dafbc1b5b98920a09f1b639ff16882c4"
    )
    assert checker.EXPECTED_PRIMARY_CANONICAL_SHA256 == (
        "0598c14e59eccaa151b0437385ca677f5c86604b16280e6c51f8392e65cbef3f"
    )


def test_subthreshold_pair_recomputes_only_the_frozen_unsupported_indication() -> None:
    receipt = checker.classify_resolution_pair(
        _classification_result(c1=2.3074e-5, c2=2.3066e-5, c3=2.5523e-9),
        _classification_result(c1=8.8497e-6, c2=8.8479e-6, c3=4.7986e-10),
    )

    assert receipt["signatures"]["96"] == {
        "C0": True,
        "C1": False,
        "C2": False,
        "C3": False,
    }
    assert receipt["ratios"] == {"C1": None, "C2": None, "C3": None}
    assert receipt["resolution_stability_pass"] is True
    assert receipt["outcome"] == checker.EXPECTED_PRIMARY_OUTCOME


def test_signature_mismatch_is_resolution_sensitive_and_unresolved() -> None:
    receipt = checker.classify_resolution_pair(
        _classification_result(c1=2e-5, c2=6e-5, c3=2e-9),
        _classification_result(c1=2e-5, c2=2e-5, c3=2e-9),
    )

    assert receipt["signatures_match"] is False
    assert receipt["resolution_stability_pass"] is False
    assert receipt["outcome"] == "rs1_resolution_sensitive_unresolved"


def test_above_floor_ratio_outside_interval_is_unresolved() -> None:
    receipt = checker.classify_resolution_pair(
        _classification_result(c1=2e-4, c2=2e-5, c3=2e-9),
        _classification_result(c1=5e-4, c2=2e-5, c3=2e-9),
    )

    assert receipt["ratios"]["C1"] == 2.5
    assert receipt["ratios_pass"] is False
    assert receipt["outcome"] == "rs1_resolution_sensitive_unresolved"


def test_candidate_reopens_only_after_both_zeroing_reductions_pass() -> None:
    receipt = checker.classify_resolution_pair(
        _classification_result(c1=4e-4, c2=1e-4, c3=2e-4),
        _classification_result(c1=5e-4, c2=1.2e-4, c3=2.5e-4),
    )

    assert receipt["mu_zeroing_reduction"]["96"] == pytest.approx(0.75)
    assert receipt["mu_zeroing_reduction"]["128"] == pytest.approx(0.76)
    assert receipt["outcome"] == "rs1_primary_mu_candidate_reopened"


def test_nonnull_c0_fails_closed() -> None:
    receipt = checker.classify_resolution_pair(
        _classification_result(c1=2e-5, c2=2e-5, c3=2e-9),
        _classification_result(
            c1=2e-5,
            c2=2e-5,
            c3=2e-9,
            c0_phi=2e-12,
        ),
    )

    assert receipt["resolution_stability_pass"] is False
    assert receipt["outcome"] == "rs1_inconclusive_or_confounded"


def test_consistent_synthetic_rows_recompute_to_expected_primary_claim() -> None:
    recomputed = checker.recompute_and_compare(_payload())

    assert recomputed["values"] == checker.EXPECTED_VALUES
    assert recomputed["signatures_match"] is True
    assert recomputed["outcome"] == checker.EXPECTED_PRIMARY_OUTCOME


def test_row_tamper_is_detected_before_classification() -> None:
    payload = _payload()
    payload["size_results"]["128"]["causal_rows"]["C3"][0]["divergences"][
        "psi"
    ] *= 2.0

    with pytest.raises(checker.CheckFailure, match="median does not match retained rows"):
        checker.recompute_and_compare(payload)


def test_claimed_outcome_tamper_is_detected() -> None:
    payload = _payload()
    payload["classification"]["outcome"] = "rs1_primary_mu_candidate_reopened"

    with pytest.raises(checker.CheckFailure, match="classification field"):
        checker.recompute_and_compare(payload)


def test_protocol_tamper_is_detected() -> None:
    payload = _payload()
    payload["protocol"]["execution_sizes"].append(160)

    with pytest.raises(checker.CheckFailure, match="frozen protocol changed"):
        checker.recompute_and_compare(payload)


def test_source_identity_tamper_is_detected() -> None:
    payload = _payload()
    payload["source_identity_gate"]["actual"]["lineum_core/math.py"] = "0" * 40

    with pytest.raises(checker.CheckFailure, match="source identity surface"):
        checker.recompute_and_compare(payload)


def test_canonical_payload_hash_reproduces_and_detects_mutation() -> None:
    payload = _payload()
    claimed = payload["canonical_payload_sha256_without_self"]

    assert checker.canonical_payload_sha256_without_self(payload) == claimed
    payload["environment"]["numpy"] = "changed"
    assert checker.canonical_payload_sha256_without_self(payload) != claimed


def test_strict_json_loader_rejects_nonfinite_constants(tmp_path: Path) -> None:
    path = tmp_path / "nonfinite.json"
    path.write_text('{"value": NaN}', encoding="utf-8")

    with pytest.raises(checker.CheckFailure, match="non-finite JSON constant"):
        checker.load_json_strict(path)
