from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import math
import platform
import subprocess
import sys
import time
from typing import Any, Callable, Mapping, Sequence

import numpy as np

SEED = 20260804
LABEL_A = 0
LABEL_B = 1
LABEL_NAMES = {LABEL_A: "A", LABEL_B: "B"}
CHANNEL_IDS = {"psi": 0, "phi": 1, "mu": 2}
CHECKPOINTS = (0, 100, 500, 1000, 2000)
PERMUTATIONS = 2000
FAIL_SAFE_MARKER = "LINEUM FAIL-SAFE"

FROZEN_ENGINE_GIT_BLOB = "bb877021810691223a0eb960a45493a2e351112a"
FROZEN_REQUIREMENTS_GIT_BLOB = "942f2b94b3d3f8c767451ae2d847a7b17c86d81e"
FROZEN_REQUIREMENTS_DEV_GIT_BLOB = "7a0907e3e6c2d15400d19b536227a509910ae7e9"

PRIMARY_SIZE = 64
PRIMARY_DT = 0.1
PRIMARY_IMPRINT_STEPS = 120
PRIMARY_SOURCE_OFF_STEPS = 2000
PRIMARY_ECHO_STEPS = 200
COMMON_WIDTH = 5.0
REPRESENTATIVE_VARIANT_IDS = (12, 17)
REPRESENTATIVE_PARAMS = (
    (12.0, 2.5, 0, 0),
    (12.0, 3.5, 0, 0),
)

P0_ACCURACY_MIN = 0.95
PASSIVE_ACCURACY_MIN = 0.90
PERMUTATION_P_MAX = 0.01
P0_IMBALANCE_MAX = 0.05
PASSIVE_IMBALANCE_MAX = 0.10
QUADRUPOLE_UNCLASSIFIED = 1e-6
TRANSPOSE_ANTISYMMETRY_MAX = 1e-12
PASSIVE_SIGNAL_MIN = 1e-6
LOW_NOISE_ACCURACY_LOSS_MAX = 0.05
HIGH_NOISE_ACCURACY_MIN = 0.80
PASSIVE_CAP_ACCURACY_DIFF_MAX = 0.05
PASSIVE_CAP_FIELD_DIFF_MAX = 1e-6
CAUSAL_NULL_MAX = 1e-12
CAUSAL_FULL_ABS_FLOOR = 1e-4
CAUSAL_SINGLE_ABS_FLOOR = 5e-5
CAUSAL_ZEROING_REDUCTION_MIN = 0.50
GRID_ERROR_MAX = 1e-10
SCALE_RATIO_MIN = 0.5
SCALE_RATIO_MAX = 2.0


@dataclass(frozen=True)
class FrozenProtocol:
    size: int = PRIMARY_SIZE
    dt: float = PRIMARY_DT
    psi_diffusion: float = 0.05
    phi_diffusion: float = 0.05
    reaction_strength: float = 0.0007
    implemented_psi_dissipation: float = 0.005
    drift_strength: float = 0.0
    disable_quantum_noise: bool = True
    use_mode_coupling: bool = False
    phi_diffusion_scales_with_dt: bool = True
    use_mu: bool = True
    mu_eta: float = 0.005
    mu_rho: float = 0.0001
    mu_cap: float = 10.0
    mu_peak_cutoff_ratio: float = 0.1
    psi_amp_cap: float = 1e6
    phi_cap: float = 1e6
    stencil_type: str = "LAP4"
    imprint_steps: int = PRIMARY_IMPRINT_STEPS
    source_off_steps: int = PRIMARY_SOURCE_OFF_STEPS
    echo_steps: int = PRIMARY_ECHO_STEPS
    common_width: float = COMMON_WIDTH


@dataclass
class TraceReceipt:
    finite: bool = True
    reset_seen: bool = False
    max_abs_psi: float = 0.0
    max_phi: float = 0.0
    max_mu: float = 0.0
    source_off_psi_max: float = 0.0
    steps_completed: int = 0

    def observe(self, state: Mapping[str, np.ndarray], *, source_off: bool = False) -> None:
        psi = np.asarray(state["psi"])
        phi = np.asarray(state["phi"])
        mu = np.asarray(state["mu"])
        finite = bool(
            np.all(np.isfinite(psi))
            and np.all(np.isfinite(phi))
            and np.all(np.isfinite(mu))
        )
        self.finite = self.finite and finite
        if finite:
            psi_max = float(np.max(np.abs(psi)))
            phi_max = float(np.max(phi))
            mu_max = float(np.max(mu))
            self.max_abs_psi = max(self.max_abs_psi, psi_max)
            self.max_phi = max(self.max_phi, phi_max)
            self.max_mu = max(self.max_mu, mu_max)
            if source_off:
                self.source_off_psi_max = max(self.source_off_psi_max, psi_max)

    def merge(self, other: "TraceReceipt") -> "TraceReceipt":
        return TraceReceipt(
            finite=self.finite and other.finite,
            reset_seen=self.reset_seen or other.reset_seen,
            max_abs_psi=max(self.max_abs_psi, other.max_abs_psi),
            max_phi=max(self.max_phi, other.max_phi),
            max_mu=max(self.max_mu, other.max_mu),
            source_off_psi_max=max(
                self.source_off_psi_max, other.source_off_psi_max
            ),
            steps_completed=self.steps_completed + other.steps_completed,
        )


@dataclass
class HistoryRecord:
    variant_id: int
    label: int
    params: tuple[float, float, int, int]
    imprint_state: dict[str, np.ndarray]
    final_source_off_state: dict[str, np.ndarray]
    checkpoints: dict[int, dict[str, np.ndarray]]
    imprint_trace: TraceReceipt
    source_off_trace: TraceReceipt

    @property
    def full_trace(self) -> TraceReceipt:
        return self.imprint_trace.merge(self.source_off_trace)


@dataclass
class EchoPairResult:
    final_a: dict[str, np.ndarray]
    final_b: dict[str, np.ndarray]
    trace_a: TraceReceipt
    trace_b: TraceReceipt
    divergences: dict[str, float]
    common_state_equal: bool


StepFunction = Callable[[Mapping[str, np.ndarray], Any], Mapping[str, np.ndarray]]


def nuisance_schedule() -> list[tuple[float, float, int, int]]:
    return [
        (separation, width, shift_x, shift_y)
        for separation in (10.0, 12.0, 14.0)
        for width in (2.5, 3.5)
        for shift_x, shift_y in ((-3, -2), (-2, 3), (0, 0), (2, -3), (3, 2))
    ]


def split_variant_masks(count: int) -> tuple[np.ndarray, np.ndarray]:
    ids = np.arange(count, dtype=np.int64)
    train = np.isin(ids % 3, (0, 1))
    held_out = ids % 3 == 2
    return train, held_out


def coordinates(size: int) -> tuple[np.ndarray, np.ndarray]:
    axis = np.arange(size, dtype=np.float64) - (size - 1) / 2.0
    row, col = np.meshgrid(axis, axis, indexing="ij")
    return row, col


def normalize_energy(amplitude: np.ndarray) -> np.ndarray:
    field = np.asarray(amplitude, dtype=np.complex128)
    energy = float(np.sum(np.abs(field) ** 2))
    if not math.isfinite(energy) or energy <= 0.0:
        raise ValueError("Amplitude must carry finite positive energy")
    return field / math.sqrt(energy)


