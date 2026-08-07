#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np

HERE = Path(__file__).resolve().parent
CANONICAL_PATH = HERE / "lineum_b4_saturation_localized_l1.py"
_SPEC = importlib.util.spec_from_file_location("lineum_b4_l1_exact", CANONICAL_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise RuntimeError("Cannot load canonical B4 localized runner")
l1 = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = l1
_SPEC.loader.exec_module(l1)

SCHEMA = "lineum-b4-q2-spatial-accounting/1"
STAGE_A_ID = "Q2-SA1-A"
STENCILS = ("LAP4", "LAP8")
PRIMARY_STEPS = l1.STEPS
RECOVERY_STEPS = l1.RECOVERY_STEPS
DT = l1.DT
PHI0 = 1.0


@dataclass(frozen=True)
class SpatialLane:
    name: str
    flow: bool
    psi_diffusion: bool
    phi_diffusion: bool


SPATIAL_LANES = (
    SpatialLane("L0", True, True, True),
    SpatialLane("S1", False, True, False),
    SpatialLane("S2", False, False, True),
    SpatialLane("S3", True, False, False),
)

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


def _lane_arrays(count: int) -> dict[str, np.ndarray]:
    # Stage A keeps every non-spatial baseline term unchanged, disables phi cap,
    # and treats any psi guard/reset contact as a failed case rather than a rescue.
    shape = (count, 1, 1)
    return {
        "use_guard": np.ones(shape, dtype=bool),
        "use_phi_cap": np.zeros(shape, dtype=bool),
        "use_tanh": np.ones(shape, dtype=bool),
        "use_denominator": np.ones(shape, dtype=bool),
        "use_mode_coupling": np.ones(shape, dtype=bool),
        "dissipation": np.full(shape, 0.005, dtype=float),
    }


def _spatial_arrays(lanes: tuple[SpatialLane, ...]) -> dict[str, np.ndarray]:
    shape = (-1, 1, 1)
    return {
        "flow": np.asarray([lane.flow for lane in lanes], dtype=bool).reshape(shape),
        "psi_diffusion": np.asarray(
            [lane.psi_diffusion for lane in lanes], dtype=bool
        ).reshape(shape),
        "phi_diffusion": np.asarray(
            [lane.phi_diffusion for lane in lanes], dtype=bool
        ).reshape(shape),
    }


def _snapshot(
    psi: np.ndarray,
    phi: np.ndarray,
    region: np.ndarray | None,
) -> dict[str, np.ndarray]:
    epsi = np.abs(psi) ** 2
    if region is None:
        local_epsi = np.zeros(psi.shape[0], dtype=float)
        local_phi = np.zeros(psi.shape[0], dtype=float)
        local_psi = np.zeros(psi.shape[0], dtype=np.complex128)
    else:
        local_epsi = np.sum(epsi * region, axis=(1, 2))
        local_phi = np.sum(phi * region, axis=(1, 2))
        local_psi = np.sum(psi * region, axis=(1, 2))
    return {
        "epsi_global": np.sum(epsi, axis=(1, 2)),
        "epsi_local": local_epsi,
        "phi_global": np.sum(phi, axis=(1, 2)),
        "phi_local": local_phi,
        "psi_sum_global": np.sum(psi, axis=(1, 2)),
        "psi_sum_local": local_psi,
    }


def _delta(
    before: dict[str, np.ndarray],
    after: dict[str, np.ndarray],
) -> dict[str, np.ndarray]:
    return {key: after[key] - before[key] for key in before}


def instrumented_step(
    current_psi: np.ndarray,
    current_phi: np.ndarray,
    kappa: np.ndarray,
    mu: np.ndarray,
    stencil: str,
    lane_arrays: dict[str, np.ndarray],
    spatial_arrays: dict[str, np.ndarray],
    active: np.ndarray | None = None,
    region: np.ndarray | None = None,
) -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    dict[str, dict[str, np.ndarray]],
    dict[str, np.ndarray],
]:
    """Exact canonical step with observer-only stage receipts and spatial toggles."""
    if active is None:
        active = np.ones(current_psi.shape[0], dtype=bool)
    original_psi = current_psi.copy()
    original_phi = current_phi.copy()

    use_guard = lane_arrays["use_guard"]
    use_phi_cap = lane_arrays["use_phi_cap"]
    use_tanh = lane_arrays["use_tanh"]
    use_denominator = lane_arrays["use_denominator"]
    use_mode_coupling = lane_arrays["use_mode_coupling"]
    dissipation = lane_arrays["dissipation"]

    drift_multiplier = 1.0 + mu
    clipped_phi = np.clip(current_phi, 0.0, 10.0)
    raw_interaction = 0.04 * clipped_phi * kappa * drift_multiplier
    interaction_factor = np.where(
        use_tanh,
        0.1 * np.tanh(raw_interaction / 0.1),
        raw_interaction,
    )
    interaction = interaction_factor * current_psi
    interaction = np.where(
        use_denominator,
        interaction / (1.0 + np.abs(interaction) / 10.0),
        interaction,
    )

    receipts: dict[str, dict[str, np.ndarray]] = {}
    start_snapshot = _snapshot(current_psi, current_phi, region)
    before = start_snapshot

    gradient_phi_x, gradient_phi_y = np.gradient(current_phi, axis=(1, 2))
    flow = (
        -0.004
        * (gradient_phi_x + 1j * gradient_phi_y)
        * kappa
        * drift_multiplier
    )
    flow = flow / (1.0 + np.abs(flow) / 10.0)
    current_psi = current_psi + np.where(spatial_arrays["flow"], flow, 0.0) * DT
    after = _snapshot(current_psi, current_phi, region)
    receipts["phi_gradient_flow"] = _delta(before, after)
    before = after

    magnitude = np.abs(current_psi)
    cap_mask = (magnitude > l1.PSI_CAP) & use_guard
    cap_rows = cap_mask.reshape(current_psi.shape[0], -1).any(axis=1)
    scale = np.ones_like(magnitude)
    scale[cap_mask] = l1.PSI_CAP / (magnitude[cap_mask] + 1e-30)
    current_psi = current_psi * scale
    after = _snapshot(current_psi, current_phi, region)
    receipts["psi_guard_clip"] = _delta(before, after)
    before = after

    current_psi = current_psi + interaction * DT
    after = _snapshot(current_psi, current_phi, region)
    receipts["feedback"] = _delta(before, after)
    before = after

    current_psi = current_psi - dissipation * current_psi * DT
    after = _snapshot(current_psi, current_phi, region)
    receipts["linear_dissipation"] = _delta(before, after)
    before = after

    psi_diff = l1.diffuse(current_psi, kappa, 0.05, stencil) * kappa * DT
    current_psi = current_psi + np.where(
        spatial_arrays["psi_diffusion"], psi_diff, 0.0
    )
    after = _snapshot(current_psi, current_phi, region)
    receipts["psi_diffusion"] = _delta(before, after)
    before = after

    energy = np.abs(current_psi) ** 2
    transferred = 0.001 * energy * kappa * DT
    phi_mode = current_phi + transferred
    new_magnitude = np.sqrt(np.maximum(energy - transferred, 0.0))
    psi_mode = current_psi / (np.sqrt(energy) + 1e-12) * new_magnitude
    dynamic_reaction = 0.0007 * (128.0 / l1.GRID_SIZE) ** 2
    phi_fallback = current_phi + dynamic_reaction * (energy - current_phi) * DT
    current_phi = np.where(use_mode_coupling, phi_mode, phi_fallback)
    current_psi = np.where(use_mode_coupling, psi_mode, current_psi)
    after = _snapshot(current_psi, current_phi, region)
    receipts["mode_transfer"] = _delta(before, after)
    before = after

    phi_diff = 0.05 * l1.diffuse(current_phi, kappa, 0.05, stencil)
    current_phi = current_phi + np.where(
        spatial_arrays["phi_diffusion"], phi_diff, 0.0
    )
    after = _snapshot(current_psi, current_phi, region)
    receipts["phi_diffusion"] = _delta(before, after)
    before = after

    phi_mask = ((current_phi < 0.0) | (current_phi > l1.PHI_CAP)) & use_phi_cap
    phi_cap_rows = phi_mask.reshape(current_phi.shape[0], -1).any(axis=1)
    current_phi = np.where(
        use_phi_cap,
        np.clip(current_phi, 0.0, l1.PHI_CAP),
        current_phi,
    )
    after = _snapshot(current_psi, current_phi, region)
    receipts["phi_cap"] = _delta(before, after)
    before = after

    bad_psi = ~np.isfinite(current_psi).reshape(current_psi.shape[0], -1).all(axis=1)
    finite_max = np.max(
        np.where(np.isfinite(np.abs(current_psi)), np.abs(current_psi), 0.0),
        axis=(1, 2),
    )
    reset_rows = use_guard[:, 0, 0] & (
        bad_psi | (finite_max >= l1.PSI_CAP * 0.99)
    )
    current_psi[reset_rows] = 0.0

    inactive = ~active
    if inactive.any():
        current_psi[inactive] = original_psi[inactive]
        current_phi[inactive] = original_phi[inactive]
        reset_rows[inactive] = False
        cap_rows[inactive] = False
        phi_cap_rows[inactive] = False

    after = _snapshot(current_psi, current_phi, region)
    receipts["reset"] = _delta(before, after)

    total_delta = _delta(start_snapshot, after)
    summed: dict[str, np.ndarray] = {}
    residual: dict[str, np.ndarray] = {}
    for key in start_snapshot:
        summed[key] = sum((receipts[stage][key] for stage in STAGES), np.zeros_like(total_delta[key]))
        residual[key] = total_delta[key] - summed[key]

    return (
        current_psi,
        current_phi,
        reset_rows,
        cap_rows,
        phi_cap_rows,
        receipts,
        residual,
    )


