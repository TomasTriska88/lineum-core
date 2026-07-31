# Mu-Phi Reduction and Continuum/Discrete Ontology Preregistration

**Status:** active preregistration; one analytic implementation result recorded; no numerical experiment or physical validation claimed  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-07-31  
**Scope:** Core-only preregistration for testing whether the current explicit `mu` state is reducible to `Phi` or joint `Psi/Phi` history, and whether stable Lineum behavior is better described as a continuum-field process, a fundamentally discrete process, or a hybrid. This report freezes questions, model families, interventions, observables, controls, decision rules, and stop conditions before repository-local execution. It does not change the Core equation, whitepapers, or canonical ontology.  
**Central questions:** Is current `mu` an independently informative state, a compact deterministic history coordinate, a higher-scale realization of `Phi`, or a redundant representation? Does the current lattice behave as a numerical sampling of a stable continuum process, or do decisive observables remain tied to cells, timesteps, thresholds, finite precision, or update events?  
**Current confidence:** high for the implementation-level statement that current `mu` is uniquely determined by complete `Psi` history, `kappa`, initial `mu`, and frozen parameters; high that current code is a hybrid of continuous-valued arrays and discrete spatial/time updates; medium that the registered experiments can distinguish useful reduction classes; low that any result can identify the fundamental ontology of nature; no evidential support yet for a literally analog universe, a fundamentally digital universe, quantum branching, consciousness, or a physical identity between `mu` and `Phi`.

## 1. Answer first

The project-owner intuition is scientifically useful but must be split into testable statements.

Lineum may be analog in the sense that its intended carrier is a continuously varying field, while the present computer code is only a grid-based measuring and integration device. A digital audio file does not imply that air pressure changes in bits. In the same way, a square NumPy array does not prove that the represented process is fundamentally cellular.

However, the reverse is also possible. A fundamentally discrete substrate can produce a smooth effective continuum at larger scales. Therefore:

```text
continuum behavior in the simulation does not prove fundamental continuity;
a lattice implementation does not prove fundamental discreteness;
only convergence, symmetry, intervention, and scale tests can classify the implemented model
```

The current `mu` question already admits one exact implementation-level result:

```text
given the complete post-update Psi-energy history,
kappa, initial mu, and frozen parameters,
the complete current mu trajectory is uniquely determined
```

Thus current `mu` cannot contain independent information beyond that complete history. It can still be a causally active Markov state: a compact local variable that saves the model from carrying its entire past explicitly.

This does not prove that `mu` equals `Phi`. Current `Phi` and `mu` use different write, transport, decay, threshold, and feedback rules. The strongest open reduction question is therefore:

```text
Can Phi alone, or a declared coarse-grained history of Phi,
replace explicit mu in closed-loop predictions and interventions?
```

## 2. Programme coordinates and lineage

Target repository and branch:

```text
repository: TomasTriska88/lineum-core
branch: develop
```

Root scientific programme:

```text
path: research/foundations/lineum-continuous-source-cosmology-validation.md
recovered version: 0.4.14
evidence cutoff: 2026-07-29
blob SHA: 3fba3925553cd5596e46c02fa35d1db91523537d
```

Mandatory continuity companion:

```text
path: research/foundations/lineum-root-programme-continuity-and-impact-ledger.md
version: 0.3.0
evidence cutoff: 2026-07-31
blob SHA: 5304874451caf32313ad0e8e3c59e53958698d79
```

Immediate conceptual parent:

```text
path: research/foundations/lineum-mu-branch-relative-identity-and-entanglement-hypothesis.md
version: 0.2.0
evidence cutoff: 2026-07-31
blob SHA: b55bc1639fc8ed6efa7b8286e9113afa88ee298c
```

Immediate mechanism-provenance predecessor:

```text
path: research/foundations/lineum-eq11-epsilon-relic-foam-provenance-comparison.md
version: 0.1.0
blob SHA: 3d814eb1b2ccca4ffc30a88c70c76bca62710c13
```

Active implementation coordinate used for this preregistration:

```text
path: lineum_core/math.py
blob SHA: bb877021810691223a0eb960a45493a2e351112a
```

Report lineage:

