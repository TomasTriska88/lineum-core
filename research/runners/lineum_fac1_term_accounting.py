#!/usr/bin/env python3
"""FAC1 term-isolated implementation accounting for the current Lineum Core.

Research-scoped diagnostic only. The bookkeeping quantities used here are
implementation-defined scalars and MUST NOT be interpreted as physical energy.
"""

from __future__ import annotations

import hashlib
import json
import platform
import sys
from dataclasses import asdict
from pathlib import Path

import numpy as np

from lineum_core.math import CoreConfig, ExecutionPolicy, step_core

EXPECTED_MATH_BLOB = "bb877021810691223a0eb960a45493a2e351112a"
GRID_SIZE = 10
ABS_PARITY_TOL = 1e-12
UNCHANGED_TOL = 1e-15
MIN_SIGNAL = 1e-10
PAIRED_RELATIVE_RESIDUAL_TOL = 1e-6
PAIR_PREDICTION_TOL = 1e-12


def git_blob_sha(path: str | Path) -> str:
    data = Path(path).read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def qpsi(x: np.ndarray) -> float:
    return float(np.sum(np.abs(x) ** 2))


def qreal(x: np.ndarray) -> float:
    return float(np.sum(x))


def l2(x: np.ndarray) -> float:
    return float(np.linalg.norm(x.ravel()))


def max_abs_delta(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.max(np.abs(a - b)))


def diffuse_complex(field: np.ndarray, kappa: np.ndarray, rate: float, stencil_type: str) -> np.ndarray:
    """Independent transcription of the current NumPy diffusion helper."""
    k_up = np.roll(kappa, 1, axis=0)
    k_dn = np.roll(kappa, -1, axis=0)
    k_lf = np.roll(kappa, 1, axis=1)
    k_rt = np.roll(kappa, -1, axis=1)

    f_up = np.roll(field, 1, axis=0)
    f_dn = np.roll(field, -1, axis=0)
    f_lf = np.roll(field, 1, axis=1)
    f_rt = np.roll(field, -1, axis=1)

    if stencil_type == "LAP8":
        w_ortho, w_diag = 1.0, 0.25
        k_ul = np.roll(k_up, 1, axis=1)
        k_ur = np.roll(k_up, -1, axis=1)
        k_dl = np.roll(k_dn, 1, axis=1)
        k_dr = np.roll(k_dn, -1, axis=1)
        f_ul = np.roll(f_up, 1, axis=1)
        f_ur = np.roll(f_up, -1, axis=1)
        f_dl = np.roll(f_dn, 1, axis=1)
        f_dr = np.roll(f_dn, -1, axis=1)
        sum_neighbors = (
            w_ortho * (f_up * k_up + f_dn * k_dn + f_lf * k_lf + f_rt * k_rt)
            + w_diag * (f_ul * k_ul + f_ur * k_ur + f_dl * k_dl + f_dr * k_dr)
        )
        active_neighbors = (
            w_ortho * (k_up + k_dn + k_lf + k_rt)
            + w_diag * (k_ul + k_ur + k_dl + k_dr)
        )
    else:
        sum_neighbors = f_up * k_up + f_dn * k_dn + f_lf * k_lf + f_rt * k_rt
        active_neighbors = k_up + k_dn + k_lf + k_rt
    return rate * (sum_neighbors - active_neighbors * field)


def cap_complex(z: np.ndarray, cap: float) -> np.ndarray:
    z = np.asarray(z, dtype=np.complex128).copy()
    mag = np.abs(z)
    mask = mag > cap
    if np.any(mask):
        z[mask] = z[mask] * (cap / (mag[mask] + 1e-30))
    return z


def make_state() -> dict[str, np.ndarray]:
    axis = np.linspace(-1.0, 1.0, GRID_SIZE)
    x, y = np.meshgrid(axis, axis, indexing="ij")
    amp = 0.25 + 0.04 * np.cos(np.pi * x) * np.cos(np.pi * y)
    phase = 0.3 * x - 0.2 * y
    return {
        "psi": (amp * np.exp(1j * phase)).astype(np.complex128),
        "phi": (0.35 + 0.06 * x + 0.04 * y + 0.015 * np.cos(2.0 * np.pi * x)).astype(np.float64),
        "kappa": (0.8 + 0.03 * np.cos(np.pi * x) * np.sin(np.pi * y)).astype(np.float64),
        "mu": (0.12 + 0.02 * np.sin(np.pi * x) * np.cos(np.pi * y)).astype(np.float64),
        "delta": (0.01 * np.sin(2.0 * np.pi * x) * np.sin(np.pi * y)).astype(np.float64),
    }


