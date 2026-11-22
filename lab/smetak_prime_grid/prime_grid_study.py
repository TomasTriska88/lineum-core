"""Independent reproduction of Smetak's 2D prime-grid slide counts.

Research-only study. Not a part of audited Lineum core.
Source: V. Smetak, J. Chlebnicek, B. Kostel, presentation
'Detekce prvocisel pomoci pi', https://www.youtube.com/watch?v=7ardq_YdtVQ
User-supplied presentation screenshots (80 frames) reviewed 2026-11-22.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Sequence

import numpy as np


SLIDE_COUNTS: dict[int, int] = {5000: 15_200_915, 20_000: 243_180_790}
PRIME_STAGES: tuple[int, ...] = (2, 3, 5, 7, 11)


def totient_sieve(n: int) -> list[int]:
    """Compute Euler's totient for every integer 0..n exactly."""
    if n < 1:
        raise ValueError("n must be at least one")
    phi = list(range(n + 1))
    for p in range(2, n + 1):
        if phi[p] == p:
            for multiple in range(p, n + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi


def coprime_grid_count(n: int) -> int:
    """Number of coprime integer pairs (x,y) with 1 <= x,y <= n."""
    return 2 * sum(totient_sieve(n)[1:]) - 1


def finite_euler_density(primes: Sequence[int]) -> float:
    """The remaining area fraction for prime 2D layers (infinite density)."""
    return math.prod(1.0 - 1.0 / (p * p) for p in primes)


def finite_prime_mask(n: int, primes: Sequence[int]) -> np.ndarray:
    """Mark points NOT covered by square-grid layers at (x mod p,y mod p)=(0,0).

    The coordinate convention is 1..n in both axes (not 0..n-1).
    """
    side = np.arange(1, n + 1, dtype=np.int64)
    mask = np.ones((n, n), dtype=bool)
    for prime in primes:
        mask &= ~((side[:, None] % prime == 0) & (side[None, :] % prime == 0))
    return mask


def prime_layer_from_waves(n: int, prime: int) -> np.ndarray:
    """Reconstruct the 2D prime grid as a finite sum of complex spatial waves.

    The 1D mode sum is 1 exactly at multiples of prime and 0 otherwise,
    apart from floating point roundoff. This is an identity, not a claim
    that the integer lattice physically propagates waves.
    """
    coordinates = np.arange(1, n + 1, dtype=float)
    modes = np.exp(2j * np.pi * np.outer(np.arange(prime), coordinates) / prime)
    line = modes.sum(axis=0) / prime
    return np.outer(line, line)


def finite_prime_mask_from_waves(n: int, primes: Sequence[int]) -> np.ndarray:
    """Synthesize the grid mask using spatial Fourier mode interference."""
    remaining = np.ones((n, n), dtype=np.complex128)
    for prime in primes:
        remaining *= 1 - prime_layer_from_waves(n, prime)
    return remaining


def strongest_nonzero_fft_peak(mask: np.ndarray) -> float:
    """Largest non-DC Fourier power, scaled by total pixels squared."""
    signal = mask.astype(float) - np.mean(mask.astype(float))
    f = np.fft.fft2(signal)
    f[0, 0] = 0
    return float(np.max(np.abs(f) ** 2) / signal.size**2)


def calculate(results_dir: Path, random_seed: int = 20261122, controls: int = 100) -> dict:
    """Run reproducible exact-number and spatial-periodicity controls."""
    results_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for n in (10, 100, 500, 1000, 5000, 20_000):
        count = coprime_grid_count(n)
        value = math.sqrt(6.0 * (n * n) / count)
        reported = SLIDE_COUNTS.get(n)
        rows.append({
            "side": n,
            "coprime_pairs_exact": count,
            "slide_reported_remaining_pixels": reported,
            "slide_minus_exact": None if reported is None else reported - count,
            "ratio_remaining": count / (n * n),
            "pi_from_area": value,
            "absolute_pi_error": abs(math.pi - value),
        })
    with (results_dir / "grid_counts.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    period = math.prod(PRIME_STAGES[:4])
    mask = finite_prime_mask(period, PRIME_STAGES[:4])
    actual_remaining = int(mask.sum())
    analytic_remaining = round(period * period * finite_euler_density(PRIME_STAGES[:4]))
    assert actual_remaining == analytic_remaining

    wave_mask = finite_prime_mask_from_waves(period, PRIME_STAGES[:4])
    wave_reconstruction_max_error = float(np.max(np.abs(wave_mask - mask.astype(float))))
    assert wave_reconstruction_max_error < 1e-12

    measured_peak = strongest_nonzero_fft_peak(mask)
    rng = np.random.default_rng(random_seed)
    controls_peaks = np.empty(controls, dtype=float)
    for i in range(controls):
        shuffled = rng.permutation(mask.ravel()).reshape(mask.shape)
        controls_peaks[i] = strongest_nonzero_fft_peak(shuffled)
    assert all(np.isfinite(controls_peaks))

    with (results_dir / "fft_control_peaks.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["null_seed", "maximum_non_dc_power"])
        writer.writerows((random_seed + i, v) for i, v in enumerate(controls_peaks))

    stages = []
    for k in range(1, len(PRIME_STAGES) + 1):
        primes = PRIME_STAGES[:k]
        stages.append({"primes": list(primes), "density_left": finite_euler_density(primes)})

    result = {
        "study_type": "number_theory_reference_geometry_not_lineum_implementation",
        "source_video": "https://www.youtube.com/watch?v=7ardq_YdtVQ",
        "source_credit": ["Vlastimil Smetak", "Jiri Chlebnicek", "Boris Kostel"],
        "archived_original_images": 80,
        "curated_distinct_views": 65,
        "pi": math.pi,
        "asymptotic_density": 6.0 / math.pi**2,
        "exact_grid_counts": rows,
        "finite_euler_stages": stages,
        "finite_period_2_3_5_7": period,
        "finite_period_remaining_points": actual_remaining,
        "finite_period_density": actual_remaining / (period * period),
        "wave_representation_max_absolute_error": wave_reconstruction_max_error,
        "fft_control": {
            "grid_side": period,
            "primes": [2, 3, 5, 7],
            "null_type": "randomly_permuted_binary_mask_equal_occupancy",
            "seed": random_seed,
            "null_samples": controls,
            "observed_peak_power": measured_peak,
            "null_max_peak_power": float(np.max(controls_peaks)),
            "null_median_peak_power": float(np.median(controls_peaks)),
            "fraction_null_at_least_observed": float(np.mean(controls_peaks >= measured_peak)),
        },
    }
    (results_dir / "results.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    output = calculate(Path(__file__).parent / "results")
    print(json.dumps({
        "slides": {r["side"]: {"exact": r["coprime_pairs_exact"], "reported": r["slide_reported_remaining_pixels"]} for r in output["exact_grid_counts"] if r["slide_reported_remaining_pixels"] is not None},
        "finite_period_density": output["finite_period_density"],
        "fft_control": output["fft_control"],
    }, indent=2))