```text
lineum-continuous-source-cosmology-validation.md v0.4.14
    |
    +-- lineum-root-programme-cross-branch-priority-review.md
    |
    +-- lineum-core-deterministic-state-transplant-pilot.md
            |
            +-- lineum-core-static-baseline-live-state-transplant-matrix.md
                    |
                    +-- lineum-core-active-growth-scaffold-repair-matrix.md
                            |
                            +-- lineum-core-eq11-growth-scaffold-provenance-gate.md
                                    |
                                    +-- lineum-eq11-epsilon-relic-foam-provenance-comparison.md v0.1.0
                                            |
                                            +-- lineum-mu-branch-relative-identity-and-entanglement-hypothesis.md v0.2.0
                                                    |
                                                    +-- this preregistration v0.1.0
```

The broad and child ClickUp tasks recorded by the continuity ledger were not reread or updated in this checkpoint because the ClickUp MCP connection was inside a returned rate-limit window. Git remains the scientific source of truth. Operational synchronization is pending and must be performed later as one batched update, without polling.

## 3. Evidence layers

### 3.1 What the code currently computes

The active Core stores `Psi` as a complex-valued array and `Phi`, `kappa`, and `mu` as real-valued arrays. Values are represented in floating point, while space is represented by a finite square lattice and evolution occurs through discrete update calls.

### 3.2 What is analytically established here

The current `mu` recurrence is deterministic. Given the exact activity sequence used by the update, `kappa`, initial `mu`, and parameters, `mu` is reconstructible without fitting.

### 3.3 What has been observed numerically

No new numerical run was executed for this report. Previous negative and positive results remain inherited with their original scope. This document records no new trajectory, convergence measurement, regression, or physical correspondence.

### 3.4 Interpretation

Current `mu` can be interpreted as a compact slow reinforcement or memory coordinate. Current `Phi` can be interpreted as a spatially transported environment or medium coordinate. Those labels are operational interpretations, not proof of separate substances.

### 3.5 Hypothesis

A continuum carrier, a discrete carrier, an analog physical substrate, a higher-scale `Phi`, a relational `mu`, and branch structure remain hypotheses. Internal model consistency cannot establish that nature uses the same ontology.

## 4. What “analog” and “digital” mean in this programme

The words are ambiguous and must not be used as one binary switch.

### 4.1 Continuous-valued state

A variable can take values from a continuous mathematical range. Current floating-point arrays approximate this, but finite precision means the implementation contains only finitely many representable numbers.

### 4.2 Continuous space

A field is defined at every point of a spatial domain. Current Core instead stores values at lattice sites.

### 4.3 Continuous time

Evolution is described by differential equations at every time. Current Core advances by finite timesteps.

### 4.4 Analog dynamics

A physical process evolves through the native continuous response of a carrier rather than through symbolic logic gates or explicit bitwise state transitions. This is a claim about the modeled substrate, not about whether the simulator runs on a digital computer.

### 4.5 Fundamentally discrete dynamics

The irreducible ontology contains cells, events, graph relations, finite state transitions, quanta, or a minimum step that cannot be removed by refinement.

### 4.6 Effective digitalization

A continuous process can appear digital because an observer applies thresholds, labels outcomes, counts defects, or stores a finite memory bit. Branch labels may therefore be properties of the observer rather than elementary divisions in the carrier.

## 5. Current implementation audit

### 5.1 Hybrid representation

Current Core is neither a literal continuous PDE implementation nor a binary cellular automaton.

```text
state values: floating-point real and complex numbers
space: finite two-dimensional square lattice
time: discrete update steps
local transport: finite-difference neighborhood operations
random events: Bernoulli linon generation plus Gaussian fluctuation
observer outputs: finite telemetry and later threshold-based analyses
```

### 5.2 Missing explicit spatial scale

The finite-difference diffusion helper returns a neighborhood sum without an explicit `1 / dx^2` factor. `np.gradient` is also called without an explicit spacing argument. Therefore a naive change from one array size to another does not hold a declared physical domain and continuum coefficient fixed.

Consequently:

```text
a raw size sweep is an implementation-sensitivity test;
it is not by itself a valid continuum-limit test
```

A separate nondimensionalized reference lane with explicit `dx` is required before claiming continuum convergence.

### 5.3 Time-step asymmetry in `Phi`

The primary `Psi` updates and mode coupling use `dt`. The `Phi` diffusion contribution uses `dt` only when the experimental flag `phi_diffusion_scales_with_dt` is enabled; its default is `False` for legacy per-update semantics.

Therefore changing `dt` under the default path changes the relative amount of `Phi` diffusion per unit declared model time. A valid continuous-time audit must separate:

