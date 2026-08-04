# Lineum Label-Retention P1 Preflight

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** one-pair deterministic preflight for the current-engine Q3 label-retention protocol  
**Central question:** does one representative equal-energy orientation pair complete imprint and clean source removal with numerically valid `phi` and `mu` traces whose passive evolution matches the preregistered implementation expectations?  
**Current confidence:** high in the frozen procedure; no result exists at version `0.1.0`

## 1. Report lineage

Root programme:

- report: `research/lineum-native-field-stress-tests.md`;
- inherited version: `0.2.2`;
- commit: `82e2245ca1e32414678189ffeb2ed976dc5ddbc2`;
- scope lock: only Q1 galactic response, Q2 attraction/saturation, Q3 information retention, and their connection to real-universe observables are active scientific goals.

Immediate protocol:

- report: `research/lineum-current-engine-label-retention-test.md`;
- inherited version: `0.1.0`;
- commit: `11e08efd53cfcc22072a7301107b30b91bb73df5`;
- frozen engine blob: `bb877021810691223a0eb960a45493a2e351112a`.

Observer preflight:

- report: `research/lineum-label-retention-p0-observer-audit.md`;
- commit: `027e321e30bcd54fe717b54bd2e68499248a0437`;
- result: both observers separated the pristine known-answer family in NumPy `2.3.5`, but the old repository NumPy `<2.0.0` environment condition prevented an official P0 pass.

Repository checkpoint before this report:

- repository: `TomasTriska88/lineum-core`;
- branch: `develop`;
- expected head: `82e2245ca1e32414678189ffeb2ed976dc5ddbc2`.

## 2. Owner scope and runtime boundary

The project owner directed that dependency work remain supporting infrastructure only. This preflight therefore does not open a separate library-modernization programme and does not change `requirements.txt`.

The available ChatGPT runtime with NumPy `2.3.5` is treated as a **candidate modern research environment** for this preflight only.

Allowed interpretation:

- whether the frozen standalone equations execute and satisfy their internal analytic and numerical checks in this runtime.

Prohibited interpretation:

- official repository dependency migration;
- active-Core compatibility;
- proof of physical information retention;
- any whitepaper or equation change.

## 3. Why this preflight exists

The full P1 lane contains `60` labelled trajectories. Before paying that cost, this checkpoint tests one central nuisance tuple and only the mechanical assumptions required by the full run:

1. exact equal initial energy;
2. finite imprint evolution;
3. nonzero label-shaped `phi` and `mu` deposit;
4. exact removal of `psi`;
5. no source regeneration during passive relaxation;
6. passive `mu` evolution matching its analytic decay law;
7. no cap or fail-safe confound;
8. deterministic transpose behaviour of the orientation observer.

A positive preflight is not a scientific memory result. A negative or invalid preflight blocks the full population run until the first failed assumption is resolved.

## 4. Frozen representative pair

Grid and source:

- grid: `N = 64`;
- separation: `12` cells;
- Gaussian width: `3.5` cells;
- shift: `(0, 0)`;
- label `A`: two horizontal lobes;
- label `B`: two vertical lobes;
- each `psi` independently normalized to `sum(abs(psi)^2) = 1`;
- initial `phi = 0`;
- initial `mu = 0`;
- uniform `kappa = 1`.

Required initial checks:

- relative energy mismatch `<= 1e-14`;
- sorted-amplitude mismatch `<= 1e-14`;
- quadrupole transpose antisymmetry error `<= 1e-12`.

## 5. Frozen dynamics

Standalone deterministic NumPy snapshot copied from the parent protocol:

- `dt = 0.1`;
- `psi_diffusion = 0.05`;
- `phi_diffusion = 0.05`;
- `reaction_strength = 0.0007`;
- implemented `psi` dissipation coefficient `0.005`;
- `drift_strength = 0`;
- stochastic generation disabled;
- mode coupling disabled;
- `phi` diffusion scaled by `dt`;
- `mu_eta = 0.005` during imprint;
- `mu_rho = 0.0001`;
- `mu_cap = 10`;
- `mu_peak_cutoff_ratio = 0.1`;
- `psi_amp_cap = 1e6`;
- `phi_cap = 1e6`.

