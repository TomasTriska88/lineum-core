import numpy as np
import sys
import os
import scipy.ndimage

from forensic_correctness import Maps
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core

def compute_lineum_state(kappa, start, goal, steps=800):
    s = kappa.shape[0]
    psi = np.zeros((s, s), dtype=np.complex128)
    phi = np.zeros((s, s), dtype=np.float64)
    delta = np.zeros((s, s), dtype=np.float64)
    cfg = CoreConfig(physics_mode_psi="wave_projected_soft")
    
    ty, tx = goal
    sy, sx = start
    for _ in range(steps):
        psi[sy, sx] += 1.0 
        ty_s, ty_e = max(0, ty-2), min(s, ty+3)
        tx_s, tx_e = max(0, tx-2), min(s, tx+3)
        psi[ty_s:ty_e, tx_s:tx_e] *= 0.1
        state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
        psi, phi = state['psi'], state['phi']
    return psi, phi

def extract_skeleton():
    print("=== PHASE 6: EMERGENT SKELETON EXTRACTION ===")
    maps = ['horizontal_wall_gap', 'labyrinth', 'diagonal']
    
    for m in maps:
        kappa, start, goal = Maps.generate(m, 64)
        psi, phi = compute_lineum_state(kappa, start, goal)
        
        # Method 1: Wave Intensity Nulls (Chladni Standing Waves)
        intensity = np.abs(psi)
        mean_int = np.mean(intensity)
        # Nodes are where intensity is significantly below average
        nodes = (intensity < (mean_int * 0.5)) & (kappa > 0.05)
        
        # Method 2: Laplacian of Phi (Curvature Ridges)
        lap = scipy.ndimage.laplace(phi)
        # Negative laplacian indicates ridges (local maxima in 1D cross-sections)
        ridges = (lap < -0.01) & (kappa > 0.05)
        
        # Topological metrics
        corridor_area = np.sum(kappa > 0.05)
        node_count = np.sum(nodes)
        ridge_count = np.sum(ridges)
        
        print(f"\\nMap: {m:>20}")
        print(f" - Corridor Floor Area: {corridor_area} pixels")
        print(f" - Standing Wave Nodes: {node_count} pixels ({(node_count/corridor_area*100):.1f}%)")
        print(f" - Phi Laplacian Ridges: {ridge_count} pixels ({(ridge_count/corridor_area*100):.1f}%)")
        
        # Heuristic check: Does it form a sparse graph? 
        # A good sparse graph should massively reduce area (e.g., 5-15% of total corridor area)
        if 0.02 < (ridge_count / corridor_area) < 0.20:
            print(" -> SKELETON DETECTED: Ridges form a highly sparse subset (Potential Medial Axis).")
        else:
            print(" -> NO SKELETON: Ridges are either washed out or too dense.")
            
if __name__ == '__main__':
    extract_skeleton()
