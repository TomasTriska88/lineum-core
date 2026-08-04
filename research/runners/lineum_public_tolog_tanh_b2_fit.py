#!/usr/bin/env python3
"""Literal public-formula B2 fit for NGC 3198.

This clean-room research runner implements only the preregistered public
phenomenological comparator. It does not import Lineum Core or TOLOG code and
it does not perform B3 convention sensitivity, B4 ablations, or Lineum fitting.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import sys
from pathlib import Path
from typing import Any

import numpy as np
import scipy
from scipy.optimize import least_squares

EXPECTED_DATA_SHA256 = "17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953"
R_S_KPC = 5.0
V0_BOUNDS = (0.0, 400.0)
K_BOUNDS = (1.0e-6, 100.0)
V0_STARTS = (25.0, 75.0, 150.0, 250.0)
K_STARTS = (0.01, 0.1, 1.0, 10.0)
CURVE_EQUIVALENCE_TOLERANCE_KMS = 1.0e-6
BOUNDARY_FRACTION = 1.0e-6
PUBLIC_REDUCED_CHI2 = 1.5
PUBLIC_WINDOW = 0.15
MATERIAL_DELTA_AIC = 10.0
MATERIAL_CHI2_FRACTION = 0.8
EXPECTED_COLUMNS = ("Rad", "Vobs", "errV", "Vgas", "Vdisk", "Vbul", "SBdisk", "SBbul")
REGIONS = (
    ("inner", 0.0, 5.0, True),
    ("transition", 5.0, 15.0, True),
    ("outer", 15.0, math.inf, False),
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_data(path: Path) -> tuple[np.ndarray, list[str], bytes]:
    payload = path.read_bytes()
    digest = sha256_bytes(payload)
    if digest != EXPECTED_DATA_SHA256:
        raise ValueError(f"Unexpected data SHA-256: {digest}")

    headers: list[str] = []
    rows: list[list[float]] = []
    for raw_line in payload.decode("utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("#"):
            headers.append(line)
            continue
        values = [float(item) for item in line.split()]
        if len(values) != len(EXPECTED_COLUMNS):
            raise ValueError(f"Expected 8 columns, found {len(values)}")
        rows.append(values)

    data = np.asarray(rows, dtype=np.float64)
    if data.shape != (43, 8):
        raise ValueError(f"Unexpected data shape: {data.shape}")
    if not np.all(np.isfinite(data)):
        raise ValueError("Non-finite data value")
    if not np.all(np.diff(data[:, 0]) > 0.0):
        raise ValueError("Radius is not strictly increasing")
    if not np.all(data[:, 2] > 0.0):
        raise ValueError("Velocity uncertainties must be positive")
    return data, headers, payload


def baryonic_literal(data: np.ndarray) -> np.ndarray:
    return np.sqrt(data[:, 3] ** 2 + data[:, 4] ** 2 + data[:, 5] ** 2)


def model_vector(radius: np.ndarray, v_bar: np.ndarray, v0: float, k_eff: float) -> np.ndarray:
    return np.sqrt(v_bar**2 + v0**2 * np.tanh(k_eff * radius / R_S_KPC))


def standardized_residuals(
    parameters: np.ndarray,
    radius: np.ndarray,
    v_bar: np.ndarray,
    observed: np.ndarray,
    uncertainty: np.ndarray,
) -> np.ndarray:
    v0, k_eff = float(parameters[0]), float(parameters[1])
    return (model_vector(radius, v_bar, v0, k_eff) - observed) / uncertainty


def scalar_model(radius: float, v_bar: float, v0: float, k_eff: float) -> float:
    return math.sqrt(v_bar * v_bar + v0 * v0 * math.tanh(k_eff * radius / R_S_KPC))


def direct_scalar_chi2(
    radius: np.ndarray,
    v_bar: np.ndarray,
    observed: np.ndarray,
    uncertainty: np.ndarray,
    v0: float,
    k_eff: float,
) -> tuple[float, list[float]]:
    residuals: list[float] = []
    total = 0.0
    for r, vb, vo, sigma in zip(radius, v_bar, observed, uncertainty):
        model = scalar_model(float(r), float(vb), v0, k_eff)
        residual = model - float(vo)
        residuals.append(residual)
        total += (residual / float(sigma)) ** 2
    return total, residuals


def region_mask(radius: np.ndarray, name: str) -> np.ndarray:
    if name == "inner":
        return radius <= 5.0
    if name == "transition":
        return (radius > 5.0) & (radius <= 15.0)
    if name == "outer":
        return radius > 15.0
    raise KeyError(name)


def region_metrics(radius: np.ndarray, residual: np.ndarray, uncertainty: np.ndarray) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for name, _, _, _ in REGIONS:
        mask = region_mask(radius, name)
        rr = residual[mask]
        ss = uncertainty[mask]
        weights = 1.0 / ss**2
        output[name] = {
            "count": int(mask.sum()),
            "radius_min": float(radius[mask].min()),
            "radius_max": float(radius[mask].max()),
            "chi2_contribution": float(np.sum((rr / ss) ** 2)),
            "rmse_km_s": float(np.sqrt(np.mean(rr**2))),
            "weighted_rmse_km_s": float(np.sqrt(np.sum(weights * rr**2) / np.sum(weights))),
            "mean_residual_km_s": float(np.mean(rr)),
            "max_abs_residual_km_s": float(np.max(np.abs(rr))),
        }
    return output


def metrics(
    radius: np.ndarray,
    observed: np.ndarray,
    uncertainty: np.ndarray,
    fitted: np.ndarray,
    parameter_count: int,
) -> dict[str, Any]:
    residual = fitted - observed
    weights = 1.0 / uncertainty**2
    chi2 = float(np.sum((residual / uncertainty) ** 2))
    dof = int(len(radius) - parameter_count)
    return {
        "N": int(len(radius)),
        "parameter_count": int(parameter_count),
        "chi2": chi2,
        "degrees_of_freedom": dof,
        "reduced_chi2": float(chi2 / dof),
        "rmse_km_s": float(np.sqrt(np.mean(residual**2))),
        "weighted_rmse_km_s": float(np.sqrt(np.sum(weights * residual**2) / np.sum(weights))),
        "standardized_rmse": float(np.sqrt(np.mean((residual / uncertainty) ** 2))),
        "max_abs_residual_km_s": float(np.max(np.abs(residual))),
        "aic_common_constant_omitted": float(chi2 + 2.0 * parameter_count),
        "regions": region_metrics(radius, residual, uncertainty),
    }


def boundary_contact(v0: float, k_eff: float) -> dict[str, bool]:
    v0_tolerance = BOUNDARY_FRACTION * (V0_BOUNDS[1] - V0_BOUNDS[0])
    k_tolerance = BOUNDARY_FRACTION * (K_BOUNDS[1] - K_BOUNDS[0])
    return {
        "V0_lower": abs(v0 - V0_BOUNDS[0]) <= v0_tolerance,
        "V0_upper": abs(v0 - V0_BOUNDS[1]) <= v0_tolerance,
        "k_eff_lower": abs(k_eff - K_BOUNDS[0]) <= k_tolerance,
        "k_eff_upper": abs(k_eff - K_BOUNDS[1]) <= k_tolerance,
    }


def covariance_receipt(jacobian: np.ndarray, reduced_chi2: float) -> dict[str, Any]:
    singular_values = np.linalg.svd(jacobian, compute_uv=False)
    rank = int(np.linalg.matrix_rank(jacobian))
    condition_number = float(singular_values[0] / singular_values[-1]) if singular_values[-1] > 0 else math.inf
    jtj = jacobian.T @ jacobian
    if rank != jacobian.shape[1] or not np.all(np.isfinite(jtj)):
        return {
            "identifiable": False,
            "rank": rank,
            "singular_values": singular_values.tolist(),
            "condition_number": condition_number,
            "unscaled_covariance": None,
            "scaled_covariance": None,
            "parameter_correlation": None,
        }
    unscaled = np.linalg.inv(jtj)
    scaled = unscaled * reduced_chi2
    denom = math.sqrt(float(scaled[0, 0] * scaled[1, 1]))
    correlation = float(scaled[0, 1] / denom) if denom > 0 else math.nan
    return {
        "identifiable": bool(np.all(np.isfinite(unscaled)) and np.all(np.isfinite(scaled)) and math.isfinite(correlation)),
        "rank": rank,
        "singular_values": singular_values.tolist(),
        "condition_number": condition_number,
        "unscaled_covariance": unscaled.tolist(),
        "scaled_covariance": scaled.tolist(),
        "scaled_standard_errors": np.sqrt(np.diag(scaled)).tolist(),
        "parameter_correlation": correlation,
    }


def json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    data, headers, payload = parse_data(args.data)
    radius = data[:, 0]
    observed = data[:, 1]
    uncertainty = data[:, 2]
    v_bar = baryonic_literal(data)

    starts: list[dict[str, Any]] = []
    solver_results: list[Any] = []
    for v0_start, k_start in itertools.product(V0_STARTS, K_STARTS):
        result = least_squares(
            standardized_residuals,
            x0=np.asarray([v0_start, k_start], dtype=np.float64),
            bounds=(np.asarray([V0_BOUNDS[0], K_BOUNDS[0]]), np.asarray([V0_BOUNDS[1], K_BOUNDS[1]])),
            args=(radius, v_bar, observed, uncertainty),
            method="trf",
            jac="2-point",
            xtol=1.0e-12,
            ftol=1.0e-12,
            gtol=1.0e-12,
            max_nfev=100000,
            loss="linear",
        )
        curve = model_vector(radius, v_bar, float(result.x[0]), float(result.x[1]))
        chi2 = float(np.sum(standardized_residuals(result.x, radius, v_bar, observed, uncertainty) ** 2))
        starts.append(
            {
                "initial": {"V0_km_s": v0_start, "k_eff": k_start},
                "success": bool(result.success),
                "status": int(result.status),
                "message": str(result.message),
                "V0_km_s": float(result.x[0]),
                "k_eff": float(result.x[1]),
                "chi2": chi2,
                "cost": float(result.cost),
                "optimality": float(result.optimality),
                "nfev": int(result.nfev),
                "njev": int(result.njev) if result.njev is not None else None,
                "active_mask": result.active_mask.tolist(),
                "curve_km_s": curve.tolist(),
            }
        )
        solver_results.append(result)

    successful_indices = [index for index, item in enumerate(starts) if item["success"] and math.isfinite(item["chi2"])]
    if not successful_indices:
        raise RuntimeError("No successful finite fit")
    best_index = min(successful_indices, key=lambda index: starts[index]["chi2"])
    best_result = solver_results[best_index]
    best = starts[best_index]
    best_curve = np.asarray(best["curve_km_s"], dtype=np.float64)

    curve_differences = []
    for index in successful_indices:
        curve = np.asarray(starts[index]["curve_km_s"], dtype=np.float64)
        curve_differences.append(float(np.max(np.abs(curve - best_curve))))
    max_curve_difference = max(curve_differences)
    all_starts_converged = len(successful_indices) == len(starts)
    all_curves_equivalent = max_curve_difference <= CURVE_EQUIVALENCE_TOLERANCE_KMS

    v0_best = float(best["V0_km_s"])
    k_best = float(best["k_eff"])
    model_metrics = metrics(radius, observed, uncertainty, best_curve, 2)
    null_metrics = metrics(radius, observed, uncertainty, v_bar, 0)
    direct_chi2, direct_residuals = direct_scalar_chi2(radius, v_bar, observed, uncertainty, v0_best, k_best)
    vector_residuals = best_curve - observed
    direct_chi2_difference = abs(direct_chi2 - model_metrics["chi2"])
    direct_residual_difference = float(np.max(np.abs(np.asarray(direct_residuals) - vector_residuals)))

    boundaries = boundary_contact(v0_best, k_best)
    no_boundary_contact = not any(boundaries.values())
    covariance = covariance_receipt(np.asarray(best_result.jac, dtype=np.float64), model_metrics["reduced_chi2"])

    delta_aic = float(null_metrics["aic_common_constant_omitted"] - model_metrics["aic_common_constant_omitted"])
    chi2_fraction = float(model_metrics["chi2"] / null_metrics["chi2"])
    materially_improves = delta_aic >= MATERIAL_DELTA_AIC and chi2_fraction <= MATERIAL_CHI2_FRACTION
    public_difference = abs(model_metrics["reduced_chi2"] - PUBLIC_REDUCED_CHI2)
    public_window_match = public_difference <= PUBLIC_WINDOW
    stable_finite = all_starts_converged and all_curves_equivalent and math.isfinite(model_metrics["chi2"])

    ambiguity = {
        "present": True,
        "items": [
            "The public literal squaring convention may not match signed-gas SPARC use.",
            "The public fit's stellar mass-to-light convention is not fully recovered.",
            "The public fit's exclusion and covariance policies are not fully recovered.",
        ],
    }

    if stable_finite and no_boundary_contact and public_window_match:
        classification = "public_metric_reproduced"
    elif stable_finite and materially_improves and not public_window_match and ambiguity["present"]:
        classification = "functional_benchmark_reproduced_but_public_metric_differs"
    elif not all_curves_equivalent:
        classification = "inconclusive"
    else:
        classification = "not_reproduced_under_declared_conditions"

    rows = []
    for index in range(len(radius)):
        rows.append(
            {
                "radius_kpc": float(radius[index]),
                "Vobs_km_s": float(observed[index]),
                "errV_km_s": float(uncertainty[index]),
                "Vbar_literal_km_s": float(v_bar[index]),
                "Vmodel_km_s": float(best_curve[index]),
                "model_residual_km_s": float(best_curve[index] - observed[index]),
                "model_standardized_residual": float((best_curve[index] - observed[index]) / uncertainty[index]),
                "null_residual_km_s": float(v_bar[index] - observed[index]),
            }
        )

    output = {
        "schema_version": "0.1.0",
        "scope": "B2 literal public-formula NGC 3198 fit only",
        "input": {
            "path": str(args.data),
            "sha256": sha256_bytes(payload),
            "headers": headers,
            "columns": list(EXPECTED_COLUMNS),
            "N": int(len(data)),
        },
        "model": {
            "baryonic_convention": "sqrt(Vgas^2 + Vdisk^2 + Vbul^2)",
            "formula": "sqrt(Vbar^2 + V0^2*tanh(k_eff*r/r_s))",
            "fixed_r_s_kpc": R_S_KPC,
            "bounds": {"V0_km_s": list(V0_BOUNDS), "k_eff": list(K_BOUNDS)},
            "starts": {"V0_km_s": list(V0_STARTS), "k_eff": list(K_STARTS)},
        },
        "solver": {
            "library": "scipy.optimize.least_squares",
            "method": "trf",
            "jacobian": "2-point",
            "loss": "linear",
            "xtol": 1.0e-12,
            "ftol": 1.0e-12,
            "gtol": 1.0e-12,
            "max_nfev": 100000,
        },
        "best_fit": {
            "start_index": best_index,
            "V0_km_s": v0_best,
            "k_eff": k_best,
            "transition_scale_r_s_over_k_eff_kpc": float(R_S_KPC / k_best),
            "half_saturation_radius_kpc": float(R_S_KPC * math.atanh(0.5) / k_best),
            "metrics": model_metrics,
            "boundary_contact": boundaries,
            "covariance": covariance,
        },
        "baryonic_null": {"metrics": null_metrics},
        "comparison": {
            "delta_aic_null_minus_model": delta_aic,
            "chi2_model_over_null": chi2_fraction,
            "materially_improves": materially_improves,
            "public_target_reduced_chi2": PUBLIC_REDUCED_CHI2,
            "public_window": PUBLIC_WINDOW,
            "absolute_public_metric_difference": public_difference,
            "public_window_match": public_window_match,
            "public_convention_ambiguity": ambiguity,
        },
        "multistart": {
            "count": len(starts),
            "converged_count": len(successful_indices),
            "all_starts_converged": all_starts_converged,
            "curve_equivalence_tolerance_km_s": CURVE_EQUIVALENCE_TOLERANCE_KMS,
            "max_curve_difference_km_s": max_curve_difference,
            "all_curves_equivalent": all_curves_equivalent,
            "starts": starts,
        },
        "independent_checks": {
            "direct_scalar_chi2": direct_chi2,
            "vector_chi2": model_metrics["chi2"],
            "absolute_chi2_difference": direct_chi2_difference,
            "max_abs_residual_difference_km_s": direct_residual_difference,
            "chi2_matches": direct_chi2_difference <= 1.0e-10,
            "residuals_match": direct_residual_difference <= 1.0e-12,
        },
        "regional_boundaries": {
            "inner": "r <= 5.0 kpc",
            "transition": "5.0 < r <= 15.0 kpc",
            "outer": "r > 15.0 kpc",
        },
        "rows": rows,
        "classification": classification,
        "anti_cheat": {
            "private_tolog_document_used": False,
            "tolog_code_copied": False,
            "post_hoc_radial_exclusion": False,
            "post_result_parameter_bound_tuning": False,
            "production_lineum_code_imported_or_modified": False,
            "lineum_emergence_claimed": False,
        },
        "environment": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "platform": platform.platform(),
            "machine": platform.machine(),
        },
    }

    rendered = json.dumps(json_safe(output), indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
