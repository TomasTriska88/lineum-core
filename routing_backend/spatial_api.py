from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import numpy as np
import scipy.ndimage
import time
import base64

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import CoreConfig, step_core

router = APIRouter(prefix="/api/v1/spatial", tags=["spatial"])

class SeedDef(BaseModel):
    x: int
    y: int
    intensity: float

class SpatialRequest(BaseModel):
    grid_size: List[int] = Field(..., min_length=2, max_length=2)
    kappa: List[List[float]]
    source_seeds: Optional[List[SeedDef]] = []
    sink_targets: Optional[List[SeedDef]] = []
    diffusion_params: Optional[Dict[str, Any]] = None
    mode: str = "full" # "preview" or "full"

def execute_diffusion(kappa_np: np.ndarray, source_seeds: list, sink_targets: list, max_iters: int, enable_telemetry: bool = False, lap_cutoff: float = -0.1):
    size = kappa_np.shape[0]
    # Initialize basic physics fields
    psi = np.zeros((size, size), dtype=np.float64)
    phi = np.zeros((size, size), dtype=np.float64)
    delta = np.zeros((size, size), dtype=np.float64)
    
    # Process sources and sinks
    sources_arr = []
    for s in source_seeds:
        if hasattr(s, 'y'):
            if 0 <= s.y < size and 0 <= s.x < size: sources_arr.append([s.y, s.x, s.intensity])
        else:
            if 0 <= s['y'] < size and 0 <= s['x'] < size: sources_arr.append([s['y'], s['x'], s['intensity']])
    sources_np = np.array(sources_arr, dtype=np.float64) if sources_arr else np.empty((0,3))
    
    sinks_arr = []
    for s in sink_targets:
        if hasattr(s, 'y'):
            if 0 <= s.y < size and 0 <= s.x < size: sinks_arr.append([s.y, s.x, s.intensity])
        else:
            if 0 <= s['y'] < size and 0 <= s['x'] < size: sinks_arr.append([s['y'], s['x'], s['intensity']])
    sinks_np = np.array(sinks_arr, dtype=np.float64) if sinks_arr else np.empty((0,3))
    
    telemetry = []
    prev_phi = np.zeros((size, size), dtype=np.float64)
    
    for i in range(max_iters):
        # The solver engine takes 2D matrices and processes single tick updates
        psi, phi, delta = step_core(
            psi=psi,
            phi=phi,
            delta=delta,
            kappa=kappa_np,
            sources=sources_np,
            sinks=sinks_np,
            physics_mode_psi="diffusion", # Explicitly suppress wave oscillator
            dt=1.0,
            dx=1.0
        )
        
        if enable_telemetry and ((i + 1) % 100 == 0 or (i + 1) in [300, 1500, max_iters]):
            delta_phi = phi - prev_phi
            bots = rank_bottlenecks(phi, top_k=5, lap_cutoff=lap_cutoff)
            
            telemetry.append({
                "iteration": i + 1,
                "sum_phi": float(np.sum(phi)),
                "max_phi": float(np.max(phi)),
                "max_abs_delta_phi": float(np.max(np.abs(delta_phi))),
                "l2_norm_delta_phi": float(np.linalg.norm(delta_phi)),
                "number_of_detected_bottlenecks": len(bots),
                "primary_bottleneck_coords": f"({bots[0]['x']},{bots[0]['y']})" if len(bots) > 0 else "None",
                "RPI": min(100, int((float(np.max(phi)) / 2000000.0) * 100))
            })
            prev_phi = phi.copy()
            
    if enable_telemetry:
        return phi, telemetry
    return phi

def rank_bottlenecks(phi: np.ndarray, top_k: int = 5, lap_cutoff: float = -0.1):
    lap = scipy.ndimage.laplace(phi)
    # The lowest peaks (most negative laplacian) are the highest pressure constraints.
    # Find local minima. We'll do a simple mask
    min_mask = scipy.ndimage.minimum_filter(lap, size=3) == lap
    # Only consider significant negative pressure
    valid_minima = min_mask & (lap < lap_cutoff)
    
    ys, xs = np.where(valid_minima)
    vals = lap[ys, xs]
    
    if len(vals) == 0:
        return []
        
    # Sort asc (most negative first)
    sorted_idx = np.argsort(vals)
    
    ranked = []
    if len(vals) > 0:
        max_severity = float(np.max(np.abs(vals)))
    else:
        max_severity = 1.0
        
    for rank, idx in enumerate(sorted_idx[:top_k]):
        raw_sev = float(abs(vals[idx]))
        criticality = int((raw_sev / max_severity) * 100) if max_severity > 0 else 0
        ranked.append({
            "rank": rank + 1,
            "x": int(xs[idx]),
            "y": int(ys[idx]),
            "raw_severity": raw_sev,
            "criticality_score": criticality
        })
    return ranked

