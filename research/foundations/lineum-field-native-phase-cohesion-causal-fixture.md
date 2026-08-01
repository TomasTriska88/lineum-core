# Field-Native Phase Cohesion Causal Fixture

**Status:** active preregistration; continuous local-field fixture frozen before execution  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-01  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`  
**Recovered root version:** 0.4.14  
**Root evidence cutoff:** 2026-07-29  
**Root blob SHA:** `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, version 0.3.0, blob `5304874451caf32313ad0e8e3c59e53958698d79`  
**Report lineage:** root programme -> pneuma cohesion fixture -> adversarial autonomy audit -> point causal-path discriminator v0.4.0 -> field-readout transfer preregistration commit `2e8d8a26129ce664010a925e720b5acaa3bf0f63` -> field-readout validation commit `0b9359c24b95e4dcd25e525a0e8c68c20343840f` -> this report  
**Operational task:** ClickUp `869echn1w`; latest closing-comment synchronization failed because the connector reported the comment tool unavailable; Git remains the scientific source of truth  
**Current Core implementation inspected but not executed:** `lineum_core/math.py`, blob `bb877021810691223a0eb960a45493a2e351112a`  
**Scope:** Validate the causal observer in a genuinely field-native local evolution law without moving points, stored pair rest lengths, member labels, or a hidden object graph. The fixture is one-dimensional and phase-only. It is not the current Lineum equation.  
**Central question:** Can a local reciprocal phase field repair a relative phase injury only when its continuous causal paths remain connected, while a global target controller repairs independently of those paths and reveals external action?  
**Current confidence:** high in the analytic null predictions; medium that the frozen observation horizon will satisfy all quantitative positive gates across three spatial resolutions; zero evidence for P2, a particle, physical pneuma, or nature.

## 1. Answer first

The hidden points are removed entirely.

The synthetic state is now a phase field `theta(s,t)` defined around a closed one-dimensional ring. Local evolution is diffusion:

```text
partial_t theta = D partial_s^2 theta
```

The discrete implementation is a conservative finite-volume field law. Every flux across one cell boundary enters one cell and leaves its neighbour. No point labels, rest lengths, target shape, or absolute phase are used by the local law.

A relational injury shifts one half of the ring by `-0.6` radians and the other by `+0.6` radians. An intact local field should diffuse that mismatch away. A causal cut sets conductivity to zero at both interfaces between the halves. Each half may smooth internally, but no phase information can cross between them, so the relative mismatch should remain.

A coordinate-wise global controller is retained only as an adversarial external null. It can restore the field despite the cuts because it reads a stored target phase at every location. Its external action must be nonzero.

This fixture tests synchronization and causal connectivity only. It does not test localization, shape persistence, vortex identity, copying, or a physical particle.

## 2. Why this is the next smallest step

The previous checkpoint established that the causal distinction survives conversion from labeled point trajectories to smooth unlabeled scalar-field readouts. It still used a hidden point generator.

The present step removes that hidden generator while keeping the scientific question narrow:

```text
previous gate:
    field observer, point-generated dynamics;

current gate:
    field observer, field-native local dynamics;

not yet authorized:
    current Lineum Core equation or P2 application.
```

A one-dimensional ring is selected because its local diffusion law, causal cuts, conservation, symmetries, and null modes are analytically transparent. Success would justify a later two-dimensional field-native fixture, not a jump directly to P2.

## 3. Field and local equation

The physical coordinate is periodic:

```text
s in [0, 2 pi)
theta(s + 2 pi, t) = theta(s,t)
z(s,t) = exp(i theta(s,t))
D = 0.20
```

For `N` finite-volume cells with spacing `ds = 2 pi/N`, let edge conductivity be `c_j` between cells `j` and `j+1` modulo `N`.

The semidiscrete local law is:

```text
d theta_j/dt = D/ds^2 * [
    c_j     (theta_{j+1} - theta_j)
  - c_{j-1} (theta_j - theta_{j-1})
]
```

All intact conductivities equal one. The cut law sets exactly two conductivities to zero:

```text
edge between N/2 - 1 and N/2 = 0
edge between N - 1 and 0 = 0
```

These two cuts disconnect the first and second halves. The local operator is symmetric, negative semidefinite, and has zero row sum. The cut operator has one constant null mode per disconnected half.

The primary integrator is the exact matrix exponential of the frozen semidiscrete operator, evaluated by its symmetric eigendecomposition:

```text
theta(T) = V exp(lambda T) V^T theta(0)
```

This removes time-integration error from the primary classification. A Crank-Nicolson solver supplies an independent numerical check.

