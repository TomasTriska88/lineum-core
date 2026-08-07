from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import platform
import sys
from pathlib import Path
from typing import Any, Sequence

import numpy as np

SCHEMA = "lineum-b4-q2-perturbation-ledger/1"
STAGE = "Q2-PV1-A"
CANONICAL_RUNNER_GIT_BLOB = "1598faf0f39e056c1684f767c2554edc63283ca4"
CANONICAL_RUNNER_SHA256 = "96153e37b4e10890d3a0ab52e9463153cfc614eb9a2f1fcc58f23baeafc988bd"
CORE_MATH_GIT_BLOB = "bb877021810691223a0eb960a45493a2e351112a"
INNER_FACTOR = 1.5
ANNULUS_FACTOR = 0.5
NUMERIC_RTOL = 1e-10
RECOVERY_ENERGY_TOLERANCE = 0.05


def analytic_delta(e_inner: float, e_annulus: float, *, active: bool) -> float:
    if not active:
        return 0.0
    return (INNER_FACTOR**2 - 1.0) * e_inner + (
        ANNULUS_FACTOR**2 - 1.0
    ) * e_annulus


def analytic_tolerance(direct_delta: float, analytic_value: float) -> float:
    return NUMERIC_RTOL * max(1.0, abs(direct_delta), abs(analytic_value))


def ledger_tolerance(ledger_before: float) -> float:
    return NUMERIC_RTOL * max(1.0, abs(ledger_before))


def balanced_annulus_factor(e_inner: float, e_annulus: float) -> float | None:
    if not math.isfinite(e_inner) or not math.isfinite(e_annulus) or e_annulus <= 0.0:
        return None
    b_squared = 1.0 - (INNER_FACTOR**2 - 1.0) * e_inner / e_annulus
    if not math.isfinite(b_squared) or b_squared < 0.0:
        return None
    return math.sqrt(b_squared)


def expected_case_keys(
    lane_names: Sequence[str],
    phi0_values: Sequence[float],
    stencils: Sequence[str],
) -> list[str]:
    return [
        f"{stencil}|{lane_name}|phi0={float(phi0):.1f}"
        for stencil in stencils
        for lane_name in lane_names
        for phi0 in phi0_values
    ]


def apply_canonical_perturbation(
    psi: np.ndarray, radius: np.ndarray, *, active: bool
) -> np.ndarray:
    result = np.array(psi, copy=True)
    if not active:
        return result
    result[radius <= 2.0] *= INNER_FACTOR
    annulus = (radius >= 3.0) & (radius <= 5.0)
    result[annulus] *= ANNULUS_FACTOR
    return result


def audit_state(
    psi: np.ndarray,
    phi: np.ndarray,
    radius: np.ndarray,
    *,
    active: bool,
) -> dict[str, Any]:
    energy = np.abs(psi) ** 2
    inner = radius <= 2.0
    annulus = (radius >= 3.0) & (radius <= 5.0)
    outer = ~(inner | annulus)

    e_inner = float(np.sum(energy[inner]))
    e_annulus = float(np.sum(energy[annulus]))
    e_outer = float(np.sum(energy[outer]))
    epsi_before = float(np.sum(energy))
    pphi_before = float(np.sum(phi))
    ledger_before = epsi_before + pphi_before

    psi_after = apply_canonical_perturbation(psi, radius, active=active)
    epsi_after = float(np.sum(np.abs(psi_after) ** 2))
    pphi_after = float(np.sum(phi))
    ledger_after = epsi_after + pphi_after

    direct_delta_epsi = epsi_after - epsi_before
    direct_delta_phi = pphi_after - pphi_before
    direct_delta_ledger = ledger_after - ledger_before
    analytic_value = analytic_delta(e_inner, e_annulus, active=active)
    discrepancy = direct_delta_epsi - analytic_value
    tolerance = analytic_tolerance(direct_delta_epsi, analytic_value)
    analytic_agreement = bool(abs(discrepancy) <= tolerance)

    if active:
        neutral = bool(abs(direct_delta_ledger) <= ledger_tolerance(ledger_before))
    else:
        neutral = None

    relative_epsi = direct_delta_epsi / max(abs(epsi_before), 1e-30)
    relative_ledger = direct_delta_ledger / max(abs(ledger_before), 1e-30)
    tolerance_fraction = abs(relative_epsi) / RECOVERY_ENERGY_TOLERANCE

    return {
        "applicability": "perturbed_active" if active else "not_applicable_inactive",
        "e_inner": e_inner,
        "e_annulus": e_annulus,
        "e_outer": e_outer,
        "epsi_before": epsi_before,
        "pphi_before": pphi_before,
        "ledger_before": ledger_before,
        "epsi_after": epsi_after,
        "pphi_after": pphi_after,
        "ledger_after": ledger_after,
        "direct_delta_epsi": direct_delta_epsi,
        "direct_delta_phi": direct_delta_phi,
        "direct_delta_ledger": direct_delta_ledger,
        "relative_delta_epsi": relative_epsi,
        "relative_delta_ledger": relative_ledger,
        "absolute_relative_epsi_shift_over_frozen_5pct_tolerance": tolerance_fraction,
        "analytic_delta_epsi": analytic_value,
        "analytic_direct_discrepancy": discrepancy,
        "analytic_tolerance": tolerance,
        "analytic_agreement": analytic_agreement,
        "ledger_neutrality_tolerance": ledger_tolerance(ledger_before),
        "ledger_neutral_within_numeric_tolerance": neutral,
        "conditional_balanced_annulus_factor": balanced_annulus_factor(
            e_inner, e_annulus
        ),
    }


