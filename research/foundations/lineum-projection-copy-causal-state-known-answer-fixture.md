# Projection Copy versus Causal State: Known-Answer Wave Fixture

**Status:** active preregistration; frozen before execution; no Lineum or physical-nature conclusion claimed  
**Version:** 0.1.0  
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
**Related Lineum evidence:** deterministic state transplant, static-recipe versus live-state matrix, copying negative results, minimum-flux observer limitations, and collective-object preregistration as restated below  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Scope:** A standalone, known-answer observer fixture testing whether identical visible morphology and matched global scalar summaries imply identical causal state. The fixture uses the exactly solvable one-dimensional free Schrödinger equation, not the Lineum equation. It compares a complete complex state, an amplitude-only projection, an opposite-chirp state with the same density and global scalar summaries, a local-current reconstruction within a declared Gaussian family, and an energy-matched smooth random-phase control.  
**Central question:** Can an observer distinguish a copy that preserves only the visible image from a copy that preserves the hidden phase organization required for the same future?  
**Current confidence:** high that the analytic system provides a valid known-answer distinction; high that opposite chirps can share density, norm, centroid, width, mean momentum, and kinetic energy while evolving to different densities; medium that the finite-grid random-phase and current-reconstruction controls will meet the frozen numerical tolerances; no evidence is claimed yet because execution has not occurred.

## 1. Answer first

This fixture tests a simple claim before any application to Lineum:

> Two objects can look exactly the same in one snapshot and match several global measurements while being different dynamical states.

The everyday picture is two identical photographs of a spring. One spring is internally compressed and the other stretched, but the photograph records only its outline. After release, their futures reveal the hidden difference.

Here the visible photograph is the probability density `rho = |psi|^2`. The hidden organization is the spatial phase of the complex wave. Two wave packets will begin with identical density and matched global summaries but opposite position-momentum correlation. One must focus while the other expands.

The frozen decision is:

```text
image_copy_is_causal_state
    only if it reproduces held-out continuation and intervention response;

same_snapshot_and_global_scalars
    are insufficient when a matched hidden-state control has a different future;

local_current_reconstruction
    is accepted only inside the explicitly declared Gaussian-chirp family;

known_answer_fixture_success
    validates an observer distinction, not a Lineum particle, soul, pneuma, or ancient physics claim.
```

## 2. Motivation and provenance

### 2.1 Project-owner direction

The project owner asked for an out-of-the-box, programme-wide study of Gnostic texts, `pneuma`, 1 Enoch, and the Dead Sea Scrolls, not limited to the current vortex or `mu` branches.

The source audit identified a recurring structural distinction between an image or visible form and the complete organization that makes a process continue. The Hypostasis of the Archons was retained only as historical inspiration for the question. It is not treated as scientific evidence.

### 2.2 Existing Lineum evidence that constrains this fixture

The root programme already records:

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

This fixture does not reproduce those Lineum runs. It creates an independent known-answer test for the observer principle they require.

### 2.3 Why a separate child report is required

The predecessor preregistered six broad mechanism matrices. This document freezes the exact first execution lane, `IC1`, before numerical output exists. It is deliberately self-contained and does not require access to Lineum code.

## 3. Evidence layers

### 3.1 Current Lineum implementation

No Lineum implementation is executed or modified here. No statement about what current `Psi`, `Phi`, `mu`, or `kappa` will do is produced by this fixture.

### 3.2 Reproducible observation

None exists in version 0.1.0. All numerical values below are parameters, analytic expectations, or acceptance thresholds frozen before execution.

### 3.3 Cautious interpretation

If the fixture passes, it will show that a snapshot morphology observer and several matched global scalars can fail to identify a causal wave state in a known system.

### 3.4 Hypothesis or analogy

The relevance to Lineum copying, collective identity, state reconstruction, `mu`, and ancient image language remains hypothetical until separate Lineum interventions are executed.

### 3.5 Real physics boundary

The free Schrödinger equation is established physics for appropriate nonrelativistic quantum systems. This numerical fixture nevertheless uses dimensionless toy units and a prepared Gaussian packet. Passing the fixture does not show that Lineum is quantum mechanics or that ancient texts encoded quantum theory.

## 4. Frozen mathematical system

Use dimensionless units:

```text
hbar = 1
mass = 1
```

The evolution equation is:

```text
i * partial_t psi(x,t) = -(1/2) * partial_xx psi(x,t)
```