## 4. Initial continuum field and formation

Each seed defines a smooth resolution-independent phase field:

```text
theta_0(s) = sum_{m=1}^4 [a_m cos(ms) + b_m sin(ms)]
a_m, b_m ~ Normal(0, 0.12^2)
```

The same coefficients are evaluated on every resolution.

Frozen formation parameters:

```text
formation seeds = 900..911
formation horizon = 5.0
local formation = intact diffusion
external formation = target controller
```

The external target is a fixed smooth field:

```text
theta_target(s) = 0.20 cos(s) + 0.10 sin(2s)
```

The global controller law is:

```text
d theta_j/dt = -k_g [theta_j - theta_target(s_j)]
k_g = 0.50
```

Its exact solution is used. The controller is external by construction because every field cell receives the target value associated with its coordinate.

## 5. Challenge and cases

The challenge is applied after formation:

```text
cells 0 .. N/2-1: theta <- theta - 0.60
cells N/2 .. N-1: theta <- theta + 0.60
challenge horizon = 30.0
```

Every challenged lane has a matched no-challenge twin with identical seed, resolution, formation history, law, and observation times.

Frozen cases:

```text
F_LOCAL_INTACT:
    local formation and intact local diffusion during challenge;

F_LOCAL_CUT:
    local formation and cut local diffusion during challenge;

F_LOCAL_REMOVED:
    local formation and zero challenge evolution;

F_GLOBAL_CONTINUOUS:
    global formation and controller active during challenge;

F_GLOBAL_CUT:
    same global controller;
    causal cuts declared but irrelevant to its equation;

F_GLOBAL_REMOVED:
    global formation and zero challenge evolution;

F_DISORDER_REMOVED:
    independent smooth random phase field with the same mode budget;
    zero challenge evolution.
```

The observer is blind to the case label and evolution operator. External-action and cut metadata are consulted only after field restoration is measured.

## 6. External action and local reciprocity

For the global challenged lane:

```text
A_ext = integral_0^T sqrt(ds * sum_j |d theta_j/dt|^2) dt
```

The integral is evaluated by the trapezoidal rule on 401 equally spaced exact-solution samples. Global positive controls require `A_ext > 0.05`.

All local, removed, and disorder lanes declare zero external action.

Local reciprocity checks:

```text
max absolute row sum of local generator < 1e-12
max absolute column sum of local generator < 1e-12
operator symmetry error < 1e-12
mean phase change under local evolution < 1e-12
```

For the cut law, mean phase within each disconnected half must remain constant below `1e-12`.

## 7. Field-only observers

The observer receives only complex fields:

```text
z_j = exp(i theta_j)
```

It does not receive unwrapped phase, the target, cut locations, operator matrices, or case labels.

### 7.1 Global-phase-invariant overlap

For challenged `C` and matched twin `T`:

```text
O = |sum_j z_C,j conjugate(z_T,j)| / N
d_overlap = sqrt(max(0, 1 - O^2))
```

The magnitude removes a uniform phase offset.

### 7.2 Reflection- and translation-invariant spectral power

Compute the discrete Fourier transform of `z`. For each unsigned wavenumber `m`, combine positive and negative powers:

```text
P_0 = |Z_0|^2
P_m = |Z_m|^2 + |Z_{-m}|^2
```

Normalize `P` by its sum. This signature is invariant under cyclic translation, reflection, and global phase.

### 7.3 Local bond-strain quantiles

For every neighbouring pair on the full observational ring, including both causal-cut locations:

```text
q_j = 1 - real(z_{j+1} conjugate(z_j))
```

Sort `q` and sample 64 equally spaced quantiles. The observer always uses the full observational adjacency and is not told which dynamical bonds were cut.

### 7.4 Differential recovery

For each distance family:

```text
d0 = challenged-to-twin distance immediately after injury
df = challenged-to-twin distance at T=30
R = 1 - df/d0
```

The three scores are:

```text
R_overlap
R_spectrum
R_bond
R_field = min(R_overlap, R_spectrum, R_bond)
```

Every initial distance must exceed `1e-8`.

## 8. Frozen grid and execution matrix

```text
seeds = 900..911
resolutions = [64, 128, 256]
field cases = 7
primary trajectories = 12 * 3 * 7 = 252
challenged and twin paths = 504
primary evolution = exact semidiscrete exponential
```

No seed, resolution, coefficient, horizon, target, challenge, observer, or threshold may change after this version is committed.

## 9. Frozen family gates