```text
legacy update semantics;
explicit-dt Phi diffusion semantics;
and a fully nondimensionalized reference model
```

### 5.4 Current `mu` read path

`mu` enters the current `Psi` update through:

```text
drift_multiplier = 1 + mu
```

This multiplier changes both the local `Phi` interaction term and the `Phi`-gradient flow term. Therefore current `mu` is causally active even when its write path is disabled, provided a nonzero `mu` state is supplied.

### 5.5 Current `mu` write path

With `use_mu = True`, define at step `n`:

```text
E_n(x) = |Psi_n(x)|^2
q_n = r * max_x E_n(x)                  when 0 < r < 1
A_n(x) = max(E_n(x) - q_n, 0)
```

The unclipped update is:

```text
mu_(n+1)(x) = mu_n(x)
              + eta * A_n(x) * kappa(x) * (1 + mu_n(x)) * dt
              - rho * mu_n(x) * dt
```

The result is then clipped to `[0, mu_cap]`.

Default parameters at the implementation coordinate are:

```text
use_mu = False
mu_eta = 0.005
mu_rho = 0.0001
mu_cap = 10.0
mu_peak_cutoff_ratio = 0.1
dt = 1.0
```

### 5.6 Current `Phi` write and transport path

Under mode coupling, `Phi` receives a local contribution proportional to:

```text
mode_coupling_strength * |Psi|^2 * kappa * dt
```

`Phi` also undergoes lattice diffusion and clipping. Unlike `mu`, it has spatial transport and no matching multiplicative `(1 + Phi)` write rule or explicit slow decay term in this path.

Current code-level classification:

```text
mu_is_not_literally_Phi;
mu_and_Phi_are_different_functionals_of_active_history;
mu_is_local_and_non-diffusive_in_this_path;
Phi_is_spatially_diffusive_in_this_path;
mu_has_thresholded_multiplicative_write_and_decay;
Phi_has_mode-coupled_write_and_diffusion
```

## 6. Analytic reducibility result for current `mu`

Ignoring clipping for one step, write:

```text
y_n(x) = 1 + mu_n(x)
B_n(x) = 1 + [eta * A_n(x) * kappa(x) - rho] * dt
```

Then:

```text
y_(n+1)(x) = B_n(x) * y_n(x) + rho * dt
```

Given `y_0`, every later value is uniquely fixed by the sequence `A_n`, which is itself fixed by the exact `Psi` energy history and threshold rule.

Before clipping, the recurrence expands to:

```text
y_n = y_0 * product_(j=0 to n-1) B_j
      + rho * dt * sum_(m=0 to n-1) product_(j=m+1 to n-1) B_j
```

Clipping does not add uncertainty; it applies another deterministic map.

### 6.1 Immediate conclusion

Within the current implementation:

```text
independent_information_in_mu_beyond_complete_Psi_history = absent
```

This is an implementation statement, not an ontological statement about nature.

### 6.2 What remains nontrivial

The recurrence does not make `mu` useless. It can be the minimal state needed to make a history-dependent process locally Markovian. Replacing it may require carrying a long, nonlinear, thresholded `Psi` history.

The harder reductions remain open:

```text
Can mu be reconstructed from Phi history alone?
Can explicit mu be removed while preserving closed-loop futures?
Can a simpler coarse-grained variable preserve interventions?
Does the reconstruction remain stable across scale and discretization changes?
```

### 6.3 Causal intervention warning

Manually assigning two different `mu` arrays to identical instantaneous `Psi/Phi/kappa` states will generally produce different futures because `mu` is read by the `Psi` update. That demonstrates causal activity of the stored state, but not independent natural ontology. The intervention creates states that may be unreachable from the declared natural history.

Both reachable-state and forced-state tests are required and must be reported separately.

## 7. Registered `mu` reduction family

### R0: current explicit `mu`

The implemented baseline: local deterministic memory, thresholded write, multiplicative reinforcement, decay, clipping, and local feedback.

### R1: `Phi` temporal-memory kernel

```text
mu_hat(x,t) = integral K(t-s) * Phi(x,s) ds
```

Discrete candidates include one-, two-, and four-timescale exponential kernels. All coefficients are trained only on the training split and then frozen.

### R2: spatiotemporally coarse-grained `Phi`

```text
mu_hat = C_(ell,tau)[Phi]
```

