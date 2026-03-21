import numpy as np
import sys
import os

from forensic_correctness import Maps
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core

def compute_lineum_phi(kappa, start, goal, steps=800):
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
    return phi

class AugmentedSteeringAgent:
    def __init__(self, start, goal, kappa, field, mode="no_backtrack"):
        self.pos = start
        self.goal = goal
        self.kappa = kappa
        self.field = field
        self.mode = mode
        self.s = kappa.shape[0]
        self.path = [start]
        self.visited = set([start])
        self.reaches = False
        self.last_dy = 0
        self.last_dx = 0
        
    def step(self):
        y, x = self.pos
        if abs(y - self.goal[0]) <= 1 and abs(x - self.goal[1]) <= 1:
            self.reaches = True
            return False
            
        best_val = float('inf')
        best_pos = None
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < self.s and 0 <= nx < self.s:
                if self.kappa[ny, nx] <= 0.05: continue 
                
                val = self.field[ny, nx]
                
                if self.mode == "no_backtrack":
                    if (ny, nx) in self.visited:
                        val += 1000.0 # Heavy penalty
                        
                elif self.mode == "momentum":
                    # Reward keeping the same direction
                    dot = (dy * self.last_dy + dx * self.last_dx)
                    val -= dot * 0.05 * self.field[y, x] # Reward momentum
                    
                elif self.mode == "goal_impulse":
                    # Add tiny A* heuristic strictly to break flats
                    dist = np.hypot(self.goal[0] - ny, self.goal[1] - nx)
                    val += dist * 0.001
                    
                elif self.mode == "lookahead_2":
                    # Min of neighbors of neighbors
                    local_min = float('inf')
                    for ddy, ddx in dirs:
                        nny, nnx = ny + ddy, nx + ddx
                        if 0 <= nny < self.s and 0 <= nnx < self.s and self.kappa[nny, nnx] > 0.05:
                            if self.field[nny, nnx] < local_min:
                                local_min = self.field[nny, nnx]
                    val = local_min # Navigate based on 2-step horizon
                    if (ny, nx) in self.visited: val += 1000.0
                    
                if val < best_val:
                    best_val = val
                    best_pos = (ny, nx)
                    
        if best_pos is None or (best_pos in self.visited and self.mode != "momentum"):
            return False 
            
        self.last_dy = best_pos[0] - y
        self.last_dx = best_pos[1] - x
        self.pos = best_pos
        self.path.append(self.pos)
        self.visited.add(self.pos)
        return True
        
def evaluate_modes():
    print("=== PHASE 6: ORGANIC STEERING RESCUES ===")
    maps = ['empty', 'labyrinth', 'diagonal', 'symmetric']
    modes = ['no_backtrack', 'momentum', 'goal_impulse', 'lookahead_2']
    
    for mode in modes:
        success = 0
        print(f"\\n--- Mode: {mode} ---")
        for m in maps:
            kappa, start, goal = Maps.generate(m, 64)
            phi = compute_lineum_phi(kappa, start, goal)
            agent = AugmentedSteeringAgent(start, goal, kappa, phi, mode)
            for _ in range(300):
                if not agent.step(): break
            
            res = "PASS" if agent.reaches else "FAIL"
            print(f"Map: {m:>10} | {res} | Len: {len(agent.path)}")
            if agent.reaches: success += 1
        print(f"Overall Success for {mode}: {success}/4")

if __name__ == '__main__':
    evaluate_modes()
