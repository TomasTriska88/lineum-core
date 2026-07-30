from __future__ import annotations

import hashlib
import json
import os
import sys
from itertools import product
from typing import Any

import numpy as np

REPOSITORY_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPOSITORY_ROOT not in sys.path:
    sys.path.insert(0, REPOSITORY_ROOT)

from lineum_core.math import CoreConfig, ExecutionPolicy, step_core


def clone_state(state: dict[str, Any]) -> dict[str, Any]:
    return {
        key: (
            value.copy()
            if isinstance(value, np.ndarray)
            else dict(value)
            if isinstance(value, dict)
            else value
        )
        for key, value in state.items()
    }


def run_steps(
    state: dict[str, Any], config: CoreConfig, steps: int
) -> dict[str, Any]:
    current = clone_state(state)
    for _ in range(steps):
        current = step_core(current, config)
    return current


def sha256_array(value: np.ndarray) -> str:
    return hashlib.sha256(
        np.ascontiguousarray(value).tobytes(order="C")
    ).hexdigest()


def nrmse(
    reference: np.ndarray,
    candidate: np.ndarray,
    mask: np.ndarray | None = None,
) -> float:
    left = reference if mask is None else reference[mask]
    right = candidate if mask is None else candidate[mask]
    numerator = float(np.sqrt(np.mean(np.abs(left - right) ** 2)))
    denominator = float(np.sqrt(np.mean(np.abs(left) ** 2)))
    return numerator / max(denominator, 1e-15)


def amplitude_correlation(
    reference: np.ndarray,
    candidate: np.ndarray,
    mask: np.ndarray,
) -> float | None:
    left = np.abs(reference[mask]).ravel()
    right = np.abs(candidate[mask]).ravel()
    if (
        left.size < 2
        or float(np.std(left)) == 0.0
        or float(np.std(right)) == 0.0
    ):
        return None
    return float(np.corrcoef(left, right)[0, 1])


def psi_energy(
    state: dict[str, Any], mask: np.ndarray | None = None
) -> float:
    energy = np.abs(state["psi"]) ** 2
    return float(np.sum(energy if mask is None else energy[mask]))


def total_field(state: dict[str, Any], key: str) -> float:
    value = np.asarray(state[key])
    if np.iscomplexobj(value):
        return float(np.sum(np.abs(value) ** 2))
    return float(np.sum(value))


def build_geometry(
    size: int = 32, contrast: float = 0.25
) -> dict[str, np.ndarray]:
    axis = np.linspace(-1.0, 1.0, size)
    y, x = np.meshgrid(axis, axis, indexing="ij")
    radius = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    ring = np.exp(-((radius - 0.45) / 0.10) ** 2)
    structured = 0.55 + contrast * (ring - float(np.mean(ring)))
    uniform = np.full_like(structured, 0.55)
    damage = (ring > 0.20) & (np.abs(theta) <= np.pi / 4.0)
    outside = ~damage
    return {
        "ring": ring,
        "theta": theta,
        "structured": structured,
        "uniform": uniform,
        "damage": damage,
        "outside": outside,
    }


def build_initial(
    geometry: dict[str, np.ndarray], structured: bool
) -> dict[str, np.ndarray]:
    ring = geometry["ring"]
    theta = geometry["theta"]
    return {
        "psi": (0.30 * ring * np.exp(1j * theta)).astype(np.complex128),
        "phi": (0.02 * ring).astype(np.float64),
        "kappa": (
            geometry["structured"] if structured else geometry["uniform"]
        )
        .astype(np.float64)
        .copy(),
        "mu": np.zeros_like(ring, dtype=np.float64),
    }


def apply_damage(
    state: dict[str, Any], damage: np.ndarray
) -> dict[str, Any]:
    damaged = clone_state(state)
    damaged["psi"][damage] = 0.0
    damaged["phi"][damage] = 0.0
    return damaged


def validate_state(state: dict[str, Any]) -> dict[str, Any]:
    arrays = [
        np.asarray(state[key]) for key in ("psi", "phi", "kappa", "mu")
    ]
    finite = all(bool(np.all(np.isfinite(value))) for value in arrays)
    max_abs_psi = float(np.max(np.abs(state["psi"])))
    reset = max_abs_psi == 0.0 and any(
        float(np.max(np.abs(value))) > 0.0 for value in arrays[1:]
    )
    return {
        "finite": finite,
        "max_abs_psi": max_abs_psi,
        "possible_fail_safe_reset": reset,
    }


