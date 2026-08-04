#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import platform
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np

SOURCE_BLOB_SHA = "bb877021810691223a0eb960a45493a2e351112a"
GRID_SIZE = 32
DT = 1.0
STEPS = 5000
RECOVERY_STEPS = 1000
SIGMA = 3.0
PHI0_VALUES = (0.0, 1.0)
STENCILS = ("LAP4", "LAP8")
PSI_CAP = 1e6
PHI_CAP = 1e6


@dataclass(frozen=True)
class Lane:
    name: str
    effective_dissipation_rate: float = 0.005
    use_tanh: bool = True
    use_interaction_denominator: bool = True
    use_mode_coupling: bool = True
    use_phi_cap: bool = True
    use_psi_guard: bool = True


LANES = (
    Lane("baseline"),
    Lane("no_hard_guards", use_phi_cap=False, use_psi_guard=False),
    Lane("no_linear_dissipation", effective_dissipation_rate=0.0),
    Lane("no_explicit_tanh", use_tanh=False),
    Lane("no_interaction_denominator", use_interaction_denominator=False),
    Lane("no_mode_coupling", use_mode_coupling=False),
    Lane("no_phi_cap", use_phi_cap=False),
)


def geometry() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    center = (GRID_SIZE - 1) / 2.0
    y, x = np.indices((GRID_SIZE, GRID_SIZE), dtype=float)
    dx = x - center
    dy = y - center
    radius = np.sqrt(dx * dx + dy * dy)
    theta = np.arctan2(dy, dx)
    return x, y, radius, theta


X, Y, RADIUS, THETA = geometry()
RADIAL_BINS = np.floor(RADIUS).astype(int)
RADIAL_BIN_COUNT = int(RADIAL_BINS.max()) + 1
GAUSSIAN = np.exp(-(RADIUS * RADIUS) / (2.0 * SIGMA * SIGMA)).astype(np.complex128)


def diffuse(
    field: np.ndarray,
    kappa: np.ndarray,
    rate: float,
    stencil: str,
) -> np.ndarray:
    k_up = np.roll(kappa, 1, axis=1)
    k_down = np.roll(kappa, -1, axis=1)
    k_left = np.roll(kappa, 1, axis=2)
    k_right = np.roll(kappa, -1, axis=2)
    f_up = np.roll(field, 1, axis=1)
    f_down = np.roll(field, -1, axis=1)
    f_left = np.roll(field, 1, axis=2)
    f_right = np.roll(field, -1, axis=2)

    if stencil == "LAP8":
        k_ul = np.roll(k_up, 1, axis=2)
        k_ur = np.roll(k_up, -1, axis=2)
        k_dl = np.roll(k_down, 1, axis=2)
        k_dr = np.roll(k_down, -1, axis=2)
        f_ul = np.roll(f_up, 1, axis=2)
        f_ur = np.roll(f_up, -1, axis=2)
        f_dl = np.roll(f_down, 1, axis=2)
        f_dr = np.roll(f_down, -1, axis=2)
        neighbour_sum = (
            f_up * k_up
            + f_down * k_down
            + f_left * k_left
            + f_right * k_right
            + 0.25 * (
                f_ul * k_ul
                + f_ur * k_ur
                + f_dl * k_dl
                + f_dr * k_dr
            )
        )
        active_neighbours = (
            k_up
            + k_down
            + k_left
            + k_right
            + 0.25 * (k_ul + k_ur + k_dl + k_dr)
        )
    else:
        neighbour_sum = (
            f_up * k_up
            + f_down * k_down
            + f_left * k_left
            + f_right * k_right
        )
        active_neighbours = k_up + k_down + k_left + k_right

    return rate * (neighbour_sum - active_neighbours * field)


def slope_rows(values: np.ndarray) -> np.ndarray:
    x = np.arange(values.shape[0], dtype=float)
    x -= x.mean()
    denominator = float(np.dot(x, x))
    centered = values - values.mean(axis=0, keepdims=True)
    return np.dot(x, centered) / denominator


