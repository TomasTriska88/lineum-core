# Lineum Public-TOLOG Three-Question Benchmark — B4

**Status:** active development programme; question 1 observational target validated, question 2 homogeneous saturation phase completed, localized saturation phase preregistered  
**Version:** 0.9.1  
**Evidence cutoff:** 2026-08-04  
**Repository:** `TomasTriska88/lineum-core`  
**Branch at preregistration:** `develop`  
**Branch head at localized-phase preregistration:** `d70c9181bba25e7f7fa968192a44fdfdcdf8f1c3`  
**Scope:** one permanent report answering exactly three public comparison questions by auditing, repairing, implementing, and validating Lineum capabilities; no private TOLOG material; no whitepaper change  
**Question 1 status:** `descriptive_target_validated_but_no_autonomous_emergence_shown`  
**Question 2 status:** `explicitly_stabilized_partial_dissipative_equilibrium_only`  
**Question 3 status:** `no_explicit_scalar_potential_minimum_yet_demonstrated`  
**Confidence:** high for the reported SPARC calculations, static implementation facts, and deterministic homogeneous saturation audit; moderate for source-structure associations; no causal galactic mechanism or fixed-potential attractor established

## Plain result

This report stays anchored to three questions only.

1. Can a grid produce realistic galactic rotation from observable initial conditions without fitting the final curve galaxy by galaxy?
2. Does Lineum stop divergence through a genuine attractor, or through inserted nonlinear bounds, damping, clipping, noise handling, and emergency resets?
3. Does the current complex-plus-auxiliary field system contain, or generate, a real scalar field with a stable potential minimum that preserves information after the original drive is removed?

The current answer is:

- the desired galactic output is tightly characterized, but neither current Lineum nor the publicly reproducible TOLOG description has yet demonstrated blind emergence from source conditions alone;
- current Lineum contains several explicit saturation and numerical safety devices; the first dynamic ablation supports only a partial dissipative `psi` equilibrium under selected homogeneous conditions, not a full natural attractor;
- current Lineum has scalar-valued auxiliary fields, but no explicit independently verified scalar potential minimum has yet been shown to preserve information autonomously.

These are development coordinates, not a terminal verdict. The project-owner objective is to use every bounded failure to identify the missing operation, construct the smallest Lineum-native repair, attack it with ablations and held-out controls, and continue until the three capabilities are implemented and validated within a declared domain. The report is not complete merely because the current engine fails a question.

The report must not become a general galaxy notebook. Every retained calculation below either defines the target for question 1, separates physical from software stabilization for question 2, develops the missing mechanism, or tests persistent scalar memory for question 3.

## Programme objective and owner direction

The project owner clarified on 2026-08-04 that the final purpose of B4 is not to conclude that Lineum cannot answer the three comparison questions. Its purpose is to determine what the current implementation does, identify exactly what is missing, develop a Lineum variant that gains the missing capability, and verify the result adversarially.

Therefore each negative or null result must be converted into a mechanism-development record containing:

1. the exact implementation or regime that failed;
2. the behavior that remained positive;
3. the location of the failure in the equation, state, source, observer, boundary, resolution, or interpretation;
4. at least three distinct repair classes when scientifically plausible;
5. the cheapest frozen discriminator among those repairs;
6. a research-only implementation of the selected candidate;
7. independent verification and ablation;
8. promotion into the engine only after the exact bounded capability is supported.

A question may be closed successfully only when an implemented Lineum variant passes its frozen gates without hiding the target output in its inputs. A current failure may falsify an implementation or regime, but it does not by itself falsify the broader Lineum development programme.

## The three controlling questions

### Question 1 — autonomous astrophysical emergence

Can the grid take only defensible source and initial conditions for a real galaxy and produce its rotation curve without manually fitting galaxy-specific output values? Can it reach a declared agreement target without a dark-matter component and without hiding the observed rotation curve in the inputs?

### Question 2 — natural saturation and divergence control

What exactly stops growth near singular, highly concentrated, or long-running conditions? Is there a stable mathematical attractor comparable to a fixed-potential minimum, or is stability produced by explicit `tanh`, bounded denominators, linear damping, hard caps, clipping, absorbing boundaries, random forcing choices, or fail-safe resets?

### Question 3 — scalar minimum and information persistence

How does the current complex field plus auxiliary fields integrate a real scalar degree of freedom with a stable potential minimum? After a localized state is written and the source is removed, does the state return to a preferred minimum after perturbation, merely decay slowly, require continued driving, or disappear?

## Evidence separation used throughout

Every conclusion must remain in one of these layers:

1. **Current implementation:** what the checked-in code actually computes.
2. **Reproduced observation:** what a frozen executable run actually produced.
3. **Cautious interpretation:** the narrow explanation compatible with the result.
4. **Hypothesis:** an unverified mechanism or analogy.
5. **Known real physics:** what has been connected to external empirical evidence, if anything.

Internal agreement, visual similarity, or a green unit test cannot by itself establish a physical law.

# Question 1 — autonomous galactic emergence

## Publicly reconstructible descriptive target

The publicly described TOLOG-like galactic addition uses a finite saturating radial contribution. For a radius `r`, the frozen reconstruction tested

```text
Vmodel^2(r) = Vbar^2(r) + V0^2 S(k_eff r / 5 kpc)
```

with two baryonic source lanes:

```text
unsigned: Vbar^2 = Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2
signed:   Vbar^2 = sign(Vgas) Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2
```

Five shapes were given equal flexibility:

```text
tanh:        S(x) = tanh(x)
exponential: S(x) = 1 - exp(-x)
rational:    S(x) = x / (1 + x)
arctan:      S(x) = (2/pi) atan((pi/2) x)
algebraic:   S(x) = x / sqrt(1 + x^2)
```

All start at zero, have unit initial slope, and saturate at one. Each receives the same two fitted parameters, amplitude `V0` and scale `k_eff`.

