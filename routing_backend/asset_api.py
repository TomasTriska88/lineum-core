from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field
import numpy as np
import base64
import io
import sys
import os
import math
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import step_core, CoreConfig

router = APIRouter(prefix="/api/v1/assets", tags=["assets"])

class VfxRequest(BaseModel):
    grid_size: int = 16 
    frames: int = 30     
    base_mass: float = 0.1
    mass_step: float = 0.1
    colormap: str = "magma"

@router.post("/generate/water_drop")
def generate_water_drop(req: VfxRequest):
    import time
    t0 = time.time()
    
    if req.grid_size > 256:
        raise HTTPException(status_code=400, detail="Grid size scaling bounds exceeded.")
        
    try:
        cmap = plt.get_cmap("gray") # Changed from req.colormap to "gray" as per instruction
    except ValueError:
        raise HTTPException(status_code=400, detail="Requested colormap not recognized.")
        
    frames_b64 = []
    
    # DECOUPLED PHYSICS ARCHITECTURE
    phys_size = 96
    sim_size = phys_size * 6 

    psi = np.full((sim_size, sim_size), 0.5, dtype=np.complex128)
    phi = np.zeros((sim_size, sim_size), dtype=np.float64)
    kappa = np.full((sim_size, sim_size), 0.25, dtype=np.float64)
    delta = np.zeros((sim_size, sim_size), dtype=np.float64)
    
    x_coords = np.arange(sim_size)
    y_coords = np.arange(sim_size)
    X, Y = np.meshgrid(x_coords, y_coords)
    
    dist = np.sqrt((X - sim_size/2)**2 + (Y - sim_size/2)**2)
    view_radius = phys_size / 2.0
    safe_zone = view_radius * 0.85
    vignette = 1.0 - np.clip((dist - safe_zone) / (view_radius - safe_zone), 0.0, 1.0)
    
    impact = 1.5 * np.cos(dist * 0.5) * np.exp(-(dist**2) / 8.0)
    psi = psi + impact + 0j
    
    config = CoreConfig(disable_quantum_noise=True, use_mode_coupling=False, physics_mode_psi="wave_baseline", dt=1.0, stencil_type="ISOTROPIC")

    # The dynamic acceleration mathematical target bounds ensuring API hits bounds within variable inputs!
    total_required_steps = view_radius / 0.10
    steps_per_frame = math.ceil(total_required_steps / req.frames)
    total_sim_steps = req.frames * steps_per_frame
    
    # Guarantee 20% terminal kinetic survival relative to frames perfectly avoiding kinetic vanishing mathematically
    decay_per_step = math.pow(0.2, 1.0 / total_sim_steps)

    for f in range(req.frames):
        for _ in range(steps_per_frame):
            state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, config)
            psi = state["psi"]
            phi = state["phi"]
            phi = phi * decay_per_step
        
        wave = np.real(psi)
        
        offset = (sim_size - phys_size) // 2
        wave_crop = wave[offset:offset+phys_size, offset:offset+phys_size]
        
        wave_centered = wave_crop - 0.5
        
        volume_contrast = np.tanh(wave_centered * 5.0)
        norm = np.clip((volume_contrast * 0.5) + 0.5, 0.0, 1.0)
        rgba = cmap(norm) 
        
        alpha_raw = np.abs(np.tanh(wave_centered * 5.0))
        vignette_crop = vignette[offset:offset+phys_size, offset:offset+phys_size]
        rgba[..., 3] = np.clip(alpha_raw * 1.2, 0.0, 1.0) * vignette_crop
        
        img_array = (rgba * 255).astype(np.uint8)
        img_hd = Image.fromarray(img_array)
        img = img_hd.resize((req.grid_size, req.grid_size), Image.Resampling.BILINEAR)
        
        buf = io.BytesIO()
        img.save(buf, format='PNG') 
        b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        frames_b64.append(b64)

    return {"frames": frames_b64}
