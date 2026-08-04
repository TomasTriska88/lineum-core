#!/usr/bin/env python3
"""B0/B1 provenance and analytic audit for the public TOLOG galactic tanh benchmark.

This research runner is a clean-room implementation of the publicly displayed
mathematical form. It does not import Lineum Core or any TOLOG code, and it does
not perform astronomical fitting.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import platform
import sys
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

OFFICIAL_SPARC_URL = "https://astroweb.case.edu/SPARC/Rotmod_LTG.zip"
ZENODO_ARCHIVE_URL = "https://zenodo.org/records/16284118/files/Rotmod_LTG.zip?download=1"
ZENODO_DOI = "10.5281/zenodo.16284118"
ZENODO_PUBLISHED_MD5 = "e4c8b92766026770ed35e5889064e12b"
TARGET_BASENAME = "NGC3198_rotmod.dat"
EXPECTED_COLUMNS = ["Rad", "Vobs", "errV", "Vgas", "Vdisk", "Vbul", "SBdisk", "SBbul"]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def md5_bytes(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()  # noqa: S324 - provenance checksum, not security


def download(url: str, timeout: float) -> tuple[bytes | None, dict[str, Any]]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Lineum-Core-public-SPARC-provenance-audit/0.1"},
    )
    started = time.time()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = response.read()
            receipt = {
                "url": url,
                "ok": True,
                "status": getattr(response, "status", None),
                "content_type": response.headers.get("Content-Type"),
                "content_length_header": response.headers.get("Content-Length"),
                "elapsed_seconds": time.time() - started,
                "error_type": None,
                "error": None,
            }
            return payload, receipt
    except Exception as exc:  # retain exact runtime failure class and message
        return None, {
            "url": url,
            "ok": False,
            "status": getattr(exc, "code", None),
            "content_type": None,
            "content_length_header": None,
            "elapsed_seconds": time.time() - started,
            "error_type": type(exc).__name__,
            "error": str(exc),
        }


def locate_target_member(names: list[str]) -> str:
    matches = [name for name in names if Path(name).name == TARGET_BASENAME]
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one {TARGET_BASENAME}; found {len(matches)}")
    return matches[0]


def parse_rotmod_text(text: str) -> dict[str, Any]:
    header_lines: list[str] = []
    rows: list[list[float]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("#"):
            header_lines.append(line)
            continue
        values = [float(item) for item in line.split()]
        rows.append(values)

    column_counts = sorted({len(row) for row in rows})
    finite = all(math.isfinite(value) for row in rows for value in row)
    radius_strictly_increasing = all(rows[index][0] < rows[index + 1][0] for index in range(len(rows) - 1))
    positive_uncertainties = all(row[2] > 0.0 for row in rows)

    return {
        "header_lines": header_lines,
        "row_count": len(rows),
        "column_counts": column_counts,
        "expected_column_count": len(EXPECTED_COLUMNS),
        "expected_columns": EXPECTED_COLUMNS,
        "all_values_finite": finite,
        "radius_strictly_increasing": radius_strictly_increasing,
        "all_velocity_uncertainties_positive": positive_uncertainties,
        "first_row": rows[0] if rows else None,
        "last_row": rows[-1] if rows else None,
    }


def inspect_archive(payload: bytes) -> dict[str, Any]:
    archive_sha256 = sha256_bytes(payload)
    archive_md5 = md5_bytes(payload)
    with zipfile.ZipFile(io.BytesIO(payload), "r") as archive:
        bad_member = archive.testzip()
        members = archive.namelist()
        target_member = locate_target_member(members)
        target_bytes = archive.read(target_member)

    try:
        target_text = target_bytes.decode("utf-8")
        encoding = "utf-8"
    except UnicodeDecodeError:
        target_text = target_bytes.decode("ascii")
        encoding = "ascii"

    parsed = parse_rotmod_text(target_text)
    gates = {
        "zip_integrity": bad_member is None,
        "published_md5_matches": archive_md5 == ZENODO_PUBLISHED_MD5,
        "target_member_unique": True,
        "target_has_eight_columns": parsed["column_counts"] == [len(EXPECTED_COLUMNS)],
        "target_values_finite": parsed["all_values_finite"],
        "target_radius_strictly_increasing": parsed["radius_strictly_increasing"],
        "target_uncertainties_positive": parsed["all_velocity_uncertainties_positive"],
    }
    return {
        "archive_bytes": len(payload),
        "archive_sha256": archive_sha256,
        "archive_md5": archive_md5,
        "zenodo_published_md5": ZENODO_PUBLISHED_MD5,
        "member_count": len(members),
        "member_names": members,
        "zip_first_bad_member": bad_member,
        "target_member": target_member,
        "target_encoding": encoding,
        "target_bytes": len(target_bytes),
        "target_sha256": sha256_bytes(target_bytes),
        "target": parsed,
        "gates": gates,
        "passed": all(gates.values()),
    }


def public_response(v_bar: float, v0: float, x: float) -> float:
    return math.sqrt(v_bar * v_bar + v0 * v0 * math.tanh(x))


def analytic_audit() -> dict[str, Any]:
    small_x = [1.0e-8, 1.0e-6, 1.0e-4]
    small_rows = []
    for x in small_x:
        observed = math.tanh(x)
        relative_error = abs(observed - x) / x
        small_rows.append({"x": x, "tanh_x": observed, "relative_error_vs_x": relative_error})

    large_x = [10.0, 20.0, 50.0]
    large_rows = [
        {"x": x, "tanh_x": math.tanh(x), "absolute_error_vs_one": abs(1.0 - math.tanh(x))}
        for x in large_x
    ]

    half_x = math.atanh(0.5)
    half_value = math.tanh(half_x)

    v0 = 173.0
    v_bar = 80.0
    k_eff = 2.0
    r_s = 5.0
    half_radius = (r_s / k_eff) * half_x
    plateau_v2 = v0 * v0
    observed_v2_at_20 = plateau_v2 * math.tanh(20.0)
    center_velocity = public_response(v_bar, v0, 0.0)

    grid = [index * 0.01 for index in range(2001)]
    values = [math.tanh(x) for x in grid]
    derivatives = [1.0 / math.cosh(x) ** 2 for x in grid]
    monotonic = all(values[index + 1] >= values[index] for index in range(len(values) - 1))
    positive_derivative = all(value > 0.0 for value in derivatives)

    radii = [index * 0.05 for index in range(401)]
    first = [math.tanh((2.0 * radius) / 5.0) for radius in radii]
    second = [math.tanh((4.0 * radius) / 10.0) for radius in radii]
    scale_degeneracy_max_abs = max(abs(a - b) for a, b in zip(first, second))

    central_added_v2_slope = v0 * v0 * (k_eff / r_s)
    numeric_step = 1.0e-6
    numeric_slope = (
        v0 * v0 * math.tanh(k_eff * numeric_step / r_s)
        - v0 * v0 * math.tanh(0.0)
    ) / numeric_step
    central_slope_relative_error = abs(numeric_slope - central_added_v2_slope) / central_added_v2_slope

    gates = {
        "tanh_zero_exact": math.tanh(0.0) == 0.0,
        "small_x_linear": max(row["relative_error_vs_x"] for row in small_rows) <= 4.0e-9,
        "large_x_plateau": max(row["absolute_error_vs_one"] for row in large_rows) <= 5.0e-9,
        "half_saturation": abs(half_value - 0.5) <= 1.0e-15,
        "finite_center": math.isfinite(center_velocity) and center_velocity == v_bar,
        "monotonic_nonnegative_domain": monotonic,
        "analytic_derivative_positive": positive_derivative,
        "plateau_velocity_squared": abs(observed_v2_at_20 - plateau_v2) <= 1.0e-12 * plateau_v2,
        "central_slope_matches_derivative": central_slope_relative_error <= 1.0e-12,
        "k_over_rs_degeneracy": scale_degeneracy_max_abs <= 1.0e-15,
    }

    return {
        "formula": "v_model(r)^2 = v_bar(r)^2 + V0^2 * tanh(k_eff * r / r_s)",
        "dimensionless_argument_requirement": "k_eff * r / r_s must be dimensionless",
        "small_x": small_rows,
        "large_x": large_rows,
        "half_saturation": {
            "x_half": half_x,
            "tanh_x_half": half_value,
            "example_k_eff": k_eff,
            "example_r_s": r_s,
            "example_half_radius": half_radius,
        },
        "plateau": {
            "V0": v0,
            "expected_added_velocity_squared": plateau_v2,
            "observed_at_x_20": observed_v2_at_20,
        },
        "center": {"v_bar": v_bar, "V0": v0, "model_velocity": center_velocity},
        "derivative": {
            "expression": "d(V0^2*tanh(k_eff*r/r_s))/dr = V0^2*(k_eff/r_s)*sech^2(k_eff*r/r_s)",
            "analytic_central_slope": central_added_v2_slope,
            "forward_difference_central_slope": numeric_slope,
            "relative_error": central_slope_relative_error,
        },
        "scale_degeneracy": {
            "comparison": "(k_eff=2,r_s=5) versus (k_eff=4,r_s=10)",
            "max_absolute_difference": scale_degeneracy_max_abs,
        },
        "gates": gates,
        "passed": all(gates.values()),
    }


def classify_archive_result(selected_source: str, archive_receipt: dict[str, Any]) -> tuple[str, bool, str | None]:
    if not archive_receipt["passed"]:
        return "archive_validation_failed", False, "Archive bytes were retrieved, but one or more provenance or structure gates failed."
    if selected_source in {"official_sparc", "local_archive"}:
        return "passed", True, None
    return "archival_mirror_only", False, "The archival mirror was usable, but the preregistered official-primary gate was not met."


def load_local_archive(path: Path) -> tuple[bytes | None, dict[str, Any]]:
    started = time.time()
    try:
        payload = path.read_bytes()
        return payload, {
            "url": None,
            "local_path": str(path),
            "ok": True,
            "elapsed_seconds": time.time() - started,
            "error_type": None,
            "error": None,
        }
    except Exception as exc:
        return None, {
            "url": None,
            "local_path": str(path),
            "ok": False,
            "elapsed_seconds": time.time() - started,
            "error_type": type(exc).__name__,
            "error": str(exc),
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=None, help="Optional pre-downloaded Rotmod_LTG.zip")
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    attempts: list[dict[str, Any]] = []
    payload: bytes | None = None
    selected_source: str | None = None

    if args.archive is not None:
        payload, receipt = load_local_archive(args.archive)
        attempts.append(receipt)
        if payload is not None:
            selected_source = "local_archive"
    else:
        for source_name, url in (
            ("official_sparc", OFFICIAL_SPARC_URL),
            ("zenodo_archival_mirror", ZENODO_ARCHIVE_URL),
        ):
            payload, receipt = download(url, args.timeout)
            receipt["source_name"] = source_name
            attempts.append(receipt)
            if payload is not None:
                selected_source = source_name
                break

    b0: dict[str, Any]
    if payload is None:
        b0 = {
            "status": "blocked_by_runtime_network",
            "passed": False,
            "selected_source": None,
            "attempts": attempts,
            "archive": None,
            "reason": "No archive bytes were retrievable; no unofficial galaxy rows were substituted.",
        }
    else:
        try:
            archive_receipt = inspect_archive(payload)
            status, passed, reason = classify_archive_result(selected_source, archive_receipt)
            b0 = {
                "status": status,
                "passed": passed,
                "selected_source": selected_source,
                "attempts": attempts,
                "archive": archive_receipt,
                "reason": reason,
            }
        except Exception as exc:
            b0 = {
                "status": "archive_validation_failed",
                "passed": False,
                "selected_source": selected_source,
                "attempts": attempts,
                "archive": None,
                "reason": f"{type(exc).__name__}: {exc}",
            }

    b1 = analytic_audit()
    if b0["passed"] and b1["passed"]:
        verdict = "b0_b1_passed"
    elif b1["passed"]:
        verdict = "b1_passed_b0_blocked"
    else:
        verdict = "b1_failed"

    output = {
        "schema_version": "0.1.0",
        "runner_scope": "B0 public-data provenance and B1 analytic known-answer audit only; no fit performed",
        "public_sources": {
            "official_sparc": OFFICIAL_SPARC_URL,
            "zenodo_archival_mirror": ZENODO_ARCHIVE_URL,
            "zenodo_doi": ZENODO_DOI,
            "zenodo_published_md5": ZENODO_PUBLISHED_MD5,
        },
        "environment": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "machine": platform.machine(),
        },
        "b0": b0,
        "b1": b1,
        "anti_cheat": {
            "private_tolog_document_used": False,
            "tolog_code_copied": False,
            "astronomical_fit_performed": False,
            "production_lineum_code_imported_or_modified": False,
        },
        "verdict": verdict,
        "b2_allowed": verdict == "b0_b1_passed",
    }

    rendered = json.dumps(output, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return 0 if b1["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
