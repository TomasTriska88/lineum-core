import numpy as np
import time
import heapq
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core
from routing_backend.main import extract_path

class HeteroMaps:
    @staticmethod
    def generate_swamp(size=64):
        # Base field starts completely permeable (kappa=1.0)
        kappa = np.ones((size, size), dtype=np.float64)
        
        # Center swamp: 30x30 region where kappa drops to 0.05
        # The center is deepest (0.05), edges of swamp are 0.5
        cy, cx = size // 2, size // 2
        radius = 15
        for y in range(cy - radius, cy + radius):
            for x in range(cx - radius, cx + radius):
                dist = np.hypot(y - cy, x - cx)
                if dist < radius:
                    # Permeability scales from 0.05 at center to 0.9 at edge
                    severity = dist / radius
                    # Non-linear mud depth
                    k = 0.05 + 0.85 * (severity ** 2)
                    kappa[y, x] = min(1.0, k)
                    
        # Force a thin hard wall (kappa=0.0) blocking the top easy bypass, forcing agents 
        # to either brave the mud or take the long bottom bypass.
        for x in range(0, size // 2 + 10):
            kappa[10, x] = 0.0
            
        start = (5, 5)
        goal = (size - 10, size - 10)
        return kappa, start, goal

def run_weighted_dijkstra(kappa, start, target):
    s = kappa.shape[0]
    g_score = { (start[0], start[1]): 0.0 }
    came_from = {}
    pq = [(0.0, start[0], start[1])]
    
    while pq:
        current_cost, y, x = heapq.heappop(pq)
        
        if (y, x) == target:
            break
            
        if current_cost > g_score.get((y, x), float('inf')):
            continue
            
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < s and 0 <= nx < s:
                k_val = kappa[ny, nx]
                if k_val <= 0.05: continue # Absolute wall
                
                # Base distance: 1.0 for straight, 1.414 for diagonal
                dist = 1.0 if (dy == 0 or dx == 0) else 1.414
                
                # Traversing through low kappa costs massively more!
                # If kappa = 0.1, travel time is 10x slower.
                transition_cost = dist * (1.0 / k_val)
                tentative_g = current_cost + transition_cost
                
                if tentative_g < g_score.get((ny, nx), float('inf')):
                    came_from[(ny, nx)] = (y, x)
                    g_score[(ny, nx)] = tentative_g
                    heapq.heappush(pq, (tentative_g, ny, nx))
                    
    # Reconstruct path
    path = []
    curr = target
    while curr in came_from:
        path.append(curr)
        curr = came_from[curr]
    path.append(start)
    path.reverse()
    
    # Calculate accumulated traversal cost (travel time)
    acc_cost = 0.0
    for p in path:
        acc_cost += 1.0 / max(0.01, kappa[p[0], p[1]])
        
    return path, acc_cost

def compute_lineum_path(kappa, start, goal, mode, steps=2000):
    s = kappa.shape[0]
    psi = np.zeros((s, s), dtype=np.complex128)
    phi = np.zeros((s, s), dtype=np.float64)
    delta = np.zeros((s, s), dtype=np.float64)
    cfg = CoreConfig(physics_mode_psi=mode, dissipation_rate=0.01)
    
    ty, tx = goal
    sy, sx = start
    
    t0 = time.time()
    for _ in range(steps):
        psi[sy, sx] += 1.0 
        ty_s, ty_e = max(0, ty-2), min(s, ty+3)
        tx_s, tx_e = max(0, tx-2), min(s, tx+3)
        psi[ty_s:ty_e, tx_s:tx_e] *= 0.1
        state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
        psi, phi = state['psi'], state['phi']
    t_solve = time.time() - t0
    
    # Use A* purely to extract the route from the global phi scalar field
    px, py = extract_path(phi, kappa, sx, sy, tx, ty, s)
    
    path = list(zip(py, px))
    acc_cost = 0.0
    for p in path:
        acc_cost += 1.0 / max(0.01, kappa[p[0], p[1]])
        
    return path, acc_cost, t_solve

def evaluate_heterogeneous():
    print("=== PHASE 7: HETEROGENEOUS PERMEABILITY (SWAMP) ===")
    
    kappa, start, goal = HeteroMaps.generate_swamp(64)
    csv_rows = ["Method,PathLength,TraversalCost,SolveTime"]
    
    # 1. Weighted Dijkstra Baseline
    t0 = time.time()
    d_path, d_cost = run_weighted_dijkstra(kappa, start, goal)
    t_dijk = time.time() - t0
    print(f"[Weighted Dijkstra] Path Len: {len(d_path):4d} | Traversal Resistance Cost: {d_cost:6.1f} | Solve: {t_dijk:.3f}s")
    csv_rows.append(f"WeightedDijkstra,{len(d_path)},{d_cost:.1f},{t_dijk:.4f}")
    
    # 2. Lineum Diffusion
    diff_path, diff_cost, t_diff = compute_lineum_path(kappa, start, goal, "diffusion", steps=2000)
    print(f"[Lineum Diffusion]  Path Len: {len(diff_path):4d} | Traversal Resistance Cost: {diff_cost:6.1f} | Solve: {t_diff:.3f}s")
    csv_rows.append(f"Diffusion,{len(diff_path)},{diff_cost:.1f},{t_diff:.4f}")
    
    # 3. Lineum Wave (For control comparison)
    wave_path, wave_cost, t_wave = compute_lineum_path(kappa, start, goal, "wave_projected_soft", steps=800)
    print(f"[Lineum Wave]       Path Len: {len(wave_path):4d} | Traversal Resistance Cost: {wave_cost:6.1f} | Solve: {t_wave:.3f}s")
    csv_rows.append(f"Wave,{len(wave_path)},{wave_cost:.1f},{t_wave:.4f}")

    with open('scripts/output/forensic_hetero.csv', 'w') as f:
        f.write('\\n'.join(csv_rows))
        
if __name__ == '__main__':
    evaluate_heterogeneous()
