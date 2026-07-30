"""Core-only research harness for deterministic state and baseline transplants.

This module is intentionally outside the installable ``lineum_core`` package.
It contains experiment-specific checkpoint, initializer, and causal-matrix logic.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import sys
from dataclasses import asdict, dataclass, is_dataclass
from typing import Any, Mapping, TypeVar

import numpy as np

REPOSITORY_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPOSITORY_ROOT not in sys.path:
    sys.path.insert(0, REPOSITORY_ROOT)

from lineum_core.math import CoreConfig, ExecutionPolicy, step_core

CHECKPOINT_FORMAT = "lineum-core-state-checkpoint"
CHECKPOINT_VERSION = 1
STATE_ARRAY_KEYS = ("psi", "phi", "kappa", "mu", "delta")
_ConfigT = TypeVar("_ConfigT")


class CheckpointFormatError(ValueError):
    """Raised when a research checkpoint is malformed or fails integrity validation."""


@dataclass(frozen=True)
class GaussianDevelopmentalBaseline:
    """Experimental recipe for constructing one deterministic initial state."""

    grid_size: int = 12
    extent: float = 1.0
    envelope_decay: float = 4.0
    psi_amplitude: float = 0.15
    phase_x: float = 1.7
    phase_y: float = -0.8
    phi_amplitude: float = 0.02
    kappa_floor: float = 0.55
    kappa_amplitude: float = 0.35
    mu_amplitude: float = 0.01

    def __post_init__(self) -> None:
        if self.grid_size < 3:
            raise ValueError("grid_size must be at least 3.")
        if self.extent <= 0.0:
            raise ValueError("extent must be positive.")
        if self.envelope_decay <= 0.0:
            raise ValueError("envelope_decay must be positive.")
        if min(
            self.psi_amplitude,
            self.phi_amplitude,
            self.kappa_floor,
            self.kappa_amplitude,
            self.mu_amplitude,
        ) < 0.0:
            raise ValueError("baseline amplitudes must be non-negative.")

    def to_record(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_record(
        cls,
        record: Mapping[str, Any],
    ) -> "GaussianDevelopmentalBaseline":
        return cls(**dict(record))


def build_baseline_state(
    baseline: GaussianDevelopmentalBaseline,
) -> dict[str, np.ndarray]:
    """Build the exact initial arrays declared by the experimental recipe."""
    axis = np.linspace(-baseline.extent, baseline.extent, baseline.grid_size)
    y, x = np.meshgrid(axis, axis, indexing="ij")
    envelope = np.exp(-baseline.envelope_decay * (x**2 + y**2))
    phase = np.exp(1j * (baseline.phase_x * x + baseline.phase_y * y))
    return {
        "psi": (baseline.psi_amplitude * envelope * phase).astype(np.complex128),
        "phi": (baseline.phi_amplitude * envelope).astype(np.float64),
        "kappa": (
            baseline.kappa_floor + baseline.kappa_amplitude * envelope
        ).astype(np.float64),
        "mu": (baseline.mu_amplitude * (1.0 - envelope)).astype(np.float64),
    }


def build_blank_state(
    grid_size: int,
    *,
    kappa_value: float = 0.55,
) -> dict[str, np.ndarray]:
    """Build the standardized blank recipient used by the research controls."""
    if grid_size < 3:
        raise ValueError("grid_size must be at least 3.")
    if kappa_value < 0.0:
        raise ValueError("kappa_value must be non-negative.")
    shape = (grid_size, grid_size)
    return {
        "psi": np.zeros(shape, dtype=np.complex128),
        "phi": np.zeros(shape, dtype=np.float64),
        "kappa": np.full(shape, kappa_value, dtype=np.float64),
        "mu": np.zeros(shape, dtype=np.float64),
    }


def _canonical_json_bytes(value: Mapping[str, Any]) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")


def _encode_array(value: Any) -> dict[str, Any]:
    array = np.ascontiguousarray(np.asarray(value))
    return {
        "dtype": array.dtype.str,
        "shape": list(array.shape),
        "data_base64": base64.b64encode(array.tobytes(order="C")).decode("ascii"),
    }


def _decode_array(record: Mapping[str, Any]) -> np.ndarray:
    try:
        dtype = np.dtype(record["dtype"])
        shape = tuple(int(item) for item in record["shape"])
        raw = base64.b64decode(record["data_base64"], validate=True)
    except (KeyError, TypeError, ValueError) as exc:
        raise CheckpointFormatError("Invalid array record.") from exc
    expected_size = int(np.prod(shape, dtype=np.int64)) * dtype.itemsize
    if len(raw) != expected_size:
        raise CheckpointFormatError(
            "Array byte length does not match its dtype and shape."
        )
    return np.frombuffer(raw, dtype=dtype).reshape(shape).copy()


def capture_numpy_rng_state() -> dict[str, Any]:
    generator, keys, position, has_gauss, cached_gaussian = np.random.get_state()
    return {
        "generator": generator,
        "keys": _encode_array(keys),
        "position": int(position),
        "has_gauss": int(has_gauss),
        "cached_gaussian": float(cached_gaussian),
    }


def restore_numpy_rng_state(record: Mapping[str, Any]) -> None:
    try:
        state = (
            str(record["generator"]),
            _decode_array(record["keys"]).astype(np.uint32, copy=False),
            int(record["position"]),
            int(record["has_gauss"]),
            float(record["cached_gaussian"]),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise CheckpointFormatError("Invalid NumPy random-generator state.") from exc
    np.random.set_state(state)


def clone_state(state: Mapping[str, Any]) -> dict[str, Any]:
    copied: dict[str, Any] = {}
    for key, value in state.items():
        if key == "telemetry":
            copied[key] = dict(value)
        elif isinstance(value, np.ndarray):
            copied[key] = value.copy()
        else:
            copied[key] = value
    return copied


def create_checkpoint(
    state: Mapping[str, Any],
    config: CoreConfig,
    *,
    step_index: int,
    include_rng_state: bool = True,
) -> dict[str, Any]:
    missing = [key for key in ("psi", "phi", "kappa") if key not in state]
    if missing:
        raise ValueError(f"State is missing required arrays: {', '.join(missing)}")
    if step_index < 0:
        raise ValueError("step_index must be non-negative.")
    if not is_dataclass(config):
        raise TypeError("Research checkpoints require a dataclass configuration.")

    payload: dict[str, Any] = {
        "format": CHECKPOINT_FORMAT,
        "version": CHECKPOINT_VERSION,
        "step_index": int(step_index),
        "config": asdict(config),
        "arrays": {
            key: _encode_array(state[key])
            for key in STATE_ARRAY_KEYS
            if key in state
        },
        "numpy_rng_state": (
            capture_numpy_rng_state() if include_rng_state else None
        ),
    }
    payload["payload_sha256"] = hashlib.sha256(
        _canonical_json_bytes(payload)
    ).hexdigest()
    return payload


def serialize_checkpoint(checkpoint: Mapping[str, Any]) -> bytes:
    return _canonical_json_bytes(checkpoint)


def load_checkpoint(
    data: bytes | str | Mapping[str, Any],
    *,
    config_type: type[_ConfigT] = CoreConfig,
    restore_rng: bool = True,
) -> tuple[dict[str, Any], _ConfigT, int]:
    if isinstance(data, Mapping):
        checkpoint = dict(data)
    else:
        try:
            checkpoint = json.loads(data)
        except (json.JSONDecodeError, TypeError, UnicodeDecodeError) as exc:
            raise CheckpointFormatError("Checkpoint is not valid UTF-8 JSON.") from exc
    if checkpoint.get("format") != CHECKPOINT_FORMAT:
        raise CheckpointFormatError("Unsupported checkpoint format.")
    if checkpoint.get("version") != CHECKPOINT_VERSION:
        raise CheckpointFormatError("Unsupported checkpoint version.")

    expected_hash = checkpoint.get("payload_sha256")
    unhashed = dict(checkpoint)
    unhashed.pop("payload_sha256", None)
    actual_hash = hashlib.sha256(_canonical_json_bytes(unhashed)).hexdigest()
    if not isinstance(expected_hash, str) or expected_hash != actual_hash:
        raise CheckpointFormatError("Checkpoint integrity hash mismatch.")

    try:
        arrays = {
            str(key): _decode_array(value)
            for key, value in checkpoint["arrays"].items()
        }
        config = config_type(**checkpoint["config"])
        step_index = int(checkpoint["step_index"])
    except (KeyError, TypeError, ValueError) as exc:
        raise CheckpointFormatError("Checkpoint metadata is invalid.") from exc
    missing = [key for key in ("psi", "phi", "kappa") if key not in arrays]
    if missing:
        raise CheckpointFormatError(
            f"Checkpoint is missing required arrays: {', '.join(missing)}"
        )
    if step_index < 0:
        raise CheckpointFormatError("Checkpoint step index is negative.")

    rng_record = checkpoint.get("numpy_rng_state")
    if restore_rng:
        if rng_record is None:
            raise CheckpointFormatError(
                "Checkpoint does not contain NumPy RNG state."
            )
        restore_numpy_rng_state(rng_record)
    return arrays, config, step_index


def run_steps(
    state: Mapping[str, Any],
    config: CoreConfig,
    steps: int,
) -> dict[str, Any]:
    if steps < 0:
        raise ValueError("steps must be non-negative.")
    current = clone_state(state)
    for _ in range(steps):
        current = step_core(current, config)
    return current


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


def run_checkpoint_pilot(
    *,
    seed: int = 314159,
    reset_seed: int = 999,
    warmup_steps: int = 5,
    continuation_steps: int = 7,
) -> dict[str, Any]:
    baseline = GaussianDevelopmentalBaseline()
    config = CoreConfig(use_mu=True, noise_strength=0.004)

    ExecutionPolicy.init_core_determinism(seed=seed, device_mode="numpy")
    donor_at_checkpoint = run_steps(
        build_baseline_state(baseline), config, warmup_steps
    )
    serialized = serialize_checkpoint(
        create_checkpoint(
            donor_at_checkpoint, config, step_index=warmup_steps
        )
    )

    uninterrupted = run_steps(
        donor_at_checkpoint, config, continuation_steps
    )
    recipient_state, recipient_config, recipient_step = load_checkpoint(serialized)
    restored = run_steps(
        recipient_state, recipient_config, continuation_steps
    )

    reset_state, reset_config, _ = load_checkpoint(
        serialized, restore_rng=False
    )
    np.random.seed(reset_seed)
    reset_history = run_steps(reset_state, reset_config, continuation_steps)

    return {
        "schema": "lineum-core-transplant-pilot-result-v1",
        "backend": "numpy",
        "seed": seed,
        "reset_seed": reset_seed,
        "warmup_steps": warmup_steps,
        "continuation_steps": continuation_steps,
        "recipient_step_index": recipient_step,
        "checkpoint_bytes": len(serialized),
        "checkpoint_file_sha256": hashlib.sha256(serialized).hexdigest(),
        "full_transfer": {
            **{
                f"{key}_bitwise_equal": bool(
                    np.array_equal(uninterrupted[key], restored[key])
                )
                for key in ("psi", "phi", "kappa", "mu")
            },
            "max_abs_psi_difference": float(
                np.max(np.abs(uninterrupted["psi"] - restored["psi"]))
            ),
            "final_psi_sha256": _array_sha256(restored["psi"]),
        },
        "reset_rng_control": {
            "psi_bitwise_equal": bool(
                np.array_equal(uninterrupted["psi"], reset_history["psi"])
            ),
            "max_abs_psi_difference": float(
                np.max(np.abs(uninterrupted["psi"] - reset_history["psi"]))
            ),
            "final_psi_sha256": _array_sha256(reset_history["psi"]),
        },
    }


def run_baseline_state_matrix(
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
    donor_live = run_steps(
        build_baseline_state(baseline), config, developmental_steps
    )

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
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--experiment",
        choices=("checkpoint", "matrix", "all"),
        default="all",
    )
    args = parser.parse_args()

    output: dict[str, Any] = {}
    if args.experiment in {"checkpoint", "all"}:
        output["checkpoint"] = run_checkpoint_pilot()
    if args.experiment in {"matrix", "all"}:
        output["matrix"] = run_baseline_state_matrix()
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
