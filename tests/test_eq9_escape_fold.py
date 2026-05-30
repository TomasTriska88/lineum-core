import pytest
import os
import torch
import numpy as np
import lineum_core.math as lmath
from lineum_core.math import step_core, CoreConfig, ExecutionPolicy

@pytest.fixture(autouse=True)
def force_pytorch():
    old_use = lmath.USE_PYTORCH
    old_env = os.environ.get("LINEUM_USE_PYTORCH")
    
    lmath.USE_PYTORCH = True
    os.environ["LINEUM_USE_PYTORCH"] = "1"
    
    ExecutionPolicy.init_core_determinism(enforce_canonical=False, seed=42)
    
    yield
    
    lmath.USE_PYTORCH = old_use
    if old_env is not None:
        os.environ["LINEUM_USE_PYTORCH"] = old_env
    else:
        os.environ.pop("LINEUM_USE_PYTORCH", None)
    
    ExecutionPolicy.init_core_determinism(enforce_canonical=False, seed=42)

def generate_state(sizes=64, phi_magnitude=5.0):
    x, y = np.meshgrid(np.linspace(-1, 1, sizes), np.linspace(-1, 1, sizes))
    r1 = np.random.rand() * 0.4 - 0.2
    r2 = np.random.rand() * 0.4 - 0.2
    packet1 = np.exp(-15 * ((x-r1)**2 + (y-r2)**2)) * 40.0
    packet2 = np.exp(-15 * ((x+r1)**2 + (y+r2)**2)) * 40.0
    phi_base = (packet1 + packet2) * phi_magnitude

    state = {
        "psi": (packet1 + packet2).astype(np.complex128),
        "phi": phi_base.astype(np.float64),
        "kappa": np.ones((sizes, sizes), dtype=np.float64)
    }
    return state

def test_eq9_escape_no_stress_equivalence():
    """Test that SoftAbs and Baseline are identical when no overflow occurs"""
    cfg_base = CoreConfig(dt=0.2, phi_cap=1000.0, fold_mode="baseline", fold_scope="none", physics_mode_psi="wave_projected")
    cfg_soft = CoreConfig(dt=0.2, phi_cap=1000.0, fold_mode="softabs", fold_scope="escape", physics_mode_psi="wave_projected")
    
    np.random.seed(42)
    state_base = generate_state(phi_magnitude=0.1)  # small phi, no overflow
    np.random.seed(42)
    state_soft = generate_state(phi_magnitude=0.1)
    
    for _ in range(10):
        state_base = step_core(state_base, cfg_base)
        state_soft = step_core(state_soft, cfg_soft)
        
    max_diff = np.max(np.abs(state_base["phi"] - state_soft["phi"]))
    assert max_diff < 0.01, f"Values diverge float32: max diff {max_diff}"
    assert state_base["telemetry"].get("fold_triggers", 0) == 0
    assert state_soft["telemetry"].get("fold_triggers", 0) == 0

def test_eq9_escape_overflow_reduces_leakage():
    """Test that SoftAbs survives and has lower/equal leakage than baseline under stress"""
    cfg_base = CoreConfig(dt=0.2, phi_cap=1.0, fold_mode="baseline", fold_scope="none", physics_mode_psi="wave_projected")
    cfg_soft = CoreConfig(dt=0.2, phi_cap=1.0, fold_mode="softabs", fold_scope="escape", physics_mode_psi="wave_projected")
    
    np.random.seed(42)
    state_base = generate_state(phi_magnitude=5.0)
    np.random.seed(42)
    state_soft = generate_state(phi_magnitude=5.0)
    
    leakage_base = 0.0
    leakage_soft = 0.0
    
    for _ in range(50):
        state_base = step_core(state_base, cfg_base)
        state_soft = step_core(state_soft, cfg_soft)
        leakage_base = max(leakage_base, state_base["telemetry"].get("spectral_leakage", 0.0))
        leakage_soft = max(leakage_soft, state_soft["telemetry"].get("spectral_leakage", 0.0))
        
    assert state_soft["telemetry"].get("fold_triggers", 0) > 0
    assert not state_soft["telemetry"]["is_nan"]
    assert leakage_soft <= leakage_base + 0.05

@pytest.mark.parametrize("seed", [42, 1024, 777])
def test_eq9_escape_multi_seed_survival(seed):
    """Test that SoftAbs survives massive overflow across multiple chaotic seeds without NaN"""
    cfg = CoreConfig(dt=0.2, phi_cap=0.5, fold_mode="softabs", fold_scope="escape", physics_mode_psi="wave_projected")
    np.random.seed(seed)
    
    state = generate_state(phi_magnitude=10.0) # Massive overflow
    for _ in range(50):
        state = step_core(state, cfg)
        
    assert not state["telemetry"]["is_nan"]

def test_eq9_escape_negative_phi_required():
    """
    Explicit regression test protecting the SoftAbs mechanism against future 'cleanups'.
    If a lower-floor clamp (phi >= 0.0) is ever introduced to 'fix' negative phi,
    it must demonstrably worsen the target behavior (increase spectral leakage).
    """
    cfg_soft = CoreConfig(dt=0.2, phi_cap=1.0, fold_mode="softabs", fold_scope="escape", physics_mode_psi="wave_projected")
    
    ExecutionPolicy.init_core_determinism(enforce_canonical=False, seed=10)
    state_true = generate_state(phi_magnitude=5.0)
    ExecutionPolicy.init_core_determinism(enforce_canonical=False, seed=10)
    state_floored = generate_state(phi_magnitude=5.0)
    
    leakage_true = 0.0
    leakage_floored = 0.0
    
    for _ in range(50):
        # Intended behavior (allowing negative phi to form inverse gradient)
        state_true = step_core(state_true, cfg_soft)
        leakage_true = max(leakage_true, state_true["telemetry"].get("spectral_leakage", 0.0))
        
        # Simulated "bug" where someone incorrectly clamps phi to >= 0
        state_floored = step_core(state_floored, cfg_soft)
        state_floored["phi"] = np.clip(state_floored["phi"], a_min=0.0, a_max=None)
        leakage_floored = max(leakage_floored, state_floored["telemetry"].get("spectral_leakage", 0.0))

    # The floored version must show degraded behavior (higher leakage)
    assert leakage_floored > leakage_true