@router.post("/diffusion/infer")
async def infer_diffusion(req: SpatialRequest):
    t0 = time.time()
    s_y, s_x = req.grid_size
    if s_y != s_x or s_y > 512:
        raise HTTPException(status_code=400, detail="Invalid grid size. Must be square and <= 512.")
        
    # Schema validation
    kappa_np = np.array(req.kappa, dtype=np.float64)
    if kappa_np.shape != (s_y, s_x):
        raise HTTPException(status_code=400, detail="Kappa matrix dimensions do not match grid_size")
        
    if np.min(kappa_np) < 0.05:
        raise HTTPException(status_code=400, detail="Kappa contains values below minimum stability threshold (0.05)")
        
    iters = 1500
    lap_cutoff = -0.1
    if req.mode == "preview":
        iters = 300 # Fast topological estimate
        
    enable_telemetry = req.diffusion_params.get("enable_telemetry", False) if req.diffusion_params else False
    
    if enable_telemetry:
        phi, telemetry_log = execute_diffusion(kappa_np, req.source_seeds, req.sink_targets, iters, True, lap_cutoff)
    else:
        phi = execute_diffusion(kappa_np, req.source_seeds, req.sink_targets, iters)
        telemetry_log = []
    
    t1 = time.time()
    
    bottlenecks = rank_bottlenecks(phi, top_k=5, lap_cutoff=lap_cutoff)
    
    # Compress standard float64 to float32 base64 for UX payload speed
    phi_f32 = phi.astype(np.float32)
    phi_b64 = base64.b64encode(phi_f32.tobytes()).decode('utf-8')
    
    t2 = time.time()
    
    compute_ms = int((t1 - t0) * 1000)
    serialization_ms = int((t2 - t1) * 1000)
    
    # Compute relative pressure index (0-100 bounding)
    raw_peak = float(np.max(phi))
    # Empirical cap for "100" based on normal 1500 iters
    empirical_max = 500000.0 if req.mode == "preview" else 2000000.0
    relative_index = min(100, int((raw_peak / empirical_max) * 100))
    
    return {
        "status": "success",
        "grid_size": [s_y, s_x],
        "pressure_heatmap": phi_b64,
        "ranked_bottlenecks": bottlenecks,
        "summary_metrics": {
            "max_pressure_value": float(np.max(phi)),
            "relative_pressure_index": min(100, int((float(np.max(phi)) / 2000000.0) * 100)),
            "compute_time_ms": int((time.time() - t0) * 1000) # Changed t1 to t0 for total compute time
        },
        "telemetry_log": telemetry_log
    }

def generate_rect_kappa(size, blocks):
    k = np.ones((size, size), dtype=np.float64)
    for b in blocks:
        k[b[1]:b[3], b[0]:b[2]] = b[4]
    return k.tolist()

