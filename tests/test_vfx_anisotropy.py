import numpy as np
import pytest
import os
import sys
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, ExecutionPolicy, step_core

def test_wave_is_perfectly_isotropic():
    original_policy = {
        "device": ExecutionPolicy._device,
        "backend": ExecutionPolicy._backend,
        "requested_mode": ExecutionPolicy._requested_mode,
        "selection_reason": ExecutionPolicy._selection_reason,
        "deterministic_mode": ExecutionPolicy._deterministic_mode,
        "is_canonical_run": ExecutionPolicy._is_canonical_run,
    }
    try:
        ExecutionPolicy.init_core_determinism(
            enforce_canonical=False,
            seed=42,
            device_mode="torch-cpu",
        )
        
        frames = 15
        phys_size = 96
        sim_size = phys_size * 6 

        psi = np.full((sim_size, sim_size), 0.5, dtype=np.complex128)
        phi = np.zeros((sim_size, sim_size), dtype=np.float64)
        kappa = np.full((sim_size, sim_size), 0.25, dtype=np.float64)
        delta = np.zeros((sim_size, sim_size), dtype=np.float64)
        
        Y, X = np.ogrid[0:sim_size, 0:sim_size]
        dist = np.sqrt((X - sim_size/2)**2 + (Y - sim_size/2)**2)
        view_radius = phys_size / 2.0
        
        impact = 2.0 * np.cos(dist * 0.15) * np.exp(-(dist**2) / 35.0)
        psi = psi + impact + 0j
        
        # CRITICAL: Validate with ISOTROPIC solver (bypasses Cartesian pixel dragging forming artifacts)
        config = CoreConfig(disable_quantum_noise=True, use_mode_coupling=False, physics_mode_psi="wave_baseline", dt=1.0, stencil_type="ISOTROPIC")
        
        total_required_steps = view_radius / 0.10
        steps_per_frame = math.ceil(total_required_steps / frames)
        total_sim_steps = frames * steps_per_frame
        decay_per_step = math.pow(0.2, 1.0 / total_sim_steps)
        
        for f in range(frames):
            for _ in range(steps_per_frame):
                state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, config)
                psi, phi = state["psi"], state["phi"]
                phi = phi * decay_per_step
                
        wave = np.real(psi)
        offset = (sim_size - phys_size) // 2
        wave_crop = wave[offset:offset+phys_size, offset:offset+phys_size]
        wave_centered = wave_crop - 0.5
        alpha_raw = np.abs(wave_centered)
        
        Yc, Xc = np.nonzero(alpha_raw > 0.05)
        assert len(Xc) > 0, "Wave faded out entirely, missing baseline parameters."
        
        center = phys_size / 2.0
        angles = np.arctan2(Yc - center, Xc - center)
        radii = np.sqrt((Xc - center)**2 + (Yc - center)**2)
        
        # Calculate radius strictly across cardinal straight trajectories Vs extreme diagonal coordinates
        mask_straight = (np.abs(np.cos(angles)) > 0.92) | (np.abs(np.sin(angles)) > 0.92)
        mask_diag = (np.abs(np.cos(angles)) < 0.77) & (np.abs(np.sin(angles)) < 0.77)
        
        r_straight = np.percentile(radii[mask_straight], 95) if np.any(mask_straight) else 0.0
        r_diag = np.percentile(radii[mask_diag], 95) if np.any(mask_diag) else 0.0
        
        diff = abs(r_straight - r_diag)
        
        # LAP8 inherently fails with values nearing >2.0 divergence marking Cartesian bias natively.
        # ISOTROPIC Operator mathematically corrects limits yielding symmetrical results essentially indistinguishable (<1.0)
        assert diff < 1.0, f"Grid Anisotropy Failure Occurred! Straight Radius: {r_straight:.1f}, Diagonal Radius: {r_diag:.1f}, Difference: {diff:.3f}"
    finally:
        ExecutionPolicy._device = original_policy["device"]
        ExecutionPolicy._backend = original_policy["backend"]
        ExecutionPolicy._requested_mode = original_policy["requested_mode"]
        ExecutionPolicy._selection_reason = original_policy["selection_reason"]
        ExecutionPolicy._deterministic_mode = original_policy["deterministic_mode"]
        ExecutionPolicy._is_canonical_run = original_policy["is_canonical_run"]