Frozen bounds and starts:

```text
V0 in [0, 400] km/s
k_eff in [1e-6, 100]
V0 starts = [25, 75, 150, 250]
k_eff starts = [0.01, 0.1, 1, 10]
16 starts per shape fit
```

The objective was quoted-error chi-squared. Two-parameter candidates used `AIC = chi2 + 4`; baryons-only used `AIC = chi2`.

## Official SPARC provenance

Input archive:

```text
Rotmod_LTG.zip
SHA-256 = 0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588
profiles = 175
```

Each profile contains radius, observed velocity, quoted velocity uncertainty, gas velocity contribution, disk velocity contribution, bulge velocity contribution, disk surface brightness, and bulge surface brightness.

The earlier mistaken label of the eighth column as gas surface density was corrected before any source-structure calculation. It is `SBbul`. The prior shape fits are unaffected because they used only columns one through six.

## NGC 3198 source-convention result

Literal tabulated stellar `M/L=1` produced:

```text
V0 = 161.2955688 km/s
k_eff = 0.09596754
chi2 = 605.6090070
reduced chi2 = 14.7709514
```

Fiducial stellar weighting produced:

```text
V0 = 132.3866012 km/s
k_eff = 0.52198556
chi2 = 28.06182217
reduced chi2 = 0.68443469
half-saturation radius = 5.26169863 kpc
```

This demonstrates strong source-policy sensitivity. A lower statistic under one stellar calibration is not by itself proof that the physical interpretation is true.

Equal-flexibility shape comparison:

| Shape | Chi-squared | Reduced chi-squared | Delta AIC |
|---|---:|---:|---:|
| `tanh` | `28.061822` | `0.684435` | `0` |
| algebraic | `41.952058` | `1.023221` | `13.890236` |
| exponential | `51.135224` | `1.247201` | `23.073402` |
| arctan | `62.226443` | `1.517718` | `34.164620` |
| rational | `101.042285` | `2.464446` | `72.980463` |

Inside this family, `tanh` lowers chi-squared by about `33.1%` relative to the nearest algebraic competitor. The best `tanh` and algebraic velocity curves differ by at most about `1.66 km/s`; the preference accumulates through many small coherent residuals.

At historical stellar `M/L=1`, algebraic is only about `1.68` AIC units behind `tanh`. Exact curvature preference is therefore calibration-dependent even though the fiducial NGC 3198 result is strong.

## Complete 175-galaxy population census

Frozen informative criteria required:

- at least ten rotation-curve rows;
- the best added shape to improve over baryons-only by at least ten AIC units;
- the winning fit not to touch a frozen parameter boundary.

Both gas-sign lanes produced identical labels and winners among the informative galaxies:

```text
official galaxies                                  175
galaxies with at least 10 rows                     124
informative galaxies                               102
tanh compatible                         82 / 102 = 80.392%
tanh tension                             6 / 102 =  5.882%
tanh strongly rejected                  14 / 102 = 13.725%
tanh exact best                         68 / 102 = 66.667%
median delta AIC tanh                               0
same label under gas-sign handling     102 / 102
same winner under gas-sign handling    102 / 102
```

Winner counts:

| Shape | Wins |
|---|---:|
| `tanh` | `68` |
| rational | `16` |
| algebraic | `10` |
| arctan | `5` |
| exponential | `3` |

Only `32/102` informative curves separated the best and second-best shapes by at least two AIC units. In that shape-identifying subset, `tanh` won `18`, rational `8`, arctan `3`, algebraic `2`, and exponential `1`.

The preregistered universal-support gate required at least `80%` compatibility and at most `10%` strong rejection. Compatibility narrowly passed, but strong rejection reached `13.725%`. The universal-rejection gate also failed. The population classification is therefore:

```text
mixed_population_evidence
```

A broad finite bounded-transition family is descriptively useful. One immutable normalized `tanh` is not universal.

Strong `tanh` wins:

```text
UGC05253, NGC5055, UGC09133, NGC2903, NGC5033, NGC3198
```

Strong rejections:

```text
UGC06787, UGC11914, NGC6015, NGC2403, NGC1003, UGC03205,
UGC02953, UGC08699, NGC0801, NGC2998, UGC06786, NGC5907,
UGC02885, UGC00128
```

## Extreme source-structure contrast

The project owner proposed one mechanism in which one contribution becomes absent, weak, or dominant in some galaxies. A source-only test compared the six strongest `tanh` wins with the fourteen strongest rejections without using the winner or missing-response curve as a feature.

Twelve preregistered source features were tested. Exactly one survived Holm correction:

```text
disk half-light proxy radius / maximum measured radius
```

Result:

```text
direction-agnostic AUC = 0.9047619048
raw exact p            = 0.0033023736
Holm-adjusted p        = 0.0396284830
correctly ordered cross-group pairs = 76 / 84
```

Group medians:

```text
six strong tanh wins:       0.09779
fourteen strong rejections: 0.16589
```

In the selected extremes, strong `tanh` cases have more centrally concentrated luminous disks relative to the measured rotation-curve extent. Simple inner bulge fraction, outer gas fraction, and gas-peak radius did not separate the groups.

This result was independently reconstructed with a second implementation. Maximum feature disagreement was `4.44e-16`; AUC and exact permutation probability agreed exactly. Leave-one-out checks retained AUC at least `0.8857`.

The result was never allowed to establish causation or a population law.

## Population extension of the concentration hypothesis

### Frozen question

Does larger normalized disk half-light radius produce a larger `tanh` penalty continuously across all `102` informative galaxies, and does it predict the fourteen strong rejections after accounting for measurement quality and source controls?

### Inputs

The extension used the verified official SPARC archive and the committed 350-row population decision table:

```text
SPARC archive SHA-256 = 0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588
population CSV SHA-256 = c28423cc6f8b935b8c6b7467966a55fe4bb91cbe5680210897365cf618e10a7d
informative galaxies = 102
```

