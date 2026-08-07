#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import platform
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

N = 32
DT = 1.0
MAIN_STEPS = 5000
RETURN_STEPS = 1000
SIGMA = 3.0
CAP_PSI = 1e6
CAP_PHI = 1e6
STENCIL_NAMES = ("LAP4", "LAP8")
START_PHI = (0.0, 1.0)
PROGRESS_INTERVAL = 500


@dataclass(frozen=True)
class IndependentLane:
    name: str
    damping: float = 0.005
    tanh_enabled: bool = True
    denominator_enabled: bool = True
    transfer_enabled: bool = True
    phi_cap_enabled: bool = True
    psi_guard_enabled: bool = True


INDEPENDENT_LANES = (
    IndependentLane("baseline"),
    IndependentLane(
        "no_hard_guards", phi_cap_enabled=False, psi_guard_enabled=False
    ),
    IndependentLane("no_linear_dissipation", damping=0.0),
    IndependentLane("no_explicit_tanh", tanh_enabled=False),
    IndependentLane("no_interaction_denominator", denominator_enabled=False),
    IndependentLane("no_mode_coupling", transfer_enabled=False),
    IndependentLane("no_phi_cap", phi_cap_enabled=False),
)


r_index, c_index = np.indices((N, N), dtype=float)
origin = (N - 1) / 2.0
distance = np.hypot(r_index - origin, c_index - origin)
angle = np.arctan2(c_index - origin, r_index - origin)
annulus_id = np.floor(distance).astype(int)
annulus_count = int(annulus_id.max()) + 1
seed_shape = np.exp(-(distance**2) / (2.0 * SIGMA**2))
seed_shape = (seed_shape / seed_shape.max()).astype(np.complex128)


def laplacian_weighted(
    state: np.ndarray, permeability: np.ndarray, coefficient: float, stencil: str
) -> np.ndarray:
    row_minus = np.roll(state, 1, axis=1)
    row_plus = np.roll(state, -1, axis=1)
    col_minus = np.roll(state, 1, axis=2)
    col_plus = np.roll(state, -1, axis=2)
    krm = np.roll(permeability, 1, axis=1)
    krp = np.roll(permeability, -1, axis=1)
    kcm = np.roll(permeability, 1, axis=2)
    kcp = np.roll(permeability, -1, axis=2)

    weighted_sum = row_minus * krm + row_plus * krp + col_minus * kcm + col_plus * kcp
    weight_sum = krm + krp + kcm + kcp
    if stencil == "LAP8":
        diagonals = (
            np.roll(row_minus, 1, axis=2) * np.roll(krm, 1, axis=2)
            + np.roll(row_minus, -1, axis=2) * np.roll(krm, -1, axis=2)
            + np.roll(row_plus, 1, axis=2) * np.roll(krp, 1, axis=2)
            + np.roll(row_plus, -1, axis=2) * np.roll(krp, -1, axis=2)
        )
        diagonal_weights = (
            np.roll(krm, 1, axis=2)
            + np.roll(krm, -1, axis=2)
            + np.roll(krp, 1, axis=2)
            + np.roll(krp, -1, axis=2)
        )
        weighted_sum = weighted_sum + 0.25 * diagonals
        weight_sum = weight_sum + 0.25 * diagonal_weights
    elif stencil != "LAP4":
        raise ValueError(stencil)
    return coefficient * (weighted_sum - weight_sum * state)


def regression_slope(series: np.ndarray) -> np.ndarray:
    t = np.arange(series.shape[0], dtype=float)
    t = t - t.mean()
    return t @ (series - series.mean(axis=0, keepdims=True)) / (t @ t)


def profile(values: np.ndarray) -> np.ndarray:
    totals = np.bincount(
        annulus_id.ravel(), weights=values.ravel(), minlength=annulus_count
    )
    counts = np.bincount(annulus_id.ravel(), minlength=annulus_count)
    return totals / np.maximum(counts, 1)


