import numpy as np
import scipy.ndimage
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core
from forensic_evidence_exporter import get_waypoint_path, run_global_astar

def generate_urban_ring(size=64):
    kappa = np.ones((size, size))
    # Outer block wall
    kappa[5:size-5, 5:10] = 0.05
    kappa[5:size-5, size-10:size-5] = 0.05
    kappa[5:10, 5:size-5] = 0.05
    kappa[size-10:size-5, 5:size-5] = 0.05
    # Central block (Courtyard open)
    kappa[20:size-20, 20:size-20] = 0.05
    kappa[25:size-25, 25:size-25] = 1.0 # The courtyard inside
    # Gates to access Ring Road & Courtyard
    kappa[5:10, size//2-2:size//2+2] = 1.0 # Top Outer Gate
    kappa[size-10:size-5, size//2-2:size//2+2] = 1.0 # Bottom Outer Gate
    kappa[size//2-2:size//2+2, 20:25] = 1.0 # Left Inner Gate
    kappa[size//2-2:size//2+2, size-25:size-20] = 1.0 # Right Inner Gate
    
    # Asphalt layer (perfect > 1.0 multipliers)
    kappa[12:18, 12:size-12] = 1.2
    kappa[size-18:size-12, 12:size-12] = 1.2
    kappa[12:size-12, 12:18] = 1.2
    kappa[12:size-12, size-18:size-12] = 1.2
    
    return kappa, (2, size//2), (size//2, size//2) # Top outside to Center courtyard

def generate_canyon(size=64):
    kappa = np.full((size, size), 0.05)
    # A sine wave canyon
    for y in range(size):
        x_center = int(size//2 + np.sin(y / 10.0) * (size//4))
        for x in range(max(0, x_center-8), min(size, x_center+8)):
            # Continuous gradient to walls
            dist = abs(x - x_center)
            kappa[y, x] = max(0.05, 1.0 - (dist / 8.0))
    return kappa, (5, int(size//2+np.sin(0.5)*size//4)), (size-5, int(size//2+np.sin((size-5)/10.0)*size//4))

def multi_corridor_bottleneck(size=64):
    # Tests Diffusion Rank Ordering
    kappa = np.full((size, size), 0.05)
    # Open Start and End areas
    kappa[0:15, :] = 1.0
    kappa[size-15:size, :] = 1.0
    
    # Corridor 1: Width 2 (Narrowest, Highest Pressure)
    kappa[15:size-15, 10:12] = 1.0
    # Corridor 2: Width 4 (Medium)
    kappa[15:size-15, 30:34] = 1.0
    # Corridor 3: Width 8 (Widest, Lowest Pressure)
    kappa[15:size-15, 50:58] = 1.0
    
    return kappa, (5, size//2), (size-5, size//2)

def run_wave_topology(kappa, start, goal, threshold_ratio=0.3):
    s = kappa.shape[0]
    psi = np.zeros((s, s), dtype=np.complex128)
    phi = np.zeros((s, s), dtype=np.float64)
    delta = np.zeros((s, s), dtype=np.float64)
    cfg = CoreConfig(physics_mode_psi="wave_projected_soft", dissipation_rate=0.01)
    
    for _ in range(800):
        psi[start[0], start[1]] += 1.0 
        psi[max(0, goal[0]-2):min(s, goal[0]+3), max(0, goal[1]-2):min(s, goal[1]+3)] *= 0.1
        state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
        psi = state['psi']
        
    intensity = np.abs(psi)
    mean_int = np.mean(intensity)
    lineum_mask = (intensity < (mean_int * threshold_ratio)) & (kappa > 0.05)
    
    L_len = get_waypoint_path(lineum_mask, start, goal, max_search=20)
    feasible = L_len < float('inf')
    return feasible, np.sum(lineum_mask), lineum_mask
def compute_diffusion_rank_ordering(size=64):
    kappa, start, goal = multi_corridor_bottleneck(size)
    psi = np.zeros((size, size), dtype=np.complex128)
    phi = np.zeros((size, size), dtype=np.float64)
    delta = np.zeros((size, size), dtype=np.float64)
    cfg = CoreConfig(physics_mode_psi="diffusion", dissipation_rate=0.01)
    
    # Run long diffusion to settle pressure
    for _ in range(1500):
        psi[start[0], start[1]] += 1.0 
        psi[max(0, goal[0]-2):min(size, goal[0]+3), max(0, goal[1]-2):min(size, goal[1]+3)] *= 0.1
        state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
        psi = state['psi']
        phi = state['phi']
        
    lap = scipy.ndimage.laplace(phi)
    
    # Measure pressure in the middle of each corridor
    y_mid = size // 2
    x_c1 = 11 # Center of 10:12
    x_c2 = 32 # Center of 30:34
    x_c3 = 54 # Center of 50:58
    
    p1 = lap[y_mid, x_c1]
    p2 = lap[y_mid, x_c2]
    p3 = lap[y_mid, x_c3]
    return p1, p2, p3

def measure_map_diversity():
    results = {}
    for map_name, gen_func in [("Canyon Pass", generate_canyon), ("Urban Ring", generate_urban_ring)]:
        kappa, start, goal = gen_func(64)
        bin_space = (kappa > 0.2).astype(int)
        dist = scipy.ndimage.distance_transform_edt(bin_space)
        lap_dist = scipy.ndimage.laplace(dist)
        edt_mask = (lap_dist < -0.5)
        
        feasible, l_nodes, l_mask = run_wave_topology(kappa, start, goal)
        e_nodes = np.sum(edt_mask)
        global_len = run_global_astar(kappa, start, goal)
        l_len = get_waypoint_path(l_mask, start, goal)
        e_len = get_waypoint_path(edt_mask, start, goal)
        
        l_detour = l_len / global_len if global_len > 0 and l_len < float('inf') else float('inf')
        e_detour = e_len / global_len if global_len > 0 and e_len < float('inf') else float('inf')
        results[map_name] = {"feasible": feasible, "l_nodes": l_nodes, "e_nodes": e_nodes, "l_detour": l_detour, "e_detour": e_detour}
    return results

def run_fragility_test():
    kappa_base, start, goal = generate_urban_ring(64)
    thresholds = [0.2, 0.25, 0.3, 0.35, 0.4]
    results_thresh = {}
    for t in thresholds:
        feasible, nodes, _ = run_wave_topology(kappa_base, start, goal, threshold_ratio=t)
        results_thresh[t] = feasible
        
    # Noise test (Uniform +/- 5%)
    noise = np.random.uniform(-0.05, 0.05, (64, 64))
    kappa_noisy = np.clip(kappa_base + noise, 0.05, 2.0)
    feasible_noisy, nodes_noisy, _ = run_wave_topology(kappa_noisy, start, goal, threshold_ratio=0.3)
    
    return results_thresh, feasible_noisy

def export_phase10():
    print("=== PHASE 10: ROBUSTNESS & GENERALIZATION ===")
    
    # 1. Map Diversity
    div = measure_map_diversity()
    for m, d in div.items():
        print(f"\\n--- {m} ---")
        print(f" Nodes -> Lineum: {d['l_nodes']:4d} | EDT: {d['e_nodes']:4d}")
        print(f" Detour -> Lineum {d['l_detour']:.2f}x | EDT {d['e_detour']:.2f}x")
        
    # 2. Diffusion Downstream Hardening
    p1, p2, p3 = compute_diffusion_rank_ordering(64)
    print("\\n--- DIFFUSION BOTTLENECK RANK ORDERING ---")
    print(f" Corridor 1 (Width 2): {p1:.5f} (Pressure Laplacian)")
    print(f" Corridor 2 (Width 4): {p2:.5f} (Pressure Laplacian)")
    print(f" Corridor 3 (Width 8): {p3:.5f} (Pressure Laplacian)")
    correct_rank = (p1 < p2) and (p2 < p3) # more negative = higher pressure
    print(f" Correct Mathematical Rank Order: {correct_rank}")
    
    # 3. Fragility
    t_res, noisy_res = run_fragility_test()
    print("\\n--- FRAGILITY & SENSITIVITY ---")
    print(f" Threshold Feasibility [0.2 to 0.4]: {t_res}")
    print(f" Uniform +/- 5% Noise Feasibility: {noisy_res}")

if __name__ == '__main__':
    export_phase10()
