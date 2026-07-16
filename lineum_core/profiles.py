"""Named physics profiles for explicit Lineum Core time semantics."""

from __future__ import annotations

from dataclasses import replace
from typing import Any, Final

from .math import CoreConfig


LEGACY_PER_UPDATE_PROFILE: Final = "legacy-per-update-v1"
RD0_C1_CONTINUOUS_TIME_PROFILE: Final = (
    "rd0-c1-deterministic-continuous-time-v1"
)

_PROFILE_DEFAULTS: dict[str, dict[str, Any]] = {
    LEGACY_PER_UPDATE_PROFILE: {},
    RD0_C1_CONTINUOUS_TIME_PROFILE: {"dt": 0.1},
}

_PROFILE_INVARIANTS: dict[str, dict[str, Any]] = {
    LEGACY_PER_UPDATE_PROFILE: {
        "phi_diffusion_scales_with_dt": False,
    },
    RD0_C1_CONTINUOUS_TIME_PROFILE: {
        "phi_diffusion_scales_with_dt": True,
        "disable_quantum_noise": True,
        "physics_mode_psi": "diffusion",
        "stencil_type": "LAP4",
        "use_mode_coupling": False,
        "use_mu": False,
        "disable_pml": True,
    },
}


def available_core_profiles() -> tuple[str, ...]:
    """Return the stable profile names accepted by ``make_core_config``."""

    return tuple(_PROFILE_INVARIANTS)


def make_core_config(profile: str, **overrides: Any) -> CoreConfig:
    """Build a Core configuration without allowing profile identity to drift.

    Numerical parameters such as ``dt`` and diffusion coefficients may be
    varied for controlled experiments. Profile-defining values are invariants:
    callers may repeat them, but cannot silently change them.
    """

    if profile not in _PROFILE_INVARIANTS:
        supported = ", ".join(available_core_profiles())
        raise ValueError(
            f"Unknown Core profile {profile!r}; expected one of: {supported}"
        )

    invariants = _PROFILE_INVARIANTS[profile]
    conflicts = {
        name: value
        for name, value in overrides.items()
        if name in invariants and value != invariants[name]
    }
    if conflicts:
        names = ", ".join(sorted(conflicts))
        raise ValueError(
            f"Profile {profile!r} fixes the following values and cannot "
            f"override them: {names}"
        )

    values = dict(_PROFILE_DEFAULTS[profile])
    values.update(overrides)
    values.update(invariants)
    return replace(CoreConfig(), **values)