`C` may smooth over a declared spatial scale `ell` and temporal scale `tau`. Scale parameters must be reported in physical-domain units in the explicit-`dx` lane and in cells only in the legacy lane.

### R3: joint `Psi/Phi` history coordinate

This family includes the exact current recurrence from `Psi` history and simpler finite-history embeddings. It tests whether explicit `mu` is only a compact state-space representation.

### R4: observationally redundant coordinate

The model without explicit `mu` reproduces all declared ordinary and intervention observables within frozen equivalence margins.

### R5: independently identifiable `mu`

A separate state role survives every admissible history reconstruction, matched-capacity control, closed-loop replacement, and intervention test.

Current implementation already rules out one strong version of R5: `mu` is not informationally independent of complete `Psi` history. A broader physical or relational `mu` remains untested.

## 8. Registered continuum/discrete family

### C0: continuous-valued lattice implementation

This is the current code-level description. Continuous-valued arrays evolve through discrete lattice and timestep updates.

### C1: continuum field with numerical lattice regulator

The lattice is only an approximation. With explicit `dx` and `dt`, declared observables approach stable limits as both vanish under a fixed physical domain and fixed nondimensional parameters.

### C2: fundamentally discrete substrate with emergent continuum

Cell or event structure is irreducible, but low-energy or large-scale observables become approximately smooth and symmetric.

### C3: hybrid event-field ontology

Continuous fields coexist with discrete creation, transition, detection, or record events. Current Bernoulli linon generation is a computational example, not validated physical evidence for this ontology.

### C4: observer-induced digitalization

The carrier remains continuous, while branches, particles, outcomes, identities, and memory bits arise from thresholds and finite observers.

### C5: finite-state or quantized carrier

State values themselves occupy an irreducible finite or countable set. Current floating-point arithmetic cannot distinguish this from ordinary numerical finite precision.

No family is selected by this preregistration.

## 9. Experimental lanes

### Lane L0: literal current-Core sensitivity

Purpose: measure how current observables depend on array size, timestep, stencil, precision, thresholds, and orientation under the existing implementation.

This lane answers:

```text
How lattice-dependent is the current code?
```

It does not answer:

```text
Does the model have a continuum limit?
```

### Lane L1: exact `Psi`-history reconstruction of `mu`

Purpose: verify the analytic recurrence against trajectories produced by the active Core.

Primary pass condition:

```text
maximum absolute reconstruction error <= 1e-12
```

for deterministic NumPy float64 trajectories that do not trigger undefined external state changes. A larger discrepancy is treated as an implementation-audit failure, not evidence for independent `mu`.

### Lane L2: `Phi`-only and coarse-grained reduction

Purpose: fit R1 and R2 on training trajectories, freeze them, and test unseen trajectories.

Candidate models:

- one exponential temporal kernel;
- two-timescale exponential kernel;
- four-timescale exponential kernel;
- local finite-lag linear model;
- Gaussian spatial smoothing plus temporal kernel;
- nonlinear but capacity-matched state-space model;
- shuffled-history and time-reversed null controls.

### Lane L3: joint-history compression

Purpose: compare the exact R3 recurrence with simpler compressed summaries of `Psi/Phi` history. Complexity, parameter count, memory length, and prediction error must be reported together.

### Lane L4: closed-loop replacement

Purpose: replace explicit `mu` feedback with frozen `mu_hat` generated from the allowed history and compare future dynamics. Passive curve fitting is not sufficient.

### Lane L5: interventions

Required interventions:

```text
mu freeze;
mu reset;
mu spatial shuffle;
wrong-history transplant;
matched instantaneous Psi/Phi/kappa with different forced mu;
matched mu with different histories;
Phi freeze;
Phi erasure while preserving mu;
mu erasure while preserving Phi;
delayed Phi response control
```

Reachable natural states and manually forced states must be analyzed separately.

### Lane L6: explicit continuum reference

Purpose: build a research-scoped reference update with declared domain length `L`, grid spacing `dx = L/N`, timestep `dt`, and spatial operators scaled by `1/dx` and `1/dx^2` where mathematically required.

This lane must remain outside the public `lineum_core/` package until validated and separately promoted.

### Lane L7: discrete and hybrid controls

Purpose: compare the continuum reference with:

- deliberately quantized state amplitudes;
- fixed finite-state updates;
- event-driven linon creation with continuous fields;
- randomized graph or lattice controls;
- threshold-only branch/particle observers;
- matched smooth continuum nulls.

