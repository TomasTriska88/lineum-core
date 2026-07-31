# Mu-Phi History Reconstruction L2 Audit and Completion-Residual Registry

**Status:** active implementation audit result; frozen transcribed-reference L2 passed inside its declared invertible domain; universal `Phi`-only sufficiency was falsified by two exact counterexamples; direct active-package and repository-supported NumPy receipts remain pending  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-07-31  
**Scope:** Core-only audit of whether consecutive `Phi` states contain enough information to reconstruct the current local `mu` trajectory and replace stored `mu` in closed-loop deterministic evolution. The report derives an exact inverse for the uniform-`kappa`, mode-coupled, unsaturated periodic lane; executes a frozen 32-run matrix; supplies an independent dense-matrix inversion; records negative controls and two non-identifiability counterexamples; and registers finite dyadic memory and completion-residual hypotheses for the next experiment. It does not modify the Core equation, validate a continuum ontology, identify dark matter, establish other universes, or treat an Egyptian mathematical analogy as physical evidence.  
**Central questions:** When is the current `mu` exactly recoverable from `Phi` history alone? Does a reconstructed `mu` preserve the future `Psi/Phi` trajectory in closed loop? Which implementation operations make the `Phi` observer non-identifying? How should a finite multiscale memory and its unresolved residual be tested without naming that residual in advance?  
**Current confidence:** high for the frozen-reference algebra and numerical result in the declared uniform, unsaturated, invertible lane; high that `Phi` history is not universally sufficient in the current model because clipping and a `kappa`-masked global threshold admit exact counterexamples; medium for active-package equivalence because the package was not imported from a clean checkout; medium-low for repository-supported-environment equivalence because this run used NumPy 2.3.5 while the repository declares NumPy below 2.0; no evidential support for a literal identity `mu = Phi`, quantum noise as the missing residual, cross-universe coupling, dark matter, ancient knowledge of Lineum, or physical correspondence with nature.

## 1. Answer first

Inside one regular part of the current model, `mu` can be removed as a stored variable and reconstructed from consecutive `Phi` snapshots without changing the simulated future beyond floating-point roundoff.

The simplest picture is a camera followed by reversible image smoothing. If the smoothing rule is known, no pixel is saturated, every observed cell is open, and the smoothing operator has no zero mode, the previous and next images contain enough information to recover what was deposited between them. In this lane, the deposited quantity is the write-time `Psi` energy. Once that energy is recovered, the corrected `mu` recurrence from L1 reproduces the stored memory.

The closed-loop matrix produced:

```text
runs: 32
grid: 32 x 32
steps per run: 80
cell-step updates: 2,621,440

maximum Psi difference: 2.2887833992611187e-16
maximum Phi difference: 3.469446951953614e-18
maximum mu difference: 6.106226635438361e-16
maximum recovered write-energy difference: 1.6930901125533637e-14
Phi clipping events in the matrix: 0
minimum diffusion symbol: 0.98
```

This is a successful closed-loop reduction **within that domain**.

It is not a universal field identity. Two exact counterexamples produced identical observable `Phi` and different `mu`:

1. `Phi` saturation mapped write energies `1000` and `2000` to the same clipped value `0.5`, while `mu` differed by `4.49955`.
2. A high-energy cell hidden behind `kappa = 0` changed the global `mu` activity threshold from `0.5` to `10.0`. Observable `Phi` remained exactly identical, while visible-cell `mu` differed by `0.02249775`.

Therefore the local verdict is:

```text
Phi-history sufficiency in the declared invertible lane = supported
universal Phi-history sufficiency in the current model = falsified
current mu as useful stored history coordinate = supported
literal physical identity mu = Phi = not established
```

## 2. Programme coordinates and lineage

Target:

```text
repository: TomasTriska88/lineum-core
branch: develop
```

Root scientific programme:

```text
path: research/foundations/lineum-continuous-source-cosmology-validation.md
version: 0.4.14
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

Conceptual parent:

```text
path: research/foundations/lineum-mu-branch-relative-identity-and-entanglement-hypothesis.md
version: 0.2.0
evidence cutoff: 2026-07-31
blob SHA: b55bc1639fc8ed6efa7b8286e9113afa88ee298c
```

Preregistered parent:

```text
path: research/foundations/lineum-mu-phi-reduction-and-continuum-preregistration.md
version: 0.1.0
evidence cutoff: 2026-07-31
blob SHA: 16fac63f7659427ee18865fce82fbad0868311bd
```

Immediate numerical predecessor:

```text
path: research/foundations/lineum-mu-psi-history-reconstruction-l1-audit.md
version: 0.1.0
evidence cutoff: 2026-07-31
blob SHA: 7ba9f83cd839a6cd383bf591b9c0b8a59fe4a6f6
```

Active implementation coordinate transcribed:

```text
path: lineum_core/math.py
blob SHA: bb877021810691223a0eb960a45493a2e351112a
path: deterministic NumPy update
mode coupling: enabled
quantum noise and linon generation: disabled
```

Lineage:

```text
lineum-continuous-source-cosmology-validation.md v0.4.14
    |
    +-- lineum-root-programme-continuity-and-impact-ledger.md v0.3.0
    |
    +-- lineum-eq11-epsilon-relic-foam-provenance-comparison.md v0.1.0
            |
            +-- lineum-mu-branch-relative-identity-and-entanglement-hypothesis.md v0.2.0
                    |
                    +-- lineum-mu-phi-reduction-and-continuum-preregistration.md v0.1.0
                            |
                            +-- lineum-mu-psi-history-reconstruction-l1-audit.md v0.1.0
                                    |
                                    +-- this L2 audit v0.1.0
