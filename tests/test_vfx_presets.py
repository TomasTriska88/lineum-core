import pytest
import math
import numpy as np
from lineum_core.math import step_core, CoreConfig

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from tools.build_vfx_pack import preset_configs

# Fixtures for creating the base arrays
def get_base_state(sim_size=96):
    psi = np.full((sim_size, sim_size), 0.5, dtype=np.complex128)
    phi = np.zeros((sim_size, sim_size), dtype=np.float64)
    kappa = np.full((sim_size, sim_size), 0.25, dtype=np.float64)
    delta = np.zeros((sim_size, sim_size), dtype=np.float64)
    
    Y, X = np.ogrid[0:sim_size, 0:sim_size]
    cx, cy = sim_size/2, sim_size/2
    dist = np.sqrt((X - cx)**2 + (Y - cy)**2)
    return {"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, dist, X, Y, cx, cy

def test_preset_water_drop_stability():
    state, dist, _, _, _, _ = get_base_state()
    # Apply impact
    state["psi"] += 1.5 * np.cos(dist * 0.5) * np.exp(-(dist**2) / 8.0)
    
    config = CoreConfig(
        disable_quantum_noise=True, 
        use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", 
        dt=1.0, 
        dissipation_rate=0.015,
        stencil_type="ISOTROPIC"
    )
    
    # Run 10 steps to test immediate numeric limits
    for f in range(10):
        if f == 8:
            state["psi"] += 0.8 * np.exp(-(dist**2) / 3.0)
        state = step_core(state, config)
        
    assert not np.isnan(np.sum(state["psi"])), "Water Drop caused NaN in psi"
    assert not np.isnan(np.sum(state["phi"])), "Water Drop caused NaN in phi"
    assert np.max(np.abs(state["psi"])) < config.psi_amp_cap * 0.9, "Water Drop triggered divergence fail-safe"

def test_preset_water_ripple_idle_stability():
    state, dist, X, Y, cx, cy = get_base_state()
    state["psi"] += 0.5 * np.exp(-(dist**2) / 10.0)
    
    config = CoreConfig(
        disable_quantum_noise=True, 
        use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", 
        dt=0.8, 
        dissipation_rate=0.02,
        stencil_type="ISOTROPIC"
    )
    
    for f in range(10):
        shift = math.sin(f * 0.5) * 0.5
        shift_dist = np.sqrt((X - (cx + shift))**2 + (Y - cy)**2)
        state["phi"] += 0.05 * np.exp(-(shift_dist**2) / 6.0)
        state = step_core(state, config)
        
    assert not np.isnan(np.sum(state["psi"])), "Water Ripple Idle caused NaN"

def test_preset_water_splash_solid_stability():
    state, dist, X, Y, cx, cy = get_base_state()
    config = CoreConfig(
        disable_quantum_noise=True, use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", dt=1.4, dissipation_rate=0.08, stencil_type="ISOTROPIC"
    )
    impact = np.zeros_like(dist)
    np.random.seed(104)
    for _ in range(25):
        angle = np.random.rand() * np.pi * 2
        radius = (np.random.rand()**1.2) * 44.0
        dx = np.cos(angle) * radius
        dy = np.sin(angle) * radius
        drop_dist2 = (X - (cx + dx))**2 + (Y - (cy + dy))**2
        impact += np.exp(-drop_dist2 / 1.0) * 1.2
        
    state["phi"] += impact * 0.1
    for _ in range(5): state = step_core(state, config)
    assert not np.isnan(np.sum(state["psi"])), "Water Splash Solid caused NaN"

def test_preset_water_mud_stability():
    state, dist, X, Y, cx, cy = get_base_state()
    config = CoreConfig(
        disable_quantum_noise=True, use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", dt=0.6, dissipation_rate=0.04, stencil_type="ISOTROPIC"
    )
    impact = np.zeros_like(dist)
    np.random.seed(210)
    for _ in range(15):
        angle = np.random.rand() * np.pi * 2
        radius = (np.random.rand()**1.2) * 35.0
        dx = np.cos(angle) * radius
        dy = np.sin(angle) * radius
        drop_dist2 = (X - (cx + dx))**2 + (Y - (cy + dy))**2
        impact += np.exp(-drop_dist2 / 3.0) * 1.0
        
    state["phi"] += impact * 0.5
    for _ in range(5): state = step_core(state, config)
    assert not np.isnan(np.sum(state["psi"])), "Water Mud caused NaN"

def test_preset_explosion_stability():
    state, dist, _, _, _, _ = get_base_state()
    state["psi"] += 3.0 * np.exp(-(dist**2) / 16.0)
    state["phi"] += 20.0 * np.exp(-(dist**2) / 8.0)
    
    config = CoreConfig(
        disable_quantum_noise=True, 
        use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", 
        dt=1.8, # Aggressive temporal scaling
        dissipation_rate=0.005,
        stencil_type="ISOTROPIC"
    )
    
    for _ in range(10):
        state = step_core(state, config)
        
    assert not np.isnan(np.sum(state["psi"])), "Explosion caused NaN in psi"
    assert not np.isnan(np.sum(state["phi"])), "Explosion caused NaN in phi"

def test_preset_fire_burst_stability():
    state, dist, _, _, _, _ = get_base_state()
    
    config = CoreConfig(
        disable_quantum_noise=False, # Stochastic linons active
        use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", 
        dt=1.2, 
        dissipation_rate=0.03, # High burn-out rate
        stencil_type="ISOTROPIC"
    )
    
    # Continuous injection logic
    for f in range(5):
        burst = 5.0 * np.exp(-(dist**2) / 4.0) * (1.0 - (f/10.0))
        state["phi"] += burst
        for _ in range(3): # 3 sub-steps per frame
            state = step_core(state, config)
            
    assert not np.isnan(np.sum(state["psi"])), "Fire Burst caused NaN"
    
def test_preset_magic_shield_stability():
    state, dist, _, _, _, _ = get_base_state()
    # Ring shaped barrier (kappa = 0)
    ring_mask = np.abs(dist - 15.0) < 2.0
    state["kappa"][ring_mask] = 0.0 
    # Blast inside the shield
    state["psi"] += 2.0 * np.exp(-(dist**2) / 4.0)
    
    config = CoreConfig(
        disable_quantum_noise=True, 
        use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", 
        dt=1.0, 
        dissipation_rate=0.005,
        stencil_type="ISOTROPIC"
    )
    
    for _ in range(10):
        state = step_core(state, config)
        
    assert not np.isnan(np.sum(state["psi"])), "Magic Shield caused NaN"

def test_preset_water_wake_trajectory():
    state, dist, X, Y, cx, cy = get_base_state()
    
    config = CoreConfig(
        disable_quantum_noise=True, 
        use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", 
        dt=1.0, 
        dissipation_rate=0.015, # Game-feel soft dissipation
        stencil_type="ISOTROPIC"
    )
    
    # Simulate a 90-degree wake (Moving Right: dir_x=1, dir_y=0)
    dir_x, dir_y = 1.0, 0.0
    
    for f in range(5):
        offset_x = (f / 15.0) * 15.0 * dir_x
        offset_y = (f / 15.0) * 15.0 * dir_y 
        wake_dist = np.sqrt((X - (cx + offset_x))**2 + (Y - (cy + offset_y))**2)
        wake_impact = 0.5 * np.exp(-(wake_dist**2) / 4.0)
        state["psi"] += wake_impact
        state["phi"] += wake_impact * 0.4
        
        for _ in range(3):
            state = step_core(state, config)
            
    assert not np.isnan(np.sum(state["psi"])), "Water Wake caused NaN"
    # Ensure energy is predominantly shifted right due to injection
    left_side = np.sum(np.abs(state["psi"][:, :int(cx)]))
    right_side = np.sum(np.abs(state["psi"][:, int(cx):]))
    assert right_side > left_side, "Directional wake energy did not logically propagate in target direction."

def test_preset_acid_pool_stability():
    state, dist, _, _, cx, cy = get_base_state()
    config = CoreConfig(
        disable_quantum_noise=False, 
        use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", 
        dt=0.8, 
        dissipation_rate=0.015,
        stencil_type="ISOTROPIC"
    )
    for f in range(5):
        bubble_x, bubble_y = cx + 5.0, cy + 5.0
        b_dist = np.sqrt((dist - bubble_x)**2 + (dist - bubble_y)**2)
        state["phi"] += 2.0 * np.exp(-(b_dist**2) / 2.0)
        state = step_core(state, config)
    assert not np.isnan(np.sum(state["psi"])), "Acid Pool caused NaN"

def test_preset_blood_splatter_stability():
    state, dist, _, _, _, _ = get_base_state()
    config = CoreConfig(
        disable_quantum_noise=True, use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", dt=1.4, dissipation_rate=0.02, stencil_type="ISOTROPIC"
    )
    impact = (1.5 + 0.5) * np.exp(-(dist**2) / 10.0)
    state["phi"] += impact * 2.0
    for _ in range(5): state = step_core(state, config)
    assert not np.isnan(np.sum(state["psi"])), "Blood Splatter caused NaN"

def test_preset_portal_vortex_stability():
    state, dist, _, _, cx, cy = get_base_state()
    config = CoreConfig(
        disable_quantum_noise=True, use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", dt=1.2, dissipation_rate=0.01, stencil_type="ISOTROPIC"
    )
    for _ in range(5): state = step_core(state, config)
    assert not np.isnan(np.sum(state["psi"])), "Portal Vortex caused NaN"

def test_preset_smoke_grenade_stability():
    state, dist, _, _, _, _ = get_base_state()
    config = CoreConfig(
        disable_quantum_noise=True, use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", dt=0.5, dissipation_rate=0.002, stencil_type="ISOTROPIC"
    )
    for _ in range(5): state = step_core(state, config)
    assert not np.isnan(np.sum(state["phi"])), "Smoke Grenade caused NaN"

def test_preset_lightning_strike_stability():
    state, dist, _, _, _, _ = get_base_state()
    config = CoreConfig(
        disable_quantum_noise=False, use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", dt=2.0, dissipation_rate=0.08, stencil_type="ISOTROPIC"
    )
    state["psi"] += 3.0 * np.exp(-(dist**2) / 25.0)
    for _ in range(5): state = step_core(state, config)
    assert not np.isnan(np.sum(state["psi"])), "Lightning Strike caused NaN"

def test_preset_linon_vortex_stability():
    state, dist, X, Y, cx, cy = get_base_state()
    config = CoreConfig(
        disable_quantum_noise=True, use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", dt=0.8, dissipation_rate=0.0, stencil_type="ISOTROPIC"
    )
    theta = np.arctan2(Y - cy, X - cx)
    amp = 1.0 - np.exp(-(dist**2) / 10.0)
    psi_defect = amp * np.exp(1j * theta * 3.0) 
    state["psi"] = 0.5 + psi_defect * 0.4 * np.exp(-(dist**2) / 150.0)
    for _ in range(20): state = step_core(state, config)
    assert not np.isnan(np.sum(state["psi"])), "Linon Vortex caused NaN"

def test_vfx_noise_boolean_invariants():
    """Ensure that standard elemental/physical simulations have noise disabled, while magical/chaotic ones have it enabled."""
    smooth_presets = ["water_drop", "water_splash_solid", "water_mud", "water_ripple_idle", "explosion", "blood_splatter", "linon_vortex", "water_wake"]
    chaotic_presets = ["fire_burst", "magic_shield", "acid_pool", "portal_vortex", "smoke_grenade", "lightning_strike", "gas_explosion", "campfire", "fireball"]
    
    for p in smooth_presets:
        assert preset_configs[p].get("disable_quantum_noise", False) is True, f"CRITICAL GEOMETRY BUG: Preset '{p}' MUST have quantum noise legally disabled (set to True) to avoid render static!"
        
    for p in chaotic_presets:
        assert preset_configs[p].get("disable_quantum_noise", False) is False, f"CRITICAL FX BUG: Preset '{p}' MUST have quantum noise enabled (set to False) to ensure turbulent phase generation!"
