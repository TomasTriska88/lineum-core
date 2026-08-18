from __future__ import annotations

from dataclasses import replace
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import subprocess
import sys
import time
from typing import Any, Mapping, Sequence

import numpy as np


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PARENT_RUNNER_PATH = (
    REPOSITORY_ROOT / "research" / "runners" / "lineum_b4_q2_mu_causal_reuse.py"
)

PROTOCOL_ID = "Q2-M1-RS1"
SEED = 20260804
REFERENCE_SIZE = 96
PROSPECTIVE_SIZE = 128
EXECUTION_SIZES = (REFERENCE_SIZE, PROSPECTIVE_SIZE)
BASE_SIZE = 64
REPRESENTATIVE_VARIANT_IDS = (12, 17)
BASE_REPRESENTATIVE_PARAMS = (
    (12.0, 2.5, 0, 0),
    (12.0, 3.5, 0, 0),
)
BASE_COMMON_WIDTH = 5.0
DT = 0.1
IMPRINT_STEPS = 120
SOURCE_OFF_STEPS = 2000
ECHO_STEPS = 200
LANES = ("C0", "C1", "C2", "C3")

CAUSAL_NULL_MAX = 1e-12
CAUSAL_FULL_ABS_FLOOR = 1e-4
CAUSAL_SINGLE_ABS_FLOOR = 5e-5
CAUSAL_ZEROING_REDUCTION_MIN = 0.50
SCALE_RATIO_MIN = 0.5
SCALE_RATIO_MAX = 2.0

REQUIRED_PYTHON = "3.11.15"
REQUIRED_NUMPY = "1.26.4"
FROZEN_SOURCE_BLOBS = {
    "research/runners/lineum_b4_q2_mu_causal_reuse.py": (
        "8f818480b6b7160a49365b730bf884a4b94d9deb"
    ),
    "lineum_core/math.py": "bb877021810691223a0eb960a45493a2e351112a",
    "requirements.txt": "942f2b94b3d3f8c767451ae2d847a7b17c86d81e",
    "requirements-dev.txt": "7a0907e3e6c2d15400d19b536227a509910ae7e9",
}