on a periodic numerical domain:

```text
x in [-L/2, L/2)
L = 80
primary grid N = 512
resolution controls N in {256, 512, 1024}
```

The exact spectral evolution for the represented periodic state is:

```text
psi_hat(k,t) = psi_hat(k,0) * exp(-i * k^2 * t / 2)
```

with:

```text
k = 2*pi*fftfreq(N, d=L/N)
```

No time-stepping approximation is required for the primary propagator.

## 5. Frozen initial family

Define the real normalized Gaussian amplitude:

```text
A(x) proportional to exp(-x^2 / (4*sigma^2))
sigma = 2.0
```

Normalize discretely so that:

```text
sum_x |A(x)|^2 * dx = 1
```

Define chirped states:

```text
psi_c(x,0) = A(x) * exp(i * c * x^2)
```

with:

```text
donor chirp c_minus = -0.12
opposite chirp c_plus = +0.12
zero chirp c_zero = 0
```

All three states have the same initial density, norm, centroid, and position variance. The two opposite-chirp states also have equal kinetic energy and zero mean momentum but opposite position-momentum covariance.

The evaluation time is frozen as:

```text
t_eval = 3.0
```

The smooth random-phase control uses:

```text
seed = 20260801
low Fourier modes n = 1 through 8
```

Its phase-gradient contribution is rescaled to match the donor's phase-gradient kinetic energy and shifted to zero density-weighted mean momentum.

## 6. Analytic known answer

For:

```text
psi(x,0) proportional to exp(-x^2/(4*sigma^2) + i*c*x^2)
```

the continuum Gaussian moments are:

```text
Var[x](0) = sigma^2
Cov_sym[x,p](0) = 2*c*sigma^2
Var[p](0) = 1/(4*sigma^2) + 4*c^2*sigma^2
```

Under free evolution:

```text
Var[x](t)
    = sigma^2
      + 2*t*Cov_sym[x,p](0)
      + t^2*Var[p](0)
```

For the frozen parameters at `t = 3`:

```text
negative chirp donor:
    Var[x] = 0.8761
    width = sqrt(0.8761) approximately 0.9360

zero phase amplitude copy:
    Var[x] = 4.5625
    width = sqrt(4.5625) approximately 2.1360

positive opposite chirp:
    Var[x] = 10.3961
    width = sqrt(10.3961) approximately 3.2243
```

Thus the donor focuses while the opposite-chirp control expands, despite matched initial density and global scalar summaries.

## 7. Frozen carrier matrix

### IC1-A: complete causal state

```text
psi_A = A * exp(i*c_minus*x^2)
```

This is the reference donor.

### IC1-B: amplitude image only

```text
psi_B = A
```

This preserves the full initial density but replaces all phase information by zero phase.

### IC1-C: matched global summaries with opposite hidden organization

```text
psi_C = A * exp(i*c_plus*x^2)
```

This preserves:

```text
density;
norm;
centroid;
position variance;
mean momentum;
kinetic energy;
absolute chirp magnitude.
```

It reverses the sign of the position-momentum covariance.

### IC1-D: amplitude plus local-current reconstruction

Compute:

```text
rho = |psi_A|^2
j = Im(conj(psi_A) * partial_x psi_A)
local phase gradient g = j/rho
```

inside the frozen support:

```text
rho > 1e-8 * max(rho)
```

Because this known family obeys:

```text
g(x) = 2*c*x
```

estimate:

```text
c_hat = sum(rho*x*g) / (2*sum(rho*x^2))
```

on the support, then reconstruct:

```text
psi_D = A * exp(i*c_hat*x^2)
```

This is a restricted family-specific reconstruction. It is not a general proof that amplitude plus current reconstructs arbitrary multidimensional wavefunctions.

### IC1-E: smooth random-phase, energy-matched null

Construct a smooth random phase from eight low Fourier modes. Remove its density-weighted mean phase gradient, then rescale its phase-gradient energy to match the donor's phase-gradient energy.

This preserves or matches:

```text
density;
norm;
centroid;
position variance;
mean momentum approximately zero;
kinetic energy within frozen numerical tolerance.
```

Its local relational organization is not the donor chirp.

### IC1-F: phase-sign label only

Record `sign(c)` without the local phase field and reconstruct using the declared Gaussian family. This control is intentionally family-specific. It tests whether a compact sufficient coordinate exists after the family is known, not whether a generic image is sufficient.

