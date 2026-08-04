#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import statistics
from pathlib import Path
from typing import Any

EXPECTED_SOURCE_BLOB = "bb877021810691223a0eb960a45493a2e351112a"


def _interaction_gain(phi_value: float, use_tanh: bool) -> float:
    bounded_phi = min(10.0, max(0.0, phi_value))
    linear_argument = 0.04 * bounded_phi
    if use_tanh:
        return 0.1 * math.tanh(linear_argument / 0.1)
    return linear_argument


def _advance(
    amplitude: float,
    phi_value: float,
    lane: dict[str, Any],
    dt: float,
    grid_size: int,
) -> tuple[float, float, bool]:
    # Independently reconstructed scalar recurrence for the frozen homogeneous case.
    # The phase is constant, so only the non-negative amplitude is needed.
    psi_cap = 1_000_000.0
    phi_cap = 1_000_000.0

    if lane["use_psi_guard"] and amplitude > psi_cap:
        amplitude = psi_cap

    drive = _interaction_gain(phi_value, lane["use_tanh"]) * amplitude
    if lane["use_interaction_denominator"]:
        drive /= 1.0 + abs(drive) / 10.0

    amplitude += drive * dt
    amplitude -= lane["effective_dissipation_rate"] * amplitude * dt
    energy = amplitude * amplitude

    if lane["use_mode_coupling"]:
        transferred = 0.001 * energy * dt
        phi_value += transferred
        residual = max(energy - transferred, 0.0)
        amplitude = amplitude / (math.sqrt(energy) + 1e-12) * math.sqrt(residual)
    else:
        reaction = 0.0007 * (128.0 / grid_size) ** 2
        phi_value += reaction * (energy - phi_value) * dt

    if lane["use_phi_cap"]:
        phi_value = min(phi_cap, max(0.0, phi_value))

    reset = False
    if lane["use_psi_guard"] and (
        not math.isfinite(amplitude) or amplitude >= 0.99 * psi_cap
    ):
        amplitude = 0.0
        reset = True
    return amplitude, phi_value, reset


def _least_squares_slope(values: list[float]) -> float:
    count = len(values)
    if count < 2:
        return 0.0
    center_x = (count - 1) / 2.0
    center_y = sum(values) / count
    numerator = 0.0
    denominator = 0.0
    for index, value in enumerate(values):
        dx = index - center_x
        numerator += dx * (value - center_y)
        denominator += dx * dx
    return 0.0 if denominator == 0.0 else numerator / denominator