```

ClickUp was not called. The previously returned MCP rate-limit window was not polled. Operational synchronization remains pending as one future batched update; Git is the scientific source of truth.

## 3. Evidence layers

### 3.1 What the implementation computes

The current deterministic NumPy lane:

1. evolves `Psi` using the current `Phi`, `kappa`, and stored `mu`;
2. measures write-time energy `E_n = |Psi|^2`;
3. writes `alpha E_n kappa` into `Phi`;
4. removes the mode-coupled amount from `Psi`;
5. diffuses and clips `Phi`;
6. writes, decays, and clips `mu` using the same pre-mode-coupling energy `E_n`.

No cross-universe field, branch index, dark-matter observable, completion field, or dyadic memory bank is implemented.

### 3.2 What was reproducibly observed

The embedded frozen reference executed the 32-run matrix, an independent dense linear solve, one deliberately wrong inverse, and two exact non-identifiability constructions. Numerical values are reported in Sections 7-10 and in the machine-readable receipt.

### 3.3 Cautious interpretation

In the regular lane, explicit `mu` is a convenient Markov memory coordinate: retaining it avoids replaying and inverting the entire `Phi` history. Exact reconstruction does not make the coordinate computationally useless.

The counterexamples show that the selected `Phi` observer can lose distinctions that remain causally relevant to `mu`. That is observer non-identifiability, not evidence that the missing information is automatically quantum, metaphysical, or external to the modeled domain.

### 3.4 Hypotheses

Finite multiscale memory, unresolved subresolution structure, projection loss, boundary input, relational state, stochastic innovation, and cross-layer input remain competing hypotheses. None is selected by this audit.

### 3.5 Observable-universe boundary

No astronomical or laboratory data were analyzed. The audit does not show that nature contains `Psi`, `Phi`, `mu`, a continuum, other universes, or the same threshold law. It supplies no dark-matter fit, gravitational lensing prediction, cosmic-microwave-background calculation, structure-growth calculation, or collision-of-clusters test.

## 4. Exact regular-lane derivation

Let:

```text
P_n       = stored Phi before step n
E_n       = write-time |Psi|^2 used by both mode coupling and mu
kappa     = 1 everywhere in the exact inversion lane
alpha     = mode_coupling_strength * dt
U_(n+1)   = Phi after local mode-coupling write and before Phi diffusion
P_(n+1)   = stored Phi after diffusion and clipping
```

Before diffusion:

```text
U_(n+1) = P_n + alpha E_n
```

For the uniform periodic lane, the stored unclipped field is:

```text
P_(n+1) = D U_(n+1)
D = I + beta L
beta = phi_diffusion * 0.05 * s
s = dt when phi_diffusion_scales_with_dt is true, otherwise 1
```

`L` is the periodic lattice stencil.

For Fourier modes `(kx, ky)`, the LAP4 symbol is:

```text
lambda_4 = 2 cos(kx) + 2 cos(ky) - 4
```

The LAP8 symbol used by the implementation is:

```text
lambda_8 =
    2 cos(kx)
  + 2 cos(ky)
  + cos(kx) cos(ky)
  - 5
```

Thus:

```text
D_hat = 1 + beta lambda
```

In the frozen matrix, the minimum value of `D_hat` was `0.98`, so the operator had no zero Fourier mode and was well conditioned.

When clipping is inactive:

```text
U_(n+1) = inverse(D) P_(n+1)
E_n = [inverse(D) P_(n+1) - P_n] / alpha
```

The corrected L1 recurrence then gives:

```text
q_n = mu_peak_cutoff_ratio * max(E_n)
A_n = max(E_n - q_n, 0)
g_n = mu_eta * A_n * kappa * dt
d   = 1 - mu_rho * dt

mu_tmp   = mu_n + g_n * (1 + mu_n)
mu_(n+1) = clip(d * mu_tmp, 0, mu_cap)
```

This is an exact algebraic reduction under the declared assumptions. No fitted kernel is used.

## 5. Conditions required by the exact inverse

The L2 result requires all of the following:

```text
mode coupling is enabled;
the write coefficient and dt are known;
the observed Phi frames are consecutive;
kappa is uniformly one in the exact Fourier lane;
the Phi stencil and timestep convention are known;
the one-step Phi diffusion operator has no zero mode;
Phi clipping did not alter the frame;
the same floating-point update semantics are used;
the current global mu threshold rule is known.
```

Failure of one condition can make the inverse wrong, unstable, or non-identifying.

The exact Fourier derivation is not claimed for general nonuniform `kappa`. A nonuniform positive `kappa` may admit a numerical inverse of its full operator, but this requires a separate conditioning and null-space audit. Cells with `kappa = 0` cannot be recovered by division through the local write channel.

## 6. Frozen matrix

Every run used:

```text
grid: 32 x 32 periodic lattice
steps: 80
initial Phi: zero
initial mu: zero
kappa: uniform one
mode coupling: enabled
mode_coupling_strength: 0.001
quantum noise and linon generation: disabled
mu_eta: 0.005
mu_rho: 0.0001
mu_cap: 10
mu_peak_cutoff_ratio: 0.1
phi_cap: 1,000,000
```

Factorial axes:

```text
initialization:
- centered Gaussian packet
- phase-winding Gaussian packet
- two separated packets
- seeded band-limited smooth random field

dt:
- 1.0
- 0.5

stencil:
- LAP4
- LAP8

Phi diffusion timestep semantics:
- legacy per-update
- dt-scaled
```

Total:

```text
4 * 2 * 2 * 2 = 32 runs
32 * 80 * 32 * 32 = 2,621,440 cell-step updates
```

At each step, two lanes were advanced:

```text
explicit lane:
    reads and updates stored mu

reconstruction lane:
    reads the previously reconstructed mu
    does not use the implementation's new mu write
    recovers E_n only from P_n and P_(n+1)
    applies the independently coded corrected mu recurrence
    uses that reconstructed mu on the next closed-loop step
```

This is stronger than passive fitting because reconstruction errors can feed back into later `Psi` and `Phi`.

## 7. Closed-loop result

Pass threshold:

```text
maximum declared state difference <= 1e-12
```

Observed maxima:

```text
Psi: 2.2887833992611187e-16
Phi: 3.469446951953614e-18
mu: 6.106226635438361e-16
write-time energy reconstruction: 1.6930901125533637e-14
```

The energy recovery error is larger than the state errors because it divides a tiny `Phi` inversion residual by the mode-coupling coefficient `0.001`. It remained far below the frozen state-equivalence threshold after propagation through the `mu` update.

Additional receipts:

```text
Phi cap events: 0
minimum raw Phi: 1.1911251868988922e-25
maximum raw Phi: 0.033402817725922504
minimum recovered energy: -1.4273318396147656e-15
maximum recovered energy: 0.9737514270379475
minimum diffusion symbol: 0.98
```

The tiny negative recovered energy is a floating-point inversion residual, not a negative physical-energy claim. It was not post-hoc clipped in the reconstruction, so the audit exposes rather than hides the numerical residue.

Local classification:

```text
L2_regular_lane_closed_loop = passed
stored_mu_needed_for_exact_future_in_this_lane = no
complete_consecutive_Phi_history_needed_by_this_reconstruction = yes
finite_memory_replacement = untested
```

## 8. Independent inversion check

A second implementation constructed the complete diffusion matrix on a `6 x 6` lattice and used `numpy.linalg.solve`. It did not use the Fourier inverse to obtain its solution.

Across LAP4, LAP8, both timesteps, and both diffusion-time conventions:

```text
maximum dense-solve preimage error:
1.1102230246251565e-16