## 10. Frozen initialization families

The first execution must include at least these distinct families:

1. smooth Gaussian amplitude with uniform phase;
2. smooth Gaussian amplitude with one phase winding;
3. two separated smooth packets;
4. band-limited random smooth field;
5. exact vacuum control;
6. translated and rotated copies of the same state;
7. uniform `kappa = 1`;
8. smooth structured `kappa` with the same mean;
9. zero `Phi` and zero `mu`;
10. controlled nonzero `Phi` and zero `mu`;
11. controlled nonzero `mu` and zero `Phi` as a forced-state control.

Primary reduction experiments disable quantum noise to isolate determinism. A secondary robustness lane re-enables stochastic terms with frozen seeds.

## 11. Resolution and timestep matrix

### 11.1 Legacy sensitivity matrix

At minimum:

```text
N in {64, 96, 128, 192}
dt in {1.0, 0.5, 0.25}
stencil in {LAP4, LAP8}
phi_diffusion_scales_with_dt in {False, True}
precision in {float64 reference, float32 diagnostic where supported}
```

Results from this matrix are labeled implementation sensitivity only.

### 11.2 Continuum-reference matrix

Use a fixed physical domain and matched nondimensional initial conditions:

```text
N in {64, 128, 256}
dx = L / N
dt chosen by a declared stability rule
```

A result is eligible for continuum classification only when coefficients and initial conditions are transformed consistently with `dx` and `dt`.

## 12. Observables

Primary continuous observables:

- mean and total `|Psi|^2` with the measure convention stated;
- maximum `|Psi|`;
- radial and angular spectra;
- `Phi` mean, variance, gradients, and spatial correlation length;
- `mu` mean, variance, support fraction, and correlation length;
- normalized reconstruction error;
- long-horizon observable divergence;
- norm, source, and transfer residuals where defined.

Structural observables:

- winding count and signed winding;
- localization metrics against shifted, shuffled, and phase-randomized nulls;
- orientation anisotropy;
- translation and rotation covariance;
- persistence and recombination accessibility;
- threshold stability bands.

Observer-dependent outputs must never be mixed with raw field convergence without labeling the observer.

## 13. Error and equivalence metrics

For a field `z` and prediction `z_hat`, define a robust normalized error:

```text
E_z = RMSE(z_hat - z) / [P95(z) - P05(z) + epsilon]
```

For each scalar observable `O`, define:

```text
E_O = RMSE(O_hat - O) / [P95(O) - P05(O) + epsilon]
```

Intervention effect agreement uses:

```text
relative_effect_error = |Delta_hat - Delta| / (|Delta| + epsilon)
```

All percentiles and normalizations are fitted on the training data and frozen.

## 14. Preregistered reduction decisions

### 14.1 Exact-history result

R3 exact reconstruction is supported for the current implementation if the active-Core trajectory and standalone recurrence agree within `1e-12` in deterministic float64 execution.

### 14.2 `Phi`-only effective reduction

R1 or R2 is supported within the tested domain only if all of the following hold on unseen trajectories:

```text
median E_mu <= 0.05;
90th percentile E_mu <= 0.10;
all primary continuous-observable E_O <= 0.10;
no intervention effect changes sign;
median relative intervention-effect error <= 0.10;
performance survives translation, rotation, resolution, and history-family splits;
matched-capacity shuffled and time-reversed controls fail materially
```

These thresholds are operational research thresholds, not universal physical constants.

### 14.3 Redundant explicit coordinate

R4 is supported only if closed-loop removal of explicit `mu` passes the same ordinary and intervention criteria and reduces state or model complexity without hiding extra history in an unconstrained predictor.

### 14.4 Independent state

Current `mu` is classified as independently causally useful but not independently informational if forced interventions matter while exact `Psi`-history reconstruction remains valid.

A stronger independent-state claim requires a natural, reachable discriminator not reproduced by admissible `Psi/Phi` histories. Forced unreachable states alone are insufficient.

### 14.5 Nonidentifiability

If several models remain equivalent over all declared observables and interventions, the verdict is:

```text
unresolved_due_to_nonidentifiability
```

Ontology must not be chosen by narrative preference.

## 15. Preregistered continuum/discrete decisions

### 15.1 Model-level continuum support

C1 gains support within the tested model if:

- primary observables converge as `dx` and `dt` decrease;
- an estimated positive convergence order is stable across at least three resolutions;
- rotation and translation anisotropy decreases with refinement;
- event and defect classifications survive preregistered threshold bands;
- improved spatial operators reduce the predicted cutoff errors;
- no lattice-locked qualitative transition survives after physical rescaling.

This supports a continuum description of the model, not fundamental continuity of nature.

### 15.2 Discrete or hybrid support

C2, C3, or C5 gains model-level support only if an irreducible discrete signature survives valid continuum controls, such as:

- a stable minimum length or event scale that cannot be removed by refinement;
- persistent orientation or dispersion structure with a declared physical scale;
- quantized observables not created by clipping, thresholds, finite precision, or counting rules;
- superior out-of-sample predictions from an explicitly discrete model at matched complexity.

A numerical artifact is not evidence for physical discreteness.

### 15.3 Observer digitalization

C4 gains support if raw fields converge smoothly while branch, particle, or outcome counts change primarily with observer thresholds and coarse-graining. This would classify digital labels as effective observer outputs.

### 15.4 Fundamental ontology remains open

Neither numerical continuum convergence nor persistent discrete code behavior can by itself prove the ontology of the observable universe.

## 16. Independent checks

No decision-relevant result is accepted from one path.

Required checks include:

1. analytic recurrence against iterative recurrence;
2. a zero-activity decay toy case;
3. a constant-activity closed-form toy case;
4. NumPy and independently written reference implementations;
5. timestep and resolution convergence;
6. translated and rotated initial states;
7. shuffled-history and time-reversed controls;
8. model-capacity matching;
9. bootstrap uncertainty over seeds or initial-condition families;
10. active-Core comparison receipt with exact source SHA.

## 17. Portable reference code for the current `mu` recurrence

The following code is a standalone analytic verifier. It does not import Lineum and does not reproduce the full Core. It freezes only the current `mu` update audited at the implementation SHA above.

```python
import numpy as np


def dynamic_floor(energy: np.ndarray, ratio: float) -> float:
    floor = float(ratio)
    if 0.0 < floor < 1.0:
        floor *= float(np.max(energy))
    return floor


def mu_step(
    mu: np.ndarray,
    energy: np.ndarray,
    kappa: np.ndarray,
    *,
    dt: float = 1.0,
    eta: float = 0.005,
    rho: float = 0.0001,
    cap: float = 10.0,
    peak_cutoff_ratio: float = 0.1,
) -> np.ndarray:
    mu = np.asarray(mu, dtype=np.float64)
    energy = np.asarray(energy, dtype=np.float64)
    kappa = np.asarray(kappa, dtype=np.float64)
    floor = dynamic_floor(energy, peak_cutoff_ratio)
    active = np.maximum(energy - floor, 0.0)
    out = (
        mu
        + eta * active * kappa * (1.0 + mu) * dt
        - rho * mu * dt
    )
    return np.clip(out, 0.0, cap)


def reconstruct_mu(
    energy_history: np.ndarray,
    kappa: np.ndarray,
    mu0: np.ndarray,
    **kwargs,
) -> np.ndarray:
    states = [np.asarray(mu0, dtype=np.float64).copy()]
    mu = states[0]
    for energy in np.asarray(energy_history, dtype=np.float64):
        mu = mu_step(mu, energy, kappa, **kwargs)
        states.append(mu.copy())
    return np.stack(states)


def constant_activity_closed_form(
    mu0: float,
    active_energy: float,
    kappa: float,
    steps: int,
    *,
    dt: float = 1.0,
    eta: float = 0.005,
    rho: float = 0.0001,
) -> float:
    factor = 1.0 + (eta * active_energy * kappa - rho) * dt
    y0 = 1.0 + mu0
    if abs(factor - 1.0) < 1e-15:
        y = y0 + steps * rho * dt
    else:
        y = (
            factor**steps * y0
            + rho * dt * (factor**steps - 1.0) / (factor - 1.0)
        )
    return y - 1.0


def self_test() -> None:
    # Zero activity: mu decays deterministically.
    mu = np.array([0.5])
    for _ in range(10):
        mu = mu_step(
            mu,
            energy=np.array([0.0]),
            kappa=np.array([1.0]),
            peak_cutoff_ratio=0.0,
            cap=1e9,
        )
    expected_decay = 0.5 * (1.0 - 0.0001) ** 10
    np.testing.assert_allclose(mu[0], expected_decay, rtol=0.0, atol=1e-14)

    # Constant active energy: iteration matches the closed form before clipping.
    mu = np.array([0.2])
    for _ in range(10):
        mu = mu_step(
            mu,
            energy=np.array([0.3]),
            kappa=np.array([0.7]),
            peak_cutoff_ratio=0.0,
            cap=1e9,
        )
    expected = constant_activity_closed_form(0.2, 0.3, 0.7, 10)
    np.testing.assert_allclose(mu[0], expected, rtol=0.0, atol=1e-14)


if __name__ == "__main__":
    self_test()
```