def summary(psi: np.ndarray, phi: np.ndarray) -> dict[str, Any]:
    energy = np.abs(psi) ** 2
    total = float(energy.sum())
    if total > 0.0 and math.isfinite(total):
        row_centre = float((energy * r_index).sum() / total)
        col_centre = float((energy * c_index).sum() / total)
        displacement = float(math.hypot(row_centre - origin, col_centre - origin))
        ordered = np.argsort(distance.ravel())
        accumulated = np.cumsum(energy.ravel()[ordered])
        half_position = int(np.searchsorted(accumulated, 0.5 * total))
        half_radius = float(distance.ravel()[ordered[min(half_position, ordered.size - 1)]])
        anisotropy = float(abs(np.sum(energy * np.exp(4j * angle))) / total)
    else:
        displacement = math.inf
        half_radius = math.inf
        anisotropy = math.inf
    return {
        "total_energy": total,
        "max_abs_psi": float(np.abs(psi).max()),
        "phi_mean": float(phi.mean()),
        "phi_max": float(phi.max()),
        "half_energy_radius": half_radius,
        "center_displacement": displacement,
        "anisotropy4": anisotropy,
        "energy_radial_profile": profile(energy).tolist(),
        "phi_radial_profile": profile(phi).tolist(),
        "fraction_r6": float(energy[distance <= 6].sum() / total) if total > 0 else 0.0,
    }


def rel_l2(left: list[float], right: list[float]) -> float:
    a = np.asarray(left)
    b = np.asarray(right)
    return float(np.linalg.norm(b - a) / (np.linalg.norm(a) + 1e-30))


def lane_vectors(specs: list[tuple[IndependentLane, float]]) -> dict[str, np.ndarray]:
    column = lambda values, dtype: np.asarray(values, dtype=dtype)[:, None, None]
    return {
        "guard": column([lane.psi_guard_enabled for lane, _ in specs], bool),
        "phi_cap": column([lane.phi_cap_enabled for lane, _ in specs], bool),
        "tanh": column([lane.tanh_enabled for lane, _ in specs], bool),
        "denominator": column([lane.denominator_enabled for lane, _ in specs], bool),
        "transfer": column([lane.transfer_enabled for lane, _ in specs], bool),
        "damping": column([lane.damping for lane, _ in specs], float),
    }


