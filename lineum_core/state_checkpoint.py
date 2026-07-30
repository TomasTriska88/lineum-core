"""Portable deterministic checkpoints for Lineum Core NumPy trajectories."""

from __future__ import annotations

import base64
import hashlib
import json
from dataclasses import asdict, is_dataclass
from typing import Any, Mapping, TypeVar

import numpy as np

from .math import CoreConfig, step_core


CHECKPOINT_FORMAT = "lineum-core-state-checkpoint"
CHECKPOINT_VERSION = 1
STATE_ARRAY_KEYS = ("psi", "phi", "kappa", "mu", "delta")
_ConfigT = TypeVar("_ConfigT")


class CheckpointFormatError(ValueError):
    """Raised when a checkpoint is malformed or fails integrity validation."""


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
    """Capture the complete legacy NumPy generator state used by Core."""
    generator, keys, position, has_gauss, cached_gaussian = np.random.get_state()
    return {
        "generator": generator,
        "keys": _encode_array(keys),
        "position": int(position),
        "has_gauss": int(has_gauss),
        "cached_gaussian": float(cached_gaussian),
    }


def restore_numpy_rng_state(record: Mapping[str, Any]) -> None:
    """Restore a generator state produced by :func:`capture_numpy_rng_state`."""
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
    """Copy the numerical state without retaining mutable array aliases."""
    copied: dict[str, Any] = {}
    for key, value in state.items():
        if key == "telemetry":
            copied[key] = dict(value)
        elif isinstance(value, np.ndarray):
            copied[key] = value.copy()
        else:
            copied[key] = value
    return copied


def _config_record(config: Any) -> dict[str, Any]:
    if not is_dataclass(config):
        raise TypeError("Lineum checkpoints require a dataclass configuration object.")
    return asdict(config)


def create_checkpoint(
    state: Mapping[str, Any],
    config: CoreConfig,
    *,
    step_index: int,
    include_rng_state: bool = True,
) -> dict[str, Any]:
    """Create an integrity-protected, JSON-serializable Core checkpoint."""
    missing = [key for key in ("psi", "phi", "kappa") if key not in state]
    if missing:
        raise ValueError(f"State is missing required arrays: {', '.join(missing)}")
    if step_index < 0:
        raise ValueError("step_index must be non-negative.")

    arrays = {
        key: _encode_array(state[key])
        for key in STATE_ARRAY_KEYS
        if key in state
    }
    payload: dict[str, Any] = {
        "format": CHECKPOINT_FORMAT,
        "version": CHECKPOINT_VERSION,
        "step_index": int(step_index),
        "config": _config_record(config),
        "arrays": arrays,
        "numpy_rng_state": (
            capture_numpy_rng_state() if include_rng_state else None
        ),
    }
    payload["payload_sha256"] = hashlib.sha256(
        _canonical_json_bytes(payload)
    ).hexdigest()
    return payload


def serialize_checkpoint(checkpoint: Mapping[str, Any]) -> bytes:
    """Serialize a checkpoint as canonical UTF-8 JSON bytes."""
    return _canonical_json_bytes(checkpoint)


def load_checkpoint(
    data: bytes | str | Mapping[str, Any],
    *,
    config_type: type[_ConfigT] = CoreConfig,
    restore_rng: bool = True,
) -> tuple[dict[str, Any], _ConfigT, int]:
    """Validate and restore a checkpoint into independent arrays and config."""
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
    """Advance an independent state copy through the canonical Core step function."""
    if steps < 0:
        raise ValueError("steps must be non-negative.")
    current = clone_state(state)
    for _ in range(steps):
        current = step_core(current, config)
    return current