def _validated_git_blob_identity(
    root: Path,
    arguments: Sequence[str],
    *,
    label: str,
) -> str:
    try:
        completed = subprocess.run(
            ["git", *arguments],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            encoding="ascii",
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        stderr = getattr(exc, "stderr", "") or ""
        detail = stderr.strip() or exc.__class__.__name__
        raise RuntimeError(f"Git source identity failed for {label}: {detail}") from exc
    identity = completed.stdout.strip().lower()
    if len(identity) != 40 or any(
        character not in "0123456789abcdef" for character in identity
    ):
        raise RuntimeError(
            f"Git source identity returned an invalid SHA-1 for {label}: {identity!r}"
        )
    return identity


def git_filtered_worktree_blob_sha1(root: Path, relative_path: str) -> str:
    return _validated_git_blob_identity(
        root,
        ["hash-object", f"--path={relative_path}", "--", relative_path],
        label=f"filtered worktree path {relative_path}",
    )


def git_head_blob_sha1(root: Path, relative_path: str) -> str:
    return _validated_git_blob_identity(
        root,
        ["rev-parse", f"HEAD:{relative_path}"],
        label=f"HEAD path {relative_path}",
    )


def verify_frozen_sources(root: Path = REPOSITORY_ROOT) -> dict[str, Any]:
    worktree = {
        path: git_filtered_worktree_blob_sha1(root, path)
        for path in FROZEN_SOURCE_BLOBS
    }
    head = {
        path: git_head_blob_sha1(root, path) for path in FROZEN_SOURCE_BLOBS
    }
    passed = all(
        worktree[path] == expected and head[path] == expected
        for path, expected in FROZEN_SOURCE_BLOBS.items()
    )
    return {
        "passed": passed,
        "method": "git_filtered_worktree_and_head_blob",
        "expected": FROZEN_SOURCE_BLOBS,
        "actual": worktree,
        "head": head,
    }


def strict_runtime_gate() -> dict[str, Any]:
    python_version = platform.python_version()
    numpy_version = np.__version__
    return {
        "passed": (
            python_version == REQUIRED_PYTHON and numpy_version == REQUIRED_NUMPY
        ),
        "python_version": python_version,
        "required_python": REQUIRED_PYTHON,
        "numpy_version": numpy_version,
        "required_numpy": REQUIRED_NUMPY,
    }


def _load_parent_runner() -> Any:
    module_name = "lineum_b4_q2_m1_frozen_parent_for_rs1"
    spec = importlib.util.spec_from_file_location(module_name, PARENT_RUNNER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load the frozen Q2-M1 parent runner")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def representative_schedule(size: int) -> tuple[tuple[float, float, int, int], ...]:
    if size not in EXECUTION_SIZES:
        raise ValueError("Q2-M1-RS1 permits representative sizes 96 and 128 only")
    scale = float(size) / float(BASE_SIZE)
    return tuple(
        (separation * scale, width * scale, shift_x, shift_y)
        for separation, width, shift_x, shift_y in BASE_REPRESENTATIVE_PARAMS
    )


def common_width(size: int) -> float:
    if size not in EXECUTION_SIZES:
        raise ValueError("Q2-M1-RS1 permits common-state sizes 96 and 128 only")
    return BASE_COMMON_WIDTH * float(size) / float(BASE_SIZE)


def full_history_floor(d_null: float) -> float:
    return max(CAUSAL_FULL_ABS_FLOOR, 10.0 * float(d_null))


def single_channel_floor(d_null: float) -> float:
    return max(CAUSAL_SINGLE_ABS_FLOOR, 5.0 * float(d_null))


def zeroing_reduction(full_value: float, zeroed_value: float) -> float:
    if full_value <= 0.0:
        return 0.0
    return 1.0 - float(zeroed_value) / float(full_value)


def run_size(
    parent: Any,
    *,
    CoreConfig: type[Any],
    step_fn: Any,
    size: int,
) -> dict[str, Any]:
    schedule = representative_schedule(size)
    imprint_cfg = parent.make_core_config(CoreConfig, dt=DT)
    source_cfg = replace(imprint_cfg, mu_eta=0.0, drift_strength=0.0)
    records: list[Any] = []

    for variant_id, params in zip(
        REPRESENTATIVE_VARIANT_IDS,
        schedule,
        strict=True,
    ):
        psi_a, psi_b = parent.make_orientation_pair(size, *params)
        for label, psi in ((parent.LABEL_A, psi_a), (parent.LABEL_B, psi_b)):
            imprinted, imprint_trace = parent.evolve(
                parent.make_state(psi),
                imprint_cfg,
                IMPRINT_STEPS,
                step_fn,
            )
            relaxed = parent.clone_state(imprinted)
            relaxed["psi"][:] = 0.0
            final_off, source_trace = parent.evolve(
                relaxed,
                source_cfg,
                SOURCE_OFF_STEPS,
                step_fn,
                source_off=True,
            )
            records.append(
                parent.HistoryRecord(
                    variant_id=variant_id,
                    label=label,
                    params=params,
                    imprint_state=imprinted,
                    final_source_off_state=final_off,
                    checkpoints={SOURCE_OFF_STEPS: parent.clone_state(final_off)},
                    imprint_trace=imprint_trace,
                    source_off_trace=source_trace,
                )
            )

    common_state = parent.make_common_state(size, common_width(size))
    echo_cfg = parent.make_core_config(CoreConfig, dt=DT)
    causal = parent.causal_population(
        records,
        lanes=LANES,
        common_state=common_state,
        echo_cfg=echo_cfg,
        echo_steps=ECHO_STEPS,
        step_fn=step_fn,
        mu_cap=10.0,
    )
    values = {
        lane: float(causal["summary"][lane]["median_divergence"]["psi"])
        for lane in LANES
    }
    c0_channel_divergences = {
        channel: float(causal["summary"]["C0"]["median_divergence"][channel])
        for channel in ("psi", "phi", "mu")
    }
    histories_valid = bool(parent.all_histories_valid(records, mu_cap=10.0))
    lanes_valid = all(bool(causal["summary"][lane]["valid"]) for lane in LANES)
    common_state_equal = all(
        bool(causal["summary"][lane]["common_state_equal"]) for lane in LANES
    )
    c0_null_pass = all(
        value <= CAUSAL_NULL_MAX for value in c0_channel_divergences.values()
    )
    valid = histories_valid and lanes_valid and common_state_equal and c0_null_pass

    return {
        "size": size,
        "scale_relative_to_n64": float(size) / float(BASE_SIZE),
        "variant_ids": REPRESENTATIVE_VARIANT_IDS,
        "schedule": schedule,
        "common_width": common_width(size),
        "values": values,
        "c0_channel_divergences": c0_channel_divergences,
        "validity": {
            "histories_valid": histories_valid,
            "lanes_valid": lanes_valid,
            "common_state_equal": common_state_equal,
            "c0_null_pass": c0_null_pass,
        },
        "valid": valid,
        "causal_summary": causal["summary"],
        "causal_rows": causal["rows"],
    }


def categorical_signature(result: Mapping[str, Any]) -> dict[str, bool]:
    values = result["values"]
    c0_channels = result["c0_channel_divergences"]
    d_null = float(values["C0"])
    return {
        "C0": all(
            float(c0_channels[channel]) <= CAUSAL_NULL_MAX
            for channel in ("psi", "phi", "mu")
        ),
        "C1": float(values["C1"]) >= full_history_floor(d_null),
        "C2": float(values["C2"]) >= single_channel_floor(d_null),
        "C3": float(values["C3"]) >= single_channel_floor(d_null),
    }


def classify_resolution_pair(
    reference: Mapping[str, Any],
    prospective: Mapping[str, Any],
) -> dict[str, Any]:
    if int(reference["size"]) != REFERENCE_SIZE:
        raise ValueError("The RS1 reference result must have size 96")
    if int(prospective["size"]) != PROSPECTIVE_SIZE:
        raise ValueError("The RS1 prospective result must have size 128")

    reference_signature = categorical_signature(reference)
    prospective_signature = categorical_signature(prospective)
    signatures_match = reference_signature == prospective_signature
    ratios: dict[str, float | None] = {}
    ratios_pass = True
    for lane in ("C1", "C2", "C3"):
        if reference_signature[lane] and prospective_signature[lane]:
            ratio = float(prospective["values"][lane]) / float(
                reference["values"][lane]
            )
            ratios[lane] = ratio
            ratios_pass = ratios_pass and SCALE_RATIO_MIN <= ratio <= SCALE_RATIO_MAX
        else:
            ratios[lane] = None

    reference_valid = bool(reference["valid"]) and reference_signature["C0"]
    prospective_valid = bool(prospective["valid"]) and prospective_signature["C0"]
    resolution_stability_pass = (
        reference_valid
        and prospective_valid
        and signatures_match
        and ratios_pass
    )
    reductions = {
        "96": zeroing_reduction(
            float(reference["values"]["C1"]),
            float(reference["values"]["C2"]),
        ),
        "128": zeroing_reduction(
            float(prospective["values"]["C1"]),
            float(prospective["values"]["C2"]),
        ),
    }

    if not reference_valid or not prospective_valid:
        outcome = "rs1_inconclusive_or_confounded"
    elif not signatures_match or not ratios_pass:
        outcome = "rs1_resolution_sensitive_unresolved"
    elif not reference_signature["C3"] and not prospective_signature["C3"]:
        outcome = "rs1_primary_mu_only_unsupported_indication"
    elif all(
        signature["C0"] and signature["C1"] and signature["C3"]
        for signature in (reference_signature, prospective_signature)
    ) and all(
        reduction >= CAUSAL_ZEROING_REDUCTION_MIN
        for reduction in reductions.values()
    ):
        outcome = "rs1_primary_mu_candidate_reopened"
    else:
        outcome = "rs1_mixed_pattern_unresolved"

    return {
        "outcome": outcome,
        "resolution_stability_pass": resolution_stability_pass,
        "signatures_match": signatures_match,
        "signatures": {
            "96": reference_signature,
            "128": prospective_signature,
        },
        "ratios": ratios,
        "ratios_pass": ratios_pass,
        "mu_zeroing_reduction": reductions,
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


def source_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    source_gate = verify_frozen_sources(REPOSITORY_ROOT)
    runtime_gate = strict_runtime_gate()
    if not source_gate["passed"]:
        raise RuntimeError("Q2-M1-RS1 frozen source identity gate failed")
    if not runtime_gate["passed"]:
        raise RuntimeError("Q2-M1-RS1 exact supported runtime gate failed")

    parent = _load_parent_runner()
    CoreConfig, ExecutionPolicy, step_fn = parent.core_bindings()
    size_results = {
        str(size): run_size(
            parent,
            CoreConfig=CoreConfig,
            step_fn=step_fn,
            size=size,
        )
        for size in EXECUTION_SIZES
    }
    classification = classify_resolution_pair(
        size_results[str(REFERENCE_SIZE)],
        size_results[str(PROSPECTIVE_SIZE)],
    )

    output = {
        "protocol_id": PROTOCOL_ID,
        "empirically_connected": False,
        "stage": "prospective_normalized_lattice_resolution_sensitivity",
        "protocol": {
            "seed": SEED,
            "execution_sizes": EXECUTION_SIZES,
            "single_new_unobserved_size": PROSPECTIVE_SIZE,
            "base_size": BASE_SIZE,
            "representative_variant_ids": REPRESENTATIVE_VARIANT_IDS,
            "base_representative_params": BASE_REPRESENTATIVE_PARAMS,
            "dt": DT,
            "imprint_steps": IMPRINT_STEPS,
            "source_off_steps": SOURCE_OFF_STEPS,
            "echo_steps": ECHO_STEPS,
            "lanes": LANES,
            "causal_null_max": CAUSAL_NULL_MAX,
            "causal_full_abs_floor": CAUSAL_FULL_ABS_FLOOR,
            "causal_single_abs_floor": CAUSAL_SINGLE_ABS_FLOOR,
            "causal_zeroing_reduction_min": CAUSAL_ZEROING_REDUCTION_MIN,
            "scale_ratio_interval": (SCALE_RATIO_MIN, SCALE_RATIO_MAX),
            "broad_or_adaptive_sweep": False,
            "continuum_convergence_claim": False,
        },
        "source_identity_gate": source_gate,
        "runtime_gate": runtime_gate,
        "environment": {
            "python": sys.version,
            "numpy": np.__version__,
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "lineum_execution_policy": ExecutionPolicy.get_metadata(),
            "git_head": _git_head(REPOSITORY_ROOT),
            "runner_sha256": source_sha256(Path(__file__)),
        },
        "size_results": size_results,
        "classification": classification,
        "evidence_boundary": {
            "normalized_lattice_sensitivity_only": True,
            "continuum_convergence_established": False,
            "retained_q2_m1_primary_reclassified": False,
            "independent_checker_run": False,
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