def radial_profile(values: np.ndarray) -> np.ndarray:
    sums = np.bincount(
        RADIAL_BINS.ravel(),
        weights=values.ravel(),
        minlength=RADIAL_BIN_COUNT,
    )
    counts = np.bincount(RADIAL_BINS.ravel(), minlength=RADIAL_BIN_COUNT)
    return sums / np.maximum(counts, 1)


def spatial_metrics(psi: np.ndarray, phi: np.ndarray) -> dict[str, Any]:
    energy = np.abs(psi) ** 2
    total = float(energy.sum())
    if total > 0.0 and math.isfinite(total):
        center = (GRID_SIZE - 1) / 2.0
        center_x = float((energy * X).sum() / total)
        center_y = float((energy * Y).sum() / total)
        displacement = float(math.hypot(center_x - center, center_y - center))
        order = np.argsort(RADIUS.ravel())
        cumulative = np.cumsum(energy.ravel()[order])
        index = int(np.searchsorted(cumulative, 0.5 * total))
        half_radius = float(RADIUS.ravel()[order[min(index, order.size - 1)]])
        anisotropy = float(
            abs(np.sum(energy * np.exp(4j * THETA))) / total
        )
    else:
        displacement = math.inf
        half_radius = math.inf
        anisotropy = math.inf

    return {
        "total_energy": total,
        "mean_energy": float(energy.mean()),
        "max_abs_psi": float(np.abs(psi).max()),
        "phi_min": float(np.nanmin(phi)),
        "phi_mean": float(np.nanmean(phi)),
        "phi_max": float(np.nanmax(phi)),
        "energy_fraction_within_radius": {
            str(radius): (
                float(energy[RADIUS <= radius].sum() / total) if total > 0.0 else 0.0
            )
            for radius in (3, 6, 10)
        },
        "half_energy_radius": half_radius,
        "center_displacement": displacement,
        "anisotropy4": anisotropy,
        "energy_radial_profile": radial_profile(energy).tolist(),
        "phi_radial_profile": radial_profile(phi).tolist(),
    }


def relative_l2(reference: list[float], candidate: list[float]) -> float:
    a = np.asarray(reference, dtype=float)
    b = np.asarray(candidate, dtype=float)
    count = min(a.size, b.size)
    return float(
        np.linalg.norm(b[:count] - a[:count])
        / (np.linalg.norm(a[:count]) + 1e-30)
    )


