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

SCHEMA = "lineum-b4-q2-ledger-neutral-control/1"
STAGE = "Q2-PV1-B"
CANONICAL_RUNNER_GIT_BLOB = "1598faf0f39e056c1684f767c2554edc63283ca4"
PV1_RUNNER_GIT_BLOB = "e3657119b855965b4fd622b3e94f08443a7c9107"
PV1_PRIMARY_GIT_BLOB = "7a7ce23471d51d9b2244256387934658b12e1f52"
PV1_CHECKER_GIT_BLOB = "c459e4a1f947aba55d01f8f30bc1aa6bae88076f"
INNER_FACTOR = 1.5
NUMERIC_RTOL = 1e-10


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load_sources() -> tuple[Any, Any]:
    here = Path(__file__).resolve().parent
    l1 = _load_module(
        "lineum_b4_q2_pv1b_canonical_l1",
        here / "lineum_b4_saturation_localized_l1.py",
    )
    pv1 = _load_module(
        "lineum_b4_q2_pv1b_audit",
        here / "lineum_b4_q2_perturbation_ledger.py",
    )
    return l1, pv1


def _energy_parts(psi: np.ndarray, radius: np.ndarray) -> tuple[float, float, float]:
    energy = np.abs(psi) ** 2
    inner = radius <= 2.0
    annulus = (radius >= 3.0) & (radius <= 5.0)
    outer = ~(inner | annulus)
    return (
        float(np.sum(energy[inner])),
        float(np.sum(energy[annulus])),
        float(np.sum(energy[outer])),
    )


def apply_balanced_perturbation(
    psi: np.ndarray,
    radius: np.ndarray,
    *,
    factor: float,
) -> np.ndarray:
    result = np.array(psi, copy=True)
    result[radius <= 2.0] *= INNER_FACTOR
    annulus = (radius >= 3.0) & (radius <= 5.0)
    result[annulus] *= factor
    return result


def perturbation_ledger_receipt(
    psi_before: np.ndarray,
    phi_before: np.ndarray,
    psi_after: np.ndarray,
) -> dict[str, Any]:
    epsi_before = float(np.sum(np.abs(psi_before) ** 2))
    epsi_after = float(np.sum(np.abs(psi_after) ** 2))
    pphi = float(np.sum(phi_before))
    ledger_before = epsi_before + pphi
    ledger_after = epsi_after + pphi
    delta = ledger_after - ledger_before
    tolerance = NUMERIC_RTOL * max(1.0, abs(ledger_before))
    return {
        "epsi_before": epsi_before,
        "epsi_after": epsi_after,
        "pphi_unchanged": pphi,
        "ledger_before": ledger_before,
        "ledger_after": ledger_after,
        "delta_ledger": delta,
        "ledger_tolerance": tolerance,
        "neutral_within_numeric_tolerance": bool(abs(delta) <= tolerance),
    }


def q2_admissible_full_recovery(row: dict[str, Any]) -> bool:
    return bool(
        row["full_recovery"]
        and row["finite"]
        and row["reset_free"]
        and row["primary_psi_cap_hits"] == 0
        and row["recovery_psi_cap_hits"] == 0
        and row["primary_phi_cap_hits"] == 0
        and row["recovery_phi_cap_hits"] == 0
    )


def compare_control(canonical: dict[str, Any], balanced: dict[str, Any] | None) -> str:
    if balanced is None:
        return "control_unavailable"
    canonical_pass = q2_admissible_full_recovery(canonical)
    balanced_pass = q2_admissible_full_recovery(balanced)
    if not canonical_pass and balanced_pass:
        return "balanced_rescues_q2_classification"
    if canonical_pass and not balanced_pass:
        return "balanced_breaks_q2_classification"
    if canonical_pass and balanced_pass:
        return "both_q2_positive"
    return "both_q2_negative"


