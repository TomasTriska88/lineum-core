#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import platform
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

SCHEMA = "lineum-b4-q2-spatial-accounting-stage-a-check/1"
PRIMARY_SCHEMA = "lineum-b4-q2-spatial-accounting-stage-a-retained/1"
STAGE_ID = "Q2-SA1-A"
CLOSURE_RTOL = 1e-10
POSITIVE_RTOL = 1e-12
COMPARE_RTOL = 1e-12
COMPARE_ATOL = 1e-8
STENCILS = ("LAP4", "LAP8")
STAGES = (
    "phi_gradient_flow",
    "psi_guard_clip",
    "feedback",
    "linear_dissipation",
    "psi_diffusion",
    "mode_transfer",
    "phi_diffusion",
    "phi_cap",
    "reset",
)


@dataclass(frozen=True)
class Lane:
    name: str
    flow: bool
    psi_diffusion: bool
    phi_diffusion: bool


LANES = (
    Lane("L0", True, True, True),
    Lane("S1", False, True, False),
    Lane("S2", False, False, True),
    Lane("S3", True, False, False),
)


def load_canonical():
    here = Path(__file__).resolve().parent
    path = here / "lineum_b4_saturation_localized_l1.py"
    spec = importlib.util.spec_from_file_location("lineum_b4_l1_checker_reference", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load canonical localized reference")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def independent_diffuse(field: np.ndarray, kappa: np.ndarray, rate: float, stencil: str) -> np.ndarray:
    k_up = np.roll(kappa, 1, axis=1)
    k_down = np.roll(kappa, -1, axis=1)
    k_left = np.roll(kappa, 1, axis=2)
    k_right = np.roll(kappa, -1, axis=2)
    f_up = np.roll(field, 1, axis=1)
    f_down = np.roll(field, -1, axis=1)
    f_left = np.roll(field, 1, axis=2)
    f_right = np.roll(field, -1, axis=2)
    if stencil == "LAP4":
        neighbour_sum = f_up * k_up + f_down * k_down + f_left * k_left + f_right * k_right
        active = k_up + k_down + k_left + k_right
    elif stencil == "LAP8":
        k_ul = np.roll(k_up, 1, axis=2)
        k_ur = np.roll(k_up, -1, axis=2)
        k_dl = np.roll(k_down, 1, axis=2)
        k_dr = np.roll(k_down, -1, axis=2)
        f_ul = np.roll(f_up, 1, axis=2)
        f_ur = np.roll(f_up, -1, axis=2)
        f_dl = np.roll(f_down, 1, axis=2)
        f_dr = np.roll(f_down, -1, axis=2)
        neighbour_sum = (
            f_up * k_up + f_down * k_down + f_left * k_left + f_right * k_right
            + 0.25 * (f_ul * k_ul + f_ur * k_ur + f_dl * k_dl + f_dr * k_dr)
        )
        active = k_up + k_down + k_left + k_right + 0.25 * (k_ul + k_ur + k_dl + k_dr)
    else:
        raise ValueError(stencil)
    return rate * (neighbour_sum - active * field)


def geometry(size: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int]:
    center = (size - 1) / 2.0
    row, column = np.indices((size, size), dtype=float)
    drow = row - center
    dcolumn = column - center
    radius = np.sqrt(drow * drow + dcolumn * dcolumn)
    bins = np.floor(radius).astype(int)
    return row, column, radius, bins, int(bins.max()) + 1


def radial_profile(values: np.ndarray, bins: np.ndarray, count: int) -> list[float]:
    sums = np.bincount(bins.ravel(), weights=values.ravel(), minlength=count)
    counts = np.bincount(bins.ravel(), minlength=count)
    return (sums / np.maximum(counts, 1)).tolist()


def metrics(psi: np.ndarray, phi: np.ndarray, row: np.ndarray, column: np.ndarray, radius: np.ndarray, bins: np.ndarray, bin_count: int) -> dict[str, Any]:
    epsi = np.abs(psi) ** 2
    total = float(epsi.sum())
    if total > 0.0 and math.isfinite(total):
        center = (psi.shape[0] - 1) / 2.0
        crow = float((epsi * row).sum() / total)
        ccolumn = float((epsi * column).sum() / total)
        displacement = float(math.hypot(crow - center, ccolumn - center))
        order = np.argsort(radius.ravel())
        cumulative = np.cumsum(epsi.ravel()[order])
        index = int(np.searchsorted(cumulative, 0.5 * total))
        half_radius = float(radius.ravel()[order[min(index, order.size - 1)]])
    else:
        displacement = math.inf
        half_radius = math.inf
    return {
        "total_energy": total,
        "half_energy_radius": half_radius,
        "center_displacement": displacement,
        "energy_radial_profile": radial_profile(epsi, bins, bin_count),
        "phi_radial_profile": radial_profile(phi, bins, bin_count),
    }


def relative_l2(reference: list[float], candidate: list[float]) -> float:
    a = np.asarray(reference, dtype=float)
    b = np.asarray(candidate, dtype=float)
    n = min(a.size, b.size)
    return float(np.linalg.norm(b[:n] - a[:n]) / (np.linalg.norm(a[:n]) + 1e-30))


def linear_slope(values: np.ndarray) -> np.ndarray:
    x = np.arange(values.shape[0], dtype=float)
    x -= x.mean()
    centered = values - values.mean(axis=0, keepdims=True)
    return np.dot(x, centered) / float(np.dot(x, x))


def snapshot(psi: np.ndarray, phi: np.ndarray, region: np.ndarray | None) -> dict[str, np.ndarray]:
    epsi = np.abs(psi) ** 2
    if region is None:
        local_epsi = np.zeros(psi.shape[0], dtype=float)
        local_phi = np.zeros(psi.shape[0], dtype=float)
    else:
        local_epsi = np.sum(epsi * region, axis=(1, 2))
        local_phi = np.sum(phi * region, axis=(1, 2))
    return {
        "epsi_global": np.sum(epsi, axis=(1, 2)),
        "epsi_local": local_epsi,
        "phi_global": np.sum(phi, axis=(1, 2)),
        "phi_local": local_phi,
    }


def delta(before: dict[str, np.ndarray], after: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    return {key: after[key] - before[key] for key in before}


def checker_step(
    psi: np.ndarray,
    phi: np.ndarray,
    kappa: np.ndarray,
    mu: np.ndarray,
    stencil: str,
    lanes: tuple[Lane, ...],
    dt: float,
    psi_cap: float,
    phi_cap: float,
    region: np.ndarray | None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, dict[str, dict[str, np.ndarray]], dict[str, np.ndarray]]:
    flow_on = np.asarray([lane.flow for lane in lanes], dtype=bool)[:, None, None]
    psi_diff_on = np.asarray([lane.psi_diffusion for lane in lanes], dtype=bool)[:, None, None]
    phi_diff_on = np.asarray([lane.phi_diffusion for lane in lanes], dtype=bool)[:, None, None]

    drift_multiplier = 1.0 + mu
    clipped_phi = np.clip(phi, 0.0, 10.0)
    raw_interaction = 0.04 * clipped_phi * kappa * drift_multiplier
    interaction_factor = 0.1 * np.tanh(raw_interaction / 0.1)
    interaction = interaction_factor * psi
    interaction = interaction / (1.0 + np.abs(interaction) / 10.0)

    start = snapshot(psi, phi, region)
    before = start
    receipts: dict[str, dict[str, np.ndarray]] = {}

    gx, gy = np.gradient(phi, axis=(1, 2))
    flow = -0.004 * (gx + 1j * gy) * kappa * drift_multiplier
    flow = flow / (1.0 + np.abs(flow) / 10.0)
    psi = psi + np.where(flow_on, flow, 0.0) * dt
    after = snapshot(psi, phi, region)
    receipts["phi_gradient_flow"] = delta(before, after)
    before = after

    magnitude = np.abs(psi)
    cap_mask = magnitude > psi_cap
    cap_rows = cap_mask.reshape(psi.shape[0], -1).any(axis=1)
    scale = np.ones_like(magnitude)
    scale[cap_mask] = psi_cap / (magnitude[cap_mask] + 1e-30)
    psi = psi * scale
    after = snapshot(psi, phi, region)
    receipts["psi_guard_clip"] = delta(before, after)
    before = after

    psi = psi + interaction * dt
    after = snapshot(psi, phi, region)
    receipts["feedback"] = delta(before, after)
    before = after

    psi = psi - 0.005 * psi * dt
    after = snapshot(psi, phi, region)
    receipts["linear_dissipation"] = delta(before, after)
    before = after

    psi_diff = independent_diffuse(psi, kappa, 0.05, stencil) * kappa * dt
    psi = psi + np.where(psi_diff_on, psi_diff, 0.0)
    after = snapshot(psi, phi, region)
    receipts["psi_diffusion"] = delta(before, after)
    before = after

    epsi = np.abs(psi) ** 2
    transferred = 0.001 * epsi * kappa * dt
    phi = phi + transferred
    new_magnitude = np.sqrt(np.maximum(epsi - transferred, 0.0))
    psi = psi / (np.sqrt(epsi) + 1e-12) * new_magnitude
    after = snapshot(psi, phi, region)
    receipts["mode_transfer"] = delta(before, after)
    before = after

    phi_diff = 0.05 * independent_diffuse(phi, kappa, 0.05, stencil)
    phi = phi + np.where(phi_diff_on, phi_diff, 0.0)
    after = snapshot(psi, phi, region)
    receipts["phi_diffusion"] = delta(before, after)
    before = after

    phi_cap_rows = np.zeros(psi.shape[0], dtype=bool)
    after = snapshot(psi, phi, region)
    receipts["phi_cap"] = delta(before, after)
    before = after

    bad = ~np.isfinite(psi).reshape(psi.shape[0], -1).all(axis=1)
    finite_max = np.max(np.where(np.isfinite(np.abs(psi)), np.abs(psi), 0.0), axis=(1, 2))
    reset_rows = bad | (finite_max >= psi_cap * 0.99)
    psi[reset_rows] = 0.0
    after = snapshot(psi, phi, region)
    receipts["reset"] = delta(before, after)

    total = delta(start, after)
    residual: dict[str, np.ndarray] = {}
    for key in total:
        summed = sum((receipts[stage][key] for stage in STAGES), np.zeros_like(total[key]))
        residual[key] = total[key] - summed

    return psi, phi, reset_rows, cap_rows, phi_cap_rows, receipts, residual


def independent_label(residual_ratio: float, transport_positive: float, transport_global_signed: float, unpaired_positive: float, other_positive: float, pre_local: float, pre_global: float) -> dict[str, Any]:
    residual_ok = residual_ratio <= CLOSURE_RTOL
    transport_limit = CLOSURE_RTOL * max(1.0, abs(pre_global))
    transport_valid = transport_global_signed <= transport_limit
    transport_credit = transport_positive if transport_valid else 0.0
    positive_total = transport_positive + unpaired_positive + other_positive
    positive_floor = POSITIVE_RTOL * max(1.0, abs(pre_local))
    if not residual_ok:
        label = "unresolved_residual"
    elif positive_total > positive_floor and transport_credit > unpaired_positive:
        label = "transport_accounted"
    elif positive_total > positive_floor and unpaired_positive >= transport_credit:
        label = "unpaired_source_dominated"
    else:
        label = "sink_or_dispersion_dominated"
    return {
        "label": label,
        "residual_ok": bool(residual_ok),
        "transport_global_noncreating": bool(transport_valid),
        "transport_credit": float(transport_credit),
    }


def independent_near_return(recovery: dict[str, Any]) -> bool:
    return bool(
        recovery["finite"] and recovery["reset_free"] and recovery["psi_cap_free"] and recovery["phi_cap_free"]
        and recovery["total_energy_relative_error"] <= 0.10
        and recovery["energy_radial_profile_l2_error"] <= 0.20
        and recovery["half_energy_radius_absolute_error"] <= 2.0
        and recovery["center_displacement_after"] <= 1.0
        and recovery["phi_radial_profile_l2_error"] <= 0.20
    )


def numeric_match(a: float, b: float) -> tuple[bool, float, float]:
    absolute = abs(a - b)
    relative = absolute / max(1.0, abs(a), abs(b))
    return bool(absolute <= COMPARE_ATOL + COMPARE_RTOL * max(abs(a), abs(b))), absolute, relative


def run_independent() -> list[dict[str, Any]]:
    ref = load_canonical()
    size = ref.GRID_SIZE
    row, column, radius, bins, bin_count = geometry(size)
    rows: list[dict[str, Any]] = []
    for stencil in STENCILS:
        count = len(LANES)
        psi = np.stack([ref.GAUSSIAN.copy() for _ in LANES])
        phi = np.ones((count, size, size), dtype=float)
        kappa = np.ones_like(phi)
        mu = np.zeros_like(phi)
        reset_hits = np.zeros(count, dtype=int)
        psi_cap_hits = np.zeros(count, dtype=int)
        phi_cap_hits = np.zeros(count, dtype=int)
        tail_phi = np.empty((ref.STEPS, count), dtype=float)

        with np.errstate(all="ignore"):
            for step in range(ref.STEPS):
                psi, phi, resets, caps, pcaps, _, _ = checker_step(
                    psi, phi, kappa, mu, stencil, LANES, ref.DT, ref.PSI_CAP, ref.PHI_CAP, None
                )
                reset_hits += resets
                psi_cap_hits += caps
                phi_cap_hits += pcaps
                tail_phi[step] = np.mean(phi, axis=(1, 2))

        pre = [metrics(psi[i], phi[i], row, column, radius, bins, bin_count) for i in range(count)]
        tail_count = max(10, ref.STEPS // 5)
        phi_slopes = linear_slope(tail_phi[-tail_count:])
        phi_means = tail_phi[-tail_count:].mean(axis=0)
        region = np.zeros((count, size, size), dtype=float)
        for i in range(count):
            region[i] = (radius <= pre[i]["half_energy_radius"]).astype(float)
        pre_local = np.sum(np.abs(psi) ** 2 * region, axis=(1, 2))
        pre_global = np.sum(np.abs(psi) ** 2, axis=(1, 2))

        inner = radius <= 2.0
        annulus = (radius >= 3.0) & (radius <= 5.0)
        psi[:, inner] *= 1.5
        psi[:, annulus] *= 0.5

        recovery_resets = np.zeros(count, dtype=int)
        recovery_caps = np.zeros(count, dtype=int)
        recovery_pcaps = np.zeros(count, dtype=int)
        signed = {stage: {key: np.zeros(count) for key in ("epsi_global", "epsi_local", "phi_global", "phi_local")} for stage in STAGES}
        positive_local = {stage: np.zeros(count) for stage in STAGES}
        max_residual = np.zeros(count)

        with np.errstate(all="ignore"):
            for _ in range(ref.RECOVERY_STEPS):
                psi, phi, resets, caps, pcaps, receipts, residual = checker_step(
                    psi, phi, kappa, mu, stencil, LANES, ref.DT, ref.PSI_CAP, ref.PHI_CAP, region
                )
                recovery_resets += resets
                recovery_caps += caps
                recovery_pcaps += pcaps
                for stage in STAGES:
                    for key in signed[stage]:
                        signed[stage][key] += receipts[stage][key]
                    positive_local[stage] += np.maximum(receipts[stage]["epsi_local"], 0.0)
                for key in ("epsi_global", "epsi_local", "phi_global", "phi_local"):
                    stage_values = np.stack([receipts[stage][key] for stage in STAGES])
                    stage_sum = np.sum(stage_values, axis=0)
                    abs_sum = np.sum(np.abs(stage_values), axis=0)
                    total_change = stage_sum + residual[key]
                    ratio = np.abs(residual[key]) / np.maximum(1.0, np.maximum(np.abs(total_change), abs_sum))
                    max_residual = np.maximum(max_residual, ratio)

        post = [metrics(psi[i], phi[i], row, column, radius, bins, bin_count) for i in range(count)]
        for i, lane in enumerate(LANES):
            energy_error = abs(post[i]["total_energy"] - pre[i]["total_energy"]) / (abs(pre[i]["total_energy"]) + 1e-30)
            eprofile = relative_l2(pre[i]["energy_radial_profile"], post[i]["energy_radial_profile"])
            pprofile = relative_l2(pre[i]["phi_radial_profile"], post[i]["phi_radial_profile"])
            radius_error = abs(post[i]["half_energy_radius"] - pre[i]["half_energy_radius"])
            finite = bool(np.isfinite(psi[i]).all() and np.isfinite(phi[i]).all())
            reset_free = bool(reset_hits[i] + recovery_resets[i] == 0)
            psi_cap_free = bool(psi_cap_hits[i] + recovery_caps[i] == 0)
            phi_cap_free = bool(phi_cap_hits[i] + recovery_pcaps[i] == 0)
            psi_recovery = bool(finite and reset_free and energy_error <= 0.05 and eprofile <= 0.10 and radius_error <= 1.0 and post[i]["center_displacement"] <= 0.5)
            phi_threshold = max(1e-10, 1e-8 * abs(phi_means[i]))
            full = bool(psi_recovery and phi_cap_free and pprofile <= 0.10 and phi_slopes[i] <= phi_threshold)
            recovery = {
                "finite": finite,
                "reset_free": reset_free,
                "psi_cap_free": psi_cap_free,
                "phi_cap_free": phi_cap_free,
                "total_energy_relative_error": float(energy_error),
                "energy_radial_profile_l2_error": float(eprofile),
                "half_energy_radius_absolute_error": float(radius_error),
                "center_displacement_after": float(post[i]["center_displacement"]),
                "phi_radial_profile_l2_error": float(pprofile),
                "localized_psi_recovery": psi_recovery,
                "localized_full_state_recovery": full,
            }
            transport_positive = float(positive_local["psi_diffusion"][i])
            unpaired_positive = float(positive_local["feedback"][i] + positive_local["phi_gradient_flow"][i])
            other_positive = float(sum(positive_local[stage][i] for stage in STAGES if stage not in {"psi_diffusion", "feedback", "phi_gradient_flow"}))
            mechanism = independent_label(float(max_residual[i]), transport_positive, float(signed["psi_diffusion"]["epsi_global"][i]), unpaired_positive, other_positive, float(pre_local[i]), float(pre_global[i]))
            rows.append({
                "stencil": stencil,
                "lane": lane.name,
                "pre": {
                    "global_epsi": float(pre_global[i]),
                    "local_epsi": float(pre_local[i]),
                    "half_energy_radius": float(pre[i]["half_energy_radius"]),
                },
                "accounting": {
                    "maximum_residual_ratio": float(max_residual[i]),
                    "positive_local_feedback": float(positive_local["feedback"][i]),
                    "positive_local_phi_gradient_flow": float(positive_local["phi_gradient_flow"][i]),
                    "positive_local_psi_diffusion": transport_positive,
                    "unpaired_positive": unpaired_positive,
                    "transport_positive": transport_positive,
                    "transport_global_signed": float(signed["psi_diffusion"]["epsi_global"][i]),
                    "feedback_global_signed": float(signed["feedback"]["epsi_global"][i]),
                    "phi_gradient_flow_global_signed": float(signed["phi_gradient_flow"]["epsi_global"][i]),
                    "linear_dissipation_global_signed": float(signed["linear_dissipation"]["epsi_global"][i]),
                    "mode_transfer_epsi_global_signed": float(signed["mode_transfer"]["epsi_global"][i]),
                    "mode_transfer_phi_global_signed": float(signed["mode_transfer"]["phi_global"][i]),
                },
                "mechanism": mechanism,
                "recovery": recovery,
                "near_return": independent_near_return(recovery),
            })
    return rows


def compare_rows(primary_rows: list[dict[str, Any]], check_rows: list[dict[str, Any]]) -> dict[str, Any]:
    primary = {(row["stencil"], row["lane"]): row for row in primary_rows}
    check = {(row["stencil"], row["lane"]): row for row in check_rows}
    expected_keys = {(stencil, lane.name) for stencil in STENCILS for lane in LANES}
    key_set_pass = set(primary) == expected_keys and set(check) == expected_keys
    numeric_mismatches: list[dict[str, Any]] = []
    categorical_mismatches: list[dict[str, Any]] = []
    max_abs = 0.0
    max_rel = 0.0

    numeric_paths = (
        ("pre", "global_epsi"), ("pre", "local_epsi"), ("pre", "half_energy_radius"),
        ("accounting", "maximum_residual_ratio"), ("accounting", "positive_local_feedback"),
        ("accounting", "positive_local_phi_gradient_flow"), ("accounting", "positive_local_psi_diffusion"),
        ("accounting", "unpaired_positive"), ("accounting", "transport_positive"),
        ("accounting", "transport_global_signed"), ("accounting", "feedback_global_signed"),
        ("accounting", "phi_gradient_flow_global_signed"), ("accounting", "linear_dissipation_global_signed"),
        ("accounting", "mode_transfer_epsi_global_signed"), ("accounting", "mode_transfer_phi_global_signed"),
        ("recovery", "total_energy_relative_error"), ("recovery", "energy_radial_profile_l2_error"),
        ("recovery", "half_energy_radius_absolute_error"), ("recovery", "center_displacement_after"),
        ("recovery", "phi_radial_profile_l2_error"),
    )
    categorical_paths = (
        ("mechanism", "label"), ("mechanism", "transport_global_noncreating"),
        ("recovery", "finite"), ("recovery", "reset_free"), ("recovery", "psi_cap_free"),
        ("recovery", "phi_cap_free"), ("recovery", "localized_psi_recovery"),
        ("recovery", "localized_full_state_recovery"), (None, "near_return"),
    )

    if key_set_pass:
        for key in sorted(expected_keys):
            prow = primary[key]
            crow = check[key]
            for group, name in numeric_paths:
                a = float(prow[group][name])
                b = float(crow[group][name])
                ok, absolute, relative = numeric_match(a, b)
                max_abs = max(max_abs, absolute)
                max_rel = max(max_rel, relative)
                if not ok:
                    numeric_mismatches.append({"case": list(key), "path": f"{group}.{name}", "primary": a, "checker": b, "absolute": absolute, "relative": relative})
            for group, name in categorical_paths:
                a = prow[name] if group is None else prow[group][name]
                b = crow[name] if group is None else crow[group][name]
                if a != b:
                    categorical_mismatches.append({"case": list(key), "path": name if group is None else f"{group}.{name}", "primary": a, "checker": b})

    checker_candidates = []
    for lane in (lane.name for lane in LANES):
        matches = [row for row in check_rows if row["lane"] == lane]
        if len(matches) == 2 and all(row["mechanism"]["label"] == "transport_accounted" and row["near_return"] for row in matches):
            checker_candidates.append(lane)
    primary_candidates = []
    for lane in (lane.name for lane in LANES):
        matches = [row for row in primary_rows if row["lane"] == lane]
        if len(matches) == 2 and all(row["mechanism"]["label"] == "transport_accounted" and row["near_return"] for row in matches):
            primary_candidates.append(lane)
    if primary_candidates != checker_candidates:
        categorical_mismatches.append({"case": ["all"], "path": "stage_b_candidates", "primary": primary_candidates, "checker": checker_candidates})

    return {
        "key_set_pass": key_set_pass,
        "numeric_mismatch_count": len(numeric_mismatches),
        "categorical_mismatch_count": len(categorical_mismatches),
        "maximum_absolute_difference": max_abs,
        "maximum_relative_difference": max_rel,
        "numeric_mismatches": numeric_mismatches,
        "categorical_mismatches": categorical_mismatches,
        "checker_stage_b_candidates": checker_candidates,
        "primary_stage_b_candidates_rederived": primary_candidates,
    }


def canonical_sha(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    primary = json.loads(args.primary.read_text(encoding="utf-8"))
    protocol_pass = bool(
        primary.get("schema") == PRIMARY_SCHEMA
        and primary.get("stage") == STAGE_ID
        and primary.get("protocol", {}).get("stencils") == list(STENCILS)
        and primary.get("protocol", {}).get("lanes") == [lane.name for lane in LANES]
        and primary.get("protocol", {}).get("closure_rtol") == CLOSURE_RTOL
        and primary.get("protocol", {}).get("positive_rtol") == POSITIVE_RTOL
        and primary.get("protocol", {}).get("phi_cap_enabled") is False
        and primary.get("protocol", {}).get("noise_enabled") is False
    )
    check_rows = run_independent()
    comparison = compare_rows(primary.get("rows", []), check_rows)
    passed = bool(protocol_pass and comparison["key_set_pass"] and comparison["numeric_mismatch_count"] == 0 and comparison["categorical_mismatch_count"] == 0)
    result = {
        "schema": SCHEMA,
        "stage": STAGE_ID,
        "passed": passed,
        "protocol_pass": protocol_pass,
        "comparison": comparison,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "independence": {
            "imports_primary_stage_a_classifier": False,
            "imports_primary_accounting_instrumentation": False,
            "independent_diffusion": True,
            "independent_stage_update": True,
            "independent_metrics": True,
            "independent_classification": True,
            "shared_input": "canonical localized initial state and frozen constants only",
        },
        "rows": check_rows,
    }
    result["canonical_payload_sha256_without_self"] = canonical_sha(result)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "passed": passed,
        "protocol_pass": protocol_pass,
        "numeric_mismatch_count": comparison["numeric_mismatch_count"],
        "categorical_mismatch_count": comparison["categorical_mismatch_count"],
        "maximum_absolute_difference": comparison["maximum_absolute_difference"],
        "maximum_relative_difference": comparison["maximum_relative_difference"],
        "checker_stage_b_candidates": comparison["checker_stage_b_candidates"],
        "payload_sha256": result["canonical_payload_sha256_without_self"],
        "environment": result["environment"],
    }, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