def lane_name(use_mu: bool, structured: bool) -> str:
    return {
        (False, False): "YS00",
        (True, False): "Y1S0",
        (False, True): "Y0S1",
        (True, True): "Y1S1",
    }[(use_mu, structured)]


def run_lane(
    *,
    formation_steps: int,
    mu_eta: float,
    contrast: float,
    use_mu: bool,
    structured: bool,
) -> dict[str, Any]:
    geometry = build_geometry(32, contrast)
    config = CoreConfig(
        disable_quantum_noise=True,
        noise_strength=0.0,
        use_mode_coupling=True,
        use_mu=use_mu,
        mu_eta=mu_eta,
        mu_rho=0.0001,
        mu_peak_cutoff_ratio=0.1,
    )
    ExecutionPolicy.init_core_determinism(
        seed=314159, device_mode="numpy"
    )
    formed = run_steps(
        build_initial(geometry, structured), config, formation_steps
    )
    reference = clone_state(formed)
    damaged = apply_damage(formed, geometry["damage"])

    immediate_damage_energy = psi_energy(damaged, geometry["damage"])
    pre_damage_reference_energy = psi_energy(reference, geometry["damage"])

    reference_repaired = run_steps(reference, config, 40)
    damaged_repaired = run_steps(damaged, config, 40)

    reference_after_energy = psi_energy(
        reference_repaired, geometry["damage"]
    )
    damaged_after_energy = psi_energy(
        damaged_repaired, geometry["damage"]
    )
    denominator = reference_after_energy - immediate_damage_energy
    recovery_fraction = (
        (damaged_after_energy - immediate_damage_energy) / denominator
        if abs(denominator) > 1e-15
        else None
    )

    removal_reference = clone_state(reference_repaired)
    removal_damaged = clone_state(damaged_repaired)
    removal_reference["kappa"] = geometry["uniform"].copy()
    removal_damaged["kappa"] = geometry["uniform"].copy()
    reference_removed = run_steps(removal_reference, config, 40)
    damaged_removed = run_steps(removal_damaged, config, 40)

    repaired_damage_energy = damaged_after_energy
    removed_damage_energy = psi_energy(
        damaged_removed, geometry["damage"]
    )
    removal_retention = removed_damage_energy / max(
        repaired_damage_energy, 1e-15
    )

    state_validation = validate_state(damaged_repaired)
    state_validation_removed = validate_state(damaged_removed)

    return {
        "lane": lane_name(use_mu, structured),
        "formation_steps": formation_steps,
        "mu_eta": mu_eta,
        "kappa_contrast": contrast,
        "kappa_mean_structured": float(
            np.mean(geometry["structured"])
        ),
        "kappa_mean_uniform": float(np.mean(geometry["uniform"])),
        "kappa_min": float(np.min(geometry["structured"])),
        "kappa_max": float(np.max(geometry["structured"])),
        "damage_cells": int(np.count_nonzero(geometry["damage"])),
        "pre_damage_reference_energy": pre_damage_reference_energy,
        "immediate_damage_energy": immediate_damage_energy,
        "reference_after_energy": reference_after_energy,
        "damaged_after_energy": damaged_after_energy,
        "recovery_fraction": recovery_fraction,
        "damage_amplitude_correlation": amplitude_correlation(
            reference_repaired["psi"],
            damaged_repaired["psi"],
            geometry["damage"],
        ),
        "outside_nrmse": nrmse(
            reference_repaired["psi"],
            damaged_repaired["psi"],
            geometry["outside"],
        ),
        "global_nrmse": nrmse(
            reference_repaired["psi"], damaged_repaired["psi"]
        ),
        "damaged_total_psi_energy": psi_energy(damaged_repaired),
        "reference_total_psi_energy": psi_energy(reference_repaired),
        "energy_ratio_to_twin": psi_energy(damaged_repaired)
        / max(psi_energy(reference_repaired), 1e-15),
        "totals_after_repair": {
            key: total_field(damaged_repaired, key)
            for key in ("psi", "phi", "mu", "kappa")
        },
        "repair_validation": state_validation,
        "removal_damage_energy": removed_damage_energy,
        "removal_reference_damage_energy": psi_energy(
            reference_removed, geometry["damage"]
        ),
        "removal_retention_vs_repaired": removal_retention,
        "removal_nrmse_to_twin": nrmse(
            reference_removed["psi"], damaged_removed["psi"]
        ),
        "removal_validation": state_validation_removed,
        "hashes_after_repair": {
            key: sha256_array(damaged_repaired[key])
            for key in ("psi", "phi", "mu")
        },
        "hashes_after_removal": {
            key: sha256_array(damaged_removed[key])
            for key in ("psi", "phi", "mu")
        },
    }