def make_orientation_pair(
    size: int,
    separation: float,
    width: float,
    shift_x: int,
    shift_y: int,
) -> tuple[np.ndarray, np.ndarray]:
    row, col = coordinates(size)

    def gaussian(dx: np.ndarray, dy: np.ndarray) -> np.ndarray:
        return np.exp(-(dx * dx + dy * dy) / (2.0 * width * width))

    horizontal = gaussian(col - separation / 2.0, row) + gaussian(
        col + separation / 2.0, row
    )
    vertical = gaussian(col, row - separation / 2.0) + gaussian(
        col, row + separation / 2.0
    )
    horizontal = np.roll(horizontal, (shift_y, shift_x), axis=(0, 1))
    vertical = np.roll(vertical, (shift_y, shift_x), axis=(0, 1))
    return normalize_energy(horizontal), normalize_energy(vertical)


def make_common_state(size: int, width: float = COMMON_WIDTH) -> np.ndarray:
    row, col = coordinates(size)
    return normalize_energy(np.exp(-(row * row + col * col) / (2.0 * width * width)))


def make_state(psi: np.ndarray) -> dict[str, np.ndarray]:
    size = psi.shape[0]
    zeros = np.zeros((size, size), dtype=np.float64)
    return {
        "psi": np.asarray(psi, dtype=np.complex128).copy(),
        "phi": zeros.copy(),
        "mu": zeros.copy(),
        "kappa": np.ones((size, size), dtype=np.float64),
    }


def clone_state(state: Mapping[str, np.ndarray]) -> dict[str, np.ndarray]:
    return {key: np.asarray(value).copy() for key, value in state.items()}


def rotate_state_quarter_turn(state: Mapping[str, np.ndarray]) -> dict[str, np.ndarray]:
    return {key: np.rot90(np.asarray(value)).copy() for key, value in state.items()}


def apply_intervention(
    source_off_state: Mapping[str, np.ndarray],
    lane: str,
    common_state: np.ndarray,
) -> dict[str, np.ndarray]:
    state = clone_state(source_off_state)
    state["psi"] = np.asarray(common_state, dtype=np.complex128).copy()
    if lane == "C0":
        state["phi"][:] = 0.0
        state["mu"][:] = 0.0
    elif lane == "C1":
        pass
    elif lane == "C2":
        state["mu"][:] = 0.0
    elif lane == "C3":
        state["phi"][:] = 0.0
    else:
        raise ValueError(f"Unknown causal lane: {lane}")
    return state


def field_weight(channel: str, value: np.ndarray) -> np.ndarray:
    if channel == "psi":
        return np.abs(np.asarray(value)) ** 2
    if channel not in {"phi", "mu"}:
        raise ValueError(f"Unknown channel: {channel}")
    return np.asarray(value, dtype=np.float64)


def quadrupole_score(weight: np.ndarray) -> float:
    field = np.maximum(np.asarray(weight, dtype=np.float64), 0.0)
    total = float(np.sum(field))
    if total <= 0.0:
        return 0.0
    row, col = coordinates(field.shape[0])
    x_center = float(np.sum(field * col) / total)
    y_center = float(np.sum(field * row) / total)
    dx = col - x_center
    dy = row - y_center
    denominator = float(np.sum(field * (dx * dx + dy * dy))) + 1e-30
    return float(np.sum(field * (dx * dx - dy * dy)) / denominator)


def quadrupole_predictions(weights: np.ndarray) -> np.ndarray:
    scores = np.asarray([quadrupole_score(field) for field in weights], dtype=float)
    predictions = np.full(len(scores), -1, dtype=np.int64)
    predictions[scores > QUADRUPOLE_UNCLASSIFIED] = LABEL_A
    predictions[scores < -QUADRUPOLE_UNCLASSIFIED] = LABEL_B
    return predictions


def recenter_integer(weight: np.ndarray) -> np.ndarray:
    field = np.maximum(np.asarray(weight, dtype=np.float64), 0.0)
    total = float(np.sum(field))
    if total <= 0.0:
        return field.copy()
    row, col = coordinates(field.shape[0])
    x_center = float(np.sum(field * col) / total)
    y_center = float(np.sum(field * row) / total)
    return np.roll(
        field,
        (-int(round(y_center)), -int(round(x_center))),
        axis=(0, 1),
    )


def pooled_feature(weight: np.ndarray, pooled_size: int = 8) -> np.ndarray:
    field = recenter_integer(weight)
    norm = float(np.linalg.norm(field))
    if norm <= 0.0:
        return np.zeros(pooled_size * pooled_size, dtype=np.float64)
    field = field / norm
    size = field.shape[0]
    if size % pooled_size != 0:
        raise ValueError("Grid size must be divisible by pooled_size")
    block = size // pooled_size
    pooled = field.reshape(pooled_size, block, pooled_size, block).mean(axis=(1, 3))
    return pooled.ravel()


def nearest_centroid_predictions(
    train_features: np.ndarray,
    train_labels: np.ndarray,
    test_features: np.ndarray,
) -> np.ndarray:
    centroids = np.stack(
        [
            np.mean(train_features[train_labels == label], axis=0)
            for label in (LABEL_A, LABEL_B)
        ]
    )
    distances = np.linalg.norm(
        test_features[:, None, :] - centroids[None, :, :], axis=2
    )
    return np.argmin(distances, axis=1).astype(np.int64)


def class_accuracy_receipt(labels: np.ndarray, predictions: np.ndarray) -> dict[str, float]:
    class_accuracies: list[float] = []
    for label in (LABEL_A, LABEL_B):
        mask = labels == label
        if not np.any(mask):
            raise ValueError("Both labels are required")
        class_accuracies.append(float(np.mean(predictions[mask] == labels[mask])))
    balanced = 0.5 * sum(class_accuracies)
    return {
        "balanced_accuracy": balanced,
        "class_a_accuracy": class_accuracies[0],
        "class_b_accuracy": class_accuracies[1],
        "class_imbalance": abs(class_accuracies[0] - class_accuracies[1]),
    }


def balanced_accuracy(labels: np.ndarray, predictions: np.ndarray) -> float:
    return class_accuracy_receipt(labels, predictions)["balanced_accuracy"]


def observer_rng(
    channel: str,
    checkpoint_code: int,
    purpose_id: int,
) -> np.random.Generator:
    return np.random.default_rng(
        np.random.SeedSequence(
            [SEED, CHANNEL_IDS[channel], int(checkpoint_code), int(purpose_id)]
        )
    )


def permutation_p_value(
    labels: np.ndarray,
    predictions: np.ndarray,
    rng: np.random.Generator,
    permutations: int = PERMUTATIONS,
) -> float:
    observed = balanced_accuracy(labels, predictions)
    exceed = 0
    for _ in range(permutations):
        shuffled = rng.permutation(labels)
        if balanced_accuracy(shuffled, predictions) >= observed:
            exceed += 1
    return (1.0 + exceed) / (permutations + 1.0)


def _pooled_predictions_for_split(
    weights: np.ndarray,
    labels: np.ndarray,
    train_mask: np.ndarray,
    held_out_mask: np.ndarray,
) -> np.ndarray:
    features = np.stack([pooled_feature(field) for field in weights])
    return nearest_centroid_predictions(
        features[train_mask],
        labels[train_mask],
        features[held_out_mask],
    )


def score_exact_observers(
    weights: np.ndarray,
    labels: np.ndarray,
    train_mask: np.ndarray,
    held_out_mask: np.ndarray,
    *,
    channel: str,
    checkpoint_code: int,
    quadrupole_purpose: int = 10,
    pooled_purpose: int = 11,
) -> dict[str, Any]:
    q_predictions_all = quadrupole_predictions(weights)
    q_predictions = q_predictions_all[held_out_mask]
    held_labels = labels[held_out_mask]
    q_receipt = class_accuracy_receipt(held_labels, q_predictions)
    q_receipt["permutation_p"] = permutation_p_value(
        held_labels,
        q_predictions,
        observer_rng(channel, checkpoint_code, quadrupole_purpose),
    )

    pooled_predictions = _pooled_predictions_for_split(
        weights, labels, train_mask, held_out_mask
    )
    pooled_receipt = class_accuracy_receipt(held_labels, pooled_predictions)
    pooled_receipt["permutation_p"] = permutation_p_value(
        held_labels,
        pooled_predictions,
        observer_rng(channel, checkpoint_code, pooled_purpose),
    )
    return {"quadrupole": q_receipt, "pooled": pooled_receipt}


