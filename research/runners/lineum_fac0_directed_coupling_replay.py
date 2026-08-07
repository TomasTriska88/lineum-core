#!/usr/bin/env python3
"""FAC0-R1 supported-runtime directed-coupling replay for Lineum Core.

The active report preserved the FAC0 base state, CoreConfig, perturbation
amplitudes, response observables, and source-inspection graph, but not the exact
smooth localized perturbation function used by the earlier manually transcribed
checker. FAC0-R1 repairs that reproducibility defect before official execution
by freezing the explicit L2-normalized Gaussian below. It keeps the original
base state, configuration, amplitudes, matched-RNG stochastic design, and causal
question, and it executes the actual current lineum_core.math.step_core NumPy
path rather than a transcription.

This supports only an implementation-level dependency graph. It does not
validate physical energy, a physical ontology, or a need for a new field.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
from pathlib import Path
from typing import Any

os.environ["LINEUM_DEVICE"] = "numpy"

import numpy as np

from lineum_core.math import CoreConfig, ExecutionPolicy, step_core

SCHEMA = "lineum-fac0-r1-directed-coupling-replay/1"
EXPECTED_MATH_GIT_BLOB = "bb877021810691223a0eb960a45493a2e351112a"
PRIMARY_EPSILON = 1.0e-4
LINEARITY_EPSILONS = (5.0e-7, 1.0e-6, 2.0e-6)
STOCHASTIC_DELTA_AMPLITUDES = (0.01, 0.05, 0.2, 0.5)
STOCHASTIC_SEEDS = tuple(range(20))
OUTPUT_FIELDS = ("psi", "phi", "mu", "kappa")

PERTURBATION = {
    "center_x": 0.23,
    "center_y": -0.17,
    "sigma_x": 0.29,
    "sigma_y": 0.31,
    "psi_phase_radians": 0.37,
    "normalization": "discrete_l2_to_one",
}

EXPECTED_NONZERO = {
    "psi": {"psi", "phi", "mu"},
    "phi": {"psi", "phi", "mu"},
    "mu": {"psi", "phi", "mu"},
    "kappa": {"psi", "phi", "mu", "kappa"},
    "delta": set(),
}


def _git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()  # Git object identity, not security


def _repo_commit() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return None


def _clone_state(state: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value.copy() if isinstance(value, np.ndarray) else value
        for key, value in state.items()
    }


def _grid() -> tuple[np.ndarray, np.ndarray]:
    axis = np.linspace(-1.0, 1.0, 10)
    return np.meshgrid(axis, axis, indexing="ij")


def _base_state() -> dict[str, np.ndarray]:
    x, y = _grid()
    psi = (0.25 + 0.04 * np.cos(np.pi * x) * np.cos(np.pi * y)) * np.exp(
        1j * (0.3 * x - 0.2 * y)
    )
    phi = 0.35 + 0.06 * x + 0.04 * y + 0.015 * np.cos(2.0 * np.pi * x)
    kappa = 0.8 + 0.03 * np.cos(np.pi * x) * np.sin(np.pi * y)
    mu = 0.12 + 0.02 * np.sin(np.pi * x) * np.cos(np.pi * y)
    delta = 0.01 * np.sin(2.0 * np.pi * x) * np.sin(np.pi * y)
    return {"psi": psi, "phi": phi, "kappa": kappa, "mu": mu, "delta": delta}


def _config(*, stochastic: bool = False) -> CoreConfig:
    return CoreConfig(
        dt=0.1,
        psi_diffusion=0.05,
        phi_diffusion=0.05,
        drift_strength=-0.004,
        stencil_type="LAP4",
        physics_mode_psi="diffusion",
        disable_quantum_noise=not stochastic,
        phi_diffusion_scales_with_dt=True,
        use_mode_coupling=True,
        mode_coupling_strength=0.001,
        use_mu=True,
        mu_eta=0.005,
        mu_rho=0.0001,
        mu_cap=10.0,
        mu_peak_cutoff_ratio=0.1,
        psi_amp_cap=1.0e6,
        grad_cap=1.0e6,
        phi_cap=1.0e6,
        disable_pml=True,
    )


def _shape() -> np.ndarray:
    x, y = _grid()
    g = np.exp(
        -0.5
        * (
            ((x - PERTURBATION["center_x"]) / PERTURBATION["sigma_x"]) ** 2
            + ((y - PERTURBATION["center_y"]) / PERTURBATION["sigma_y"]) ** 2
        )
    )
    norm = float(np.linalg.norm(g.ravel()))
    if not np.isfinite(norm) or norm <= 0.0:
        raise RuntimeError("invalid FAC0-R1 perturbation normalization")
    return g / norm


def _perturb(
    state: dict[str, np.ndarray], field: str, epsilon: float
) -> dict[str, np.ndarray]:
    out = _clone_state(state)
    g = _shape()
    if field == "psi":
        out[field] = out[field] + epsilon * g * np.exp(
            1j * PERTURBATION["psi_phase_radians"]
        )
    else:
        out[field] = out[field] + epsilon * g
    return out


def _step(
    state: dict[str, np.ndarray], cfg: CoreConfig, *, seed: int
) -> dict[str, Any]:
    np.random.seed(seed)
    return step_core(_clone_state(state), cfg)


def _response_norms(a: dict[str, Any], b: dict[str, Any]) -> dict[str, float]:
    return {
        field: float(np.linalg.norm(np.asarray(b[field]) - np.asarray(a[field])))
        for field in OUTPUT_FIELDS
    }


def _deterministic_matrix(epsilon: float) -> dict[str, dict[str, float]]:
    state = _base_state()
    cfg = _config(stochastic=False)
    baseline = _step(state, cfg, seed=42)
    matrix: dict[str, dict[str, float]] = {}
    for field in ("psi", "phi", "mu", "kappa", "delta"):
        changed = _step(_perturb(state, field, epsilon), cfg, seed=42)
        matrix[field] = _response_norms(baseline, changed)
    return matrix


def _graph_check(matrix: dict[str, dict[str, float]]) -> dict[str, Any]:
    required_failures: list[dict[str, Any]] = []
    forbidden_failures: list[dict[str, Any]] = []
    required_threshold = PRIMARY_EPSILON * 1.0e-12
    forbidden_threshold = 1.0e-15
    for source, responses in matrix.items():
        expected = EXPECTED_NONZERO[source]
        for target, value in responses.items():
            if target in expected:
                if not (np.isfinite(value) and value > required_threshold):
                    required_failures.append(
                        {"source": source, "target": target, "value": value}
                    )
            elif not (np.isfinite(value) and value <= forbidden_threshold):
                forbidden_failures.append(
                    {"source": source, "target": target, "value": value}
                )
    return {
        "required_threshold": required_threshold,
        "forbidden_threshold": forbidden_threshold,
        "required_failures": required_failures,
        "forbidden_failures": forbidden_failures,
        "passed": not required_failures and not forbidden_failures,
    }


def _linearity() -> dict[str, Any]:
    rows: dict[str, dict[str, dict[str, float]]] = {}
    for eps in LINEARITY_EPSILONS:
        matrix = _deterministic_matrix(eps)
        rows[f"{eps:.17g}"] = {
            source: {target: value / eps for target, value in response.items()}
            for source, response in matrix.items()
        }
    primary_edges = (
        ("psi", "psi"),
        ("phi", "phi"),
        ("mu", "mu"),
        ("kappa", "kappa"),
    )
    stability: dict[str, Any] = {}
    passed = True
    for source, target in primary_edges:
        vals = [
            rows[f"{eps:.17g}"][source][target]
            for eps in LINEARITY_EPSILONS
        ]
        mean = float(np.mean(vals))
        rel_span = float((max(vals) - min(vals)) / (abs(mean) + 1.0e-30))
        stability[f"{source}->{target}"] = {
            "slopes": vals,
            "relative_span": rel_span,
        }
        passed = passed and np.isfinite(rel_span) and rel_span <= 1.0e-4
    return {"rows": rows, "primary_stability": stability, "passed": bool(passed)}


def _stochastic_delta() -> dict[str, Any]:
    state = _base_state()
    cfg = _config(stochastic=True)
    rows = []
    for amplitude in STOCHASTIC_DELTA_AMPLITUDES:
        diffs = []
        for seed in STOCHASTIC_SEEDS:
            baseline = _step(state, cfg, seed=seed)
            changed = _step(_perturb(state, "delta", amplitude), cfg, seed=seed)
            diffs.append(_response_norms(baseline, changed)["psi"])
        changed_count = sum(value > 1.0e-15 for value in diffs)
        rows.append(
            {
                "delta_perturbation_l2": amplitude,
                "changed_seeds": changed_count,
                "seed_count": len(STOCHASTIC_SEEDS),
                "maximum_psi_difference": float(max(diffs)),
                "mean_psi_difference": float(np.mean(diffs)),
            }
        )
    return {
        "rows": rows,
        "passed": rows[-1]["changed_seeds"] > 0,
        "criterion": (
            "largest frozen delta perturbation changes Psi for at least one "
            "matched-RNG seed"
        ),
    }


def _runtime_receipt() -> dict[str, Any]:
    version = tuple(int(x) for x in np.__version__.split(".")[:2])
    supported = version >= (1, 24) and version < (2, 0)
    return {
        "python": platform.python_version(),
        "numpy": np.__version__,
        "platform": platform.platform(),
        "execution_backend": ExecutionPolicy.get_metadata(),
        "repository_numpy_contract": ">=1.24,<2.0.0",
        "repository_numpy_contract_pass": supported,
    }


def run() -> dict[str, Any]:
    ExecutionPolicy.init_core_determinism(
        enforce_canonical=True, seed=42, device_mode="numpy"
    )
    math_path = Path(__file__).resolve().parents[2] / "lineum_core" / "math.py"
    math_blob = _git_blob_sha(math_path)
    matrix = _deterministic_matrix(PRIMARY_EPSILON)
    graph = _graph_check(matrix)
    linearity = _linearity()
    stochastic = _stochastic_delta()
    runtime = _runtime_receipt()

    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "status": (
            "supported_runtime_replay"
            if runtime["repository_numpy_contract_pass"]
            else "unsupported_runtime_diagnostic"
        ),
        "scientific_scope": (
            "implementation-level FAC0 directed response only; no physical-energy "
            "or ontology validation"
        ),
        "repository_commit": _repo_commit(),
        "source": {
            "math_path": "lineum_core/math.py",
            "expected_math_git_blob": EXPECTED_MATH_GIT_BLOB,
            "observed_math_git_blob": math_blob,
            "math_blob_match": math_blob == EXPECTED_MATH_GIT_BLOB,
        },
        "reproducibility_repair": {
            "prior_fac0_exact_replay_possible": False,
            "reason": (
                "prior permanent report omitted the exact smooth localized "
                "perturbation function"
            ),
            "r1_change": (
                "freeze an explicit L2-normalized anisotropic Gaussian and "
                "constant complex Psi perturbation phase before official "
                "supported-runtime execution"
            ),
            "base_state_changed": False,
            "core_config_changed": False,
            "primary_epsilon_changed": False,
            "linearity_epsilons_changed": False,
            "stochastic_delta_amplitudes_changed": False,
        },
        "perturbation": PERTURBATION,
        "primary_epsilon": PRIMARY_EPSILON,
        "deterministic_response_l2": matrix,
        "graph_check": graph,
        "linearity_check": linearity,
        "stochastic_delta_matched_rng": stochastic,
        "environment": runtime,
    }
    payload["passed"] = bool(
        runtime["repository_numpy_contract_pass"]
        and payload["source"]["math_blob_match"]
        and graph["passed"]
        and linearity["passed"]
        and stochastic["passed"]
    )
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), allow_nan=False
    )
    payload["canonical_payload_sha256_without_self"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    payload = run()
    print(
        json.dumps(
            payload,
            indent=None if args.compact else 2,
            sort_keys=True,
            allow_nan=False,
        )
    )
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