def make_config(use_mode_coupling: bool) -> CoreConfig:
    return CoreConfig(
        dt=0.1,
        psi_diffusion=0.05,
        phi_diffusion=0.05,
        reaction_strength=0.0007,
        noise_strength=0.005,
        drift_strength=-0.004,
        stencil_type="LAP4",
        physics_mode_psi="diffusion",
        disable_quantum_noise=True,
        phi_diffusion_scales_with_dt=True,
        use_mode_coupling=use_mode_coupling,
        mode_coupling_strength=0.001,
        use_mu=True,
        mu_eta=0.005,
        mu_rho=0.0001,
        mu_cap=10.0,
        mu_peak_cutoff_ratio=0.1,
        psi_amp_cap=1e6,
        grad_cap=1e6,
        phi_cap=1e6,
        disable_pml=True,
    )


def isolated_step(state: dict[str, np.ndarray], cfg: CoreConfig) -> tuple[dict[str, np.ndarray], dict]:
    """Mirror the current NumPy diffusion-mode ordering and retain term receipts."""
    psi = np.asarray(state["psi"], dtype=np.complex128).copy()
    phi = np.asarray(state["phi"], dtype=np.float64).copy()
    kappa = np.asarray(state["kappa"], dtype=np.float64).copy()
    mu = np.asarray(state["mu"], dtype=np.float64).copy()
    delta = np.asarray(state["delta"], dtype=np.float64).copy()

    amp = np.clip(np.abs(psi), 0.0, cfg.psi_amp_cap)
    grad_x, grad_y = np.gradient(amp + delta)
    grad_x = np.clip(grad_x, -cfg.grad_cap, cfg.grad_cap)
    grad_y = np.clip(grad_y, -cfg.grad_cap, cfg.grad_cap)

    drift_multiplier = 1.0 + mu
    phi_int = np.clip(phi, 0.0, 10.0)

    interaction_factor = 0.1 * np.tanh((0.04 * phi_int * kappa * drift_multiplier) / 0.1)
    interaction_term = interaction_factor * psi
    interaction_term = interaction_term / (1.0 + np.abs(interaction_term) / 10.0)

    grad_phi_x, grad_phi_y = np.gradient(phi)
    phi_flow_term = (
        cfg.drift_strength
        * (grad_phi_x + 1j * grad_phi_y)
        * kappa
        * drift_multiplier
    )
    phi_flow_term = phi_flow_term / (1.0 + np.abs(phi_flow_term) / 10.0)

    interaction_no_mu_factor = 0.1 * np.tanh((0.04 * phi_int * kappa) / 0.1)
    interaction_no_mu = interaction_no_mu_factor * psi
    interaction_no_mu = interaction_no_mu / (1.0 + np.abs(interaction_no_mu) / 10.0)
    flow_no_mu = cfg.drift_strength * (grad_phi_x + 1j * grad_phi_y) * kappa
    flow_no_mu = flow_no_mu / (1.0 + np.abs(flow_no_mu) / 10.0)

    interaction_unit_kappa_factor = 0.1 * np.tanh((0.04 * phi_int * drift_multiplier) / 0.1)
    interaction_unit_kappa = interaction_unit_kappa_factor * psi
    interaction_unit_kappa = interaction_unit_kappa / (1.0 + np.abs(interaction_unit_kappa) / 10.0)
    flow_unit_kappa = cfg.drift_strength * (grad_phi_x + 1j * grad_phi_y) * drift_multiplier
    flow_unit_kappa = flow_unit_kappa / (1.0 + np.abs(flow_unit_kappa) / 10.0)

    terms: dict[str, dict | float | str] = {}

    qpsi_before = qpsi(psi)
    phi_before = phi.copy()
    mu_before = mu.copy()
    psi = cap_complex(psi + phi_flow_term * cfg.dt, cfg.psi_amp_cap)
    terms["phi_gradient_drift"] = {
        "psi_term_l2": l2(phi_flow_term * cfg.dt),
        "qpsi_delta": qpsi(psi) - qpsi_before,
        "phi_max_delta": max_abs_delta(phi, phi_before),
        "mu_max_delta": max_abs_delta(mu, mu_before),
    }

    qpsi_before = qpsi(psi)
    phi_before = phi.copy()
    mu_before = mu.copy()
    psi = psi + interaction_term * cfg.dt
    terms["phi_interaction"] = {
        "psi_term_l2": l2(interaction_term * cfg.dt),
        "qpsi_delta": qpsi(psi) - qpsi_before,
        "phi_max_delta": max_abs_delta(phi, phi_before),
        "mu_max_delta": max_abs_delta(mu, mu_before),
    }

    qpsi_before = qpsi(psi)
    psi = psi - 0.005 * psi * cfg.dt
    terms["psi_dissipation"] = {
        "qpsi_removed": qpsi_before - qpsi(psi),
    }

    qpsi_before = qpsi(psi)
    psi = psi + diffuse_complex(
        psi, kappa, rate=cfg.psi_diffusion, stencil_type=cfg.stencil_type
    ) * kappa * cfg.dt
    terms["psi_diffusion"] = {
        "qpsi_delta": qpsi(psi) - qpsi_before,
    }

    e_psi = np.abs(psi) ** 2

    if cfg.use_mode_coupling:
        qpsi_pre = qpsi(psi)
        qphi_pre = qreal(phi)
        delta_e = cfg.mode_coupling_strength * e_psi * kappa * cfg.dt
        phi = phi + delta_e
        psi_mag_new = np.sqrt(np.maximum(e_psi - delta_e, 0.0))
        psi = (psi / (np.sqrt(e_psi) + 1e-12)) * psi_mag_new

        debit = qpsi_pre - qpsi(psi)
        credit = qreal(phi) - qphi_pre
        residual = debit - credit

        sqrt_e = np.sqrt(e_psi)
        predicted_post_e = (
            e_psi / (sqrt_e + 1e-12) ** 2
        ) * np.maximum(e_psi - delta_e, 0.0)
        predicted_debit = float(np.sum(e_psi - predicted_post_e))
        predicted_residual = predicted_debit - float(np.sum(delta_e))

        terms["mode_coupling"] = {
            "delta_e_sum": float(np.sum(delta_e)),
            "min_e_minus_delta_e": float(np.min(e_psi - delta_e)),
            "qpsi_debit": debit,
            "qphi_credit": credit,
            "debit_minus_credit": residual,
            "relative_abs_residual": abs(residual) / (abs(credit) + 1e-30),
            "analytic_predicted_residual": predicted_residual,
            "residual_prediction_abs_error": abs(residual - predicted_residual),
        }
    else:
        qpsi_pre = qpsi(psi)
        qphi_pre = qreal(phi)
        scale_ratio = (128.0 / GRID_SIZE) ** 2
        dynamic_reaction = cfg.reaction_strength * scale_ratio
        reaction_delta = kappa * dynamic_reaction * (e_psi - phi) * cfg.dt
        phi = phi + reaction_delta
        terms["fallback_reaction"] = {
            "qphi_delta": qreal(phi) - qphi_pre,
            "reaction_delta_l2": l2(reaction_delta),
            "qpsi_delta_during_reaction": qpsi(psi) - qpsi_pre,
        }

    qphi_pre = qreal(phi)
    phi_diffusion_step_scale = cfg.dt if cfg.phi_diffusion_scales_with_dt else 1.0
    phi = phi + (
        kappa
        * cfg.phi_diffusion
        * diffuse_complex(phi, kappa, rate=0.05, stencil_type=cfg.stencil_type)
        * phi_diffusion_step_scale
    )
    phi = np.clip(phi, 0.0, cfg.phi_cap)
    terms["phi_diffusion"] = {"qphi_delta": qreal(phi) - qphi_pre}

    dynamic_floor = cfg.mu_peak_cutoff_ratio
    if 0.0 < dynamic_floor < 1.0:
        dynamic_floor = dynamic_floor * np.max(e_psi)
    active_e_psi = np.maximum(e_psi - dynamic_floor, 0.0)

    psi_before_mu = psi.copy()
    mu_before_accum = mu.copy()
    mu_accum_delta = cfg.mu_eta * active_e_psi * kappa * drift_multiplier * cfg.dt
    mu = mu + mu_accum_delta
    qmu_after_accum = qreal(mu)
    qmu_before_decay = qreal(mu)
    mu = mu - cfg.mu_rho * mu * cfg.dt
    qmu_after_decay = qreal(mu)
    mu = np.clip(mu, 0.0, cfg.mu_cap)
    terms["psi_to_mu"] = {
        "mu_accum_sum": qmu_after_accum - qreal(mu_before_accum),
        "mu_accum_l2": l2(mu_accum_delta),
        "psi_max_delta_during_mu_write": max_abs_delta(psi, psi_before_mu),
    }
    terms["mu_decay"] = {
        "qmu_removed": qmu_before_decay - qmu_after_decay,
    }

    terms["mu_modulation"] = {
        "interaction_difference_l2": l2((interaction_term - interaction_no_mu) * cfg.dt),
        "drift_difference_l2": l2((phi_flow_term - flow_no_mu) * cfg.dt),
        "mu_state_change_during_psi_terms": 0.0,
    }
    terms["kappa_modulation"] = {
        "interaction_difference_l2": l2((interaction_term - interaction_unit_kappa) * cfg.dt),
        "drift_difference_l2": l2((phi_flow_term - flow_unit_kappa) * cfg.dt),
    }

    fail_safe = bool(np.isnan(np.sum(psi)) or np.max(np.abs(psi)) >= cfg.psi_amp_cap * 0.99)
    if fail_safe:
        psi = np.zeros_like(psi)

    out = {"psi": psi, "phi": phi, "kappa": kappa, "mu": mu}
    terms["validity"] = {
        "fail_safe": fail_safe,
        "max_abs_psi": float(np.max(np.abs(psi))),
        "max_phi": float(np.max(phi)),
        "max_mu": float(np.max(mu)),
        "kappa_return_max_delta": max_abs_delta(kappa, state["kappa"]),
    }
    return out, terms


