# Projection Copy versus Causal State: Known-Answer Wave Fixture

**Status:** validated known-answer observer fixture; Lineum application not executed  
**Version:** 0.2.0  
**Evidence cutoff:** 2026-08-01  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`  
**Recovered root version:** 0.4.14  
**Root evidence cutoff:** 2026-07-29  
**Root blob SHA:** `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`  
**Continuity version:** 0.3.0  
**Continuity evidence cutoff:** 2026-07-31  
**Continuity blob SHA:** `5304874451caf32313ad0e8e3c59e53958698d79`  
**Immediate conceptual predecessor:** `research/foundations/lineum-ancient-texts-dynamic-boundary-protocol-and-reconstruction-hypotheses.md`, version 0.1.0, blob `3ec1d893e4309cb2e06b97a2fc09d658f05ab149`  
**Earlier source audit:** `research/foundations/lineum-gnostic-enochic-dead-sea-scrolls-metaphor-audit.md`, version 0.2.0, blob `aa7895df7e66ff348159c8ecbb6d06a92f22950c`  
**Frozen preregistration checkpoint:** version 0.1.0, commit `26d69ae1e88296c94bae3a37a56c40b9626aece3`, blob `55fe94b2cff13de31845c9780ac2725237ebaffd`  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Scope:** A standalone known-answer observer fixture testing whether identical visible morphology and matched global scalar summaries imply identical causal state. The fixture uses the exactly solvable one-dimensional free Schrödinger equation, not the Lineum equation. It compares a complete complex state, an amplitude-only projection, an opposite-chirp state with the same density and global scalar summaries, a local-current reconstruction within a declared Gaussian family, and an energy-matched smooth random-phase control.  
**Central question:** Can an observer distinguish a copy that preserves only the visible image from a copy that preserves the hidden phase organization required for the same future?  
**Current confidence:** high that the declared known-answer fixture validly separates projected image from causal state; high that the result is numerically and analytically reproduced across the declared resolutions; high that the family-specific local-current reconstruction worked in this fixture; low that any current Lineum observer already captures the analogous causal state; no evidence that Lineum is quantum mechanics or that ancient texts encoded modern physics.

## 1. Answer first

The fixture passed its primary gate.

Two packets began with the same visible density, norm, centroid, width, mean momentum, and kinetic energy. Their only declared difference was the sign of a hidden spatial phase correlation. Three model-time units later:

```text
negative-chirp donor width:       0.9360021367
positive-chirp matched width:     3.5208095660
future density NRMSE:             0.7342728120
```

The donor focused while the scalar-matched control expanded.

A zero-phase image copy also failed to reproduce the donor future:

```text
zero-phase image width:           2.1360009363
future density NRMSE:             0.5504431435
```

A reconstruction using amplitude plus local current recovered the donor chirp and future to floating-point precision:

```text
reconstructed chirp:             -0.12000000000000001
future density NRMSE:             2.9461453002e-16
state infidelity:                 0
```

The plain-language result is:

> A perfect copy of the visible image was not a copy of the dynamical state. The missing information was not a mystical substance; in this known system it was ordinary phase organization, recoverable from a suitable current observable inside the declared family.

This validates an observer distinction only. It does not establish a Lineum particle, copying mechanism, soul, `pneuma`, branch, or physical correspondence.

## 2. Version history and preregistration correction

### 2.1 Preserved preregistration

Version 0.1.0 was committed before execution at:

```text
commit: 26d69ae1e88296c94bae3a37a56c40b9626aece3
blob:   55fe94b2cff13de31845c9780ac2725237ebaffd
```

It froze:

```text
L = 80
N in {256, 512, 1024}
primary N = 512
sigma = 2.0
c_minus = -0.12
c_plus = +0.12
t_eval = 3.0
random seed = 20260801
random modes = 1..8
support threshold = 1e-8 * max(rho)
primary density and width metrics
all acceptance thresholds
```

No parameter, seed, metric, threshold, or carrier was changed after output inspection.

### 2.2 Arithmetic transcription error discovered after execution

Version 0.1.0 contained the correct analytic formula:

```text
Var[x](t)
    = sigma^2
      + 2*t*Cov_sym[x,p](0)
      + t^2*Var[p](0)
```

but manually reported the positive-chirp substitution as:

```text
incorrect transcription: Var[x](3) = 10.3961, width approximately 3.2243
```

The correct substitution is:

```text
sigma^2 = 4
2*t*Cov = 2*3*0.96 = 5.76
t^2*Var[p] = 9*0.2929 = 2.6361