maximum Fourier preimage error:
1.6653345369377348e-16

maximum dense-versus-Fourier difference:
1.942890293094024e-16

maximum matrix condition number:
1.0204081632653066
```

This confirms both the algebraic symbol and the good conditioning of the frozen regular lane.

## 9. Negative control: wrong diffusion semantics

For every `dt = 0.5` configuration, reconstruction intentionally used the opposite `phi_diffusion_scales_with_dt` convention.

Observed ranges:

```text
maximum mu error:
0.0015241827422114232 to 0.0035763982963578633

maximum recovered write-energy error:
0.013587865480030298 to 0.026196313253229353
```

The inverse therefore depends on the exact implementation convention. The positive result is not a generic curve-fitting procedure that succeeds under an incorrect model.

## 10. Exact non-identifiability counterexamples

### 10.1 C1: `Phi` saturation

Frozen toy parameters:

```text
grid: 4 x 4
kappa: one
initial Phi: zero
initial mu: zero
phi_cap: 0.5
write energy A: uniform 1000
write energy B: uniform 2000
```

Uniform fields have zero diffusion contribution. Both writes therefore clip to:

```text
Phi_A = Phi_B = 0.5
```

But:

```text
mu_A = 4.49955
mu_B = 8.9991
difference = 4.49955
```

Verdict:

```text
same consecutive observable Phi;
different current mu;
Phi-only identification fails after saturation
```

This loss is caused by explicit `np.clip`, not ordinary `float64` representation.

### 10.2 C2: hidden `kappa = 0` energy changes the global threshold

Frozen toy parameters:

```text
grid: 4 x 4
initial Phi: zero
initial mu: zero
visible cells: kappa = 1 and write energy = 5
one hidden cell: kappa = 0
case A hidden energy: 5
case B hidden energy: 100
mu_peak_cutoff_ratio: 0.1
```

Because the hidden cell has `kappa = 0`, it writes nothing into `Phi` in either case. The complete observable `Phi` arrays are exactly equal:

```text
maximum Phi difference = 0.0
```

However, the `mu` threshold is based on the global maximum energy before multiplication by `kappa`:

```text
case A global floor = 0.5
case B global floor = 10.0
```

Visible-cell result:

```text
case A maximum visible mu = 0.02249775
case B maximum visible mu = 0.0
difference = 0.02249775
```

Verdict:

```text
same observable Phi;
different visible mu;
a kappa-masked variable can influence the global mu write
without appearing in the local Phi write
```

This is an implementation-level nonlocal threshold effect. It is not quantum nonlocality, entanglement, another universe, or dark matter.

## 11. Floating-point rounding versus information destruction

`float64` rounds arithmetic to finite precision. The closed-loop differences near `10^-16` are consistent with changing the order of mathematically equivalent floating-point operations.

That is distinct from explicit many-to-one maps:

```text
Phi clipping:
    many values above phi_cap -> one stored value

kappa masking:
    local source multiplied by zero -> no local Phi record

projection:
    Phi stores a declared function of the larger state, not every state component

global threshold:
    a hidden maximum can alter visible mu activity