def independent_step(
    psi: np.ndarray,
    phi: np.ndarray,
    permeability: np.ndarray,
    stencil: str,
    switches: dict[str, np.ndarray],
    active: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    old_psi = psi.copy()
    old_phi = phi.copy()
    multiplier = np.ones_like(phi)

    phi_for_interaction = np.clip(phi, 0.0, 10.0)
    raw_gain = 0.04 * phi_for_interaction * permeability * multiplier
    gain = np.where(switches["tanh"], 0.1 * np.tanh(raw_gain / 0.1), raw_gain)
    source = gain * psi
    source = np.where(
        switches["denominator"], source / (1.0 + np.abs(source) / 10.0), source
    )

    row_gradient, column_gradient = np.gradient(phi, axis=(1, 2))
    drift = -0.004 * (row_gradient + 1j * column_gradient) * permeability
    drift = drift / (1.0 + np.abs(drift) / 10.0)
    psi = psi + drift * DT

    magnitude = np.abs(psi)
    psi_cap_mask = (magnitude > CAP_PSI) & switches["guard"]
    psi_cap_rows = psi_cap_mask.reshape(psi.shape[0], -1).any(axis=1)
    factor = np.ones_like(magnitude)
    factor[psi_cap_mask] = CAP_PSI / (magnitude[psi_cap_mask] + 1e-30)
    psi = psi * factor

    psi = psi + source * DT
    psi = psi - switches["damping"] * psi * DT
    psi = psi + laplacian_weighted(psi, permeability, 0.05, stencil) * permeability * DT

    energy = np.abs(psi) ** 2
    transfer_amount = 0.001 * energy * permeability * DT
    transferred_phi = phi + transfer_amount
    transferred_psi = psi / (np.sqrt(energy) + 1e-12) * np.sqrt(
        np.maximum(energy - transfer_amount, 0.0)
    )
    fallback_phi = phi + 0.0007 * (128.0 / N) ** 2 * (energy - phi) * DT
    phi = np.where(switches["transfer"], transferred_phi, fallback_phi)
    psi = np.where(switches["transfer"], transferred_psi, psi)

    phi = phi + 0.05 * laplacian_weighted(phi, permeability, 0.05, stencil)
    phi_cap_mask = ((phi < 0.0) | (phi > CAP_PHI)) & switches["phi_cap"]
    phi_cap_rows = phi_cap_mask.reshape(phi.shape[0], -1).any(axis=1)
    phi = np.where(switches["phi_cap"], np.clip(phi, 0.0, CAP_PHI), phi)

    finite_psi = np.isfinite(psi)
    finite_magnitude = np.where(finite_psi, np.abs(psi), 0.0)
    reset_rows = switches["guard"][:, 0, 0] & (
        ~finite_psi.reshape(psi.shape[0], -1).all(axis=1)
        | (finite_magnitude.max(axis=(1, 2)) >= CAP_PSI * 0.99)
    )
    psi[reset_rows] = 0.0

    inactive = ~active
    psi[inactive] = old_psi[inactive]
    phi[inactive] = old_phi[inactive]
    reset_rows[inactive] = False
    psi_cap_rows[inactive] = False
    phi_cap_rows[inactive] = False
    return psi, phi, reset_rows, psi_cap_rows, phi_cap_rows


def progress(stencil: str, phase: str, done: int, total: int, start: float) -> None:
    if done != total and done % PROGRESS_INTERVAL:
        return
    print(
        json.dumps(
            {
                "checker_phase": phase,
                "stencil": stencil,
                "completed": done,
                "total": total,
                "elapsed_seconds": round(time.monotonic() - start, 3),
            },
            sort_keys=True,
        ),
        file=sys.stderr,
        flush=True,
    )


def rerun_stencil(stencil: str) -> list[dict[str, Any]]:
    specs = [(lane, phi0) for lane in INDEPENDENT_LANES for phi0 in START_PHI]
    count = len(specs)
    psi = np.stack([seed_shape.copy() for _ in specs])
    phi = np.stack([np.full((N, N), phi0) for _, phi0 in specs])
    permeability = np.ones((count, N, N))
    switches = lane_vectors(specs)
    active = np.ones(count, dtype=bool)
    last_psi = psi.copy()
    last_phi = phi.copy()
    failure_stage: list[str | None] = [None] * count
    failure_step = np.full(count, -1, dtype=int)
    reset_count = np.zeros(count, dtype=int)
    psi_cap_count = np.zeros(count, dtype=int)
    phi_cap_count = np.zeros(count, dtype=int)
    energies = np.empty((MAIN_STEPS, count))
    phi_means = np.empty((MAIN_STEPS, count))
    initial = [summary(psi[i], phi[i]) for i in range(count)]

    start = time.monotonic()
    with np.errstate(all="ignore"):
        for step in range(MAIN_STEPS):
            psi, phi, reset, psi_cap, phi_cap = independent_step(
                psi, phi, permeability, stencil, switches, active
            )
            reset_count += reset
            psi_cap_count += psi_cap
            phi_cap_count += phi_cap
            finite = (
                np.isfinite(psi).reshape(count, -1).all(axis=1)
                & np.isfinite(phi).reshape(count, -1).all(axis=1)
            )
            failed = active & ~finite
            for index in np.flatnonzero(failed):
                failure_stage[index] = "primary"
                failure_step[index] = step + 1
            psi[failed] = last_psi[failed]
            phi[failed] = last_phi[failed]
            active[failed] = False
            valid = active & finite
            last_psi[valid] = psi[valid]
            last_phi[valid] = phi[valid]
            energies[step] = np.mean(np.abs(psi) ** 2, axis=(1, 2))
            phi_means[step] = np.mean(phi, axis=(1, 2))
            progress(stencil, "primary", step + 1, MAIN_STEPS, start)

    pre = [summary(psi[i], phi[i]) for i in range(count)]
    tail = MAIN_STEPS // 5
    energy_slope = regression_slope(energies[-tail:])
    phi_slope = regression_slope(phi_means[-tail:])
    phi_tail_mean = phi_means[-tail:].mean(axis=0)

    psi[:, distance <= 2] *= np.where(active[:, None], 1.5, 1.0)
    psi[:, (distance >= 3) & (distance <= 5)] *= np.where(active[:, None], 0.5, 1.0)
    last_psi[active] = psi[active]
    return_resets = np.zeros(count, dtype=int)
    return_psi_caps = np.zeros(count, dtype=int)
    return_phi_caps = np.zeros(count, dtype=int)
    start = time.monotonic()
    with np.errstate(all="ignore"):
        for step in range(RETURN_STEPS):
            psi, phi, reset, psi_cap, phi_cap = independent_step(
                psi, phi, permeability, stencil, switches, active
            )
            return_resets += reset
            return_psi_caps += psi_cap
            return_phi_caps += phi_cap
            finite = (
                np.isfinite(psi).reshape(count, -1).all(axis=1)
                & np.isfinite(phi).reshape(count, -1).all(axis=1)
            )
            failed = active & ~finite
            for index in np.flatnonzero(failed):
                failure_stage[index] = "recovery"
                failure_step[index] = step + 1
            psi[failed] = last_psi[failed]
            phi[failed] = last_phi[failed]
            active[failed] = False
            valid = active & finite
            last_psi[valid] = psi[valid]
            last_phi[valid] = phi[valid]
            progress(stencil, "recovery", step + 1, RETURN_STEPS, start)

    post = [summary(psi[i], phi[i]) for i in range(count)]
    output: list[dict[str, Any]] = []
    for index, (lane, phi0) in enumerate(specs):
        e_error = abs(post[index]["total_energy"] - pre[index]["total_energy"]) / (
            abs(pre[index]["total_energy"]) + 1e-30
        )
        e_profile = rel_l2(
            pre[index]["energy_radial_profile"], post[index]["energy_radial_profile"]
        )
        p_profile = rel_l2(
            pre[index]["phi_radial_profile"], post[index]["phi_radial_profile"]
        )
        r_error = abs(post[index]["half_energy_radius"] - pre[index]["half_energy_radius"])
        nontrivial = bool(
            pre[index]["total_energy"]
            >= max(1e-12, initial[index]["total_energy"] * 0.01)
            and pre[index]["fraction_r6"] >= 0.5
        )
        finite = failure_stage[index] is None
        reset_free = reset_count[index] + return_resets[index] == 0
        psi_recovery = bool(
            finite
            and reset_free
            and e_error <= 0.05
            and e_profile <= 0.10
            and r_error <= 1.0
            and post[index]["center_displacement"] <= 0.5
        )
        threshold = max(1e-10, 1e-8 * abs(phi_tail_mean[index]))
        full = bool(
            psi_recovery
            and phi_cap_count[index] + return_phi_caps[index] == 0
            and p_profile <= 0.10
            and phi_slope[index] <= threshold
        )
        output.append(
            {
                "key": (lane.name, stencil, phi0),
                "pre_total_energy": pre[index]["total_energy"],
                "pre_max_abs_psi": pre[index]["max_abs_psi"],
                "pre_phi_mean": pre[index]["phi_mean"],
                "pre_phi_max": pre[index]["phi_max"],
                "pre_half_radius": pre[index]["half_energy_radius"],
                "pre_anisotropy": pre[index]["anisotropy4"],
                "post_total_energy": post[index]["total_energy"],
                "post_phi_mean": post[index]["phi_mean"],
                "post_phi_max": post[index]["phi_max"],
                "energy_slope": float(energy_slope[index]),
                "phi_slope": float(phi_slope[index]),
                "energy_error": e_error,
                "energy_profile_error": e_profile,
                "phi_profile_error": p_profile,
                "half_radius_error": r_error,
                "centre_displacement": post[index]["center_displacement"],
                "finite": finite,
                "reset_free": reset_free,
                "psi_cap_free": bool(psi_cap_count[index] + return_psi_caps[index] == 0),
                "phi_cap_free": bool(phi_cap_count[index] + return_phi_caps[index] == 0),
                "psi_recovery": psi_recovery,
                "full_recovery": full,
                "nontrivial_secondary": nontrivial,
                "failure_stage": failure_stage[index],
                "failure_step": None if failure_stage[index] is None else int(failure_step[index]),
            }
        )
    return output


def primary_projection(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "key": (row["lane"], row["stencil"], row["phi0"]),
        "pre_total_energy": row["pre_perturbation"]["total_energy"],
        "pre_max_abs_psi": row["pre_perturbation"]["max_abs_psi"],
        "pre_phi_mean": row["pre_perturbation"]["phi_mean"],
        "pre_phi_max": row["pre_perturbation"]["phi_max"],
        "pre_half_radius": row["pre_perturbation"]["half_energy_radius"],
        "pre_anisotropy": row["pre_perturbation"]["anisotropy4"],
        "post_total_energy": row["post_recovery"]["total_energy"],
        "post_phi_mean": row["post_recovery"]["phi_mean"],
        "post_phi_max": row["post_recovery"]["phi_max"],
        "energy_slope": row["tail"]["energy_slope_per_step"],
        "phi_slope": row["tail"]["phi_slope_per_step"],
        "energy_error": row["recovery"]["total_energy_relative_error"],
        "energy_profile_error": row["recovery"]["energy_radial_profile_l2_error"],
        "phi_profile_error": row["recovery"]["phi_radial_profile_l2_error"],
        "half_radius_error": row["recovery"]["half_energy_radius_absolute_error"],
        "centre_displacement": row["recovery"]["center_displacement_after"],
        "finite": row["boundedness"]["finite"],
        "reset_free": row["boundedness"]["reset_free"],
        "psi_cap_free": row["boundedness"]["psi_cap_free"],
        "phi_cap_free": row["boundedness"]["phi_cap_free"],
        "psi_recovery": row["recovery"]["localized_psi_recovery"],
        "full_recovery": row["recovery"]["localized_full_state_recovery"],
        "nontrivial_secondary": row["recovery"][
            "secondary_nontrivial_localized_pre_state"
        ],
        "failure_stage": row["events"]["failure_stage"],
        "failure_step": row["events"]["failure_step"],
    }


def numeric_values_match(a: float, b: float) -> bool:
    """Compare numeric diagnostics while preserving declared non-finite sentinels."""
    if math.isnan(a) or math.isnan(b):
        return math.isnan(a) and math.isnan(b)
    if math.isinf(a) or math.isinf(b):
        return a == b
    return math.isclose(a, b, rel_tol=5e-11, abs_tol=5e-12)


def check(primary: dict[str, Any]) -> dict[str, Any]:
    independent: list[dict[str, Any]] = []
    for stencil in STENCIL_NAMES:
        independent.extend(rerun_stencil(stencil))
    expected = {tuple(item["key"]): item for item in independent}
    observed = {
        tuple(item["key"]): item
        for item in (primary_projection(row) for row in primary["rows"])
    }
    key_pass = expected.keys() == observed.keys()

    numerical_fields = (
        "pre_total_energy",
        "pre_max_abs_psi",
        "pre_phi_mean",
        "pre_phi_max",
        "pre_half_radius",
        "pre_anisotropy",
        "post_total_energy",
        "post_phi_mean",
        "post_phi_max",
        "energy_slope",
        "phi_slope",
        "energy_error",
        "energy_profile_error",
        "phi_profile_error",
        "half_radius_error",
        "centre_displacement",
    )
    categorical_fields = (
        "finite",
        "reset_free",
        "psi_cap_free",
        "phi_cap_free",
        "psi_recovery",
        "full_recovery",
        "nontrivial_secondary",
        "failure_stage",
        "failure_step",
    )
    max_absolute = 0.0
    max_relative = 0.0
    numeric_mismatches: list[dict[str, Any]] = []
    category_mismatches: list[dict[str, Any]] = []
    for key in sorted(expected):
        left = expected[key]
        right = observed[key]
        for field in numerical_fields:
            a = float(left[field])
            b = float(right[field])
            if math.isfinite(a) and math.isfinite(b):
                difference = abs(a - b)
                relative = difference / (abs(a) + 1e-30)
                max_absolute = max(max_absolute, difference)
                max_relative = max(max_relative, relative)
            if not numeric_values_match(a, b):
                numeric_mismatches.append(
                    {"key": key, "field": field, "independent": a, "primary": b}
                )
        for field in categorical_fields:
            if left[field] != right[field]:
                category_mismatches.append(
                    {
                        "key": key,
                        "field": field,
                        "independent": left[field],
                        "primary": right[field],
                    }
                )

    fidelity = primary.get("fidelity_corrections", {})
    fidelity_pass = all(
        (
            fidelity.get("gaussian_peak_normalized_to_one"),
            fidelity.get("production_gradient_axis_order_preserved"),
            fidelity.get("nontrivial_gate_demoted_to_secondary"),
            fidelity.get("unregistered_large_value_failfast_removed"),
            fidelity.get("last_finite_failure_state_preserved"),
            fidelity.get(
                "stencil_decision_compares_all_boundedness_and_recovery_statuses"
            ),
            fidelity.get("one_sided_phi_slope_gate_preserved"),
            fidelity.get("absolute_phi_slope_added_as_secondary"),
            fidelity.get("physical_parameters_or_primary_thresholds_changed") is False,
        )
    )
    protocol_pass = bool(
        primary.get("schema") == "lineum-b4-saturation-localized-l1/2"
        and primary["protocol"]["grid_size"] == 32
        and primary["protocol"]["dt"] == 1.0
        and primary["protocol"]["steps"] == 5000
        and primary["protocol"]["recovery_steps"] == 1000
        and primary["protocol"]["gaussian_peak"] == 1.0
        and len(primary["rows"]) == 28
    )
    passed = bool(
        key_pass
        and not numeric_mismatches
        and not category_mismatches
        and fidelity_pass
        and protocol_pass
    )
    return {
        "schema": "lineum-b4-saturation-localized-l1-check/1",
        "passed": passed,
        "independence": {
            "imports_primary_runner": False,
            "recomputes_all_28_runs": True,
            "separate_update_and_metric_implementation": True,
        },
        "protocol_pass": protocol_pass,
        "fidelity_receipt_pass": fidelity_pass,
        "key_set_pass": key_pass,
        "numeric_mismatch_count": len(numeric_mismatches),
        "categorical_mismatch_count": len(category_mismatches),
        "maximum_absolute_difference": max_absolute,
        "maximum_relative_difference": max_relative,
        "numeric_mismatches": numeric_mismatches[:20],
        "categorical_mismatches": category_mismatches[:20],
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
    }


def json_ready(value: Any) -> Any:
    """Return a strict-JSON representation without changing in-memory metrics."""
    if isinstance(value, np.generic):
        return json_ready(value.item())
    if isinstance(value, float) and not math.isfinite(value):
        if math.isnan(value):
            return "NaN"
        return "Infinity" if value > 0 else "-Infinity"
    if isinstance(value, dict):
        return {key: json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_ready(item) for item in value]
    return value


def restore_nonfinite(value: Any) -> Any:
    """Restore explicit non-finite markers from the strict primary JSON."""
    if value == "Infinity":
        return math.inf
    if value == "-Infinity":
        return -math.inf
    if value == "NaN":
        return math.nan
    if isinstance(value, dict):
        return {key: restore_nonfinite(item) for key, item in value.items()}
    if isinstance(value, list):
        return [restore_nonfinite(item) for item in value]
    return value


def json_scalar(value: Any) -> Any:
    """Convert NumPy scalar values at the JSON boundary only."""
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(f"Object of type {value.__class__.__name__} is not JSON serializable")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    primary = restore_nonfinite(json.loads(args.result.read_text(encoding="utf-8")))
    receipt = check(primary)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(
            json_ready(receipt),
            indent=2,
            sort_keys=True,
            allow_nan=False,
            default=json_scalar,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps(receipt, indent=2, sort_keys=True, default=json_scalar))
    if not receipt["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
