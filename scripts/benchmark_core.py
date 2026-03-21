import time
import numpy as np
import sys
import os

try:
    import psutil
    has_psutil = True
except ImportError:
    has_psutil = False

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import step_core, CoreConfig

def measure_run(cfg, s, iters):
    psi = np.zeros((s, s), dtype=np.complex128)
    phi = np.zeros((s, s), dtype=np.float64)
    kappa = np.ones((s, s), dtype=np.float64)
    delta = np.zeros((s, s), dtype=np.float64)
    
    latencies = []
    start_total = time.time()
    for _ in range(iters):
        t0 = time.time()
        psi[5, 5] += 1.0
        state = step_core({'psi': psi, 'phi': phi, 'kappa': kappa, 'delta': delta}, cfg)
        psi, phi = state['psi'], state['phi']
        latencies.append((time.time() - t0) * 1000)
    total_runtime = time.time() - start_total
    return latencies, total_runtime

def benchmark_routing_scaling():
    print('\\n=== ROUTING SCALING: DIFFUSION VS WAVE ===')
    sizes = [64, 128, 256, 512]
    
    for s in sizes:
        print(f'\\n-- Grid {s}x{s} --')
        for mode in ['diffusion', 'wave_projected_soft']:
            cfg = CoreConfig(dt=0.1, physics_mode_psi=mode, use_mode_coupling=False, wave_lpf_enabled=(mode != 'diffusion'))
            
            # Cold Run
            cold_lat, cold_tot = measure_run(cfg, s, iters=5)
            cold_ms = np.mean(cold_lat)
            
            # Warm Run
            if has_psutil:
                process = psutil.Process(os.getpid())
                mem_before = process.memory_info().rss / 1e6
                
            warm_lat, warm_tot = measure_run(cfg, s, iters=50)
            
            p50 = np.percentile(warm_lat, 50)
            p95 = np.percentile(warm_lat, 95)
            p99 = np.percentile(warm_lat, 99)
            
            mem_str = ''
            if has_psutil:
                mem_after = process.memory_info().rss / 1e6
                mem_str = f'Peak RSS: {mem_after:.1f}MB'
                
            print(f'[{mode.upper()}]')
            print(f'  Cold Run: {cold_ms:.2f} ms/step | Warm Avg: {np.mean(warm_lat):.2f} ms/step')
            print(f'  Total Warm Runtime (50 iters): {warm_tot:.3f} s | {mem_str}')
            print(f'  Latencies - p50: {p50:.2f}ms | p95: {p95:.2f}ms | p99: {p99:.2f}ms')

def benchmark_topology_wrap_around():
    print('\\n=== TOPOLOGY CORRECTNESS: TUNNELING VS WRAP-AROUND ===')
    s = 64
    
    def run_topo(mode, wall_start, wall_end):
        psi = np.zeros((s, s), dtype=np.complex128)
        phi = np.zeros((s, s), dtype=np.float64)
        kappa = np.ones((s, s), dtype=np.float64)
        delta = np.zeros((s, s), dtype=np.float64)
        kappa[wall_start:wall_end, :] = 0.0
        
        cfg = CoreConfig(dt=0.1, physics_mode_psi=mode, use_mode_coupling=False, wave_lpf_enabled=True, wave_damping_edge=10.0)
        for _ in range(100):
            psi[10, 32] += 1.0
            state = step_core({'psi': psi, 'phi': phi, 'kappa': kappa, 'delta': delta}, cfg)
            psi, phi = state['psi'], state['phi']
            
        top_e = np.sum(np.abs(psi[0:wall_start-2, :])**2)
        tunnel_e = np.sum(np.abs(psi[wall_end+2:50, :])**2)
        wrap_e = np.sum(np.abs(psi[55:64, :])**2)
        return top_e, tunnel_e, wrap_e

    for mode in ['wave_projected_soft', 'wave_projected']:
        print(f'\\nMode: {mode}')
        t, tun, w = run_topo(mode, 32, 33) # 1-pixel wall
        print(f'  1-px Wall -> Top: {t:.2f} | Tunnel Leak: {tun:.4f} | Wrap Leak: {w:.4f}')
        t, tun, w = run_topo(mode, 30, 40) # 10-pixel wall
        print(f'  10-px Wall-> Top: {t:.2f} | Tunnel Leak: {tun:.4f} | Wrap Leak: {w:.4f}')

def benchmark_hash_collision():
    print('\\n=== HASH TOPOLOGICAL SIGNATURE AVALANCHE ===')
    pass # Ignored for this specific table output to focus on Routing

if __name__ == '__main__':
    benchmark_routing_scaling()
    benchmark_topology_wrap_around()