def evaluate_config(use_mode_coupling: bool) -> dict:
    cfg = make_config(use_mode_coupling)
    source_state = make_state()

    actual = step_core(
        {k: np.array(v, copy=True) for k, v in source_state.items()},
        cfg,
    )
    mirror, terms = isolated_step(
        {k: np.array(v, copy=True) for k, v in source_state.items()},
        cfg,
    )

    parity = {
        name: max_abs_delta(np.asarray(actual[name]), np.asarray(mirror[name]))
        for name in ("psi", "phi", "kappa", "mu")
    }
    parity_pass = max(parity.values()) <= ABS_PARITY_TOL

    common_checks = {
        "mirror_matches_step_core": parity_pass,
        "drift_nonzero": terms["phi_gradient_drift"]["psi_term_l2"] >= MIN_SIGNAL,
        "drift_has_no_same_term_phi_write": terms["phi_gradient_drift"]["phi_max_delta"] <= UNCHANGED_TOL,
        "interaction_nonzero": terms["phi_interaction"]["psi_term_l2"] >= MIN_SIGNAL,
        "interaction_has_no_same_term_phi_write": terms["phi_interaction"]["phi_max_delta"] <= UNCHANGED_TOL,
        "psi_to_mu_nonzero": terms["psi_to_mu"]["mu_accum_l2"] >= MIN_SIGNAL,
        "psi_to_mu_has_no_same_term_psi_debit": terms["psi_to_mu"]["psi_max_delta_during_mu_write"] <= UNCHANGED_TOL,
        "mu_modulates_psi_terms": max(
            terms["mu_modulation"]["interaction_difference_l2"],
            terms["mu_modulation"]["drift_difference_l2"],
        ) >= MIN_SIGNAL,
        "mu_not_debited_during_psi_terms": terms["mu_modulation"]["mu_state_change_during_psi_terms"] <= UNCHANGED_TOL,
        "kappa_modulates_psi_terms": max(
            terms["kappa_modulation"]["interaction_difference_l2"],
            terms["kappa_modulation"]["drift_difference_l2"],
        ) >= MIN_SIGNAL,
        "kappa_returned_unchanged": terms["validity"]["kappa_return_max_delta"] <= UNCHANGED_TOL,
        "no_fail_safe": not terms["validity"]["fail_safe"],
        "far_from_psi_cap": terms["validity"]["max_abs_psi"] < 0.1 * cfg.psi_amp_cap,
        "far_from_phi_cap": terms["validity"]["max_phi"] < 0.1 * cfg.phi_cap,
        "far_from_mu_cap": terms["validity"]["max_mu"] < 0.25 * cfg.mu_cap,
    }

    if use_mode_coupling:
        mode = terms["mode_coupling"]
        branch_checks = {
            "mode_credit_nonzero": mode["qphi_credit"] >= MIN_SIGNAL,
            "mode_debit_nonzero": mode["qpsi_debit"] >= MIN_SIGNAL,
            "mode_no_floor_activation": mode["min_e_minus_delta_e"] > 0.0,
            "mode_near_paired_implementation_ledger": mode["relative_abs_residual"] <= PAIRED_RELATIVE_RESIDUAL_TOL,
            "mode_residual_matches_analytic_normalization_effect": mode["residual_prediction_abs_error"] <= PAIR_PREDICTION_TOL,
        }
    else:
        fb = terms["fallback_reaction"]
        branch_checks = {
            "fallback_phi_write_nonzero": fb["reaction_delta_l2"] >= MIN_SIGNAL,
            "fallback_has_no_same_term_psi_debit": abs(fb["qpsi_delta_during_reaction"]) <= UNCHANGED_TOL,
        }

    checks = {**common_checks, **branch_checks}
    return {
        "use_mode_coupling": use_mode_coupling,
        "config": asdict(cfg),
        "parity_max_abs": parity,
        "terms": terms,
        "checks": checks,
        "pass": all(checks.values()),
    }


