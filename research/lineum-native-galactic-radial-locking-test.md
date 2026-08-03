# Lineum-Native Galactic Radial-Locking Test

**Status:** active  
**Version:** 0.2.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** preregistered dimensionless Lineum-native test on the NGC 3198 radial profile; not a physical gravity or velocity prediction  
**Current confidence:** high that the protocol distinguishes a genuine Lineum-engine response from several obvious construction artifacts; no result has yet been produced  
**Operational task:** ClickUp task `869edcdkk`

## 1. Report lineage and migration record

Root programme report:

- `research/lineum-native-field-stress-tests.md`, version 0.1.0, evidence cutoff 2026-08-04.

This report is the durable Lineum Core version of the preregistered radial-locking protocol originally drafted on 2026-08-04 in a temporary collaboration branch of another repository. The scientific content was moved here because the experiment concerns only Lineum implementation, Lineum observables, public astrophysical data, and Lineum-native controls.

The two collaboration briefs from that branch were intentionally not imported. They are not ancestors, dependencies, or evidence sources for this report. No external private theory, equation, manuscript, or unpublished dataset is reproduced here.

No candidate physics is promoted into the public Core library or whitepapers by this report.

## 2. Central question

Can current Lineum coupled-field dynamics, when initialized only with a radially varying visible-disk profile, generate a robust long-range radial response whose outer proxy is approximately constant, without:

- inserting an explicit `1/r` force law;
- inserting the observed outer rotation curve into the initial state;
- fitting parameters to the outer observed velocities;
- adding a dark-halo term;
- using the external `delta` field in the primary lane;
- choosing the metric or pass threshold after seeing the result?

The first experiment is deliberately dimensionless. A positive result would mean only that a Lineum-native field response with the declared shape emerged in the tested numerical model. It would not establish physical gravity, a prediction in km/s, a replacement for dark matter, or equivalence with another theory.

## 3. Owner constraint

The project owner required that the demonstration show the strength of Lineum itself rather than solve the galaxy problem with an unrelated fitted equation. The primary lane therefore uses the current Lineum update path and its existing fields `psi`, `phi`, `kappa`, and optionally `mu`.

Every consequential step, including negative results and protocol corrections, must be captured continuously in this report.

## 4. Frozen implementation snapshot

Repository: `TomasTriska88/lineum-core`  
Branch: `develop`  
Programme-start commit: `adcec5f65470e90207246724280bacbb77ec0185`  
Primary source file: `lineum_core/math.py`  
Frozen source blob SHA: `bb877021810691223a0eb960a45493a2e351112a`

The primary execution lane uses the NumPy implementation of the current `_step_numpy` semantics.

Relevant implemented operations in the frozen source are:

1. `psi` is a complex field.
2. `phi`, `kappa`, and `mu` are real fields.
3. The primary lane sets `delta = 0`; the galactic profile is encoded only in the initial magnitude of `psi`.
4. With `disable_quantum_noise = True`, probabilistic linon generation and Gaussian fluctuation injection are disabled.
5. The drift contribution is

   `phi_flow_term = drift_strength * (grad(phi)_x + i grad(phi)_y) * kappa * (1 + mu)`,

   followed by a soft magnitude compression.
6. `psi` also receives local interaction, fixed numerical dissipation, and `kappa`-weighted diffusion.
7. With mode coupling enabled, local `|psi|^2` transfers energy into `phi` using `mode_coupling_strength`.
8. `phi` diffuses using the current legacy per-update semantics because `phi_diffusion_scales_with_dt = False` by default.
9. With `use_mu = True`, `mu` accumulates above-threshold `|psi|^2`, decays, and multiplies drift through `1 + mu`.
10. The NumPy path currently subtracts `0.005 * psi * dt` directly; changing the declared `dissipation_rate` field alone does not change this operation. This is an implementation fact and a constraint on later ablations.

## 5. Input data and provenance

Target: NGC 3198.  
Published SPARC distance: 13.8 Mpc.  
Columns: radius, observed velocity, observed-velocity uncertainty, gas contribution, unit-mass-to-light stellar-disk contribution, bulge contribution, stellar-disk surface brightness, bulge surface brightness.

