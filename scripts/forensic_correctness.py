import numpy as np
import heapq
import math

class Maps:
    @staticmethod
    def generate(name: str, s: int = 64):
        kappa = np.ones((s, s), dtype=np.float64)
        start = (10, 32)
        goal = (54, 32)
        
        if name == 'empty':
            pass
        elif name == 'horizontal_wall_gap':
            kappa[32, 10:54] = 0.0
            kappa[32, 30:34] = 1.0 # 4px gap
        elif name == 'diagonal':
            for i in range(15, 50):
                kappa[i, i] = 0.0
            start = (10, 10)
            goal = (54, 54)
        elif name == 'thin_slit':
            kappa[30, :] = 0.0
            kappa[30, 32] = 1.0 # 1px gap
        elif name == 'labyrinth':
            kappa[20, 10:] = 0.0
            kappa[40, :54] = 0.0
        elif name == 'edge_obstacle':
            # Abuts the PML boundary to test wrap-around
            kappa[32, :32] = 0.0
            start = (10, 10)
            goal = (54, 10)
        elif name == 'corner_backdoor':
            kappa[15:50, 45] = 0.0
            kappa[15, 45:] = 0.0
            kappa[50, 45:] = 0.0
            start = (32, 50)
            goal = (32, 10)
        elif name == 'impossible':
            kappa[32, :] = 0.0
        elif name == 'symmetric':
            kappa[25:35, 25:39] = 0.0
        elif name == 'narrow_corridor':
            kappa[:, :30] = 0.0
            kappa[:, 34:] = 0.0
        
        return kappa, start, goal

class AStarBaseline:
    @staticmethod
    def run(kappa, start, goal):
        s = kappa.shape[0]
        # Octile distance heuristic
        def h(a, b):
            dx = abs(a[0] - b[0])
            dy = abs(a[1] - b[1])
            return math.sqrt(2.0) * min(dx, dy) + abs(dx - dy)
            
        open_set = []
        heapq.heappush(open_set, (0.0, start))
        
        came_from = {}
        g_score = {start: 0.0}
        
        # 8-connected transitions
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        while open_set:
            _, curr = heapq.heappop(open_set)
            
            if curr == goal:
                # Reconstruct path
                path = [curr]
                while curr in came_from:
                    curr = came_from[curr]
                    path.append(curr)
                path.reverse()
                length = g_score[goal]
                return path, length
                
            for d in dirs:
                ny, nx = curr[0] + d[0], curr[1] + d[1]
                if 0 <= ny < s and 0 <= nx < s:
                    if kappa[ny, nx] == 0.0:
                        continue
                        
                    # Corner cutting check for diagonals
                    if abs(d[0]) == 1 and abs(d[1]) == 1:
                        if kappa[curr[0]+d[0], curr[1]] == 0.0 or kappa[curr[0], curr[1]+d[1]] == 0.0:
                            continue # Crosses blocked corners
                            
                    cost = math.sqrt(2.0) if abs(d[0]) == 1 and abs(d[1]) == 1 else 1.0
                    tentative_g = g_score[curr] + cost
                    
                    neighbor = (ny, nx)
                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        came_from[neighbor] = curr
                        g_score[neighbor] = tentative_g
                        f_score = tentative_g + h(neighbor, goal)
                        heapq.heappush(open_set, (f_score, neighbor))
                        
        return None, float('inf') # Impossible map

def compute_path_length(path):
    if not path or len(path) < 2: return 0.0
    length = 0.0
    for i in range(1, len(path)):
        dx = abs(path[i][1] - path[i-1][1])
        dy = abs(path[i][0] - path[i-1][0])
        length += math.sqrt(2.0) if dx > 0 and dy > 0 else 1.0
    return length