correct Var[x](3) = 4 + 5.76 + 2.6361 = 12.3961
correct width = sqrt(12.3961) = 3.52080956599473
```

Classification:

```text
error_type = arithmetic_transcription_error
formula_error = false
parameter_change = false
acceptance_threshold_change = false
result_invalidation = false
```

The executable calculation used the frozen formula, not the incorrect manually summed number. The analytic-width acceptance rule was defined against the formula and passed at every resolution. Git history preserves the original error.

## 3. Motivation and inherited evidence

The ancient-text source audit supplied only the question: can an image preserve appearance while omitting what makes a process continue?

The root Lineum programme already records related but separate evidence:

```text
exact live state plus exact future RNG state
    -> bit-for-bit continuation over the tested horizon;

same static recipe under independent developmental history
    -> broad morphology resemblance but not donor identity;

recipe plus live state
    -> no additional causal effect beyond live state;

existing copying experiments
    -> no content-specific descendant under the declared gates;

minimum-flux and image-overlap observers
    -> non-identifying because smooth or transported disorder can pass.
```

This fixture independently validates the observer principle in a system with a known analytic answer. It does not replay or extend the Lineum runs.

## 4. Evidence layers

### 4.1 What current Lineum computes

Nothing in current Lineum was executed or changed. No result about current `Psi`, `Phi`, `mu`, `kappa`, P2, a vortex collective, or a Core equation is produced here.

### 4.2 What was reproducibly observed

Under the declared free-wave fixture:

- all carriers shared the same initial density to floating-point tolerance;
- the donor and opposite chirp also matched mean momentum and kinetic energy exactly at reported precision;
- the matched packets evolved to strongly different densities and widths;
- the family-specific local-current reconstruction reproduced the donor;
- the random-phase control matched kinetic energy and mean momentum but diverged even more strongly;
- analytic moments, norm conservation, and three-resolution comparisons passed.

### 4.3 Cautious interpretation

A snapshot density, even supplemented by several global scalar summaries, was not sufficient to identify the causal wave state. Local phase-current organization carried decision-relevant information in this family.

### 4.4 Hypothesis or analogy

Lineum morphology, defect count, overlap, orientation, collective invariant vectors, `mu` traces, and ancient image language may have analogous observer limitations. This remains untested in Lineum.

### 4.5 Real-physics and metaphysical boundary

The free Schrödinger equation is established for appropriate nonrelativistic quantum systems. The fixture is dimensionless and deliberately prepared. It does not show that:

- Lineum is a quantum theory;
- a Lineum phase is a soul;
- `pneuma` is wave phase or current;
- ancient authors described a wavefunction;
- a missing observer variable is metaphysical.

## 5. Mathematical system

Use dimensionless units:

```text
hbar = 1
mass = 1
```

Evolution:

```text
i * partial_t psi(x,t) = -(1/2) * partial_xx psi(x,t)
```

Periodic numerical domain:

```text
x in [-L/2, L/2)
L = 80
N in {256, 512, 1024}
```

Exact spectral propagation for the represented periodic state:

```text
psi_hat(k,t) = psi_hat(k,0) * exp(-i*k^2*t/2)
k = 2*pi*fftfreq(N, d=L/N)
```

Initial amplitude and phase family:

```text
A(x) proportional to exp(-x^2/(4*sigma^2))
sigma = 2
psi_c(x,0) = A(x) * exp(i*c*x^2)
c_minus = -0.12
c_plus = +0.12
t_eval = 3
```

Analytic moments:

```text
Var[x](0) = sigma^2
Cov_sym[x,p](0) = 2*c*sigma^2
Var[p](0) = 1/(4*sigma^2) + 4*c^2*sigma^2

Var[x](t)
    = sigma^2
      + 2*t*Cov_sym[x,p](0)
      + t^2*Var[p](0)
```

Correct analytic widths at `t = 3`:

```text
c = -0.12: 0.9360021367496979
c =  0.00: 2.1360009363293826
c = +0.12: 3.52080956599473
```

## 6. Carrier definitions

```text
IC1-A complete donor:
    A * exp(-0.12*i*x^2)

IC1-B amplitude-only image:
    A

IC1-C opposite hidden organization:
    A * exp(+0.12*i*x^2)
    same density, norm, centroid, variance, mean momentum, and kinetic energy as A