The self-test code was independently sanity-checked during report preparation, but no active-Core trajectory was executed in this connector-only checkpoint.

## 18. External physical constraints

These sources constrain methodology and interpretation; they do not validate Lineum.

- K. Symanzik, “Continuum Limit and Improved Action in Lattice Theories. I. Principles and phi4 Theory,” *Nuclear Physics B* 226, 187-204 (1983), DOI: `10.1016/0550-3213(83)90468-6`. Finite lattice-spacing effects must be identified and systematically reduced before continuum claims.
- Nico Klein, Dean Lee, and Ulf-G. Meißner, “Lattice Improvement in Lattice Effective Field Theory,” arXiv: `1807.04234` (2018). The work explicitly benchmarks how lattice errors scale after improvement.
- V. Vasileiou et al., “Constraints on Lorentz Invariance Violation from Fermi-Large Area Telescope Observations of Gamma-Ray Bursts,” *Physical Review D* 87, 122001 (2013), DOI: `10.1103/PhysRevD.87.122001`. The reported absence of energy-dependent vacuum dispersion places strong bounds on some Lorentz-violating high-energy models.
- Ivan Kharuk and Sergey Sibiryakov, “Emergent Lorentz Invariance with Chiral Fermions,” arXiv: `1505.04130` (2015). A microscopic theory without Lorentz symmetry can in principle approach approximate Lorentz symmetry at low energy, so low-energy symmetry alone does not establish a continuous microscopic substrate.

Known real physics therefore does not currently justify the statement that the universe is fundamentally analog or fundamentally digital. Naive fixed lattices with preferred directions face strong symmetry and dispersion constraints, but discrete models with emergent symmetry are not excluded merely by being discrete.

## 19. Root-programme impact matrix

| Root branch | Relationship | Required handling |
|---|---|---|
| source accounting | `constrains` | `mu` reconstruction must not hide a source, norm pump, or undeclared reservoir |
| P1 pump/randomness | `depends_on` | deterministic primary lane separates memory from random innovations; stochastic lane remains secondary |
| P2 centered-only remnant | `reopens` | continuum and observer audits may change whether the remnant is classified as physical structure or lattice population |
| observer audit | `depends_on` | branch, particle, and digital labels require threshold-stability analysis |
| ST1B seam | `constrains` | numerical domain decomposition is not evidence of physically discrete universes |
| ST1C membrane | `unaffected` initially | current passive-boundary failure is not repaired by renaming the substrate analog |
| deterministic transplant | `supports` method | exact state replay supplies a control for history-coordinate reconstruction |
| static recipe/live state | `supports` distinction | broad resemblance must remain separate from exact dynamic state |
| copying and heredity | `unaffected` | history compression is not copying, identity, or heredity |
| `mu x kappa` repair | `reopens` interpretation | weak local repair does not decide whether `mu` is a history coordinate or separate medium |
| Eq-11.1 | `not_yet_compared` numerically | growth-law provenance remains separate from continuum ontology |
| epsilon cycle | `not_yet_compared` | a finite reservoir cannot be inferred from analog continuity |
| Relic Foam | `reopens` | persistent environment scars require scale and lattice-artifact checks |
| Quantum Foam | `constrains` | primordial discreteness and branch fractality remain separate hypotheses |
| quantum interpretation programme | `depends_on` | branch structure cannot be assessed before observer and continuum stability are known |
| physical correspondence | `blocked` | model-level convergence is necessary but insufficient for nature claims |

## 20. Stop conditions

Stop and record a failure before interpretation if:

