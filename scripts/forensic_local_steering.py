import numpy as np
import time
import os
import sys
import collections

from forensic_correctness import Maps
from forensic_baseline import run_bfs_flow_field

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core

def compute_lineum_phi(kappa, start, goal, mode="wave_projected_soft", steps=800):
    s = kappa.shape[0]
    psi = np.zeros((s, s), dtype=np.complex128)
    phi = np.zeros((s, s), dtype=np.float64)
    delta = np.zeros((s, s), dtype=np.float64)
    cfg = CoreConfig(dissipation_rate=0.005, reaction_strength=0.1, phi_diffusion=0.05, physics_mode_psi=mode)
    
    ty, tx = goal
    sy, sx = start
    for _ in range(steps):
        psi[sy, sx] += 1.0 # Simulate global presence
        ty_s, ty_e = max(0, ty-2), min(s, ty+3)
        tx_s, tx_e = max(0, tx-2), min(s, tx+3)
        psi[ty_s:ty_e, tx_s:tx_e] *= 0.1
        state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
        psi, phi = state['psi'], state['phi']
    return phi

class LocalSteeringAgent:
    def __init__(self, start, goal, kappa, scalar_field):
        self.pos = start
        self.goal = goal
        self.kappa = kappa
        self.field = scalar_field
        self.s = kappa.shape[0]
        self.path = [start]
        
        self.hit_wall = False
        self.corner_cut = False
        self.oscillating = False
        self.reaches = False
        self.valid = False
        
    def step(self):
        y, x = self.pos
        if abs(y - self.goal[0]) <= 1 and abs(x - self.goal[1]) <= 1:
            self.reaches = True
            self.valid = not self.hit_wall and not self.corner_cut
            return False # Stop
            
        best_val = float('inf')
        best_pos = None
        
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < self.s and 0 <= nx < self.s:
                if self.kappa[ny, nx] <= 0.05: continue # Blocked
                
                # Check corner cutting
                if dy != 0 and dx != 0:
                    if self.kappa[y, nx] <= 0.05 and self.kappa[ny, x] <= 0.05:
                        continue 
                        
                val = self.field[ny, nx]
                if val < best_val:
                    best_val = val
                    best_pos = (ny, nx)
                    
        if best_pos is None or best_pos in self.path:
            self.oscillating = True
            return False # Stuck in local minima or oscillating
            
        self.pos = best_pos
        self.path.append(self.pos)
        return True # Continue
        
def evaluate_steering():
    print("=== PHASE 5: FIELD GUIDANCE VERIFICATION ===")
    maps = ['empty', 'horizontal_wall_gap', 'diagonal', 'thin_slit', 'labyrinth', 
            'edge_obstacle', 'corner_backdoor', 'impossible', 'symmetric']
            
    csv_rows = ["Map,Method,PathLength,Reaches,HitWall,Oscillating,Valid"]
    
    for m in maps:
        kappa, start, goal = Maps.generate(m, 64)
        
        print(f"\\nEvaluate Map: {m}")
        
        # 1. Dijkstra Baseline
        dijkstra_field = run_bfs_flow_field(kappa, goal)
        d_agent = LocalSteeringAgent(start, goal, kappa, dijkstra_field)
        for _ in range(64 * 64):
            if not d_agent.step(): break
        print(f" [Dijkstra] Reach:{str(d_agent.reaches):5s}, Oscillating:{str(d_agent.oscillating):5s}, Length:{len(d_agent.path)}")
        csv_rows.append(f"{m},Dijkstra,{len(d_agent.path)},{d_agent.reaches},{d_agent.hit_wall},{d_agent.oscillating},{d_agent.valid}")
        
        # 2. Lineum Wave Baseline
        wave_field = compute_lineum_phi(kappa, start, goal, "wave_projected_soft")
        w_agent = LocalSteeringAgent(start, goal, kappa, wave_field)
        for _ in range(64 * 64):
            if not w_agent.step(): break
        print(f" [Lineum Wave] Reach:{str(w_agent.reaches):5s}, Oscillating:{str(w_agent.oscillating):5s}, Length:{len(w_agent.path)}")
        csv_rows.append(f"{m},Wave,{len(w_agent.path)},{w_agent.reaches},{w_agent.hit_wall},{w_agent.oscillating},{w_agent.valid}")

        # 3. Lineum Diffusion Baseline
        diff_field = compute_lineum_phi(kappa, start, goal, "diffusion")
        diff_agent = LocalSteeringAgent(start, goal, kappa, diff_field)
        for _ in range(64 * 64):
            if not diff_agent.step(): break
        print(f" [Lineum Diff] Reach:{str(diff_agent.reaches):5s}, Oscillating:{str(diff_agent.oscillating):5s}, Length:{len(diff_agent.path)}")
        csv_rows.append(f"{m},Diffusion,{len(diff_agent.path)},{diff_agent.reaches},{diff_agent.hit_wall},{diff_agent.oscillating},{diff_agent.valid}")

    with open('scripts/output/forensic_local_steering.csv', 'w') as f:
        f.write('\n'.join(csv_rows))
        
if __name__ == '__main__':
    evaluate_steering()
