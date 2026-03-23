import numpy as np
import pytest
import os
import sys
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import step_core, CoreConfig

def test_wave_boundary_expansion():
    frames = 30
    phys_size = 96
    sim_size = phys_size * 6 

    psi = np.full((sim_size, sim_size), 0.5, dtype=np.complex128)
    phi = np.zeros((sim_size, sim_size), dtype=np.float64)
    kappa = np.full((sim_size, sim_size), 0.25, dtype=np.float64)
    delta = np.zeros((sim_size, sim_size), dtype=np.float64)
    
    Y, X = np.ogrid[0:sim_size, 0:sim_size]
    dist = np.sqrt((X - sim_size/2)**2 + (Y - sim_size/2)**2)
    view_radius = phys_size / 2.0
    safe_zone = view_radius * 0.85  
    vignette = 1.0 - np.clip((dist - safe_zone) / (view_radius - safe_zone), 0.0, 1.0)
    
    impact = 2.0 * np.cos(dist * 0.15) * np.exp(-(dist**2) / 35.0)
    psi = psi + impact + 0j
    
    config = CoreConfig(disable_quantum_noise=True, use_mode_coupling=False, physics_mode_psi="wave_baseline", dt=1.0, stencil_type="LAP8")
    
    max_radius_reached = 0.0
    
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
        vignette_crop = vignette[offset:offset+phys_size, offset:offset+phys_size]
        
        alpha_raw = np.abs(wave_centered)
        alpha = np.clip((alpha_raw - 0.005) * 8.0, 0.0, 1.0) * vignette_crop
        
        Yc, Xc = np.nonzero(alpha > 0.1)
        if len(Xc) > 0:
            r_max = np.max(np.sqrt((Xc - phys_size/2)**2 + (Yc - phys_size/2)**2))
            if r_max > max_radius_reached:
                max_radius_reached = r_max
                
    assert max_radius_reached > (view_radius * 0.90), f"Wave faded too early: Max radius reached {max_radius_reached:.2f} out of {view_radius:.2f}"
    assert max_radius_reached <= view_radius, "Wave exceeded mathematical crop boundaries."
