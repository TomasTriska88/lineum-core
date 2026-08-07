#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import platform
import sys
from pathlib import Path
from typing import Any

import numpy as np

SCHEMA = "lineum-b4-q2-spatial-accounting-stage-a/1"
STAGE_A_ID = "Q2-SA1-A"
CLOSURE_RTOL = 1e-10
POSITIVE_RTOL = 1e-12
NEAR_RETURN_FACTOR = 2.0
STENCILS = ("LAP4", "LAP8")
LANE_NAMES = ("L0", "S1", "S2", "S3")
TRACKED_KEYS = ("epsi_global", "epsi_local", "phi_global", "phi_local")
SOURCE_STAGES = ("feedback", "phi_gradient_flow")


def _load_accounting():
    here = Path(__file__).resolve().parent
    path = here / "lineum_b4_q2_spatial_accounting.py"
    spec = importlib.util.spec_from_file_location("lineum_b4_sa_primary", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load committed B4 spatial-accounting instrumentation")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def closure_ratio(residual: float, total_change: float, absolute_stage_sum: float) -> float:
    scale = max(1.0, abs(total_change), abs(absolute_stage_sum))
    return abs(residual) / scale


def classify_mechanism(
    residual_ratio: float,
    transport_positive: float,
    transport_global_signed: float,
    unpaired_positive: float,
    other_positive: float,
    pre_local_epsi: float,
    pre_global_epsi: float,
) -> dict[str, Any]:
    residual_ok = bool(residual_ratio <= CLOSURE_RTOL)
    global_transport_limit = CLOSURE_RTOL * max(1.0, abs(pre_global_epsi))
    transport_valid = bool(transport_global_signed <= global_transport_limit)
    transport_credit = float(transport_positive if transport_valid else 0.0)
    positive_total = float(transport_positive + unpaired_positive + other_positive)
    positive_floor = POSITIVE_RTOL * max(1.0, abs(pre_local_epsi))
    material_positive = bool(positive_total > positive_floor)

    if not residual_ok:
        label = "unresolved_residual"
    elif material_positive and transport_credit > unpaired_positive:
        label = "transport_accounted"
    elif material_positive and unpaired_positive >= transport_credit:
        label = "unpaired_source_dominated"
    else:
        label = "sink_or_dispersion_dominated"

    return {
        "label": label,
        "residual_ok": residual_ok,
        "transport_global_noncreating": transport_valid,
        "transport_credit": transport_credit,
        "positive_total": positive_total,
        "positive_floor": positive_floor,
    }


def near_return(metrics: dict[str, Any]) -> bool:
    return bool(
        metrics["finite"]
        and metrics["reset_free"]
        and metrics["psi_cap_free"]
        and metrics["phi_cap_free"]
        and metrics["total_energy_relative_error"] <= 0.05 * NEAR_RETURN_FACTOR
        and metrics["energy_radial_profile_l2_error"] <= 0.10 * NEAR_RETURN_FACTOR
        and metrics["half_energy_radius_absolute_error"] <= 1.0 * NEAR_RETURN_FACTOR
        and metrics["center_displacement_after"] <= 0.5 * NEAR_RETURN_FACTOR
        and metrics["phi_radial_profile_l2_error"] <= 0.10 * NEAR_RETURN_FACTOR
    )


def stage_b_candidates(rows: list[dict[str, Any]]) -> list[str]:
    candidates: list[str] = []
    for lane in LANE_NAMES:
        by_stencil = {
            row["stencil"]: row
            for row in rows
            if row["lane"] == lane and row["stencil"] in STENCILS
        }
        if set(by_stencil) != set(STENCILS):
            continue
        if all(
            by_stencil[stencil]["mechanism"]["label"] == "transport_accounted"
            and by_stencil[stencil]["near_return"]
            for stencil in STENCILS
        ):
            candidates.append(lane)
    return candidates


def _relative_l2(reference: list[float], candidate: list[float]) -> float:
    a = np.asarray(reference, dtype=float)
    b = np.asarray(candidate, dtype=float)
    n = min(a.size, b.size)
    return float(np.linalg.norm(b[:n] - a[:n]) / (np.linalg.norm(a[:n]) + 1e-30))


def _json_ready(value: Any) -> Any:
    if isinstance(value, np.generic):
        return _json_ready(value.item())
    if isinstance(value, np.ndarray):
        return _json_ready(value.tolist())
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    if isinstance(value, float) and not math.isfinite(value):
        if math.isnan(value):
            return "NaN"
        return "Infinity" if value > 0 else "-Infinity"
    if isinstance(value, dict):
        return {key: _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    return value


def _run_stencil(sa, stencil: str) -> list[dict[str, Any]]:
    l1 = sa.l1
    lanes = sa.SPATIAL_LANES
    if tuple(lane.name for lane in lanes) != LANE_NAMES:
        raise RuntimeError("Committed Stage A lane map changed")
    count = len(lanes)
    psi = np.stack([l1.GAUSSIAN.copy() for _ in lanes])
    phi = np.ones((count, l1.GRID_SIZE, l1.GRID_SIZE), dtype=float)
    kappa = np.ones_like(phi)
    mu = np.zeros_like(phi)
    lane_arrays = sa._lane_arrays(count)
    spatial_arrays = sa._spatial_arrays(lanes)

    reset_hits = np.zeros(count, dtype=int)
    psi_cap_hits = np.zeros(count, dtype=int)
    phi_cap_hits = np.zeros(count, dtype=int)
    tail_phi = np.empty((l1.STEPS, count), dtype=float)

    with np.errstate(all="ignore"):
        for step in range(l1.STEPS):
            output = sa.instrumented_step(
                psi, phi, kappa, mu, stencil, lane_arrays, spatial_arrays, region=None
            )
            psi, phi = output[:2]
            reset_hits += output[2]
            psi_cap_hits += output[3]
            phi_cap_hits += output[4]
            tail_phi[step] = np.mean(phi, axis=(1, 2))

    pre = [l1.spatial_metrics(psi[i], phi[i]) for i in range(count)]
    tail_count = max(10, l1.STEPS // 5)
    phi_slopes = l1.slope_rows(tail_phi[-tail_count:])
    phi_tail_means = tail_phi[-tail_count:].mean(axis=0)

    region = np.zeros((count, l1.GRID_SIZE, l1.GRID_SIZE), dtype=float)
    for index, metrics in enumerate(pre):
        radius = float(metrics["half_energy_radius"])
        if math.isfinite(radius):
            region[index] = (l1.RADIUS <= radius).astype(float)

    pre_local_epsi = np.sum(np.abs(psi) ** 2 * region, axis=(1, 2))
    pre_global_epsi = np.sum(np.abs(psi) ** 2, axis=(1, 2))

    perturb_inner = l1.RADIUS <= 2.0
    perturb_annulus = (l1.RADIUS >= 3.0) & (l1.RADIUS <= 5.0)
    psi[:, perturb_inner] *= 1.5
    psi[:, perturb_annulus] *= 0.5

    recovery_reset_hits = np.zeros(count, dtype=int)
    recovery_psi_cap_hits = np.zeros(count, dtype=int)
    recovery_phi_cap_hits = np.zeros(count, dtype=int)
    stage_signed = {
        stage: {key: np.zeros(count, dtype=float) for key in TRACKED_KEYS}
        for stage in sa.STAGES
    }
    stage_positive_local_epsi = {
        stage: np.zeros(count, dtype=float) for stage in sa.STAGES
    }
    max_residual_ratio = np.zeros(count, dtype=float)

    with np.errstate(all="ignore"):
        for _ in range(l1.RECOVERY_STEPS):
            output = sa.instrumented_step(
                psi, phi, kappa, mu, stencil, lane_arrays, spatial_arrays, region=region
            )
            psi, phi = output[:2]
            recovery_reset_hits += output[2]
            recovery_psi_cap_hits += output[3]
            recovery_phi_cap_hits += output[4]
            receipts = output[5]
            residual = output[6]

            for stage in sa.STAGES:
                for key in TRACKED_KEYS:
                    values = np.asarray(receipts[stage][key], dtype=float)
                    stage_signed[stage][key] += values
                local_epsi = np.asarray(receipts[stage]["epsi_local"], dtype=float)
                stage_positive_local_epsi[stage] += np.maximum(local_epsi, 0.0)

            for key in TRACKED_KEYS:
                values = np.asarray(residual[key], dtype=float)
                stage_values = np.stack(
                    [np.asarray(receipts[stage][key], dtype=float) for stage in sa.STAGES]
                )
                stage_sum = np.sum(stage_values, axis=0)
                absolute_stage_sum = np.sum(np.abs(stage_values), axis=0)
                total_change = stage_sum + values
                ratios = np.abs(values) / np.maximum(
                    1.0, np.maximum(np.abs(total_change), absolute_stage_sum)
                )
                max_residual_ratio = np.maximum(max_residual_ratio, ratios)

    post = [l1.spatial_metrics(psi[i], phi[i]) for i in range(count)]
    rows: list[dict[str, Any]] = []
    for index, lane in enumerate(lanes):
        energy_error = abs(post[index]["total_energy"] - pre[index]["total_energy"]) / (
            abs(pre[index]["total_energy"]) + 1e-30
        )
        energy_profile_error = _relative_l2(
            pre[index]["energy_radial_profile"], post[index]["energy_radial_profile"]
        )
        phi_profile_error = _relative_l2(
            pre[index]["phi_radial_profile"], post[index]["phi_radial_profile"]
        )
        half_radius_error = abs(
            post[index]["half_energy_radius"] - pre[index]["half_energy_radius"]
        )
        finite = bool(
            np.isfinite(psi[index]).all()
            and np.isfinite(phi[index]).all()
            and math.isfinite(energy_error)
            and math.isfinite(energy_profile_error)
            and math.isfinite(phi_profile_error)
        )
        reset_free = bool(reset_hits[index] + recovery_reset_hits[index] == 0)
        psi_cap_free = bool(psi_cap_hits[index] + recovery_psi_cap_hits[index] == 0)
        phi_cap_free = bool(phi_cap_hits[index] + recovery_phi_cap_hits[index] == 0)
        psi_recovery = bool(
            finite
            and reset_free
            and energy_error <= 0.05
            and energy_profile_error <= 0.10
            and half_radius_error <= 1.0
            and post[index]["center_displacement"] <= 0.5
        )
        phi_stationary_threshold = max(1e-10, 1e-8 * abs(phi_tail_means[index]))
        phi_stationary = bool(phi_slopes[index] <= phi_stationary_threshold)
        full_recovery = bool(
            psi_recovery
            and phi_cap_free
            and phi_profile_error <= 0.10
            and phi_stationary
        )

        transport_positive = float(stage_positive_local_epsi["psi_diffusion"][index])
        unpaired_positive = float(
            stage_positive_local_epsi["feedback"][index]
            + stage_positive_local_epsi["phi_gradient_flow"][index]
        )
        other_positive = float(
            sum(
                stage_positive_local_epsi[stage][index]
                for stage in sa.STAGES
                if stage not in {"psi_diffusion", "feedback", "phi_gradient_flow"}
            )
        )
        mechanism = classify_mechanism(
            residual_ratio=float(max_residual_ratio[index]),
            transport_positive=transport_positive,
            transport_global_signed=float(stage_signed["psi_diffusion"]["epsi_global"][index]),
            unpaired_positive=unpaired_positive,
            other_positive=other_positive,
            pre_local_epsi=float(pre_local_epsi[index]),
            pre_global_epsi=float(pre_global_epsi[index]),
        )
        recovery_metrics = {
            "finite": finite,
            "reset_free": reset_free,
            "psi_cap_free": psi_cap_free,
            "phi_cap_free": phi_cap_free,
            "total_energy_relative_error": float(energy_error),
            "energy_radial_profile_l2_error": float(energy_profile_error),
            "phi_radial_profile_l2_error": float(phi_profile_error),
            "half_energy_radius_absolute_error": float(half_radius_error),
            "center_displacement_after": float(post[index]["center_displacement"]),
            "localized_psi_recovery": psi_recovery,
            "localized_full_state_recovery": full_recovery,
            "phi_slope_per_step": float(phi_slopes[index]),
            "phi_stationary_threshold": float(phi_stationary_threshold),
        }
        rows.append(
            {
                "lane": lane.name,
                "stencil": stencil,
                "spatial_flags": {
                    "phi_gradient_flow": bool(lane.flow),
                    "psi_diffusion": bool(lane.psi_diffusion),
                    "phi_diffusion": bool(lane.phi_diffusion),
                },
                "pre_perturbation": pre[index],
                "post_recovery": post[index],
                "fixed_region_half_energy_radius": float(pre[index]["half_energy_radius"]),
                "fixed_region_pre_epsi": float(pre_local_epsi[index]),
                "global_pre_epsi": float(pre_global_epsi[index]),
                "events": {
                    "reset_hits": int(reset_hits[index] + recovery_reset_hits[index]),
                    "psi_cap_hits": int(psi_cap_hits[index] + recovery_psi_cap_hits[index]),
                    "phi_cap_hits": int(phi_cap_hits[index] + recovery_phi_cap_hits[index]),
                },
                "recovery": recovery_metrics,
                "near_return": near_return(recovery_metrics),
                "accounting": {
                    "maximum_residual_ratio": float(max_residual_ratio[index]),
                    "stage_signed": {
                        stage: {
                            key: float(stage_signed[stage][key][index])
                            for key in TRACKED_KEYS
                        }
                        for stage in sa.STAGES
                    },
                    "positive_local_epsi": {
                        stage: float(stage_positive_local_epsi[stage][index])
                        for stage in sa.STAGES
                    },
                    "transport_positive": transport_positive,
                    "unpaired_positive": unpaired_positive,
                    "other_positive": other_positive,
                },
                "mechanism": mechanism,
            }
        )
    return rows


def run_stage_a() -> dict[str, Any]:
    sa = _load_accounting()
    rows: list[dict[str, Any]] = []
    for stencil in STENCILS:
        rows.extend(_run_stencil(sa, stencil))
    candidates = stage_b_candidates(rows)
    return {
        "schema": SCHEMA,
        "stage": STAGE_A_ID,
        "protocol": {
            "grid_size": sa.l1.GRID_SIZE,
            "dt": sa.l1.DT,
            "primary_steps": sa.l1.STEPS,
            "recovery_steps": sa.l1.RECOVERY_STEPS,
            "phi0": 1.0,
            "stencils": STENCILS,
            "lanes": LANE_NAMES,
            "phi_cap_enabled": False,
            "noise_enabled": False,
            "perturbation": "multiply radius<=2 by 1.5 and radius 3..5 by 0.5",
            "closure_rtol": CLOSURE_RTOL,
            "positive_rtol": POSITIVE_RTOL,
            "near_return_factor": NEAR_RETURN_FACTOR,
            "q2_positive_by_stage_a": False,
        },
        "rows": rows,
        "stage_b_candidates": candidates,
        "combinations_s4_s7_remain_dormant": len(candidates) == 0,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
    }


def canonical_payload_sha256(result: dict[str, Any]) -> str:
    data = json.dumps(
        _json_ready(result), sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run_stage_a()
    result["canonical_payload_sha256_without_self"] = canonical_payload_sha256(result)
    payload = json.dumps(_json_ready(result), indent=2, sort_keys=True, allow_nan=False) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")
    print(json.dumps({
        "stage_b_candidates": result["stage_b_candidates"],
        "labels": {f"{r['stencil']}:{r['lane']}": r["mechanism"]["label"] for r in result["rows"]},
        "near_return": {f"{r['stencil']}:{r['lane']}": r["near_return"] for r in result["rows"]},
        "environment": result["environment"],
        "payload_sha256": result["canonical_payload_sha256_without_self"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
