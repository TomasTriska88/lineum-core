#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import statistics
from collections import OrderedDict
from pathlib import Path

POSITIVE = ["UGC05253", "NGC5055", "UGC09133", "NGC2903", "NGC5033", "NGC3198"]
NEGATIVE = [
    "UGC06787", "UGC11914", "NGC6015", "NGC2403", "NGC1003", "UGC03205",
    "UGC02953", "UGC08699", "NGC0801", "NGC2998", "UGC06786", "NGC5907",
    "UGC02885", "UGC00128",
]
ORDER = POSITIVE + NEGATIVE

FEATURE_NAMES = [
    "stellar_half_light_r_over_rmax",
    "stellar_r80_over_rmax",
    "disk_half_light_r_over_rmax",
    "disk_r80_over_rmax",
    "stellar_light_fraction_inner_quarter",
    "disk_light_fraction_inner_quarter",
    "disk_velocity_peak_r_over_rmax",
    "abs_gas_velocity_peak_r_over_rmax",
    "median_bulge_v2_fraction_inner_quarter",
    "median_disk_v2_fraction_inner_quarter",
    "median_gas_v2_fraction_outer_quarter",
    "median_vbar_inner_to_outer",
]
CONTROL_NAMES = [
    "row_count",
    "rmax",
    "median_fractional_velocity_error",
    "radial_step_cv",
]
ARCHIVE_SHA256 = "0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_rows(path: Path) -> list[list[float]]:
    rows: list[list[float]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        vals = [float(x) for x in line.split()]
        if len(vals) != 8:
            raise ValueError(f"{path}: expected 8 numeric columns, got {len(vals)}")
        rows.append(vals)
    if len(rows) < 2:
        raise ValueError(f"{path}: expected at least two data rows")
    if any(rows[i + 1][0] <= rows[i][0] for i in range(len(rows) - 1)):
        raise ValueError(f"{path}: radii are not strictly increasing")
    if any(row[2] <= 0 for row in rows):
        raise ValueError(f"{path}: velocity uncertainties must be positive")
    return rows


def cumulative_profile(r: list[float], sigma: list[float]) -> list[float]:
    integrand = [2.0 * math.pi * ri * max(si, 0.0) for ri, si in zip(r, sigma)]
    cumulative = [0.0]
    for i in range(1, len(r)):
        cumulative.append(
            cumulative[-1]
            + 0.5 * (integrand[i - 1] + integrand[i]) * (r[i] - r[i - 1])
        )
    return cumulative


def interpolate_cumulative(r: list[float], cumulative: list[float], x: float) -> float:
    if x <= r[0]:
        return cumulative[0]
    if x >= r[-1]:
        return cumulative[-1]
    for i in range(1, len(r)):
        if x <= r[i]:
            t = (x - r[i - 1]) / (r[i] - r[i - 1])
            return cumulative[i - 1] + t * (cumulative[i] - cumulative[i - 1])
    return cumulative[-1]


def quantile_radius(r: list[float], cumulative: list[float], q: float) -> float:
    total = cumulative[-1]
    if total <= 0:
        raise ValueError("non-positive cumulative light proxy")
    target = q * total
    for i in range(1, len(r)):
        if cumulative[i] >= target:
            delta = cumulative[i] - cumulative[i - 1]
            t = 0.0 if delta == 0 else (target - cumulative[i - 1]) / delta
            return r[i - 1] + t * (r[i] - r[i - 1])
    return r[-1]


def median(values: list[float]) -> float:
    return float(statistics.median(values))


def extract_features(rows: list[list[float]]) -> tuple[OrderedDict[str, float], OrderedDict[str, float]]:
    cols = list(zip(*rows))
    r, vobs, err, vgas, vdisk, vbul, sbdisk, sbbul = [list(c) for c in cols]
    rmax = r[-1]
    stellar = [max(0.0, 0.5 * d + 0.7 * b) for d, b in zip(sbdisk, sbbul)]
    disk = [max(0.0, d) for d in sbdisk]

    cumulative_stellar = cumulative_profile(r, stellar)
    cumulative_disk = cumulative_profile(r, disk)

    inner_cut = 0.25 * rmax
    stellar_inner = (
        interpolate_cumulative(r, cumulative_stellar, inner_cut) / cumulative_stellar[-1]
    )
    disk_inner = (
        interpolate_cumulative(r, cumulative_disk, inner_cut) / cumulative_disk[-1]
    )

    disk_peak_index = max(range(len(r)), key=lambda i: vdisk[i])
    gas_peak_index = max(range(len(r)), key=lambda i: abs(vgas[i]))

    vbar2 = [
        g * g + 0.5 * d * d + 0.7 * b * b
        for g, d, b in zip(vgas, vdisk, vbul)
    ]
    inner = [i for i, ri in enumerate(r) if ri <= inner_cut]
    outer = [i for i, ri in enumerate(r) if ri >= 0.75 * rmax]
    if not inner or not outer:
        raise ValueError("missing data rows in an inner or outer radial quarter")

    bulge_fraction = median(
        [0.7 * vbul[i] ** 2 / vbar2[i] if vbar2[i] > 0 else 0.0 for i in inner]
    )
    disk_fraction = median(
        [0.5 * vdisk[i] ** 2 / vbar2[i] if vbar2[i] > 0 else 0.0 for i in inner]
    )
    gas_fraction = median(
        [vgas[i] ** 2 / vbar2[i] if vbar2[i] > 0 else 0.0 for i in outer]
    )
    vbar_ratio = median([math.sqrt(vbar2[i]) for i in inner]) / median(
        [math.sqrt(vbar2[i]) for i in outer]
    )

    steps = [r[i + 1] - r[i] for i in range(len(r) - 1)]
    step_cv = (
        statistics.pstdev(steps) / statistics.mean(steps) if len(steps) > 1 else 0.0
    )

    features = OrderedDict(
        [
            (FEATURE_NAMES[0], quantile_radius(r, cumulative_stellar, 0.5) / rmax),
            (FEATURE_NAMES[1], quantile_radius(r, cumulative_stellar, 0.8) / rmax),
            (FEATURE_NAMES[2], quantile_radius(r, cumulative_disk, 0.5) / rmax),
            (FEATURE_NAMES[3], quantile_radius(r, cumulative_disk, 0.8) / rmax),
            (FEATURE_NAMES[4], stellar_inner),
            (FEATURE_NAMES[5], disk_inner),
            (FEATURE_NAMES[6], r[disk_peak_index] / rmax),
            (FEATURE_NAMES[7], r[gas_peak_index] / rmax),
            (FEATURE_NAMES[8], bulge_fraction),
            (FEATURE_NAMES[9], disk_fraction),
            (FEATURE_NAMES[10], gas_fraction),
            (FEATURE_NAMES[11], vbar_ratio),
        ]
    )
    controls = OrderedDict(
        [
            (CONTROL_NAMES[0], float(len(r))),
            (CONTROL_NAMES[1], rmax),
            (
                CONTROL_NAMES[2],
                median([e / max(abs(v), 1e-300) for e, v in zip(err, vobs)]),
            ),
            (CONTROL_NAMES[3], step_cv),
        ]
    )
    return features, controls


def average_ranks(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    start = 0
    while start < len(values):
        end = start + 1
        while end < len(values) and values[order[end]] == values[order[start]]:
            end += 1
        average = ((start + 1) + end) / 2.0
        for j in range(start, end):
            ranks[order[j]] = average
        start = end
    return ranks


def auc_from_ranks(ranks: list[float], positive_indices: tuple[int, ...]) -> float:
    n1 = len(positive_indices)
    n0 = len(ranks) - n1
    rank_sum = sum(ranks[i] for i in positive_indices)
    u = rank_sum - n1 * (n1 + 1) / 2.0
    return u / (n1 * n0)


def exact_auc_test(values: list[float], positive_count: int = 6) -> dict[str, float | int | str]:
    ranks = average_ranks(values)
    observed = auc_from_ranks(ranks, tuple(range(positive_count)))
    observed_deviation = abs(observed - 0.5)
    extreme = 0
    total = 0
    for combo in itertools.combinations(range(len(values)), positive_count):
        total += 1
        candidate = auc_from_ranks(ranks, combo)
        if abs(candidate - 0.5) >= observed_deviation - 1e-15:
            extreme += 1
    return {
        "auc_positive_high": observed,
        "auc_direction_agnostic": max(observed, 1.0 - observed),
        "direction": (
            "higher_in_strong_tanh"
            if observed > 0.5
            else "lower_in_strong_tanh"
            if observed < 0.5
            else "none"
        ),
        "exact_two_sided_p": extreme / total,
        "extreme_assignments": extreme,
        "total_assignments": total,
    }


def apply_holm(stats: OrderedDict[str, dict[str, float | int | str]]) -> None:
    ordered = sorted(stats, key=lambda name: float(stats[name]["exact_two_sided_p"]))
    running = 0.0
    m = len(ordered)
    for i, name in enumerate(ordered):
        adjusted = min(1.0, (m - i) * float(stats[name]["exact_two_sided_p"]))
        running = max(running, adjusted)
        stats[name]["holm_adjusted_p"] = running


def summarize(values: list[float]) -> dict[str, float]:
    return {
        "median": median(values),
        "mean": sum(values) / len(values),
        "min": min(values),
        "max": max(values),
    }


def measured_span_disk_r50(rows: list[list[float]]) -> float:
    r = [row[0] for row in rows]
    disk = [max(0.0, row[6]) for row in rows]
    cumulative = cumulative_profile(r, disk)
    r50 = quantile_radius(r, cumulative, 0.5)
    return (r50 - r[0]) / (r[-1] - r[0])


def leave_one_out_disk_test(values: list[float]) -> list[dict[str, float | str]]:
    labels = [True] * len(POSITIVE) + [False] * len(NEGATIVE)
    results = []
    for omitted in range(len(values)):
        reduced_values = [v for i, v in enumerate(values) if i != omitted]
        reduced_labels = [v for i, v in enumerate(labels) if i != omitted]
        positive_indices = tuple(i for i, label in enumerate(reduced_labels) if label)
        ranks = average_ranks(reduced_values)
        observed = auc_from_ranks(ranks, positive_indices)
        observed_deviation = abs(observed - 0.5)
        extreme = 0
        total = 0
        for combo in itertools.combinations(range(len(reduced_values)), len(positive_indices)):
            total += 1
            candidate = auc_from_ranks(ranks, combo)
            if abs(candidate - 0.5) >= observed_deviation - 1e-15:
                extreme += 1
        results.append(
            {
                "omitted": ORDER[omitted],
                "auc_direction_agnostic": max(observed, 1.0 - observed),
                "exact_two_sided_p": extreme / total,
            }
        )
    return results


def run(data_dir: Path) -> dict:
    rows_by_name: OrderedDict[str, list[list[float]]] = OrderedDict()
    file_receipts: OrderedDict[str, dict[str, str | int]] = OrderedDict()
    for name in ORDER:
        path = data_dir / f"{name}_rotmod.dat"
        raw = path.read_bytes()
        rows = load_rows(path)
        rows_by_name[name] = rows
        file_receipts[name] = {
            "file": path.name,
            "sha256": sha256_bytes(raw),
            "rows": len(rows),
        }

    feature_values: OrderedDict[str, OrderedDict[str, float]] = OrderedDict()
    control_values: OrderedDict[str, OrderedDict[str, float]] = OrderedDict()
    for name, rows in rows_by_name.items():
        feature_values[name], control_values[name] = extract_features(rows)

    feature_stats: OrderedDict[str, dict[str, float | int | str]] = OrderedDict()
    for feature in FEATURE_NAMES:
        feature_stats[feature] = exact_auc_test(
            [feature_values[name][feature] for name in ORDER]
        )
    apply_holm(feature_stats)

    control_stats: OrderedDict[str, dict[str, float | int | str]] = OrderedDict()
    for feature in CONTROL_NAMES:
        control_stats[feature] = exact_auc_test(
            [control_values[name][feature] for name in ORDER]
        )

    strong = [
        name
        for name in FEATURE_NAMES
        if float(feature_stats[name]["holm_adjusted_p"]) <= 0.05
        and float(feature_stats[name]["auc_direction_agnostic"]) >= 0.80
    ]
    partial = [
        name
        for name in FEATURE_NAMES
        if name not in strong
        and float(feature_stats[name]["exact_two_sided_p"]) <= 0.05
        and float(feature_stats[name]["auc_direction_agnostic"]) >= 0.75
    ]
    classification = (
        "simple_source_separator_supported"
        if strong
        else "partial_source_signal_only"
        if partial
        else "no_simple_source_separator"
    )

    winning_feature = min(
        FEATURE_NAMES, key=lambda name: float(feature_stats[name]["holm_adjusted_p"])
    )
    winning_values = [feature_values[name][winning_feature] for name in ORDER]
    span_values = [measured_span_disk_r50(rows_by_name[name]) for name in ORDER]
    span_test = exact_auc_test(span_values)

    return {
        "schema": "lineum-b4-source-structure-discriminator/1",
        "classification": classification,
        "groups": {"strong_tanh": POSITIVE, "strong_rejection": NEGATIVE},
        "input": {
            "official_archive_sha256": ARCHIVE_SHA256,
            "selected_file_receipts": file_receipts,
            "column_schema": [
                "radius_kpc",
                "vobs_km_s",
                "errv_km_s",
                "vgas_km_s",
                "vdisk_km_s",
                "vbul_km_s",
                "sbdisk_lsun_pc2",
                "sbbul_lsun_pc2",
            ],
        },
        "method": {
            "primary_features": FEATURE_NAMES,
            "measurement_controls": CONTROL_NAMES,
            "positive_count": len(POSITIVE),
            "negative_count": len(NEGATIVE),
            "exact_assignments": math.comb(len(ORDER), len(POSITIVE)),
            "strong_gate": "Holm-adjusted p <= 0.05 and direction-agnostic AUC >= 0.80",
            "partial_gate": "raw p <= 0.05 and direction-agnostic AUC >= 0.75, strong gate failed",
            "cumulative_rule": "trapezoidal 2*pi*r*Sigma over measured samples; linear interpolation of cumulative endpoint values",
            "stellar_proxy": "0.5*SBdisk + 0.7*SBbul",
        },
        "checks": {
            "selected_galaxies": len(ORDER),
            "all_files_present": True,
            "all_have_eight_columns": True,
            "all_radii_strictly_increasing": True,
            "all_velocity_uncertainties_positive": True,
        },
        "per_galaxy": {
            name: {
                "group": "strong_tanh" if name in POSITIVE else "strong_rejection",
                "features": feature_values[name],
                "controls": control_values[name],
            }
            for name in ORDER
        },
        "feature_statistics": feature_stats,
        "control_statistics": control_stats,
        "strong_source_separators": strong,
        "partial_source_separators": partial,
        "winning_feature": winning_feature,
        "winning_feature_group_summary": {
            "strong_tanh": summarize(winning_values[: len(POSITIVE)]),
            "strong_rejection": summarize(winning_values[len(POSITIVE) :]),
        },
        "post_hoc_robustness": {
            "winning_feature_measured_span_normalization": span_test,
            "leave_one_out": leave_one_out_disk_test(winning_values),
            "scope_note": "Post-hoc robustness checks do not change the preregistered classification.",
        },
        "interpretation_limits": [
            "The selected contrast compares outcome-defined extremes and is not a held-out population predictor.",
            "A source separator is not evidence of causation or a Lineum/TOLOG mechanism.",
            "Median fractional velocity uncertainty also separates the selected groups and remains a possible measurement confound.",
            "The result does not establish dark-matter replacement, modified gravity, or an emergent tanh.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.data_dir)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "classification": result["classification"],
                "winning_feature": result["winning_feature"],
                "strong_source_separators": result["strong_source_separators"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