def score_passive_observers(
    weights: np.ndarray,
    labels: np.ndarray,
    train_mask: np.ndarray,
    held_out_mask: np.ndarray,
    *,
    channel: str,
    checkpoint: int,
    imprint_rms: float,
) -> dict[str, Any]:
    checkpoint_code = checkpoint + 1
    exact = score_exact_observers(
        weights,
        labels,
        train_mask,
        held_out_mask,
        channel=channel,
        checkpoint_code=checkpoint_code,
    )
    result: dict[str, Any] = {"exact": exact}
    for name, scale, noise_purpose, q_purpose, pooled_purpose in (
        ("low", 1e-4, 20, 30, 31),
        ("high", 1e-3, 21, 32, 33),
    ):
        noisy = np.asarray(weights, dtype=np.float64).copy()
        noisy += observer_rng(channel, checkpoint_code, noise_purpose).normal(
            0.0,
            scale * imprint_rms,
            size=noisy.shape,
        )
        if channel in {"phi", "mu"}:
            noisy = np.maximum(noisy, 0.0)
        result[name] = score_exact_observers(
            noisy,
            labels,
            train_mask,
            held_out_mask,
            channel=channel,
            checkpoint_code=checkpoint_code,
            quadrupole_purpose=q_purpose,
            pooled_purpose=pooled_purpose,
        )
    result["relative_signal_amplitude"] = float(
        np.median(np.sqrt(np.mean(np.asarray(weights) ** 2, axis=(1, 2))))
        / (imprint_rms + 1e-30)
    )
    return result


def passive_record_pass(score: Mapping[str, Any], *, lane_valid: bool) -> bool:
    if not lane_valid:
        return False
    if float(score["relative_signal_amplitude"]) < PASSIVE_SIGNAL_MIN:
        return False
    for observer in ("quadrupole", "pooled"):
        exact = score["exact"][observer]
        low = score["low"][observer]
        high = score["high"][observer]
        if float(exact["balanced_accuracy"]) < PASSIVE_ACCURACY_MIN:
            return False
        if float(exact["permutation_p"]) > PERMUTATION_P_MAX:
            return False
        if float(exact["class_imbalance"]) > PASSIVE_IMBALANCE_MAX:
            return False
        if (
            float(exact["balanced_accuracy"]) - float(low["balanced_accuracy"])
            > LOW_NOISE_ACCURACY_LOSS_MAX
        ):
            return False
        if float(high["balanced_accuracy"]) < HIGH_NOISE_ACCURACY_MIN:
            return False
        if float(low["permutation_p"]) > PERMUTATION_P_MAX:
            return False
        if float(high["permutation_p"]) > PERMUTATION_P_MAX:
            return False
    return True


def p0_pass(audit: Mapping[str, Any]) -> bool:
    for observer in ("quadrupole", "pooled"):
        row = audit[observer]
        if float(row["balanced_accuracy"]) < P0_ACCURACY_MIN:
            return False
        if float(row["permutation_p"]) > PERMUTATION_P_MAX:
            return False
        if float(row["class_imbalance"]) > P0_IMBALANCE_MAX:
            return False
    return float(audit["transpose_antisymmetry_error"]) <= TRANSPOSE_ANTISYMMETRY_MAX


def normalized_pair_distance(a: np.ndarray, b: np.ndarray) -> float:
    numerator = float(np.linalg.norm(np.asarray(a) - np.asarray(b)))
    denominator = (
        0.5 * (float(np.linalg.norm(a)) + float(np.linalg.norm(b))) + 1e-30
    )
    return numerator / denominator


def analytic_mu_decay(mu0: np.ndarray, *, mu_rho: float, dt: float, steps: int) -> np.ndarray:
    return np.asarray(mu0, dtype=np.float64) * (1.0 - mu_rho * dt) ** int(steps)


def single_channel_floor(d_null: float) -> float:
    return max(CAUSAL_SINGLE_ABS_FLOOR, 5.0 * float(d_null))


def full_history_floor(d_null: float) -> float:
    return max(CAUSAL_FULL_ABS_FLOOR, 10.0 * float(d_null))


def zeroing_reduction(full_value: float, zeroed_value: float) -> float:
    if full_value <= 0.0:
        return 0.0
    return 1.0 - float(zeroed_value) / float(full_value)


def ratio_within_scale(control: float, primary: float) -> bool:
    if primary <= 0.0:
        return False
    ratio = float(control) / float(primary)
    return SCALE_RATIO_MIN <= ratio <= SCALE_RATIO_MAX


def lane_valid(trace: TraceReceipt, *, mu_cap: float, require_source_off: bool) -> bool:
    if not trace.finite or trace.reset_seen:
        return False
    if trace.max_abs_psi >= 0.1 * 1e6:
        return False
    if trace.max_phi >= 0.1 * 1e6:
        return False
    if trace.max_mu >= 0.25 * float(mu_cap):
        return False
    if require_source_off and trace.source_off_psi_max > 1e-15:
        return False
    return True


def c3_cap_control_pass(
    *,
    primary_value: float,
    cap_value: float,
    primary_d_null: float,
    cap_d_null: float,
    primary_valid: bool,
    cap_valid: bool,
) -> dict[str, Any]:
    primary_floor = single_channel_floor(primary_d_null)
    cap_floor = single_channel_floor(cap_d_null)
    primary_pass = primary_valid and primary_value >= primary_floor
    cap_pass = cap_valid and cap_value >= cap_floor
    ratio: float | None = None
    ratio_pass = True
    if primary_value >= primary_floor and cap_value >= cap_floor:
        ratio = cap_value / (primary_value + 1e-30)
        ratio_pass = SCALE_RATIO_MIN <= ratio <= SCALE_RATIO_MAX
    passed = primary_valid and cap_valid and primary_pass == cap_pass and ratio_pass
    return {
        "passed": passed,
        "primary_pass": primary_pass,
        "cap_pass": cap_pass,
        "primary_floor": primary_floor,
        "cap_floor": cap_floor,
        "ratio": ratio,
        "ratio_pass": ratio_pass,
    }


def scale_control_pass(
    primary: Mapping[str, float],
    control: Mapping[str, float],
    *,
    primary_valid: bool,
    control_valid: bool,
) -> dict[str, Any]:
    primary_d_null = float(primary["C0"])
    control_d_null = float(control["C0"])
    primary_signature = {
        "C0": primary_d_null <= CAUSAL_NULL_MAX,
        "C1": float(primary["C1"]) >= full_history_floor(primary_d_null),
        "C2": float(primary["C2"]) >= single_channel_floor(primary_d_null),
        "C3": float(primary["C3"]) >= single_channel_floor(primary_d_null),
    }
    control_signature = {
        "C0": control_d_null <= CAUSAL_NULL_MAX,
        "C1": float(control["C1"]) >= full_history_floor(control_d_null),
        "C2": float(control["C2"]) >= single_channel_floor(control_d_null),
        "C3": float(control["C3"]) >= single_channel_floor(control_d_null),
    }
    ratios: dict[str, float | None] = {}
    ratios_pass = True
    for lane in ("C1", "C2", "C3"):
        primary_floor = (
            full_history_floor(primary_d_null)
            if lane == "C1"
            else single_channel_floor(primary_d_null)
        )
        control_floor = (
            full_history_floor(control_d_null)
            if lane == "C1"
            else single_channel_floor(control_d_null)
        )
        if float(primary[lane]) >= primary_floor and float(control[lane]) >= control_floor:
            ratio = float(control[lane]) / (float(primary[lane]) + 1e-30)
            ratios[lane] = ratio
            ratios_pass = ratios_pass and SCALE_RATIO_MIN <= ratio <= SCALE_RATIO_MAX
        else:
            ratios[lane] = None
    passed = (
        primary_valid
        and control_valid
        and primary_signature == control_signature
        and ratios_pass
    )
    return {
        "passed": passed,
        "primary_signature": primary_signature,
        "control_signature": control_signature,
        "ratios": ratios,
        "ratios_pass": ratios_pass,
    }