@router.get("/diffusion/demos/{scenario_id}")
async def get_demo(scenario_id: str):
    size = 128
    
    if scenario_id == "evacuation_door":
        # Narrowing exit crush-doors
        blocks = [
            (20, 0, 30, 60, 0.05), # Wall 1
            (20, 70, 30, 128, 0.05), # Wall 2
            (80, 0, 90, 40, 0.05), # Inner wall
            (80, 80, 90, 128, 0.05)
        ]
        k = generate_rect_kappa(size, blocks)
        return {
            "scenario_summary": "This scenario highlights where pressure dynamically accumulates when spatial flow is forced through narrowing structural exits.",
            "grid_size": [size, size],
            "kappa": k,
            "source_seeds": [{"x": 10, "y": 64, "intensity": 10.0}],
            "sink_targets": [{"x": 120, "y": 64, "intensity": 0.1}],
            "diffusion_params": {"max_iterations": 1000}
        }
        
    elif scenario_id == "swamp_bypass":
        k_np = np.ones((size, size), dtype=np.float64)
        # Giant swamp
        y, x = np.ogrid[0:size, 0:size]
        mask = (x - size//2)**2 + (y - size//2)**2 < (size//3)**2
        k_np[mask] = 0.2
        # Curved asphalt bypass
        for t in np.linspace(0, np.pi, 100):
            bx = int(size//2 + np.cos(t)*(size//2))
            by = int(size//2 + np.sin(t)*(size//2))
            if 0 <= by < size and 0 <= bx < size:
                k_np[by-4:by+4, bx-4:bx+4] = 1.0 
        return {
            "scenario_summary": "This scenario demonstrates topographical friction, showing how high-resistance terrain natively blocks out optimal vectors and cascades pressure into strict bypasses.",
            "grid_size": [size, size],
            "kappa": k_np.tolist(),
            "source_seeds": [{"x": 5, "y": size//2, "intensity": 20.0}],
            "sink_targets": [{"x": size-5, "y": size//2, "intensity": 0.1}],
            "diffusion_params": {"max_iterations": 1200}
        }
        
    elif scenario_id == "organic_canyon":
        k_np = np.full((size, size), 0.05, dtype=np.float64)
        for y in range(size):
            x_c = int(size//2 + np.sin(y/12.0) * 20)
            k_np[y, max(0, x_c-8):min(size, x_c+8)] = 0.9
        
        return {
            "scenario_summary": "This scenario tracks continuous pressure flow through a chaotic, organic valley, isolating the primary structural choke points where terrain organically limits throughput.",
            "grid_size": [size, size],
            "kappa": k_np.tolist(),
            "source_seeds": [{"x": size//2, "y": 5, "intensity": 50.0}],
            "sink_targets": [{"x": size//2, "y": size-5, "intensity": 0.05}],
            "diffusion_params": {"max_iterations": 1500}
        }
        
    elif scenario_id == "narrow_tunnel":
        k_np = np.full((size, size), 0.05, dtype=np.float64)
        k_np[60:68, :] = 1.0 # Narrow clear tunnel
        return {
            "scenario_summary": "Simple narrow tunnel boundary test.",
            "grid_size": [size, size],
            "kappa": k_np.tolist(),
            "source_seeds": [{"x": 10, "y": 64, "intensity": 20.0}],
            "sink_targets": [{"x": 118, "y": 64, "intensity": 0.1}]
        }
        
    elif scenario_id == "wide_corridor":
        k_np = np.full((size, size), 0.05, dtype=np.float64)
        k_np[30:98, :] = 1.0 # Wide clear corridor
        return {
            "scenario_summary": "Simple wide corridor boundary test.",
            "grid_size": [size, size],
            "kappa": k_np.tolist(),
            "source_seeds": [{"x": 10, "y": 64, "intensity": 50.0}],
            "sink_targets": [{"x": 118, "y": 64, "intensity": 0.1}]
        }
        
    elif scenario_id == "branching":
        k_np = np.full((size, size), 0.05, dtype=np.float64)
        k_np[60:68, 0:64] = 1.0 # Trunk
        k_np[30:38, 64:128] = 1.0 # Upper branch
        k_np[90:98, 64:128] = 1.0 # Lower branch
        k_np[30:98, 60:68] = 1.0 # Connection
        return {
            "scenario_summary": "Symmetrical branching for divergence tests.",
            "grid_size": [size, size],
            "kappa": k_np.tolist(),
            "source_seeds": [{"x": 10, "y": 64, "intensity": 40.0}],
            "sink_targets": [{"x": 118, "y": 34, "intensity": 0.1}, {"x": 118, "y": 94, "intensity": 0.1}]
        }
        
    elif scenario_id == "pegs":
        k_np = np.full((size, size), 1.0, dtype=np.float64)
        k_np[50:60, 40:50] = 0.05
        k_np[70:80, 40:50] = 0.05
        k_np[60:70, 80:90] = 0.05
        return {
            "scenario_summary": "Open field with obstacle pegs.",
            "grid_size": [size, size],
            "kappa": k_np.tolist(),
            "source_seeds": [{"x": 10, "y": 64, "intensity": 40.0}],
            "sink_targets": [{"x": 118, "y": 64, "intensity": 0.1}]
        }
        
    raise HTTPException(status_code=404, detail="Demo scenario not found")