```

The current regular result shows no meaningful loss from ordinary `float64` rounding over the frozen horizon. It does not establish long-horizon numerical stability, arbitrary precision equivalence, or continuum convergence.

## 12. Reduction verdict

The strongest permitted statement is:

> In the deterministic frozen NumPy reference transcribed from the stated source blob, with uniform `kappa = 1`, mode coupling enabled, known invertible `Phi` diffusion, consecutive unsaturated `Phi` frames, and the frozen parameter matrix, the explicit current `mu` can be reconstructed from `Phi` history and replaced in closed loop without a material change in `Psi`, `Phi`, or `mu`.

The strongest prohibited statements include:

- `mu` is literally the same array or physical substance as `Phi`;
- `mu` is redundant in every current-Core state;
- any finite summary of `Phi` is already sufficient;
- the residual is quantum noise;
- the residual comes from other universes;
- `mu` explains dark matter;
- Lineum has established an analog or continuous ontology;
- the Eye-of-Horus or Rhind-papyrus fractions encode Lineum physics.

Machine classification:

```text
L2_transcribed_reference_regular_domain = passed
active_package_import_match = pending
repository_supported_numpy_receipt = pending
Phi_only_universal_identifiability = falsified
mu_as_exact_regular_lane_Phi_history_coordinate = supported
mu_as_practical_finite_memory = untested
mu_equals_Phi_ontology = not_established
```

## 13. Completion-residual registry H0-H6

Define an observer or finite memory model `F_J` and residual:

```text
mu_hat_J(t) = F_J[Phi history up to t]
r_J(t) = mu(t) - mu_hat_J(t)
```

The residual is a measurement of what the selected observer failed to reconstruct. Its name must not prejudge its cause.

### H0: no residual under the declared observer

```text
r_J = 0 within frozen tolerance
```

Full consecutive unsaturated `Phi` history supports H0 in the exact regular lane. H0 has not been shown for a finite-memory observer or the general current model.

### H1: numerical or subresolution residual

The residual arises from finite precision, timestep, lattice resolution, unresolved fast modes, ill-conditioning, or a non-converged discretization.

Required discriminator: precision, `dt`, explicit-`dx`, conditioning, and resolution refinement.

### H2: projection residual

`Phi` omits information retained in `Psi`, phase, a global statistic, clipping history, or another implemented state component.

The two exact counterexamples provide positive implementation-level examples of projection/non-injectivity. They do not identify a new physical field.

### H3: boundary residual

The observed domain is incomplete, so input or state outside its boundary affects the interior.

Required discriminator: nested domains, flux accounting, absorbing versus periodic boundaries, and measured boundary interventions.

### H4: relational residual

The relevant information belongs to correlations or relations among locations, objects, histories, or domains rather than one local scalar field.

Required discriminator: matched local marginals with altered joint relations and a registered relational observable.

### H5: stochastic innovation

A new random input is conditionally unpredictable from prior `Phi` history.

Required discriminator: frozen-seed conditional replay, innovation whiteness, timestep scaling, and comparison with deterministic hidden-state alternatives. The word “quantum” is prohibited until specifically quantum observables and constraints are reproduced.

### H6: cross-layer or other-domain input

A speculative family may be written:

```text
r_a = sum over b != a of C_ab Phi_b
```

where `a` labels the observed domain and `b` hypothetical other domains.

This variant is registered because it was proposed by the project owner, including the possible analogy that an unseen cross-domain contribution could resemble `mu` or an apparent gravitational source. Current Core has no `b`, no `C_ab`, and no corresponding observable. H6 remains `untested_speculative` and must compete with H1-H5 and a no-extra-layer null.

A dark-matter interpretation would additionally have to reproduce gravitational lensing, galaxy and cluster dynamics, cosmic-microwave-background constraints, structure growth, and colliding-cluster observations. None was tested here.

## 14. Dyadic finite-memory hypothesis

The project owner proposed the mathematical sequence:

```text
1/2 + 1/4 + 1/8 + 1/16 + 1/32 + 1/64 = 63/64
```

as a metaphor for a finite observer that records successively coarser layers and leaves an unresolved completion.

This report uses that idea only as hypothesis provenance. It does not rely on a claim that ancient Egyptian mathematics encoded modern physics.

A testable family is:

```text
mu_hat_J(t) = sum from j=1 to J of 2^(-j) C_j[Phi history](t)
```

where every `C_j` must have declared units and may represent a frozen temporal block, exponential memory channel, or spatiotemporal coarse-graining at scale `2^j`.

The dyadic weights are not privileged. L3 must compare them against:

```text
D0: exact full-history inverse from this report
D1: one exponential memory channel
D2: freely spaced multiexponential channels
D3: dyadic timescales with dyadic weights
D4: dyadic timescales with fitted frozen weights
D5: equal-weight multiscale channels
D6: random fixed weights with matched capacity
D7: finite-lag linear state model
D8: joint finite Psi/Phi memory
D9: no-memory instantaneous Phi null
```

The relevant missing quantity is:

```text
completion residual = observed mu - frozen finite-memory prediction
```

It must first be measured. Calling it “Heka,” “quantum noise,” “dark matter,” “another universe,” or “spirit” before discriminating H0-H6 would convert a useful metaphor into an unfalsifiable label.

## 15. Root-programme impact matrix

| Root or child branch | Relationship | Evidence in this audit | Cheapest next discriminator |
|---|---|---|---|
| Current local `mu` as independently informative beyond all accessible history | `contradicts` inside regular full-`Phi` lane | Closed-loop exact reconstruction | Active-package receipt and nonuniform-`kappa` audit |
| Current `mu` as causal stored memory | `supports` | It is read by future `Psi`; reconstructed value must be restored each step | Finite-memory replacement |
| `mu` as higher-scale or slower `Phi` | `supports` as a representation candidate, not ontology | Complete `Phi` history suffices in one domain | L3 matched-capacity finite multiscale comparison |
| Universal `Phi` sufficiency | `contradicts` | Saturation and hidden-threshold counterexamples | Classify reachable frequency of non-identifying regimes |
| Relational or branch-aware `mu` | `constrains` | No richer state is needed in the regular lane | Define a relational observable absent from H0-H3 |
| Analog/continuum ontology | `unaffected` | No explicit-`dx` refinement | Explicit-`dx` convergence lane |
| Source and energy accounting | `unaffected` | Reconstruction is informational, not a closed fuel ledger | Preserve root source-accounting gate |
| Localization, particle, identity, copying, heredity | `unaffected` | No corresponding observer or intervention | Preserve root observer gates |
| Eq-11.1, epsilon, Relic Foam | `unaffected` | Not executed or merged | Preserve distinct provenance lanes |
| Cross-domain/dark-matter hypothesis | `not_yet_compared` | H6 registered only | Define a causal kernel and astronomical observables before testing |
| Research reliability | `supports` bounded adversarial inference | Positive domain and exact failures are both retained | Supported-environment and active-package receipts |

## 16. Limitations and validity threats

1. The active `lineum_core.math` package was not imported from a clean checkout.
2. The frozen adapter transcribes the deterministic NumPy path at the stated source blob.
3. The execution environment used Python `3.13.5` and NumPy `2.3.5`; the repository declares `numpy>=1.24,<2.0.0`.
4. Uniform `kappa = 1` is essential to the exact FFT inverse used in the main matrix.
5. The horizon was 80 steps on a fixed `32 x 32` grid.
6. No stochastic source, linon generation, clipping event, nonuniform boundary, explicit `dx`, arbitrary precision, Torch backend, or GPU backend was tested.
7. The initial conditions are representative frozen probes, not a proof over all reachable states.
8. Exact counterexamples establish non-identifiability of the observer; they do not measure how often the failures occur naturally.
9. The historical dyadic analogy supplies no scientific evidence.
10. No physical-universe correspondence was tested.

## 17. Reopen triggers

Reopen or supersede this report if:

- `lineum_core/math.py` changes its mode-coupling order, `Phi` diffusion, clipping, `mu` threshold, decay, write point, `kappa` use, precision, or backend;
- a clean active-package run differs from the frozen adapter above `1e-12`;
- NumPy below 2.0 produces a material difference;
- a nonuniform-`kappa` operator has an unexpected null space or unstable inverse;
- clipping or hidden-threshold states are shown unreachable under the declared natural dynamics;
- a finite-memory model passes all held-out closed-loop and intervention gates;
- a residual survives numerical, projection, boundary, relational, and stochastic controls;
- an H6 model supplies a declared causal kernel and independently passes relevant physical observations.

## 18. Next cross-program discriminator

The next experiment is a standalone preregistered L3 finite-memory comparison.

It must:

1. generate train, validation, and held-out initialization families;
2. freeze all memory operators and weights before held-out evaluation;
3. compare D0-D9 at matched parameter count and storage cost;
4. evaluate passive `mu` prediction and closed-loop `Psi/Phi` futures separately;
5. include saturation, nonuniform `kappa`, wrong-history transfer, history reset, and shuffled-history interventions;
6. report residual structure rather than assigning it a cause;
7. classify H0-H6 only after the registered controls;
8. remain separate from dark-matter, quantum, branch, and continuum claims.

## 19. Reproduction

Requirements for the historical run:

```text
Python 3.13.5
NumPy 2.3.5
CPU
periodic arrays
no external files
```

Repository-supported revalidation must additionally run under:

```text
numpy>=1.24,<2.0.0
```

Run:

```bash
python l2_audit.py
```

Complete executable verifier:

```python
import itertools, json, platform, sys
from dataclasses import dataclass, replace
import numpy as np