IC1-D amplitude plus local-current reconstruction:
    recover c from j/rho = 2*c*x inside rho > 1e-8*max(rho)

IC1-E smooth random phase:
    seed 20260801, modes 1..8, zero density-weighted mean momentum,
    phase-gradient kinetic energy matched to A

IC1-F family coordinate:
    known sign and magnitude of c inside the declared Gaussian-chirp family
```

IC1-D and IC1-F are intentionally family-specific. They demonstrate that a compact sufficient coordinate may exist after the model class is known. They are not generic wavefunction reconstruction algorithms.

## 7. Frozen metrics

```text
norm N = integral |psi|^2 dx
centroid X = integral x*|psi|^2 dx / N
variance Vx = integral (x-X)^2*|psi|^2 dx / N
width W = sqrt(Vx)
mean momentum P = integral Im(conj(psi)*partial_x psi) dx / N
kinetic energy K = (1/2)*integral |partial_x psi|^2 dx

fidelity F
    = |integral conj(psi_A)*psi_test dx|^2 / (N_A*N_test)

state infidelity = 1-F

density NRMSE
    = sqrt(mean((rho_test-rho_A)^2)) / sqrt(mean(rho_A^2))

width relative error
    = |W_test-W_A| / W_A

norm drift
    = |N(t)-N(0)| / N(0)
```

## 8. Acceptance results

### 8.1 Initial image equality

Frozen limits:

```text
density NRMSE <= 1e-12
norm relative difference <= 1e-12
centroid absolute difference <= 1e-10
variance relative difference <= 1e-12
```

Observed primary-grid maxima across A-F:

```text
density NRMSE:          2.472799585886279e-16
norm relative diff:     1.1102230246251568e-16
centroid absolute diff: 1.3877787807814457e-16
variance relative diff: 3.330669073875469e-16
verdict: pass
```

### 8.2 Opposite-chirp scalar matching

Frozen limits:

```text
A-C mean momentum absolute difference <= 1e-9
A-C kinetic energy relative difference <= 1e-9
```

Observed:

```text
mean momentum absolute difference: 0
kinetic energy relative difference: 0
A kinetic energy: 0.14645000000000002
C kinetic energy: 0.14645000000000002
verdict: pass
```

The stronger control therefore matched not only appearance but also the declared global energy and mean motion.

### 8.3 Norm conservation

Frozen limit:

```text
max norm drift <= 1e-12
```

Observed across all resolutions and carriers:

```text
2.220446049250313e-16
verdict: pass
```

### 8.4 Analytic widths

Frozen limit:

```text
relative error <= 5e-5
```

Observed maximum for A, B, C across all resolutions:

```text
2.0790684231309798e-16
verdict: pass
```

### 8.5 Local-current reconstruction

Frozen limits:

```text
|c_hat-c_minus| <= 1e-8
future density NRMSE <= 1e-8
state infidelity <= 1e-10
```

Observed at `N = 512`:

```text
c_hat:                 -0.12000000000000001
absolute chirp error:   1.3877787807814457e-17
future density NRMSE:   2.946145300150784e-16
state infidelity:       0
verdict: pass
```

### 8.6 Projection-copy rejection

Frozen limits for B and C:

```text
future density NRMSE >= 0.10
width relative error >= 0.50
```

Observed at `N = 512`:

```text
B amplitude-only image:
    future density NRMSE: 0.5504431434603918
    width relative error: 1.2820470728269113
    width:                2.1360009363293826
    verdict: pass rejection gate

C opposite chirp, scalar and energy matched:
    future density NRMSE: 0.7342728119998727
    width relative error: 2.7615400945780655
    width:                3.52080956599473
    verdict: pass rejection gate