Primary provenance:

- Federico Lelli, Stacy S. McGaugh, and James M. Schombert, “SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves,” *The Astronomical Journal* 152, 157 (2016), DOI: 10.3847/0004-6256/152/6/157.
- Official SPARC data page: https://astroweb.case.edu/SPARC/

The complete numerical input used by this report is reproduced below so the report remains portable.

```text
# Distance = 13.8 Mpc
# Rad Vobs errV Vgas Vdisk Vbul SBdisk SBbul
# kpc km/s km/s km/s km/s km/s L/pc^2 L/pc^2
0.32 24.40 35.90 0.00 63.28 0.00 1084.92 0.00
0.64 43.30 16.30 0.00 73.66 0.00 590.57 0.00
0.96 45.50 16.10 0.00 78.98 0.00 410.97 0.00
1.28 58.50 15.40 0.35 82.70 0.00 329.34 0.00
1.61 68.80 7.61 0.15 84.22 0.00 268.62 0.00
1.93 76.90 10.30 -0.05 83.17 0.00 247.67 0.00
2.24 82.00 8.09 -0.47 87.04 0.00 227.56 0.00
2.57 86.90 7.60 -0.95 88.91 0.00 205.02 0.00
2.89 97.60 3.03 -1.43 88.98 0.00 200.20 0.00
3.21 100.00 5.31 -1.14 93.81 0.00 208.58 0.00
3.54 107.00 7.51 -0.39 101.22 0.00 208.47 0.00
3.85 113.00 7.32 0.36 108.53 0.00 196.07 0.00
4.17 117.00 5.21 1.52 115.51 0.00 179.96 0.00
4.50 119.00 5.67 3.07 120.51 0.00 164.19 0.00
4.82 127.00 5.39 4.63 125.42 0.00 150.99 0.00
5.15 132.00 4.34 6.02 129.40 0.00 138.08 0.00
5.46 134.00 2.36 7.16 133.15 0.00 126.00 0.00
5.78 137.00 0.89 8.31 136.45 0.00 113.63 0.00
6.10 140.00 2.84 9.46 139.41 0.00 101.19 0.00
6.43 142.00 0.88 10.61 141.85 0.00 86.52 0.00
6.74 144.00 1.23 11.77 142.32 0.00 70.23 0.00
7.06 146.00 1.57 12.87 140.94 0.00 57.67 0.00
8.04 147.00 3.00 16.39 135.68 0.00 40.74 0.00
9.04 148.00 3.00 20.03 130.79 0.00 31.83 0.00
10.04 152.00 2.00 23.68 128.10 0.00 26.64 0.00
11.04 155.00 2.00 27.08 126.67 0.00 21.02 0.00
12.05 156.00 2.00 30.11 124.98 0.00 15.42 0.00
14.05 157.00 2.00 34.48 118.12 0.00 6.42 0.00
16.07 153.00 2.00 36.43 108.22 0.00 2.95 0.00
18.13 153.00 2.00 37.76 101.10 0.00 2.39 0.00
20.05 154.00 2.00 39.83 96.40 0.00 1.44 0.00
22.12 153.00 2.00 40.92 91.56 0.00 0.72 0.00
24.03 150.00 2.00 41.77 87.03 0.00 0.28 0.00
26.10 149.00 2.00 43.71 82.67 0.00 0.16 0.00
28.16 148.00 2.00 45.41 79.06 0.00 0.08 0.00
30.08 146.00 2.00 45.29 76.07 0.00 0.04 0.00
32.14 147.00 2.00 44.56 73.27 0.00 0.02 0.00
34.06 148.00 2.00 44.81 70.91 0.00 0.01 0.00
36.12 148.00 2.00 45.90 68.62 0.00 0.01 0.00
38.19 149.00 2.00 46.75 66.59 0.00 0.00 0.00
40.10 150.00 2.00 47.48 64.84 0.00 0.00 0.00
42.17 150.00 3.00 48.93 63.10 0.00 0.00 0.00
44.08 149.00 3.00 47.84 61.63 0.00 0.00 0.00
```