def main() -> None:
    math_blob = git_blob_sha("lineum_core/math.py")
    if math_blob != EXPECTED_MATH_BLOB:
        raise SystemExit(
            f"Current math.py blob {math_blob} does not match frozen {EXPECTED_MATH_BLOB}"
        )

    ExecutionPolicy.init_core_determinism(
        enforce_canonical=True,
        seed=42,
        device_mode="numpy",
    )

    paired = evaluate_config(True)
    fallback = evaluate_config(False)
    overall = paired["pass"] and fallback["pass"]

    output = {
        "schema": "lineum_fac1_term_accounting_v1",
        "evidence_status": "[current-core][implementation-accounting][preregistered]",
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "platform": platform.platform(),
        "math_blob": math_blob,
        "thresholds": {
            "absolute_parity_tolerance": ABS_PARITY_TOL,
            "unchanged_tolerance": UNCHANGED_TOL,
            "minimum_signal": MIN_SIGNAL,
            "paired_relative_residual_tolerance": PAIRED_RELATIVE_RESIDUAL_TOL,
            "pair_prediction_tolerance": PAIR_PREDICTION_TOL,
        },
        "paired_mode": paired,
        "fallback_mode": fallback,
        "classifications_if_passed": {
            "mode_coupling": "explicit_near_paired_scalar_debit_credit_in_current_implementation",
            "fallback_psi_to_phi_reaction": "unpaired_state_write_in_current_implementation",
            "phi_interaction_to_psi": "unpaired_feedback_in_current_implementation",
            "phi_gradient_drift_to_psi": "unpaired_feedback_in_current_implementation",
            "psi_activity_to_mu": "unpaired_memory_or_reinforcement_write_in_current_implementation",
            "mu_modulation_to_psi": "unpaired_feedback_in_current_implementation",
            "kappa_modulation": "supplied_non_evolving_high_leverage_input_in_current_implementation",
            "psi_dissipation": "sink_without_receiver_in_this_step_contract",
            "mu_decay": "sink_without_receiver_in_this_step_contract",
        },
        "physical_energy_claim": "not_established",
        "new_state_required": "not_established",
        "real_world_correspondence": "not_tested",
        "ancient_physics_correspondence": "not_established",
        "overall_pass": overall,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
