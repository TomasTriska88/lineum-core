import numpy as np
import time
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core

def generate_mock_layers(s=64):
    # Base height map (hill on the left, flat on right)
    dem = np.zeros((s, s))
    for y in range(s):
        for x in range(s):
            dem[y, x] = 100.0 * np.exp(-((x - 10)**2 + (y - s//2)**2) / 400.0)
            
    # Derive Slope factor (0.0 to 1.0, where high slope is low kappa)
    gy, gx = np.gradient(dem)
    slope_mag = np.sqrt(gy**2 + gx**2)
    f_slope = np.clip(1.0 - (slope_mag / 5.0), 0.05, 1.0)
    
    # Wetlands: A lake in the center right
    f_wet = np.ones((s, s))
    for y in range(s):
        for x in range(s):
            if np.hypot(x - 45, y - s//2) < 12:
                f_wet[y, x] = 0.1 # Deep mud
                
    # Roads: A diagonal highway from (0,0) to (s,s)
    f_road = np.ones((s, s))
    for i in range(s):
        for w in range(-2, 3):
            if 0 <= i+w < s:
                # Road gives a strict bonus (makes it highly permeable)
                f_road[i, i+w] = 1.0
                # Reduce friction of surrounding dirt
                if f_wet[i, i+w] == 0.1: f_wet[i, i+w] = 0.8
                
    return f_slope, f_wet, f_road

def compute_topology(kappa, mode="wave_projected_soft"):
    s = kappa.shape[0]
    psi = np.zeros((s, s), dtype=np.complex128)
    phi = np.zeros((s, s), dtype=np.float64)
    delta = np.zeros((s, s), dtype=np.float64)
    cfg = CoreConfig(physics_mode_psi=mode, dissipation_rate=0.01)
    
    t0 = time.time()
    for _ in range(800):
        # Flood the entire left edge as source, right edge as sink
        psi[5:s-5, 2:5] += 1.0 
        psi[5:s-5, s-5:s-2] *= 0.1
        state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
        psi, phi = state['psi'], state['phi']
    t_solve = time.time() - t0
    
    intensity = np.abs(psi)
    mean_int = np.mean(intensity)
    nodes = np.sum((intensity < (mean_int * 0.4)) & (kappa > 0.05))
    
    return nodes, t_solve

def evaluate_phase_b():
    print("=== PHASE B: SEMI-SYNTHETIC KAPPA COMPOSITIONS ===")
    f_slope, f_wet, f_road = generate_mock_layers(64)
    
    # Variant 1: Pure Multiplicative
    k_mult = np.clip(f_slope * f_wet * f_road, 0.05, 1.0)
    
    # Variant 2: Additive Weighted
    k_add = np.clip(0.5 * f_slope + 0.3 * f_wet + 0.2 * f_road, 0.05, 1.0)
    
    # Variant 3: Capped Hybrid (Slope strictly gates capability, roads and wetlands modify it)
    k_hyb = np.clip(f_slope * np.clip((f_wet + (f_road - 1.0)), 0.05, 1.2), 0.05, 1.0)

    variants = [
        ("Multiplicative", k_mult),
        ("Additive Sum  ", k_add),
        ("Capped Hybrid ", k_hyb)
    ]
    
    for name, kappa in variants:
        nodes, t_solve = compute_topology(kappa)
        avg_k = np.mean(kappa)
        # We measure how the topological skeleton "shifts" based on the composition formula
        print(f"\\n--- {name} ---")
        print(f"  Mean Permeability: {avg_k:.3f}")
        print(f"  Detected Skeleton Ribs (px): {nodes:4d} | Extraction Time: {t_solve:.3f}s")
        if avg_k < 0.4:
            print("  -> Inference: Severe global dampening. Topology collapses into a single thin survival thread.")
        elif nodes > 800:
            print("  -> Inference: Topology overly dense. Additive layer diluted absolute physical barriers.")
        else:
            print("  -> Inference: Balanced topological skeleton mapping roads avoiding deep mud.")

if __name__ == '__main__':
    evaluate_phase_b()
