from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
from typing import Any

SCHEMA = "lineum-b4-q2-perturbation-ledger-check/1"
PRIMARY_SCHEMA = "lineum-b4-q2-perturbation-ledger/1-retained-table"
STAGE = "Q2-PV1-A-CHECK"
PRIMARY_STAGE = "Q2-PV1-A"
COMPARE_RTOL = 1e-12
NUMERIC_RTOL = 1e-10
FROZEN_RECOVERY_ENERGY_TOLERANCE = 0.05
INNER_FACTOR = 1.5
ANNULUS_FACTOR = 0.5
EXPECTED_CANONICAL_RUNNER_BLOB = "1598faf0f39e056c1684f767c2554edc63283ca4"
EXPECTED_PRIMARY_RUNNER_BLOB = "e3657119b855965b4fd622b3e94f08443a7c9107"
EXPECTED_PRIMARY_TEST_BLOB = "403c1cb8747cebf3280009b3b2ffcd814c72e060"
EXPECTED_COLUMNS = [
    "case_key",
    "finite",
    "active_before_perturbation",
    "resets",
    "psi_cap_hits",
    "phi_cap_hits",
    "applicability",
    "e_inner",
    "e_annulus",
    "e_outer",
    "epsi_before",
    "pphi_before",
    "epsi_after",
    "direct_delta_epsi",
    "direct_delta_phi",
    "direct_delta_ledger",
    "relative_delta_epsi",
    "relative_delta_ledger",
    "analytic_delta_epsi",
    "analytic_direct_discrepancy",
    "absolute_relative_epsi_shift_over_frozen_5pct_tolerance",
    "ledger_neutral_within_numeric_tolerance",
]
LANES = [
    "baseline",
    "no_hard_guards",
    "no_linear_dissipation",
    "no_explicit_tanh",
    "no_interaction_denominator",
    "no_mode_coupling",
    "no_phi_cap",
]
STENCILS = ["LAP4", "LAP8"]
PHI0_VALUES = [0.0, 1.0]
NUMERIC_FIELDS = [
    "epsi_before",
    "epsi_after",
    "direct_delta_epsi",
    "direct_delta_phi",
    "direct_delta_ledger",
    "relative_delta_epsi",
    "relative_delta_ledger",
    "analytic_delta_epsi",
    "analytic_direct_discrepancy",
    "absolute_relative_epsi_shift_over_frozen_5pct_tolerance",
]
CATEGORICAL_FIELDS = [
    "applicability",
    "ledger_neutral_within_numeric_tolerance",
]


def expected_case_keys() -> list[str]:
    return [
        f"{stencil}|{lane}|phi0={phi0:.1f}"
        for stencil in STENCILS
        for lane in LANES
        for phi0 in PHI0_VALUES
    ]


def compare_tolerance(a: float, b: float) -> float:
    return COMPARE_RTOL * max(1.0, abs(a), abs(b))


def close_enough(a: float, b: float) -> bool:
    if not math.isfinite(a) or not math.isfinite(b):
        return a == b
    return abs(a - b) <= compare_tolerance(a, b)


def _column_map(payload: dict[str, Any]) -> dict[str, int]:
    columns = payload.get("columns")
    if columns != EXPECTED_COLUMNS:
        raise ValueError("primary columns do not match the frozen checker schema")
    return {name: index for index, name in enumerate(columns)}