### Frozen gates

Primary continuous gate:

```text
Spearman rho > 0
and two-sided permutation p <= 0.05
```

Secondary rejection gate:

```text
AUC for larger concentration ratio predicting rejection >= 0.70
and directional permutation p <= 0.05
```

Confound-adjusted support required either a positive significant partial rank association after controlling for quoted fractional error, row count, maximum measured radius, radial-step irregularity, and bulge presence, or repeated cross-validated improvement when concentration was added to those controls.

### Result

The preregistered direction failed.

```text
Spearman rho = -0.2254398887
permutation p = 0.0225597744
observed direction = opposite to preregistration
```

The negative sign means that across the whole population, larger normalized disk half-light radius was associated with a smaller rather than larger `tanh` penalty. That cannot be used as support for the proposed monotonic mechanism because the direction was frozen in advance.

Binary rejection result:

```text
AUC for larger ratio predicting rejection = 0.2759740260
direction-agnostic AUC = 0.7240259740
directional permutation p = 0.9966400336
observed direction = opposite to preregistration
```

After the frozen controls:

```text
partial rank association = -0.1118160246
Freedman-Lane permutation p = 0.2753772462
```

Repeated seven-fold cross-validation over 100 deterministic repeats also did not help. Adding disk concentration improved log loss in only `4/100` repeats:

```text
median control-only AUC = 0.8652597403
median full AUC         = 0.8538961039
median log-loss improvement = -0.0069372364
mean log-loss improvement   = -0.0088618388
```

The full model was generally worse than the measurement-control model.

All fourteen strong rejections occurred in the low- or middle-fractional-error terciles. The highest-error tercile contained no strong rejection. This is consistent with a measurement-identification effect: imprecise curves often cannot distinguish nearby saturation shapes and are therefore less likely to strongly reject anything.

Removing the original fourteen rejections eliminated the continuous association:

```text
remaining n = 88
Spearman rho = -0.0665651434
permutation p = 0.5374546255
```

Classification:

```text
no_population_extension
```

### Independent verification

A second implementation reconstructed all `102` concentration values directly from the official archive, used separate scalar rank and pair-count code, and repeated independent randomization checks.

```text
maximum feature difference = 5.55e-17
Spearman difference         = 0
AUC difference              = 0
independent checker         = passed
```

A complete deterministic rerun reproduced byte-identical primary result and row-table hashes:

```text
full result SHA-256 = a3721fbbf58d0c2ef48849b2d7573041c64589c2137828e1b2fdf3c0a5e39536
rows CSV SHA-256    = fcdb1593f57d8f6da357ac05c5a2b60aae575622b2837ea4326b384186db3cc5
```

### Narrow interpretation

The compact-disk contrast remains true for the selected six-versus-fourteen extremes, but it does not generalize as a one-dimensional monotonic population rule.

This is a decision-relevant negative result. It rejects only the simple statement:

> larger normalized disk half-light radius directly and monotonically worsens `tanh` across all informative galaxies.

It does not reject:

- nonlinear or threshold behavior;
- interactions with inclination, distance, radial coverage, stellar calibration, or measurement precision;
- source projection through a nonlocal response;
- one mechanism with several terms;
- multiple physical regimes.

Because the denominator is the farthest measured rotation-curve point rather than a physical edge, observer and measurement geometry remain material alternative explanations.

## Question 1 verdict and development target

### Current implementation

The current Lineum engine has not yet been supplied only with a galaxy's independently observable baryonic source conditions and asked to predict the rotation curve blindly.

### Reproduced observation

A two-parameter finite saturating addition describes many SPARC galaxies well. `tanh` is the leading tested shape but is not exact and universal.

### Interpretation

The target for a future emergent mechanism is constrained: it must commonly produce `tanh`-like finite transitions, produce systematic non-`tanh` exceptions, and explain which source or observer variables select the curvature.

### Hypothesis

A shared grid mechanism may project differently through different source geometries or may change regime when a transport, screening, leakage, memory, or coupling contribution becomes weak or dominant.

### Development completion condition

Question 1 is not closed by recording that blind prediction is absent. It requires a research variant that accepts only independently observable source conditions, freezes universal parameters before held-out evaluation, and predicts held-out rotation curves without using their observed velocities during calibration.

### Not established

Neither Lineum nor the publicly reproducible TOLOG material has yet demonstrated the full chain:

```text
independently observed galaxy source
-> grid dynamics with frozen universal parameters
-> blind rotation-curve prediction
-> declared agreement on held-out galaxies
```

A fitted macroscopic formula is not autonomous emergence.

# Question 2 — natural saturation and divergence control

## Current implementation audit

The checked-in `lineum_core/math.py` defines these relevant default configuration values:

```text
dt = 1.0
psi_diffusion = 0.05
phi_diffusion = 0.05
dissipation_rate = 0.005
reaction_strength = 0.0007
noise_strength = 0.005
drift_strength = -0.004
mode_coupling_strength = 0.001
psi_amp_cap = 1e6
grad_cap = 1e6
phi_cap = 1e6
mu_cap = 10
fold_mode = softabs
fold_scope = escape
```

The implementation contains several distinct bounded or stabilizing operations. They must not be conflated into one natural attractor.

### A. Inserted bounded nonlinearities

1. Linon probability uses a logistic sigmoid.
2. The local interaction coefficient uses explicit `tanh`:

```text
interaction_factor = 0.1 * tanh(0.04 * clipped_phi * kappa * (1 + mu) / 0.1)
```

3. The interaction term is further bounded by

```text
interaction_term /= 1 + |interaction_term| / 10
```

4. The phi-gradient flow term is bounded by the same denominator form.

These are explicit mathematical saturation choices. A bounded result from them is not evidence that the grid discovered `tanh` or a saturation law emergently.

### B. Linear or transfer damping

