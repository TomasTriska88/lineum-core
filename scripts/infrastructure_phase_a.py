import numpy as np
import scipy.ndimage
import scipy.spatial
import time
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core

class SyntheticInferenceMaps:
    @staticmethod
    def construct_map(name, s=64):
        kappa = np.ones((s, s), dtype=np.float64)
        start = (5, s // 2)
        goal = (s - 5, s // 2)
        
        if name == "bottleneck":
            kappa[30:35, 0:28] = 0.0
            kappa[30:35, 36:s] = 0.0
        elif name == "swamp_bypass":
            cx, cy = s//2, s//2
            for y in range(s):
                for x in range(s):
                    if np.hypot(y-cy, x-cx) < 15:
                        kappa[y, x] = 0.1
        elif name == "gates":
            kappa[20, 0:s] = 0.0
            kappa[20, 10:15] = 1.0 # open gate
            kappa[40, 0:s] = 0.0
            kappa[40, 50:55] = 1.0 # open gate
        elif name == "valleys":
            # Hard center mountain
            for y in range(15, 50):
                for x in range(20, 44):
                    kappa[y, x] = 0.0
            # Left valley is narrow but straight (x: 10-15) -> width 5
            kappa[15:50, 0:15] = 1.0 
            # Right valley is wide but longer (bump out)
            kappa[15:50, 44:s] = 1.0 
        elif name == "roundabout":
            kappa[20:44, 20:44] = 0.0 # giant center obstacle
        elif name == "dead_zone":
            # Room with one entrance
            kappa[10:54, 10:54] = 0.0
            kappa[12:52, 12:52] = 1.0 # inside is open
            kappa[52:54, 30:34] = 1.0 # door
            start = (5, 5)
            goal = (s - 5, s - 5)
            # The inside of the room is technically reachable, but the flow shouldn't go there
            
        return kappa, start, goal

def classical_medial_axis(kappa):
    # Skeleton representing the pure geometric centerlines of free space
    # Assumes kappa > 0.05 is free
    binary_space = (kappa > 0.05).astype(int)
    t0 = time.time()
    distance_map = scipy.ndimage.distance_transform_edt(binary_space)
    # Extract ridges of the distance map using Laplacian
    lap = scipy.ndimage.laplace(distance_map)
    ridge_count = np.sum(lap < -0.5)
    t1 = time.time()
    return ridge_count, (t1 - t0)

def compute_lineum_infrastructure(kappa, start, goal, mode, steps=800):
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
    
    # Topology Extractors
    corridor_area = np.sum(kappa > 0.05)
    
    if mode == "diffusion":
        # Diffusion highlights pressure / flow density (using laplacian of the field)
        lap = scipy.ndimage.laplace(phi)
        pressure_ridges = np.sum(lap < -0.001)
        skeleton_nodes = 0
    elif "wave" in mode:
        # Wave highlights Chladni nodes (destructive interference mapping skeletons)
        intensity = np.abs(psi)
        mean_int = np.mean(intensity)
        nodes = (intensity < (mean_int * 0.5)) & (kappa > 0.05)
        skeleton_nodes = np.sum(nodes)
        pressure_ridges = 0
        
    return skeleton_nodes, pressure_ridges, corridor_area, t_solve

def evaluate_phase_a():
    print("=== PHASE A: SYNTHETIC INFRASTRUCTURE INFERENCE ===")
    scenarios = ["bottleneck", "swamp_bypass", "gates", "valleys", "roundabout", "dead_zone"]
    
    for scene in scenarios:
        kappa, start, goal = SyntheticInferenceMaps.construct_map(scene, 64)
        c_skel, c_time = classical_medial_axis(kappa)
        
        w_skel, w_pres, c_area, w_time = compute_lineum_infrastructure(kappa, start, goal, "wave_projected_soft", steps=800)
        d_skel, d_pres, _, d_time = compute_lineum_infrastructure(kappa, start, goal, "diffusion", steps=2000)
        
        print(f"\\n--- {scene.upper()} ---")
        print(f"  [Classical Medial Axis] Skeleton pixels: {c_skel:4d} | Runtime: {c_time:.4f}s")
        print(f"  [Lineum Wave]       Chladni Skeleton px: {w_skel:4d} | Runtime: {w_time:.4f}s")
        print(f"  [Lineum Diffusion]  Pressure Ridges px : {d_pres:4d} | Runtime: {d_time:.4f}s")

if __name__ == '__main__':
    evaluate_phase_a()