```

### 8.7 Energy-matched random phase

Frozen validity limits:

```text
|mean momentum| <= 1e-8
kinetic-energy relative difference <= 1e-6
```

Observed at `N = 512`:

```text
|mean momentum|:                  1.734723475976807e-17
kinetic-energy relative diff:     0
future density NRMSE versus A:    0.8118333028193129
future width:                     3.114082435414552
verdict: valid control; divergent future
```

The random control phase contains a linear correction used to remove density-weighted mean momentum. The Gaussian amplitude is negligible at the periodic seam, and the result was identical across the declared resolutions to reported precision. This control remains supporting rather than necessary for the primary result.

### 8.8 Resolution sensitivity

Frozen limit:

```text
max width difference between N=512 and N=1024 for A, B, C <= 1e-5
```

Observed:

```text
1.1102230246251565e-16
verdict: pass
```

### 8.9 Continuity diagnostic

Using a centered spectral finite difference at `epsilon = 1e-5`:

```text
partial_t rho = -partial_x j
```

Observed normalized residual:

```text
8.678529200790882e-11
maximum absolute residual: 8.462591738478409e-12
verdict: supporting diagnostic pass
```

## 9. Human-readable result table

Primary grid `N = 512`, `t = 3`:

| Carrier | Initial kinetic energy | Initial mean momentum | Future width | Future density NRMSE vs A | Future fidelity vs A |
|---|---:|---:|---:|---:|---:|
| A complete donor | 0.14645000000000002 | -3.469446951953615e-17 | 0.9360021367496979 | 0 | 1 |
| B amplitude only | 0.03125 | -1.4963947229399215e-17 | 2.1360009363293826 | 0.5504431434603918 | 0.7213873210309517 |
| C opposite chirp | 0.14645000000000002 | -3.469446951953615e-17 | 3.52080956599473 | 0.7342728119998727 | 0.4619344188369688 |
| D current reconstruction | 0.14645000000000002 | 0 | 0.9360021367496978 | 2.946145300150784e-16 | 1 |
| E energy-matched random phase | 0.14645000000000002 | -1.734723475976807e-17 | 3.114082435414552 | 0.8118333028193129 | 0.47120137868636114 |
| F known-family chirp coordinate | 0.14645000000000002 | -3.469446951953615e-17 | 0.9360021367496979 | 0 | 1 |

## 10. Machine-readable retained output

```json
{
  "environment": {
    "python": "3.13.5",
    "numpy": "2.3.5",
    "platform": "Linux-6.12.13-x86_64-with-glibc2.41"
  },
  "frozen_parameters": {
    "L": 80.0,
    "N": [256, 512, 1024],
    "primary_N": 512,
    "sigma": 2.0,
    "c_minus": -0.12,
    "c_plus": 0.12,
    "t_eval": 3.0,
    "seed": 20260801,
    "random_modes": [1, 2, 3, 4, 5, 6, 7, 8],
    "support_relative_threshold": 1e-8
  },
  "preregistration_correction": {
    "type": "arithmetic_transcription_error",
    "incorrect_positive_variance": 10.3961,
    "correct_positive_variance": 12.3961,
    "correct_positive_width": 3.52080956599473,
    "formula_changed": false,
    "threshold_changed": false
  },
  "primary_results": {
    "c_hat": -0.12000000000000001,
    "initial_max_density_nrmse": 2.472799585886279e-16,
    "initial_max_norm_relative_difference": 1.1102230246251568e-16,
    "initial_max_centroid_absolute_difference": 1.3877787807814457e-16,
    "initial_max_variance_relative_difference": 3.330669073875469e-16,
    "A_C_mean_momentum_absolute_difference": 0.0,
    "A_C_kinetic_energy_relative_difference": 0.0,
    "max_norm_drift": 2.220446049250313e-16,
    "max_analytic_width_relative_error": 2.0790684231309798e-16,
    "D_future_density_nrmse": 2.946145300150784e-16,
    "D_future_state_infidelity": 0.0,
    "B_future_density_nrmse": 0.5504431434603918,
    "B_future_width_relative_error": 1.2820470728269113,
    "C_future_density_nrmse": 0.7342728119998727,
    "C_future_width_relative_error": 2.7615400945780655,
    "E_mean_momentum_absolute": 1.734723475976807e-17,
    "E_kinetic_energy_relative_difference": 0.0,
    "E_future_density_nrmse": 0.8118333028193129,
    "width_N512_N1024_max_difference_A_B_C": 1.1102230246251565e-16,
    "continuity_nrmse": 8.678529200790882e-11,
    "continuity_max_absolute_residual": 8.462591738478409e-12
  },
  "widths_by_resolution": {
    "256": {
      "A": 0.9360021367496978,
      "B": 2.136000936329383,
      "C": 3.52080956599473,
      "D": 0.9360021367496978,
      "E": 3.1140824354145518,
      "F": 0.9360021367496978
    },
    "512": {
      "A": 0.9360021367496979,
      "B": 2.1360009363293826,
      "C": 3.52080956599473,
      "D": 0.9360021367496978,
      "E": 3.114082435414552,
      "F": 0.9360021367496979
    },
    "1024": {
      "A": 0.9360021367496978,
      "B": 2.1360009363293826,
      "C": 3.52080956599473,
      "D": 0.9360021367496976,
      "E": 3.1140824354145518,
      "F": 0.9360021367496978
    }
  },
  "random_phase_metadata": {
    "scale": 0.47832648633721253,
    "base_phase_energy": 0.5035048053143143,
    "target_phase_energy": 0.11519999999999997,
    "density_weighted_mean_gradient_before_removal": 0.24457590447388264
  },
  "decision": "O1",
  "lineum_application": "not_executed"
}
```

## 11. Exact executed Python

The following code is the retained executable implementation of the primary matrix and resolution checks. It requires only NumPy.

```python
import numpy as np
import json
import math

