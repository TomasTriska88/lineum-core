import numpy as np
import scipy.ndimage
import time
import os
import sys
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from forensic_evidence_exporter import get_waypoint_path, run_global_astar
from infrastructure_phase_c import generate_fractal_dem
from lineum_core.math import CoreConfig, step_core

def compute_dem_evidence():
    print("=== MULTI-VARIANT DEM PILOT (EVIDENCE PACK) ===")
    kappa, field = generate_fractal_dem(100)
    s = kappa.shape[0]
    start = (5, 50)
    goal = (95, 50)
    
    # Run Lineum Wave
    psi = np.zeros((s, s), dtype=np.complex128)
    phi = np.zeros((s, s), dtype=np.float64)
    delta = np.zeros((s, s), dtype=np.float64)
    cfg = CoreConfig(physics_mode_psi="wave_projected_soft", dissipation_rate=0.01)
    for _ in range(800):
        psi[0:5, :] += 1.0  
        psi[s-5:s, :] *= 0.1
        state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
        psi = state['psi']
        
    intensity = np.abs(psi)
    mean_int = np.mean(intensity)
    lineum_mask = (intensity < (mean_int * 0.3)) & (kappa > 0.05)
    
    # Extrakce EDT Baseline
    bin_space = (kappa > 0.2).astype(int)
    dist = scipy.ndimage.distance_transform_edt(bin_space)
    lap_dist = scipy.ndimage.laplace(dist)
    edt_mask = (lap_dist < -0.5)
    
    # Downstream metrics
    global_len = run_global_astar(kappa, start, goal)
    L_len = get_waypoint_path(lineum_mask, start, goal, max_search=20)
    E_len = get_waypoint_path(edt_mask, start, goal, max_search=20)
    
    L_detour = L_len / global_len if (global_len > 0 and L_len < float('inf')) else float('inf')
    E_detour = E_len / global_len if (global_len > 0 and E_len < float('inf')) else float('inf')
    
    open_area = np.sum(kappa > 0.05)
    L_nodes = np.sum(lineum_mask)
    E_nodes = np.sum(edt_mask)
    L_compact = L_nodes / open_area
    E_compact = E_nodes / open_area
    
    print(f"\\n--- FRACTAL DEM (100x100) ---")
    print(f" Graph Economy (Nodes)  -> Lineum: {L_nodes:4d} | EDT: {E_nodes:4d}")
    print(f" Navigation Usability   -> Lineum Detour Ratio: {L_detour:4.2f}x (EDT {E_detour:4.2f}x)")
    
    # Render PNG
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.title("Kappa (Slope + Lakes)")
    plt.imshow(kappa, cmap='terrain')
    
    plt.subplot(1, 3, 2)
    plt.title(f"Classical EDT\\nNodes: {E_nodes} | Detour {E_detour:.2f}x")
    plt.imshow(edt_mask, cmap='hot')
    
    plt.subplot(1, 3, 3)
    plt.title(f"Lineum Wave\\nNodes: {L_nodes} | Detour {L_detour:.2f}x")
    plt.imshow(lineum_mask, cmap='plasma')
    plt.savefig("scripts/output/evidence/overlay_dem_fractal.png")
    
if __name__ == '__main__':
    compute_dem_evidence()