def baseline_equivalence_step(
    psi: np.ndarray,
    phi: np.ndarray,
    kappa: np.ndarray,
    mu: np.ndarray,
    stencil: str,
    active: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    count = psi.shape[0]
    lanes = tuple(SpatialLane(f"L0-{index}", True, True, True) for index in range(count))
    output = instrumented_step(
        psi,
        phi,
        kappa,
        mu,
        stencil,
        _lane_arrays(count),
        _spatial_arrays(lanes),
        active=active,
        region=None,
    )
    return output[:5]


def _strict_json(value: Any) -> Any:
    if isinstance(value, np.generic):
        return _strict_json(value.item())
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    if isinstance(value, float) and not math.isfinite(value):
        if math.isnan(value):
            return "NaN"
        return "Infinity" if value > 0 else "-Infinity"
    if isinstance(value, np.ndarray):
        return _strict_json(value.tolist())
    if isinstance(value, dict):
        return {key: _strict_json(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_strict_json(item) for item in value]
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--mode",
        choices=("protocol",),
        default="protocol",
        help="Scientific Stage A execution is intentionally not enabled before preregistration.",
    )
    args = parser.parse_args()
    payload = {
        "schema": SCHEMA,
        "stage": STAGE_A_ID,
        "status": "instrumentation_only_scientific_execution_disabled",
        "canonical_runner": str(CANONICAL_PATH.name),
        "spatial_lanes": [asdict(lane) for lane in SPATIAL_LANES],
        "stages": STAGES,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(_strict_json(payload), indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
