"""Independent scalar check for the key historical-plot reconstruction."""
from __future__ import annotations

import math
import mpmath as mp

mp.mp.dps = 50


def normalize(values):
    low, high = values[0], values[-1]
    return [(value - low) / (high - low) for value in values]


def pearson(left, right):
    mean_left = sum(left) / len(left)
    mean_right = sum(right) / len(right)
    numerator = sum(
        (a - mean_left) * (b - mean_right) for a, b in zip(left, right)
    )
    denominator = math.sqrt(
        sum((a - mean_left) ** 2 for a in left)
        * sum((b - mean_right) ** 2 for b in right)
    )
    return numerator / denominator


def euclidean(left, right):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


zeros_49 = [float(mp.im(mp.zetazero(index))) for index in range(1, 50)]
zeros_15 = zeros_49[:15]
riemann_49 = normalize(zeros_49)
riemann_15 = normalize(zeros_15)
staircase_49 = [math.floor(index / 7) / 6 for index in range(49)]
staircase_15 = [math.floor(index / 7) / 2 for index in range(15)]

pearson_49 = pearson(riemann_49, staircase_49)
euclidean_49 = euclidean(riemann_49, staircase_49)
pearson_15 = pearson(riemann_15, staircase_15)
euclidean_15 = euclidean(riemann_15, staircase_15)

assert abs(pearson_49 - 0.9842156096489157) < 1e-15
assert abs(euclidean_49 - 0.7254094546265594) < 1e-15
assert abs(pearson_15 - 0.8624831263677383) < 1e-15
assert abs(euclidean_15 - 1.1669392742086542) < 1e-15
assert [
    index
    for index in range(49)
    if index == 0 or staircase_49[index] != staircase_49[index - 1]
] == [0, 7, 14, 21, 28, 35, 42]

print(
    {
        "pearson_49": pearson_49,
        "euclidean_49": euclidean_49,
        "pearson_15": pearson_15,
        "euclidean_15": euclidean_15,
        "status": "passed",
    }
)
