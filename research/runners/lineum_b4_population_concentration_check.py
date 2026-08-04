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
import random
import zipfile
from pathlib import Path

ARCHIVE_SHA256 = "0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588"
TABLE_CSV_SHA256 = "c28423cc6f8b935b8c6b7467966a55fe4bb91cbe5680210897365cf618e10a7d"
INDEPENDENT_DRAWS = 20_000


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode_table(path: Path) -> list[dict[str, str]]:
    raw = lzma.decompress(base64.b64decode(path.read_bytes()))
    if hashlib.sha256(raw).hexdigest() != TABLE_CSV_SHA256:
        raise ValueError("Population table SHA-256 mismatch")
    return list(csv.DictReader(io.StringIO(raw.decode("utf-8"))))


def independent_profile(data: bytes) -> list[tuple[float, ...]]:
    rows: list[tuple[float, ...]] = []
    for raw in data.decode("utf-8").split("\n"):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        values = tuple(float(x) for x in line.split())
        if len(values) != 8:
            raise ValueError("Unexpected profile width")
        rows.append(values)
    if any(rows[i + 1][0] <= rows[i][0] for i in range(len(rows) - 1)):
        raise ValueError("Radii are not increasing")
    if any(row[2] <= 0 for row in rows):
        raise ValueError("Non-positive velocity uncertainty")
    return rows


def independent_half_ratio(rows: list[tuple[float, ...]]) -> float:
    radii = [row[0] for row in rows]
    brightness = [max(row[6], 0.0) for row in rows]
    areas: list[float] = []
    total = 0.0
    for index in range(len(rows) - 1):
        left = 2.0 * math.pi * radii[index] * brightness[index]
        right = 2.0 * math.pi * radii[index + 1] * brightness[index + 1]
        area = 0.5 * (left + right) * (radii[index + 1] - radii[index])
        areas.append(area)
        total += area
    target = 0.5 * total
    accumulated = 0.0
    crossing = radii[-1]
    for index, area in enumerate(areas):
        if accumulated + area >= target:
            fraction = 0.0 if area == 0.0 else (target - accumulated) / area
            crossing = radii[index] + fraction * (radii[index + 1] - radii[index])
            break
        accumulated += area
    return crossing / radii[-1]


def average_ranks(values: list[float]) -> list[float]:
    ordered = sorted(enumerate(values), key=lambda item: item[1])
    ranks = [0.0] * len(values)
    start = 0
    while start < len(values):
        end = start + 1
        while end < len(values) and ordered[end][1] == ordered[start][1]:
            end += 1
        average = ((start + 1) + end) / 2.0
        for index in range(start, end):
            ranks[ordered[index][0]] = average
        start = end
    return ranks


def correlation(left: list[float], right: list[float]) -> float:
    mean_left = sum(left) / len(left)
    mean_right = sum(right) / len(right)
    numerator = sum((a - mean_left) * (b - mean_right) for a, b in zip(left, right))
    left_norm = math.sqrt(sum((a - mean_left) ** 2 for a in left))
    right_norm = math.sqrt(sum((b - mean_right) ** 2 for b in right))
    return numerator / (left_norm * right_norm)


def spearman(left: list[float], right: list[float]) -> float:
    return correlation(average_ranks(left), average_ranks(right))


def auc(scores: list[float], labels: list[bool]) -> float:
    positive = [score for score, label in zip(scores, labels) if label]
    negative = [score for score, label in zip(scores, labels) if not label]
    wins = 0.0
    for pos in positive:
        for neg in negative:
            wins += 1.0 if pos > neg else (0.5 if pos == neg else 0.0)
    return wins / (len(positive) * len(negative))


def mc_correlation_p(scores: list[float], outcomes: list[float], observed: float) -> float:
    x_ranks = average_ranks(scores)
    y_ranks = average_ranks(outcomes)
    rng = random.Random(777)
    extreme = 0
    shuffled = y_ranks[:]
    for _ in range(INDEPENDENT_DRAWS):
        rng.shuffle(shuffled)
        if abs(correlation(x_ranks, shuffled)) >= abs(observed) - 1e-15:
            extreme += 1
    return (extreme + 1) / (INDEPENDENT_DRAWS + 1)