1. In NumPy diffusion mode and PyTorch diffusion mode, the code applies

```text
psi -= 0.005 * psi * dt
```

2. With mode coupling enabled, energy is moved from `psi` into `phi`:

```text
delta_e = mode_coupling_strength * |psi|^2 * kappa * dt
phi += delta_e
|psi| -> sqrt(max(|psi|^2 - delta_e, 0))
```

3. Optional `mu` decays linearly through `mu_rho`.
4. Projected wave modes can add edge damping and a perfectly matched absorbing boundary layer.

These may create dissipative steady states, but a dissipative steady state is not automatically a fixed potential minimum.

### C. Hard numerical guards

1. `psi` amplitude is capped at `psi_amp_cap`.
2. gradients are clipped at `grad_cap`.
3. `phi` is clipped or folded around `phi_cap`.
4. `mu` is clipped at `mu_cap`.
5. if `psi` becomes NaN or approaches `99%` of its amplitude cap, the complete `psi` field is reset to zero.

These are explicitly labelled numerical guards or fail-safes in the code. Stability that requires them is numerical containment, not a demonstrated physical attractor.

### D. Stochastic driving

Unless `disable_quantum_noise` is true, the diffusion path contains probabilistic linon generation and Gaussian fluctuation forcing. Noise can seed or maintain activity, but random forcing cannot be used as evidence that noise is the mechanism that stops divergence unless an intervention demonstrates that claim.

## Configuration contradiction discovered

`CoreConfig` exposes

```text
dissipation_rate = 0.005
```

but the current diffusion update does not read `cfg.dissipation_rate`. It uses the literal constant `0.005` in both NumPy and PyTorch diffusion paths.

Consequences:

- changing `CoreConfig(dissipation_rate=...)` does not currently perform the intended dissipation ablation in diffusion mode;
- tests or reports that assume this parameter controls damping may be misleading;
- a research-only shadow step or a later tested engine correction is required to separate zero, default, and enhanced damping.

This is an implementation fact, not yet a production-code change.

## Analytic homogeneous-cell sanity check

Consider a deterministic homogeneous region with no spatial gradients, `kappa=1`, `mu=0`, noise disabled, and mode coupling enabled.

For small amplitude, the local interaction contributes approximately

```text
a(phi) = 0.1 * tanh(0.4 * clip(phi, 0, 10))
```

while the hard-coded linear damping removes approximately `0.005 psi` per unit time and mode coupling removes an additional small fraction of `psi` energy.

Near `phi=0`, `a(phi)=0`, so small `psi` decays. Once `phi` rises above a small positive threshold, the explicit interaction can overcome linear damping. At large amplitude, the downstream denominator makes the interaction approach a finite additive drive while linear damping continues to grow with amplitude. This combination can create a finite dissipative equilibrium.

That equilibrium, if reproduced, would be caused by the inserted bounded interaction plus damping and energy transfer. It would not yet demonstrate an independently derived scalar potential minimum.

Meanwhile, default mode coupling continually adds non-negative energy to `phi`. In a homogeneous driven state, `phi` has no explicit local decay term in that branch and can continue toward the hard `phi_cap` unless diffusion or geometry exports it. A `phi` value stopped by the cap is not a natural minimum.

## Frozen dynamic saturation audit

### Question

Which operations are necessary and sufficient for bounded long-run behavior in the current Lineum update, and does any state return to the same finite attractor after perturbation without relying on stochastic forcing, hard clipping, or fail-safe reset?

### Scope

- research-only runner outside the installable package;
- no production engine change;
- NumPy diffusion path first because it is deterministic, directly inspectable, and does not require GPU behavior;
- PyTorch wave modes remain a separate later lane only if the diffusion result leaves the question unresolved.

### Initial states

Two frozen families:

1. **Homogeneous cells:** constant complex `psi` magnitude `0.01`, constant `kappa=1`, `mu=0`, and initial `phi` in `{0, 0.05, 0.15, 1, 10}`.
2. **Localized source:** centered Gaussian `psi` with peak `1`, `phi` in `{0, 1}`, `kappa=1`, zero `mu`, on grids `{32, 64, 128}`.

Frozen time steps:

```text
dt in {0.1, 0.5, 1.0}
```

Primary duration:

```text
5000 updates
```

A shorter fail-fast run may stop a lane only after NaN, reset, or cap dependence is recorded.

### Frozen lanes

1. **Current deterministic baseline:** quantum noise and linon generation disabled; all other default diffusion operations retained.
2. **Stochastic baseline:** current defaults, fixed seeds.
3. **Dissipation-parameter invariance control:** `dissipation_rate=0`, `0.005`, and `1`; expected identical output under current implementation. This verifies the configuration contradiction.
4. **No hard amplitude guards:** research shadow step with very high caps and fail-safe reset disabled, while preserving the equation otherwise.
5. **No linear dissipation:** research shadow step replacing the hard-coded `0.005` by zero.
6. **No explicit `tanh`:** research shadow step replacing the interaction coefficient by its linear small-signal form while retaining the downstream bounded denominator.
7. **No interaction denominator:** retain `tanh` but remove the `1 + |term|/10` bounding denominator.
8. **No mode-coupling transfer:** use the existing fallback reaction lane.
9. **No `phi` cap/fold:** research shadow step with unbounded diagnostic `phi` and no overflow fold.
10. **Noise-only zero-state control:** zero `psi`, zero `phi`, default stochastic forcing.

Each research-shadow modification changes one operation at a time. Combined removals are prohibited until single-operation ablations are recorded.

### Observables

For every lane and seed:

- mean and maximum `|psi|^2`;
- maximum `|psi|`;
- minimum, mean, and maximum `phi`;
- `mu` range if enabled;
- cap, fold, and fail-safe reset counts;
- NaN or infinity occurrence;
- last-20%-window slope of mean energy;
- last-20%-window coefficient of variation;
- dominant oscillation amplitude where applicable;
- distance between pre-perturbation and recovered state.

