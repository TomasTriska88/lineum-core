"""Contracts for named Lineum Core physics profiles."""

from __future__ import annotations

import pytest

from lineum_core.math import CoreConfig
from lineum_core.profiles import (
    LEGACY_PER_UPDATE_PROFILE,
    RD0_C1_CONTINUOUS_TIME_PROFILE,
    available_core_profiles,
    make_core_config,
)


def test_profile_names_are_explicit_and_discoverable():
    assert available_core_profiles() == (
        LEGACY_PER_UPDATE_PROFILE,
        RD0_C1_CONTINUOUS_TIME_PROFILE,
    )


def test_legacy_profile_preserves_the_existing_default_configuration():
    assert make_core_config(LEGACY_PER_UPDATE_PROFILE) == CoreConfig()
    assert (
        make_core_config(LEGACY_PER_UPDATE_PROFILE).phi_diffusion_scales_with_dt
        is False
    )


def test_rd0_c1_profile_selects_only_the_validated_deterministic_lane():
    config = make_core_config(RD0_C1_CONTINUOUS_TIME_PROFILE)

    assert config.dt == pytest.approx(0.1)
    assert config.phi_diffusion_scales_with_dt is True
    assert config.disable_quantum_noise is True
    assert config.physics_mode_psi == "diffusion"
    assert config.stencil_type == "LAP4"
    assert config.use_mode_coupling is False
    assert config.use_mu is False
    assert config.disable_pml is True


def test_rd0_c1_profile_allows_time_refinement_without_identity_drift():
    config = make_core_config(
        RD0_C1_CONTINUOUS_TIME_PROFILE,
        dt=0.025,
        phi_diffusion=0.02,
    )

    assert config.dt == pytest.approx(0.025)
    assert config.phi_diffusion == pytest.approx(0.02)
    assert config.phi_diffusion_scales_with_dt is True
    assert config.disable_quantum_noise is True


@pytest.mark.parametrize(
    "field,value",
    [
        ("phi_diffusion_scales_with_dt", False),
        ("disable_quantum_noise", False),
        ("physics_mode_psi", "wave_baseline"),
        ("stencil_type", "LAP8"),
        ("use_mode_coupling", True),
        ("use_mu", True),
        ("disable_pml", False),
    ],
)
def test_rd0_c1_profile_rejects_identity_changing_overrides(field, value):
    with pytest.raises(ValueError, match=field):
        make_core_config(RD0_C1_CONTINUOUS_TIME_PROFILE, **{field: value})


def test_legacy_profile_cannot_silently_enable_continuous_time_scaling():
    with pytest.raises(ValueError, match="phi_diffusion_scales_with_dt"):
        make_core_config(
            LEGACY_PER_UPDATE_PROFILE,
            phi_diffusion_scales_with_dt=True,
        )


def test_unknown_profile_fails_closed():
    with pytest.raises(ValueError, match="Unknown Core profile"):
        make_core_config("canonical")