## 6. Primary input construction

The primary lane uses only the stellar-disk surface-brightness column as the radial shape supplied to Lineum. Observed velocities, velocity errors, and baryonic velocity contributions are not used to construct or tune the field.

Construction:

1. Interpolate the non-negative `SBdisk(r)` profile onto the radial coordinate of a square grid.
2. Set values outside the largest tabulated radius to zero.
3. Normalize the interpolated surface brightness by its maximum.
4. Encode the normalized profile as the initial magnitude of `psi` with constant phase zero.
5. Set `phi = 0`, `mu = 0`, `delta = 0`, and `kappa = 1` everywhere.

The first frozen grid is `128 × 128`. The maximum tabulated radius maps to 44 grid cells, leaving a margin between the disk edge and the periodic boundary. This mapping is dimensionless and was chosen before the result is known.

Initial amplitude scale: `0.25`.  
Rationale: this keeps the initial field far below numerical caps while giving the existing mode-coupling channel a measurable signal. It is not fitted to the observed velocity curve.

## 7. Frozen baseline configuration

```text
dt = 1.0
psi_diffusion = 0.05
phi_diffusion = 0.05
drift_strength = -0.004
stencil_type = LAP4
physics_mode_psi = diffusion
disable_quantum_noise = True
phi_diffusion_scales_with_dt = False
use_mode_coupling = True
mode_coupling_strength = 0.001
use_mu = False
psi_amp_cap = 1e6
grad_cap = 1e6
phi_cap = 1e6
kappa = 1 everywhere
delta = 0 everywhere
steps = 2000
```

No parameter in the baseline is fitted to NGC 3198 velocities.

## 8. Preregistered observer

The baseline observer is derived from the radial profile of `phi`, because `phi` is the implemented local reaction and transient-memory channel generated from `|psi|^2`.

At each retained time:

1. Compute the azimuthal mean `phi_bar(r)` in one-cell radial bins.
2. Compute the centered radial derivative `g_phi(r) = |d phi_bar / dr|`.
3. Define a dimensionless circular-response proxy:

   `v_phi(r) = sqrt(r * g_phi(r))`.

This proxy is an observer, not an implemented physical velocity. It asks whether the generated `phi` topography has the radial shape that would correspond to a constant circular speed under the classical relation `v^2 = r g`.

A second, less interpretation-dependent shape diagnostic is preregistered:

- local log-slope of the gradient, `s_g(r) = d log(g_phi) / d log(r)`.

An ideal plateau proxy would have `s_g ≈ -1` over the same radial interval.

## 9. Preregistered evaluation region and metrics

To reduce center discretization and periodic-boundary contamination:

- inner excluded radius: `r < 8` cells;
- primary outer evaluation band: `24 <= r <= 40` cells;
- all cells at `r > 48` are excluded from the primary result.

At the final step and over the final 20% of retained times, report:

1. `plateau_cv`: coefficient of variation of `v_phi(r)` in the primary outer band.
2. `plateau_slope`: ordinary least-squares slope of normalized `v_phi` versus normalized radius in the band.
3. `gradient_log_slope`: median local log-slope of `g_phi` in the band.
4. `temporal_cv`: coefficient of variation of the band-mean proxy over the final 20% of retained times.
5. `radial_signal_ratio`: mean `g_phi` in the outer band divided by the numerical floor plus mean `g_phi` in the excluded far field `48 < r <= 56`.
6. Maximum amplitudes of `psi`, `phi`, and `mu`, plus any fail-safe or cap approach.

## 10. Frozen decision criteria

The baseline may be called a **candidate radial-locking signal** only when all of the following hold:

- `plateau_cv <= 0.10`;
- `abs(plateau_slope) <= 0.15`;
- `-1.25 <= gradient_log_slope <= -0.75`;
- `temporal_cv <= 0.10`;
- the outer-band gradient is at least ten times the floating-point or measured numerical floor in the far field;
- no cap, fail-safe reset, NaN, or comparable instability occurs.

These thresholds classify a simulation shape. They do not validate physical gravity.

## 11. Mandatory controls and interventions