### Perturbation test

After an apparent stationary state, multiply a centered region of `psi` by `1.5` and reduce a neighboring region by `50%`. Continue for another `1000` updates.

A return to the previous state requires both:

```text
relative mean-energy difference <= 5%
relative radial-profile L2 difference <= 10%
```

The target must be the pre-perturbation state from the same lane, not a post-hoc fitted template.

### Classification gates

`hard_guard_dependent` if removing caps or reset changes a bounded baseline into cap approach, NaN, infinity, or unbounded positive tail slope.

`explicit_nonlinearity_dependent` if removing `tanh` or the interaction denominator destroys the bounded state while hard guards remain inactive in the baseline.

`dissipation_dependent` if removing linear damping destroys the bounded state while the explicit nonlinearities remain.

`mode_transfer_dependent` if disabling mode coupling materially changes boundedness or recovery.

`noise_not_required` if the deterministic baseline remains bounded and recovers without stochastic forcing.

`noise_required_for_activity` if the deterministic zero or small state decays but stochastic forcing sustains a bounded active state.

`dissipative_attractor_supported` only if a finite state remains bounded without hard-guard activation, is stable across the frozen `dt` and grid sizes, and returns after perturbation.

`fixed_potential_attractor_not_shown` remains the default unless a separately defined scalar potential and its minimum explain the recovery quantitatively.

### Prohibited interpretation

Even a successful dissipative attractor would show stability of this implementation under the tested conditions. It would not prove that nature uses the same mechanism, that a galactic singularity is solved, or that TOLOG's Dark Heart has been reproduced.

## Homogeneous saturation phase result

### Executed scope

The first phase reduced the current deterministic NumPy diffusion update to a spatially homogeneous cell:

```text
kappa = 1
mu = 0
delta = 0
all spatial gradients = 0
diffusion contribution = 0
quantum noise and linon generation = disabled
initial |psi| = 0.01
```

The reduction retained the same local interaction, hard-coded linear damping, mode-coupling transfer, `phi` handling, and guards as the current implementation unless one declared operation was ablated.

Frozen grid sizes, time steps, and initial `phi` values were:

```text
grid sizes = {32, 64, 128}
dt = {0.1, 0.5, 1.0}
phi0 = {0, 0.05, 0.15, 1, 10}
5000 primary updates
1000 post-perturbation recovery updates
```

Nine single-operation lanes produced `405` retained runs:

```text
baseline
configured dissipation = 0
configured dissipation = 1
no hard guards
no linear dissipation
no explicit tanh
no interaction denominator
no mode coupling
no phi cap
```

The perturbation multiplied the homogeneous `psi` amplitude by `1.5`. Recovery required the final energy to return within `5%` of the same lane's pre-perturbation state. A radial-profile test is impossible in a homogeneous reduction and remains reserved for the localized phase.

### Reproduced results

The configured dissipation parameter was exactly inert:

```text
maximum difference among configured rates 0, 0.005, and 1 = 0
```

This confirms dynamically, not only statically, that `CoreConfig.dissipation_rate` does not currently control the diffusion damping term.

Baseline outcomes across all `45` homogeneous combinations were:

```text
decayed to zero = 6
decaying        = 12
growing         = 21
stationary      = 6
```

All six stationary baseline cases were the `dt=1` high-`phi` lanes (`phi0` equal to `1` or `10` across three nominal grid sizes). They returned after perturbation with relative energy error about:

```text
0.00536 = 0.536%
```

They triggered no `psi` fail-safe reset. Their finite `psi` equilibrium was approximately:

```text
|psi| = 1708.90035
```

but their `phi` value reached the hard cap:

```text
phi = 1,000,000
```

Therefore these rows show recovery of one bounded `psi` component while the full state is cap-supported.

Removing the downstream interaction denominator caused every high-`phi` lane to hit the guard reset:

```text
18 / 18 high-phi runs reset
```

The denominator

```text
1 + |interaction_term| / 10
```

is therefore necessary for bounded high-`phi` behavior in this tested homogeneous regime.

Removing explicit `tanh` did not remove all finite stationary `psi` states:

```text
stationary high-phi rows without tanh = 6
maximum final |psi| without tanh = 1788.57180
```

Thus the explicit `tanh` is not individually necessary for a finite homogeneous `psi` equilibrium while the denominator, damping, transfer, cap, and guards remain.

Removing the hard-coded linear dissipation produced no successful high-`phi` recovery within the frozen horizon:

```text
recovery passes = 0 / 18
maximum final |psi| = 18106.61161
```

This supports linear-dissipation dependence for timely recovery under the tested conditions. It does not prove mathematical divergence at infinite time.

Removing the `phi` cap left `psi` broadly finite under the tested horizon but exposed monotonic `phi` accumulation:

```text
maximum final phi = 13,402,932.35238
minimum positive late-time phi slope = 121.18393 per update
```

No homogeneous uncapped `phi` fixed point was observed. The apparent full-state stationarity of the capped baseline is therefore not a natural fixed minimum of `phi`.

### Independent verification and preserved failure

A second implementation reconstructed the homogeneous scalar recurrence independently, using amplitude-only scalar arithmetic and not importing the primary runner.

It reproduced all `405` rows:

```text
exact categorical mismatches = 0
maximum numeric relative difference = 1.12e-14
configured-dissipation invariance = passed
high-phi denominator instability = passed
uncapped-phi positive-tail check = passed
overall independent check = passed
```

The first version of the independent checker failed and is retained permanently. It incorrectly required every `dt` lane to reach its analytic asymptote within the frozen `5000`-step horizon:

```text
baseline maximum fixed-point relative error = 0.1435
no-dissipation maximum fixed-point relative error = 0.8312
linearized-interaction maximum fixed-point relative error = 0.0784
```

