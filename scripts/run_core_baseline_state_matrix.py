"""Run the first Core-only developmental-baseline/live-state disassembly matrix."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from typing import Any, Mapping

import numpy as np

from lineum_core.developmental_baseline import (
    GaussianDevelopmentalBaseline,
    build_baseline_state,
    build_blank_state,
)
from lineum_core.math import CoreConfig, ExecutionPolicy
from lineum_core.state_checkpoint import clone_state, run_steps


def _array_sha256(value: np.ndarray) -> str:
    array = np.ascontiguousarray(value)
    return hashlib.sha256(array.tobytes(order="C")).hexdigest()


def _nrmse(reference: np.ndarray, candidate: np.ndarray) -> float:
    numerator = float(np.sqrt(np.mean(np.abs(reference - candidate) ** 2)))
    denominator = float(np.sqrt(np.mean(np.abs(reference) ** 2)))
    return numerator / max(denominator, 1e-15)


def _amplitude_correlation(reference: np.ndarray, candidate: np.ndarray) -> float:
    left = np.abs(reference).ravel()
    right = np.abs(candidate).ravel()
    left_std = float(np.std(left))
    right_std = float(np.std(right))
    if left_std == 0.0 or right_std == 0.0:
        return 1.0 if np.array_equal(left, right) else 0.0
    return float(np.corrcoef(left, right)[0, 1])


def _state_receipt(
    reference: Mapping[str, Any],
    candidate: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        key: {
            "bitwise_equal": bool(np.array_equal(reference[key], candidate[key])),
            "nrmse": _nrmse(reference[key], candidate[key]),
            "candidate_sha256": _array_sha256(candidate[key]),
        }
        for key in ("psi", "phi", "kappa", "mu")
    } | {
        "psi_amplitude_correlation": _amplitude_correlation(
            reference["psi"], candidate["psi"]
        )
    }


def run_matrix(
    *,
    donor_seed: int = 314159,
    independent_seed: int = 271828,
    challenge_seed: int = 161803,
    developmental_steps: int = 5,
    challenge_steps: int = 7,
) -> dict[str, Any]:
    baseline = GaussianDevelopmentalBaseline()
    config = CoreConfig(use_mu=True, noise_strength=0.004)

    ExecutionPolicy.init_core_determinism(seed=donor_seed, device_mode="numpy")
    donor_initial = build_baseline_state(baseline)
    donor_live = run_steps(donor_initial, config, developmental_steps)

    ExecutionPolicy.init_core_determinism(seed=donor_seed, device_mode="numpy")
    replayed_live = run_steps(
        build_baseline_state(baseline), config, developmental_steps
    )

    ExecutionPolicy.init_core_determinism(seed=independent_seed, device_mode="numpy")
    independently_grown = run_steps(
        build_baseline_state(baseline), config, developmental_steps
    )

    lanes = {
        "N0_blank": build_blank_state(
            baseline.grid_size, kappa_value=baseline.kappa_floor
        ),
        "B1_baseline_independent_history": independently_grown,
        "X1_live_state_only": clone_state(donor_live),
        "BX_baseline_plus_live_state": clone_state(donor_live),
    }

    ExecutionPolicy.init_core_determinism(seed=challenge_seed, device_mode="numpy")
    reference = run_steps(clone_state(donor_live), config, challenge_steps)

    receipts: dict[str, Any] = {}
    for name, lane_state in lanes.items():
        ExecutionPolicy.init_core_determinism(
            seed=challenge_seed, device_mode="numpy"
        )
        result = run_steps(lane_state, config, challenge_steps)
        receipts[name] = _state_receipt(reference, result)

    return {
        "schema": "lineum-core-baseline-state-matrix-v1",
        "config": asdict(config),
        "baseline": baseline.to_record(),
        "donor_seed": donor_seed,
        "independent_seed": independent_seed,
        "challenge_seed": challenge_seed,
        "developmental_steps": developmental_steps,
        "challenge_steps": challenge_steps,
        "same_history_replay": _state_receipt(donor_live, replayed_live),
        "independent_history_at_transplant": _state_receipt(
            donor_live, independently_grown
        ),
        "lanes_after_common_challenge": receipts,
        "baseline_runtime_causal_input": False,
        "baseline_runtime_note": (
            "The active Core solver consumes only the live arrays and CoreConfig. "
            "The baseline recipe is an initializer and provenance record, not a "
            "separate input to step_core after transplantation."
        ),
    }


def main() -> None:
    print(json.dumps(run_matrix(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