```text
F_LOCAL_INTACT:
    R_overlap > 0.95
    R_spectrum > 0.90
    R_bond > 0.95
    external action < 1e-12

F_LOCAL_CUT:
    R_field < 0.10
    external action < 1e-12

F_LOCAL_REMOVED:
    R_field < 0.10
    external action < 1e-12

F_GLOBAL_CONTINUOUS:
    R_overlap > 0.99
    R_spectrum > 0.99
    R_bond > 0.99
    external action > 0.05

F_GLOBAL_CUT:
    same restoration and action gates as F_GLOBAL_CONTINUOUS

F_GLOBAL_REMOVED:
    R_field < 0.10
    external action < 1e-12

F_DISORDER_REMOVED:
    R_field < 0.10
    external action < 1e-12

local cut sensitivity:
    R_field(F_LOCAL_INTACT) - R_field(F_LOCAL_CUT) > 0.85
    for every seed and resolution

global cut invariance:
    challenged and twin fields are bit-identical between the two global cases;
    all three recovery scores differ by less than 1e-14.
```

## 10. Resolution and symmetry gates

Continuum-consistent coefficients are evaluated at `N=64`, `128`, and `256` from the same seed coefficients.

For every positive family and seed:

```text
absolute R_field difference between N=128 and N=256 < 0.02
family classification unchanged across all resolutions
```

For all `N=128`, `F_LOCAL_INTACT` trajectories, apply common transformations to challenged and twin complex fields:

```text
cyclic translation by 37 cells
reflection j -> -j
uniform phase shift by 0.73 radians
```

Every recovery score must change by less than `1e-12`.

## 11. Independent solver and analytic gates

The primary exact semidiscrete result is compared with Crank-Nicolson for seed `900`, `N=64`, local intact and local cut:

```text
CN steps = [0.10, 0.05]
max final field difference between exact and dt=0.05 < 2e-4
error at dt=0.05 < error at dt=0.10
```

Analytic nulls:

```text
local cut challenge difference is piecewise constant and lies in the cut operator nullspace;
removed and disorder lanes are static after challenge;
global full and cut equations are identical;
local full and cut generators have no positive eigenvalue above 1e-12;
local Dirichlet energy cannot increase above 1e-12 tolerance.
```

Any failed independent or analytic check invalidates the implementation before interpretation.

## 12. Outcome interpretation

```text
all gates pass:
    validate a field-native causal synchronization observer in this one-dimensional fixture;
    next build a two-dimensional field-native localization fixture before P2;

local intact fails:
    the selected horizon or field observer is unsupported under this frozen protocol;
    preserve the result and stop at the negative-result owner gate;

cut or removed lanes restore:
    the observer is non-identifying or the implementation leaks across the declared cut;

local reciprocity or conservation fails:
    implementation invalid; no scientific verdict;

global controller fails:
    adversarial positive control invalid;

resolution or symmetry fails:
    no continuum-transfer claim.
```

## 13. Evidence-layer separation

```text
current Lineum implementation:
    not executed and not modified;

reproducible synthetic field evidence:
    not yet available at preregistration;

cautious interpretation if successful:
    local continuous-field synchronization can be distinguished from global target control;

hypothesis:
    related causal observers may later be applicable to a localized Lineum field process;

physical universe:
    no particle, material, biological, quantum, gravitational, or cosmological correspondence tested.
```

## 14. Root-programme impact before execution

| Root branch | Relation | Pre-execution impact |
|---|---|---|
| Collective-particle observer | `depends_on` | Removes the hidden moving-point generator but tests synchronization only. |
| P2 vortex-gas remnant | `unaffected` | Application remains prohibited. |
| Minimum-flux observer | `supports` | Adds causal cuts, matched disorder, and multiple symmetry-invariant field distances. |
| Source accounting | `supports` | Global target restoration receives an explicit external-action ledger. |
| `mu x kappa` repair | `unaffected` | No current field receives a repair role. |
| Boundary programme | `constrains` | Zero conductivity is a synthetic causal intervention, not a physical membrane claim. |
| Identity and copying | `unaffected` | No localized object, turnover, copying, or descent is present. |
| Ancient-text audit | `constrains` | Pneuma remains a metaphor that motivated a discriminator, not an implemented substance. |
| Physical universe | `not_yet_compared` | No empirical claim follows from a phase-diffusion fixture. |

## 15. Current verdict

```text
field_readout_transfer = validated
field_native_phase_protocol = frozen
field_native_phase_execution = not_started
current_Core_execution = not_started
P2_application = prohibited
production_code_change = none
whitepaper_change = none
next_action = execute the exact frozen matrix in ChatGPT
```
