"""Deterministic initial-state recipes for Core-only carrier experiments."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping

import numpy as np


@dataclass(frozen=True)
class GaussianDevelopmentalBaseline:
    """A portable recipe for constructing one deterministic Core initial state."""

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
    """Build the exact initial arrays declared by a baseline recipe."""
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
    """Build the standardized blank recipient used by Core carrier controls."""
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
