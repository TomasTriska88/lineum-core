#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import io
import json
import lzma
import math
import zipfile
from pathlib import Path

import numpy as np
from scipy.stats import rankdata
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss, roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ARCHIVE_SHA256 = "0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588"
TABLE_CSV_SHA256 = "c28423cc6f8b935b8c6b7467966a55fe4bb91cbe5680210897365cf618e10a7d"
SEED = 20260804
N_PERM = 100_000
STRONG_TANH = {"UGC05253", "NGC5055", "UGC09133", "NGC2903", "NGC5033", "NGC3198"}
ORIGINAL_REJECTIONS = {
    "UGC06787", "UGC11914", "NGC6015", "NGC2403", "NGC1003", "UGC03205",
    "UGC02953", "UGC08699", "NGC0801", "NGC2998", "UGC06786", "NGC5907",
    "UGC02885", "UGC00128",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def decode_population_table(path: Path) -> tuple[list[dict[str, str]], str]:
    payload = base64.b64decode(path.read_bytes())
    raw = lzma.decompress(payload)
    digest = hashlib.sha256(raw).hexdigest()
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8"))))
    return rows, digest


def as_bool(value: str) -> bool:
    return value.strip().lower() == "true"


def parse_profile(data: bytes) -> np.ndarray:
    rows: list[list[float]] = []
    for raw_line in data.decode("utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        values = [float(x) for x in line.split()]
        if len(values) != 8:
            raise ValueError(f"Expected eight numeric columns, got {len(values)}")
        rows.append(values)
    array = np.asarray(rows, dtype=float)
    if array.shape[0] < 2:
        raise ValueError("At least two radial samples are required")
    if not np.all(np.diff(array[:, 0]) > 0):
        raise ValueError("Radii must be strictly increasing")
    if not np.all(array[:, 2] > 0):
        raise ValueError("Velocity uncertainties must be positive")
    return array


def disk_half_light_ratio(array: np.ndarray, span_normalized: bool = False) -> float:
    radius = array[:, 0]
    sigma = np.maximum(array[:, 6], 0.0)
    integrand = 2.0 * np.pi * radius * sigma
    increments = 0.5 * (integrand[:-1] + integrand[1:]) * np.diff(radius)
    cumulative = np.concatenate([[0.0], np.cumsum(increments)])
    total = float(cumulative[-1])
    if total <= 0:
        raise ValueError("Disk-light proxy is non-positive")
    target = 0.5 * total
    index = int(np.searchsorted(cumulative, target, side="left"))
    if index == 0:
        crossing = float(radius[0])
    else:
        lower = float(cumulative[index - 1])
        upper = float(cumulative[index])
        fraction = 0.0 if upper == lower else (target - lower) / (upper - lower)
        crossing = float(radius[index - 1] + fraction * (radius[index] - radius[index - 1]))
    if span_normalized:
        return (crossing - float(radius[0])) / float(radius[-1] - radius[0])
    return crossing / float(radius[-1])


def profile_controls(array: np.ndarray) -> dict[str, float]:
    radius, velocity, uncertainty = array[:, 0], array[:, 1], array[:, 2]
    fractional = uncertainty / np.maximum(np.abs(velocity), 1e-12)
    steps = np.diff(radius)
    step_cv = float(np.std(steps, ddof=0) / np.mean(steps))
    return {
        "median_fractional_velocity_error": float(np.median(fractional)),
        "radial_step_cv": step_cv,
        "row_count_profile": int(len(radius)),
        "rmax_profile": float(radius[-1]),
        "span_normalized_disk_half_light": disk_half_light_ratio(array, span_normalized=True),
    }


def pearson(a: np.ndarray, b: np.ndarray) -> float:
    ac = np.asarray(a, dtype=float) - float(np.mean(a))
    bc = np.asarray(b, dtype=float) - float(np.mean(b))
    denominator = float(np.linalg.norm(ac) * np.linalg.norm(bc))
    return float(ac @ bc / denominator)


def spearman(a: np.ndarray, b: np.ndarray) -> float:
    return pearson(rankdata(a, method="average"), rankdata(b, method="average"))


def auc_larger_positive(scores: np.ndarray, labels: np.ndarray) -> float:
    positive = scores[labels]
    negative = scores[~labels]
    wins = 0.0
    for value in positive:
        wins += float(np.sum(value > negative)) + 0.5 * float(np.sum(value == negative))
    return wins / (len(positive) * len(negative))


def permutation_correlation_p(x: np.ndarray, y: np.ndarray, observed: float, seed: int, n_perm: int) -> tuple[float, int]:
    xr = rankdata(x, method="average")
    yr = rankdata(y, method="average")
    xc = xr - float(np.mean(xr))
    yc = yr - float(np.mean(yr))
    denominator = float(np.linalg.norm(xc) * np.linalg.norm(yc))
    rng = np.random.default_rng(seed)
    extreme = 0
    chunk = 5000
    for start in range(0, n_perm, chunk):
        count = min(chunk, n_perm - start)
        permutations = np.asarray([rng.permutation(len(yc)) for _ in range(count)], dtype=int)
        values = (yc[permutations] @ xc) / denominator
        extreme += int(np.sum(np.abs(values) >= abs(observed) - 1e-15))
    return (extreme + 1) / (n_perm + 1), extreme


def permutation_auc_p(scores: np.ndarray, labels: np.ndarray, observed: float, seed: int, n_perm: int) -> tuple[float, int]:
    ranks = rankdata(scores, method="average")
    n_positive = int(np.sum(labels))
    n = len(labels)
    n_negative = n - n_positive
    rank_constant = n_positive * (n_positive + 1) / 2.0
    rng = np.random.default_rng(seed)
    extreme = 0
    for _ in range(n_perm):
        selected = rng.choice(n, n_positive, replace=False)
        auc = (float(np.sum(ranks[selected])) - rank_constant) / (n_positive * n_negative)
        if auc >= observed - 1e-15:
            extreme += 1
    return (extreme + 1) / (n_perm + 1), extreme


def residualize(values: np.ndarray, design: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    coefficients = np.linalg.lstsq(design, values, rcond=None)[0]
    fitted = design @ coefficients
    return values - fitted, fitted


def freedman_lane_p(residual_x: np.ndarray, residual_y: np.ndarray, design: np.ndarray, observed: float, seed: int, n_perm: int) -> tuple[float, int]:
    pseudo_inverse = np.linalg.pinv(design)
    rng = np.random.default_rng(seed)
    norm_x = float(np.linalg.norm(residual_x))
    extreme = 0
    chunk = 2000
    for start in range(0, n_perm, chunk):
        count = min(chunk, n_perm - start)
        permutations = np.asarray([rng.permutation(len(residual_y)) for _ in range(count)], dtype=int)
        permuted = residual_y[permutations]
        coefficients = permuted @ pseudo_inverse.T
        residuals = permuted - coefficients @ design.T
        correlations = (residuals @ residual_x) / (norm_x * np.linalg.norm(residuals, axis=1))
        extreme += int(np.sum(np.abs(correlations) >= abs(observed) - 1e-15))
    return (extreme + 1) / (n_perm + 1), extreme


def repeated_cross_validation(controls: np.ndarray, concentration: np.ndarray, labels: np.ndarray) -> dict:
    full = np.column_stack([controls, concentration])
    records = []
    for repeat in range(100):
        splitter = StratifiedKFold(n_splits=7, shuffle=True, random_state=SEED + repeat)
        probability_controls = np.zeros(len(labels), dtype=float)
        probability_full = np.zeros(len(labels), dtype=float)
        for train, test in splitter.split(controls, labels):
            common = dict(C=1.0, solver="liblinear", class_weight="balanced", max_iter=10000, random_state=SEED + repeat)
            control_model = make_pipeline(StandardScaler(), LogisticRegression(**common))
            full_model = make_pipeline(StandardScaler(), LogisticRegression(**common))
            control_model.fit(controls[train], labels[train])
            full_model.fit(full[train], labels[train])
            probability_controls[test] = control_model.predict_proba(controls[test])[:, 1]
            probability_full[test] = full_model.predict_proba(full[test])[:, 1]
        control_loss = float(log_loss(labels, probability_controls, labels=[0, 1]))
        full_loss = float(log_loss(labels, probability_full, labels=[0, 1]))
        records.append({
            "repeat": repeat,
            "control_log_loss": control_loss,
            "full_log_loss": full_loss,
            "log_loss_improvement": control_loss - full_loss,
            "control_auc": float(roc_auc_score(labels, probability_controls)),
            "full_auc": float(roc_auc_score(labels, probability_full)),
        })
    improvements = np.asarray([row["log_loss_improvement"] for row in records])
    full_aucs = np.asarray([row["full_auc"] for row in records])
    control_aucs = np.asarray([row["control_auc"] for row in records])
    return {
        "records": records,
        "improved_repeats": int(np.sum(improvements > 0)),
        "median_log_loss_improvement": float(np.median(improvements)),
        "mean_log_loss_improvement": float(np.mean(improvements)),
        "median_full_auc": float(np.median(full_aucs)),
        "median_control_auc": float(np.median(control_aucs)),
        "full_auc_range": [float(np.min(full_aucs)), float(np.max(full_aucs))],
    }


def summarize(values: np.ndarray) -> dict[str, float | int]:
    return {"n": int(len(values)), "median": float(np.median(values)), "mean": float(np.mean(values)), "min": float(np.min(values)), "max": float(np.max(values))}


def run(archive: Path, table_b64: Path) -> tuple[dict, list[dict]]:
    archive_digest = sha256_file(archive)
    if archive_digest != ARCHIVE_SHA256:
        raise ValueError(f"Unexpected archive SHA-256: {archive_digest}")
    table_rows, table_digest = decode_population_table(table_b64)
    if table_digest != TABLE_CSV_SHA256:
        raise ValueError(f"Unexpected population-table SHA-256: {table_digest}")
    unsigned = {row["galaxy"]: row for row in table_rows if row["lane"] == "unsigned_fiducial"}
    signed = {row["galaxy"]: row for row in table_rows if row["lane"] == "signed_fiducial"}
    if set(unsigned) != set(signed):
        raise ValueError("Cross-lane galaxy membership differs")
    cross_lane = {
        "same_informative": all(unsigned[g]["informative"] == signed[g]["informative"] for g in unsigned),
        "same_tanh_label": all(unsigned[g]["tanh_label"] == signed[g]["tanh_label"] for g in unsigned),
        "same_winner": all(unsigned[g]["best_shape"] == signed[g]["best_shape"] for g in unsigned),
    }
    if not all(cross_lane.values()):
        raise ValueError(f"Cross-lane identity failed: {cross_lane}")
    profiles = {}
    profile_features = {}
    profile_controls_map = {}
    with zipfile.ZipFile(archive) as handle:
        members = handle.namelist()
        if len(members) != 175:
            raise ValueError(f"Expected 175 profiles, found {len(members)}")
        for member in members:
            galaxy = member.removesuffix("_rotmod.dat")
            array = parse_profile(handle.read(member))
            profiles[galaxy] = array
            profile_features[galaxy] = disk_half_light_ratio(array)
            profile_controls_map[galaxy] = profile_controls(array)
    selected = []
    for galaxy in sorted(unsigned):
        row = unsigned[galaxy]
        if not as_bool(row["informative"]):
            continue
        if galaxy not in profiles:
            raise ValueError(f"Missing official profile for {galaxy}")
        controls = profile_controls_map[galaxy]
        if int(row["n_rows"]) != controls["row_count_profile"]:
            raise ValueError(f"Row-count mismatch for {galaxy}")
        if abs(float(row["rmax_kpc"]) - controls["rmax_profile"]) > 1e-12:
            raise ValueError(f"Rmax mismatch for {galaxy}")
        selected.append({
            "galaxy": galaxy,
            "n_rows": int(row["n_rows"]),
            "rmax_kpc": float(row["rmax_kpc"]),
            "has_bulge": as_bool(row["has_bulge"]),
            "best_shape": row["best_shape"],
            "delta_aic_tanh": float(row["delta_aic_tanh"]),
            "tanh_label": row["tanh_label"],
            "tanh_best": as_bool(row["tanh_best"]),
            "shape_identified": as_bool(row["shape_identified"]),
            "strong_rejection": row["tanh_label"] == "strongly_rejected",
            "strong_tanh_win": galaxy in STRONG_TANH,
            "disk_half_light_r_over_rmax": profile_features[galaxy],
            "span_normalized_disk_half_light": controls["span_normalized_disk_half_light"],
            "median_fractional_velocity_error": controls["median_fractional_velocity_error"],
            "radial_step_cv": controls["radial_step_cv"],
        })
    if len(selected) != 102:
        raise ValueError(f"Expected 102 informative galaxies, found {len(selected)}")
    x = np.asarray([row["disk_half_light_r_over_rmax"] for row in selected], dtype=float)
    y = np.asarray([row["delta_aic_tanh"] for row in selected], dtype=float)
    labels = np.asarray([row["strong_rejection"] for row in selected], dtype=bool)
    rho = spearman(x, y)
    rho_p, rho_extreme = permutation_correlation_p(x, y, rho, SEED, N_PERM)
    auc = auc_larger_positive(x, labels)
    auc_p, auc_extreme = permutation_auc_p(x, labels, auc, SEED + 1, N_PERM)
    continuous_controls = np.column_stack([
        rankdata([row["median_fractional_velocity_error"] for row in selected], method="average"),
        rankdata([row["n_rows"] for row in selected], method="average"),
        rankdata([row["rmax_kpc"] for row in selected], method="average"),
        rankdata([row["radial_step_cv"] for row in selected], method="average"),
    ])
    bulge = np.asarray([row["has_bulge"] for row in selected], dtype=float)[:, None]
    design = np.column_stack([np.ones(len(selected)), continuous_controls, bulge])
    residual_x, _ = residualize(rankdata(x, method="average"), design)
    residual_y, _ = residualize(rankdata(y, method="average"), design)
    partial = pearson(residual_x, residual_y)
    partial_p, partial_extreme = freedman_lane_p(residual_x, residual_y, design, partial, SEED + 2, N_PERM)
    controls_for_cv = np.column_stack([
        [row["median_fractional_velocity_error"] for row in selected],
        [row["n_rows"] for row in selected],
        [row["rmax_kpc"] for row in selected],
        [row["radial_step_cv"] for row in selected],
        [float(row["has_bulge"]) for row in selected],
    ])
    cv = repeated_cross_validation(controls_for_cv, x, labels.astype(int))
    remaining_indices = [i for i, row in enumerate(selected) if row["galaxy"] not in ORIGINAL_REJECTIONS]
    remaining_x = x[remaining_indices]
    remaining_y = y[remaining_indices]
    remaining_rho = spearman(remaining_x, remaining_y)
    remaining_p, _ = permutation_correlation_p(remaining_x, remaining_y, remaining_rho, SEED + 3, N_PERM)
    bulge_strata = {}
    for value in (False, True):
        indices = [i for i, row in enumerate(selected) if row["has_bulge"] is value]
        value_x, value_y = x[indices], y[indices]
        value_rho = spearman(value_x, value_y)
        value_p, _ = permutation_correlation_p(value_x, value_y, value_rho, SEED + 10 + int(value), N_PERM)
        bulge_strata[str(value).lower()] = {"n": len(indices), "rho": value_rho, "p": value_p, "strong_rejections": int(np.sum(labels[indices]))}
    errors = np.asarray([row["median_fractional_velocity_error"] for row in selected])
    ordered = np.argsort(errors)
    tercile_indices = np.array_split(ordered, 3)
    error_strata = {}
    for offset, (name, indices) in enumerate(zip(("low", "middle", "high"), tercile_indices)):
        value_rho = spearman(x[indices], y[indices])
        value_p, _ = permutation_correlation_p(x[indices], y[indices], value_rho, SEED + 20 + offset, N_PERM)
        error_strata[name] = {"n": len(indices), "rho": value_rho, "p": value_p, "strong_rejections": int(np.sum(labels[indices])), "error_range": [float(np.min(errors[indices])), float(np.max(errors[indices]))]}
    span_x = np.asarray([row["span_normalized_disk_half_light"] for row in selected])
    span_rho = spearman(span_x, y)
    span_rho_p, _ = permutation_correlation_p(span_x, y, span_rho, SEED + 30, N_PERM)
    span_auc = auc_larger_positive(span_x, labels)
    span_auc_p, _ = permutation_auc_p(span_x, labels, span_auc, SEED + 31, N_PERM)
    primary_pass = rho > 0 and rho_p <= 0.05
    binary_pass = auc >= 0.70 and auc_p <= 0.05
    adjusted_or_cv = (partial > 0 and partial_p <= 0.05) or (cv["improved_repeats"] >= 80 and cv["median_log_loss_improvement"] > 0 and cv["median_full_auc"] >= 0.65)
    if primary_pass and binary_pass and adjusted_or_cv:
        classification = "population_source_signal_supported"
    elif primary_pass or binary_pass:
        classification = "partial_population_source_signal"
    else:
        classification = "no_population_extension"
    group_summary = {
        "six_strong_tanh_wins": summarize(x[[row["strong_tanh_win"] for row in selected]]),
        "fourteen_strong_rejections": summarize(x[labels]),
        "remaining_eighty_two_informative": summarize(x[np.asarray([not row["strong_tanh_win"] and not row["strong_rejection"] for row in selected])]),
        "all_compatible": summarize(x[np.asarray([row["tanh_label"] == "compatible" for row in selected])]),
        "all_tension": summarize(x[np.asarray([row["tanh_label"] == "tension" for row in selected])]),
    }
    result = {
        "schema": "lineum-b4-population-concentration-result/1",
        "classification": classification,
        "inputs": {"official_archive_sha256": archive_digest, "population_csv_sha256": table_digest, "informative_galaxies": len(selected), "strong_rejections": int(np.sum(labels)), "cross_lane_checks": cross_lane},
        "primary_continuous": {"spearman_rho": rho, "two_sided_permutation_p": rho_p, "extreme_permutations": rho_extreme, "permutations": N_PERM, "preregistered_direction_pass": primary_pass, "observed_direction": "opposite_to_preregistered" if rho < 0 else "as_preregistered"},
        "secondary_binary": {"auc_larger_concentration_predicts_rejection": auc, "direction_agnostic_auc": max(auc, 1.0 - auc), "directional_permutation_p": auc_p, "extreme_permutations": auc_extreme, "permutations": N_PERM, "preregistered_direction_pass": binary_pass, "observed_direction": "opposite_to_preregistered" if auc < 0.5 else "as_preregistered"},
        "adjusted_partial_spearman": {"rho": partial, "two_sided_freedman_lane_p": partial_p, "extreme_permutations": partial_extreme, "permutations": N_PERM, "controls": ["median_fractional_velocity_error", "row_count", "maximum_measured_radius", "radial_step_coefficient_of_variation", "has_tabulated_bulge"]},
        "cross_validation": cv,
        "group_summary": group_summary,
        "robustness": {"exclude_original_fourteen_rejections": {"n": len(remaining_indices), "spearman_rho": remaining_rho, "permutation_p": remaining_p}, "bulge_strata": bulge_strata, "quoted_error_terciles": error_strata, "measured_span_normalization": {"spearman_rho": span_rho, "spearman_p": span_rho_p, "auc_larger_predicts_rejection": span_auc, "auc_directional_p": span_auc_p}},
        "decision_gates": {"primary_continuous_pass": primary_pass, "secondary_binary_pass": binary_pass, "adjusted_or_cross_validated_pass": adjusted_or_cv},
        "interpretation": {"reproduced_observation": "The compact-disk contrast remains true for the six strongest tanh wins versus the fourteen strongest rejections, but it does not generalize as a monotonic population relation across all 102 informative galaxies.", "measurement_warning": "All fourteen strong rejections occur in the low- or middle-fractional-error terciles; low-information curves often cannot distinguish neighboring saturation shapes.", "scope_safe_negative": "The simple one-dimensional monotonic disk-concentration extension is unsupported under the frozen test. This does not reject nonlinear, conditional, interaction-based, or source-projection mechanisms."},
        "environment": {"python": __import__("platform").python_version(), "numpy": np.__version__, "scipy": __import__("scipy").__version__, "scikit_learn": __import__("sklearn").__version__},
        "per_galaxy": selected,
    }
    return result, selected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--population-table-b64", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--table", type=Path, required=True)
    args = parser.parse_args()
    result, rows = run(args.archive, args.population_table_b64)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with args.table.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"classification": result["classification"], "spearman": result["primary_continuous"], "binary": result["secondary_binary"], "adjusted": result["adjusted_partial_spearman"], "cross_validation": {k: v for k, v in result["cross_validation"].items() if k != "records"}}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
