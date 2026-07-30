import numpy as np
import os
from dataclasses import dataclass
from typing import Dict, Any

try:
    import torch
except ImportError:
    torch = None


TORCH_AVAILABLE = torch is not None
DEVICE_MODES = frozenset({"numpy", "torch-cpu", "cuda"})
_configured_device_mode = os.environ.get("LINEUM_DEVICE", "").strip().lower()
USE_PYTORCH = TORCH_AVAILABLE and (
    _configured_device_mode in {"torch-cpu", "cuda"}
    or (
        not _configured_device_mode
        and os.environ.get("LINEUM_USE_PYTORCH", "0") == "1"
    )
)


@dataclass(frozen=True)
class CudaCompatibility:
    available: bool
    compatible: bool
    device_architecture: str | None
    compiled_architectures: tuple[str, ...]
    reason: str

class ExecutionPolicy:
    """
    Centralized policy for device selection, seeds, and determinism.
    All execution paths (CLI, API, Exploratory) must consult this layer.
    """
    _device = None
    _backend = None
    _requested_mode = None
    _selection_reason = None
    _deterministic_mode = False
    _is_canonical_run = False

    @classmethod
    def _resolve_device_mode(cls, device_mode=None):
        raw_mode = device_mode
        if raw_mode is None:
            raw_mode = os.environ.get("LINEUM_DEVICE")
        if raw_mode is None or not str(raw_mode).strip():
            legacy_pytorch = os.environ.get("LINEUM_USE_PYTORCH", "0") == "1"
            raw_mode = "torch-cpu" if legacy_pytorch or USE_PYTORCH else "numpy"
        mode = str(raw_mode).strip().lower()
        if mode not in DEVICE_MODES:
            valid = ", ".join(sorted(DEVICE_MODES))
            raise ValueError(f"LINEUM_DEVICE must be one of: {valid}")
        return mode

    @classmethod
    def cuda_compatibility(cls):
        if not TORCH_AVAILABLE:
            return CudaCompatibility(
                available=False,
                compatible=False,
                device_architecture=None,
                compiled_architectures=(),
                reason="PyTorch is not installed.",
            )
        if not torch.cuda.is_available():
            return CudaCompatibility(
                available=False,
                compatible=False,
                device_architecture=None,
                compiled_architectures=(),
                reason="CUDA is not available to PyTorch.",
            )
        try:
            major, minor = torch.cuda.get_device_capability()
            device_architecture = f"sm_{major}{minor}"
            compiled_architectures = tuple(torch.cuda.get_arch_list())
        except (AssertionError, RuntimeError) as exc:
            return CudaCompatibility(
                available=True,
                compatible=False,
                device_architecture=None,
                compiled_architectures=(),
                reason=f"CUDA compatibility could not be verified: {exc}",
            )
        compatible = device_architecture in compiled_architectures
        reason = (
            "CUDA device architecture is supported by this PyTorch build."
            if compatible
            else (
                f"CUDA device architecture {device_architecture} is not present in "
                f"this PyTorch build ({', '.join(compiled_architectures) or 'none'})."
            )
        )
        return CudaCompatibility(
            available=True,
            compatible=compatible,
            device_architecture=device_architecture,
            compiled_architectures=compiled_architectures,
            reason=reason,
        )

    @classmethod
    def _select_device(cls, requested_mode, enforce_canonical):
        cls._requested_mode = requested_mode
        cls._selection_reason = None
        if requested_mode == "numpy":
            cls._backend = "numpy"
            cls._device = None
            return
        if not TORCH_AVAILABLE:
            raise RuntimeError(
                f"LINEUM_DEVICE={requested_mode} requires an installed PyTorch build."
            )
        cls._backend = "pytorch"
        if enforce_canonical:
            cls._device = torch.device("cpu")
            if requested_mode == "cuda":
                cls._selection_reason = (
                    "Canonical audit requires the deterministic CPU pipeline; "
                    "the explicit CUDA request was not used."
                )
            return
        if requested_mode == "torch-cpu":
            cls._device = torch.device("cpu")
            return
        compatibility = cls.cuda_compatibility()
        if not compatibility.compatible:
            raise RuntimeError(compatibility.reason)
        cls._device = torch.device("cuda")

    @classmethod
    def init_core_determinism(
        cls,
        enforce_canonical=True,
        seed=42,
        device_mode=None,
    ):
        cls._is_canonical_run = enforce_canonical
        cls._deterministic_mode = True
        requested_mode = cls._resolve_device_mode(device_mode)
        cls._select_device(requested_mode, enforce_canonical)

        # Lock seeds
        if cls._backend == "pytorch":
            torch.manual_seed(seed)
            if cls._device.type == "cuda":
                torch.cuda.manual_seed_all(seed)
            torch.use_deterministic_algorithms(True, warn_only=True)

            # OS/environment level determinism
            os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':4096:8'

        np.random.seed(seed)
        np.random.RandomState(seed) # Explicit initialization fallback

    @classmethod
    def get_device(cls):
        if cls._backend is None:
            requested_mode = cls._resolve_device_mode()
            cls._select_device(requested_mode, cls._is_canonical_run)
        return cls._device

    @classmethod
    def uses_pytorch(cls):
        cls.get_device()
        return cls._backend == "pytorch"

    @classmethod
    def get_metadata(cls):
        d = cls.get_device()
        device_name = "CPU"
        if d is not None and d.type == 'cuda':
            device_name = torch.cuda.get_device_name(d)
        cuda_available = TORCH_AVAILABLE and torch.cuda.is_available()
        inspect_cuda = cls._requested_mode == "cuda" or (
            d is not None and d.type == "cuda"
        )
        cuda_status = cls.cuda_compatibility() if inspect_cuda else None

        return {
            "execution_device": d.type if d else "numpy",
            "execution_backend": cls._backend,
            "requested_device_mode": cls._requested_mode,
            "deterministic_mode": cls._deterministic_mode,
            "canonical_audit_allowed_on_cuda": False,
            "cuda_available": cuda_available,
            "cuda_compatible": cuda_status.compatible if cuda_status else None,
            "cuda_device_architecture": (
                cuda_status.device_architecture if cuda_status else None
            ),
            "cuda_compiled_architectures": (
                list(cuda_status.compiled_architectures) if cuda_status else []
            ),
            "device_name": device_name,
            "enforced_canonical": cls._is_canonical_run,
            "reason": cls._selection_reason,
        }