@dataclass(frozen=True)
class Cfg:
    dt: float = 1.0
    psi_diffusion: float = 0.05
    phi_diffusion: float = 0.05
    drift_strength: float = -0.004
    stencil_type: str = "LAP4"
    phi_diffusion_scales_with_dt: bool = False
    mode_coupling_strength: float = 0.001
    mu_eta: float = 0.005
    mu_rho: float = 0.0001
    mu_cap: float = 10.0
    mu_peak_cutoff_ratio: float = 0.1
    psi_amp_cap: float = 1e6
    phi_cap: float = 1e6

def diffuse(f, k, rate, stencil):
    ku,kd,kl,kr = (np.roll(k,1,0),np.roll(k,-1,0),np.roll(k,1,1),np.roll(k,-1,1))
    fu,fd,fl,fr = (np.roll(f,1,0),np.roll(f,-1,0),np.roll(f,1,1),np.roll(f,-1,1))
    if stencil == "LAP8":
        kul,kur,kdl,kdr = (np.roll(ku,1,1),np.roll(ku,-1,1),np.roll(kd,1,1),np.roll(kd,-1,1))
        ful,fur,fdl,fdr = (np.roll(fu,1,1),np.roll(fu,-1,1),np.roll(fd,1,1),np.roll(fd,-1,1))
        s = fu*ku+fd*kd+fl*kl+fr*kr + .25*(ful*kul+fur*kur+fdl*kdl+fdr*kdr)
        a = ku+kd+kl+kr + .25*(kul+kur+kdl+kdr)
    else:
        s, a = fu*ku+fd*kd+fl*kl+fr*kr, ku+kd+kl+kr
    return rate*(s-a*f)

def cap_complex(z, cap):
    z=np.asarray(z,np.complex128).copy(); m=np.abs(z); hit=m>cap
    if np.any(hit): z[hit] *= cap/(m[hit]+1e-30)
    return z

def mu_step(mu, e, k, c):
    mu=np.asarray(mu,float).copy(); drift=1+mu; q=c.mu_peak_cutoff_ratio
    if 0<q<1: q *= np.max(e)
    a=np.maximum(e-q,0)
    mu += c.mu_eta*a*k*drift*c.dt; mu -= c.mu_rho*mu*c.dt
    return np.clip(mu,0,c.mu_cap)

def step(s,c,write_mu):
    psi=np.asarray(s["psi"],np.complex128).copy(); phi=np.asarray(s["phi"],float).copy()
    k=np.asarray(s["kappa"],float).copy(); mu=np.asarray(s["mu"],float).copy(); drift=1+mu
    pint=np.clip(phi,0,10); inter=.1*np.tanh((.04*pint*k*drift)/.1)*psi; inter/=1+np.abs(inter)/10
    gx,gy=np.gradient(phi); flow=c.drift_strength*(gx+1j*gy)*k*drift; flow/=1+np.abs(flow)/10
    psi += flow*c.dt; psi=cap_complex(psi,c.psi_amp_cap); psi += inter*c.dt; psi -= .005*psi*c.dt
    psi += diffuse(psi,k,c.psi_diffusion,c.stencil_type)*k*c.dt
    e=np.abs(psi)**2; de=c.mode_coupling_strength*e*k*c.dt; pre=phi+de
    psi=(psi/(np.sqrt(e)+1e-12))*np.sqrt(np.maximum(e-de,0))
    scale=c.dt if c.phi_diffusion_scales_with_dt else 1.
    raw=pre+k*c.phi_diffusion*diffuse(pre,k,.05,c.stencil_type)*scale; phi=np.clip(raw,0,c.phi_cap)
    if write_mu: mu=mu_step(mu,e,k,c)
    return {"psi":psi,"phi":phi,"kappa":k,"mu":mu},{"e":e,"pre":pre,"raw":raw}

def symbol(n,c):
    k=2*np.pi*np.fft.fftfreq(n); ky,kx=np.meshgrid(k,k,indexing="ij")
    if c.stencil_type=="LAP8": lam=2*np.cos(kx)+2*np.cos(ky)+np.cos(kx)*np.cos(ky)-5
    else: lam=2*np.cos(kx)+2*np.cos(ky)-4
    scale=c.dt if c.phi_diffusion_scales_with_dt else 1.
    return 1+c.phi_diffusion*.05*scale*lam

def recover(phi0,phi1,c):
    pre=np.fft.ifft2(np.fft.fft2(phi1)/symbol(phi1.shape[0],c)).real
    return (pre-phi0)/(c.mode_coupling_strength*c.dt)

def initials(n=32):
    y,x=np.indices((n,n)); q=(n-1)/2; r2=(x-q)**2+(y-q)**2
    g=np.exp(-r2/(2*(n/9)**2)).astype(complex); vortex=g*np.exp(1j*np.arctan2(y-q,x-q))
    ra=(x-.32*n)**2+(y-.5*n)**2; rb=(x-.68*n)**2+(y-.5*n)**2
    two=np.exp(-ra/(2*(n/12)**2))+.8*np.exp(.7j)*np.exp(-rb/(2*(n/12)**2))
    rng=np.random.default_rng(20260731); z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    kx=np.fft.fftfreq(n)[None,:]; ky=np.fft.fftfreq(n)[:,None]
    smooth=np.fft.ifft2(np.fft.fft2(z)*np.exp(-(kx*kx+ky*ky)/(2*.09**2)))
    smooth=smooth/np.max(np.abs(smooth))*.8
    return {"gaussian":g,"phase_winding":vortex,"two_packets":two,"smooth_random":smooth}

