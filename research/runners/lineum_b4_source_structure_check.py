#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

POSITIVE = ["UGC05253", "NGC5055", "UGC09133", "NGC2903", "NGC5033", "NGC3198"]
NEGATIVE = [
    "UGC06787", "UGC11914", "NGC6015", "NGC2403", "NGC1003", "UGC03205",
    "UGC02953", "UGC08699", "NGC0801", "NGC2998", "UGC06786", "NGC5907",
    "UGC02885", "UGC00128",
]
ORDER = POSITIVE + NEGATIVE
FEATURES = [
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


def read_numeric(path: Path) -> list[tuple[float, ...]]:
    out = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        text = raw.strip()
        if not text or text.startswith("#"):
            continue
        fields = text.split()
        if len(fields) != 8:
            raise AssertionError(f"{path}: wrong column count")
        out.append(tuple(float(fields[i]) for i in range(8)))
    return out


def scalar_median(values: list[float]) -> float:
    z = sorted(values)
    middle = len(z) // 2
    return z[middle] if len(z) % 2 else (z[middle - 1] + z[middle]) / 2.0


def light_summary(radius: list[float], density: list[float]) -> tuple[float, float, float]:
    endpoint = [0.0]
    for i in range(len(radius) - 1):
        left = 2.0 * math.pi * radius[i] * max(density[i], 0.0)
        right = 2.0 * math.pi * radius[i + 1] * max(density[i + 1], 0.0)
        endpoint.append(
            endpoint[-1] + (radius[i + 1] - radius[i]) * (left + right) / 2.0
        )
    total = endpoint[-1]

    def inverse(frac: float) -> float:
        target = frac * total
        for i in range(1, len(radius)):
            if endpoint[i] >= target:
                width = endpoint[i] - endpoint[i - 1]
                fraction = 0.0 if width == 0 else (target - endpoint[i - 1]) / width
                return radius[i - 1] + fraction * (radius[i] - radius[i - 1])
        return radius[-1]

    cut = radius[-1] / 4.0
    inside = 0.0
    if cut >= radius[-1]:
        inside = total
    elif cut > radius[0]:
        for i in range(1, len(radius)):
            if radius[i] >= cut:
                fraction = (cut - radius[i - 1]) / (radius[i] - radius[i - 1])
                inside = endpoint[i - 1] + fraction * (endpoint[i] - endpoint[i - 1])
                break
    return inverse(0.5) / radius[-1], inverse(0.8) / radius[-1], inside / total


def reconstruct(text_path: Path) -> list[float]:
    rows = read_numeric(text_path)
    radius = [row[0] for row in rows]
    gas = [row[3] for row in rows]
    disk_v = [row[4] for row in rows]
    bulge_v = [row[5] for row in rows]
    disk_sb = [max(0.0, row[6]) for row in rows]
    bulge_sb = [max(0.0, row[7]) for row in rows]
    stellar_sb = [0.5 * d + 0.7 * b for d, b in zip(disk_sb, bulge_sb)]

    stellar_50, stellar_80, stellar_inner = light_summary(radius, stellar_sb)
    disk_50, disk_80, disk_inner = light_summary(radius, disk_sb)

    disk_max = max(disk_v)
    disk_peak = radius[next(i for i, value in enumerate(disk_v) if value == disk_max)] / radius[-1]
    absolute_gas = [abs(value) for value in gas]
    gas_max = max(absolute_gas)
    gas_peak = radius[next(i for i, value in enumerate(absolute_gas) if value == gas_max)] / radius[-1]

    baryonic_squared = [
        gas[i] ** 2 + 0.5 * disk_v[i] ** 2 + 0.7 * bulge_v[i] ** 2
        for i in range(len(rows))
    ]
    inner_indices = [i for i, value in enumerate(radius) if value <= radius[-1] / 4.0]
    outer_indices = [i for i, value in enumerate(radius) if value >= 3.0 * radius[-1] / 4.0]

    bulge_fraction = scalar_median(
        [
            0.7 * bulge_v[i] ** 2 / baryonic_squared[i]
            if baryonic_squared[i] > 0
            else 0.0
            for i in inner_indices
        ]
    )
    disk_fraction = scalar_median(
        [
            0.5 * disk_v[i] ** 2 / baryonic_squared[i]
            if baryonic_squared[i] > 0
            else 0.0
            for i in inner_indices
        ]
    )
    gas_fraction = scalar_median(
        [
            gas[i] ** 2 / baryonic_squared[i]
            if baryonic_squared[i] > 0
            else 0.0
            for i in outer_indices
        ]
    )
    velocity_ratio = scalar_median(
        [math.sqrt(baryonic_squared[i]) for i in inner_indices]
    ) / scalar_median([math.sqrt(baryonic_squared[i]) for i in outer_indices])

    return [
        stellar_50,
        stellar_80,
        disk_50,
        disk_80,
        stellar_inner,
        disk_inner,
        disk_peak,
        gas_peak,
        bulge_fraction,
        disk_fraction,
        gas_fraction,
        velocity_ratio,
    ]


def auc_pairwise(values: list[float], positive: tuple[int, ...]) -> float:
    p = set(positive)
    negative = [i for i in range(len(values)) if i not in p]
    score = 0.0
    for i in positive:
        for j in negative:
            if values[i] > values[j]:
                score += 1.0
            elif values[i] == values[j]:
                score += 0.5
    return score / (len(positive) * len(negative))


def permutation_test(values: list[float]) -> tuple[float, int, int]:
    observed = auc_pairwise(values, tuple(range(6)))
    deviation = abs(observed - 0.5)
    extreme = 0
    total = 0
    for combo in itertools.combinations(range(20), 6):
        total += 1
        if abs(auc_pairwise(values, combo) - 0.5) >= deviation - 1e-15:
            extreme += 1
    return observed, extreme, total


def toy_checks() -> dict[str, float | bool]:
    radius = [i / 1000.0 for i in range(1001)]
    uniform = light_summary(radius, [1.0] * len(radius))
    exponential = light_summary(radius, [math.exp(-5.0 * r) for r in radius])
    central = light_summary(radius, [math.exp(-50.0 * r) for r in radius])
    return {
        "uniform_half_radius": uniform[0],
        "uniform_expected_half_radius": math.sqrt(0.5),
        "uniform_half_radius_abs_error": abs(uniform[0] - math.sqrt(0.5)),
        "concentration_ordering_passed": central[0] < exponential[0] < uniform[0],
        "inner_fraction_ordering_passed": central[2] > exponential[2] > uniform[2],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--result", type=Path, required=True)
    args = parser.parse_args()

    retained = json.loads(args.result.read_text(encoding="utf-8"))
    reconstructed = {
        name: reconstruct(args.data_dir / f"{name}_rotmod.dat") for name in ORDER
    }

    max_feature_difference = 0.0
    max_auc_difference = 0.0
    max_p_difference = 0.0
    for feature_index, feature in enumerate(FEATURES):
        values = [reconstructed[name][feature_index] for name in ORDER]
        observed, extreme, total = permutation_test(values)
        retained_stat = retained["feature_statistics"][feature]
        max_auc_difference = max(
            max_auc_difference, abs(observed - retained_stat["auc_positive_high"])
        )
        max_p_difference = max(
            max_p_difference, abs(extreme / total - retained_stat["exact_two_sided_p"])
        )
        if extreme != retained_stat["extreme_assignments"] or total != retained_stat["total_assignments"]:
            raise AssertionError(f"{feature}: exact permutation count mismatch")
        for name in ORDER:
            max_feature_difference = max(
                max_feature_difference,
                abs(
                    reconstructed[name][feature_index]
                    - retained["per_galaxy"][name]["features"][feature]
                ),
            )

    toys = toy_checks()
    passed = (
        max_feature_difference <= 1e-14
        and max_auc_difference <= 1e-14
        and max_p_difference <= 1e-14
        and toys["uniform_half_radius_abs_error"] <= 2e-6
        and toys["concentration_ordering_passed"]
        and toys["inner_fraction_ordering_passed"]
    )
    output = {
        "passed": passed,
        "max_feature_difference": max_feature_difference,
        "max_auc_difference": max_auc_difference,
        "max_exact_p_difference": max_p_difference,
        "toy_checks": toys,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
