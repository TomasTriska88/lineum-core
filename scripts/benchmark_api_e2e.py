import time
import os
import sys
import numpy as np
import json

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)

sys.path.append(os.path.join(root_dir, 'portal', 'src', 'lib', 'data'))
from routing_backend.main import RouteRequest, AgentDef, Point, extract_path
from forensic_correctness import Maps

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core

def generate_request_dict(n_agents):
    kappa, start, goal = Maps.generate('labyrinth', 64)
    agents = []
    np.random.seed(42)
    for i in range(min(n_agents, 500)):
        y, x = np.random.randint(5, 59, 2)
        if kappa[y, x] > 0.0:
            agents.append({"id": f"a{i}", "start": {"x": int(x), "y": int(y)}, "color": "#FFFFFF"})
            
    # Send 500 explicitly, let backend generate the rest up to n_agents via `agent_count`
    return {
        "size": 64,
        "agents": agents,
        "target": {"x": int(goal[1]), "y": int(goal[0])},
        "kappa_flat": kappa.flatten().tolist(),
        "max_steps": 100,
        "agent_count": n_agents,
        "return_paths": True
    }

def run_lifecycle(n_agents, is_cold):
    import gc
    gc.collect()
    
    raw_dict = generate_request_dict(n_agents)
    
    # 1. PARSE (Pydantic)
    t0 = time.time()
    req = RouteRequest(**raw_dict)
    t_parse = time.time() - t0
    
    # 2. SOLVE (Physics setup + stepping)
    t1 = time.time()
    kappa = np.array(req.kappa_flat).reshape((64, 64))
    psi = np.zeros((64, 64), dtype=np.complex128)
    phi = np.zeros((64, 64), dtype=np.float64)
    delta = np.zeros((64, 64), dtype=np.float64)
    cfg = CoreConfig(physics_mode_psi="wave_projected_soft", wave_lpf_enabled=True)
    
    # Vectorize start coords to bypass pure python loops in physics step
    ys = [a.start.y for a in req.agents]
    xs = [a.start.x for a in req.agents]
    y_arr = np.array(ys, dtype=int)
    x_arr = np.array(xs, dtype=int)
    
    for step in range(100):
        psi[y_arr, x_arr] += 1.0
        psi[req.target.y, req.target.x] *= 0.1
        state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
        psi, phi = state['psi'], state['phi']
    t_solve = time.time() - t1
    
    # 3. SAMPLE (Gradient Extraction - capped to 500 visual agents as per API)
    t2 = time.time()
    paths = {}
    visual_agents = req.agents[:500] if len(req.agents) > 500 else req.agents
    for idx, agent in enumerate(visual_agents):
        # We enforce Svelte limit here to measure reality of what CPU does
        px, py = extract_path(phi, kappa, agent.start.x, agent.start.y, req.target.x, req.target.y, 64)
        paths[agent.id] = {"x": px, "y": py, "color": agent.color}
    t_sample = time.time() - t2
    
    # 4. SERIALIZE (JSON Assembly)
    t3 = time.time()
    payload = {
        "step": 100,
        "max_steps": req.max_steps,
        "phi_flat": phi.flatten().tolist(),
        "paths": paths
    }
    json_str = json.dumps(payload)
    out_size_mb = len(json_str) / 1024 / 1024
    t_serialize = time.time() - t3
    
    return [t_parse, t_solve, t_sample, t_serialize], out_size_mb

def profile_api():
    print("=== END-TO-END API LIFECYCLE BENCHMARK ===")
    counts = [1, 10, 100, 1000, 5000]
    
    # Warmup
    print("Warming up JIT...")
    run_lifecycle(10, True)
    
    csv_rows = ["State,Agent_Count,Parse_s,Solve_s,Sample_s,Serialize_s,Total_s,Payload_MB"]
    
    for c in counts:
        print(f"\\nProfiling N={c}")
        # Cold (First run of loop)
        cold_times, c_mb = run_lifecycle(c, True)
        
        # Warm (Avg of next 3)
        warm_arrays = [run_lifecycle(c, False)[0] for _ in range(3)]
        warm_times = np.mean(warm_arrays, axis=0)
        
        for state, times in [("Cold", cold_times), ("Warm", warm_times)]:
            t_tot = sum(times)
            csv_rows.append(f"{state},{c},{times[0]:.4f},{times[1]:.4f},{times[2]:.4f},{times[3]:.4f},{t_tot:.4f},{c_mb:.2f}")
            print(f"  [{state}] Parse:{times[0]:.3f}s | Solve:{times[1]:.3f}s | Sample:{times[2]:.3f}s | Ser:{times[3]:.3f}s | Total:{t_tot:.3f}s | Out:{c_mb:.2f}MB")
            
    with open('scripts/output/e2e_api_lifecycle.csv', 'w') as f:
        f.write('\\n'.join(csv_rows))
        
if __name__ == '__main__':
    profile_api()