@dataclass(frozen=True)
class CoreConfig:
    # --- Physic Constants ---
    dt: float = 1.0
    psi_diffusion: float = 0.05
    phi_diffusion: float = 0.05
    dissipation_rate: float = 0.005
    reaction_strength: float = 0.0007
    noise_strength: float = 0.005
    drift_strength: float = -0.004
    
    # --- Integration Specifics ---
    stencil_type: str = "LAP4"  # "LAP4" or "LAP8"
    physics_mode_psi: str = "diffusion"  # "diffusion" | "wave_baseline" | "wave_projected" | "wave_projected_soft"
    disable_quantum_noise: bool = False
    # Experimental RD-0-C1 path. False preserves legacy per-update semantics.
    phi_diffusion_scales_with_dt: bool = False
    wave_damping_edge: float = 0.05
    wave_lpf_enabled: bool = False
    wave_lpf_cutoff: float = 0.35
    kappa_soft_blur_iters: int = 2
    
    # --- Mode Coupling (Energy Transfer) ---
    use_mode_coupling: bool = True
    mode_coupling_strength: float = 0.001
    
    # --- HDD Track (Mu) ---
    use_mu: bool = False
    mu_eta: float = 0.005
    mu_rho: float = 0.0001
    mu_cap: float = 10.0
    mu_peak_cutoff_ratio: float = 0.1
    
    # --- Safe Numerical CFL Guards (NOT Physics) ---
    psi_amp_cap: float = 1e6
    grad_cap: float = 1e6
    phi_cap: float = 1e6
    
    # --- Eq9 Escape Stabilizer ---
    fold_mode: str = "softabs"
    fold_scope: str = "escape"
    
    # --- Boundary Conditions ---
    disable_pml: bool = False