- active-Core `mu` reconstruction disagrees with the audited recurrence beyond numerical tolerance;
- changing `dt` or `N` is interpreted without preserving the declared physical scaling;
- a predictor uses future data, hidden explicit `mu`, or target leakage;
- a more complex model is credited without matched-capacity controls;
- branch or particle counts change materially under reasonable threshold bands;
- clipping or fail-safe resets dominate a retained lane;
- continuum extrapolation uses fewer than three valid resolutions;
- stochastic comparisons do not reuse frozen seeds or equivalent realized inputs;
- ClickUp unavailability is used to infer task priority from repository `todo.md`;
- a model-level result is promoted to a claim about nature.

## 21. Current verdict

```text
current_Core_representation = continuous_valued_discrete_lattice_hybrid
current_mu_literal_identity_with_Phi = false_in_code
current_mu_independent_of_complete_Psi_history = false_in_code
current_mu_as_compact_history_state = analytically_supported
current_mu_reducibility_to_Phi_only = open
current_mu_closed_loop_redundancy = open
continuum_limit_of_current_legacy_update = not_demonstrated
analog_fundamental_ontology = open_hypothesis
discrete_fundamental_ontology = open_hypothesis
observer_induced_digitalization = open_hypothesis
physical_correspondence = unvalidated
```

## 22. Immediate next execution

The cheapest decisive repository-local step is:

```text
record deterministic active-Core trajectories with use_mu enabled;
store the exact post-kinematic energy sequence used by the mu update;
reconstruct mu with the standalone recurrence;
require agreement within 1e-12;
then test frozen Phi-only kernels on held-out trajectories;
only after passive success attempt closed-loop replacement and interventions
```

The continuum lane begins in parallel only with a written nondimensionalization and explicit `dx/dt` reference update. A raw array-size sweep must not be presented as a continuum result.

## 23. Prohibited interpretations

This preregistration does not establish that:

- Lineum is fundamentally analog;
- the observable universe is analog;
- spacetime is continuous;
- spacetime is discrete;
- floating-point values are physical continua;
- the square lattice is a physical lattice;
- linons are physical digital events;
- `mu` equals `Phi`;
- `mu` is a soul, consciousness, identity, or branch substrate;
- continuum convergence would prove reality is continuous;
- lattice dependence would prove reality is discrete;
- a branch count is meaningful before the observer is stable;
- Lineum reproduces quantum mechanics, relativity, particles, or nature.

## 24. Limitations

- No active-Core simulation, test suite, build, or local import was executed in this checkpoint.
- The exact `mu` reducibility statement follows from the audited update structure and must still receive an active-Core comparison receipt.
- The report does not yet contain the full executable continuum reference because its nondimensionalization must be frozen before code is written.
- The legacy Core update contains no explicit `dx`, so its raw resolution sweep cannot answer the continuum question.
- The external references constrain methodology and selected observable consequences, not the total space of analog or discrete theories.
- ClickUp task state was not synchronized because the MCP quota remained unavailable.
- An accidentally created empty helper branch named `codex/tmp` exists at the same starting point as `develop`; it contains no report change and was not used. The available connector exposed no safe branch-deletion action in this checkpoint. It must be removed later through an authenticated Git or GitHub interface.

## 25. Continuous ledger

- `2026-07-31 owner analogy`: preserved the description that the owner supplies scrap and components while the research process attempts to assemble and test a motor.
- `2026-07-31 analog intuition`: registered the hypothesis that Lineum’s simplest basis may be analog rather than digital.
- `terminology correction`: separated continuous values, continuous space, continuous time, analog dynamics, fundamental discreteness, and observer-induced digitalization.
- `implementation audit`: classified current Core as a continuous-valued, finite-precision, discrete-lattice, discrete-timestep hybrid.
- `scale warning`: recorded that current spatial operators omit explicit `dx`, so a raw size sweep is not a continuum-limit test.
- `time warning`: recorded the legacy default in which `Phi` diffusion does not scale with `dt`.
- `analytic result`: established that current `mu` is a deterministic functional of complete `Psi` energy history, `kappa`, initial `mu`, and frozen parameters.
- `ontology correction`: separated deterministic history reducibility from causal usefulness and from literal identity with `Phi`.
- `reduction programme`: froze R0-R5, passive reconstruction, closed-loop replacement, and reachable versus forced interventions.
- `continuum programme`: froze C0-C5, legacy sensitivity, explicit-`dx` continuum reference, discrete controls, and observer-threshold audits.
- `promotion boundary`: prohibited whitepaper or Core-equation changes from this preregistration alone.