def git_blob_sha1_bytes(content: bytes) -> str:
    header = f"blob {len(content)}\0".encode("ascii")
    return hashlib.sha1(header + content).hexdigest()


def git_blob_sha1_file(path: Path) -> str:
    return git_blob_sha1_bytes(path.read_bytes())


def source_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_frozen_sources(root: Path) -> dict[str, Any]:
    checks = {
        "lineum_core/math.py": FROZEN_ENGINE_GIT_BLOB,
        "requirements.txt": FROZEN_REQUIREMENTS_GIT_BLOB,
        "requirements-dev.txt": FROZEN_REQUIREMENTS_DEV_GIT_BLOB,
    }
    actual = {path: git_blob_sha1_file(root / path) for path in checks}
    passed = all(actual[path] == expected for path, expected in checks.items())
    return {"passed": passed, "expected": checks, "actual": actual}


def core_bindings() -> tuple[type[Any], type[Any], StepFunction]:
    from lineum_core.math import CoreConfig, ExecutionPolicy, step_core

    ExecutionPolicy.init_core_determinism(
        enforce_canonical=True,
        seed=SEED,
        device_mode="numpy",
    )
    if ExecutionPolicy.uses_pytorch():
        raise RuntimeError("Q2-M1 requires the active NumPy Core path")
    return CoreConfig, ExecutionPolicy, step_core


def make_core_config(
    CoreConfig: type[Any],
    *,
    dt: float,
    mu_cap: float = 10.0,
    mu_rho: float = 0.0001,
    mu_eta: float = 0.005,
) -> Any:
    return CoreConfig(
        dt=dt,
        psi_diffusion=0.05,
        phi_diffusion=0.05,
        dissipation_rate=0.005,
        reaction_strength=0.0007,
        drift_strength=0.0,
        stencil_type="LAP4",
        physics_mode_psi="diffusion",
        disable_quantum_noise=True,
        phi_diffusion_scales_with_dt=True,
        use_mode_coupling=False,
        use_mu=True,
        mu_eta=mu_eta,
        mu_rho=mu_rho,
        mu_cap=mu_cap,
        mu_peak_cutoff_ratio=0.1,
        psi_amp_cap=1e6,
        phi_cap=1e6,
    )


def runtime_dependency_gate() -> dict[str, Any]:
    version = tuple(int(part) for part in np.__version__.split(".")[:2])
    passed = (1, 24) <= version < (2, 0)
    return {
        "passed": passed,
        "numpy_version": np.__version__,
        "required": ">=1.24,<2.0.0",
        "preferred": "1.26.4",
        "python_version": platform.python_version(),
    }


def step_with_receipt(
    state: Mapping[str, np.ndarray],
    cfg: Any,
    step_fn: StepFunction,
) -> tuple[dict[str, np.ndarray], bool, str]:
    captured = io.StringIO()
    call_state = clone_state(state)
    with redirect_stdout(captured):
        result = step_fn(call_state, cfg)
    text = captured.getvalue()
    reset_seen = FAIL_SAFE_MARKER in text
    return clone_state(result), reset_seen, text


def evolve(
    state: Mapping[str, np.ndarray],
    cfg: Any,
    steps: int,
    step_fn: StepFunction,
    *,
    source_off: bool = False,
) -> tuple[dict[str, np.ndarray], TraceReceipt]:
    out = clone_state(state)
    trace = TraceReceipt()
    trace.observe(out, source_off=source_off)
    for _ in range(int(steps)):
        out, reset_seen, _ = step_with_receipt(out, cfg, step_fn)
        trace.reset_seen = trace.reset_seen or reset_seen
        trace.steps_completed += 1
        trace.observe(out, source_off=source_off)
    return out, trace


def run_source_off(
    imprint_state: Mapping[str, np.ndarray],
    cfg: Any,
    step_fn: StepFunction,
    checkpoints: Sequence[int] = CHECKPOINTS,
) -> tuple[dict[int, dict[str, np.ndarray]], TraceReceipt]:
    relaxed = clone_state(imprint_state)
    relaxed["psi"][:] = 0.0
    receipt = TraceReceipt()
    receipt.observe(relaxed, source_off=True)
    snapshots: dict[int, dict[str, np.ndarray]] = {0: clone_state(relaxed)}
    previous = 0
    for checkpoint in checkpoints[1:]:
        segment, trace = evolve(
            relaxed,
            cfg,
            checkpoint - previous,
            step_fn,
            source_off=True,
        )
        receipt = receipt.merge(trace)
        relaxed = segment
        snapshots[int(checkpoint)] = clone_state(relaxed)
        previous = int(checkpoint)
    return snapshots, receipt


def run_history_population(
    *,
    size: int,
    schedule: Sequence[tuple[float, float, int, int]],
    imprint_cfg: Any,
    source_off_cfg: Any,
    imprint_steps: int,
    step_fn: StepFunction,
) -> list[HistoryRecord]:
    records: list[HistoryRecord] = []
    for variant_id, params in enumerate(schedule):
        psi_a, psi_b = make_orientation_pair(size, *params)
        energy_a = float(np.sum(np.abs(psi_a) ** 2))
        energy_b = float(np.sum(np.abs(psi_b) ** 2))
        rel_energy = abs(energy_a - energy_b) / max(energy_a, energy_b)
        if rel_energy > 1e-14:
            raise RuntimeError("Frozen initial label-energy equality gate failed")
        if params[2:] == (0, 0):
            sorted_error = float(
                np.max(np.abs(np.sort(np.abs(psi_a).ravel()) - np.sort(np.abs(psi_b).ravel())))
            )
            if sorted_error > 1e-14:
                raise RuntimeError("Frozen transpose amplitude-multiset gate failed")
        for label, psi in ((LABEL_A, psi_a), (LABEL_B, psi_b)):
            initial = make_state(psi)
            if not np.array_equal(initial["phi"], np.zeros_like(initial["phi"])):
                raise RuntimeError("Initial phi must be exact zero")
            if not np.array_equal(initial["mu"], np.zeros_like(initial["mu"])):
                raise RuntimeError("Initial mu must be exact zero")
            imprinted, imprint_trace = evolve(
                initial, imprint_cfg, imprint_steps, step_fn
            )
            checkpoints, source_off_trace = run_source_off(
                imprinted, source_off_cfg, step_fn
            )
            records.append(
                HistoryRecord(
                    variant_id=variant_id,
                    label=label,
                    params=tuple(params),
                    imprint_state=imprinted,
                    final_source_off_state=clone_state(checkpoints[PRIMARY_SOURCE_OFF_STEPS]),
                    checkpoints=checkpoints,
                    imprint_trace=imprint_trace,
                    source_off_trace=source_off_trace,
                )
            )
    return records