def _diffuse_complex_numpy(field, kappa, rate, stencil_type):
    k_up = np.roll(kappa, 1, axis=0)
    k_dn = np.roll(kappa, -1, axis=0)
    k_lf = np.roll(kappa, 1, axis=1)
    k_rt = np.roll(kappa, -1, axis=1)
    
    f_up = np.roll(field, 1, axis=0)
    f_dn = np.roll(field, -1, axis=0)
    f_lf = np.roll(field, 1, axis=1)
    f_rt = np.roll(field, -1, axis=1)
    
    if stencil_type == "LAP8":
        w_ortho = 1.0
        w_diag = 0.25
        k_ul = np.roll(k_up, 1, axis=1)
        k_ur = np.roll(k_up, -1, axis=1)
        k_dl = np.roll(k_dn, 1, axis=1)
        k_dr = np.roll(k_dn, -1, axis=1)
        
        f_ul = np.roll(f_up, 1, axis=1)
        f_ur = np.roll(f_up, -1, axis=1)
        f_dl = np.roll(f_dn, 1, axis=1)
        f_dr = np.roll(f_dn, -1, axis=1)
        
        sum_neighbors = (w_ortho * (f_up*k_up + f_dn*k_dn + f_lf*k_lf + f_rt*k_rt) + 
                        w_diag * (f_ul*k_ul + f_ur*k_ur + f_dl*k_dl + f_dr*k_dr))
        active_neighbors = (w_ortho * (k_up + k_dn + k_lf + k_rt) + 
                           w_diag * (k_ul + k_ur + k_dl + k_dr))
    else:
        # Default LAP4
        sum_neighbors = f_up*k_up + f_dn*k_dn + f_lf*k_lf + f_rt*k_rt
        active_neighbors = k_up + k_dn + k_lf + k_rt

    return rate * (sum_neighbors - active_neighbors * field)

def _diffuse_complex_torch(field, kappa, rate, stencil_type):
    import torch
    k_up = torch.roll(kappa, 1, dims=0)
    k_dn = torch.roll(kappa, -1, dims=0)
    k_lf = torch.roll(kappa, 1, dims=1)
    k_rt = torch.roll(kappa, -1, dims=1)
    
    f_up = torch.roll(field, 1, dims=0)
    f_dn = torch.roll(field, -1, dims=0)
    f_lf = torch.roll(field, 1, dims=1)
    f_rt = torch.roll(field, -1, dims=1)
    
    if stencil_type == "LAP8":
        w_ortho = 1.0
        w_diag = 0.25
        k_ul = torch.roll(k_up, 1, dims=1)
        k_ur = torch.roll(k_up, -1, dims=1)
        k_dl = torch.roll(k_dn, 1, dims=1)
        k_dr = torch.roll(k_dn, -1, dims=1)
        
        f_ul = torch.roll(f_up, 1, dims=1)
        f_ur = torch.roll(f_up, -1, dims=1)
        f_dl = torch.roll(f_dn, 1, dims=1)
        f_dr = torch.roll(f_dn, -1, dims=1)
        
        sum_neighbors = (w_ortho * (f_up*k_up + f_dn*k_dn + f_lf*k_lf + f_rt*k_rt) + 
                        w_diag * (f_ul*k_ul + f_ur*k_ur + f_dl*k_dl + f_dr*k_dr))
        active_neighbors = (w_ortho * (k_up + k_dn + k_lf + k_rt) + 
                           w_diag * (k_ul + k_ur + k_dl + k_dr))
    else:
        # Default LAP4
        sum_neighbors = f_up*k_up + f_dn*k_dn + f_lf*k_lf + f_rt*k_rt
        active_neighbors = k_up + k_dn + k_lf + k_rt

    return rate * (sum_neighbors - active_neighbors * field)


def _cap_complex_magnitude_numpy(z, cap):
    z = np.asarray(z, dtype=np.complex128)
    mag = np.abs(z)
    mask = mag > cap
    if np.any(mask):
        z[mask] = z[mask] * (cap / (mag[mask] + 1e-30))
    return z

def _cap_complex_magnitude_torch(z, cap):
    import torch
    mag = torch.abs(z)
    mask = mag > cap
    if torch.any(mask):
        scale = torch.ones_like(mag)
        scale[mask] = cap / (mag[mask] + 1e-8)
        z = z * scale
    return z


def _safe_angle_torch(z):
    import torch
    angles = torch.angle(z)
    return torch.where(torch.isnan(angles), torch.zeros_like(angles), angles)


