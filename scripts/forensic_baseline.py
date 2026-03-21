import numpy as np
import time
import psutil
import os
import heapq
import collections
from forensic_correctness import Maps, LineumRouter, AStarBaseline

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core

def run_bfs_flow_field(kappa, goal):
    s = kappa.shape[0]
    cost_map = np.full((s, s), float('inf'))
    q = collections.deque([(0.0, goal)])
    cost_map[goal[0], goal[1]] = 0.0
    
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    while q:
        dist, curr = q.popleft()
        
        for d in dirs:
            ny, nx = curr[0] + d[0], curr[1] + d[1]
            if 0 <= ny < s and 0 <= nx < s and kappa[ny, nx] > 0.0:
                step_c = dist + (1.414 if d[0]!=0 and d[1]!=0 else 1.0)
                if step_c < cost_map[ny, nx]:
                    cost_map[ny, nx] = step_c
                    q.append((step_c, (ny, nx)))
                    
    return cost_map

def extract_bfs_path(cost_map, start, goal):
    s = cost_map.shape[0]
    path = [start]
    curr = start
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for _ in range(s * s):
        if curr == goal:
            break
        best_cost = float('inf')
        best_n = None
        for d in dirs:
            ny, nx = curr[0] + d[0], curr[1] + d[1]
            if 0 <= ny < s and 0 <= nx < s:
                if cost_map[ny, nx] < best_cost:
                    best_cost = cost_map[ny, nx]
                    best_n = (ny, nx)
        if best_n is None or best_cost >= cost_map[curr[0], curr[1]]:
            break
        curr = best_n
        path.append(curr)
    return path

def run_lineum_precompute(kappa, mode, goal):
    s = kappa.shape[0]
    psi = np.zeros((s, s), dtype=np.complex128)
    phi = np.zeros((s, s), dtype=np.float64)
    delta = np.zeros((s, s), dtype=np.float64)
    
    cfg = CoreConfig(
        dissipation_rate=0.005, noise_strength=0.0, reaction_strength=0.1, 
        phi_diffusion=0.05, physics_mode_psi=mode, wave_lpf_enabled=True
    )
    
    ty, tx = goal
    # Inject globally but draw centrally
    for step in range(800):
        # Flood the map with energy
        psi += 0.01
        
        # Suction
        ty_s, ty_e = max(0, ty-2), min(s, ty+3)
        tx_s, tx_e = max(0, tx-2), min(s, tx+3)
        psi[ty_s:ty_e, tx_s:tx_e] *= 0.0
        
        state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
        psi, phi = state["psi"], state["phi"]
        
    return phi

def get_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024 # MB

def run_baseline_ablation():
    print("=== FORENSIC HEAD-TO-HEAD LATENCY BASELINE ===")
    kappa, default_start, goal = Maps.generate('labyrinth', 64)
    s = 64
    
    np.random.seed(42)
    agents_1000 = []
    while len(agents_1000) < 1000:
        y, x = np.random.randint(5, 59, 2)
        if kappa[y, x] > 0.0:
            agents_1000.append((y, x))
            
    agent_counts = [1, 10, 100, 1000]
    methods = ['astar', 'bfs_flow', 'lineum_diffusion', 'lineum_wave']
    
    csv_rows = ["Method,Agent_Count,Setup_Time,Queries_Time,Total_Time,Peak_RSS"]
    
    print("\\nMap: labyrinth (64x64)")
    for method in methods:
        print(f"\\n--- {method.upper()} ---")
        
        for ac in agent_counts:
            active_agents = agents_1000[:ac]
            
            t0 = time.time()
            setup_time = 0.0
            queries_time = 0.0
            
            if method == 'astar':
                setup_time = 0.0 # No setup
                t_q0 = time.time()
                for a in active_agents:
                    AStarBaseline.run(kappa, a, goal)
                queries_time = time.time() - t_q0
                
            elif method == 'bfs_flow':
                t_s0 = time.time()
                flow = run_bfs_flow_field(kappa, goal)
                setup_time = time.time() - t_s0
                t_q0 = time.time()
                for a in active_agents:
                    extract_bfs_path(flow, a, goal)
                queries_time = time.time() - t_q0
                
            elif method == 'lineum_diffusion':
                t_s0 = time.time()
                phi = run_lineum_precompute(kappa, "diffusion", goal)
                setup_time = time.time() - t_s0
                t_q0 = time.time()
                for a in active_agents:
                    LineumRouter.extract_path(phi, kappa, a[1], a[0], goal[1], goal[0], s)
                queries_time = time.time() - t_q0
                
            elif method == 'lineum_wave':
                t_s0 = time.time()
                phi = run_lineum_precompute(kappa, "wave_projected_soft", goal)
                setup_time = time.time() - t_s0
                t_q0 = time.time()
                for a in active_agents:
                    LineumRouter.extract_path(phi, kappa, a[1], a[0], goal[1], goal[0], s)
                queries_time = time.time() - t_q0
                
            total = setup_time + queries_time
            rss = get_memory()
            csv_rows.append(f"{method},{ac},{setup_time:.4f},{queries_time:.4f},{total:.4f},{rss:.1f}")
            print(f" Agents: {ac:4d} | Setup: {setup_time:.3f}s | Query: {queries_time:.3f}s | Total: {total:.3f}s | RAM: {rss:.1f}MB")
            
    with open('scripts/output/latency_baseline.csv', 'w') as f:
        f.write('\\n'.join(csv_rows))

if __name__ == '__main__':
    # Warmup Numpy/PyTorch JIT
    run_bfs_flow_field(np.ones((10,10)), (5,5))
    run_baseline_ablation()