L = 80.0
sigma = 2.0
c_minus = -0.12
c_plus = 0.12
t_eval = 3.0
seed = 20260801
Ns = [256, 512, 1024]


def grid(N):
    dx = L / N
    x = np.linspace(-L / 2, L / 2, N, endpoint=False)
    k = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    return x, dx, k


def normalize(psi, dx):
    return psi / np.sqrt(np.sum(np.abs(psi) ** 2) * dx)


def derivative(psi, k):
    return np.fft.ifft(1j * k * np.fft.fft(psi))


def propagate(psi, k, t):
    return np.fft.ifft(
        np.fft.fft(psi) * np.exp(-0.5j * (k ** 2) * t)
    )


def observables(psi, x, dx, k):
    rho = np.abs(psi) ** 2
    norm = np.sum(rho) * dx
    centroid = np.sum(x * rho) * dx / norm
    variance = np.sum((x - centroid) ** 2 * rho) * dx / norm
    dpsi = derivative(psi, k)
    momentum = np.sum(np.imag(np.conj(psi) * dpsi)) * dx / norm
    kinetic = 0.5 * np.sum(np.abs(dpsi) ** 2) * dx
    xp = np.real(
        np.sum(np.conj(psi) * x * (-1j * dpsi)) * dx
    ) / norm
    covariance = xp - centroid * momentum
    return {
        "norm": float(norm),
        "centroid": float(centroid),
        "variance": float(variance),
        "width": float(np.sqrt(variance)),
        "mean_momentum": float(momentum),
        "kinetic_energy": float(kinetic),
        "xp_cov": float(covariance),
    }


def density_nrmse(psi, reference):
    density = np.abs(psi) ** 2
    ref_density = np.abs(reference) ** 2
    return float(
        np.sqrt(np.mean((density - ref_density) ** 2))
        / np.sqrt(np.mean(ref_density ** 2))
    )


def fidelity(psi, reference, dx):
    norm_psi = np.sum(np.abs(psi) ** 2) * dx
    norm_ref = np.sum(np.abs(reference) ** 2) * dx
    overlap = np.sum(np.conj(reference) * psi) * dx
    return float(np.abs(overlap) ** 2 / (norm_psi * norm_ref))


def analytic_variance(c, t):
    covariance = 2 * c * sigma ** 2
    momentum_variance = (
        1 / (4 * sigma ** 2) + 4 * c ** 2 * sigma ** 2
    )
    return (
        sigma ** 2
        + 2 * t * covariance
        + t ** 2 * momentum_variance
    )


def make_random_phase(amplitude, x, dx, k, c_target):
    rng = np.random.default_rng(seed)
    coefficients = rng.normal(size=(8, 2))
    phase_base = np.zeros_like(x)
    for index, mode in enumerate(range(1, 9)):
        mode_k = 2 * np.pi * mode / L
        a, b = coefficients[index]
        phase_base += (
            a * np.cos(mode_k * x) + b * np.sin(mode_k * x)
        )

    phase_gradient = np.real(
        derivative(phase_base.astype(complex), k)
    )
    density = amplitude ** 2
    norm = np.sum(density) * dx
    weighted_mean = (
        np.sum(density * phase_gradient) * dx / norm
    )

    adjusted_phase = phase_base - weighted_mean * x
    adjusted_gradient = phase_gradient - weighted_mean
    target_phase_energy = 0.5 * np.sum(
        density * (2 * c_target * x) ** 2
    ) * dx
    base_phase_energy = 0.5 * np.sum(
        density * adjusted_gradient ** 2
    ) * dx
    scale = np.sqrt(target_phase_energy / base_phase_energy)

    return amplitude * np.exp(1j * scale * adjusted_phase), {
        "scale": float(scale),
        "base_phase_energy": float(base_phase_energy),
        "target_phase_energy": float(target_phase_energy),
        "weighted_mean_before_removal": float(weighted_mean),
    }