def _step_numpy(state: Dict[str, Any], cfg: CoreConfig) -> Dict[str, Any]:
    psi = np.asarray(state.get("psi"), dtype=np.complex128)
    phi = np.asarray(state.get("phi"), dtype=np.float64)
    kappa = np.asarray(state.get("kappa"), dtype=np.float64)
    mu = np.asarray(state.get("mu", np.zeros_like(phi)), dtype=np.float64)
    # The external semantic delta if supplied
    delta = np.asarray(state.get("delta", np.zeros_like(phi)), dtype=np.float64) 
    
    size = psi.shape[0]

    amp = np.abs(psi)
    amp = np.clip(amp, 0.0, cfg.psi_amp_cap)

    grad_x, grad_y = np.gradient(amp + delta)
    grad_x = np.clip(grad_x, -cfg.grad_cap, cfg.grad_cap)
    grad_y = np.clip(grad_y, -cfg.grad_cap, cfg.grad_cap)
    grad_mag = np.sqrt(np.clip(grad_x**2 + grad_y**2, 0.0, 1e12))
    
    # Probabilistic Linon Generation
    if getattr(cfg, "disable_quantum_noise", False):
        linon_complex = 0.0
        fluctuation = 0.0
    else:
        probability = (1.0 / (1.0 + np.exp(-5.0 * (amp + grad_mag)))) * kappa
        linons = (np.random.rand(size, size) < probability).astype(np.float64)
        linon_effect = np.clip((0.03 + 0.02 * np.clip(amp, a_min=0, a_max=None)) * linons, 0.0, 10.0)
        linon_complex = linon_effect * np.exp(1j * np.angle(psi))

        fluctuation = np.clip(np.random.normal(0.0, cfg.noise_strength, (size, size)), -1.0, 1.0) * np.exp(1j * np.angle(psi))

    # Calculate mu-modulated drift multiplier (ALWAYS READ)
    drift_multiplier = 1.0 + mu

    phi_int = np.clip(phi, 0.0, 10.0)
    interaction_factor = 0.1 * np.tanh((0.04 * phi_int * kappa * drift_multiplier) / 0.1)
    interaction_term = interaction_factor * psi
    int_mag = np.abs(interaction_term)
    interaction_term = interaction_term / (1.0 + int_mag / 10.0)
        
    grad_phi_x, grad_phi_y = np.gradient(phi)
    phi_flow_term = cfg.drift_strength * (grad_phi_x + 1j * grad_phi_y) * kappa * drift_multiplier
    flow_mag = np.abs(phi_flow_term)
    phi_flow_term = phi_flow_term / (1.0 + flow_mag / 10.0)
    
    # 1. Kinematic update
    psi += phi_flow_term * cfg.dt
    psi = _cap_complex_magnitude_numpy(psi, cfg.psi_amp_cap)

    psi += ((linon_complex + fluctuation) * kappa + interaction_term) * cfg.dt

    psi -= 0.005 * psi * cfg.dt # dissipation
    psi += _diffuse_complex_numpy(psi, kappa, rate=cfg.psi_diffusion, stencil_type=cfg.stencil_type) * kappa * cfg.dt

    e_psi = np.abs(psi)**2

    # 2. Mode-Coupling or Baseline Reaction
    if cfg.use_mode_coupling:
        delta_e = cfg.mode_coupling_strength * e_psi * kappa * cfg.dt
        phi += delta_e
        
        # Energy conservation
        psi_mag_new = np.sqrt(np.maximum(e_psi - delta_e, 0.0))
        psi = (psi / (np.sqrt(e_psi) + 1e-12)) * psi_mag_new
    else:
        scale_ratio = (128.0 / size) ** 2
        dynamic_reaction = cfg.reaction_strength * scale_ratio
        # This is strictly a fallback mapping, avoiding amp^2 clipping logic (now driven purely by generic absorption)
        phi += kappa * dynamic_reaction * (e_psi - phi) * cfg.dt

    phi_diffusion_step_scale = (
        cfg.dt if cfg.phi_diffusion_scales_with_dt else 1.0
    )
    phi += (
        kappa
        * cfg.phi_diffusion
        * _diffuse_complex_numpy(
            phi, kappa, rate=0.05, stencil_type=cfg.stencil_type
        )
        * phi_diffusion_step_scale
    )
    phi = np.clip(phi, 0.0, cfg.phi_cap)

    # 3. Mu update (The HDD track)
    if cfg.use_mu:
        # Dynamic relative sparsity: Isolate absolute structural peaks
        dynamic_floor = cfg.mu_peak_cutoff_ratio
        if dynamic_floor > 0 and dynamic_floor < 1.0:
            dynamic_floor = dynamic_floor * np.max(e_psi)
            
        active_e_psi = np.maximum(e_psi - dynamic_floor, 0.0)
        mu += cfg.mu_eta * active_e_psi * kappa * drift_multiplier * cfg.dt
        mu -= cfg.mu_rho * mu * cfg.dt
        mu = np.clip(mu, 0.0, cfg.mu_cap)

    # Numeric Fail-Safe
    if np.isnan(np.sum(psi)) or np.max(np.abs(psi)) >= cfg.psi_amp_cap * 0.99:
        print("!!! LINEUM FAIL-SAFE (CPU): Numeric divergence detected. Resetting Psi. !!!")
        psi = np.zeros_like(psi)

    e_psi_mean = float(np.mean(np.abs(psi)**2))
    max_abs_psi = float(np.max(np.abs(psi)))
    is_nan = bool(np.isnan(np.sum(psi)) or np.isnan(np.sum(phi)))

    out_state = {
        "psi": psi,
        "phi": phi,
        "kappa": kappa,
        "mu": mu,
        "telemetry": {
            "N_t": e_psi_mean,
            "max_abs_psi": max_abs_psi,
            "cap_triggers": 0,
            "cap_trigger_pct": 0.0,
            "fold_triggers": 0,
            "fold_trigger_pct": 0.0,
            "is_nan": is_nan,
            "n_step_1_delta": 0.0,
            "n_step_2_delta": 0.0,
            "spectral_leakage": 0.0,
            "norm_drift": abs(e_psi_mean)
        }
    }
    return out_state


