import numpy as np
from lineum_core.math import step_core, CoreConfig

def test_disable_quantum_noise_maintains_perfect_vacuum():
    """
    By default, Lineum natively injects quantum fluctuations (linons/noise).
    Assert that setting disable_quantum_noise=True strictly enforces
    a mathematically flawless 0.0 variance on an unperturbed vacuum,
    preventing asset whiteout.
    """
    size = 32
    psi = np.full((size, size), 0.5, dtype=np.complex128)
    phi = np.zeros((size, size), dtype=np.float64)
    delta = np.zeros((size, size), dtype=np.float64)
    kappa = np.full((size, size), 0.25, dtype=np.float64)
    
    # 1. Execute completely clean physics block
    state_clean = step_core(
        {"psi": psi.copy(), "phi": phi.copy(), "kappa": kappa.copy(), "delta": delta.copy()},
        CoreConfig(disable_quantum_noise=True, use_mode_coupling=False, dt=1.0)
    )
    
    # Analyze the variance of the resulting real amplitude
    wave_clean = np.real(state_clean["psi"])
    assert np.var(wave_clean) < 1e-10, "Vacuum should be perfectly mathematically flat with quantum noise disabled."
    
    # 2. Verify the native engine still accurately boils when bypass is correctly disabled (default)
    state_noisy = step_core(
        {"psi": psi.copy(), "phi": phi.copy(), "kappa": kappa.copy(), "delta": delta.copy()},
        CoreConfig(disable_quantum_noise=False, use_mode_coupling=False, dt=1.0)
    )
    wave_noisy = np.real(state_noisy["psi"])
    assert np.var(wave_noisy) > 0.0, "Native Lineum vacuum must mathematically boil (fluctuate) without the bypass."