all_results = {}

for N in Ns:
    x, dx, k = grid(N)
    raw_amplitude = np.exp(-x ** 2 / (4 * sigma ** 2))
    amplitude = normalize(raw_amplitude.astype(complex), dx).real

    psi_A = amplitude * np.exp(1j * c_minus * x ** 2)
    psi_B = amplitude.astype(complex)
    psi_C = amplitude * np.exp(1j * c_plus * x ** 2)

    donor_derivative = derivative(psi_A, k)
    density = np.abs(psi_A) ** 2
    current = np.imag(np.conj(psi_A) * donor_derivative)
    support = density > 1e-8 * density.max()
    local_gradient = current[support] / density[support]
    c_hat = np.sum(
        density[support] * x[support] * local_gradient
    ) / (
        2 * np.sum(density[support] * x[support] ** 2)
    )

    psi_D = amplitude * np.exp(1j * c_hat * x ** 2)
    psi_E, random_metadata = make_random_phase(
        amplitude, x, dx, k, c_minus
    )
    psi_F = amplitude * np.exp(
        1j * np.sign(c_minus) * abs(c_minus) * x ** 2
    )

    carriers = {
        "A": psi_A,
        "B": psi_B,
        "C": psi_C,
        "D": psi_D,
        "E": psi_E,
        "F": psi_F,
    }

    initial = {
        name: observables(state, x, dx, k)
        for name, state in carriers.items()
    }
    evolved = {
        name: propagate(state, k, t_eval)
        for name, state in carriers.items()
    }
    final = {
        name: observables(state, x, dx, k)
        for name, state in evolved.items()
    }

    comparisons = {}
    for name, state in evolved.items():
        state_fidelity = fidelity(state, evolved["A"], dx)
        comparisons[name] = {
            "future_density_nrmse_vs_A": density_nrmse(
                state, evolved["A"]
            ),
            "future_fidelity_vs_A": state_fidelity,
            "future_state_infidelity_vs_A": 1 - state_fidelity,
            "future_width_relative_error_vs_A": abs(
                final[name]["width"] - final["A"]["width"]
            ) / final["A"]["width"],
            "initial_density_nrmse_vs_A": density_nrmse(
                carriers[name], carriers["A"]
            ),
            "initial_fidelity_vs_A": fidelity(
                carriers[name], carriers["A"], dx
            ),
            "norm_drift": abs(
                final[name]["norm"] - initial[name]["norm"]
            ) / initial[name]["norm"],
        }

    analytic = {}
    for name, chirp in (
        ("A", c_minus),
        ("B", 0.0),
        ("C", c_plus),
        ("D", c_hat),
        ("F", c_minus),
    ):
        analytic_width = np.sqrt(
            analytic_variance(chirp, t_eval)
        )
        analytic[name] = {
            "analytic_width": float(analytic_width),
            "numeric_width": final[name]["width"],
            "relative_error": float(
                abs(final[name]["width"] - analytic_width)
                / analytic_width
            ),
        }

    all_results[str(N)] = {
        "dx": dx,
        "c_hat": float(c_hat),
        "random_metadata": random_metadata,
        "initial": initial,
        "final": final,
        "comparisons": comparisons,
        "analytic": analytic,
    }

print(json.dumps(all_results, indent=2, sort_keys=True))
```

The continuity diagnostic was executed separately with the same grid, donor, derivative, and propagator:

```python
epsilon = 1e-5
rho = np.abs(psi_A) ** 2
j = np.imag(np.conj(psi_A) * derivative(psi_A, k))
minus_dx_j = -np.real(derivative(j.astype(complex), k))

rho_plus = np.abs(propagate(psi_A, k, epsilon)) ** 2
rho_minus = np.abs(propagate(psi_A, k, -epsilon)) ** 2
rho_t = (rho_plus - rho_minus) / (2 * epsilon)

continuity_nrmse = (
    np.sqrt(np.mean((rho_t - minus_dx_j) ** 2))
    / np.sqrt(np.mean(minus_dx_j ** 2))
)
```

## 12. Decision and interpretation

The frozen decision table selects:

```text
Outcome O1:
    A and D match;
    B and C share the initial image but diverge strongly in future density;
    analytic and resolution checks pass.