_fft_symbol_cache = {}

def _get_fft_symbol(size: int, stencil_type: str, device, dtype):
    import torch
    import numpy as np
    key = (size, stencil_type, device, dtype)
    if key in _fft_symbol_cache:
        return _fft_symbol_cache[key]
    
    if stencil_type == "ISOTROPIC":
        # Analytical Isotropic Laplacian in Fourier Space
        # Bypasses all grid geometry artifacts ensuring perfectly radial boundary traversal.
        kx = torch.fft.fftfreq(size, d=1.0, device=device) * 2 * np.pi
        ky = torch.fft.fftfreq(size, d=1.0, device=device) * 2 * np.pi
        Ky, Kx = torch.meshgrid(ky, kx, indexing='ij')
        symbol = -(Kx**2 + Ky**2)
    else:
        kernel = torch.zeros((size, size), device=device, dtype=dtype)
        if stencil_type == "LAP8":
            kernel[0, 0] = -5.0
            kernel[1, 0] = 1.0; kernel[-1, 0] = 1.0
            kernel[0, 1] = 1.0; kernel[0, -1] = 1.0
            kernel[1, 1] = 0.25; kernel[-1, 1] = 0.25
            kernel[1, -1] = 0.25; kernel[-1, -1] = 0.25
        else:
            kernel[0, 0] = -4.0
            kernel[1, 0] = 1.0; kernel[-1, 0] = 1.0
            kernel[0, 1] = 1.0; kernel[0, -1] = 1.0
            
        symbol = torch.fft.fft2(kernel).real
        
    _fft_symbol_cache[key] = symbol
    return symbol