Imprint:

- `120` updates;
- dimensionless horizon `T = 12`.

Passive source-off:

- set `psi` to exact zero after imprint;
- set `mu_eta = 0`;
- keep `drift_strength = 0`;
- continue `phi` reaction, `phi` diffusion, and `mu` decay;
- checkpoints after `0`, `100`, `500`, `1000`, and `2000` source-off updates.

## 6. Frozen observers

For `phi` and `mu`, record at every checkpoint:

- RMS amplitude;
- relative signal amplitude compared with end of imprint;
- centroid-corrected quadrupole score;
- predicted orientation from quadrupole sign;
- maximum field value;
- finite-state status.

For `psi`, record maximum absolute value during passive source-off.

No pooled-field classifier is used in this one-pair preflight because a one-pair result cannot provide a valid train/held-out population split. The pooled observer remains mandatory for the later full P1 run.

## 7. Analytic passive-mu expectation

With `psi = 0`, `mu_eta = 0`, and no cap interaction:

`mu_(n+1) = (1 - mu_rho dt) mu_n`.

Therefore:

`mu_n = (1 - mu_rho dt)^n mu_0`.

The expected decay factor at checkpoint `n` is:

`f_n = (1 - 0.0001 * 0.1)^n`.

The pointwise normalized shape should remain unchanged apart from floating arithmetic.

## 8. Preflight validity gates

The preflight is valid only if all hold:

- no NaN or infinity;
- no fail-safe reset;
- `max(abs(psi)) <= 1e-15` at every passive checkpoint;
- `max(abs(psi)) < 0.1 psi_amp_cap` during imprint;
- `max(phi) < 0.1 phi_cap`;
- `max(mu) < 0.25 mu_cap`;
- initial equality checks pass;
- horizontal and vertical quadrupole signs remain opposite when the channel amplitude is above its readout floor;
- relative error between observed and analytic `mu` RMS decay factor `<= 1e-12` at every checkpoint;
- normalized passive `mu` shape difference from checkpoint zero `<= 1e-12`;
- transpose-pair field mismatch after transposition `<= 1e-12` relative L2 for `phi` and `mu` at every checkpoint.

## 9. Outcome meanings

### `preflight_passed`

All mechanical and analytic gates pass. The full P1 population run may be prepared under the same candidate runtime, with the result still provisional until active-Core and dependency compatibility are audited.

### `preflight_invalid`

A numerical, source-removal, symmetry, cap, or analytic gate fails. The full P1 run is blocked. The first failed operation must be located before another mechanism or parameter is selected.

### `preflight_nonidentifying`

The run is numerically valid, but `phi` or `mu` does not receive any orientation-shaped deposit above the declared signal floor. This constrains the corresponding current channel for this representative source, but is not yet the full population negative result.

## 10. Cross-question impact

- Q1: only a causal history channel that survives later full tests can justify a radial assembly-history experiment.
- Q2: cap-free persistent feedback could later motivate hysteresis or basin tests; passive decay alone is not attraction.
- Q3: this preflight checks whether the current fields can carry the simplest structural label mechanically.
- Real universe: no empirical or physical bridge is tested here.

## 11. Execution record placeholder

Before the run, record:

- exact script source and SHA-256;
- exact command;
- Python, NumPy, operating system, and architecture;
- wall-clock time.

After the run, append:

- complete machine-readable output;
- all failed and passed gates;
- exact narrow verdict;
- implications for the full P1 run;
- explicit claims not established.

## 12. Prohibited conclusions at version 0.1.0

This preregistration does not establish that:

- `phi` or `mu` retains information;
- a nonzero orientation trace is permanent memory;
- passive `mu` decay is an attractor;
- history dependence explains galaxy rotation curves;
- current Lineum is compatible with every NumPy 2.x release;
- a new equation or whitepaper change is warranted.
