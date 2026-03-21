import time
import os
import sys
import numpy as np
import json
import psutil

from forensic_correctness import Maps

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core

def get_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024 # MB

def profile_field_latency():
    print("=== PHASE 5: GUIDANCE FIELD API LATENCY ===")
    counts = [1, 10, 100, 1000, 5000]
    kappa, start, goal = Maps.generate('labyrinth', 64)
    s = 64
    
    np.random.seed(42)
    agents_5000 = []
    while len(agents_5000) < 5000:
        y, x = np.random.randint(5, 59, 2)
        if kappa[y, x] > 0.0:
            agents_5000.append((y, x))
            
    cfg = CoreConfig(physics_mode_psi="wave_projected_soft", wave_lpf_enabled=True)
    
    csv_rows = ["Agent_Count,Solve_s,Serialize_s,Total_s,Payload_MB,Peak_RSS"]
    
    for c in counts:
        print(f"\\nProfiling Field API N={c}")
        active = agents_5000[:c]
        y_arr = np.array([a[0] for a in active], dtype=int)
        x_arr = np.array([a[1] for a in active], dtype=int)
        
        psi = np.zeros((s, s), dtype=np.complex128)
        phi = np.zeros((s, s), dtype=np.float64)
        delta = np.zeros((s, s), dtype=np.float64)
        
        t0 = time.time()
        for step in range(100):
            psi[y_arr, x_arr] += 1.0 # O(1) vectorized inject
            ty_s, ty_e = max(0, goal[0]-2), min(s, goal[0]+3)
            tx_s, tx_e = max(0, goal[1]-2), min(s, goal[1]+3)
            psi[ty_s:ty_e, tx_s:tx_e] *= 0.1
            
            state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
            psi, phi = state['psi'], state['phi']
        t_solve = time.time() - t0
        
        t1 = time.time()
        max_phi = np.max(phi)
        phi_normalized = (phi / max_phi).flatten().tolist() if max_phi > 0 else phi.flatten().tolist()
        payload = {
            "step": 100,
            "phi_flat": phi_normalized 
            # NO PATHS COMPUTED OR ATTACHED
        }
        json_str = json.dumps(payload)
        out_size_mb = len(json_str) / 1024 / 1024
        t_serialize = time.time() - t1
        
        rss = get_memory()
        tot = t_solve + t_serialize
        
        csv_rows.append(f"{c},{t_solve:.4f},{t_serialize:.4f},{tot:.4f},{out_size_mb:.3f},{rss:.1f}")
        print(f" [Field API] Solve:{t_solve:.3f}s | Serialize:{t_serialize:.3f}s | Total:{tot:.3f}s | Payload:{out_size_mb:.3f}MB | RAM:{rss:.1f}MB")
        
    with open('scripts/output/forensic_guidance_field.csv', 'w') as f:
        f.write('\\n'.join(csv_rows))
        
if __name__ == '__main__':
    profile_field_latency()