def run_stencil(stencil: str) -> list[dict[str, Any]]:
    specs = [(lane, phi0) for lane in LANES for phi0 in PHI0_VALUES]
    batch_size = len(specs)
    psi = np.stack([GAUSSIAN.copy() for _ in specs])
    phi = np.stack(
        [np.full((GRID_SIZE, GRID_SIZE), phi0, dtype=float) for _, phi0 in specs]
    )
    kappa = np.ones((batch_size, GRID_SIZE, GRID_SIZE))
    mu = np.zeros_like(kappa)

    use_guard = np.array([lane.use_psi_guard for lane, _ in specs])[:, None, None]
    use_phi_cap = np.array([lane.use_phi_cap for lane, _ in specs])[:, None, None]
    use_tanh = np.array([lane.use_tanh for lane, _ in specs])[:, None, None]
    use_denominator = np.array(
        [lane.use_interaction_denominator for lane, _ in specs]
    )[:, None, None]
    use_mode_coupling = np.array(
        [lane.use_mode_coupling for lane, _ in specs]
    )[:, None, None]
    dissipation = np.array(
        [lane.effective_dissipation_rate for lane, _ in specs]
    )[:, None, None]

    initial = [spatial_metrics(psi[i], phi[i]) for i in range(batch_size)]
    resets = np.zeros(batch_size, dtype=int)
    psi_cap_hits = np.zeros(batch_size, dtype=int)
    phi_cap_hits = np.zeros(batch_size, dtype=int)
    nonfinite = np.zeros(batch_size, dtype=bool)
    steps_completed = np.full(batch_size, STEPS, dtype=int)
    active = np.ones(batch_size, dtype=bool)
    energies = np.empty((STEPS, batch_size))
    phi_means = np.empty((STEPS, batch_size))

    def one_step(
        current_psi: np.ndarray,
        current_phi: np.ndarray,
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        amplitude = np.abs(current_psi)
        guarded_amplitude = np.where(
            use_guard,
            np.minimum(amplitude, PSI_CAP),
            amplitude,
        )
        gradient_y, gradient_x = np.gradient(guarded_amplitude, axis=(1, 2))
        gradient_x = np.where(
            use_guard,
            np.clip(gradient_x, -PSI_CAP, PSI_CAP),
            gradient_x,
        )
        gradient_y = np.where(
            use_guard,
            np.clip(gradient_y, -PSI_CAP, PSI_CAP),
            gradient_y,
        )

        drift_multiplier = 1.0 + mu
        clipped_phi = np.clip(current_phi, 0.0, 10.0)
        raw_interaction = 0.04 * clipped_phi * kappa * drift_multiplier
        interaction_factor = np.where(
            use_tanh,
            0.1 * np.tanh(raw_interaction / 0.1),
            raw_interaction,
        )
        interaction = interaction_factor * current_psi
        interaction = np.where(
            use_denominator,
            interaction / (1.0 + np.abs(interaction) / 10.0),
            interaction,
        )

        gradient_phi_y, gradient_phi_x = np.gradient(current_phi, axis=(1, 2))
        flow = (
            -0.004
            * (gradient_phi_x + 1j * gradient_phi_y)
            * kappa
            * drift_multiplier
        )
        flow = flow / (1.0 + np.abs(flow) / 10.0)

        current_psi = current_psi + flow * DT
        magnitude = np.abs(current_psi)
        cap_mask = (magnitude > PSI_CAP) & use_guard
        cap_rows = cap_mask.reshape(batch_size, -1).any(axis=1)
        scale = np.ones_like(magnitude)
        scale[cap_mask] = PSI_CAP / (magnitude[cap_mask] + 1e-30)
        current_psi = current_psi * scale

        current_psi = current_psi + interaction * DT
        current_psi = current_psi - dissipation * current_psi * DT
        current_psi = (
            current_psi
            + diffuse(current_psi, kappa, 0.05, stencil) * kappa * DT
        )

        energy = np.abs(current_psi) ** 2
        transferred = 0.001 * energy * kappa * DT
        phi_mode = current_phi + transferred
        new_magnitude = np.sqrt(np.maximum(energy - transferred, 0.0))
        psi_mode = current_psi / (np.sqrt(energy) + 1e-12) * new_magnitude
        dynamic_reaction = 0.0007 * (128.0 / GRID_SIZE) ** 2
        phi_fallback = current_phi + dynamic_reaction * (energy - current_phi) * DT
        current_phi = np.where(use_mode_coupling, phi_mode, phi_fallback)
        current_psi = np.where(use_mode_coupling, psi_mode, current_psi)

        current_phi = current_phi + 0.05 * diffuse(
            current_phi,
            kappa,
            0.05,
            stencil,
        )
        phi_mask = ((current_phi < 0.0) | (current_phi > PHI_CAP)) & use_phi_cap
        phi_cap_rows = phi_mask.reshape(batch_size, -1).any(axis=1)
        current_phi = np.where(
            use_phi_cap,
            np.clip(current_phi, 0.0, PHI_CAP),
            current_phi,
        )

        bad_psi = ~np.isfinite(current_psi).reshape(batch_size, -1).all(axis=1)
        max_psi = np.nanmax(np.abs(current_psi).reshape(batch_size, -1), axis=1)
        reset_rows = use_guard[:, 0, 0] & (
            bad_psi | (max_psi >= PSI_CAP * 0.99)
        )
        current_psi[reset_rows] = 0.0
        return current_psi, current_phi, reset_rows, cap_rows, phi_cap_rows

    with np.errstate(all="ignore"):
        for step_index in range(STEPS):
            psi, phi, reset_rows, cap_rows, phi_cap_rows = one_step(psi, phi)
            resets += reset_rows
            psi_cap_hits += cap_rows
            phi_cap_hits += phi_cap_rows
            energies[step_index] = np.nanmean(np.abs(psi) ** 2, axis=(1, 2))
            phi_means[step_index] = np.nanmean(phi, axis=(1, 2))
            huge = (
                np.nanmax(np.abs(psi).reshape(batch_size, -1), axis=1) > 1e15
            ) | (
                np.nanmax(np.abs(phi).reshape(batch_size, -1), axis=1) > 1e18
            )
            bad = (
                ~np.isfinite(psi).reshape(batch_size, -1).all(axis=1)
                | ~np.isfinite(phi).reshape(batch_size, -1).all(axis=1)
                | huge
            )
            newly_bad = bad & active
            steps_completed[newly_bad] = step_index + 1
            nonfinite |= bad
            active &= ~bad
            if newly_bad.any():
                psi[newly_bad] = 0.0
                phi[newly_bad] = 0.0

    pre = [spatial_metrics(psi[i], phi[i]) for i in range(batch_size)]
    tail_count = max(10, STEPS // 5)
    energy_slopes = slope_rows(energies[-tail_count:])
    phi_slopes = slope_rows(phi_means[-tail_count:])
    energy_means = energies[-tail_count:].mean(axis=0)
    phi_tail_means = phi_means[-tail_count:].mean(axis=0)
    energy_cv = energies[-tail_count:].std(axis=0) / (
        np.abs(energy_means) + 1e-30
    )
    phi_cv = phi_means[-tail_count:].std(axis=0) / (
        np.abs(phi_tail_means) + 1e-30
    )

    psi[:, RADIUS <= 2.0] *= 1.5
    psi[:, (RADIUS >= 3.0) & (RADIUS <= 5.0)] *= 0.5
    recovery_resets = np.zeros(batch_size, dtype=int)
    recovery_psi_cap_hits = np.zeros(batch_size, dtype=int)
    recovery_phi_cap_hits = np.zeros(batch_size, dtype=int)

    with np.errstate(all="ignore"):
        for _ in range(RECOVERY_STEPS):
            psi, phi, reset_rows, cap_rows, phi_cap_rows = one_step(psi, phi)
            recovery_resets += reset_rows
            recovery_psi_cap_hits += cap_rows
            recovery_phi_cap_hits += phi_cap_rows
            bad = (
                ~np.isfinite(psi).reshape(batch_size, -1).all(axis=1)
                | ~np.isfinite(phi).reshape(batch_size, -1).all(axis=1)
                | (
                    np.nanmax(np.abs(psi).reshape(batch_size, -1), axis=1)
                    > 1e15
                )
                | (
                    np.nanmax(np.abs(phi).reshape(batch_size, -1), axis=1)
                    > 1e18
                )
            )
            nonfinite |= bad
            active &= ~bad
            if bad.any():
                psi[bad] = 0.0
                phi[bad] = 0.0

    post = [spatial_metrics(psi[i], phi[i]) for i in range(batch_size)]
    rows: list[dict[str, Any]] = []
    for index, (lane, phi0) in enumerate(specs):
        energy_error = abs(
            post[index]["total_energy"] - pre[index]["total_energy"]
        ) / (abs(pre[index]["total_energy"]) + 1e-30)
        energy_profile_error = relative_l2(
            pre[index]["energy_radial_profile"],
            post[index]["energy_radial_profile"],
        )
        phi_profile_error = relative_l2(
            pre[index]["phi_radial_profile"],
            post[index]["phi_radial_profile"],
        )
        half_radius_error = abs(
            post[index]["half_energy_radius"]
            - pre[index]["half_energy_radius"]
        )
        nontrivial = bool(
            pre[index]["total_energy"]
            >= max(1e-12, initial[index]["total_energy"] * 0.01)
            and pre[index]["energy_fraction_within_radius"]["6"] >= 0.5
        )
        psi_recovery = bool(
            nontrivial
            and not nonfinite[index]
            and resets[index] + recovery_resets[index] == 0
            and energy_error <= 0.05
            and energy_profile_error <= 0.10
            and half_radius_error <= 1.0
            and post[index]["center_displacement"] <= 0.5
        )
        phi_stationary_threshold = max(
            1e-10,
            1e-8 * abs(phi_tail_means[index]),
        )
        full_recovery = bool(
            psi_recovery
            and phi_cap_hits[index] + recovery_phi_cap_hits[index] == 0
            and phi_profile_error <= 0.10
            and phi_slopes[index] <= phi_stationary_threshold
        )
        rows.append(
            {
                "lane": lane.name,
                "lane_settings": asdict(lane),
                "stencil": stencil,
                "phi0": phi0,
                "steps_completed": int(steps_completed[index]),
                "initial": initial[index],
                "pre_perturbation": pre[index],
                "post_recovery": post[index],
                "tail": {
                    "energy_mean": float(energy_means[index]),
                    "energy_slope_per_step": float(energy_slopes[index]),
                    "energy_cv": float(energy_cv[index]),
                    "phi_mean": float(phi_tail_means[index]),
                    "phi_slope_per_step": float(phi_slopes[index]),
                    "phi_cv": float(phi_cv[index]),
                    "phi_stationary_threshold": float(phi_stationary_threshold),
                },
                "events": {
                    "resets_before": int(resets[index]),
                    "resets_after": int(recovery_resets[index]),
                    "psi_cap_hits_before": int(psi_cap_hits[index]),
                    "psi_cap_hits_after": int(recovery_psi_cap_hits[index]),
                    "phi_cap_hits_before": int(phi_cap_hits[index]),
                    "phi_cap_hits_after": int(recovery_phi_cap_hits[index]),
                    "nonfinite_or_failfast": bool(nonfinite[index]),
                },
                "recovery": {
                    "total_energy_relative_error": float(energy_error),
                    "energy_radial_profile_l2_error": float(
                        energy_profile_error
                    ),
                    "phi_radial_profile_l2_error": float(phi_profile_error),
                    "half_energy_radius_absolute_error": float(
                        half_radius_error
                    ),
                    "center_displacement_after": float(
                        post[index]["center_displacement"]
                    ),
                    "nontrivial_localized_pre_state": nontrivial,
                    "localized_psi_recovery": psi_recovery,
                    "localized_full_state_recovery": full_recovery,
                },
            }
        )
    return rows


def run() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for stencil in STENCILS:
        rows.extend(run_stencil(stencil))

    pairs = []
    for lane in LANES:
        for phi0 in PHI0_VALUES:
            lap4 = next(
                row
                for row in rows
                if row["lane"] == lane.name
                and row["phi0"] == phi0
                and row["stencil"] == "LAP4"
            )
            lap8 = next(
                row
                for row in rows
                if row["lane"] == lane.name
                and row["phi0"] == phi0
                and row["stencil"] == "LAP8"
            )
            pairs.append(
                {
                    "lane": lane.name,
                    "phi0": phi0,
                    "lap4_psi_recovery": lap4["recovery"][
                        "localized_psi_recovery"
                    ],
                    "lap8_psi_recovery": lap8["recovery"][
                        "localized_psi_recovery"
                    ],
                    "lap4_full_recovery": lap4["recovery"][
                        "localized_full_state_recovery"
                    ],
                    "lap8_full_recovery": lap8["recovery"][
                        "localized_full_state_recovery"
                    ],
                    "lap4_anisotropy": lap4["pre_perturbation"][
                        "anisotropy4"
                    ],
                    "lap8_anisotropy": lap8["pre_perturbation"][
                        "anisotropy4"
                    ],
                    "lap4_radial_error": lap4["recovery"][
                        "energy_radial_profile_l2_error"
                    ],
                    "lap8_radial_error": lap8["recovery"][
                        "energy_radial_profile_l2_error"
                    ],
                }
            )

    baseline = [row for row in rows if row["lane"] == "baseline"]
    uncapped_phi = [row for row in rows if row["lane"] == "no_phi_cap"]
    lap8_specific = any(
        pair["lap8_full_recovery"]
        and not pair["lap4_full_recovery"]
        and pair["lap8_anisotropy"] < pair["lap4_anisotropy"]
        for pair in pairs
    )
    same_classification = all(
        pair["lap4_psi_recovery"] == pair["lap8_psi_recovery"]
        and pair["lap4_full_recovery"] == pair["lap8_full_recovery"]
        for pair in pairs
    )
    material_advantage = any(
        abs(pair["lap4_radial_error"] - pair["lap8_radial_error"]) > 0.10
        or abs(pair["lap4_anisotropy"] - pair["lap8_anisotropy"]) > 0.10
        for pair in pairs
        if math.isfinite(pair["lap4_radial_error"])
        and math.isfinite(pair["lap8_radial_error"])
    )
    phi_resolved = all(
        not row["events"]["nonfinite_or_failfast"]
        and row["tail"]["phi_slope_per_step"]
        <= row["tail"]["phi_stationary_threshold"]
        and row["recovery"]["phi_radial_profile_l2_error"] <= 0.10
        for row in uncapped_phi
    )

    classification = {
        "phase": "localized_l1_screen_completed",
        "baseline_nontrivial_localized_states": sum(
            row["recovery"]["nontrivial_localized_pre_state"]
            for row in baseline
        ),
        "baseline_localized_psi_recoveries": sum(
            row["recovery"]["localized_psi_recovery"] for row in baseline
        ),
        "baseline_localized_full_state_recoveries": sum(
            row["recovery"]["localized_full_state_recovery"]
            for row in baseline
        ),
        "spatial_transport_resolves_phi": bool(phi_resolved),
        "lap8_specific_stabilization": bool(lap8_specific),
        "stencil_not_decisive_in_l1": bool(
            same_classification and not material_advantage
        ),
        "development_programme_terminal_failure": False,
    }

    lane_summary: dict[str, Any] = {}
    for lane in LANES:
        subset = [row for row in rows if row["lane"] == lane.name]
        lane_summary[lane.name] = {
            "runs": len(subset),
            "nontrivial_states": sum(
                row["recovery"]["nontrivial_localized_pre_state"]
                for row in subset
            ),
            "psi_recoveries": sum(
                row["recovery"]["localized_psi_recovery"] for row in subset
            ),
            "full_recoveries": sum(
                row["recovery"]["localized_full_state_recovery"]
                for row in subset
            ),
            "reset_runs": sum(
                row["events"]["resets_before"]
                + row["events"]["resets_after"]
                > 0
                for row in subset
            ),
            "nonfinite_runs": sum(
                row["events"]["nonfinite_or_failfast"] for row in subset
            ),
            "phi_cap_hit_runs": sum(
                row["events"]["phi_cap_hits_before"]
                + row["events"]["phi_cap_hits_after"]
                > 0
                for row in subset
            ),
            "max_pre_abs_psi": max(
                row["pre_perturbation"]["max_abs_psi"] for row in subset
            ),
            "max_pre_phi": max(
                row["pre_perturbation"]["phi_max"] for row in subset
            ),
        }

    return {
        "schema": "lineum-b4-saturation-localized-l1/1",
        "source": {
            "path": "lineum_core/math.py",
            "git_blob_sha": SOURCE_BLOB_SHA,
            "reference": (
                "frozen batched research implementation of the deterministic "
                "NumPy diffusion path"
            ),
        },
        "protocol": {
            "grid_size": GRID_SIZE,
            "dt": DT,
            "steps": STEPS,
            "recovery_steps": RECOVERY_STEPS,
            "sigma_cells": SIGMA,
            "phi0_values": PHI0_VALUES,
            "stencils": STENCILS,
            "lanes": [asdict(lane) for lane in LANES],
            "noise_disabled": True,
            "boundary": "periodic through numpy.roll",
            "perturbation": (
                "multiply radius<=2 by 1.5 and radius 3..5 by 0.5"
            ),
            "nontrivial_diagnostic": (
                "pre energy >=1% initial and >=50% within radius 6; "
                "fixed before execution"
            ),
        },
        "classification": classification,
        "lane_summary": lane_summary,
        "stencil_pairs": pairs,
        "rows": rows,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "execution_note": (
            "Initial per-run implementation timed out without producing a result. "
            "This batched implementation preserves equations and protocol while "
            "vectorizing independent rows."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "classification": result["classification"],
                "lane_summary": result["lane_summary"],
                "environment": result["environment"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
