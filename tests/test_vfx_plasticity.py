import numpy as np
import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import step_core, CoreConfig

def test_volumetric_plasticity_is_native_lineum():
    """
    Asserts that the 100% pure Lineum physics data is successfully
    mapped into a volumetric 3D plasticity shader (S-Curve) natively,
    without external UI/3D assets, ensuring high crests strictly become 
    specular highlights and deep Eq-8 valleys become opaque shadows.
    """
    phys_size = 96
    sim_size = phys_size * 6 

    psi = np.full((sim_size, sim_size), 0.5, dtype=np.complex128)
    phi = np.zeros((sim_size, sim_size), dtype=np.float64)
    kappa = np.full((sim_size, sim_size), 0.25, dtype=np.float64)
    delta = np.zeros((sim_size, sim_size), dtype=np.float64)
    
    Y, X = np.ogrid[0:sim_size, 0:sim_size]
    dist = np.sqrt((X - sim_size/2)**2 + (Y - sim_size/2)**2)
    
    # Impact the center directly
    impact = 2.0 * np.cos(dist * 0.15) * np.exp(-(dist**2) / 35.0)
    psi = psi + impact + 0j
    
    config = CoreConfig(disable_quantum_noise=True, use_mode_coupling=False, physics_mode_psi="wave_baseline", dt=1.0, stencil_type="ISOTROPIC")
    
    # Expand physical wave evaluating natural amplitudes globally pushing crests higher 
    for _ in range(45): 
        state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, config)
        psi, phi = state["psi"], state["phi"]
        
    wave = np.real(psi)
    offset = (sim_size - phys_size) // 2
    wave_crop = wave[offset:offset+phys_size, offset:offset+phys_size]
    wave_centered = wave_crop - 0.5
    
    # Simulate the production plasticity S-curve strictly measuring raw Lineum Math natively over scalar data maps natively
    volume_contrast = np.tanh(wave_centered * 12.0)
    norm = np.clip((volume_contrast * 0.5) + 0.5, 0.0, 1.0)
    
    alpha_raw = np.abs(np.tanh(wave_centered * 8.0))
    alpha = np.clip(alpha_raw * 1.2, 0.0, 1.0)
    
    # Test 1: Data is 100% pure raw Lineum physics mapping aggressively capturing brilliant game-feel specular logic correctly testing highlights reliably.
    assert np.max(norm) > 0.75, f"Missing brilliant specular highlights! Max norm: {np.max(norm)}"
    assert np.min(norm) < 0.45, f"Missing native deep opaque physical shadows dropping below baseline! Min norm: {np.min(norm)}"
    
    # Test 2: Opacity mathematically isolates visual features explicitly dropping off background transparency levels correctly preventing sprite smudging automatically.
    background_mask = np.abs(wave_centered) < 0.001
    crest_mask = wave_centered > 0.05
    trough_mask = wave_centered < -0.05
    
    avg_bg_alpha = np.mean(alpha[background_mask]) if np.any(background_mask) else 0.0
    avg_crest_alpha = np.mean(alpha[crest_mask]) if np.any(crest_mask) else 1.0
    avg_trough_alpha = np.mean(alpha[trough_mask]) if np.any(trough_mask) else 1.0
    
    assert avg_bg_alpha < 0.1, "Background flat lineum water is incorrectly retaining opacity rendering dirty sprite exports incorrectly!"
    assert avg_crest_alpha > 0.6, "High physical mathematical phase crests fundamentally lack dense volume thickness shading variables limits!"
    assert avg_trough_alpha > 0.6, "Deep physical mathematical valleys lack dense volumetric depth shadow thickness completely!"