```

Supported within this fixture:

```text
snapshot_density_is_not_causal_state = true
selected_global_scalars_are_not_causal_state = true
matched_energy_and_mean_momentum_are_not_sufficient = true
local_current_recovers_declared_gaussian_chirp_family = true
complete_complex_state_determines_declared_unitary_future = true
```

Not supported:

```text
all_images_are_noncausal = false_as_universal_claim
all_phase_information_is_always_required = not_tested
local_current_reconstructs_arbitrary_state = not_tested
Lineum_observer_failure_of_same_type = not_tested
Lineum_copying_or_heredity = not_established
soul_pneuma_or_ancient_physics_correspondence = not_established
```

## 13. Root-programme impact matrix

| Root or child branch | Relation after result | Impact |
|---|---|---|
| Minimum-flux observer is non-identifying | `supports` | Provides a known-answer example in which visible state summaries omit causal phase organization. |
| Exact live-state continuation | `supports` | Independently illustrates why complete state can reproduce a future that a projection cannot. |
| Static recipe versus live state | `supports` | Supplies an analytic analogue of morphology-family resemblance without donor continuation. |
| Copying and heredity negative result | `unaffected` | No descendant or content transfer was created. |
| `mu` reduction-first programme | `supports` | Missing predictive state should be reconstructed from admissible observables or history before adding ontology. |
| Collective-particle hypothesis | `constrains` | Shape, count, and invariant summaries must be challenged by hidden-state-matched future interventions. |
| P2 multi-defect remnant | `unaffected` | No P2 package or current observer was executed. |
| Dynamic boundary and source ledgers | `unaffected` | The fixture contains no active boundary or resource store. |
| Ancient-text audit | `supports` | One textual motif generated a valid systems question; the text itself supplied no scientific evidence. |
| Physical quantum, particle, soul, and cosmology mappings | `unaffected` | No correspondence was promoted. |

## 14. Limitations

1. The fixture is linear, unitary, one-dimensional, and exactly solvable.
2. The Gaussian-chirp family makes the hidden coordinate unusually transparent.
3. IC1-D and IC1-F rely on knowing that family.
4. The result does not establish the minimal sufficient state for nonlinear stochastic Lineum dynamics.
5. The random-phase control is supporting and includes a negligible-seam linear phase correction.
6. No measurement noise, coarse grid, incomplete current, detector threshold, or phase singularity was tested.
7. No copying, growth, repair, source accounting, boundary, or collective membership process was simulated.
8. A successful known-answer observer is necessary but not sufficient for applying the same logic to Lineum.

## 15. Reopen triggers

Reopen or supersede this result if:

- an independent derivation finds the Gaussian moment formula wrong;
- the reported code does not reproduce the machine-readable values;
- another implementation reveals a periodic-domain artifact above the frozen tolerances;
- the random-phase control is shown to contaminate the primary A/B/C/D conclusion;
- a simpler known-answer fixture invalidates the chosen metrics;
- future Lineum application requires an observer for topology or collective relations that this scalar fixture cannot test.

## 16. Promotion boundary

This result may inform only research-observer design.

It does not authorize:

- a change to `lineum_core/`;
- a Lineum equation change;
- a public `image`, `spirit`, `pneuma`, or `causal soul` concept;
- a whitepaper claim;
- a quantum correspondence claim;
- a claim that phase is a soul or that ancient authors described wave mechanics;
- application to P2 without exact package recovery and a separate preregistration.

## 17. Current verdict

```text
fixture_status = validated_known_answer_observer_fixture
preregistration_arithmetic_error = disclosed_and_corrected_without_parameter_change
initial_image_sufficiency = falsified_in_declared_fixture
matched_global_scalar_sufficiency = falsified_in_declared_fixture
matched_energy_and_mean_momentum_sufficiency = falsified_in_declared_fixture
complete_complex_state_sufficiency = supported_for_declared_unitary_evolution
local_current_family_reconstruction = supported_in_declared_gaussian_family
energy_matched_random_phase_control = valid_and_divergent
lineum_application = not_executed
ancient_text_as_scientific_evidence = no
physical_or_metaphysical_correspondence = not_established
next_action = preregister_TS1_binary_mechanism_known_answer_fixture_before_execution
```