def run_source_off_from_existing_imprints(
    records: Sequence[HistoryRecord],
    cfg: Any,
    step_fn: StepFunction,
) -> list[HistoryRecord]:
    output: list[HistoryRecord] = []
    for record in records:
        checkpoints, source_off_trace = run_source_off(record.imprint_state, cfg, step_fn)
        output.append(
            HistoryRecord(
                variant_id=record.variant_id,
                label=record.label,
                params=record.params,
                imprint_state=clone_state(record.imprint_state),
                final_source_off_state=clone_state(checkpoints[PRIMARY_SOURCE_OFF_STEPS]),
                checkpoints=checkpoints,
                imprint_trace=record.imprint_trace,
                source_off_trace=source_off_trace,
            )
        )
    return output


def record_labels(records: Sequence[HistoryRecord]) -> tuple[np.ndarray, np.ndarray]:
    labels = np.asarray([record.label for record in records], dtype=np.int64)
    variant_ids = np.asarray([record.variant_id for record in records], dtype=np.int64)
    return labels, variant_ids


def masks_for_records(
    records: Sequence[HistoryRecord], schedule_size: int
) -> tuple[np.ndarray, np.ndarray]:
    _, variant_ids = record_labels(records)
    train_variants, held_variants = split_variant_masks(schedule_size)
    return train_variants[variant_ids], held_variants[variant_ids]


def checkpoint_weights(
    records: Sequence[HistoryRecord], channel: str, checkpoint: int
) -> np.ndarray:
    return np.stack(
        [field_weight(channel, record.checkpoints[checkpoint][channel]) for record in records]
    )


def imprint_rms(records: Sequence[HistoryRecord], channel: str) -> float:
    values = np.stack(
        [field_weight(channel, record.imprint_state[channel]) for record in records]
    )
    return float(np.median(np.sqrt(np.mean(values * values, axis=(1, 2)))))


def all_histories_valid(records: Sequence[HistoryRecord], *, mu_cap: float) -> bool:
    return all(
        lane_valid(record.full_trace, mu_cap=mu_cap, require_source_off=True)
        for record in records
    )


def p0_observer_audit(
    schedule: Sequence[tuple[float, float, int, int]], size: int = PRIMARY_SIZE
) -> dict[str, Any]:
    fields: list[np.ndarray] = []
    labels: list[int] = []
    variant_ids: list[int] = []
    antisymmetry_errors: list[float] = []
    for variant_id, params in enumerate(schedule):
        psi_a, psi_b = make_orientation_pair(size, *params)
        weight_a = field_weight("psi", psi_a)
        weight_b = field_weight("psi", psi_b)
        fields.extend((weight_a, weight_b))
        labels.extend((LABEL_A, LABEL_B))
        variant_ids.extend((variant_id, variant_id))
        if params[2:] == (0, 0):
            antisymmetry_errors.append(
                abs(quadrupole_score(weight_a) + quadrupole_score(weight_b))
            )
    labels_array = np.asarray(labels, dtype=np.int64)
    variant_array = np.asarray(variant_ids, dtype=np.int64)
    train_variants, held_variants = split_variant_masks(len(schedule))
    train_mask = train_variants[variant_array]
    held_mask = held_variants[variant_array]
    audit = score_exact_observers(
        np.stack(fields),
        labels_array,
        train_mask,
        held_mask,
        channel="psi",
        checkpoint_code=0,
    )
    audit["transpose_antisymmetry_error"] = max(antisymmetry_errors, default=0.0)
    audit["passed"] = p0_pass(audit)
    return audit


def passive_scores(
    records: Sequence[HistoryRecord],
    *,
    channel: str,
    schedule_size: int,
) -> dict[str, Any]:
    labels, _ = record_labels(records)
    train_mask, held_mask = masks_for_records(records, schedule_size)
    base_rms = imprint_rms(records, channel)
    scores: dict[str, Any] = {}
    for checkpoint in CHECKPOINTS:
        scores[str(checkpoint)] = score_passive_observers(
            checkpoint_weights(records, channel, checkpoint),
            labels,
            train_mask,
            held_mask,
            channel=channel,
            checkpoint=checkpoint,
            imprint_rms=base_rms,
        )
    return scores


def passive_cap_independence(
    primary_records: Sequence[HistoryRecord],
    cap_records: Sequence[HistoryRecord],
    *,
    schedule_size: int,
) -> dict[str, Any]:
    labels, _ = record_labels(primary_records)
    train_mask, held_mask = masks_for_records(primary_records, schedule_size)
    max_accuracy_difference = {"quadrupole": 0.0, "pooled": 0.0}
    checkpoint_field_differences: dict[str, float] = {}
    for checkpoint in CHECKPOINTS:
        primary_weights = checkpoint_weights(primary_records, "mu", checkpoint)
        cap_weights = checkpoint_weights(cap_records, "mu", checkpoint)
        primary_score = score_exact_observers(
            primary_weights,
            labels,
            train_mask,
            held_mask,
            channel="mu",
            checkpoint_code=checkpoint + 1,
        )
        cap_score = score_exact_observers(
            cap_weights,
            labels,
            train_mask,
            held_mask,
            channel="mu",
            checkpoint_code=checkpoint + 1,
        )
        for observer in ("quadrupole", "pooled"):
            difference = abs(
                float(primary_score[observer]["balanced_accuracy"])
                - float(cap_score[observer]["balanced_accuracy"])
            )
            max_accuracy_difference[observer] = max(
                max_accuracy_difference[observer], difference
            )
        matched = [
            normalized_pair_distance(primary, raised)
            for primary, raised in zip(primary_weights, cap_weights)
        ]
        checkpoint_field_differences[str(checkpoint)] = float(np.median(matched))
    max_primary_mu = max(record.full_trace.max_mu for record in primary_records)
    max_cap_mu = max(record.full_trace.max_mu for record in cap_records)
    field_max = max(checkpoint_field_differences.values())
    passed = (
        max_primary_mu < 0.25 * 10.0
        and max_cap_mu < 0.25 * 100.0
        and max_accuracy_difference["quadrupole"] <= PASSIVE_CAP_ACCURACY_DIFF_MAX
        and max_accuracy_difference["pooled"] <= PASSIVE_CAP_ACCURACY_DIFF_MAX
        and field_max <= PASSIVE_CAP_FIELD_DIFF_MAX
        and all_histories_valid(primary_records, mu_cap=10.0)
        and all_histories_valid(cap_records, mu_cap=100.0)
    )
    return {
        "passed": passed,
        "max_primary_mu": max_primary_mu,
        "max_cap_mu": max_cap_mu,
        "max_accuracy_difference": max_accuracy_difference,
        "checkpoint_median_normalized_field_difference": checkpoint_field_differences,
        "max_median_normalized_field_difference": field_max,
    }


def echo_pair(
    source_a: Mapping[str, np.ndarray],
    source_b: Mapping[str, np.ndarray],
    *,
    lane: str,
    common_state: np.ndarray,
    echo_cfg: Any,
    echo_steps: int,
    step_fn: StepFunction,
) -> EchoPairResult:
    a = apply_intervention(source_a, lane, common_state)
    b = apply_intervention(source_b, lane, common_state)
    common_equal = bool(np.array_equal(a["psi"], b["psi"]))
    final_a, trace_a = evolve(a, echo_cfg, echo_steps, step_fn)
    final_b, trace_b = evolve(b, echo_cfg, echo_steps, step_fn)
    divergences = {
        channel: normalized_pair_distance(final_a[channel], final_b[channel])
        for channel in ("psi", "phi", "mu")
    }
    return EchoPairResult(
        final_a=final_a,
        final_b=final_b,
        trace_a=trace_a,
        trace_b=trace_b,
        divergences=divergences,
        common_state_equal=common_equal,
    )