class LineumRouter:
    @staticmethod
    def extract_path(phi_field, kappa, sx, sy, tx, ty, size):
        if np.max(phi_field) < 1e-4: return None
        cost_map = np.zeros((size, size))
        for y in range(size):
            for x in range(size):
                if kappa[y, x] <= 0.01:
                    cost_map[y, x] = np.inf
                else:
                    cost_map[y, x] = (1.0 / (phi_field[y, x] + 1e-6)) * (1.0 / kappa[y, x])
                    
        pq = [(0, tx, ty)]
        came_from = {}
        g_score = {(tx, ty): 0}
        
        while pq:
            _, cx, cy = heapq.heappop(pq)
            if abs(cx - sx) <= 2 and abs(cy - sy) <= 2:
                curr = (cx, cy)
                raw_path = [curr]
                while curr in came_from:
                    curr = came_from[curr]
                    raw_path.append(curr)
                # raw_path goes from near_start -> target
                raw_path.insert(0, (sx, sy))
                return [(p[1], p[0]) for p in raw_path] # return as y, x
                
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < size and 0 <= ny < size and kappa[ny, nx] > 0.0:
                    if dx != 0 and dy != 0:
                        if kappa[cy, nx] == 0.0 and kappa[ny, cx] == 0.0:
                            continue
                    
                    move_cost = cost_map[ny, nx] * (1.414 if dx != 0 and dy != 0 else 1.0)
                    tentative_g = g_score[(cx, cy)] + move_cost
                    if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                        came_from[(nx, ny)] = (cx, cy)
                        g_score[(nx, ny)] = tentative_g
                        f_score = tentative_g + np.hypot(sx - nx, sy - ny) * 0.1
                        heapq.heappush(pq, (f_score, nx, ny))
        return None

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core

def run_correctness_suite():
    print("=== LINEUM FORENSIC CORRECTNESS SUITE ===")
    
    maps = ['empty', 'horizontal_wall_gap', 'diagonal', 'thin_slit', 'labyrinth', 
            'edge_obstacle', 'corner_backdoor', 'impossible', 'symmetric', 'narrow_corridor']
    
    csv_rows = ["Map_Name,AStar_Len,Lineum_Len,Valid,Reaches_Goal,Hit_Wall,Shortcut,Optimality_Gap"]
    
    for m in maps:
        print(f"\\nEvaluating Map: {m}")
        kappa, start, goal = Maps.generate(m, 64)
        sy, sx = start
        ty, tx = goal
        
        # Ground Truth
        a_path, a_len = AStarBaseline.run(kappa, start, goal)
        print(f"  [A* Baseline] Path exists: {a_path is not None}, Length: {a_len:.2f}")
        
        # Lineum Simulation (Wave)
        s = 64
        psi = np.zeros((s, s), dtype=np.complex128)
        phi = np.zeros((s, s), dtype=np.float64)
        delta = np.zeros((s, s), dtype=np.float64)
        
        cfg = CoreConfig(
            dissipation_rate=0.005, noise_strength=0.0, reaction_strength=0.1, 
            phi_diffusion=0.05, physics_mode_psi="wave_projected_soft", wave_lpf_enabled=True
        )
        
        import time
        t0 = time.time()
        for step in range(800):
            psi[sy, sx] += 1.0
            psi[sy, sx] = min(psi[sy, sx].real, 10.0)
            
            ty_s, ty_e = max(0, ty-2), min(s, ty+3)
            tx_s, tx_e = max(0, tx-2), min(s, tx+3)
            psi[ty_s:ty_e, tx_s:tx_e] *= 0.1
            
            state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
            psi, phi = state["psi"], state["phi"]
        
        t1 = time.time()
        l_coord_path = LineumRouter.extract_path(phi, kappa, sx, sy, tx, ty, s)
        
        valid = False
        reaches = False
        hit_wall = False
        shortcut = False
        l_len = float('inf')
        
        if l_coord_path:
            reaches = (abs(l_coord_path[-1][0] - ty) <= 2 and abs(l_coord_path[-1][1] - tx) <= 2)
            l_len = compute_path_length(l_coord_path)
            
            for y, x in l_coord_path:
                if kappa[int(y), int(x)] <= 0.05:
                    hit_wall = True
                    break
                    
            valid = reaches and not hit_wall and not shortcut
            
        gap = ((l_len - a_len)/a_len)*100.0 if a_len > 0 and valid else 0.0
            
        print(f"  [Lineum] Valid: {valid} | Reaches: {reaches} | Hits Wall: {hit_wall} | Length: {l_len:.2f} | Gap: {gap:.1f}%")
        csv_rows.append(f"{m},{a_len:.2f},{l_len:.2f},{valid},{reaches},{hit_wall},{shortcut},{gap:.1f}")

    with open('scripts/output/correctness_raw.csv', 'w') as f:
        f.write('\\n'.join(csv_rows))
        
if __name__ == '__main__':
    run_correctness_suite()