Those values reflect finite-time convergence, not disagreement with the independently reconstructed recurrence. The checker was corrected to test the frozen run itself, the declared classifications, and analytically valid directional controls rather than imposing an unregistered convergence deadline.

A complete primary rerun was byte-identical to the first retained result.

### Question 2 interim classification

```text
explicitly_stabilized_partial_dissipative_equilibrium_only
```

The evidence supports a finite and perturbation-recovering `psi` equilibrium in a narrow subset of homogeneous conditions. It also shows that:

- the interaction denominator is essential in the tested high-`phi` regime;
- the hard-coded linear damping is important for recovery within the frozen horizon;
- explicit `tanh` is not individually essential for finite homogeneous `psi`;
- `phi` has no demonstrated uncapped homogeneous fixed point;
- the exposed dissipation parameter is not wired to the implemented damping;
- a full fixed-potential attractor is not shown.

The homogeneous reduction contains no spatial gradients, diffusion, localization, radial profile, boundary interaction, or stochastic forcing. The preregistered localized phase remains necessary before question 2 can be closed.

## Localized spatial phase preregistration

### Development question

Can spatial transport and neighbour coupling turn the partial homogeneous `psi` equilibrium into a localized, perturbation-recovering full state without hard `phi` containment? Does the eight-neighbour 3x3 stencil add a reproducible stabilizing or isotropy advantage over the four-neighbour stencil?

### Source snapshot and implementation boundary

The research runner must embed a frozen reference update derived from:

```text
lineum_core/math.py Git blob = bb877021810691223a0eb960a45493a2e351112a
```

It must not modify or import a mutable production implementation as its sole reproduction path. The exact current NumPy diffusion order, coefficients, periodic `np.roll` boundary convention, explicit interaction, damping, diffusion, mode transfer, `phi` diffusion, caps, and reset must be represented. One operation may be changed per declared ablation.

### Stage L1 screening domain

The first retained spatial step is intentionally small and frozen before result inspection:

```text
grid size = 32 x 32
dt = 1.0
primary updates = 5000
recovery updates = 1000
stencils = {LAP4, LAP8}
initial phi = {0, 1}
kappa = 1 everywhere
mu = 0 everywhere
delta = 0 everywhere
quantum noise and linon generation = disabled
```

Initial `psi` is a centered real Gaussian with peak magnitude `1` and standard deviation `3` cells:

```text
psi(x,y) = exp(-(x^2 + y^2) / (2 * 3^2))
```

The field is placed far enough from the periodic boundary that initial wrap-around is negligible. This stage tests the checked-in cell-scale dynamics and boundary interaction; it is not yet a continuum-limit claim.

Frozen single-operation lanes:

```text
baseline
no hard guards
no linear dissipation
no explicit tanh
no interaction denominator
no mode coupling
no phi cap
```

Total retained L1 runs before any fail-fast termination:

```text
2 stencils * 2 phi starts * 7 lanes = 28
```

### Perturbation

After 5000 updates:

- multiply `psi` inside radius `2` cells by `1.5`;
- multiply `psi` in the neighbouring annulus from radius `3` through `5` cells by `0.5`;
- preserve phase;
- do not alter `phi` directly;
- continue for 1000 updates.

The pre-perturbation state of the same lane is the only recovery target.

### Spatial observables

For every run record:

- total and mean `psi` energy;
- maximum `|psi|`;
- minimum, mean, and maximum `phi`;
- late-window energy and `phi` slopes and coefficients of variation;
- reset, cap, and non-finite events;
- energy fraction within radii `3`, `6`, and `10` cells;
- energy half-radius;
- centre-of-energy displacement;
- radial profiles of `|psi|^2` and `phi` using fixed integer-radius bins;
- fourfold angular anisotropy of `|psi|^2`, where zero is rotationally uniform and larger values indicate square-grid imprint;
- post-perturbation energy, radial-profile, half-radius, and centre recovery errors.

### L1 gates

`localized_psi_recovery` requires:

```text
no reset or non-finite event
relative total-energy recovery error <= 5%
relative radial-profile L2 error <= 10%
absolute half-radius change <= 1 cell
centre displacement after recovery <= 0.5 cell
```

`localized_full_state_recovery` additionally requires:

```text
no phi-cap hit
relative phi radial-profile L2 error <= 10%
late phi slope <= max(1e-10, 1e-8 * abs(late phi mean)) per update
```

`spatial_transport_resolves_phi` requires the uncapped-phi lane to remain finite, avoid a persistent positive late-time `phi` slope, and recover its pre-perturbation `phi` profile.

`lap8_specific_stabilization` requires LAP8 to pass `localized_full_state_recovery` while the paired LAP4 run fails, without relying on a reset or cap, and with lower fourfold anisotropy.

`stencil_not_decisive_in_L1` applies when paired LAP4 and LAP8 runs receive the same boundedness and recovery classification and neither has a material advantage larger than ten percentage points in radial recovery or anisotropy.

A candidate that passes L1 must proceed to the already frozen `dt` values `{0.1, 0.5, 1.0}` and grids `{32, 64, 128}` before any stable-attractor claim. L1 failure is not a terminal programme verdict; it activates the repair map below.

### Repair map if the current spatial system fails

The following candidate classes are registered before execution:

1. **Transport repair:** current `phi` diffusion or boundary export is insufficient; test a conservative flux or physically scaled diffusion without a local hard cap.
2. **Bidirectional exchange repair:** mode coupling deposits energy into `phi` one way; test a reversible or detailed-balance exchange between `psi` and `phi`.
3. **Local relaxation repair:** add the smallest explicit return term for `phi`, first as a linear leakage control and then as a potential-derived force.
4. **Existing-field feedback repair:** test whether `mu`, dynamic `kappa`, or the existing foam/topology can provide state-dependent release without a new fundamental field.
5. **Potential-minimum repair:** only if existing ingredients cannot produce the required observable, introduce a research-only scalar potential candidate with declared minima and energy accounting.
6. **Localization repair:** if every bounded state simply disperses, test a conservative nonlinear localization term separately from saturation.
7. **Boundary and scaling repair:** if results change qualitatively with stencil, domain, or time step, correct discretization and physical scaling before interpreting a mechanism.