def matrix():
    out=[]; maxima=np.zeros(4); cap=0; minraw=np.inf; maxraw=-np.inf; I=initials()
    for name,dt,st,scaled in itertools.product(I,(1.,.5),("LAP4","LAP8"),(False,True)):
        c=Cfg(dt=dt,stencil_type=st,phi_diffusion_scales_with_dt=scaled)
        z=np.zeros((32,32)); k=np.ones((32,32)); a={"psi":I[name].copy(),"phi":z.copy(),"kappa":k.copy(),"mu":z.copy()}
        b={key:value.copy() for key,value in a.items()}; err=np.zeros(4); mine=np.inf; maxe=-np.inf; localcap=0
        for _ in range(80):
            oldphi=b["phi"].copy(); an,ai=step(a,c,True); bn,bi=step(b,c,False); eh=recover(oldphi,bn["phi"],c)
            bn["mu"]=mu_step(b["mu"],eh,k,c)
            e=np.array([np.max(np.abs(an["psi"]-bn["psi"])),np.max(np.abs(an["phi"]-bn["phi"])),np.max(np.abs(an["mu"]-bn["mu"])),np.max(np.abs(ai["e"]-eh))],float)
            err=np.maximum(err,e); maxima=np.maximum(maxima,e); mine=min(mine,float(eh.min())); maxe=max(maxe,float(eh.max()))
            localcap += int(np.count_nonzero((bi["raw"]<0)|(bi["raw"]>c.phi_cap))); minraw=min(minraw,float(bi["raw"].min())); maxraw=max(maxraw,float(bi["raw"].max())); a,b=an,bn
        cap += localcap; out.append([name,dt,st,scaled,*map(float,err),mine,maxe,float(symbol(32,c).min()),localcap])
    return {"columns":["init","dt","stencil","phi_dt_scaled","psi_err","phi_err","mu_err","energy_err","min_ehat","max_ehat","min_symbol","cap_events"],"rows":out,"global_max":{"psi":maxima[0],"phi":maxima[1],"mu":maxima[2],"energy":maxima[3]},"cap_events":cap,"min_phi_raw":minraw,"max_phi_raw":maxraw}

def dense_check():
    rng=np.random.default_rng(12345); rows=[]
    for st,dt,scaled in itertools.product(("LAP4","LAP8"),(1.,.5),(False,True)):
        c=Cfg(dt=dt,stencil_type=st,phi_diffusion_scales_with_dt=scaled); n=6
        p=rng.random((n,n))*.2; e=rng.random((n,n))*3; pre=p+c.mode_coupling_strength*e*c.dt; k=np.ones((n,n)); scale=c.dt if scaled else 1.
        after=pre+c.phi_diffusion*diffuse(pre,k,.05,st)*scale; D=np.zeros((n*n,n*n))
        for j in range(n*n):
            f=np.zeros((n,n)); f.flat[j]=1; D[:,j]=(f+c.phi_diffusion*diffuse(f,k,.05,st)*scale).ravel()
        dense=np.linalg.solve(D,after.ravel()).reshape(n,n); fft=np.fft.ifft2(np.fft.fft2(after)/symbol(n,c)).real
        rows.append([st,dt,scaled,float(np.max(np.abs(dense-pre))),float(np.max(np.abs(fft-pre))),float(np.max(np.abs(dense-fft))),float(np.linalg.cond(D))])
    return {"columns":["stencil","dt","scaled","dense_err","fft_err","dense_fft","condition"],"rows":rows}

def wrong_control():
    I=initials(); rows=[]
    for name,st,true_scaled in itertools.product(I,("LAP4","LAP8"),(False,True)):
        c=Cfg(dt=.5,stencil_type=st,phi_diffusion_scales_with_dt=true_scaled); wrong=replace(c,phi_diffusion_scales_with_dt=not true_scaled)
        z=np.zeros((32,32)); k=np.ones((32,32)); s={"psi":I[name].copy(),"phi":z.copy(),"kappa":k,"mu":z.copy()}; wm=z.copy(); old=s["phi"].copy(); me=ee=0.
        for _ in range(80):
            sn,internal=step(s,c,True); ew=recover(old,sn["phi"],wrong); wm=mu_step(wm,ew,k,c)
            me=max(me,float(np.max(np.abs(sn["mu"]-wm)))); ee=max(ee,float(np.max(np.abs(internal["e"]-ew)))); s=sn; old=s["phi"].copy()
        rows.append([name,st,true_scaled,me,ee])
    return {"rows":rows,"mu_range":[min(r[3] for r in rows),max(r[3] for r in rows)],"energy_range":[min(r[4] for r in rows),max(r[4] for r in rows)]}

def phi_mu_from_e(e,phi,k,c):
    pre=phi+c.mode_coupling_strength*e*k*c.dt; scale=c.dt if c.phi_diffusion_scales_with_dt else 1.
    raw=pre+k*c.phi_diffusion*diffuse(pre,k,.05,c.stencil_type)*scale
    return np.clip(raw,0,c.phi_cap),mu_step(np.zeros_like(phi),e,k,c)

def counterexamples():
    z=np.zeros((4,4)); o=np.ones((4,4)); c=replace(Cfg(),phi_cap=.5)
    pa,ma=phi_mu_from_e(np.full((4,4),1000.),z,o,c); pb,mb=phi_mu_from_e(np.full((4,4),2000.),z,o,c)
    k=o.copy(); k[0,0]=0; ea=np.full((4,4),5.); eb=ea.copy(); eb[0,0]=100.
    pc,mc=phi_mu_from_e(ea,z,k,Cfg()); pd,md=phi_mu_from_e(eb,z,k,Cfg()); vis=k>0
    return {"saturation":{"phi_equal":bool(np.array_equal(pa,pb)),"phi":float(pa[0,0]),"mu_a":float(ma[0,0]),"mu_b":float(mb[0,0]),"mu_difference":float(abs(mb[0,0]-ma[0,0]))},"kappa_global_floor":{"phi_max_difference":float(np.max(np.abs(pc-pd))),"visible_mu_a":float(np.max(mc[vis])),"visible_mu_b":float(np.max(md[vis])),"visible_mu_difference":float(np.max(np.abs(mc[vis]-md[vis]))),"floor_a":float(.1*ea.max()),"floor_b":float(.1*eb.max())}}