def causal_population(
    records: Sequence[HistoryRecord],
    *,
    lanes: Sequence[str],
    common_state: np.ndarray,
    echo_cfg: Any,
    echo_steps: int,
    step_fn: StepFunction,
    mu_cap: float,
) -> dict[str, Any]:
    by_variant: dict[int, dict[int, HistoryRecord]] = {}
    for record in records:
        by_variant.setdefault(record.variant_id, {})[record.label] = record
    rows: dict[str, list[dict[str, Any]]] = {lane: [] for lane in lanes}
    for variant_id in sorted(by_variant):
        record_a = by_variant[variant_id][LABEL_A]
        record_b = by_variant[variant_id][LABEL_B]
        for lane in lanes:
            result = echo_pair(
                record_a.final_source_off_state,
                record_b.final_source_off_state,
                lane=lane,
                common_state=common_state,
                echo_cfg=echo_cfg,
                echo_steps=echo_steps,
                step_fn=step_fn,
            )
            trace_a = record_a.full_trace.merge(result.trace_a)
            trace_b = record_b.full_trace.merge(result.trace_b)
            valid = (
                lane_valid(trace_a, mu_cap=mu_cap, require_source_off=True)
                and lane_valid(trace_b, mu_cap=mu_cap, require_source_off=True)
                and result.common_state_equal
            )
            rows[lane].append(
                {
                    "variant_id": variant_id,
                    "divergences": result.divergences,
                    "valid": valid,
                    "common_state_equal": result.common_state_equal,
                }
            )
    summary = {
        lane: {
            "median_divergence": {
                channel: float(
                    np.median([row["divergences"][channel] for row in lane_rows])
                )
                for channel in ("psi", "phi", "mu")
            },
            "valid": all(bool(row["valid"]) for row in lane_rows),
            "common_state_equal": all(
                bool(row["common_state_equal"]) for row in lane_rows
            ),
        }
        for lane, lane_rows in rows.items()
    }
    return {"rows": rows, "summary": summary}


def representative_summary(
    causal: Mapping[str, Any], variant_ids: Sequence[int] = REPRESENTATIVE_VARIANT_IDS
) -> dict[str, float]:
    result: dict[str, float] = {}
    for lane in ("C0", "C1", "C2", "C3"):
        values = [
            row["divergences"]["psi"]
            for row in causal["rows"][lane]
            if row["variant_id"] in set(variant_ids)
        ]
        if len(values) != len(variant_ids):
            raise RuntimeError(f"Missing representative rows for {lane}")
        result[lane] = float(np.median(values))
    return result


def representative_valid(
    causal: Mapping[str, Any], variant_ids: Sequence[int] = REPRESENTATIVE_VARIANT_IDS
) -> bool:
    wanted = set(variant_ids)
    return all(
        row["valid"]
        for lane in ("C0", "C1", "C2", "C3")
        for row in causal["rows"][lane]
        if row["variant_id"] in wanted
    )


def grid_control_for_pair(
    record_a: HistoryRecord,
    record_b: HistoryRecord,
    *,
    lane: str,
    common_state: np.ndarray,
    echo_cfg: Any,
    echo_steps: int,
    step_fn: StepFunction,
    mu_cap: float,
) -> dict[str, Any]:
    normal = echo_pair(
        record_a.final_source_off_state,
        record_b.final_source_off_state,
        lane=lane,
        common_state=common_state,
        echo_cfg=echo_cfg,
        echo_steps=echo_steps,
        step_fn=step_fn,
    )
    transformed_source_a = rotate_state_quarter_turn(record_b.final_source_off_state)
    transformed_source_b = rotate_state_quarter_turn(record_a.final_source_off_state)
    transformed_common = np.rot90(common_state).copy()
    transformed = echo_pair(
        transformed_source_a,
        transformed_source_b,
        lane=lane,
        common_state=transformed_common,
        echo_cfg=echo_cfg,
        echo_steps=echo_steps,
        step_fn=step_fn,
    )
    errors: dict[str, float] = {}
    for channel in ("psi", "phi", "mu"):
        error_a = normalized_pair_distance(
            transformed.final_a[channel], np.rot90(normal.final_b[channel])
        )
        error_b = normalized_pair_distance(
            transformed.final_b[channel], np.rot90(normal.final_a[channel])
        )
        errors[channel] = max(error_a, error_b)
    base_valid = (
        lane_valid(record_a.full_trace.merge(normal.trace_a), mu_cap=mu_cap, require_source_off=True)
        and lane_valid(record_b.full_trace.merge(normal.trace_b), mu_cap=mu_cap, require_source_off=True)
    )
    transformed_valid = (
        lane_valid(record_b.full_trace.merge(transformed.trace_a), mu_cap=mu_cap, require_source_off=True)
        and lane_valid(record_a.full_trace.merge(transformed.trace_b), mu_cap=mu_cap, require_source_off=True)
    )
    passed = (
        base_valid
        and transformed_valid
        and normal.common_state_equal
        and transformed.common_state_equal
        and all(value <= GRID_ERROR_MAX for value in errors.values())
    )
    return {"passed": passed, "errors": errors, "base_valid": base_valid, "transformed_valid": transformed_valid}


def representative_grid_controls(
    records: Sequence[HistoryRecord],
    *,
    common_state: np.ndarray,
    echo_cfg: Any,
    echo_steps: int,
    step_fn: StepFunction,
    mu_cap: float,
) -> dict[str, Any]:
    lookup = {(record.variant_id, record.label): record for record in records}
    result: dict[str, Any] = {}
    for lane in ("C1", "C3"):
        rows = []
        for variant_id in REPRESENTATIVE_VARIANT_IDS:
            rows.append(
                grid_control_for_pair(
                    lookup[(variant_id, LABEL_A)],
                    lookup[(variant_id, LABEL_B)],
                    lane=lane,
                    common_state=common_state,
                    echo_cfg=echo_cfg,
                    echo_steps=echo_steps,
                    step_fn=step_fn,
                    mu_cap=mu_cap,
                )
            )
        result[lane] = {
            "passed": all(row["passed"] for row in rows),
            "rows": rows,
            "max_errors": {
                channel: max(row["errors"][channel] for row in rows)
                for channel in ("psi", "phi", "mu")
            },
        }
    return result


def scaled_representative_schedule(size: int) -> list[tuple[float, float, int, int]]:
    if size == 64:
        return list(REPRESENTATIVE_PARAMS)
    if size == 96:
        scale = 96.0 / 64.0
        return [
            (separation * scale, width * scale, 0, 0)
            for separation, width, _, _ in REPRESENTATIVE_PARAMS
        ]
    raise ValueError("Only frozen representative sizes 64 and 96 are permitted")