def _protocol_errors(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if payload.get("schema") != PRIMARY_SCHEMA:
        errors.append("schema")
    if payload.get("stage") != PRIMARY_STAGE:
        errors.append("stage")
    if payload.get("status") != "primary_pending_independent_check":
        errors.append("status")

    protocol = payload.get("protocol", {})
    expected_protocol = {
        "grid_size": 32,
        "primary_steps": 5000,
        "recovery_steps": 0,
        "stencils": STENCILS,
        "phi0_values": PHI0_VALUES,
        "inner_factor": INNER_FACTOR,
        "annulus_factor": ANNULUS_FACTOR,
        "numeric_rtol": NUMERIC_RTOL,
        "frozen_recovery_energy_tolerance": FROZEN_RECOVERY_ENERGY_TOLERANCE,
    }
    for key, expected in expected_protocol.items():
        if protocol.get(key) != expected:
            errors.append(f"protocol.{key}")

    gate = payload.get("pre_execution_gate", {})
    if gate.get("source_identity_checks_passed") is not True:
        errors.append("pre_execution_gate.source_identity_checks_passed")
    if gate.get("tests_failed") != 0:
        errors.append("pre_execution_gate.tests_failed")
    if not isinstance(gate.get("tests_passed"), int) or gate.get("tests_passed", 0) <= 0:
        errors.append("pre_execution_gate.tests_passed")

    source = payload.get("source_execution", {})
    expected_sources = {
        "canonical_localized_runner_git_blob": EXPECTED_CANONICAL_RUNNER_BLOB,
        "q2_pv1_runner_git_blob": EXPECTED_PRIMARY_RUNNER_BLOB,
        "q2_pv1_test_git_blob": EXPECTED_PRIMARY_TEST_BLOB,
    }
    for key, expected in expected_sources.items():
        if source.get(key) != expected:
            errors.append(f"source_execution.{key}")
    for key in (
        "full_runtime_payload_sha256_without_self",
        "runtime_output_file_sha256",
    ):
        value = source.get(key)
        if not isinstance(value, str) or len(value) != 64:
            errors.append(f"source_execution.{key}")
    if not isinstance(source.get("workflow_source_commit"), str) or len(
        source.get("workflow_source_commit", "")
    ) != 40:
        errors.append("source_execution.workflow_source_commit")
    return errors


def derive_row(row: list[Any], col: dict[str, int]) -> dict[str, Any]:
    active = bool(row[col["active_before_perturbation"]])
    e_inner = float(row[col["e_inner"]])
    e_annulus = float(row[col["e_annulus"]])
    e_outer = float(row[col["e_outer"]])
    pphi_before = float(row[col["pphi_before"]])

    epsi_before = e_inner + e_annulus + e_outer
    if active:
        epsi_after = (
            INNER_FACTOR**2 * e_inner
            + ANNULUS_FACTOR**2 * e_annulus
            + e_outer
        )
        analytic_delta = (INNER_FACTOR**2 - 1.0) * e_inner + (
            ANNULUS_FACTOR**2 - 1.0
        ) * e_annulus
        applicability = "perturbed_active"
    else:
        epsi_after = epsi_before
        analytic_delta = 0.0
        applicability = "not_applicable_inactive"

    direct_delta = epsi_after - epsi_before
    direct_delta_phi = 0.0
    direct_delta_ledger = direct_delta
    ledger_before = epsi_before + pphi_before
    relative_delta_epsi = direct_delta / max(abs(epsi_before), 1e-30)
    relative_delta_ledger = direct_delta_ledger / max(abs(ledger_before), 1e-30)
    discrepancy = direct_delta - analytic_delta
    analytic_tolerance = NUMERIC_RTOL * max(
        1.0, abs(direct_delta), abs(analytic_delta)
    )
    analytic_agreement = abs(discrepancy) <= analytic_tolerance
    if active:
        neutral = abs(direct_delta_ledger) <= NUMERIC_RTOL * max(
            1.0, abs(ledger_before)
        )
    else:
        neutral = None

    return {
        "case_key": row[col["case_key"]],
        "applicability": applicability,
        "epsi_before": epsi_before,
        "epsi_after": epsi_after,
        "direct_delta_epsi": direct_delta,
        "direct_delta_phi": direct_delta_phi,
        "direct_delta_ledger": direct_delta_ledger,
        "relative_delta_epsi": relative_delta_epsi,
        "relative_delta_ledger": relative_delta_ledger,
        "analytic_delta_epsi": analytic_delta,
        "analytic_direct_discrepancy": discrepancy,
        "absolute_relative_epsi_shift_over_frozen_5pct_tolerance": (
            abs(relative_delta_epsi) / FROZEN_RECOVERY_ENERGY_TOLERANCE
        ),
        "analytic_agreement": analytic_agreement,
        "ledger_neutral_within_numeric_tolerance": neutral,
        "active_before_perturbation": active,
    }


def check_payload(payload: dict[str, Any]) -> dict[str, Any]:
    protocol_errors = _protocol_errors(payload)
    try:
        col = _column_map(payload)
    except ValueError as exc:
        protocol_errors.append(str(exc))
        col = {name: index for index, name in enumerate(EXPECTED_COLUMNS)}

    rows = payload.get("rows")
    if not isinstance(rows, list):
        rows = []
        protocol_errors.append("rows_not_list")

    actual_keys: list[str] = []
    duplicate_keys: list[str] = []
    seen: set[str] = set()
    numeric_mismatches: list[dict[str, Any]] = []
    categorical_mismatches: list[dict[str, Any]] = []
    derived_rows: list[dict[str, Any]] = []
    max_abs = 0.0
    max_rel = 0.0

    for row in rows:
        if not isinstance(row, list) or len(row) != len(EXPECTED_COLUMNS):
            protocol_errors.append("row_shape")
            continue
        key = str(row[col["case_key"]])
        actual_keys.append(key)
        if key in seen:
            duplicate_keys.append(key)
        seen.add(key)
        derived = derive_row(row, col)
        derived_rows.append(derived)

        for field in NUMERIC_FIELDS:
            stored = float(row[col[field]])
            expected = float(derived[field])
            abs_diff = abs(stored - expected)
            rel_diff = abs_diff / max(1.0, abs(stored), abs(expected))
            max_abs = max(max_abs, abs_diff)
            max_rel = max(max_rel, rel_diff)
            if not close_enough(stored, expected):
                numeric_mismatches.append(
                    {
                        "case_key": key,
                        "field": field,
                        "stored": stored,
                        "independent": expected,
                        "absolute_difference": abs_diff,
                        "tolerance": compare_tolerance(stored, expected),
                    }
                )

        for field in CATEGORICAL_FIELDS:
            stored = row[col[field]]
            expected = derived[field]
            if stored != expected:
                categorical_mismatches.append(
                    {
                        "case_key": key,
                        "field": field,
                        "stored": stored,
                        "independent": expected,
                    }
                )

    expected_keys = expected_case_keys()
    key_set_pass = (
        len(actual_keys) == len(expected_keys)
        and not duplicate_keys
        and set(actual_keys) == set(expected_keys)
    )

    active_count = sum(row["active_before_perturbation"] for row in derived_rows)
    inactive_count = len(derived_rows) - active_count
    neutral_count = sum(
        row["ledger_neutral_within_numeric_tolerance"] is True
        for row in derived_rows
    )
    non_neutral_count = sum(
        row["ledger_neutral_within_numeric_tolerance"] is False
        for row in derived_rows
    )
    analytic_pass = all(row["analytic_agreement"] for row in derived_rows)
    all_neutral = non_neutral_count == 0
    outcome = (
        "technical_or_methodological_failure"
        if not key_set_pass or not analytic_pass
        else "non_neutral_detected"
        if non_neutral_count > 0
        else "all_applicable_cases_neutral"
    )

    derived_summary = {
        "case_count": len(derived_rows),
        "key_set_pass": key_set_pass,
        "applicable_active_case_count": active_count,
        "inactive_not_applicable_case_count": inactive_count,
        "analytic_direct_all_pass": analytic_pass,
        "ledger_neutral_applicable_count": neutral_count,
        "ledger_non_neutral_applicable_count": non_neutral_count,
        "all_applicable_cases_neutral": all_neutral,
        "outcome": outcome,
    }
    primary_summary = payload.get("summary", {})
    for field, expected in derived_summary.items():
        if primary_summary.get(field) != expected:
            categorical_mismatches.append(
                {
                    "case_key": "__summary__",
                    "field": field,
                    "stored": primary_summary.get(field),
                    "independent": expected,
                }
            )

    passed = (
        not protocol_errors
        and key_set_pass
        and not numeric_mismatches
        and not categorical_mismatches
        and analytic_pass
    )
    return {
        "schema": SCHEMA,
        "stage": STAGE,
        "passed": passed,
        "protocol_pass": not protocol_errors,
        "protocol_errors": protocol_errors,
        "key_set_pass": key_set_pass,
        "duplicate_keys": duplicate_keys,
        "numeric_mismatch_count": len(numeric_mismatches),
        "categorical_mismatch_count": len(categorical_mismatches),
        "maximum_absolute_difference": max_abs,
        "maximum_relative_difference": max_rel,
        "compare_rtol": COMPARE_RTOL,
        "decision_numeric_rtol": NUMERIC_RTOL,
        "numeric_mismatches": numeric_mismatches,
        "categorical_mismatches": categorical_mismatches,
        "independent_summary": derived_summary,
        "primary_summary": primary_summary,
        "source_binding": payload.get("source_execution", {}),
        "checker_environment": {"python": platform.python_version()},
    }


def canonical_payload_sha256(payload: dict[str, Any]) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Independently check retained B4 Q2-PV1-A sufficient statistics."
    )
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    primary = json.loads(args.primary.read_text(encoding="utf-8"))
    result = check_payload(primary)
    result["canonical_payload_sha256_without_self"] = canonical_payload_sha256(result)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False))
    return 0 if result["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