result={"environment":{"python":sys.version.split()[0],"numpy":np.__version__,"platform":platform.platform()},"declared_numpy":">=1.24,<2.0.0","supported_numpy_environment":np.lib.NumpyVersion(np.__version__)<"2.0.0","dense_check":dense_check(),"closed_loop":matrix(),"wrong_semantics":wrong_control(),"counterexamples":counterexamples()}
print(json.dumps(result,sort_keys=True,separators=(",",":")))
```

## 20. Machine-readable output

The exact compact JSON emitted by the verifier is retained below. The per-run matrix contains all 32 configurations; columns are declared in the payload.

```json
{"closed_loop":{"cap_events":0,"columns":["init","dt","stencil","phi_dt_scaled","psi_err","phi_err","mu_err","energy_err","min_ehat","max_ehat","min_symbol","cap_events"],"global_max":{"energy":1.6930901125533637e-14,"mu":6.106226635438361e-16,"phi":3.469446951953614e-18,"psi":2.2887833992611187e-16},"max_phi_raw":0.033402817725922504,"min_phi_raw":1.1911251868988922e-25,"rows":[["gaussian",1.0,"LAP4",false,5.551115288561903e-17,0.0,5.412337245047638e-16,9.992007221626409e-15,-5.410508092706881e-17,0.9372129210688147,0.98,0],["gaussian",1.0,"LAP4",true,5.551115288561903e-17,0.0,5.412337245047638e-16,9.992007221626409e-15,-5.410508092706881e-17,0.9372129210688147,0.98,0],["gaussian",1.0,"LAP8",false,5.551115288561903e-17,0.0,5.412337245047638e-16,9.992007221626409e-15,-5.410508092706881e-17,0.9372129210688147,0.98,0],["gaussian",1.0,"LAP8",true,5.551115288561903e-17,0.0,5.412337245047638e-16,9.992007221626409e-15,-5.410508092706881e-17,0.9372129210688147,0.98,0],["gaussian",0.5,"LAP4",false,5.551115288561903e-17,0.0,5.551115123125783e-16,1.1934897514720433e-14,-7.979727989493313e-17,0.9683234072054236,0.98,0],["gaussian",0.5,"LAP4",true,5.551115288561903e-17,0.0,5.551115123125783e-16,1.2434497875801753e-14,-1.1796119636642288e-16,0.9683234072054235,0.99,0],["gaussian",0.5,"LAP8",false,5.551115288561903e-17,0.0,5.551115123125783e-16,1.1934897514720433e-14,-9.020562075079397e-17,0.9683234072054236,0.98,0],["gaussian",0.5,"LAP8",true,5.551115288561903e-17,0.0,5.551115123125783e-16,1.2656542480726785e-14,-1.196959198423997e-16,0.9683234072054236,0.99,0],["phase_winding",1.0,"LAP4",false,6.206335383118183e-17,8.673617379884035e-19,5.204170427930421e-16,9.547918011776346e-15,-1.5178830414797062e-16,0.9008698621985278,0.98,0],["phase_winding",1.0,"LAP4",true,6.206335383118183e-17,8.673617379884035e-19,5.204170427930421e-16,9.547918011776346e-15,-1.5178830414797062e-16,0.9008698621985278,0.98,0],["phase_winding",1.0,"LAP8",false,5.594315114139762e-17,8.673617379884035e-19,5.204170427930421e-16,9.547918011776346e-15,-1.6653345369377348e-16,0.9008698621985279,0.98,0],["phase_winding",1.0,"LAP8",true,5.594315114139762e-17,8.673617379884035e-19,5.204170427930421e-16,9.547918011776346e-15,-1.6653345369377348e-16,0.9008698621985279,0.98,0],["phase_winding",0.5,"LAP4",false,6.206335383118183e-17,8.673617379884035e-19,5.551115123125783e-16,1.2434497875801753e-14,-2.7755575615628914e-16,0.949785939561998,0.98,0],["phase_winding",0.5,"LAP4",true,6.206335383118183e-17,8.673617379884035e-19,5.551115123125783e-16,1.3322676295501878e-14,-3.3306690738754696e-16,0.9497859395619979,0.99,0],["phase_winding",0.5,"LAP8",false,6.206335383118183e-17,8.673617379884035e-19,5.551115123125783e-16,1.2878587085651816e-14,-2.914335439641036e-16,0.949785939561998,0.98,0],["phase_winding",0.5,"LAP8",true,6.206335383118183e-17,8.673617379884035e-19,5.551115123125783e-16,1.3322676295501878e-14,-3.3306690738754696e-16,0.9497859395619979,0.99,0],["two_packets",1.0,"LAP4",false,1.2412670766236366e-16,1.734723475976807e-18,5.551115123125783e-16,1.0658141036401503e-14,-5.204170427930421e-16,0.9438847647150218,0.98,0],["two_packets",1.0,"LAP4",true,1.2412670766236366e-16,1.734723475976807e-18,5.551115123125783e-16,1.0658141036401503e-14,-5.204170427930421e-16,0.9438847647150218,0.98,0],["two_packets",1.0,"LAP8",false,1.1443916996305594e-16,1.734723475976807e-18,5.551115123125783e-16,1.0658141036401503e-14,-5.204170427930421e-16,0.9438847647150218,0.98,0],["two_packets",1.0,"LAP8",true,1.1443916996305594e-16,1.734723475976807e-18,5.551115123125783e-16,1.0658141036401503e-14,-5.204170427930421e-16,0.9438847647150218,0.98,0],["two_packets",0.5,"LAP4",false,2.2887833992611187e-16,3.469446951953614e-18,6.106226635438361e-16,1.687538997430238e-14,-1.4273318396147656e-15,0.9737514270379475,0.98,0],["two_packets",0.5,"LAP4",true,2.2887833992611187e-16,3.469446951953614e-18,6.106226635438361e-16,1.6930901125533637e-14,-1.4273318396147656e-15,0.9737514270379475,0.99,0],["two_packets",0.5,"LAP8",false,2.2887833992611187e-16,3.469446951953614e-18,6.106226635438361e-16,1.687538997430238e-14,-1.4085954624931674e-15,0.9737514270379475,0.98,0],["two_packets",0.5,"LAP8",true,2.2887833992611187e-16,3.469446951953614e-18,6.106226635438361e-16,1.6930901125533637e-14,-1.4273318396147656e-15,0.9737514270379475,0.99,0],["smooth_random",1.0,"LAP4",false,6.938893903907228e-17,4.336808689942018e-19,2.7755575615628914e-16,4.884981308350689e-15,-5.551115123125783e-17,0.5732929330895686,0.98,0],["smooth_random",1.0,"LAP4",true,6.938893903907228e-17,4.336808689942018e-19,2.7755575615628914e-16,4.884981308350689e-15,-5.551115123125783e-17,0.5732929330895686,0.98,0],["smooth_random",1.0,"LAP8",false,6.206335383118183e-17,4.336808689942018e-19,2.7755575615628914e-16,4.884981308350689e-15,-5.551115123125783e-17,0.5732929330895686,0.98,0],["smooth_random",1.0,"LAP8",true,6.206335383118183e-17,4.336808689942018e-19,2.7755575615628914e-16,4.884981308350689e-15,-5.551115123125783e-17,0.5732929330895686,0.98,0],["smooth_random",0.5,"LAP4",false,5.721958498152797e-17,4.336808689942018e-19,3.0531133177191805e-16,6.328271240363392e-15,-1.1102230246251565e-16,0.6179245787147299,0.98,0],["smooth_random",0.5,"LAP4",true,5.721958498152797e-17,4.336808689942018e-19,3.0531133177191805e-16,6.5503158452884236e-15,-1.1102230246251565e-16,0.6179245787147299,0.99,0],["smooth_random",0.5,"LAP8",false,5.721958498152797e-17,4.336808689942018e-19,3.0531133177191805e-16,6.439293542825908e-15,-1.1102230246251565e-16,0.6179245787147299,0.98,0],["smooth_random",0.5,"LAP8",true,5.721958498152797e-17,4.336808689942018e-19,3.0531133177191805e-16,6.5503158452884236e-15,-1.1102230246251565e-16,0.6179245787147299,0.99,0]]},"counterexamples":{"kappa_global_floor":{"floor_a":0.5,"floor_b":10.0,"phi_max_difference":0.0,"visible_mu_a":0.02249775,"visible_mu_b":0.0,"visible_mu_difference":0.02249775},"saturation":{"mu_a":4.49955,"mu_b":8.9991,"mu_difference":4.49955,"phi":0.5,"phi_equal":true}},"declared_numpy":">=1.24,<2.0.0","dense_check":{"columns":["stencil","dt","scaled","dense_err","fft_err","dense_fft","condition"],"rows":[["LAP4",1.0,false,1.1102230246251565e-16,1.1102230246251565e-16,1.1102230246251565e-16,1.0204081632653066],["LAP4",1.0,true,1.1102230246251565e-16,1.1102230246251565e-16,1.1102230246251565e-16,1.0204081632653066],["LAP4",0.5,false,8.326672684688674e-17,1.1102230246251565e-16,1.1102230246251565e-16,1.0204081632653066],["LAP4",0.5,true,8.326672684688674e-17,1.1102230246251565e-16,1.1102230246251565e-16,1.0101010101010102],["LAP8",1.0,false,1.1102230246251565e-16,1.6653345369377348e-16,1.942890293094024e-16,1.0204081632653066],["LAP8",1.0,true,1.1102230246251565e-16,1.6653345369377348e-16,1.942890293094024e-16,1.0204081632653066],["LAP8",0.5,false,1.1102230246251565e-16,1.1102230246251565e-16,1.3877787807814457e-16,1.0204081632653066],["LAP8",0.5,true,1.1102230246251565e-16,1.1102230246251565e-16,1.3877787807814457e-16,1.0101010101010102]]},"environment":{"numpy":"2.3.5","platform":"Linux-6.12.13-x86_64-with-glibc2.41","python":"3.13.5"},"supported_numpy_environment":false,"wrong_semantics":{"energy_range":[0.013587865480030298,0.026196313253229353],"mu_range":[0.0015241827422114232,0.0035763982963578633],"rows":[["gaussian","LAP4",false,0.0018718456477478107,0.015215993492412927],["gaussian","LAP4",true,0.0019118252037271105,0.01569334120525906],["gaussian","LAP8",false,0.002430591024040321,0.018924944128466403],["gaussian","LAP8",true,0.002505451605894035,0.01980119806225561],["phase_winding","LAP4",false,0.0015241827422114232,0.013587865480030298],["phase_winding","LAP4",true,0.0015618384475030114,0.014003170904176354],["phase_winding","LAP8",false,0.0020688704264066873,0.017261723636231574],["phase_winding","LAP8",true,0.002139994381534658,0.018049844022799522],["two_packets","LAP4",false,0.0022981029652449636,0.01979114476931354],["two_packets","LAP4",true,0.002342722318686707,0.02039789864347313],["two_packets","LAP8",false,0.002946456127782937,0.023397004481862438],["two_packets","LAP8",true,0.003036388805942425,0.024494371133226167],["smooth_random","LAP4",false,0.002594833839065807,0.02192047707681949],["smooth_random","LAP4",true,0.002670340374750849,0.022591898344268557],["smooth_random","LAP8",false,0.003467702128183098,0.02497860836454391],["smooth_random","LAP8",true,0.0035763982963578633,0.026196313253229353]]}}
```

## 21. Final local verdict

```text
what_current_implementation_computes:
    Phi records a diffused and clipped mode-coupled projection of write-time Psi energy;
    mu records a thresholded, multiplicative, decaying projection of the same energy.

what_was_observed:
    exact full-Phi-history closed-loop reconstruction passed in 32 regular runs;
    a dense independent inverse agreed;
    a wrong inverse failed;
    two exact same-Phi/different-mu counterexamples passed.

cautious_interpretation:
    current mu can be a useful stored coordinate of Phi-readable history in a regular lane;
    Phi is not a universally identifying observer of current mu.

hypotheses:
    finite dyadic memory and H0-H6 completion-residual families remain open.

known_physics_boundary:
    no quantum, dark-matter, multiverse, consciousness, or physical-ontology claim was tested.
```