The cheapest next discriminator will be selected from the exact L1 failure location. No blind parameter sweep or unrestricted hybrid is permitted.

### Prohibited interpretation

L1 can identify what the current spatial implementation does and which operation is necessary under the tested cell-scale conditions. It cannot establish a physical 3x3 elementary cell, continuum convergence, a galactic attractor, or a TOLOG Dark Heart mechanism.

# Question 3 — scalar minimum and information persistence

## Current implementation audit

The current state includes:

- complex `psi`;
- real scalar arrays `phi`, `kappa`, and optional `mu`;
- external scalar `delta` when supplied.

A scalar-valued array is not automatically a scalar field with a fixed potential minimum.

No explicit local potential of the form

```text
V(q) with dV/dq = 0 at a declared stable minimum
```

has yet been identified and validated as the persistence mechanism for `phi`, `kappa`, or `mu` in the current update.

Observed implementation roles:

- `phi` accumulates transferred `psi` energy or relaxes toward `|psi|^2` in the fallback branch, diffuses, and is clipped or folded;
- `kappa` is read as a permeability or mask and is not dynamically evolved by `step_core`;
- `mu` accumulates selected `psi` energy, decays linearly, and is capped;
- none of those facts alone establishes a stable information-bearing potential minimum.

## Current classification

```text
no_explicit_scalar_potential_minimum_yet_demonstrated
```

## Later frozen destructive memory test

This test will begin only after question 2 identifies which stabilization operations are active.

1. write a localized state using a frozen source;
2. remove the source completely;
3. run without stochastic forcing;
4. apply positive and negative local perturbations;
5. compare decay, recovery, relocation, and destruction;
6. repeat across grid size and time step;
7. distinguish a stable minimum from slow relaxation or hard clipping.

A memory claim requires persistence without continued source input and recovery toward a predeclared state after perturbation. Slow decay alone is not a stable potential minimum.

Question 3 is not closed by documenting that the current field lacks a demonstrated minimum. The development target is a smallest-ingredient Lineum mechanism that stores a localized state after source removal, returns toward a declared state after perturbation, and passes destructive controls without continued driving or hard clipping.

# Root-programme impact

| Statement | Current impact |
|---|---|
| Finite saturating addition is useful for NGC 3198 | `supports` |
| Exact `tanh` is preferred on fiducial NGC 3198 | `supports` |
| Exact normalized `tanh` is universal across galaxies | `contradicts` within tested family |
| Broad bounded-transition family is common | `supports` descriptively |
| Disk concentration alone monotonically controls population `tanh` penalty | `contradicts` under frozen extension |
| Observer and measurement geometry are irrelevant | `contradicts` as an allowed assumption |
| Lineum currently predicts galactic rotation blindly | `not_yet_supported`; development target remains active |
| Public TOLOG evidence reproduces blind 98% emergence | `not_yet_supported` from public reproducible material |
| Lineum stability is purely emergent | `contradicts` in the homogeneous tested regime; explicit denominator, damping, cap, and guards materially shape the result |
| A partial dissipative `psi` equilibrium exists | `supports` for six high-`phi`, `dt=1` homogeneous lanes only |
| Current Lineum has a proven fixed potential attractor | `contradicts` as a conclusion from the homogeneous phase; repair programme remains active |
| Current Lineum has a proven persistent scalar minimum | `not_yet_supported`; development target remains active |
| A 3x3 neighbourhood is uniquely required | `not_yet_supported`; L1 comparison preregistered |
| B4 is intended only to judge the present engine | `contradicts`; B4 is an audit-repair-validation programme |

# Retained artifacts and reproduction

## Population shape census

Committed tools:

- `research/runners/lineum_b4_sparc_population_shape_census.py`
- `research/runners/lineum_b4_sparc_population_fit_batch.py`
- `research/runners/lineum_b4_sparc_population_finalize.py`
- `research/runners/lineum_b4_sparc_population_summary_check.py`

Committed outputs:

- `research/results/lineum_b4_sparc_population_shape_census_summary.json`
- `research/results/lineum_b4_sparc_population_shape_census.csv.xz.b64`

Expected result:

```text
classification = mixed_population_evidence
informative = 102
tanh compatible = 82
tanh strongly rejected = 14
tanh best = 68
```

## Extreme source discriminator

- `research/runners/lineum_b4_source_structure_discriminator.py`
- `research/runners/lineum_b4_source_structure_check.py`
- `research/results/lineum_b4_source_structure_discriminator.json`

Expected result:

```text
classification = simple_source_separator_supported
winning feature = disk_half_light_r_over_rmax
AUC = 0.9047619048
Holm-adjusted p = 0.0396284830
```

## Population concentration extension

- `research/runners/lineum_b4_population_concentration_extension.py`
- `research/runners/lineum_b4_population_concentration_check.py`
- `research/results/lineum_b4_population_concentration_summary.json`
- `research/results/lineum_b4_population_concentration_result.json.xz.b64`
- `research/results/lineum_b4_population_concentration_rows.csv.xz.b64`

Artifact SHA-256 values:

```text
primary runner       8b136f41377a275e3087a76081839157047abbcabb0efa2b6cc6e6cf31690df0
independent checker  4c63528f3affdf22d088a825fc48acad50e6af7d6f9bf32caa7070047d394b4d
full result JSON     a3721fbbf58d0c2ef48849b2d7573041c64589c2137828e1b2fdf3c0a5e39536
full result XZ+B64   55550f4302c8f570aaebe22cab0250942b0967873ed20e314f906c837384f8bd
rows CSV             fcdb1593f57d8f6da357ac05c5a2b60aae575622b2837ea4326b384186db3cc5
rows XZ+B64          44cb6c09c13b11df608093dcac803144132b4d7807670a16dd915fab9be63799
```

