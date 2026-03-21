import numpy as np
import scipy.ndimage
import heapq
import time
import os
import sys
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core
from infrastructure_phase_a import SyntheticInferenceMaps

def astar_grid(mask, start, goal):
    def heur(a, b): return np.hypot(a[0]-b[0], a[1]-b[1])
    frontier = []
    heapq.heappush(frontier, (0, start))
    cost_so_far = {start: 0}
    
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal: break
        
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nyt, nxt = current[0] + dy, current[1] + dx
            if 0 <= nyt < mask.shape[0] and 0 <= nxt < mask.shape[1] and mask[nyt, nxt]:
                new_cost = cost_so_far[current] + (1.0 if dy == 0 or dx == 0 else 1.414)
                if (nyt, nxt) not in cost_so_far or new_cost < cost_so_far[(nyt, nxt)]:
                    cost_so_far[(nyt, nxt)] = new_cost
                    priority = new_cost + heur(goal, (nyt, nxt))
                    heapq.heappush(frontier, (priority, (nyt, nxt)))
                    
    return cost_so_far.get(goal, float('inf'))

def get_waypoint_path(mask, start, goal, max_search=8):
    nodes = np.argwhere(mask)
    if len(nodes) == 0: return float('inf')
    
    def find_nearest(target):
        dists = np.hypot(nodes[:, 0] - target[0], nodes[:, 1] - target[1])
        min_idx = np.argmin(dists)
        if dists[min_idx] > max_search: return None
        return tuple(nodes[min_idx])
        
    s_node = find_nearest(start)
    g_node = find_nearest(goal)
    if not s_node or not g_node: return float('inf')
    
    length = astar_grid(mask, s_node, g_node)
    if length < float('inf'):
        length += np.hypot(start[0]-s_node[0], start[1]-s_node[1])
        length += np.hypot(goal[0]-g_node[0], goal[1]-g_node[1])
    return length

def run_global_astar(kappa, start, goal):
    mask = kappa > 0.05
    return get_waypoint_path(mask, start, goal, max_search=1)

def compute_evidence(scenario="bottleneck"):
    kappa, start, goal = SyntheticInferenceMaps.construct_map(scenario, 64)
    s = kappa.shape[0]
    
    # Run Lineum Engine
    psi = np.zeros((s, s), dtype=np.complex128)
    phi = np.zeros((s, s), dtype=np.float64)
    delta = np.zeros((s, s), dtype=np.float64)
    cfg = CoreConfig(physics_mode_psi="wave_projected_soft", dissipation_rate=0.01)
    
    for _ in range(800):
        psi[start[0], start[1]] += 1.0 
        ty_s, ty_e = max(0, goal[0]-2), min(s, goal[0]+3)
        tx_s, tx_e = max(0, goal[1]-2), min(s, goal[1]+3)
        psi[ty_s:ty_e, tx_s:tx_e] *= 0.1
        state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
        psi = state['psi']
        
    # Extrakce Lineum (Wave Chladni)
    intensity = np.abs(psi)
    mean_int = np.mean(intensity)
    lineum_mask = (intensity < (mean_int * 0.3)) & (kappa > 0.05)
    
    # Extrakce EDT Baseline
    bin_space = (kappa > 0.2).astype(int)
    dist = scipy.ndimage.distance_transform_edt(bin_space)
    lap_dist = scipy.ndimage.laplace(dist)
    edt_mask = (lap_dist < -0.5)
    
    # Downstream Navigation Usability (Detour Ratio)
    global_len = run_global_astar(kappa, start, goal)
    L_len = get_waypoint_path(lineum_mask, start, goal)
    E_len = get_waypoint_path(edt_mask, start, goal)
    
    L_detour = L_len / global_len if (global_len > 0 and L_len < float('inf')) else float('inf')
    E_detour = E_len / global_len if (global_len > 0 and E_len < float('inf')) else float('inf')
    
    # Graph Economy (Compactness)
    open_area = np.sum(kappa > 0.05)
    L_nodes = np.sum(lineum_mask)
    E_nodes = np.sum(edt_mask)
    L_compact = L_nodes / open_area
    E_compact = E_nodes / open_area
    
    # Render Overlays
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.title("Kappa Matrix")
    plt.imshow(kappa, cmap='gray')
    
    plt.subplot(1, 3, 2)
    plt.title(f"Classical EDT\\nNodes: {E_nodes} | Detour: {E_detour:.2f}")
    plt.imshow(edt_mask, cmap='hot')
    
    plt.subplot(1, 3, 3)
    plt.title(f"Lineum Wave\\nNodes: {L_nodes} | Detour: {L_detour:.2f}")
    plt.imshow(lineum_mask, cmap='plasma')
    plt.savefig(f"scripts/output/evidence/overlay_{scenario}.png")
    plt.close()
    
    return {
        "scenario": scenario,
        "L_nodes": L_nodes, "E_nodes": E_nodes,
        "L_compact": L_compact, "E_compact": E_compact,
        "L_detour": L_detour, "E_detour": E_detour,
        "L_feasible": L_len < float('inf')
    }

def build_evidence_pack():
    print("=== PHASE 9: DOWNSTREAM WAYPOINT VALIDATION ===")
    scenarios = ["bottleneck", "swamp_bypass", "gates", "valleys", "roundabout", "dead_zone"]
    results = []
    
    for sc in scenarios:
        res = compute_evidence(sc)
        results.append(res)
        print(f"\\n--- {sc.upper()} ---")
        print(f" Graph Economy (Nodes)  -> Lineum: {res['L_nodes']:4d} | EDT: {res['E_nodes']:4d}")
        print(f" Navigation Usability   -> Feasible: {res['L_feasible']} | Detour Ratio: {res['L_detour']:4.2f}x (EDT {res['E_detour']:4.2f}x)")
        
    # Write CSV Evidence
    csv_header = "Scenario,Lineum_Nodes,EDT_Nodes,Lineum_Compactness,EDT_Compactness,Lineum_Detour,EDT_Detour,Lineum_Feasible\\n"
    csv_rows = [csv_header]
    for r in results:
        csv_rows.append(f"{r['scenario']},{r['L_nodes']},{r['E_nodes']},{r['L_compact']:.3f},{r['E_compact']:.3f},{r['L_detour']:.3f},{r['E_detour']:.3f},{r['L_feasible']}\\n")
        
    with open('scripts/output/evidence/graph_metrics.csv', 'w') as f:
        f.writelines(csv_rows)

if __name__ == '__main__':
    build_evidence_pack()