def _load_canonical_runner() -> Any:
    path = Path(__file__).with_name("lineum_b4_saturation_localized_l1.py")
    spec = importlib.util.spec_from_file_location("lineum_b4_q2_pv1_canonical_l1", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load canonical runner from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _run_primary_states(l1: Any, stencil: str) -> list[dict[str, Any]]:
    specs = [(lane, phi0) for lane in l1.LANES for phi0 in l1.PHI0_VALUES]
    batch_size = len(specs)
    psi = np.stack([l1.GAUSSIAN.copy() for _ in specs])
    phi = np.stack(
        [
            np.full((l1.GRID_SIZE, l1.GRID_SIZE), phi0, dtype=float)
            for _, phi0 in specs
        ]
    )
    kappa = np.ones((batch_size, l1.GRID_SIZE, l1.GRID_SIZE))
    mu = np.zeros_like(kappa)
    lane_arrays = l1.build_lane_arrays(specs)

    resets = np.zeros(batch_size, dtype=int)
    psi_cap_hits = np.zeros(batch_size, dtype=int)
    phi_cap_hits = np.zeros(batch_size, dtype=int)
    active = np.ones(batch_size, dtype=bool)
    failure_step = np.full(batch_size, -1, dtype=int)
    failure_stage: list[str | None] = [None] * batch_size
    failure_reason: list[str | None] = [None] * batch_size
    last_finite_psi = psi.copy()
    last_finite_phi = phi.copy()

    with np.errstate(all="ignore"):
        for step_index in range(l1.STEPS):
            psi, phi, reset_rows, cap_rows, phi_cap_rows = l1.advance_batch_one_step(
                psi, phi, kappa, mu, stencil, lane_arrays, active
            )
            resets += reset_rows
            psi_cap_hits += cap_rows
            phi_cap_hits += phi_cap_rows
            psi, phi, _ = l1._mark_failures(
                psi,
                phi,
                active,
                last_finite_psi,
                last_finite_phi,
                failure_step,
                failure_stage,
                failure_reason,
                step_index + 1,
                "primary",
            )

    rows: list[dict[str, Any]] = []
    for index, (lane, phi0) in enumerate(specs):
        active_before = bool(active[index])
        audit = audit_state(
            psi[index],
            phi[index],
            l1.RADIUS,
            active=active_before,
        )
        rows.append(
            {
                "case_key": f"{stencil}|{lane.name}|phi0={float(phi0):.1f}",
                "stencil": stencil,
                "lane": lane.name,
                "phi0": float(phi0),
                "primary": {
                    "finite": bool(failure_reason[index] is None),
                    "active_before_perturbation": active_before,
                    "resets": int(resets[index]),
                    "psi_cap_hits": int(psi_cap_hits[index]),
                    "phi_cap_hits": int(phi_cap_hits[index]),
                    "failure_step": (
                        None
                        if failure_reason[index] is None
                        else int(failure_step[index])
                    ),
                    "failure_reason": failure_reason[index],
                },
                "audit": audit,
            }
        )
    return rows


def _canonical_payload_sha256(payload: dict[str, Any]) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def run() -> dict[str, Any]:
    l1 = _load_canonical_runner()
    rows: list[dict[str, Any]] = []
    for stencil in l1.STENCILS:
        rows.extend(_run_primary_states(l1, stencil))

    expected_keys = expected_case_keys(
        [lane.name for lane in l1.LANES], l1.PHI0_VALUES, l1.STENCILS
    )
    actual_keys = [row["case_key"] for row in rows]
    key_set_pass = len(rows) == 28 and set(actual_keys) == set(expected_keys)

    applicable = [row for row in rows if row["audit"]["applicability"] == "perturbed_active"]
    inactive = [row for row in rows if row["audit"]["applicability"] == "not_applicable_inactive"]
    analytic_pass = all(row["audit"]["analytic_agreement"] for row in rows)
    neutral_count = sum(
        row["audit"]["ledger_neutral_within_numeric_tolerance"] is True
        for row in applicable
    )
    nonneutral_count = sum(
        row["audit"]["ledger_neutral_within_numeric_tolerance"] is False
        for row in applicable
    )

    if not key_set_pass or not analytic_pass:
        outcome = "technical_or_methodological_failure"
    elif nonneutral_count > 0:
        outcome = "non_neutral_detected"
    else:
        outcome = "all_applicable_cases_neutral"

    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "stage": STAGE,
        "status": "primary_pending_independent_check",
        "source": {
            "canonical_localized_runner_git_blob": CANONICAL_RUNNER_GIT_BLOB,
            "canonical_localized_runner_sha256": CANONICAL_RUNNER_SHA256,
            "core_math_git_blob_at_preregistration": CORE_MATH_GIT_BLOB,
        },
        "protocol": {
            "grid_size": int(l1.GRID_SIZE),
            "primary_steps": int(l1.STEPS),
            "recovery_steps": 0,
            "stencils": list(l1.STENCILS),
            "phi0_values": [float(value) for value in l1.PHI0_VALUES],
            "lane_names": [lane.name for lane in l1.LANES],
            "noise_disabled": True,
            "inner_radius_max": 2.0,
            "annulus_radius_min": 3.0,
            "annulus_radius_max": 5.0,
            "inner_factor": INNER_FACTOR,
            "annulus_factor": ANNULUS_FACTOR,
            "numeric_rtol": NUMERIC_RTOL,
            "frozen_recovery_energy_tolerance": RECOVERY_ENERGY_TOLERANCE,
            "inactive_case_semantics": (
                "canonical perturbation is a no-op when the frozen runner marks a case "
                "inactive before perturbation; such rows remain in the 28-case key set "
                "but are not evidence for ledger neutrality"
            ),
        },
        "summary": {
            "case_count": len(rows),
            "key_set_pass": key_set_pass,
            "applicable_active_case_count": len(applicable),
            "inactive_not_applicable_case_count": len(inactive),
            "analytic_direct_all_pass": analytic_pass,
            "ledger_neutral_applicable_count": neutral_count,
            "ledger_non_neutral_applicable_count": nonneutral_count,
            "all_applicable_cases_neutral": bool(
                key_set_pass and analytic_pass and nonneutral_count == 0
            ),
            "outcome": outcome,
        },
        "rows": rows,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
    }
    payload["canonical_payload_sha256_without_self"] = _canonical_payload_sha256(payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the frozen B4 Q2-PV1-A audit.")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "stage": STAGE,
                "outcome": payload["summary"]["outcome"],
                "case_count": payload["summary"]["case_count"],
                "applicable_active_case_count": payload["summary"][
                    "applicable_active_case_count"
                ],
                "inactive_not_applicable_case_count": payload["summary"][
                    "inactive_not_applicable_case_count"
                ],
                "ledger_non_neutral_applicable_count": payload["summary"][
                    "ledger_non_neutral_applicable_count"
                ],
                "payload_sha256": payload["canonical_payload_sha256_without_self"],
            },
            sort_keys=True,
        )
    )
    return 0 if payload["summary"]["outcome"] != "technical_or_methodological_failure" else 2


if __name__ == "__main__":
    raise SystemExit(main())