def _reproduce_row(
    lane: dict[str, Any],
    dt: float,
    grid_size: int,
    phi0: float,
    steps: int,
    recovery_steps: int,
    initial_abs_psi: float,
) -> dict[str, Any]:
    amplitude = initial_abs_psi
    phi_value = phi0
    energies: list[float] = []
    phis: list[float] = []
    reset_count = 0
    diverged = False
    completed = steps

    for index in range(steps):
        amplitude, phi_value, reset = _advance(
            amplitude, phi_value, lane, dt, grid_size
        )
        reset_count += int(reset)
        energy = amplitude * amplitude
        energies.append(energy)
        phis.append(phi_value)
        if (
            not math.isfinite(energy)
            or not math.isfinite(phi_value)
            or amplitude > 1e15
            or abs(phi_value) > 1e18
        ):
            diverged = True
            completed = index + 1
            break

    tail_count = max(10, len(energies) // 5)
    energy_tail = energies[-tail_count:]
    phi_tail = phis[-tail_count:]
    tail_mean = sum(energy_tail) / len(energy_tail)
    tail_std = statistics.pstdev(energy_tail)
    tail_cv = tail_std / (abs(tail_mean) + 1e-30)
    energy_slope = _least_squares_slope(energy_tail)
    phi_slope = _least_squares_slope(phi_tail)

    reference_amplitude = amplitude
    reference_phi = phi_value
    reference_energy = reference_amplitude * reference_amplitude

    amplitude *= 1.5
    recovery_resets = 0
    for _ in range(recovery_steps):
        amplitude, phi_value, reset = _advance(
            amplitude, phi_value, lane, dt, grid_size
        )
        recovery_resets += int(reset)
        if (
            not math.isfinite(amplitude)
            or not math.isfinite(phi_value)
            or amplitude > 1e15
            or abs(phi_value) > 1e18
        ):
            diverged = True
            break

    recovered_energy = amplitude * amplitude if math.isfinite(amplitude) else math.inf
    energy_error = abs(recovered_energy - reference_energy) / (
        abs(reference_energy) + 1e-30
    )
    phi_error = abs(phi_value - reference_phi) / (abs(reference_phi) + 1e-30)

    if diverged:
        outcome = "diverged"
    elif reset_count + recovery_resets > 0:
        outcome = "guard_reset"
    elif tail_mean < 1e-16:
        outcome = "decayed_to_zero"
    elif (
        abs(energy_slope) <= max(1e-12, abs(tail_mean) * 1e-8)
        and tail_cv <= 1e-4
    ):
        outcome = "stationary"
    elif energy_slope > 0.0:
        outcome = "growing"
    else:
        outcome = "decaying"

    return {
        "steps_completed": completed,
        "outcome": outcome,
        "final_abs_psi": reference_amplitude,
        "final_energy": reference_energy,
        "final_phi": reference_phi,
        "tail_energy_mean": tail_mean,
        "tail_energy_cv": tail_cv,
        "tail_energy_slope_per_step": energy_slope,
        "tail_phi_slope_per_step": phi_slope,
        "resets_before_perturbation": reset_count,
        "resets_after_perturbation": recovery_resets,
        "recovery_energy_relative_error": energy_error,
        "recovery_phi_relative_error": phi_error,
        "recovery_pass_energy": energy_error <= 0.05,
        "diverged": diverged,
    }


def _relative_difference(left: float, right: float) -> float:
    return abs(left - right) / max(1.0, abs(left), abs(right))


def check(path: Path) -> dict[str, Any]:
    result = json.loads(path.read_text(encoding="utf-8"))
    protocol = result["protocol"]
    lanes = {lane["name"]: lane for lane in protocol["lanes"]}

    numeric_fields = (
        "final_abs_psi",
        "final_energy",
        "final_phi",
        "tail_energy_mean",
        "tail_energy_cv",
        "tail_energy_slope_per_step",
        "tail_phi_slope_per_step",
        "recovery_energy_relative_error",
        "recovery_phi_relative_error",
    )
    exact_fields = (
        "steps_completed",
        "outcome",
        "resets_before_perturbation",
        "resets_after_perturbation",
        "recovery_pass_energy",
        "diverged",
    )

    max_numeric_relative_difference = 0.0
    exact_mismatches: list[dict[str, Any]] = []
    for retained in result["rows"]:
        reproduced = _reproduce_row(
            lanes[retained["lane"]],
            float(retained["dt"]),
            int(retained["grid_size"]),
            float(retained["phi0"]),
            int(protocol["steps"]),
            int(protocol["recovery_steps"]),
            float(protocol["initial_abs_psi"]),
        )
        for field in numeric_fields:
            max_numeric_relative_difference = max(
                max_numeric_relative_difference,
                _relative_difference(float(retained[field]), float(reproduced[field])),
            )
        for field in exact_fields:
            if retained[field] != reproduced[field]:
                exact_mismatches.append(
                    {
                        "lane": retained["lane"],
                        "dt": retained["dt"],
                        "grid_size": retained["grid_size"],
                        "phi0": retained["phi0"],
                        "field": field,
                        "retained": retained[field],
                        "reproduced": reproduced[field],
                    }
                )

    lookup = {
        (row["lane"], row["dt"], row["grid_size"], row["phi0"]): row
        for row in result["rows"]
    }

    max_config_difference = 0.0
    for dt in protocol["dt_values"]:
        for size in protocol["grid_sizes"]:
            for phi0 in protocol["phi0_values"]:
                baseline = lookup[("baseline", dt, size, phi0)]
                for lane_name in (
                    "configured_dissipation_zero",
                    "configured_dissipation_one",
                ):
                    comparison = lookup[(lane_name, dt, size, phi0)]
                    for field in (
                        "final_abs_psi",
                        "final_phi",
                        "recovery_energy_relative_error",
                    ):
                        max_config_difference = max(
                            max_config_difference,
                            abs(float(baseline[field]) - float(comparison[field])),
                        )

    stationary_high_phi = [
        row
        for row in result["rows"]
        if row["lane"] == "baseline"
        and row["phi0"] >= 1.0
        and row["outcome"] == "stationary"
    ]
    stationary_recovery_pass = bool(stationary_high_phi) and all(
        row["recovery_pass_energy"] for row in stationary_high_phi
    )

    no_denominator_high_phi = [
        row
        for row in result["rows"]
        if row["lane"] == "no_interaction_denominator" and row["phi0"] >= 1.0
    ]
    no_phi_cap_high_phi = [
        row
        for row in result["rows"]
        if row["lane"] == "no_phi_cap" and row["phi0"] >= 1.0
    ]

    checks = {
        "source_blob_sha_pass": result["source"]["git_blob_sha"] == EXPECTED_SOURCE_BLOB,
        "row_count": len(result["rows"]),
        "expected_row_count_pass": len(result["rows"]) == 405,
        "independent_recurrence_max_relative_difference": max_numeric_relative_difference,
        "independent_recurrence_numeric_pass": max_numeric_relative_difference <= 1e-12,
        "independent_recurrence_exact_mismatch_count": len(exact_mismatches),
        "independent_recurrence_exact_pass": not exact_mismatches,
        "configured_dissipation_max_difference": max_config_difference,
        "configured_dissipation_invariance_pass": max_config_difference <= 1e-15,
        "stationary_high_phi_count": len(stationary_high_phi),
        "stationary_high_phi_recovery_pass": stationary_recovery_pass,
        "no_denominator_high_phi_unstable_pass": all(
            row["outcome"] in {"diverged", "guard_reset"}
            for row in no_denominator_high_phi
        ),
        "uncapped_phi_positive_tail_pass": all(
            row["tail_phi_slope_per_step"] > 0.0 for row in no_phi_cap_high_phi
        ),
        "initial_checker_failure_preserved": {
            "status": "failed",
            "reason": "The first checker incorrectly required every dt lane to reach its analytic asymptote within the frozen 5000-step horizon.",
            "baseline_fixed_point_max_relative_error": 0.1435,
            "no_dissipation_fixed_point_max_relative_error": 0.8312,
            "linearized_interaction_fixed_point_max_relative_error": 0.0784,
        },
    }
    boolean_checks = [
        checks["source_blob_sha_pass"],
        checks["expected_row_count_pass"],
        checks["independent_recurrence_numeric_pass"],
        checks["independent_recurrence_exact_pass"],
        checks["configured_dissipation_invariance_pass"],
        checks["stationary_high_phi_recovery_pass"],
        checks["no_denominator_high_phi_unstable_pass"],
        checks["uncapped_phi_positive_tail_pass"],
    ]
    checks["passed"] = all(boolean_checks)
    if exact_mismatches:
        checks["exact_mismatch_examples"] = exact_mismatches[:10]
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    checks = check(args.result)
    args.output.write_text(
        json.dumps(checks, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(checks, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