def run_representative_control(
    *,
    CoreConfig: type[Any],
    step_fn: StepFunction,
    size: int,
    dt: float,
    imprint_steps: int,
    source_off_steps: int,
    echo_steps: int,
    common_width: float,
) -> dict[str, Any]:
    if source_off_steps != PRIMARY_SOURCE_OFF_STEPS and not (
        dt == 0.05 and source_off_steps == 2 * PRIMARY_SOURCE_OFF_STEPS
    ):
        raise ValueError("Representative source-off horizon is not frozen")
    schedule = scaled_representative_schedule(size)
    imprint_cfg = make_core_config(CoreConfig, dt=dt)
    source_cfg = replace(imprint_cfg, mu_eta=0.0, drift_strength=0.0)
    records: list[HistoryRecord] = []
    for local_variant_id, params in enumerate(schedule):
        psi_a, psi_b = make_orientation_pair(size, *params)
        for label, psi in ((LABEL_A, psi_a), (LABEL_B, psi_b)):
            imprinted, imprint_trace = evolve(make_state(psi), imprint_cfg, imprint_steps, step_fn)
            relaxed = clone_state(imprinted)
            relaxed["psi"][:] = 0.0
            final_off, source_trace = evolve(
                relaxed, source_cfg, source_off_steps, step_fn, source_off=True
            )
            records.append(
                HistoryRecord(
                    variant_id=local_variant_id,
                    label=label,
                    params=params,
                    imprint_state=imprinted,
                    final_source_off_state=final_off,
                    checkpoints={source_off_steps: clone_state(final_off)},
                    imprint_trace=imprint_trace,
                    source_off_trace=source_trace,
                )
            )
    common = make_common_state(size, common_width)
    echo_cfg = make_core_config(CoreConfig, dt=dt)
    causal = causal_population(
        records,
        lanes=("C0", "C1", "C2", "C3"),
        common_state=common,
        echo_cfg=echo_cfg,
        echo_steps=echo_steps,
        step_fn=step_fn,
        mu_cap=10.0,
    )
    values = {
        lane: float(causal["summary"][lane]["median_divergence"]["psi"])
        for lane in ("C0", "C1", "C2", "C3")
    }
    valid = all(causal["summary"][lane]["valid"] for lane in ("C0", "C1", "C2", "C3"))
    return {"values": values, "valid": valid}


def classify_primary(
    *,
    p0_valid: bool,
    primary_histories_valid: bool,
    cap_histories_valid: bool,
    passive_mu_pass: bool,
    cap_independence_pass: bool,
    causal_summary: Mapping[str, Any],
    c3_cap_pass: bool,
    full_grid_pass: bool,
    c3_grid_pass: bool,
    dt_control_pass: bool,
    resolution_control_pass: bool,
) -> dict[str, Any]:
    d_null = float(causal_summary["C0"]["median_divergence"]["psi"])
    c0_null_pass = (
        causal_summary["C0"]["valid"]
        and all(
            float(causal_summary["C0"]["median_divergence"][channel]) <= CAUSAL_NULL_MAX
            for channel in ("psi", "phi", "mu")
        )
    )
    c1_value = float(causal_summary["C1"]["median_divergence"]["psi"])
    c2_value = float(causal_summary["C2"]["median_divergence"]["psi"])
    c3_value = float(causal_summary["C3"]["median_divergence"]["psi"])
    c1_pass = causal_summary["C1"]["valid"] and c1_value >= full_history_floor(d_null)
    c2_pass = causal_summary["C2"]["valid"] and c2_value >= single_channel_floor(d_null)
    c3_single_pass = causal_summary["C3"]["valid"] and c3_value >= single_channel_floor(d_null)
    mu_zeroing_reduction = zeroing_reduction(c1_value, c2_value)
    phi_zeroing_reduction = zeroing_reduction(c1_value, c3_value)
    common_pass = all(
        bool(causal_summary[lane]["common_state_equal"])
        for lane in ("C0", "C1", "C2", "C3")
    )
    mu_primary_causal_pass = (
        c0_null_pass
        and c1_pass
        and c3_single_pass
        and mu_zeroing_reduction >= CAUSAL_ZEROING_REDUCTION_MIN
        and common_pass
    )
    all_nuisance_pass = (
        c3_cap_pass
        and full_grid_pass
        and c3_grid_pass
        and dt_control_pass
        and resolution_control_pass
    )
    mu_candidate_pass = (
        p0_valid
        and primary_histories_valid
        and cap_histories_valid
        and passive_mu_pass
        and cap_independence_pass
        and mu_primary_causal_pass
        and all_nuisance_pass
    )

    validity_pass = (
        p0_valid
        and primary_histories_valid
        and cap_histories_valid
        and c0_null_pass
        and common_pass
        and all(causal_summary[lane]["valid"] for lane in ("C1", "C2", "C3"))
    )
    if not validity_pass:
        outcome = "inconclusive_or_confounded"
    elif mu_primary_causal_pass and not all_nuisance_pass:
        outcome = "inconclusive_or_confounded"
    elif mu_candidate_pass:
        outcome = "mu_causal_reuse_candidate_retained"
    elif passive_mu_pass and not c3_single_pass:
        outcome = "mu_passive_archive_without_demonstrated_causal_reuse"
    elif c1_pass and c2_pass and not c3_single_pass:
        outcome = "phi_only_candidate_mu_only_guide_unsupported"
    elif c1_pass and not c2_pass and not c3_single_pass:
        outcome = "joint_or_distributed_history_remains_open"
    elif not c1_pass and not c2_pass and not c3_single_pass:
        outcome = "current_deterministic_phi_mu_reuse_unsupported_in_domain"
    else:
        outcome = "mixed_causal_result_requires_bounded_interpretation"

    return {
        "outcome": outcome,
        "mu_candidate_pass": mu_candidate_pass,
        "c0_null_pass": c0_null_pass,
        "c1_pass": c1_pass,
        "c2_pass": c2_pass,
        "c3_single_pass": c3_single_pass,
        "mu_primary_causal_pass": mu_primary_causal_pass,
        "mu_zeroing_reduction": mu_zeroing_reduction,
        "phi_zeroing_reduction": phi_zeroing_reduction,
        "d_null": d_null,
        "c1_floor": full_history_floor(d_null),
        "single_channel_floor": single_channel_floor(d_null),
        "all_nuisance_pass": all_nuisance_pass,
    }


def _git_head(root: Path) -> str | None:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return completed.stdout.strip() or None


def _json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, np.ndarray):
        return _json_safe(value.tolist())
    if isinstance(value, (np.floating, float)):
        numeric = float(value)
        return numeric if math.isfinite(numeric) else None
    if isinstance(value, (np.integer, int)) and not isinstance(value, bool):
        return int(value)
    if isinstance(value, (np.bool_, bool)):
        return bool(value)
    return value