def _evolve_primary(l1: Any, stencil: str) -> dict[str, Any]:
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
    energies = np.empty((l1.STEPS, batch_size))
    phi_means = np.empty((l1.STEPS, batch_size))

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
            energies[step_index] = np.mean(np.abs(psi) ** 2, axis=(1, 2))
            phi_means[step_index] = np.mean(phi, axis=(1, 2))

    pre = [l1.spatial_metrics(psi[index], phi[index]) for index in range(batch_size)]
    tail_count = max(10, l1.STEPS // 5)
    phi_slopes = l1.slope_rows(phi_means[-tail_count:])
    phi_tail_means = phi_means[-tail_count:].mean(axis=0)

    return {
        "specs": specs,
        "psi": psi,
        "phi": phi,
        "kappa": kappa,
        "mu": mu,
        "lane_arrays": lane_arrays,
        "resets": resets,
        "psi_cap_hits": psi_cap_hits,
        "phi_cap_hits": phi_cap_hits,
        "active": active,
        "failure_step": failure_step,
        "failure_stage": failure_stage,
        "failure_reason": failure_reason,
        "pre": pre,
        "phi_slopes": phi_slopes,
        "phi_tail_means": phi_tail_means,
    }


def _run_recovery_branch(
    l1: Any,
    primary: dict[str, Any],
    stencil: str,
    psi_start: np.ndarray,
    branch_active: np.ndarray,
) -> list[dict[str, Any]]:
    psi = np.array(psi_start, copy=True)
    phi = np.array(primary["phi"], copy=True)
    active = np.array(branch_active, copy=True)
    last_finite_psi = psi.copy()
    last_finite_phi = phi.copy()
    failure_step = np.array(primary["failure_step"], copy=True)
    failure_stage = list(primary["failure_stage"])
    failure_reason = list(primary["failure_reason"])
    recovery_resets = np.zeros(psi.shape[0], dtype=int)
    recovery_psi_cap_hits = np.zeros(psi.shape[0], dtype=int)
    recovery_phi_cap_hits = np.zeros(psi.shape[0], dtype=int)
    recovery_steps_completed = np.zeros(psi.shape[0], dtype=int)

    with np.errstate(all="ignore"):
        for recovery_index in range(l1.RECOVERY_STEPS):
            active_before = active.copy()
            psi, phi, reset_rows, cap_rows, phi_cap_rows = l1.advance_batch_one_step(
                psi,
                phi,
                primary["kappa"],
                primary["mu"],
                stencil,
                primary["lane_arrays"],
                active,
            )
            recovery_resets += reset_rows
            recovery_psi_cap_hits += cap_rows
            recovery_phi_cap_hits += phi_cap_rows
            psi, phi, newly_bad = l1._mark_failures(
                psi,
                phi,
                active,
                last_finite_psi,
                last_finite_phi,
                failure_step,
                failure_stage,
                failure_reason,
                recovery_index + 1,
                "recovery",
            )
            completed_now = active_before & ~newly_bad
            recovery_steps_completed[completed_now] = recovery_index + 1

    post = [l1.spatial_metrics(psi[index], phi[index]) for index in range(psi.shape[0])]
    rows: list[dict[str, Any]] = []
    for index, (lane, phi0) in enumerate(primary["specs"]):
        pre = primary["pre"][index]
        energy_error = abs(post[index]["total_energy"] - pre["total_energy"]) / (
            abs(pre["total_energy"]) + 1e-30
        )
        energy_profile_error = l1.relative_l2(
            pre["energy_radial_profile"], post[index]["energy_radial_profile"]
        )
        phi_profile_error = l1.relative_l2(
            pre["phi_radial_profile"], post[index]["phi_radial_profile"]
        )
        half_radius_error = abs(
            post[index]["half_energy_radius"] - pre["half_energy_radius"]
        )
        finite = failure_reason[index] is None
        reset_free = bool(primary["resets"][index] + recovery_resets[index] == 0)
        psi_recovery = bool(
            finite
            and reset_free
            and energy_error <= 0.05
            and energy_profile_error <= 0.10
            and half_radius_error <= 1.0
            and post[index]["center_displacement"] <= 0.5
        )
        phi_stationary_threshold = max(
            1e-10, 1e-8 * abs(primary["phi_tail_means"][index])
        )
        phi_one_sided_stationary = bool(
            primary["phi_slopes"][index] <= phi_stationary_threshold
        )
        full_recovery = bool(
            psi_recovery
            and primary["phi_cap_hits"][index] + recovery_phi_cap_hits[index] == 0
            and phi_profile_error <= 0.10
            and phi_one_sided_stationary
        )
        rows.append(
            {
                "case_key": f"{stencil}|{lane.name}|phi0={float(phi0):.1f}",
                "stencil": stencil,
                "lane": lane.name,
                "phi0": float(phi0),
                "finite": finite,
                "reset_free": reset_free,
                "primary_resets": int(primary["resets"][index]),
                "recovery_resets": int(recovery_resets[index]),
                "primary_psi_cap_hits": int(primary["psi_cap_hits"][index]),
                "recovery_psi_cap_hits": int(recovery_psi_cap_hits[index]),
                "primary_phi_cap_hits": int(primary["phi_cap_hits"][index]),
                "recovery_phi_cap_hits": int(recovery_phi_cap_hits[index]),
                "recovery_steps_completed": int(recovery_steps_completed[index]),
                "energy_error": float(energy_error),
                "energy_profile_error": float(energy_profile_error),
                "phi_profile_error": float(phi_profile_error),
                "half_energy_radius_error": float(half_radius_error),
                "center_displacement": float(post[index]["center_displacement"]),
                "psi_recovery": psi_recovery,
                "phi_one_sided_stationary": phi_one_sided_stationary,
                "full_recovery": full_recovery,
            }
        )
    return rows


def run_stencil(l1: Any, pv1: Any, stencil: str) -> list[dict[str, Any]]:
    primary = _evolve_primary(l1, stencil)
    batch_size = len(primary["specs"])

    canonical_psi = np.array(primary["psi"], copy=True)
    balanced_psi = np.array(primary["psi"], copy=True)
    balanced_available = np.zeros(batch_size, dtype=bool)
    factors: list[float | None] = [None] * batch_size
    perturbation_receipts: list[dict[str, Any] | None] = [None] * batch_size

    inner = l1.RADIUS <= 2.0
    annulus = (l1.RADIUS >= 3.0) & (l1.RADIUS <= 5.0)
    canonical_psi[:, inner] *= np.where(primary["active"][:, None], 1.5, 1.0)
    canonical_psi[:, annulus] *= np.where(primary["active"][:, None], 0.5, 1.0)

    for index in range(batch_size):
        if not bool(primary["active"][index]):
            continue
        e_inner, e_annulus, _ = _energy_parts(primary["psi"][index], l1.RADIUS)
        factor = pv1.balanced_annulus_factor(e_inner, e_annulus)
        factors[index] = factor
        if factor is None:
            continue
        candidate = apply_balanced_perturbation(
            primary["psi"][index], l1.RADIUS, factor=factor
        )
        receipt = perturbation_ledger_receipt(
            primary["psi"][index], primary["phi"][index], candidate
        )
        perturbation_receipts[index] = receipt
        balanced_psi[index] = candidate
        balanced_available[index] = True

    canonical_rows = _run_recovery_branch(
        l1, primary, stencil, canonical_psi, np.array(primary["active"], copy=True)
    )
    balanced_rows = _run_recovery_branch(
        l1, primary, stencil, balanced_psi, balanced_available
    )

    rows: list[dict[str, Any]] = []
    for index, (lane, phi0) in enumerate(primary["specs"]):
        balanced_row = balanced_rows[index] if balanced_available[index] else None
        rows.append(
            {
                "case_key": f"{stencil}|{lane.name}|phi0={float(phi0):.1f}",
                "active_before_perturbation": bool(primary["active"][index]),
                "balanced_annulus_factor": factors[index],
                "control_available": bool(balanced_available[index]),
                "perturbation_ledger": perturbation_receipts[index],
                "canonical": canonical_rows[index],
                "balanced": balanced_row,
                "comparison": compare_control(canonical_rows[index], balanced_row),
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
    l1, pv1 = _load_sources()
    rows: list[dict[str, Any]] = []
    for stencil in l1.STENCILS:
        rows.extend(run_stencil(l1, pv1, stencil))

    available = [row for row in rows if row["control_available"]]
    unavailable = [row for row in rows if not row["control_available"]]
    neutral_failures = [
        row["case_key"]
        for row in available
        if not row["perturbation_ledger"]["neutral_within_numeric_tolerance"]
    ]
    canonical_positive = sum(
        q2_admissible_full_recovery(row["canonical"]) for row in rows
    )
    balanced_positive = sum(
        q2_admissible_full_recovery(row["balanced"])
        for row in available
        if row["balanced"] is not None
    )
    rescued = [
        row["case_key"]
        for row in available
        if row["comparison"] == "balanced_rescues_q2_classification"
    ]
    changed = [
        row["case_key"]
        for row in available
        if row["comparison"]
        in {"balanced_rescues_q2_classification", "balanced_breaks_q2_classification"}
    ]

    if len(rows) != 28 or neutral_failures:
        outcome = "technical_or_methodological_failure"
    elif rescued:
        outcome = "ledger_neutral_control_rescues_q2_classification"
    else:
        outcome = "ledger_neutral_control_does_not_rescue_q2_classification"

    factors = [row["balanced_annulus_factor"] for row in available]
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "stage": STAGE,
        "status": "primary_pending_independent_check",
        "source_binding": {
            "canonical_localized_runner_git_blob": CANONICAL_RUNNER_GIT_BLOB,
            "q2_pv1_runner_git_blob": PV1_RUNNER_GIT_BLOB,
            "q2_pv1_primary_git_blob": PV1_PRIMARY_GIT_BLOB,
            "q2_pv1_checker_git_blob": PV1_CHECKER_GIT_BLOB,
        },
        "protocol": {
            "grid_size": int(l1.GRID_SIZE),
            "primary_steps": int(l1.STEPS),
            "recovery_steps": int(l1.RECOVERY_STEPS),
            "stencils": list(l1.STENCILS),
            "phi0_values": [float(value) for value in l1.PHI0_VALUES],
            "lane_names": [lane.name for lane in l1.LANES],
            "inner_radius_max": 2.0,
            "annulus_radius_min": 3.0,
            "annulus_radius_max": 5.0,
            "inner_factor": INNER_FACTOR,
            "balanced_formula": "sqrt(1 - 1.25 * E_inner / E_annulus)",
            "unavailable_rule": "E_annulus <= 0 or b_squared < 0; no clipping, abs, tuning, or alternate formula",
            "recovery_observer": "exact frozen localized-L1 recovery metrics and thresholds",
            "q2_admissibility": "full recovery plus finite/reset-free and zero psi/phi cap contacts",
        },
        "summary": {
            "case_count": len(rows),
            "control_available_count": len(available),
            "control_unavailable_count": len(unavailable),
            "control_unavailable_keys": [row["case_key"] for row in unavailable],
            "neutral_perturbation_failure_count": len(neutral_failures),
            "neutral_perturbation_failures": neutral_failures,
            "balanced_annulus_factor_min": None if not factors else float(min(factors)),
            "balanced_annulus_factor_max": None if not factors else float(max(factors)),
            "canonical_q2_positive_count": int(canonical_positive),
            "balanced_q2_positive_count": int(balanced_positive),
            "q2_classification_changed_count": len(changed),
            "q2_classification_changed_keys": changed,
            "balanced_rescue_count": len(rescued),
            "balanced_rescue_keys": rescued,
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
    parser = argparse.ArgumentParser(
        description="Run the preregistered B4 Q2 ledger-neutral radial control."
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload["summary"], sort_keys=True))
    return 0 if payload["summary"]["outcome"] != "technical_or_methodological_failure" else 2


if __name__ == "__main__":
    raise SystemExit(main())