def _step_pytorch(state: Dict[str, Any], cfg: CoreConfig) -> Dict[str, Any]:
    import torch
    device = ExecutionPolicy.get_device()
    
    psi = torch.tensor(state.get("psi"), dtype=torch.complex128, device=device)
    phi = torch.tensor(state.get("phi"), dtype=torch.float64, device=device)
    kappa = torch.tensor(state.get("kappa"), dtype=torch.float64, device=device)
    mu = torch.tensor(state.get("mu", np.zeros_like(state.get("phi"))), dtype=torch.float64, device=device)
    delta = torch.tensor(state.get("delta", np.zeros_like(state.get("phi"))), dtype=torch.float64, device=device)

    size = psi.shape[0]

    amp = torch.abs(psi)
    amp = torch.clamp(amp, 0.0, cfg.psi_amp_cap)

    grads = torch.gradient(amp + delta)
    grad_x = torch.clamp(grads[0], -cfg.grad_cap, cfg.grad_cap)
    grad_y = torch.clamp(grads[1], -cfg.grad_cap, cfg.grad_cap)
    grad_mag = torch.sqrt(torch.clamp(grad_x**2 + grad_y**2, 0.0, 1e12))
    
    if getattr(cfg, "disable_quantum_noise", False):
        linons = torch.zeros((size, size), device=device, dtype=torch.float64)
        fluct_base = torch.zeros((size, size), device=device, dtype=torch.float64)
    else:
        probability = torch.sigmoid(5.0 * (amp + grad_mag)) * kappa
        linons = (torch.rand(size, size, device=device, dtype=torch.float64) < probability).to(torch.float64)
        fluct_base = torch.clamp(torch.normal(0.0, cfg.noise_strength, (size, size), device=device, dtype=torch.float64), min=-1.0, max=1.0)

    # Calculate mu-modulated drift multiplier (ALWAYS READ)
    drift_multiplier = 1.0 + mu

    phi_int = torch.clamp(phi, 0.0, 10.0)
    interaction_factor = 0.1 * torch.tanh((0.04 * phi_int * kappa * drift_multiplier) / 0.1)

    grads_phi = torch.gradient(phi)
    phi_flow_term = cfg.drift_strength * (grads_phi[0] + 1j * grads_phi[1]) * kappa * drift_multiplier
    flow_mag = torch.abs(phi_flow_term)
    phi_flow_term = phi_flow_term / (1.0 + flow_mag / 10.0)
    
    def compute_N(curr_psi):
        amp_c = torch.clamp(torch.abs(curr_psi), 0.0, cfg.psi_amp_cap)
        linon_eff = torch.clamp((0.03 + 0.02 * amp_c) * linons, max=10.0)
        linon_comp = linon_eff * torch.exp(1j * _safe_angle_torch(curr_psi))
        fluct_comp = fluct_base * torch.exp(1j * _safe_angle_torch(curr_psi))
        
        int_term = interaction_factor * curr_psi
        int_mag_c = torch.abs(int_term)
        int_term = int_term / (1.0 + int_mag_c / 10.0)
        
        return phi_flow_term + (linon_comp + fluct_comp) * kappa + int_term

    cap_trigger_count = 0
    fold_trigger_count = 0
    physics_mode = getattr(cfg, "physics_mode_psi", "diffusion")
    
    # Lab harness for testing Eq9 bounds
    def get_op(x, mode):
        if mode == "hardabs": return torch.abs(x) # Negative control
        if mode == "huber":
            ax = torch.abs(x)
            return torch.where(ax <= 0.01, (x**2)/(2*0.01), ax - 0.005) # Secondary check
        return torch.sqrt(x**2 + 1e-8) - 1e-4 # Candidate default (softabs)
    
    n_step_1_delta = 0.0
    n_step_2_delta = 0.0

    if "wave" in physics_mode:
        if cfg.dt != 0:
            e_before = torch.mean(torch.abs(psi)**2).item()
            psi = psi + compute_N(psi) * (cfg.dt / 2.0)
            n_step_1_delta = torch.mean(torch.abs(psi)**2).item() - e_before
        
        if cfg.dt != 0:
            symbol = _get_fft_symbol(size, cfg.stencil_type, device, torch.float64)
            
            psi_hat = torch.fft.fft2(psi)
            psi_hat = psi_hat * torch.exp(1j * cfg.psi_diffusion * symbol * cfg.dt)
            
            if getattr(cfg, "wave_lpf_enabled", False):
                freqs = torch.fft.fftfreq(size, device=device)
                fx, fy = torch.meshgrid(freqs, freqs, indexing='ij')
                fr = torch.sqrt(fx**2 + fy**2)
                lpf = torch.exp(-(fr / getattr(cfg, "wave_lpf_cutoff", 0.35))**8)
                psi_hat = psi_hat * lpf
                
            psi = torch.fft.ifft2(psi_hat)
            
        if cfg.dt != 0:
            e_before = torch.mean(torch.abs(psi)**2).item()
            psi = psi + compute_N(psi) * (cfg.dt / 2.0)
            n_step_2_delta = torch.mean(torch.abs(psi)**2).item() - e_before
            
        if "projected" in physics_mode:
            if "soft" in physics_mode:
                # Smooth the kappa obstacle boundary to avoid hard high-frequency edges
                k_sm = kappa
                for _ in range(getattr(cfg, "kappa_soft_blur_iters", 2)):
                    k_up = torch.roll(k_sm, 1, dims=0)
                    k_dn = torch.roll(k_sm, -1, dims=0)
                    k_lf = torch.roll(k_sm, 1, dims=1)
                    k_rt = torch.roll(k_sm, -1, dims=1)
                    k_sm = (k_sm + 0.25 * (k_up + k_dn + k_lf + k_rt)) / 2.0
                psi = psi * k_sm
            else:
                psi = psi * kappa
            
            gamma_obs = getattr(cfg, "wave_damping_edge", 0.0)
            if gamma_obs > 0.0:
                not_kappa = 1.0 - kappa
                k_up = torch.roll(not_kappa, 1, dims=0)
                k_dn = torch.roll(not_kappa, -1, dims=0)
                k_lf = torch.roll(not_kappa, 1, dims=1)
                k_rt = torch.roll(not_kappa, -1, dims=1)
                dilated = torch.clamp(not_kappa + k_up + k_dn + k_lf + k_rt, 0.0, 1.0)
                ring = torch.clamp(dilated - not_kappa, 0.0, 1.0)
                psi = psi * torch.exp(-gamma_obs * ring * cfg.dt)
                
        # --- HARD PADDING WALL & PML Absorbing Boundary (Torus Fix) ---
        pml_depth = 6
        if size > pml_depth * 2 and not getattr(cfg, "disable_pml", False):
            pml_mask = torch.zeros_like(phi)
            pml_mask[:pml_depth, :] = 1.0
            pml_mask[-pml_depth:, :] = 1.0
            pml_mask[:, :pml_depth] = 1.0
            pml_mask[:, -pml_depth:] = 1.0
            psi = psi * torch.exp(-20.0 * pml_mask * cfg.dt)
            
            psi[0, :] = 0.0
            psi[-1, :] = 0.0
            psi[:, 0] = 0.0
            psi[:, -1] = 0.0
        
        amp_post = torch.abs(psi)
        cap_mask = amp_post > cfg.psi_amp_cap
        cap_trigger_count = int(cap_mask.sum().item())
        if cap_trigger_count > 0:
            psi = _cap_complex_magnitude_torch(psi, cfg.psi_amp_cap)
    else:
        # Standard diffusion mode
        linon_effect = torch.clamp((0.03 + 0.02 * torch.clamp(amp, min=0.0)) * linons, max=10.0)
        linon_complex = linon_effect * torch.exp(1j * _safe_angle_torch(psi))
        fluctuation = fluct_base * torch.exp(1j * _safe_angle_torch(psi))
        
        interaction_term = interaction_factor * psi
        int_mag = torch.abs(interaction_term)
        interaction_term = interaction_term / (1.0 + int_mag / 10.0)

        psi += phi_flow_term * cfg.dt
        psi = _cap_complex_magnitude_torch(psi, cfg.psi_amp_cap)

        psi += ((linon_complex + fluctuation) * kappa + interaction_term) * cfg.dt

        psi -= 0.005 * psi * cfg.dt
        psi += _diffuse_complex_torch(psi, kappa, rate=cfg.psi_diffusion, stencil_type=cfg.stencil_type) * kappa * cfg.dt
        
        amp_post = torch.abs(psi)
        cap_mask = amp_post > cfg.psi_amp_cap
        cap_trigger_count = int(cap_mask.sum().item())

    e_psi = torch.abs(psi)**2

    # 2. Mode-Coupling or Baseline Reaction
    if cfg.use_mode_coupling:
        delta_e = cfg.mode_coupling_strength * e_psi * kappa * cfg.dt
        phi += delta_e
        
        psi_mag_new = torch.sqrt(torch.clamp(e_psi - delta_e, min=0.0))
        psi = (psi / (torch.sqrt(e_psi) + 1e-12)) * psi_mag_new
    else:
        scale_ratio = (128.0 / size) ** 2
        dynamic_reaction = cfg.reaction_strength * scale_ratio
        phi += kappa * dynamic_reaction * (e_psi - phi) * cfg.dt

    phi_diffusion_step_scale = (
        cfg.dt if cfg.phi_diffusion_scales_with_dt else 1.0
    )
    phi += (
        kappa
        * cfg.phi_diffusion
        * _diffuse_complex_torch(
            phi, kappa, rate=0.05, stencil_type=cfg.stencil_type
        )
        * phi_diffusion_step_scale
    )
    
    # ---------------------------------------------
    # [Eq9 Escape Channel / Overflow-Fold]
    # Eq9 overflow handling now supports a local SoftAbs-based smooth-fold path 
    # in the escape channel. Instead of only destructively clipping phi overflow 
    # at phi_cap, the solver can locally reflect overflow into an inverted phi 
    # gradient, improving escape behavior under saturation while preserving baseline 
    # behavior outside stressed regimes.
    # IMPORTANT: Negative phi is explicitly intended, tested, and functionally 
    # required for the escape behavior here. Do not add a lower-floor clamp 
    # (min=0.0) as it destroys the escape jet and worsens spectral leakage.
    # ---------------------------------------------
    if getattr(cfg, "fold_scope", "none") == "escape" and getattr(cfg, "fold_mode", "baseline") != "baseline":
        overflow_mag = torch.clamp(phi - cfg.phi_cap, min=0.0)
        fold_trigger_count += int((overflow_mag > 0).sum().item())
        reflected_pressure = get_op(overflow_mag, getattr(cfg, "fold_mode", "softabs"))
        # phi is allowed to safely reflect downwards (invert tension)
        phi = torch.clamp(phi, 0.0, cfg.phi_cap) - reflected_pressure
    else:
        # Legacy fallback
        phi = torch.clamp(phi, 0.0, cfg.phi_cap)

    # 3. Mu update (The HDD track)
    if cfg.use_mu:
        # Dynamic relative sparsity: Isolate absolute structural peaks
        dynamic_floor = cfg.mu_peak_cutoff_ratio
        if dynamic_floor > 0 and dynamic_floor < 1.0:
            dynamic_floor = dynamic_floor * torch.max(e_psi)
            
        active_e_psi = torch.clamp(e_psi - dynamic_floor, min=0.0)
        mu += cfg.mu_eta * active_e_psi * kappa * drift_multiplier * cfg.dt
        mu -= cfg.mu_rho * mu * cfg.dt
        mu = torch.clamp(mu, 0.0, cfg.mu_cap)

    is_nan = torch.isnan(torch.sum(psi))
    max_abs_psi = torch.max(torch.abs(psi))

    if is_nan or max_abs_psi >= cfg.psi_amp_cap * 0.99:
        print("!!! LINEUM FAIL-SAFE (GPU): Numeric divergence detected. Resetting Psi. !!!")
        psi = torch.zeros_like(psi)

    e_psi_mean = torch.mean(torch.abs(psi)**2).item()
    
    # Compute high frequency spectral leakage
    psi_hat_telemetry = torch.fft.fft2(psi)
    freqs = torch.fft.fftfreq(size, device=device)
    fx, fy = torch.meshgrid(freqs, freqs, indexing='ij')
    fr = torch.sqrt(fx**2 + fy**2)
    hf_mask = fr > 0.35
    hf_energy = torch.sum(torch.abs(psi_hat_telemetry[hf_mask])**2).item()
    total_energy = torch.sum(torch.abs(psi_hat_telemetry)**2).item() + 1e-12
    spectral_leakage = hf_energy / total_energy
    
    out_state = {
        "psi": psi.cpu().numpy(),
        "phi": phi.cpu().numpy(),
        "kappa": kappa.cpu().numpy(),
        "mu": mu.cpu().numpy(),
        "telemetry": {
            "N_t": e_psi_mean,
            "max_abs_psi": max_abs_psi.item(),
            "cap_triggers": cap_trigger_count,
            "cap_trigger_pct": (cap_trigger_count / (size*size)) * 100.0,
            "fold_triggers": fold_trigger_count,
            "fold_trigger_pct": (fold_trigger_count / (size*size)) * 100.0,
            "is_nan": bool(is_nan.item()) or torch.isnan(phi).any().item(),
            "n_step_1_delta": n_step_1_delta,
            "n_step_2_delta": n_step_2_delta,
            "spectral_leakage": spectral_leakage,
            "norm_drift": abs(e_psi_mean)
        }
    }
    return out_state


def step_core(state: Dict[str, Any], cfg: CoreConfig = CoreConfig()) -> Dict[str, Any]:
    """
    The Single Source of Truth for Lineum Canonical Eq-4' Physics.
    Evaluates the continuous topological math across the discretized ROM (\\kappa) and RAM (\\phi).
    Uses the explicit execution policy; CUDA is never selected implicitly.
    """
    assert "psi" in state and "phi" in state and "kappa" in state, "State must contain psi, phi, and kappa."
    
    if ExecutionPolicy.uses_pytorch():
        return _step_pytorch(state, cfg)
            
    return _step_numpy(state, cfg)


# ── Forward-compatible aliases (Step A - Renaming safely) ──
# Eq4Config/step_eq4 are legacy names. Conceptually we
# now operate under "Eq-7 / Wave Core", but the config dataclass is the
# same structure. New code should use CoreConfig / step_core.
Eq4Config = CoreConfig
step_eq4 = step_core
