#!/usr/bin/env python3
"""FAC2-R1 componentwise software accounting for the current NumPy diffusion Core.

Research-scoped diagnostic only. The bookkeeping observables are implementation-defined
and MUST NOT be interpreted as a common physical energy, charge, mass, or invariant.
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import platform
from dataclasses import replace
from pathlib import Path

import numpy as np

from lineum_core.math import CoreConfig, ExecutionPolicy, step_core

EXPECTED_MATH_BLOB = "bb877021810691223a0eb960a45493a2e351112a"
GRID_SIZE = 10
ABS_PARITY_TOL = 1e-12
LEDGER_RESIDUAL_TOL = 1e-12
UNCHANGED_TOL = 1e-15
MIN_SIGNAL = 1e-10
SEED = 0


def git_blob_sha(path: str | Path) -> str:
    data = Path(path).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def qpsi(x: np.ndarray) -> float:
    return float(np.sum(np.abs(x) ** 2))


def qreal(x: np.ndarray) -> float:
    return float(np.sum(x))


def l2(x: np.ndarray) -> float:
    return float(np.linalg.norm(np.asarray(x).ravel()))


def max_abs_delta(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.max(np.abs(np.asarray(a) - np.asarray(b))))


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


def cap_complex(z: np.ndarray, cap: float) -> tuple[np.ndarray, int]:
    z = np.asarray(z, dtype=np.complex128).copy()
    mag = np.abs(z)
    mask = mag > cap
    count = int(np.count_nonzero(mask))
    if count:
        z[mask] = z[mask] * (cap / (mag[mask] + 1e-30))
    return z, count


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


def make_config(
    *,
    use_mode_coupling: bool = True,
    noise: bool = False,
    disable_pml: bool = True,
    psi_amp_cap: float = 1e6,
    phi_cap: float = 1e6,
    mu_cap: float = 10.0,
    fold_mode: str = "softabs",
    fold_scope: str = "escape",
) -> CoreConfig:
    return CoreConfig(
        dt=0.1,
        psi_diffusion=0.05,
        phi_diffusion=0.05,
        reaction_strength=0.0007,
        noise_strength=0.005,
        drift_strength=-0.004,
        stencil_type="LAP4",
        physics_mode_psi="diffusion",
        disable_quantum_noise=not noise,
        phi_diffusion_scales_with_dt=True,
        use_mode_coupling=use_mode_coupling,
        mode_coupling_strength=0.001,
        use_mu=True,
        mu_eta=0.005,
        mu_rho=0.0001,
        mu_cap=mu_cap,
        mu_peak_cutoff_ratio=0.1,
        psi_amp_cap=psi_amp_cap,
        grad_cap=1e6,
        phi_cap=phi_cap,
        fold_mode=fold_mode,
        fold_scope=fold_scope,
        disable_pml=disable_pml,
    )


def snapshot_quantities(psi: np.ndarray, phi: np.ndarray, mu: np.ndarray) -> dict[str, float]:
    return {"qpsi": qpsi(psi), "qphi": qreal(phi), "qmu": qreal(mu)}


def delta_receipt(before: dict[str, float], after: dict[str, float]) -> dict[str, float]:
    return {name: after[name] - before[name] for name in before}


def isolated_step(
    state: dict[str, np.ndarray],
    cfg: CoreConfig,
    *,
    seed: int = SEED,
) -> tuple[dict[str, np.ndarray], dict]:
    """Mirror the exact current NumPy diffusion ordering and retain block receipts."""
    psi = np.asarray(state["psi"], dtype=np.complex128).copy()
    phi = np.asarray(state["phi"], dtype=np.float64).copy()
    kappa = np.asarray(state["kappa"], dtype=np.float64).copy()
    mu = np.asarray(state["mu"], dtype=np.float64).copy()
    delta = np.asarray(state["delta"], dtype=np.float64).copy()

    initial = snapshot_quantities(psi, phi, mu)
    receipts: dict[str, dict] = {}
    rng = np.random.RandomState(seed)

    amp = np.clip(np.abs(psi), 0.0, cfg.psi_amp_cap)
    grad_x, grad_y = np.gradient(amp + delta)
    grad_x = np.clip(grad_x, -cfg.grad_cap, cfg.grad_cap)
    grad_y = np.clip(grad_y, -cfg.grad_cap, cfg.grad_cap)
    grad_mag = np.sqrt(np.clip(grad_x**2 + grad_y**2, 0.0, 1e12))

    if cfg.disable_quantum_noise:
        linon_complex = np.zeros_like(psi)
        fluctuation = np.zeros_like(psi)
        linon_count = 0
    else:
        probability = (1.0 / (1.0 + np.exp(-5.0 * (amp + grad_mag)))) * kappa
        linons = (rng.rand(GRID_SIZE, GRID_SIZE) < probability).astype(np.float64)
        linon_count = int(np.count_nonzero(linons))
        linon_effect = np.clip(
            (0.03 + 0.02 * np.clip(amp, a_min=0, a_max=None)) * linons,
            0.0,
            10.0,
        )
        linon_complex = linon_effect * np.exp(1j * np.angle(psi))
        fluctuation = np.clip(
            rng.normal(0.0, cfg.noise_strength, (GRID_SIZE, GRID_SIZE)),
            -1.0,
            1.0,
        ) * np.exp(1j * np.angle(psi))

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

    before = snapshot_quantities(psi, phi, mu)
    psi = psi + phi_flow_term * cfg.dt
    after = snapshot_quantities(psi, phi, mu)
    receipts["psi_drift"] = {
        "observable_delta": delta_receipt(before, after),
        "state_increment_l2": l2(phi_flow_term * cfg.dt),
    }

    before = snapshot_quantities(psi, phi, mu)
    psi, psi_cap_count = cap_complex(psi, cfg.psi_amp_cap)
    after = snapshot_quantities(psi, phi, mu)
    receipts["psi_cap_after_drift"] = {
        "observable_delta": delta_receipt(before, after),
        "trigger_count": psi_cap_count,
    }

    source_increment = (linon_complex + fluctuation) * kappa * cfg.dt
    interaction_increment = interaction_term * cfg.dt
    combined_increment = source_increment + interaction_increment
    psi_before_add = psi.copy()
    before = snapshot_quantities(psi, phi, mu)
    psi = psi + combined_increment
    after = snapshot_quantities(psi, phi, mu)
    psi_after_interaction_only = psi_before_add + interaction_increment
    psi_after_source_only = psi_before_add + source_increment
    receipts["psi_source_plus_interaction"] = {
        "observable_delta": delta_receipt(before, after),
        "source_increment_l2": l2(source_increment),
        "interaction_increment_l2": l2(interaction_increment),
        "combined_increment_l2": l2(combined_increment),
        "linon_count": linon_count,
        "source_qpsi_marginal_given_interaction": qpsi(psi) - qpsi(psi_after_interaction_only),
        "interaction_qpsi_marginal_given_source": qpsi(psi) - qpsi(psi_after_source_only),
        "scalar_partition_note": "marginals_are_counterfactual_diagnostics_not_additive_ledger_terms",
    }

    before = snapshot_quantities(psi, phi, mu)
    psi = psi - 0.005 * psi * cfg.dt
    after = snapshot_quantities(psi, phi, mu)
    receipts["psi_dissipation"] = {"observable_delta": delta_receipt(before, after)}

    before = snapshot_quantities(psi, phi, mu)
    psi = psi + diffuse_complex(
        psi, kappa, rate=cfg.psi_diffusion, stencil_type=cfg.stencil_type
    ) * kappa * cfg.dt
    after = snapshot_quantities(psi, phi, mu)
    receipts["psi_diffusion"] = {"observable_delta": delta_receipt(before, after)}

    e_psi = np.abs(psi) ** 2

    if cfg.use_mode_coupling:
        before = snapshot_quantities(psi, phi, mu)
        delta_e = cfg.mode_coupling_strength * e_psi * kappa * cfg.dt
        phi = phi + delta_e
        psi_mag_new = np.sqrt(np.maximum(e_psi - delta_e, 0.0))
        psi = (psi / (np.sqrt(e_psi) + 1e-12)) * psi_mag_new
        after = snapshot_quantities(psi, phi, mu)
        receipts["mode_coupling"] = {
            "observable_delta": delta_receipt(before, after),
            "delta_e_sum": float(np.sum(delta_e)),
            "min_e_minus_delta_e": float(np.min(e_psi - delta_e)),
        }
    else:
        before = snapshot_quantities(psi, phi, mu)
        scale_ratio = (128.0 / GRID_SIZE) ** 2
        dynamic_reaction = cfg.reaction_strength * scale_ratio
        reaction_delta = kappa * dynamic_reaction * (e_psi - phi) * cfg.dt
        phi = phi + reaction_delta
        after = snapshot_quantities(psi, phi, mu)
        receipts["fallback_reaction"] = {
            "observable_delta": delta_receipt(before, after),
            "reaction_increment_l2": l2(reaction_delta),
        }

    before = snapshot_quantities(psi, phi, mu)
    phi = phi + (
        kappa
        * cfg.phi_diffusion
        * diffuse_complex(phi, kappa, rate=0.05, stencil_type=cfg.stencil_type)
        * (cfg.dt if cfg.phi_diffusion_scales_with_dt else 1.0)
    )
    after = snapshot_quantities(psi, phi, mu)
    receipts["phi_diffusion_raw"] = {"observable_delta": delta_receipt(before, after)}

    before = snapshot_quantities(psi, phi, mu)
    phi_pre_clip = phi.copy()
    phi = np.clip(phi, 0.0, cfg.phi_cap)
    phi_clip_count = int(np.count_nonzero(phi != phi_pre_clip))
    after = snapshot_quantities(psi, phi, mu)
    receipts["phi_clip"] = {
        "observable_delta": delta_receipt(before, after),
        "trigger_count": phi_clip_count,
    }

    if cfg.use_mu:
        dynamic_floor = cfg.mu_peak_cutoff_ratio
        if 0.0 < dynamic_floor < 1.0:
            dynamic_floor = dynamic_floor * np.max(e_psi)
        active_e_psi = np.maximum(e_psi - dynamic_floor, 0.0)

        before = snapshot_quantities(psi, phi, mu)
        mu = mu + cfg.mu_eta * active_e_psi * kappa * drift_multiplier * cfg.dt
        after = snapshot_quantities(psi, phi, mu)
        receipts["mu_accumulation"] = {"observable_delta": delta_receipt(before, after)}

        before = snapshot_quantities(psi, phi, mu)
        mu = mu - cfg.mu_rho * mu * cfg.dt
        after = snapshot_quantities(psi, phi, mu)
        receipts["mu_decay"] = {"observable_delta": delta_receipt(before, after)}

        before = snapshot_quantities(psi, phi, mu)
        mu_pre_clip = mu.copy()
        mu = np.clip(mu, 0.0, cfg.mu_cap)
        mu_clip_count = int(np.count_nonzero(mu != mu_pre_clip))
        after = snapshot_quantities(psi, phi, mu)
        receipts["mu_clip"] = {
            "observable_delta": delta_receipt(before, after),
            "trigger_count": mu_clip_count,
        }
    else:
        mu_clip_count = 0

    before = snapshot_quantities(psi, phi, mu)
    fail_safe = bool(np.isnan(np.sum(psi)) or np.max(np.abs(psi)) >= cfg.psi_amp_cap * 0.99)
    if fail_safe:
        psi = np.zeros_like(psi)
    after = snapshot_quantities(psi, phi, mu)
    receipts["psi_fail_safe_reset"] = {
        "observable_delta": delta_receipt(before, after),
        "triggered": fail_safe,
    }

    final = snapshot_quantities(psi, phi, mu)
    ledger_sums = {name: 0.0 for name in initial}
    for receipt in receipts.values():
        for observable, value in receipt["observable_delta"].items():
            ledger_sums[observable] += value
    actual_delta = {name: final[name] - initial[name] for name in initial}
    residual = {name: actual_delta[name] - ledger_sums[name] for name in initial}

    out = {"psi": psi, "phi": phi, "kappa": kappa, "mu": mu}
    diagnostics = {
        "initial": initial,
        "final": final,
        "actual_delta": actual_delta,
        "ledger_sums": ledger_sums,
        "ledger_residual": residual,
        "receipts": receipts,
        "guard_counts": {
            "psi_cap_after_drift": psi_cap_count,
            "phi_clip": phi_clip_count,
            "mu_clip": mu_clip_count,
            "psi_fail_safe_reset": fail_safe,
        },
    }
    return out, diagnostics


def run_actual(state: dict[str, np.ndarray], cfg: CoreConfig, *, seed: int) -> dict:
    np.random.seed(seed)
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        out = step_core({k: np.array(v, copy=True) for k, v in state.items()}, cfg)
    out["_captured_stdout"] = capture.getvalue()
    return out


def evaluate_branch(name: str, cfg: CoreConfig, *, seed: int = SEED) -> dict:
    source_state = make_state()
    actual = run_actual(source_state, cfg, seed=seed)
    mirror, diagnostics = isolated_step(source_state, cfg, seed=seed)

    parity = {
        key: max_abs_delta(actual[key], mirror[key])
        for key in ("psi", "phi", "kappa", "mu")
    }
    ledger_ok = all(abs(x) <= LEDGER_RESIDUAL_TOL for x in diagnostics["ledger_residual"].values())
    parity_ok = max(parity.values()) <= ABS_PARITY_TOL
    kappa_ok = max_abs_delta(actual["kappa"], source_state["kappa"]) <= UNCHANGED_TOL

    return {
        "name": name,
        "config": {
            "use_mode_coupling": cfg.use_mode_coupling,
            "disable_quantum_noise": cfg.disable_quantum_noise,
            "disable_pml": cfg.disable_pml,
            "psi_amp_cap": cfg.psi_amp_cap,
            "phi_cap": cfg.phi_cap,
            "mu_cap": cfg.mu_cap,
            "fold_mode": cfg.fold_mode,
            "fold_scope": cfg.fold_scope,
        },
        "seed": seed,
        "parity_max_abs": parity,
        "telemetry": actual.get("telemetry", {}),
        "captured_stdout": actual.get("_captured_stdout", ""),
        "diagnostics": diagnostics,
        "checks": {
            "mirror_matches_step_core": parity_ok,
            "componentwise_software_ledger_closes": ledger_ok,
            "kappa_returned_unchanged": kappa_ok,
        },
        "pass": bool(parity_ok and ledger_ok and kappa_ok),
    }


def compare_states(a: dict, b: dict) -> dict[str, float]:
    return {
        key: max_abs_delta(a[key], b[key])
        for key in ("psi", "phi", "kappa", "mu")
    }


def main() -> None:
    ExecutionPolicy.init_core_determinism(
        enforce_canonical=True,
        seed=SEED,
        device_mode="numpy",
    )

    if git_blob_sha("lineum_core/math.py") != EXPECTED_MATH_BLOB:
        raise RuntimeError("Current math.py blob differs from frozen FAC2-R1 source identity.")

    deterministic_paired_cfg = make_config(use_mode_coupling=True, noise=False, disable_pml=True)
    stochastic_paired_cfg = make_config(use_mode_coupling=True, noise=True, disable_pml=True)
    deterministic_fallback_cfg = make_config(use_mode_coupling=False, noise=False, disable_pml=True)
    pml_flag_cfg = replace(deterministic_paired_cfg, disable_pml=False)
    fold_null_cfg = replace(deterministic_paired_cfg, fold_mode="baseline", fold_scope="none")
    guard_cfg = make_config(
        use_mode_coupling=True,
        noise=False,
        disable_pml=True,
        psi_amp_cap=0.24,
        phi_cap=0.40,
        mu_cap=0.125,
        fold_mode="softabs",
        fold_scope="escape",
    )

    branches = {
        "deterministic_paired": evaluate_branch("deterministic_paired", deterministic_paired_cfg),
        "stochastic_paired": evaluate_branch("stochastic_paired", stochastic_paired_cfg),
        "deterministic_fallback": evaluate_branch("deterministic_fallback", deterministic_fallback_cfg),
        "pml_flag_false": evaluate_branch("pml_flag_false", pml_flag_cfg),
        "fold_flags_baseline": evaluate_branch("fold_flags_baseline", fold_null_cfg),
        "guard_stress": evaluate_branch("guard_stress", guard_cfg),
    }

    state = make_state()
    pml_true_actual = run_actual(state, deterministic_paired_cfg, seed=SEED)
    pml_false_actual = run_actual(state, pml_flag_cfg, seed=SEED)
    fold_soft_actual = run_actual(state, deterministic_paired_cfg, seed=SEED)
    fold_baseline_actual = run_actual(state, fold_null_cfg, seed=SEED)

    pml_effect = compare_states(pml_true_actual, pml_false_actual)
    fold_effect = compare_states(fold_soft_actual, fold_baseline_actual)

    stochastic_source = branches["stochastic_paired"]["diagnostics"]["receipts"]["psi_source_plus_interaction"]
    deterministic_source = branches["deterministic_paired"]["diagnostics"]["receipts"]["psi_source_plus_interaction"]
    guard = branches["guard_stress"]
    guard_counts = guard["diagnostics"]["guard_counts"]
    telemetry = guard["telemetry"]

    specific_checks = {
        "deterministic_source_increment_zero": deterministic_source["source_increment_l2"] <= UNCHANGED_TOL,
        "stochastic_source_increment_nonzero": stochastic_source["source_increment_l2"] >= MIN_SIGNAL,
        "stochastic_linon_events_nonzero": stochastic_source["linon_count"] > 0,
        "numpy_pml_flag_has_no_effect": max(pml_effect.values()) <= UNCHANGED_TOL,
        "numpy_fold_flags_have_no_effect": max(fold_effect.values()) <= UNCHANGED_TOL,
        "guard_psi_cap_activated": guard_counts["psi_cap_after_drift"] > 0,
        "guard_phi_clip_activated": guard_counts["phi_clip"] > 0,
        "guard_mu_clip_activated": guard_counts["mu_clip"] > 0,
        "guard_fail_safe_reset_activated": guard_counts["psi_fail_safe_reset"] is True,
        "numpy_guard_telemetry_cap_count_remains_zero": telemetry.get("cap_triggers") == 0,
        "numpy_guard_telemetry_fold_count_remains_zero": telemetry.get("fold_triggers") == 0,
    }

    all_branch_pass = all(branch["pass"] for branch in branches.values())
    overall_pass = bool(all_branch_pass and all(specific_checks.values()))

    output = {
        "schema": "lineum_fac2_numpy_componentwise_accounting_r1",
        "math_blob": EXPECTED_MATH_BLOB,
        "scope": "current_numpy_diffusion_step_only",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "platform": platform.platform(),
        "seed": SEED,
        "thresholds": {
            "absolute_parity_tolerance": ABS_PARITY_TOL,
            "ledger_residual_tolerance": LEDGER_RESIDUAL_TOL,
            "unchanged_tolerance": UNCHANGED_TOL,
            "minimum_signal": MIN_SIGNAL,
        },
        "branches": branches,
        "pml_flag_effect_max_abs": pml_effect,
        "fold_flag_effect_max_abs": fold_effect,
        "specific_checks": specific_checks,
        "overall_pass": overall_pass,
        "classifications_if_passed": {
            "componentwise_numpy_software_accounting": "closed_within_frozen_step_domain",
            "stochastic_source": "explicit_open_psi_state_increment_without_finite_stock",
            "pml_in_numpy_diffusion_path": "not_implemented_flag_has_no_state_effect",
            "fold_in_numpy_diffusion_path": "not_implemented_flags_have_no_state_effect",
            "numpy_cap_fold_telemetry": "does_not_report_guard_activity_even_when_direct_state_accounting_detects_it",
            "kappa": "supplied_non_evolving_modulator",
            "fac2_full_cross_backend_status": "not_complete_requires_separate_pytorch_wave_pml_fold_decision",
        },
        "physical_energy_claim": "not_established",
        "new_state_required": "not_established",
        "real_world_correspondence": "not_tested",
        "ancient_physics_correspondence": "not_established",
        "scalar_partition_warning": (
            "Qpsi is quadratic, so simultaneous source+interaction additions have cross terms; "
            "their counterfactual marginals are diagnostics, not unique additive scalar ledger shares."
        ),
    }

    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