def toy_metric_check() -> dict[str, float]:
    ref_after = 10.0
    damaged_immediate = 2.0
    improved = 6.0
    worse = 1.0
    return {
        "half_recovery": (improved - damaged_immediate)
        / (ref_after - damaged_immediate),
        "negative_recovery": (worse - damaged_immediate)
        / (ref_after - damaged_immediate),
    }


def run_matrix() -> dict[str, Any]:
    toy = toy_metric_check()
    assert toy == {"half_recovery": 0.5, "negative_recovery": -0.125}
    results: list[dict[str, Any]] = []
    for formation_steps, mu_eta, contrast in product(
        (20, 60), (0.005, 0.020), (0.25, 0.40)
    ):
        geometry = build_geometry(32, contrast)
        assert abs(float(np.mean(geometry["structured"])) - 0.55) < 1e-14
        assert float(np.min(geometry["structured"])) > 0.0
        assert float(np.max(geometry["structured"])) <= 1.0
        cell_lanes = []
        for use_mu, structured in (
            (False, False),
            (True, False),
            (False, True),
            (True, True),
        ):
            cell_lanes.append(
                run_lane(
                    formation_steps=formation_steps,
                    mu_eta=mu_eta,
                    contrast=contrast,
                    use_mu=use_mu,
                    structured=structured,
                )
            )
        results.append(
            {
                "cell": {
                    "formation_steps": formation_steps,
                    "mu_eta": mu_eta,
                    "kappa_contrast": contrast,
                },
                "lanes": cell_lanes,
            }
        )

    supportive_cells = []
    for cell in results:
        lanes = {lane["lane"]: lane for lane in cell["lanes"]}
        combined = lanes["Y1S1"]
        competitors = [
            lanes[name]["recovery_fraction"]
            for name in ("Y1S0", "Y0S1", "YS00")
        ]
        best_single_outside = min(
            lanes[name]["outside_nrmse"]
            for name in ("Y1S0", "Y0S1")
        )
        valid = (
            combined["recovery_fraction"] is not None
            and all(value is not None for value in competitors)
            and combined["recovery_fraction"]
            >= max(competitors) + 0.10
            and combined["outside_nrmse"] <= best_single_outside + 0.10
            and combined["energy_ratio_to_twin"] <= 1.25
            and combined["repair_validation"]["max_abs_psi"] < 10.0
            and combined["repair_validation"]["finite"]
            and not combined["repair_validation"][
                "possible_fail_safe_reset"
            ]
        )
        if valid:
            supportive_cells.append(cell["cell"])

    return {
        "schema": "lineum-core-active-mu-kappa-repair-feasibility-v1",
        "environment": {
            "python": "3.13.5",
            "numpy": np.__version__,
            "backend": "numpy-isolated",
        },
        "toy_metric_check": toy,
        "cells": results,
        "supportive_cells": supportive_cells,
        "combined_supported_in_any_cell": bool(supportive_cells),
    }


if __name__ == "__main__":
    first = run_matrix()
    second = run_matrix()
    first_json = json.dumps(
        first, sort_keys=True, separators=(",", ":"), allow_nan=False
    )
    second_json = json.dumps(
        second, sort_keys=True, separators=(",", ":"), allow_nan=False
    )
    assert first_json == second_json
    print(json.dumps(first, indent=2, sort_keys=True, allow_nan=False))
    print(
        "RESULT_SHA256",
        hashlib.sha256(first_json.encode("utf-8")).hexdigest(),
    )
