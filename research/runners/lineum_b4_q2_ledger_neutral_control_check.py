from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np

SCHEMA = "lineum-b4-q2-ledger-neutral-control-check/1"
STAGE = "Q2-PV1-B-CHECK"
PRIMARY_SCHEMA = "lineum-b4-q2-ledger-neutral-control/1"
PRIMARY_STAGE = "Q2-PV1-B"

GRID_SIZE = 32
DT = 1.0
PRIMARY_STEPS = 5000
RECOVERY_STEPS = 1000
SIGMA = 3.0
PHI0_VALUES = (0.0, 1.0)
STENCILS = ("LAP4", "LAP8")
PSI_CAP = 1e6
PHI_CAP = 1e6
INNER_FACTOR = 1.5
CANONICAL_ANNULUS_FACTOR = 0.5
LEDGER_RTOL = 1e-10
COMPARE_ATOL = 1e-8
COMPARE_RTOL = 1e-12

EXPECTED_CANONICAL_RUNNER_BLOB = "1598faf0f39e056c1684f767c2554edc63283ca4"
EXPECTED_PV1_RUNNER_BLOB = "e3657119b855965b4fd622b3e94f08443a7c9107"
EXPECTED_PV1_PRIMARY_BLOB = "7a7ce23471d51d9b2244256387934658b12e1f52"
EXPECTED_PV1_CHECKER_BLOB = "c459e4a1f947aba55d01f8f30bc1aa6bae88076f"
EXPECTED_PRIMARY_BLOB = "50d3f15d881e0665a450982053a9216f9cf5739c"
EXPECTED_REPORT_BLOB = "bab3f46f7dffa6f1242bcb27da1c6585fcb379b3"


@dataclass(frozen=True)
class Lane:
    name: str
    dissipation: float = 0.005
    use_tanh: bool = True
    use_denominator: bool = True
    use_mode_coupling: bool = True
    use_phi_cap: bool = True
    use_psi_guard: bool = True


LANES = (
    Lane("baseline"),
    Lane("no_hard_guards", use_phi_cap=False, use_psi_guard=False),
    Lane("no_linear_dissipation", dissipation=0.0),
    Lane("no_explicit_tanh", use_tanh=False),
    Lane("no_interaction_denominator", use_denominator=False),
    Lane("no_mode_coupling", use_mode_coupling=False),
    Lane("no_phi_cap", use_phi_cap=False),
)


def geometry() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    center = (GRID_SIZE - 1) / 2.0
    row, col = np.indices((GRID_SIZE, GRID_SIZE), dtype=float)
    radius = np.hypot(row - center, col - center)
    return row, col, radius


ROW, COL, RADIUS = geometry()
RADIAL_BINS = np.floor(RADIUS).astype(int)
RADIAL_BIN_COUNT = int(RADIAL_BINS.max()) + 1
_GAUSSIAN_RAW = np.exp(-(RADIUS**2) / (2.0 * SIGMA**2))
GAUSSIAN = (_GAUSSIAN_RAW / _GAUSSIAN_RAW.max()).astype(np.complex128)


def raw_laplacian(field: np.ndarray, stencil: str) -> np.ndarray:
    axial = (
        np.roll(field, 1, axis=1)
        + np.roll(field, -1, axis=1)
        + np.roll(field, 1, axis=2)
        + np.roll(field, -1, axis=2)
    )
    if stencil == "LAP4":
        return axial - 4.0 * field
    if stencil == "LAP8":
        diagonal = (
            np.roll(np.roll(field, 1, axis=1), 1, axis=2)
            + np.roll(np.roll(field, 1, axis=1), -1, axis=2)
            + np.roll(np.roll(field, -1, axis=1), 1, axis=2)
            + np.roll(np.roll(field, -1, axis=1), -1, axis=2)
        )
        return axial + 0.25 * diagonal - 5.0 * field
    raise ValueError(f"Unsupported stencil: {stencil}")