The following order is frozen before execution.

### Lane A: baseline

Current engine, disk in initial `psi`, `phi = 0`, `mu` disabled, no quantum noise.

### Lane B: drift-off control

Identical to Lane A except `drift_strength = 0`.

Purpose: determine whether any retained shape depends on implemented `phi`-gradient feedback rather than only on `phi` being a smoothed record of the initial disk.

### Lane C: coupling-off control

Identical to Lane A except `mode_coupling_strength = 0`.

Purpose: confirm that a non-zero `phi` response requires the implemented `psi -> phi` channel.

### Lane D: shuffled radial-profile control

Randomly permute the tabulated surface-brightness values across their radii before interpolation while preserving the value distribution. Use frozen seed 41.

Purpose: determine whether the result is specific to coherent radial ordering rather than merely the histogram of input amplitudes.

### Lane E: synthetic exponential-disk known-shape control

Replace the SPARC profile by `exp(-r / 8)` with the same amplitude scale and support.

Purpose: determine whether a similar proxy is a generic consequence of diffusion from any centrally concentrated disk.

### Lane F: `mu` intervention

Enable current `mu` with default parameters only after Lanes A–E are recorded.

Purpose: test whether the structural-memory channel strengthens, weakens, destabilizes, or leaves unchanged any baseline response.

## 12. Robustness gates after the first retained result

A baseline signal must not be interpreted beyond `reproduced` until it survives:

- grid sizes 96, 128, and 192 with geometrically equivalent radial mapping;
- `LAP4` and `LAP8` stencils;
- at least one timestep-sensitive comparison that preserves intended update semantics;
- repeated seeded noise-enabled runs only after the deterministic result is known;
- a disk-to-boundary margin change;
- an independently written radial binning and metric implementation;
- explicit check that the periodic image of the disk is not responsible for the outer profile.

## 13. Expected meanings of possible outcomes

### Positive baseline, failed drift-off control

The current Lineum feedback loop contributes causally to the retained shape within the tested numerical domain. Further robustness checks are justified.

### Similar baseline and drift-off profiles

The observer mainly detects passive `phi` smoothing or the initial profile. This is not evidence for a Lineum-native locking mechanism.

### Baseline fails the frozen shape criteria

Current default Lineum dynamics do not produce the preregistered radial-locking proxy under this initialization and parameter regime. This is a bounded negative result, not a universal falsification of all Lineum variants.

### Coupling-off produces a non-zero comparable signal

The runner, observer, or initialization is contaminated or implemented incorrectly. Stop and repair before interpretation.

### Shuffled or synthetic controls perform equally well

The effect is non-specific and likely geometric or numerical rather than a discriminating response to the NGC 3198 disk profile.

### `mu` alone creates a signal absent from baseline

This reopens the structural-memory mechanism as a candidate but does not retroactively validate the baseline or establish physical gravity.

## 14. Known risks registered before execution

- The periodic finite grid can create long-range image interactions.
- `phi` diffusion may mechanically create broad profiles even without drift feedback.
- The velocity-like observer can make some gradient shapes look visually flat; the log-slope and controls are required to reduce this circularity.
- The current NumPy implementation uses a direct fixed dissipation constant rather than the configurable field.
- A one-galaxy result cannot establish universality.
- Surface brightness is not a complete baryonic mass model.
- The simulation is dimensionless and currently lacks a validated conversion to kpc, km/s, gravitational acceleration, lensing, or cosmological observables.

## 15. Root-programme impact matrix before execution

| Root conclusion | Current child status |
|---|---|
| Lineum-native mechanisms must be separated from unrelated fitted equations | supports the frozen design |
| Existing Lineum behaviour should be tested before adding new equation terms | supports |
| No completed Lineum astrophysical forward model exists | unaffected |
| No physical gravity or dark-matter conclusion is currently established | unaffected |
| A bounded falsifiable radial-response test is justified | supports |

## 16. Execution log

No simulation has been executed at version 0.2.0. The next consequential action is Lane A followed immediately by Lane B, with exact runner code and machine-readable outputs to be embedded in this report before any later lane begins.