def mc_auc_p(scores: list[float], labels: list[bool], observed: float) -> float:
    rng = random.Random(778)
    shuffled = labels[:]
    extreme = 0
    for _ in range(INDEPENDENT_DRAWS):
        rng.shuffle(shuffled)
        if auc(scores, shuffled) >= observed - 1e-15:
            extreme += 1
    return (extreme + 1) / (INDEPENDENT_DRAWS + 1)


def run(archive: Path, table_path: Path, result_path: Path) -> dict:
    if digest(archive) != ARCHIVE_SHA256:
        raise ValueError("Official archive SHA-256 mismatch")
    table = decode_table(table_path)
    unsigned = {row["galaxy"]: row for row in table if row["lane"] == "unsigned_fiducial" and row["informative"].lower() == "true"}
    signed = {row["galaxy"]: row for row in table if row["lane"] == "signed_fiducial" and row["informative"].lower() == "true"}
    if set(unsigned) != set(signed) or len(unsigned) != 102:
        raise ValueError("Frozen informative membership mismatch")
    result = json.loads(result_path.read_text(encoding="utf-8"))
    result_rows = {row["galaxy"]: row for row in result["per_galaxy"]}
    if set(result_rows) != set(unsigned):
        raise ValueError("Result membership mismatch")
    independent: dict[str, float] = {}
    with zipfile.ZipFile(archive) as handle:
        for galaxy in sorted(unsigned):
            independent[galaxy] = independent_half_ratio(independent_profile(handle.read(f"{galaxy}_rotmod.dat")))
    maximum_difference = max(abs(independent[galaxy] - result_rows[galaxy]["disk_half_light_r_over_rmax"]) for galaxy in independent)
    scores = [independent[galaxy] for galaxy in sorted(independent)]
    outcomes = [float(unsigned[galaxy]["delta_aic_tanh"]) for galaxy in sorted(independent)]
    labels = [unsigned[galaxy]["tanh_label"] == "strongly_rejected" for galaxy in sorted(independent)]
    rho = spearman(scores, outcomes)
    auc_value = auc(scores, labels)
    rho_primary = result["primary_continuous"]["spearman_rho"]
    auc_primary = result["secondary_binary"]["auc_larger_concentration_predicts_rejection"]
    p_rho = mc_correlation_p(scores, outcomes, rho)
    p_auc = mc_auc_p(scores, labels, auc_value)
    checks = {
        "archive_sha256_pass": True,
        "membership_pass": True,
        "maximum_feature_difference": maximum_difference,
        "feature_tolerance_pass": maximum_difference <= 1e-12,
        "independent_spearman_rho": rho,
        "spearman_difference": abs(rho - rho_primary),
        "spearman_pass": abs(rho - rho_primary) <= 1e-15,
        "independent_auc": auc_value,
        "auc_difference": abs(auc_value - auc_primary),
        "auc_pass": abs(auc_value - auc_primary) <= 1e-15,
        "independent_correlation_mc_p_20000": p_rho,
        "primary_correlation_mc_p_100000": result["primary_continuous"]["two_sided_permutation_p"],
        "correlation_mc_agreement_pass": abs(p_rho - result["primary_continuous"]["two_sided_permutation_p"]) <= 0.01,
        "independent_auc_mc_p_20000": p_auc,
        "primary_auc_mc_p_100000": result["secondary_binary"]["directional_permutation_p"],
        "auc_mc_agreement_pass": abs(p_auc - result["secondary_binary"]["directional_permutation_p"]) <= 0.01,
    }
    checks["passed"] = all(checks[key] for key in ("archive_sha256_pass", "membership_pass", "feature_tolerance_pass", "spearman_pass", "auc_pass", "correlation_mc_agreement_pass", "auc_mc_agreement_pass"))
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--population-table-b64", type=Path, required=True)
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    checks = run(args.archive, args.population_table_b64, args.result)
    args.output.write_text(json.dumps(checks, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(checks, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