def lane_arrays(specs: list[tuple[Lane, float]]) -> dict[str, np.ndarray]:
    def col(values: Iterable[Any], dtype: Any) -> np.ndarray:
        return np.asarray(list(values), dtype=dtype)[:, None, None]

    return {
        "guard": col((lane.use_psi_guard for lane, _ in specs), bool),
        "phi_cap": col((lane.use_phi_cap for lane, _ in specs), bool),
        "tanh": col((lane.use_tanh for lane, _ in specs), bool),
        "denominator": col((lane.use_denominator for lane, _ in specs), bool),
        "mode": col((lane.use_mode_coupling for lane, _ in specs), bool),
        "dissipation": col((lane.dissipation for lane, _ in specs), float),
    }


def update_step(
    psi: np.ndarray,
    phi: np.ndarray,
    stencil: str,
    arrays: dict[str, np.ndarray],
    active: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    old_psi = psi.copy()
    old_phi = phi.copy()

    clipped_phi = np.clip(phi, 0.0, 10.0)
    raw = 0.04 * clipped_phi
    factor = np.where(arrays["tanh"], 0.1 * np.tanh(raw / 0.1), raw)
    interaction = factor * psi
    interaction = np.where(
        arrays["denominator"],
        interaction / (1.0 + np.abs(interaction) / 10.0),
        interaction,
    )

    grad_row, grad_col = np.gradient(phi, axis=(1, 2))
    flow = -0.004 * (grad_row + 1j * grad_col)
    flow = flow / (1.0 + np.abs(flow) / 10.0)

    psi = psi + flow * DT
    magnitude = np.abs(psi)
    guard_mask = (magnitude > PSI_CAP) & arrays["guard"]
    psi_cap_rows = guard_mask.reshape(psi.shape[0], -1).any(axis=1)
    scale = np.ones_like(magnitude)
    scale[guard_mask] = PSI_CAP / (magnitude[guard_mask] + 1e-30)
    psi = psi * scale

    psi = psi + interaction * DT
    psi = psi - arrays["dissipation"] * psi * DT
    psi = psi + 0.05 * raw_laplacian(psi, stencil) * DT

    energy = np.abs(psi) ** 2
    transfer = 0.001 * energy * DT
    phi_mode = phi + transfer
    new_magnitude = np.sqrt(np.maximum(energy - transfer, 0.0))
    psi_mode = psi / (np.sqrt(energy) + 1e-12) * new_magnitude

    fallback_rate = 0.0007 * (128.0 / GRID_SIZE) ** 2
    phi_fallback = phi + fallback_rate * (energy - phi) * DT
    phi = np.where(arrays["mode"], phi_mode, phi_fallback)
    psi = np.where(arrays["mode"], psi_mode, psi)

    phi = phi + 0.0025 * raw_laplacian(phi, stencil)
    phi_guard_mask = ((phi < 0.0) | (phi > PHI_CAP)) & arrays["phi_cap"]
    phi_cap_rows = phi_guard_mask.reshape(phi.shape[0], -1).any(axis=1)
    phi = np.where(arrays["phi_cap"], np.clip(phi, 0.0, PHI_CAP), phi)

    bad_psi = ~np.isfinite(psi).reshape(psi.shape[0], -1).all(axis=1)
    finite_max = np.max(
        np.where(np.isfinite(np.abs(psi)), np.abs(psi), 0.0), axis=(1, 2)
    )
    reset_rows = arrays["guard"][:, 0, 0] & (
        bad_psi | (finite_max >= PSI_CAP * 0.99)
    )
    psi[reset_rows] = 0.0

    inactive = ~active
    if inactive.any():
        psi[inactive] = old_psi[inactive]
        phi[inactive] = old_phi[inactive]
        reset_rows[inactive] = False
        psi_cap_rows[inactive] = False
        phi_cap_rows[inactive] = False

    return psi, phi, reset_rows, psi_cap_rows, phi_cap_rows


def mark_nonfinite(
    psi: np.ndarray,
    phi: np.ndarray,
    active: np.ndarray,
    last_psi: np.ndarray,
    last_phi: np.ndarray,
    failure_reason: list[str | None],
) -> tuple[np.ndarray, np.ndarray]:
    finite = (
        np.isfinite(psi).reshape(psi.shape[0], -1).all(axis=1)
        & np.isfinite(phi).reshape(phi.shape[0], -1).all(axis=1)
    )
    bad = active & ~finite
    for index in np.flatnonzero(bad):
        failure_reason[index] = "nonfinite_state"
    if bad.any():
        psi[bad] = last_psi[bad]
        phi[bad] = last_phi[bad]
        active[bad] = False
    good = active & finite
    last_psi[good] = psi[good]
    last_phi[good] = phi[good]
    return psi, phi


def radial_profile(values: np.ndarray) -> np.ndarray:
    sums = np.bincount(
        RADIAL_BINS.ravel(), weights=values.ravel(), minlength=RADIAL_BIN_COUNT
    )
    counts = np.bincount(RADIAL_BINS.ravel(), minlength=RADIAL_BIN_COUNT)
    return sums / np.maximum(counts, 1)


def spatial_metrics(psi: np.ndarray, phi: np.ndarray) -> dict[str, Any]:
    energy = np.abs(psi) ** 2
    total = float(np.sum(energy))
    if total > 0.0 and math.isfinite(total):
        center = (GRID_SIZE - 1) / 2.0
        center_row = float(np.sum(energy * ROW) / total)
        center_col = float(np.sum(energy * COL) / total)
        displacement = float(math.hypot(center_row - center, center_col - center))
        order = np.argsort(RADIUS.ravel())
        cumulative = np.cumsum(energy.ravel()[order])
        index = int(np.searchsorted(cumulative, 0.5 * total))
        half_radius = float(RADIUS.ravel()[order[min(index, order.size - 1)]])
    else:
        displacement = math.inf
        half_radius = math.inf
    return {
        "total_energy": total,
        "center_displacement": displacement,
        "half_energy_radius": half_radius,
        "energy_radial_profile": radial_profile(energy),
        "phi_radial_profile": radial_profile(phi),
    }


def relative_l2(reference: np.ndarray, candidate: np.ndarray) -> float:
    count = min(reference.size, candidate.size)
    return float(
        np.linalg.norm(candidate[:count] - reference[:count])
        / (np.linalg.norm(reference[:count]) + 1e-30)
    )


def slope_rows(values: np.ndarray) -> np.ndarray:
    x = np.arange(values.shape[0], dtype=float)
    x -= x.mean()
    denominator = float(np.dot(x, x))
    centered = values - values.mean(axis=0, keepdims=True)
    return np.dot(x, centered) / denominator


def balanced_factor(e_inner: float, e_annulus: float) -> float | None:
    if not math.isfinite(e_inner) or not math.isfinite(e_annulus) or e_annulus <= 0.0:
        return None
    b2 = 1.0 - 1.25 * e_inner / e_annulus
    if not math.isfinite(b2) or b2 < 0.0:
        return None
    return math.sqrt(b2)


def perturbation_receipt(
    psi_before: np.ndarray, phi_before: np.ndarray, psi_after: np.ndarray
) -> dict[str, Any]:
    e_before = float(np.sum(np.abs(psi_before) ** 2))
    e_after = float(np.sum(np.abs(psi_after) ** 2))
    p_phi = float(np.sum(phi_before))
    ledger_before = e_before + p_phi
    ledger_after = e_after + p_phi
    delta = ledger_after - ledger_before
    tolerance = LEDGER_RTOL * max(1.0, abs(ledger_before))
    return {
        "delta_ledger": delta,
        "epsi_after": e_after,
        "epsi_before": e_before,
        "ledger_after": ledger_after,
        "ledger_before": ledger_before,
        "ledger_tolerance": tolerance,
        "neutral_within_numeric_tolerance": bool(abs(delta) <= tolerance),
        "pphi_unchanged": p_phi,
    }


def q2_positive(row: dict[str, Any]) -> bool:
    return bool(
        row["full_recovery"]
        and row["finite"]
        and row["reset_free"]
        and row["primary_psi_cap_hits"] == 0
        and row["recovery_psi_cap_hits"] == 0
        and row["primary_phi_cap_hits"] == 0
        and row["recovery_phi_cap_hits"] == 0
    )


def comparison_label(canonical: dict[str, Any], balanced: dict[str, Any] | None) -> str:
    if balanced is None:
        return "control_unavailable"
    c = q2_positive(canonical)
    b = q2_positive(balanced)
    if not c and b:
        return "balanced_rescues_q2_classification"
    if c and not b:
        return "balanced_breaks_q2_classification"
    if c and b:
        return "both_q2_positive"
    return "both_q2_negative"


def expected_keys() -> list[str]:
    return [
        f"{stencil}|{lane.name}|phi0={float(phi0):.1f}"
        for stencil in STENCILS
        for lane in LANES
        for phi0 in PHI0_VALUES
    ]


def evolve_primary(stencil: str) -> dict[str, Any]:
    specs = [(lane, phi0) for lane in LANES for phi0 in PHI0_VALUES]
    count = len(specs)
    psi = np.stack([GAUSSIAN.copy() for _ in specs])
    phi = np.stack(
        [np.full((GRID_SIZE, GRID_SIZE), phi0, dtype=float) for _, phi0 in specs]
    )
    arrays = lane_arrays(specs)
    active = np.ones(count, dtype=bool)
    resets = np.zeros(count, dtype=int)
    psi_caps = np.zeros(count, dtype=int)
    phi_caps = np.zeros(count, dtype=int)
    failure_reason: list[str | None] = [None] * count
    last_psi = psi.copy()
    last_phi = phi.copy()
    phi_means = np.empty((PRIMARY_STEPS, count), dtype=float)

    with np.errstate(all="ignore"):
        for step in range(PRIMARY_STEPS):
            psi, phi, reset_rows, psi_cap_rows, phi_cap_rows = update_step(
                psi, phi, stencil, arrays, active
            )
            resets += reset_rows
            psi_caps += psi_cap_rows
            phi_caps += phi_cap_rows
            psi, phi = mark_nonfinite(
                psi, phi, active, last_psi, last_phi, failure_reason
            )
            phi_means[step] = np.mean(phi, axis=(1, 2))

    pre = [spatial_metrics(psi[i], phi[i]) for i in range(count)]
    tail = max(10, PRIMARY_STEPS // 5)
    phi_slopes = slope_rows(phi_means[-tail:])
    phi_tail_means = phi_means[-tail:].mean(axis=0)
    return {
        "specs": specs,
        "psi": psi,
        "phi": phi,
        "arrays": arrays,
        "active": active,
        "resets": resets,
        "psi_caps": psi_caps,
        "phi_caps": phi_caps,
        "failure_reason": failure_reason,
        "pre": pre,
        "phi_slopes": phi_slopes,
        "phi_tail_means": phi_tail_means,
    }


def recovery_branch(
    primary: dict[str, Any],
    stencil: str,
    psi_start: np.ndarray,
    branch_active: np.ndarray,
) -> list[dict[str, Any]]:
    psi = np.array(psi_start, copy=True)
    phi = np.array(primary["phi"], copy=True)
    active = np.array(branch_active, copy=True)
    last_psi = psi.copy()
    last_phi = phi.copy()
    failure_reason = list(primary["failure_reason"])
    recovery_resets = np.zeros(psi.shape[0], dtype=int)
    recovery_psi_caps = np.zeros(psi.shape[0], dtype=int)
    recovery_phi_caps = np.zeros(psi.shape[0], dtype=int)
    completed = np.zeros(psi.shape[0], dtype=int)

    with np.errstate(all="ignore"):
        for step in range(RECOVERY_STEPS):
            active_before = active.copy()
            psi, phi, reset_rows, psi_cap_rows, phi_cap_rows = update_step(
                psi, phi, stencil, primary["arrays"], active
            )
            recovery_resets += reset_rows
            recovery_psi_caps += psi_cap_rows
            recovery_phi_caps += phi_cap_rows
            before_mark = active.copy()
            psi, phi = mark_nonfinite(
                psi, phi, active, last_psi, last_phi, failure_reason
            )
            newly_bad = before_mark & ~active
            completed[active_before & ~newly_bad] = step + 1

    post = [spatial_metrics(psi[i], phi[i]) for i in range(psi.shape[0])]
    rows: list[dict[str, Any]] = []
    for i, (lane, phi0) in enumerate(primary["specs"]):
        pre = primary["pre"][i]
        energy_error = abs(post[i]["total_energy"] - pre["total_energy"]) / (
            abs(pre["total_energy"]) + 1e-30
        )
        energy_profile_error = relative_l2(
            pre["energy_radial_profile"], post[i]["energy_radial_profile"]
        )
        phi_profile_error = relative_l2(
            pre["phi_radial_profile"], post[i]["phi_radial_profile"]
        )
        half_error = abs(
            post[i]["half_energy_radius"] - pre["half_energy_radius"]
        )
        finite = failure_reason[i] is None
        reset_free = bool(primary["resets"][i] + recovery_resets[i] == 0)
        psi_recovery = bool(
            finite
            and reset_free
            and energy_error <= 0.05
            and energy_profile_error <= 0.10
            and half_error <= 1.0
            and post[i]["center_displacement"] <= 0.5
        )
        phi_threshold = max(1e-10, 1e-8 * abs(primary["phi_tail_means"][i]))
        phi_stationary = bool(primary["phi_slopes"][i] <= phi_threshold)
        full_recovery = bool(
            psi_recovery
            and primary["phi_caps"][i] + recovery_phi_caps[i] == 0
            and phi_profile_error <= 0.10
            and phi_stationary
        )
        rows.append(
            {
                "case_key": f"{stencil}|{lane.name}|phi0={float(phi0):.1f}",
                "center_displacement": float(post[i]["center_displacement"]),
                "energy_error": float(energy_error),
                "energy_profile_error": float(energy_profile_error),
                "finite": finite,
                "full_recovery": full_recovery,
                "half_energy_radius_error": float(half_error),
                "lane": lane.name,
                "phi0": float(phi0),
                "phi_one_sided_stationary": phi_stationary,
                "phi_profile_error": float(phi_profile_error),
                "primary_phi_cap_hits": int(primary["phi_caps"][i]),
                "primary_psi_cap_hits": int(primary["psi_caps"][i]),
                "primary_resets": int(primary["resets"][i]),
                "psi_recovery": psi_recovery,
                "recovery_phi_cap_hits": int(recovery_phi_caps[i]),
                "recovery_psi_cap_hits": int(recovery_psi_caps[i]),
                "recovery_resets": int(recovery_resets[i]),
                "recovery_steps_completed": int(completed[i]),
                "reset_free": reset_free,
                "stencil": stencil,
            }
        )
    return rows


def run_stencil(stencil: str) -> list[dict[str, Any]]:
    primary = evolve_primary(stencil)
    count = len(primary["specs"])
    inner = RADIUS <= 2.0
    annulus = (RADIUS >= 3.0) & (RADIUS <= 5.0)

    canonical_psi = np.array(primary["psi"], copy=True)
    canonical_psi[:, inner] *= np.where(primary["active"][:, None], INNER_FACTOR, 1.0)
    canonical_psi[:, annulus] *= np.where(
        primary["active"][:, None], CANONICAL_ANNULUS_FACTOR, 1.0
    )

    balanced_psi = np.array(primary["psi"], copy=True)
    available = np.zeros(count, dtype=bool)
    factors: list[float | None] = [None] * count
    receipts: list[dict[str, Any] | None] = [None] * count
    for i in range(count):
        if not bool(primary["active"][i]):
            continue
        energy = np.abs(primary["psi"][i]) ** 2
        e_inner = float(np.sum(energy[inner]))
        e_annulus = float(np.sum(energy[annulus]))
        factor = balanced_factor(e_inner, e_annulus)
        factors[i] = factor
        if factor is None:
            continue
        candidate = np.array(primary["psi"][i], copy=True)
        candidate[inner] *= INNER_FACTOR
        candidate[annulus] *= factor
        balanced_psi[i] = candidate
        available[i] = True
        receipts[i] = perturbation_receipt(
            primary["psi"][i], primary["phi"][i], candidate
        )

    canonical_rows = recovery_branch(
        primary, stencil, canonical_psi, np.array(primary["active"], copy=True)
    )
    balanced_rows = recovery_branch(primary, stencil, balanced_psi, available)

    rows: list[dict[str, Any]] = []
    for i, (lane, phi0) in enumerate(primary["specs"]):
        balanced = balanced_rows[i] if available[i] else None
        rows.append(
            {
                "active_before_perturbation": bool(primary["active"][i]),
                "balanced": balanced,
                "balanced_annulus_factor": factors[i],
                "canonical": canonical_rows[i],
                "case_key": f"{stencil}|{lane.name}|phi0={float(phi0):.1f}",
                "comparison": comparison_label(canonical_rows[i], balanced),
                "control_available": bool(available[i]),
                "perturbation_ledger": receipts[i],
            }
        )
    return rows


def sanitize(value: Any) -> Any:
    if isinstance(value, float):
        return value if math.isfinite(value) else None
    if isinstance(value, dict):
        return {k: sanitize(v) for k, v in value.items()}
    if isinstance(value, list):
        return [sanitize(v) for v in value]
    return value


def numeric_match(a: Any, b: Any) -> bool:
    if a is None or b is None:
        return a is None and b is None
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    try:
        af = float(a)
        bf = float(b)
    except (TypeError, ValueError):
        return False
    return abs(af - bf) <= COMPARE_ATOL + COMPARE_RTOL * max(abs(af), abs(bf))


NUMERIC_BRANCH_FIELDS = (
    "center_displacement",
    "energy_error",
    "energy_profile_error",
    "half_energy_radius_error",
    "phi_profile_error",
)
NUMERIC_LEDGER_FIELDS = (
    "delta_ledger",
    "epsi_after",
    "epsi_before",
    "ledger_after",
    "ledger_before",
    "ledger_tolerance",
    "pphi_unchanged",
)
CATEGORICAL_BRANCH_FIELDS = (
    "case_key",
    "finite",
    "full_recovery",
    "lane",
    "phi0",
    "phi_one_sided_stationary",
    "primary_phi_cap_hits",
    "primary_psi_cap_hits",
    "primary_resets",
    "psi_recovery",
    "recovery_phi_cap_hits",
    "recovery_psi_cap_hits",
    "recovery_resets",
    "recovery_steps_completed",
    "reset_free",
    "stencil",
)


def compare_case(
    checker: dict[str, Any], primary: dict[str, Any]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    numeric: list[dict[str, Any]] = []
    categorical: list[dict[str, Any]] = []
    key = checker["case_key"]

    for field in ("active_before_perturbation", "control_available", "comparison"):
        if checker[field] != primary[field]:
            categorical.append(
                {
                    "case_key": key,
                    "path": field,
                    "checker": checker[field],
                    "primary": primary[field],
                }
            )

    if not numeric_match(
        checker["balanced_annulus_factor"], primary["balanced_annulus_factor"]
    ):
        numeric.append(
            {
                "case_key": key,
                "path": "balanced_annulus_factor",
                "checker": checker["balanced_annulus_factor"],
                "primary": primary["balanced_annulus_factor"],
            }
        )

    for branch in ("canonical", "balanced"):
        c_branch = checker[branch]
        p_branch = primary[branch]
        if c_branch is None or p_branch is None:
            if c_branch is not None or p_branch is not None:
                categorical.append(
                    {
                        "case_key": key,
                        "path": branch,
                        "checker": c_branch is not None,
                        "primary": p_branch is not None,
                    }
                )
            continue
        for field in NUMERIC_BRANCH_FIELDS:
            if not numeric_match(c_branch[field], p_branch[field]):
                numeric.append(
                    {
                        "case_key": key,
                        "path": f"{branch}.{field}",
                        "checker": c_branch[field],
                        "primary": p_branch[field],
                    }
                )
        for field in CATEGORICAL_BRANCH_FIELDS:
            if c_branch[field] != p_branch[field]:
                categorical.append(
                    {
                        "case_key": key,
                        "path": f"{branch}.{field}",
                        "checker": c_branch[field],
                        "primary": p_branch[field],
                    }
                )

    c_ledger = checker["perturbation_ledger"]
    p_ledger = primary["perturbation_ledger"]
    if c_ledger is None or p_ledger is None:
        if c_ledger is not None or p_ledger is not None:
            categorical.append(
                {
                    "case_key": key,
                    "path": "perturbation_ledger",
                    "checker": c_ledger is not None,
                    "primary": p_ledger is not None,
                }
            )
    else:
        for field in NUMERIC_LEDGER_FIELDS:
            if not numeric_match(c_ledger[field], p_ledger[field]):
                numeric.append(
                    {
                        "case_key": key,
                        "path": f"perturbation_ledger.{field}",
                        "checker": c_ledger[field],
                        "primary": p_ledger[field],
                    }
                )
        if (
            c_ledger["neutral_within_numeric_tolerance"]
            != p_ledger["neutral_within_numeric_tolerance"]
        ):
            categorical.append(
                {
                    "case_key": key,
                    "path": "perturbation_ledger.neutral_within_numeric_tolerance",
                    "checker": c_ledger["neutral_within_numeric_tolerance"],
                    "primary": p_ledger["neutral_within_numeric_tolerance"],
                }
            )
    return numeric, categorical


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    available = [row for row in rows if row["control_available"]]
    unavailable = [row for row in rows if not row["control_available"]]
    neutral_failures = [
        row["case_key"]
        for row in available
        if not row["perturbation_ledger"]["neutral_within_numeric_tolerance"]
    ]
    canonical_positive = sum(q2_positive(row["canonical"]) for row in rows)
    balanced_positive = sum(
        q2_positive(row["balanced"])
        for row in available
        if row["balanced"] is not None
    )
    changed = [
        row["case_key"]
        for row in available
        if row["comparison"]
        in {"balanced_rescues_q2_classification", "balanced_breaks_q2_classification"}
    ]
    rescued = [
        row["case_key"]
        for row in available
        if row["comparison"] == "balanced_rescues_q2_classification"
    ]
    factors = [row["balanced_annulus_factor"] for row in available]
    if len(rows) != 28 or neutral_failures:
        outcome = "technical_or_methodological_failure"
    elif rescued:
        outcome = "ledger_neutral_control_rescues_q2_classification"
    else:
        outcome = "ledger_neutral_control_does_not_rescue_q2_classification"
    return {
        "balanced_annulus_factor_max": None if not factors else float(max(factors)),
        "balanced_annulus_factor_min": None if not factors else float(min(factors)),
        "balanced_q2_positive_count": int(balanced_positive),
        "balanced_rescue_count": len(rescued),
        "balanced_rescue_keys": rescued,
        "canonical_q2_positive_count": int(canonical_positive),
        "case_count": len(rows),
        "control_available_count": len(available),
        "control_unavailable_count": len(unavailable),
        "control_unavailable_keys": [row["case_key"] for row in unavailable],
        "neutral_perturbation_failure_count": len(neutral_failures),
        "neutral_perturbation_failures": neutral_failures,
        "outcome": outcome,
        "q2_classification_changed_count": len(changed),
        "q2_classification_changed_keys": changed,
    }


def protocol_errors(primary: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if primary.get("schema") != PRIMARY_SCHEMA:
        errors.append("primary_schema")
    if primary.get("stage") != PRIMARY_STAGE:
        errors.append("primary_stage")
    protocol = primary.get("protocol", {})
    expected_protocol = {
        "annulus_radius_max": 5.0,
        "annulus_radius_min": 3.0,
        "balanced_formula": "sqrt(1 - 1.25 * E_inner / E_annulus)",
        "grid_size": GRID_SIZE,
        "inner_factor": INNER_FACTOR,
        "inner_radius_max": 2.0,
        "lane_names": [lane.name for lane in LANES],
        "phi0_values": [0.0, 1.0],
        "primary_steps": PRIMARY_STEPS,
        "recovery_steps": RECOVERY_STEPS,
        "stencils": ["LAP4", "LAP8"],
        "unavailable_rule": "E_annulus <= 0 or b_squared < 0; no clipping, abs, tuning, or alternate formula",
    }
    for key, expected in expected_protocol.items():
        if protocol.get(key) != expected:
            errors.append(f"protocol.{key}")
    binding = primary.get("source_binding", {})
    expected_binding = {
        "canonical_localized_runner_git_blob": EXPECTED_CANONICAL_RUNNER_BLOB,
        "q2_pv1_runner_git_blob": EXPECTED_PV1_RUNNER_BLOB,
        "q2_pv1_primary_git_blob": EXPECTED_PV1_PRIMARY_BLOB,
        "q2_pv1_checker_git_blob": EXPECTED_PV1_CHECKER_BLOB,
    }
    for key, expected in expected_binding.items():
        if binding.get(key) != expected:
            errors.append(f"source_binding.{key}")
    return errors


def canonical_hash(payload: dict[str, Any]) -> str:
    encoded = json.dumps(
        sanitize(payload), sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def run(primary_path: Path) -> dict[str, Any]:
    primary = json.loads(primary_path.read_text(encoding="utf-8"))
    errors = protocol_errors(primary)
    checker_rows: list[dict[str, Any]] = []
    for stencil in STENCILS:
        checker_rows.extend(run_stencil(stencil))
    checker_rows = sanitize(checker_rows)
    primary_rows = primary.get("rows", [])

    expected = set(expected_keys())
    checker_map = {row["case_key"]: row for row in checker_rows}
    primary_map = {row["case_key"]: row for row in primary_rows}
    key_set_pass = (
        len(checker_rows) == 28
        and len(primary_rows) == 28
        and set(checker_map) == expected
        and set(primary_map) == expected
    )

    numeric: list[dict[str, Any]] = []
    categorical: list[dict[str, Any]] = []
    if key_set_pass:
        for key in sorted(expected):
            n, c = compare_case(checker_map[key], primary_map[key])
            numeric.extend(n)
            categorical.extend(c)

    checker_summary = summarize(checker_rows)
    primary_summary = primary.get("summary", {})
    summary_mismatches: list[dict[str, Any]] = []
    for field, value in checker_summary.items():
        p = primary_summary.get(field)
        if isinstance(value, float) or isinstance(p, float):
            if not numeric_match(value, p):
                summary_mismatches.append(
                    {"field": field, "checker": value, "primary": p}
                )
        elif value != p:
            summary_mismatches.append(
                {"field": field, "checker": value, "primary": p}
            )
    categorical.extend(
        {
            "case_key": None,
            "path": f"summary.{m['field']}",
            "checker": m["checker"],
            "primary": m["primary"],
        }
        for m in summary_mismatches
    )

    absolute_differences: list[float] = []
    relative_differences: list[float] = []
    for mismatch in numeric:
        a, b = mismatch["checker"], mismatch["primary"]
        if a is None or b is None:
            continue
        af, bf = float(a), float(b)
        absolute_differences.append(abs(af - bf))
        relative_differences.append(
            abs(af - bf) / max(abs(af), abs(bf), 1e-30)
        )

    passed = bool(
        not errors
        and key_set_pass
        and not numeric
        and not categorical
        and checker_summary["neutral_perturbation_failure_count"] == 0
    )

    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "stage": STAGE,
        "passed": passed,
        "protocol_pass": not errors,
        "protocol_errors": errors,
        "key_set_pass": key_set_pass,
        "compare_atol": COMPARE_ATOL,
        "compare_rtol": COMPARE_RTOL,
        "numeric_mismatch_count": len(numeric),
        "numeric_mismatches": numeric,
        "categorical_mismatch_count": len(categorical),
        "categorical_mismatches": categorical,
        "maximum_absolute_difference_among_mismatches": (
            0.0 if not absolute_differences else max(absolute_differences)
        ),
        "maximum_relative_difference_among_mismatches": (
            0.0 if not relative_differences else max(relative_differences)
        ),
        "independent_summary": checker_summary,
        "primary_summary": primary_summary,
        "independence": {
            "imports_primary_pv1b_runner": False,
            "imports_primary_pv1b_decision_function": False,
            "reimplements_update_equation": True,
            "reimplements_diffusion": True,
            "reimplements_metrics": True,
            "reimplements_balanced_factor": True,
            "shared_inputs": (
                "frozen public equation/constants, grid geometry, lane definitions, "
                "thresholds, and the retained primary JSON used only after recomputation"
            ),
        },
        "source_binding": {
            "primary_git_blob": EXPECTED_PRIMARY_BLOB,
            "report_git_blob_at_checker_freeze": EXPECTED_REPORT_BLOB,
            "canonical_localized_runner_git_blob": EXPECTED_CANONICAL_RUNNER_BLOB,
        },
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
    }
    payload["canonical_payload_sha256_without_self"] = canonical_hash(payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Independently reproduce and compare the frozen B4 Q2 PV1-B control."
    )
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = run(args.primary)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "passed": payload["passed"],
                "protocol_pass": payload["protocol_pass"],
                "key_set_pass": payload["key_set_pass"],
                "numeric_mismatch_count": payload["numeric_mismatch_count"],
                "categorical_mismatch_count": payload["categorical_mismatch_count"],
                "independent_summary": payload["independent_summary"],
                "payload_sha256": payload["canonical_payload_sha256_without_self"],
            },
            sort_keys=True,
            allow_nan=False,
        )
    )
    return 0 if payload["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
