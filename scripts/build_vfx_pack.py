import numpy as np
from PIL import Image
import sys
import time
import os
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lineum_core.math import step_core, CoreConfig
import matplotlib.pyplot as plt

def run_vfx(preset_name, view_sizes=[32, 48, 64], angle_deg=0, variant=1):
    frames = 30
    phys_size = 96
    sim_size = phys_size * 6 

    pil_frames_hd = []   
    cmap = plt.get_cmap("gray")
    
    psi = np.full((sim_size, sim_size), 0.5, dtype=np.complex128)
    phi = np.zeros((sim_size, sim_size), dtype=np.float64)
    kappa = np.full((sim_size, sim_size), 0.25, dtype=np.float64)
    delta = np.zeros((sim_size, sim_size), dtype=np.float64)
    
    Y, X = np.ogrid[0:sim_size, 0:sim_size]
    
    cx, cy = sim_size/2, sim_size/2
    dist = np.sqrt((X - cx)**2 + (Y - cy)**2)
    view_radius = phys_size / 2.0
    safe_zone = view_radius * 0.85  
    vignette = 1.0 - np.clip((dist - safe_zone) / (view_radius - safe_zone), 0.0, 1.0)

    # Configuration map for presets
    preset_configs = {
        "water_drop": {"dt": 1.0, "disable_quantum_noise": False, "contrast_scale": 4.0, "dissipation": 0.015},
        "water_splash_solid": {"dt": 1.4, "disable_quantum_noise": False, "contrast_scale": 3.5, "dissipation": 0.08},
        "water_mud": {"dt": 0.6, "disable_quantum_noise": False, "contrast_scale": 3.2, "dissipation": 0.04},
        "water_ripple_idle": {"dt": 1.0, "disable_quantum_noise": False, "contrast_scale": 5.0, "dissipation": 0.005},
        "explosion": {"dt": 1.5, "disable_quantum_noise": False, "contrast_scale": 0.8, "dissipation": 0.08, "steps_factor": 1.5},
        "fire_burst": {"dt": 1.2, "disable_quantum_noise": True, "contrast_scale": 3.0, "dissipation": 0.03},
        "magic_shield": {"dt": 1.0, "disable_quantum_noise": False, "contrast_scale": 6.0},
        "acid_pool": {"dt": 0.8, "disable_quantum_noise": True, "contrast_scale": 4.0, "dissipation": 0.015},
        "blood_splatter": {"dt": 1.4, "disable_quantum_noise": False, "contrast_scale": 8.0, "dissipation": 0.02},
        "portal_vortex": {"dt": 1.2, "disable_quantum_noise": False, "contrast_scale": 5.0, "dissipation": 0.01},
        "smoke_grenade": {"dt": 0.5, "disable_quantum_noise": False, "contrast_scale": 2.5, "dissipation": 0.002},
        "lightning_strike": {"dt": 2.0, "disable_quantum_noise": True, "contrast_scale": 20.0, "dissipation": 0.08},
        "linon_vortex": {"dt": 0.8, "disable_quantum_noise": False, "contrast_scale": 15.0, "dissipation": 0.0},
        "water_wake": {"dt": 1.0, "disable_quantum_noise": False, "contrast_scale": 3.5, "dissipation": 0.015},
        # 5. Volumetric Multi-Phase Substepped Fire Physics
        "gas_explosion": {"dt": 0.55, "disable_quantum_noise": False, "contrast_scale": 1.8, "dissipation": 0.05, "steps_factor": 1.0},
        "campfire": {"dt": 1.2, "disable_quantum_noise": False, "contrast_scale": 2.2, "steps_factor": 1.5, "decay_per_step": 0.90},
        "fireball": {"dt": 1.4, "disable_quantum_noise": False, "contrast_scale": 2.0, "steps_factor": 2.0, "decay_per_step": 0.93},
    }

    if preset_name not in preset_configs:
        raise ValueError(f"Unknown preset {preset_name}")

    config_params = preset_configs[preset_name]
    dt = config_params.get("dt", 1.0)
    noise_enabled = not config_params.get("disable_quantum_noise", False)
    contrast_scale = config_params.get("contrast_scale", 5.0)
    dissipation = config_params.get("dissipation", 0.005)
    steps_factor = config_params.get("steps_factor", 1.0)
    decay_per_step = config_params.get("decay_per_step", None) # New parameter for fire physics

    # Apply specific initial conditions based on preset
    if preset_name == "water_drop":
        np.random.seed(50 + variant)
        asym = (np.random.rand(sim_size, sim_size) - 0.5) * 0.2
        impact = 1.5 * np.cos(dist * 0.5) * np.exp(-(dist**2) / 8.0) * (1.0 + asym)
        psi = psi + impact + 0j
        
    elif preset_name == "water_splash_solid":
        contrast_scale = 3.5
        dissipation = 0.08
        
        impact = np.zeros((sim_size, sim_size))
        np.random.seed(104 + variant**2 * 10)
        for _ in range(25):
            angle = np.random.rand() * np.pi * 2
            # Wide scatter across the 96px screen, leaving isolated drops
            radius = (np.random.rand()**1.2) * 44.0
            dx = np.cos(angle) * radius
            dy = np.sin(angle) * radius
            drop_dist2 = (X - (cx + dx))**2 + (Y - (cy + dy))**2
            # Sharper, heavier isolated droplets
            impact += np.exp(-drop_dist2 / 1.0) * 1.2
        
        psi = psi + impact + 0j
        # Microscopic phi to prevent global shockwave ring merging
        phi = phi + impact * 0.1
        
    elif preset_name == "water_mud":
        dt = 0.6
        noise_enabled = False
        contrast_scale = 3.2
        dissipation = 0.04
        
        impact = np.zeros((sim_size, sim_size))
        np.random.seed(200 + variant * 10)
        for _ in range(15):
            angle = np.random.rand() * np.pi * 2
            radius = (np.random.rand()**1.2) * 35.0
            dx = np.cos(angle) * radius
            dy = np.sin(angle) * radius
            drop_dist2 = (X - (cx + dx))**2 + (Y - (cy + dy))**2
            impact += np.exp(-drop_dist2 / 3.0) * 1.0
            
        psi = psi + impact + 0j
        phi = phi + impact * 0.5
        
    elif preset_name == "water_ripple_idle":
        dt = 1.0 # Ensure wave speed matches the walking phase (100% speed)
        contrast_scale = 5.0  # Even higher contrast for far edge visibility
        dissipation = 0.005
        
        # Hollow Ring Injection: Push water outwards from a radius, leaving the very center clean for models
        impact_ring = 1.0 * np.exp(-((dist - 6.0)**2) / 8.0)
        impact_core_dip = 0.6 * np.exp(-(dist**2) / 4.0)  # Gently depress the exact center
        
        psi = psi + (impact_ring - impact_core_dip) + 0j
        
    elif preset_name == "explosion":
        dt = 1.5                  # Fast shockwave expansion
        steps_factor = 1.5
        contrast_scale = 0.8      # Mnohem menší kontrast proti bandingu (dovolí plynulý gradient energie)
        dissipation = 0.08        # Extreme dissipation to instantly kill trailing "zebra" ringing
        
        # Clean massive hollow shockwave (pure displacement, no kinetic phi instability)
        impact_ring = 8.0 * np.exp(-((dist - 3.0)**2) / 6.0)
        impact_core_dip = 6.0 * np.exp(-(dist**2) / 4.0)
        
        psi = psi + (impact_ring - impact_core_dip) + 0j
        # Phi is left untouched to prevent PDE numerical ringing
        
    elif preset_name == "gas_explosion":
        noise_enabled = False     
        dt = 0.55                 # Bezpečné rychlé šíření okrajových vln
        steps_factor = 1.0        
        contrast_scale = 1.8      # Vyšší kontrast pro ohraničené a definované roje oblak
        dissipation = 0.05        

        
    elif preset_name == "fire_burst":
        dt = 1.2
        noise_enabled = True
        contrast_scale = 3.0
        dissipation = 0.03
        
    elif preset_name == "magic_shield":
        contrast_scale = 6.0
        ring_mask = np.abs(dist - 15.0) < 2.0
        kappa[ring_mask] = 0.0 
        impact = 2.0 * np.exp(-(dist**2) / 4.0)
        psi = psi + impact + 0j
        
    elif preset_name == "acid_pool":
        dt = 0.8
        noise_enabled = True
        contrast_scale = 4.0
        dissipation = 0.015
        
    elif preset_name == "blood_splatter":
        dt = 1.4
        contrast_scale = 8.0
        dissipation = 0.02
        # Asymmetric hit
        np.random.seed(42)  # Deterministic splatter
        asym = np.random.rand(sim_size, sim_size) * 0.5
        impact = (1.5 + asym) * np.exp(-(dist**2) / 10.0)
        psi = psi + impact + 0j
        phi = phi + impact * 2.0
        
    elif preset_name == "portal_vortex":
        dt = 1.2
        contrast_scale = 5.0
        dissipation = 0.01
        
    elif preset_name == "smoke_grenade":
        dt = 0.5 # Slow, thick movement
        contrast_scale = 2.5 # Very soft translucency
        dissipation = 0.002 # Hangs in the air a long time
        
    elif preset_name == "lightning_strike":
        dt = 2.0
        noise_enabled = True
        contrast_scale = 20.0 # Sharp, jagged digital look
        dissipation = 0.08 # Unstable, dissipates instantly
        np.random.seed(1337)
        strike = (np.random.rand(sim_size, sim_size) > 0.95).astype(float) * np.exp(-(dist**2) / 25.0)
        psi = psi + strike * 3.0 + 0j
        
    elif preset_name == "linon_vortex":
        dt = 0.8
        noise_enabled = False
        contrast_scale = 15.0 # extreme contrast to capture fine 4D phase wrapping
        dissipation = 0.0   # Linons are eternal standing waves
        
        # Real topological quantum phase vortex (Charge = 3 for beautiful spirals)
        theta = np.arctan2(Y - cy, X - cx)
        amp = 1.0 - np.exp(-(dist**2) / 10.0) # Hollow core
        # Inject the exact fundamental string equation directly into psi
        psi_defect = amp * np.exp(1j * theta * 3.0) 
        # Overlay the defect on the baseline
        psi = 0.5 + psi_defect * 0.4 * np.exp(-(dist**2) / 150.0)
        
    elif preset_name == "water_wake":
        dt = 1.0
        contrast_scale = 3.5  # Softer visual contrast for elegant game-feel
        dissipation = 0.015   # Higher dissipation so the trailing wake fades out gracefully
        # Dynamic injection in loop with 'angle_deg'

    elif preset_name == "campfire":
        dt = 1.2
        noise_enabled = False
        contrast_scale = 2.2
        steps_factor = 1.5
        
    elif preset_name == "fireball":
        dt = 1.4
        noise_enabled = False
        contrast_scale = 2.0
        steps_factor = 2.0

    else:
        raise ValueError(f"Unknown preset {preset_name}")
    
    config = CoreConfig(
        disable_quantum_noise=not noise_enabled, 
        use_mode_coupling=False, 
        physics_mode_psi="wave_baseline", 
        dt=dt, 
        dissipation_rate=dissipation,
        stencil_type="ISOTROPIC"
    )
    
    # Calculate bounding
    base_phase_velocity = 0.10
    total_required_steps = (view_radius / base_phase_velocity) * steps_factor
    
    # We keep physical speed calibrated to 30 frames, but simulate 45 frames
    # so the engine physically advances 50% further into the ripples' future.
    steps_per_frame = max(1, math.ceil(total_required_steps / 30.0)) 
    
    total_sim_steps = frames * steps_per_frame
    
    if preset_name == "campfire":
        decay_per_step = 0.90
    elif preset_name == "fireball":
        decay_per_step = 0.93
    else:
        decay_per_step = math.pow(0.2, 1.0 / total_sim_steps)
    
    rad = math.radians(angle_deg)
    dir_x = math.sin(rad) # X axis
    dir_y = -math.cos(rad) # Y axis (negative is up array)

    for f in range(frames):
        if preset_name == "water_drop" and f == 8:
            np.random.seed(100 + variant)
            dx = (np.random.rand() - 0.5) * 4.0
            dy = (np.random.rand() - 0.5) * 4.0
            crown_dist = np.sqrt((X - (cx + dx))**2 + (Y - (cy + dy))**2)
            crown = 0.8 * np.exp(-(crown_dist**2) / (3.0 + np.random.rand()))
            psi = psi + crown + 0j
            
        elif preset_name == "water_ripple_idle" and f < 20:
            shift = math.sin(f * 0.5) * 0.5
            shift_x = cx + shift
            shift_dist = np.sqrt((X - shift_x)**2 + (Y - cy)**2)
            ripple = 0.05 * np.exp(-(shift_dist**2) / 6.0)
            phi = phi + ripple
            
        elif preset_name == "fire_burst" and f < 10:
            burst = 5.0 * np.exp(-(dist**2) / 4.0) * (1.0 - (f/10.0))
            phi = phi + burst
            
        elif preset_name == "gas_explosion":
            # 100% LINEUM PHYSICS ENGINE (Eq-8)
            # Uživatel má naprostou pravdu: "mud" a "acid_pool" vypadají świetně,
            # protože jejich injekce hmoty je primitivní a nesymetrická!
            # Když jsem se snažil naprogramovat "kontinuální hoření stovek bublin",
            # vyrobil jsem uniformní kruh a rozbil gradienty do čisté bílé.
            # Řešení: Zkombinovat "water_mud" masivní kapky (na začátku)
            # s "acid_pool" bubláním hybnosti (během hoření). 
            
            # 1. Hlavní těleso mraku - kontinuální mikroskopické vaření plazmatu
            if f < 8:
                np.random.seed(300 + f * variant)
                # Uživatelská intuice: "když jich budeme mít dost, uděláme výbuch ne?"
                # Injektujeme obrovské množství drobných vln, které budou interferovat a tvořit detail
                for _ in range(70): 
                    if f < 2:
                        # 1. Počáteční zažehnutí: Udržujeme symetrický kulatý tlak pro hladký oválný start
                        r = np.random.rand() * 8.0
                    else:
                        # 2. Rayleigho–Taylorovy nestability: Expanze do zubatých tvarů s časem
                        r = np.random.rand() * 20.0 * (1.0 + f * 0.1) 
                    
                    angle = np.random.rand() * np.pi * 2.0
                    sx = cx + r * math.cos(angle)
                    sy = cy + r * math.sin(angle)
                    
                    dist = np.sqrt((X - sx)**2 + (Y - sy)**2)
                    size = 1.0 + np.random.rand() * 3.0 # Mikroskopické bublinky!
                    power = 0.3 + np.random.rand() * 0.5 
                    
                    psi += power * np.exp(-(dist**2) / (size**2))
                    
            # 2. Vnitřní mikroturbulence "vaření plazmatu" (jako acid_pool)
            if f < 12:
                np.random.seed(800 + f * variant)
                # Neustále bubláme hybnost (phi) z centra, aby se vlna "vařila" a nenechala střed prázdný
                for _ in range(8):
                    bx = cx + np.random.uniform(-10, 10)
                    by = cy + np.random.uniform(-10, 10)
                    b_dist = np.sqrt((X - bx)**2 + (Y - by)**2)
                    
                    # Drobné rázové vlnky vystřelují z centra
                    phi += 1.0 * np.exp(-(b_dist**2) / 4.0)

        elif preset_name == "smoke_grenade" and f < 15:
            # Continuous thick injection expanding outwards
            smoke = 1.0 * np.exp(-(dist**2) / (4.0 + f))
            phi = phi + smoke
            
        elif preset_name == "campfire":
            # Kontinuální lokální hoření posazené lehce dolů
            np.random.seed(400 + f * variant)
            
            # Ohniště (pevě ukotvené)
            burn_cx = cx
            burn_cy = cy + 10 # Ohniště je posunuté dolů od čistého středu
            
            # Křičíme tepelnou energii
            for _ in range(8):
                bx = burn_cx + np.random.uniform(-4, 4)
                by = burn_cy + np.random.uniform(-2, 2)
                b_dist = np.sqrt((X - bx)**2 + (Y - by)**2)
                phi += 0.8 * np.exp(-(b_dist**2) / 3.0)
                
            # Umělá gravitace / vztlak: potlačíme šíření vlny směrem dolů a do stran
            # Maska musí být absolutně plynulá (gradient), jinak vyvolá PDE ringing!
            dist_down = np.clip((Y - burn_cy) / 30.0, 0.0, 1.0)
            dist_side = np.clip(np.abs(X - cx) / 40.0, 0.0, 1.0)
            
            buoyancy_mask = 1.0 - (dist_down * 0.3) - (dist_side * 0.15)
            
            # Nesmíme škálovat absolutní psi (zničilo by to hladinu 0.5 a vyvolalo globální šok)
            # Tlumíme pouze relativní výchylku od 0.5 a kinetickou hybnost phi
            psi = 0.5 + (psi - 0.5) * buoyancy_mask
            phi *= buoyancy_mask
            
        elif preset_name == "fireball":
            # Letící ohnivá koule. Silný kontinuální zdroj letící vpřed.
            np.random.seed(500 + f * variant)
            
            # Startujeme vlevo a letíme doprava a lehce nahoru (jako kometa)
            fly_x = cx - 15 + (f / 30.0) * 30.0
            fly_y = cy + 5 - (f / 30.0) * 10.0
            
            # Ohnisko plazmy vpředu (Shockwave head)
            dist_head = np.sqrt((X - fly_x)**2 + (Y - fly_y)**2)
            phi += 1.5 * np.exp(-(dist_head**2) / 4.0)
            
            # Chaos v ohonu (mikrovýbuchy tažené za sebou)
            if f > 2:
                for _ in range(5):
                    # Injektujeme do vlečky za kometou
                    tail_x = fly_x - np.random.rand() * 8.0
                    tail_y = fly_y + np.random.rand() * 4.0
                    b_dist = np.sqrt((X - tail_x)**2 + (Y - tail_y)**2)
                    phi += 0.5 * np.exp(-(b_dist**2) / 2.0)
            
        elif preset_name == "water_wake" and f < 15:
            # Shift center by direction vector
            offset_x = (f / 15.0) * 15.0 * dir_x
            offset_y = (f / 15.0) * 15.0 * dir_y 
            wake_dist = np.sqrt((X - (cx + offset_x))**2 + (Y - (cy + offset_y))**2)
            # Drastically softer, smaller injection for 'game-feel' aesthetics
            wake_impact = 0.5 * np.exp(-(wake_dist**2) / 4.0)
            psi = psi + wake_impact + 0j
            phi = phi + (wake_impact * 0.4)

        for _ in range(steps_per_frame):
            state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, config)
            psi, phi = state["psi"], state["phi"]
            phi = phi * decay_per_step
        
        wave = np.real(psi)
        
        # Game-Feel Character Hollow Mask for wakes
        if preset_name == "water_wake":
            # Track character bounds (stops moving at f=15)
            move_factor = min(f, 15) / 15.0
            char_x = cx + move_factor * 15.0 * dir_x
            char_y = cy + move_factor * 15.0 * dir_y
            char_dist = np.sqrt((X - char_x)**2 + (Y - char_y)**2)
            # Soft black hole where the character's body/feet are
            char_mask = 1.0 - 0.85 * np.exp(-(char_dist**2) / 12.0)
            # Must offset wave back to 0.5 baseline for masking cleanly
            wave = (wave - 0.5) * char_mask + 0.5

        offset = (sim_size - phys_size) // 2
        wave_crop = wave[offset:offset+phys_size, offset:offset+phys_size]
        wave_centered = wave_crop - 0.5
        
        volume_contrast = np.tanh(wave_centered * contrast_scale)
        norm = np.clip((volume_contrast * 0.5) + 0.5, 0.0, 1.0)
        rgba = cmap(norm) 
        alpha_raw = np.abs(np.tanh(wave_centered * contrast_scale))
        vignette_crop = vignette[offset:offset+phys_size, offset:offset+phys_size]
        
        # Global smooth alpha fade ending in completely transparent padding frames
        if preset_name == "gas_explosion" or preset_name == "campfire" or preset_name == "fireball":
            # Nativní renderování Thermocline Shading (pozitivní = bílá plazma, negativní = kouř)
            offset = (sim_size - phys_size) // 2
            psi_crop = psi[offset:offset+phys_size, offset:offset+phys_size]
            
            # Mapování vlny: pozitivní tlak = erupce (fire), negativní vakuum = vakuum wake (smoke)
            val = np.tanh((np.real(psi_crop) - 0.5) * contrast_scale)
            
            # Rozštěpíme vlnu na Light a Shadow masky pro zachování stínování
            light_mask = np.clip(val, 0.0, 1.0)
            shadow_mask = np.clip(-val, 0.0, 1.0)
            
            # Grayscale Raw výstup: Zářivá plazma = Bílá, Toxický kouř = Tmavě šedá
            peak_color = np.array([255, 255, 255], dtype=float) 
            trough_color = np.array([80, 80, 80], dtype=float)
            
            # Aditivní smíchání fází vlnové rovnice do šedotónového bufferu
            colored = (peak_color * light_mask[..., None]) + (trough_color * shadow_mask[..., None])
            
            # Aktivita = intenzita obou jevů
            activity = np.abs(val)
            
            vignette_crop = vignette[offset:offset+phys_size, offset:offset+phys_size]
            
            # Fireball and Campfire don't fade out as quickly as an explosion
            if preset_name == "gas_explosion":
                fade_start_frame = int(frames * 0.40)
            else:
                fade_start_frame = int(frames * 0.70)
                
            fade_end_frame = frames - 5
            if f < fade_start_frame:
                global_fade = 1.0
            elif f >= fade_end_frame:
                global_fade = 0.0
            else:
                global_fade = 1.0 - ((f - fade_start_frame) / (fade_end_frame - fade_start_frame))
                
            # Jemný vizuál, kouř i zánět jsou jasně čitelné z activity
            alpha_channel = np.clip(activity * 255 * 1.5 * global_fade * vignette_crop, 0, 255)
            
            final_pixels = np.zeros((phys_size, phys_size, 4), dtype=np.uint8)
            final_pixels[..., :3] = np.clip(colored, 0, 255).astype(np.uint8)
            final_pixels[..., 3] = alpha_channel.astype(np.uint8)
            img_array = final_pixels # Use the custom rendered pixels
        
        if preset_name not in ["linon_vortex", "gas_explosion", "campfire", "fireball"]:
            empty_frames = 5 # 5 frames of pure invisible padding at the end
            fade_start_frame = int(frames * 0.60) # Start fading at 60% completion
            fade_end_frame = frames - empty_frames
            
            if f >= fade_end_frame:
                global_fade = 0.0
            elif f >= fade_start_frame:
                global_fade = 1.0 - ((f - fade_start_frame) / (fade_end_frame - fade_start_frame))
            else:
                global_fade = 1.0
        elif preset_name == "linon_vortex":
            global_fade = 1.0
        # For gas_explosion, global_fade is handled within its custom rendering block
        
        if preset_name != "gas_explosion": # Apply default alpha calculation if not gas_explosion
            rgba[..., 3] = np.clip(alpha_raw * 1.3, 0.0, 1.0) * vignette_crop * global_fade
            img_array = (rgba * 255).astype(np.uint8) # Default img_array
        
        img_hd = Image.fromarray(img_array)
        pil_frames_hd.append(img_hd)
    
    os.makedirs("output_assets/vfx_pack", exist_ok=True)
    
    for view_size in view_sizes:
        pil_frames_native = [img.resize((view_size, view_size), Image.Resampling.BILINEAR) for img in pil_frames_hd]
        pil_frames_upscaled = [img.resize((256, 256), Image.Resampling.NEAREST) for img in pil_frames_native]
        
        if preset_name == "water_wake":
            f_name = f"water_wake_{angle_deg}_{view_size}"
        elif preset_name in ["water_drop", "water_splash_solid", "water_mud", "gas_explosion"]:
            f_name = f"{preset_name}_v{variant}_{view_size}"
        else:
            f_name = f"{preset_name}_{view_size}"
            
        webp_path = f"output_assets/vfx_pack/{f_name}.webp"
        pil_frames_upscaled[0].save(
            webp_path, "WEBP", save_all=True, append_images=pil_frames_upscaled[1:], duration=33, loop=0
        )
        
        cols = min(8, frames)
        rows = (frames + cols - 1) // cols
        sheet = Image.new("RGBA", (cols * view_size, rows * view_size), (0,0,0,0))
        for idx, frame_img in enumerate(pil_frames_native):
            x = (idx % cols) * view_size
            y = (idx // cols) * view_size
            sheet.paste(frame_img, (x, y))
        
        sheet_path = f"output_assets/vfx_pack/spritesheet_{f_name}.png"
        sheet.save(sheet_path)
        print(f"Generated {f_name}")

if __name__ == "__main__":
    t0 = time.time()
    sizes = [16, 32, 48, 64, 128, 256, 512]
    base_presets = ["gas_explosion", "campfire", "fireball"]
    wake_angles = []
    print("Starting Final Full Optimized VFX Multiplexer Generation (with 16px-512px and masks)...")
    
    multi_variant = ["water_drop", "water_splash_solid", "water_mud", "gas_explosion"]
    for p in base_presets:
        if p in multi_variant:
            for v in [1, 2, 3]:
                run_vfx(p, view_sizes=sizes, variant=v)
        else:
            run_vfx(p, view_sizes=sizes)
        
    for ang in wake_angles:
        run_vfx("water_wake", view_sizes=sizes, angle_deg=ang)
            
    print(f"VFX AAA Matrix Generation completed perfectly via Multiplexing in {time.time()-t0:.2f}s")