Minimal reproduction:

```bash
python research/runners/lineum_b4_population_concentration_extension.py \
  --archive Rotmod_LTG.zip \
  --population-table-b64 research/results/lineum_b4_sparc_population_shape_census.csv.xz.b64 \
  --output population_concentration_result.json \
  --table population_concentration_rows.csv

python research/runners/lineum_b4_population_concentration_check.py \
  --archive Rotmod_LTG.zip \
  --population-table-b64 research/results/lineum_b4_sparc_population_shape_census.csv.xz.b64 \
  --result population_concentration_result.json \
  --output population_concentration_check.json
```

Expected result:

```text
classification = no_population_extension
Spearman rho = -0.2254398887
primary direction pass = false
rejection AUC in preregistered direction = 0.2759740260
adjusted association p = 0.2753772462
independent checker = passed
```

## Homogeneous saturation audit

- `research/runners/lineum_b4_saturation_homogeneous_audit.py`
- `research/runners/lineum_b4_saturation_homogeneous_check.py`
- `research/results/lineum_b4_saturation_homogeneous_summary.json`
- `research/results/lineum_b4_saturation_homogeneous_result.json.xz.b64`
- `research/results/lineum_b4_saturation_homogeneous_check.json`
- `research/results/lineum_b4_saturation_homogeneous_initial_failed_check.json`

Source implementation:

```text
lineum_core/math.py Git blob = bb877021810691223a0eb960a45493a2e351112a
```

Local pre-transport SHA-256 values:

```text
primary runner        a7fc18d0fe2f921473bf50580807dc39df0861d6f02f979ee745f3e78d7ed478
corrected checker     91a35e01018fbe2f829677b1db6648252c751969dd8040b613b1774f866d4eee
full result JSON      f7cdfaa0cdbbca87d4f6f1d832fb53d57c54a187f920b39de8eb04d806940f39
full result XZ+B64    9a54eb142561216348917abbe43653d6265140d6c7e167706820d13fb71db15a
corrected check       598ea3dc84665c2d56a8b45bb93e56d11a85cbf74105775aabee6b6f717b8608
summary JSON          6d9797ec464e769ecfc3a86f44d7f5eca69c5a2def23297a70a942574477f29f
```

Minimal reproduction:

```bash
python research/runners/lineum_b4_saturation_homogeneous_audit.py \
  --output homogeneous_saturation_result.json

python research/runners/lineum_b4_saturation_homogeneous_check.py \
  --result homogeneous_saturation_result.json \
  --output homogeneous_saturation_check.json
```

Expected interim result:

```text
question_2_interim = explicitly_stabilized_partial_dissipative_equilibrium_only
rows = 405
configured dissipation maximum difference = 0
stationary high-phi baseline rows = 6
high-phi no-denominator resets = 18 / 18
stationary high-phi no-tanh rows = 6
uncapped phi has positive late-time slope
independent checker = passed
```

# Numerical and environment limitations

The original population fits used:

```text
Python 3.13.5
NumPy 2.3.5
SciPy 1.17.0
```

The repository declares NumPy below `2.0`. Independent reconstruction and alternative checks reduce but do not erase that mismatch. A rerun in a repository-supported NumPy environment remains desirable.

The population concentration extension additionally used scikit-learn `1.8.0`. Its principal rank, permutation, and independent-check results do not depend on the cross-validation model.

The homogeneous deterministic phase of the question-2 audit is complete. It used Python `3.13.5` and NumPy `2.3.5`, but the independently checked recurrence is scalar and does not depend on SciPy, scikit-learn, PyTorch, or GPU behavior. The localized spatial phase must record its own environment and remains subject to a repository-supported NumPy rerun if executed under NumPy 2.x.

# Prohibited conclusions

This report does not establish:

- a universal galactic `tanh` law;
- autonomous 98% galactic emergence in Lineum or TOLOG;
- absence of dark matter;
- modified gravity;
- a physical 3x3 elementary cell;
- a TOLOG Dark Heart derivation;
- an emergent `tanh` from current Lineum code;
- a natural Lineum attractor independent of inserted bounds;
- a stable scalar potential minimum;
- a persistent information field;
- that disk concentration causes the observed shape family;
- that a lower chi-squared identifies physical truth;
- that current implementation failures are terminal limits on future Lineum development.

# Version history

- `0.1.0`: froze and executed the NGC 3198 equal-flexibility test.
- `0.2.0`: opened the early-Lineum threshold audit.
- `0.3.0`: reconstructed the supplied staircase as quantized linear rendering; original dynamics remained provenance-blocked.
- `0.4.0`: preregistered the complete SPARC population census.
- `0.5.0`: completed the population census; `mixed_population_evidence`.
- `0.6.0`: recorded the owner's one-mechanism-with-weak-or-absent-term hypothesis and preregistered the extreme source discriminator.
- `0.6.1`: corrected `SBdisk` and `SBbul` provenance before source execution.
- `0.7.0`: completed the extreme source discriminator; compact disk association supported inside the selected contrast.
- `0.8.0`: reorganized the single report around the three controlling questions; completed the all-102 population concentration extension as `no_population_extension`; recorded observer/measurement confounding; opened and preregistered the question-2 saturation audit; documented the unused `dissipation_rate` configuration contradiction.
- `0.9.0`: completed and independently checked the homogeneous deterministic saturation phase; retained the initial checker failure; classified question 2 provisionally as `explicitly_stabilized_partial_dissipative_equilibrium_only`; localized spatial phase remained pending.
- `0.9.1`: recorded the owner's audit-repair-validation objective; made current failures explicitly non-terminal; preregistered the L1 localized LAP4/LAP8 screening and its repair map before execution.
