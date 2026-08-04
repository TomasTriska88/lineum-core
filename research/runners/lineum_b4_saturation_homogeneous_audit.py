#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import numpy as np

SOURCE_BLOB_SHA = "bb877021810691223a0eb960a45493a2e351112a"
STEPS = 5000
RECOVERY_STEPS = 1000
DT_VALUES = (0.1, 0.5, 1.0)
GRID_SIZES = (32, 64, 128)
PHI_VALUES = (0.0, 0.05, 0.15, 1.0, 10.0)


@dataclass(frozen=True)
class Lane:
    name: str
    configured_dissipation_rate: float = 0.005
    effective_dissipation_rate: float = 0.005
    use_tanh: bool = True
    use_interaction_denominator: bool = True
    use_mode_coupling: bool = True
    use_phi_cap: bool = True
    use_psi_guard: bool = True


LANES = (
    Lane("baseline"),
    Lane("configured_dissipation_zero", configured_dissipation_rate=0.0),
    Lane("configured_dissipation_one", configured_dissipation_rate=1.0),
    Lane("no_hard_guards", use_phi_cap=False, use_psi_guard=False),
    Lane("no_linear_dissipation", effective_dissipation_rate=0.0),
    Lane("no_explicit_tanh", use_tanh=False),
    Lane("no_interaction_denominator", use_interaction_denominator=False),
    Lane("no_mode_coupling", use_mode_coupling=False),
    Lane("no_phi_cap", use_phi_cap=False),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def interaction_coefficient(phi: float, use_tanh: bool) -> float:
    phi_int = min(max(phi, 0.0), 10.0)
    raw = 0.04 * phi_int
    return 0.1 * math.tanh(raw / 0.1) if use_tanh else raw


def step_homogeneous(
    psi: complex,
    phi: float,
    lane: Lane,
    dt: float,
    grid_size: int,
    psi_amp_cap: float = 1e6,
    phi_cap: float = 1e6,
) -> tuple[complex, float, bool]:
    # Exact homogeneous deterministic reduction of the checked-in NumPy diffusion path:
    # no gradients, no diffusion contribution, kappa=1, mu=0, delta=0,
    # disable_quantum_noise=True.
    if lane.use_psi_guard and abs(psi) > psi_amp_cap:
        psi *= psi_amp_cap / (abs(psi) + 1e-30)

    factor = interaction_coefficient(phi, lane.use_tanh)
    interaction = factor * psi
    if lane.use_interaction_denominator:
        interaction /= 1.0 + abs(interaction) / 10.0

    psi += interaction * dt
    # Current implementation ignores CoreConfig.dissipation_rate and uses literal 0.005.
    psi -= lane.effective_dissipation_rate * psi * dt
    e_psi = abs(psi) ** 2

    if lane.use_mode_coupling:
        delta_e = 0.001 * e_psi * dt
        phi += delta_e
        new_mag = math.sqrt(max(e_psi - delta_e, 0.0))
        psi = psi / (math.sqrt(e_psi) + 1e-12) * new_mag
    else:
        dynamic_reaction = 0.0007 * (128.0 / grid_size) ** 2
        phi += dynamic_reaction * (e_psi - phi) * dt

    if lane.use_phi_cap:
        phi = min(max(phi, 0.0), phi_cap)

    reset = False
    if lane.use_psi_guard and (
        not math.isfinite(psi.real + psi.imag) or abs(psi) >= psi_amp_cap * 0.99
    ):
        psi = 0.0j
        reset = True
    return psi, phi, reset


def linear_slope(values: np.ndarray) -> float:
    if len(values) < 2:
        return 0.0
    x = np.arange(len(values), dtype=float)
    x -= x.mean()
    y = values.astype(float)
    y -= y.mean()
    denom = float(np.dot(x, x))
    return 0.0 if denom == 0 else float(np.dot(x, y) / denom)


def summarize_run(lane: Lane, dt: float, grid_size: int, phi0: float) -> dict[str, Any]:
    psi = 0.01 + 0.0j
    phi = float(phi0)
    energies = np.empty(STEPS, dtype=float)
    phis = np.empty(STEPS, dtype=float)
    resets = 0
    stop_step = STEPS
    diverged = False

    for step in range(STEPS):
        psi, phi, reset = step_homogeneous(psi, phi, lane, dt, grid_size)
        resets += int(reset)
        energies[step] = abs(psi) ** 2
        phis[step] = phi
        if not (math.isfinite(energies[step]) and math.isfinite(phi)) or abs(psi) > 1e15 or abs(phi) > 1e18:
            stop_step = step + 1
            diverged = True
            energies = energies[:stop_step]
            phis = phis[:stop_step]
            break

    tail_count = max(10, len(energies) // 5)
    tail_e = energies[-tail_count:]
    tail_phi = phis[-tail_count:]
    mean_tail = float(np.mean(tail_e))
    cv_tail = float(np.std(tail_e) / (abs(mean_tail) + 1e-30))
    e_slope = linear_slope(tail_e)
    phi_slope = linear_slope(tail_phi)

    pre_psi = psi
    pre_phi = phi
    pre_energy = abs(pre_psi) ** 2
    psi *= 1.5
    recovery_resets = 0
    for _ in range(RECOVERY_STEPS):
        psi, phi, reset = step_homogeneous(psi, phi, lane, dt, grid_size)
        recovery_resets += int(reset)
        if not (math.isfinite(abs(psi)) and math.isfinite(phi)) or abs(psi) > 1e15 or abs(phi) > 1e18:
            diverged = True
            break
    post_energy = abs(psi) ** 2 if math.isfinite(abs(psi)) else math.inf
    energy_recovery_error = abs(post_energy - pre_energy) / (abs(pre_energy) + 1e-30)
    phi_recovery_error = abs(phi - pre_phi) / (abs(pre_phi) + 1e-30)

    if diverged:
        outcome = "diverged"
    elif resets + recovery_resets > 0:
        outcome = "guard_reset"
    elif mean_tail < 1e-16:
        outcome = "decayed_to_zero"
    elif abs(e_slope) <= max(1e-12, abs(mean_tail) * 1e-8) and cv_tail <= 1e-4:
        outcome = "stationary"
    elif e_slope > 0:
        outcome = "growing"
    else:
        outcome = "decaying"

    return {
        "lane": lane.name,
        "configured_dissipation_rate": lane.configured_dissipation_rate,
        "effective_dissipation_rate": lane.effective_dissipation_rate,
        "dt": dt,
        "grid_size": grid_size,
        "phi0": phi0,
        "steps_completed": stop_step,
        "outcome": outcome,
        "final_abs_psi": float(abs(pre_psi)),
        "final_energy": float(pre_energy),
        "final_phi": float(pre_phi),
        "tail_energy_mean": mean_tail,
        "tail_energy_cv": cv_tail,
        "tail_energy_slope_per_step": e_slope,
        "tail_phi_slope_per_step": phi_slope,
        "resets_before_perturbation": resets,
        "resets_after_perturbation": recovery_resets,
        "recovery_energy_relative_error": float(energy_recovery_error),
        "recovery_phi_relative_error": float(phi_recovery_error),
        "recovery_pass_energy": bool(energy_recovery_error <= 0.05),
        "diverged": diverged,
    }


def run() -> dict[str, Any]:
    rows = [
        summarize_run(lane, dt, size, phi0)
        for lane in LANES
        for dt in DT_VALUES
        for size in GRID_SIZES
        for phi0 in PHI_VALUES
    ]

    baseline = {
        (row["dt"], row["grid_size"], row["phi0"]): row
        for row in rows if row["lane"] == "baseline"
    }
    invariance_differences = []
    for name in ("configured_dissipation_zero", "configured_dissipation_one"):
        lookup = {
            (row["dt"], row["grid_size"], row["phi0"]): row
            for row in rows if row["lane"] == name
        }
        for key, base in baseline.items():
            other = lookup[key]
            invariance_differences.extend([
                abs(base["final_abs_psi"] - other["final_abs_psi"]),
                abs(base["final_phi"] - other["final_phi"]),
                abs(base["recovery_energy_relative_error"] - other["recovery_energy_relative_error"]),
            ])

    by_lane: dict[str, dict[str, Any]] = {}
    for lane in LANES:
        subset = [row for row in rows if row["lane"] == lane.name]
        by_lane[lane.name] = {
            "runs": len(subset),
            "outcome_counts": {
                outcome: sum(row["outcome"] == outcome for row in subset)
                for outcome in sorted({row["outcome"] for row in subset})
            },
            "diverged_runs": sum(row["diverged"] for row in subset),
            "reset_runs": sum((row["resets_before_perturbation"] + row["resets_after_perturbation"]) > 0 for row in subset),
            "energy_recovery_passes": sum(row["recovery_pass_energy"] for row in subset),
            "phi_cap_hits": sum(abs(row["final_phi"] - 1e6) <= 1e-6 for row in subset),
            "max_final_abs_psi": max(row["final_abs_psi"] for row in subset if math.isfinite(row["final_abs_psi"])),
            "max_abs_phi_slope": max(abs(row["tail_phi_slope_per_step"]) for row in subset if math.isfinite(row["tail_phi_slope_per_step"])),
        }

    # Narrow homogeneous classifications.
    no_denom = by_lane["no_interaction_denominator"]
    no_phi_cap_rows = [row for row in rows if row["lane"] == "no_phi_cap" and row["phi0"] >= 1.0]
    baseline_active = [row for row in rows if row["lane"] == "baseline" and row["phi0"] >= 1.0]
    baseline_guard_free = all(row["resets_before_perturbation"] == 0 for row in baseline_active)
    baseline_recovers = all(row["recovery_pass_energy"] for row in baseline_active)
    phi_unbounded_without_cap = all(row["tail_phi_slope_per_step"] > 0 for row in no_phi_cap_rows)

    classification = {
        "configured_dissipation_parameter_inert": max(invariance_differences) <= 1e-15,
        "interaction_denominator_required_for_high_phi_boundedness": no_denom["diverged_runs"] > 0 or no_denom["reset_runs"] > 0,
        "psi_dissipative_equilibrium_in_high_phi_baseline": all(row["outcome"] == "stationary" for row in baseline_active),
        "baseline_high_phi_energy_recovery": baseline_recovers,
        "baseline_high_phi_no_reset": baseline_guard_free,
        "phi_has_no_homogeneous_uncapped_fixed_point": phi_unbounded_without_cap,
        "full_fixed_potential_attractor_shown": False,
        "phase_status": "homogeneous_reduction_completed_localized_phase_pending",
    }

    return {
        "schema": "lineum-b4-saturation-homogeneous-audit/1",
        "source": {
            "path": "lineum_core/math.py",
            "git_blob_sha": SOURCE_BLOB_SHA,
            "reduction": "exact homogeneous deterministic NumPy diffusion path with kappa=1, mu=0, zero gradients, zero diffusion contribution, and quantum noise disabled",
        },
        "protocol": {
            "steps": STEPS,
            "recovery_steps": RECOVERY_STEPS,
            "dt_values": DT_VALUES,
            "grid_sizes": GRID_SIZES,
            "phi0_values": PHI_VALUES,
            "lanes": [asdict(lane) for lane in LANES],
            "initial_abs_psi": 0.01,
        },
        "classification": classification,
        "dissipation_parameter_max_difference": max(invariance_differences),
        "lane_summary": by_lane,
        "rows": rows,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "classification": result["classification"],
        "dissipation_parameter_max_difference": result["dissipation_parameter_max_difference"],
        "lane_summary": result["lane_summary"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