### IC1-G: energy-matched phase-random null failure fallback

If IC1-E cannot meet its frozen energy and mean-momentum tolerances because of periodic seam or construction artifacts, classify IC1-E as an invalid control. Do not tune its mode count, threshold, or seed after inspecting future outcomes. The primary decision then uses A, B, C, D, and F only.

## 8. Frozen observables

For every carrier at `t = 0` and `t = t_eval`, record:

```text
norm N = integral |psi|^2 dx;
centroid X = integral x*|psi|^2 dx / N;
position variance Vx = integral (x-X)^2*|psi|^2 dx / N;
width W = sqrt(Vx);
mean momentum P = integral Im(conj(psi)*partial_x psi) dx / N;
kinetic energy K = (1/2)*integral |partial_x psi|^2 dx;
position-momentum covariance when full state is available;
```

Compare each carrier with the donor using:

```text
state fidelity F = |integral conj(psi_A)*psi_test dx|^2 / (N_A*N_test);
state infidelity = 1-F;

density NRMSE
    = sqrt(mean((rho_test-rho_A)^2))
      / sqrt(mean(rho_A^2));

width relative error
    = |W_test-W_A| / W_A;

norm drift
    = |N(t)-N(0)| / N(0).
```

State fidelity is global-phase invariant. Density NRMSE is the primary future-image discriminator.

## 9. Frozen acceptance criteria

### 9.1 Initial image equality

For A, B, C, D, E, and F:

```text
initial density NRMSE <= 1e-12
initial norm relative difference <= 1e-12
initial centroid absolute difference <= 1e-10
initial variance relative difference <= 1e-12
```

### 9.2 Matched-scalar opposite-chirp control

For A versus C at `t = 0`:

```text
mean momentum absolute difference <= 1e-9
kinetic energy relative difference <= 1e-9
```

Failure blocks the primary interpretation.

### 9.3 Exact spectral conservation

For every valid carrier and resolution:

```text
norm drift <= 1e-12
```

### 9.4 Analytic width check

For A, B, and C at every resolution:

```text
relative error against analytic width <= 5e-5
```

Failure blocks interpretation until the numerical implementation is corrected without changing scientific thresholds.

### 9.5 Complete-state continuation

IC1-A compared with itself must satisfy machine-level equality. This is a pipeline sanity check, not evidence.

### 9.6 Current reconstruction

IC1-D must satisfy:

```text
|c_hat-c_minus| <= 1e-8
future density NRMSE versus donor <= 1e-8
state infidelity versus donor <= 1e-10
```

Failure means the declared restricted reconstruction is invalid.

### 9.7 Projection-copy rejection

At `t = 3`, both B and C must satisfy:

```text
future density NRMSE versus donor >= 0.10
width relative error versus donor >= 0.50
```

If either matched hidden-state control does not diverge as analytically predicted, the fixture fails.

### 9.8 Energy-matched random-phase control

IC1-E is valid only if at `t = 0`:

```text
|mean momentum| <= 1e-8
kinetic energy relative difference versus donor <= 1e-6
```

If valid, it is expected to satisfy:

```text
future density NRMSE versus donor >= 0.10
```

The primary result does not depend on this expectation.

### 9.9 Resolution sensitivity

For A, B, and C:

```text
maximum width difference between N=512 and N=1024 <= 1e-5
```

The N=256 lane is diagnostic and may be less accurate while still meeting the analytic tolerance.

## 10. Frozen decision table

```text
Outcome O1:
    A and D match;
    B and C share the initial image but diverge strongly in future density;
    analytic and resolution checks pass.
Meaning:
    the fixture supports the observer distinction between projected image and causal state.

Outcome O2:
    B or C does not diverge despite analytic prediction.
Meaning:
    implementation or metric failure; no observer conclusion retained.

Outcome O3:
    D fails while A/B/C pass.
Meaning:
    image insufficiency remains demonstrated, but local-current reconstruction is unsupported under the declared implementation.

Outcome O4:
    E fails construction tolerances while A/B/C/D pass.
Meaning:
    random-phase null is invalid and excluded without replacement in this checkpoint.

Outcome O5:
    analytic or norm checks fail.
Meaning:
    hard stop; no result may inform Lineum.
```

## 11. Independent checks

At least two independent checks are mandatory:

1. compare numerical widths with the analytic Gaussian covariance formula;
2. repeat the spectral evolution at `N = 256, 512, 1024`;
3. verify chirp energy and mean momentum both analytically and numerically;
4. inspect the continuity relation at `t = 0` for the donor:

```text
partial_t rho = -partial_x j
```

using an infinitesimal spectral finite difference only as a diagnostic.

The retained conclusion requires checks 1 and 2. Checks 3 and 4 are supporting diagnostics.

## 12. Frozen executable algorithm

The result version must include the exact executed Python code. The algorithm is frozen as follows:

```python
for N in (256, 512, 1024):
    create periodic grid and spectral wave numbers
    create and discretely normalize Gaussian amplitude
    construct A, B, C
    compute donor local current and family-specific c_hat
    construct D
    construct E from seed 20260801 and modes 1..8
    construct F from the known chirp-sign family coordinate

    for each valid carrier:
        compute t0 observables
        propagate exactly in Fourier space to t_eval=3
        compute future observables and comparisons with donor

    compare A, B, C widths with analytic formula

serialize all scalar results as deterministic JSON-compatible data
```

No plotting choice can affect acceptance. Plots may be produced only as illustrations after scalar decisions are frozen.

## 13. Stop conditions and prohibited tuning

Stop without a retained result if:

- A and C do not match the frozen scalar summaries;
- spectral norm conservation fails;
- analytic width comparison fails;
- N=512 and N=1024 disagree beyond tolerance;
- density NRMSE implementation fails the self-comparison test;
- a threshold or metric definition is ambiguous during execution.

Do not change after outcome inspection:

```text
L;
N values;
sigma;
chirp magnitude;
t_eval;
random seed;
random mode count;
support threshold;
acceptance thresholds;
primary metrics.
```

A later corrected experiment requires a version increment and an explicit reason.

## 14. Root-programme impact matrix

| Root or child branch | Relation before execution | Potential impact if O1 passes |
|---|---|---|
| Minimum-flux observer is non-identifying | `supports` | Adds a known-answer demonstration that a visible movie summary can omit causal phase organization. |
| Exact live-state continuation | `supports` | Clarifies why complete state can reproduce a future that a projection cannot. |
| Static recipe versus live state | `supports` | Provides an independent analytic analogue of morphology without donor state. |
| Copying and heredity negative result | `unaffected` | Does not create a descendant or reopen the exact failed copying implementation. |
| `mu` reduction-first programme | `supports` | Reinforces reconstruction from accessible history or current before adding ontology. |
| Collective-particle hypothesis | `constrains` | A collective image or invariant vector must predict intervention response, not merely shape. |
| P2 vortex-gas remnant | `unaffected` | No P2 data are executed here. |
| Dynamic boundary and source ledgers | `unaffected` | IC1 does not test boundaries or resources. |
| Physical quantum, particle, soul, or ancient-physics mapping | `unaffected` | No correspondence is promoted.

## 15. Reopen triggers

Reopen or supersede this preregistration if:

- an equation or analytic moment formula is found to be incorrect before execution;
- the finite periodic domain materially contaminates the Gaussian at the boundary;
- the current-reconstruction formula is shown to be dimensionally or numerically invalid;
- the random-phase construction cannot define a valid periodic control;
- a stronger known-answer system separates the same observer classes with fewer assumptions.

Any correction after numerical output is inspected must preserve this version in Git history and state which result was invalidated.

## 16. Promotion boundary

This is research-only observer validation.

Do not:

- modify `lineum_core/`;
- modify the Lineum equation;
- add `image`, `spirit`, `pneuma`, `causal soul`, or another interpretation-bearing public API;
- update a whitepaper;
- claim quantum correspondence;
- claim that phase is a soul or that ancient authors described a wavefunction;
- apply the acceptance criteria to P2 without exact P2 package recovery and a separate preregistration.

## 17. Current verdict before execution

```text
fixture_status = preregistered_not_executed
initial_image_sufficiency = analytically_expected_false
matched_global_scalar_sufficiency = analytically_expected_false
complete_complex_state_sufficiency = analytically_expected_true_for_declared_evolution
local_current_family_reconstruction = plausible_untested
energy_matched_random_phase_control = construction_untested
lineum_application = not_authorized
physical_or_metaphysical_correspondence = not_established
next_action = execute_frozen_fixture_once_then_update_this_report_before_any_next_lane
```
