"""Persistent reproducibility tests for the external Smetak prime-grid hypothesis."""
from __future__ import annotations

import math

import numpy as np

from prime_grid_study import coprime_grid_count, finite_euler_density, finite_prime_mask, finite_prime_mask_from_waves


def test_totient_formula_matches_brute_force():
    for side in (1, 2, 3, 4, 5, 7, 11, 17, 31):
        brute = sum(math.gcd(x, y) == 1 for x in range(1, side + 1) for y in range(1, side + 1))
        assert coprime_grid_count(side) == brute


def test_slide_5000_exact():
    assert coprime_grid_count(5_000) == 15_200_915


def test_slide_20000_differs_by_one():
    assert coprime_grid_count(20_000) == 243_180_791


def test_finite_euler_density_exact_on_product_period():
    primes = [2, 3, 5, 7]
    size = math.prod(primes)
    observed = int(finite_prime_mask(size, primes).sum())
    expected = size * size * finite_euler_density(primes)
    assert observed == round(expected)


def test_mixed_prime_layers_are_not_same_as_all_prime_sieve():
    size = 210
    primes = [2, 3, 5, 7]
    finite = int(finite_prime_mask(size, primes).sum())
    full_coprime = coprime_grid_count(size)
    assert finite >= full_coprime
    assert finite > full_coprime


def test_fft_input_preserves_expected_occupancy():
    mask = finite_prime_mask(42, [2, 3, 7])
    assert mask.dtype == np.bool_
    assert mask.shape == (42, 42)
    assert mask.sum() == round((42 * 42) * finite_euler_density([2, 3, 7]))


def test_fourier_wave_interference_is_identical_to_arithmetic_grids():
    for side, primes in [(20, [2, 3, 5]), (42, [2, 3, 7]), (60, [2, 3, 5])]:
        arith = finite_prime_mask(side, primes).astype(float)
        wave = finite_prime_mask_from_waves(side, primes)
        assert np.max(np.abs(arith - wave)) < 1e-12