def run_primary() -> dict[str, Any]:
    started = time.perf_counter()
    root = Path(__file__).resolve().parents[2]
    source_gate = verify_frozen_sources(root)
    runtime_gate = runtime_dependency_gate()
    if not source_gate["passed"]:
        raise RuntimeError("Frozen source identity gate failed")
    if not runtime_gate["passed"]:
        raise RuntimeError("Supported NumPy runtime gate failed")

    CoreConfig, ExecutionPolicy, step_fn = core_bindings()
    protocol = FrozenProtocol()
    schedule = nuisance_schedule()
    p0 = p0_observer_audit(schedule)
    if not p0["passed"]:
        raise RuntimeError("P0 observer validity gate failed")

    primary_imprint_cfg = make_core_config(CoreConfig, dt=protocol.dt, mu_cap=10.0)
    primary_source_cfg = replace(primary_imprint_cfg, mu_eta=0.0, drift_strength=0.0)
    cap_imprint_cfg = make_core_config(CoreConfig, dt=protocol.dt, mu_cap=100.0)
    cap_source_cfg = replace(cap_imprint_cfg, mu_eta=0.0, drift_strength=0.0)
    high_decay_source_cfg = replace(
        primary_source_cfg,
        mu_rho=0.01,
    )

    primary_records = run_history_population(
        size=protocol.size,
        schedule=schedule,
        imprint_cfg=primary_imprint_cfg,
        source_off_cfg=primary_source_cfg,
        imprint_steps=protocol.imprint_steps,
        step_fn=step_fn,
    )
    cap_records = run_history_population(
        size=protocol.size,
        schedule=schedule,
        imprint_cfg=cap_imprint_cfg,
        source_off_cfg=cap_source_cfg,
        imprint_steps=protocol.imprint_steps,
        step_fn=step_fn,
    )
    high_decay_records = run_source_off_from_existing_imprints(
        primary_records,
        high_decay_source_cfg,
        step_fn,
    )

    primary_histories_valid = all_histories_valid(primary_records, mu_cap=10.0)
    cap_histories_valid = all_histories_valid(cap_records, mu_cap=100.0)
    high_decay_histories_valid = all_histories_valid(high_decay_records, mu_cap=10.0)

    phi_scores = passive_scores(primary_records, channel="phi", schedule_size=len(schedule))
    mu_scores = passive_scores(primary_records, channel="mu", schedule_size=len(schedule))
    high_decay_mu_scores = passive_scores(
        high_decay_records, channel="mu", schedule_size=len(schedule)
    )
    passive_phi_final_pass = passive_record_pass(
        phi_scores[str(PRIMARY_SOURCE_OFF_STEPS)], lane_valid=primary_histories_valid
    )
    passive_mu_final_pass_raw = passive_record_pass(
        mu_scores[str(PRIMARY_SOURCE_OFF_STEPS)], lane_valid=primary_histories_valid
    )
    high_decay_mu_final_pass = passive_record_pass(
        high_decay_mu_scores[str(PRIMARY_SOURCE_OFF_STEPS)],
        lane_valid=high_decay_histories_valid,
    )
    cap_independence = passive_cap_independence(
        primary_records, cap_records, schedule_size=len(schedule)
    )
    passive_mu_final_pass = passive_mu_final_pass_raw and cap_independence["passed"]

    common = make_common_state(protocol.size, protocol.common_width)
    primary_echo_cfg = make_core_config(CoreConfig, dt=protocol.dt, mu_cap=10.0)
    cap_echo_cfg = make_core_config(CoreConfig, dt=protocol.dt, mu_cap=100.0)
    causal = causal_population(
        primary_records,
        lanes=("C0", "C1", "C2", "C3"),
        common_state=common,
        echo_cfg=primary_echo_cfg,
        echo_steps=protocol.echo_steps,
        step_fn=step_fn,
        mu_cap=10.0,
    )
    cap_causal = causal_population(
        cap_records,
        lanes=("C0", "C1", "C3"),
        common_state=common,
        echo_cfg=cap_echo_cfg,
        echo_steps=protocol.echo_steps,
        step_fn=step_fn,
        mu_cap=100.0,
    )

    d_null = float(causal["summary"]["C0"]["median_divergence"]["psi"])
    cap_d_null = float(cap_causal["summary"]["C0"]["median_divergence"]["psi"])
    c3_cap = c3_cap_control_pass(
        primary_value=float(causal["summary"]["C3"]["median_divergence"]["psi"]),
        cap_value=float(cap_causal["summary"]["C3"]["median_divergence"]["psi"]),
        primary_d_null=d_null,
        cap_d_null=cap_d_null,
        primary_valid=bool(causal["summary"]["C3"]["valid"]),
        cap_valid=bool(cap_causal["summary"]["C3"]["valid"]),
    )

    grid_controls = representative_grid_controls(
        primary_records,
        common_state=common,
        echo_cfg=primary_echo_cfg,
        echo_steps=protocol.echo_steps,
        step_fn=step_fn,
        mu_cap=10.0,
    )

    primary_rep_values = representative_summary(causal)
    primary_rep_valid = representative_valid(causal)
    dt_control_raw = run_representative_control(
        CoreConfig=CoreConfig,
        step_fn=step_fn,
        size=64,
        dt=0.05,
        imprint_steps=240,
        source_off_steps=4000,
        echo_steps=400,
        common_width=5.0,
    )
    resolution_control_raw = run_representative_control(
        CoreConfig=CoreConfig,
        step_fn=step_fn,
        size=96,
        dt=0.1,
        imprint_steps=120,
        source_off_steps=2000,
        echo_steps=200,
        common_width=7.5,
    )
    dt_control = scale_control_pass(
        primary_rep_values,
        dt_control_raw["values"],
        primary_valid=primary_rep_valid,
        control_valid=dt_control_raw["valid"],
    )
    resolution_control = scale_control_pass(
        primary_rep_values,
        resolution_control_raw["values"],
        primary_valid=primary_rep_valid,
        control_valid=resolution_control_raw["valid"],
    )

    classification = classify_primary(
        p0_valid=bool(p0["passed"]),
        primary_histories_valid=primary_histories_valid,
        cap_histories_valid=cap_histories_valid,
        passive_mu_pass=passive_mu_final_pass,
        cap_independence_pass=bool(cap_independence["passed"]),
        causal_summary=causal["summary"],
        c3_cap_pass=bool(c3_cap["passed"]),
        full_grid_pass=bool(grid_controls["C1"]["passed"]),
        c3_grid_pass=bool(grid_controls["C3"]["passed"]),
        dt_control_pass=bool(dt_control["passed"]),
        resolution_control_pass=bool(resolution_control["passed"]),
    )

    source_off_mu_analytic_errors = []
    for record in primary_records:
        predicted = analytic_mu_decay(
            record.checkpoints[0]["mu"],
            mu_rho=0.0001,
            dt=0.1,
            steps=2000,
        )
        observed = record.checkpoints[2000]["mu"]
        source_off_mu_analytic_errors.append(
            normalized_pair_distance(observed, predicted)
        )

    output: dict[str, Any] = {
        "protocol_id": "Q2-M1",
        "empirically_connected": False,
        "stage": "A_existing_mu_causal_reuse",
        "protocol": asdict(protocol),
        "source_identity_gate": source_gate,
        "runtime_gate": runtime_gate,
        "environment": {
            "python": sys.version,
            "numpy": np.__version__,
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "lineum_execution_policy": ExecutionPolicy.get_metadata(),
            "git_head": _git_head(root),
            "runner_sha256": source_sha256(Path(__file__)),
        },
        "p0_observer_audit": p0,
        "validity": {
            "primary_histories_valid": primary_histories_valid,
            "cap_raised_histories_valid": cap_histories_valid,
            "high_decay_histories_valid": high_decay_histories_valid,
            "primary_max_mu": max(record.full_trace.max_mu for record in primary_records),
            "cap_raised_max_mu": max(record.full_trace.max_mu for record in cap_records),
            "primary_source_off_psi_max": max(
                record.full_trace.source_off_psi_max for record in primary_records
            ),
            "max_source_off_mu_analytic_normalized_error": max(
                source_off_mu_analytic_errors, default=0.0
            ),
        },
        "passive": {
            "phi": phi_scores,
            "mu": mu_scores,
            "high_decay_mu": high_decay_mu_scores,
            "phi_final_retained": passive_phi_final_pass,
            "mu_final_retained_before_cap_control": passive_mu_final_pass_raw,
            "mu_final_retained": passive_mu_final_pass,
            "high_decay_mu_final_retained": high_decay_mu_final_pass,
            "cap_independence": cap_independence,
        },
        "causal": {
            "primary_summary": causal["summary"],
            "primary_rows": causal["rows"],
            "cap_raised_summary": cap_causal["summary"],
            "c3_cap_control": c3_cap,
            "grid_controls": grid_controls,
            "primary_representative_values": primary_rep_values,
            "dt_control_values": dt_control_raw["values"],
            "dt_control": dt_control,
            "resolution_control_values": resolution_control_raw["values"],
            "resolution_control": resolution_control,
        },
        "classification": classification,
        "evidence_boundary": {
            "implemented_history_dependence_only": True,
            "q2_rescue_tested": False,
            "physical_memory_field_established": False,
            "gravity_established": False,
            "quantum_memory_established": False,
            "consciousness_established": False,
            "cosmology_established": False,
        },
        "wall_clock_seconds": time.perf_counter() - started,
    }
    return _json_safe(output)


def main() -> None:
    result = run_primary()
    encoded_without_self = json.dumps(
        result,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    result["canonical_payload_sha256_without_self"] = hashlib.sha256(
        encoded_without_self
    ).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
