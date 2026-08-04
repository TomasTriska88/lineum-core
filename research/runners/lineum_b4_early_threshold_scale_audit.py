"""Reproduce the B4 early-Lineum threshold and scale audit.

This runner reconstructs the historical 49-point and 15-point plots from their
published metrics, compares the reconstructed staircase with declared numerical
families, and evaluates transition positions separately from rendered plateaus.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.optimize import least_squares, minimize_scalar

SEED = 20260804
N = 49


def endpoint_norm(values: np.ndarray | list[float]) -> np.ndarray:
    arr = np.asarray(values, dtype=float)
    return (arr - arr[0]) / (arr[-1] - arr[0])


def metrics(prediction: np.ndarray, target: np.ndarray) -> dict[str, float]:
    prediction = np.asarray(prediction, dtype=float)
    target = np.asarray(target, dtype=float)
    error = prediction - target
    return {
        "pearson": float(np.corrcoef(prediction, target)[0, 1]),
        "rmse": float(np.sqrt(np.mean(error**2))),
        "euclidean": float(np.linalg.norm(error)),
        "max_abs": float(np.max(np.abs(error))),
        "sse": float(np.sum(error**2)),
    }


def coefficient_of_variation(values: np.ndarray) -> float:
    arr = np.asarray(values, dtype=float)
    return float(np.std(arr) / np.mean(arr))


def build_sequences() -> dict[str, np.ndarray]:
    mp.mp.dps = 50
    riemann = np.array(
        [float(mp.im(mp.zetazero(index))) for index in range(1, N + 1)],
        dtype=float,
    )
    primes = np.array(list(sp.primerange(1, 10000))[:N], dtype=float)
    fibonacci = [1.0, 1.0]
    for _ in range(N - 2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fibonacci = np.asarray(fibonacci, dtype=float)
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    phi_power = np.asarray([phi**index for index in range(N)], dtype=float)
    beatty_phi = np.floor(np.arange(1, N + 1) * phi)
    beatty_phi2 = np.floor(np.arange(1, N + 1) * phi**2)
    riemann_unfolded = (
        riemann / (2.0 * np.pi) * np.log(riemann / (2.0 * np.pi))
        - riemann / (2.0 * np.pi)
        + 7.0 / 8.0
    )
    prime_unfolded = np.array([float(mp.li(value)) for value in primes])
    return {
        "riemann": riemann,
        "primes": primes,
        "fibonacci": fibonacci,
        "phi_power": phi_power,
        "beatty_phi": beatty_phi,
        "beatty_phi2": beatty_phi2,
        "riemann_unfolded": riemann_unfolded,
        "prime_unfolded": prime_unfolded,
    }


def main(output_path: str) -> None:
    seq = build_sequences()
    index = np.arange(N, dtype=float)
    x = index / (N - 1)
    staircase_49 = np.floor(index / 7.0) / 6.0
    riemann_49 = endpoint_norm(seq["riemann"])

    index_15 = np.arange(15, dtype=float)
    staircase_15 = np.floor(index_15 / 7.0) / 2.0
    riemann_15 = endpoint_norm(seq["riemann"][:15])

    candidates = {
        "linear_index": x,
        "riemann_raw": riemann_49,
        "riemann_unfolded": endpoint_norm(seq["riemann_unfolded"]),
        "primes_raw": endpoint_norm(seq["primes"]),
        "primes_unfolded_li": endpoint_norm(seq["prime_unfolded"]),
        "fibonacci_raw": endpoint_norm(seq["fibonacci"]),
        "fibonacci_log": endpoint_norm(np.log(seq["fibonacci"])),
        "phi_power_raw": endpoint_norm(seq["phi_power"]),
        "phi_power_log": endpoint_norm(np.log(seq["phi_power"])),
        "beatty_phi": endpoint_norm(seq["beatty_phi"]),
        "beatty_phi2": endpoint_norm(seq["beatty_phi2"]),
    }
    full_series = [
        {"candidate": name, **metrics(values, staircase_49)}
        for name, values in candidates.items()
    ]

    transition_indices = np.arange(0, 43, 7, dtype=float)
    transition_target = endpoint_norm(transition_indices)
    transition_candidates = {
        "linear": np.linspace(0.0, 1.0, 7),
        "riemann_raw": endpoint_norm(seq["riemann"][:7]),
        "riemann_unfolded": endpoint_norm(seq["riemann_unfolded"][:7]),
        "primes_raw": endpoint_norm(seq["primes"][:7]),
        "primes_unfolded_li": endpoint_norm(seq["prime_unfolded"][:7]),
        "fibonacci_raw": endpoint_norm(seq["fibonacci"][:7]),
        "phi_power_raw": endpoint_norm(seq["phi_power"][:7]),
        "beatty_phi": endpoint_norm(seq["beatty_phi"][:7]),
        "beatty_phi2": endpoint_norm(seq["beatty_phi2"][:7]),
    }
    transition_results = [
        {
            "candidate": name,
            **metrics(values, transition_target),
            "values": [float(value) for value in values],
        }
        for name, values in transition_candidates.items()
    ]

    spacings = {
        "target_equal": np.diff(transition_indices),
        "riemann_raw": np.diff(seq["riemann"][:7]),
        "riemann_unfolded": np.diff(seq["riemann_unfolded"][:7]),
        "primes_raw": np.diff(seq["primes"][:7]),
        "primes_unfolded_li": np.diff(seq["prime_unfolded"][:7]),
        "fibonacci_raw": np.diff(seq["fibonacci"][:7]),
        "phi_power_raw": np.diff(seq["phi_power"][:7]),
        "beatty_phi": np.diff(seq["beatty_phi"][:7]),
        "beatty_phi2": np.diff(seq["beatty_phi2"][:7]),
    }
    spacing_results = [
        {
            "candidate": name,
            "cv": coefficient_of_variation(values),
            "gaps": [float(value) for value in values],
        }
        for name, values in spacings.items()
    ]

    rng = np.random.default_rng(SEED)
    random_49 = []
    for _ in range(10):
        interiors = np.sort(rng.random((20000, N - 2)), axis=1)
        monotone = np.column_stack(
            [np.zeros(20000), interiors, np.ones(20000)]
        )
        random_49.append(
            np.sqrt(np.mean((monotone - staircase_49[None, :]) ** 2, axis=1))
        )
    random_49 = np.concatenate(random_49)
    interiors_7 = np.sort(rng.random((500000, 5)), axis=1)
    monotone_7 = np.column_stack(
        [np.zeros(500000), interiors_7, np.ones(500000)]
    )
    random_7 = np.sqrt(
        np.mean((monotone_7 - transition_target[None, :]) ** 2, axis=1)
    )
    for result in full_series:
        result["fraction_random_monotone_better"] = float(
            np.mean(random_49 < result["rmse"])
        )
    for result in transition_results:
        result["fraction_random_monotone_better"] = float(
            np.mean(random_7 < result["rmse"])
        )

    def half_tanh(k_value: float) -> np.ndarray:
        if k_value < 1e-8:
            return x.copy()
        return np.tanh(k_value * x) / np.tanh(k_value)

    tanh_fit = minimize_scalar(
        lambda log_k: np.mean(
            (half_tanh(float(np.exp(log_k))) - staircase_49) ** 2
        ),
        bounds=(-12.0, 6.0),
        method="bounded",
    )
    power_fit = minimize_scalar(
        lambda log_a: np.mean((x ** float(np.exp(log_a)) - staircase_49) ** 2),
        bounds=(-6.0, 6.0),
        method="bounded",
    )

    def logistic_curve(parameters: np.ndarray) -> np.ndarray:
        slope = float(np.exp(parameters[0]))
        center = float(parameters[1])
        sigmoid = lambda value: 1.0 / (
            1.0 + np.exp(-np.clip(value, -700.0, 700.0))
        )
        low = sigmoid(-slope * center)
        high = sigmoid(slope * (1.0 - center))
        return (sigmoid(slope * (x - center)) - low) / (high - low)

    logistic_fit = least_squares(
        lambda parameters: logistic_curve(parameters) - staircase_49,
        x0=np.array([0.0, 0.5]),
        bounds=(np.array([-8.0, -1.0]), np.array([8.0, 2.0])),
        xtol=1e-14,
        ftol=1e-14,
        gtol=1e-14,
        max_nfev=100000,
    )

    riemann_gaps = np.diff(seq["riemann"])
    prime_gaps = np.diff(seq["primes"])
    result = {
        "schema": "lineum-b4-early-threshold-scale-audit-1.0",
        "seed": SEED,
        "source_status": (
            "image-derived exact reconstruction verified by matching published "
            "metrics; named raw CSV unavailable on current develop"
        ),
        "screenshot_reconstruction": {
            "49_point": {
                "formula": "floor(index/7)/6",
                "pearson": float(np.corrcoef(riemann_49, staircase_49)[0, 1]),
                "euclidean": float(np.linalg.norm(riemann_49 - staircase_49)),
            },
            "15_point": {
                "formula": "floor(index/7)/2",
                "pearson": float(np.corrcoef(riemann_15, staircase_15)[0, 1]),
                "euclidean": float(np.linalg.norm(riemann_15 - staircase_15)),
            },
            "riemann_vs_linear_49": metrics(riemann_49, x),
            "staircase_vs_linear_49": metrics(staircase_49, x),
            "riemann_vs_linear_15": metrics(riemann_15, index_15 / 14.0),
        },
        "full_series_candidates": sorted(full_series, key=lambda item: item["rmse"]),
        "transition_candidates": sorted(
            transition_results, key=lambda item: item["rmse"]
        ),
        "spacing_candidates": sorted(spacing_results, key=lambda item: item["cv"]),
        "random_controls": {
            "full_49": {
                "n": int(random_49.size),
                "median": float(np.median(random_49)),
                "p05": float(np.quantile(random_49, 0.05)),
                "p01": float(np.quantile(random_49, 0.01)),
            },
            "transitions_7": {
                "n": int(random_7.size),
                "median": float(np.median(random_7)),
                "p05": float(np.quantile(random_7, 0.05)),
                "p01": float(np.quantile(random_7, 0.01)),
            },
        },
        "smooth_fits_to_drawn_staircase": {
            "linear": metrics(x, staircase_49),
            "half_tanh": {
                "parameters": {"k": float(np.exp(tanh_fit.x))},
                **metrics(half_tanh(float(np.exp(tanh_fit.x))), staircase_49),
            },
            "power": {
                "parameters": {"a": float(np.exp(power_fit.x))},
                **metrics(x ** float(np.exp(power_fit.x)), staircase_49),
            },
            "logistic": {
                "parameters": {
                    "a": float(np.exp(logistic_fit.x[0])),
                    "c": float(logistic_fit.x[1]),
                },
                **metrics(logistic_curve(logistic_fit.x), staircase_49),
            },
            "quantized_linear": {
                "formula": "floor(index/7)/6",
                "rmse": 0.0,
                "euclidean": 0.0,
                "max_abs": 0.0,
                "sse": 0.0,
            },
        },
        "gap_trends": {
            "riemann_zero_gaps": {
                "first_half_mean": float(np.mean(riemann_gaps[:24])),
                "second_half_mean": float(np.mean(riemann_gaps[24:])),
            },
            "prime_gaps": {
                "first_half_mean": float(np.mean(prime_gaps[:24])),
                "second_half_mean": float(np.mean(prime_gaps[24:])),
            },
        },
    }
    Path(output_path).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    main(args.output)
