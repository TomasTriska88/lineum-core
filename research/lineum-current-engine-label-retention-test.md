# Lineum Current-Engine Label-Retention Test

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** preregistered deterministic test of whether the current `psi`-`phi`-`mu` dynamics retain and causally reuse distinguishable structural history  
**Central question:** after two equal-energy histories are made observationally identical in current `psi`, can their past still be decoded from `phi` or `mu`, and can the retained fields cause different future evolution?  
**Current confidence:** high in the protocol and implementation audit; no simulation result exists at version `0.1.0`

## 1. Report lineage

Root programme:

- title: `Lineum-Native Field Stress-Test Programme`;
- root report: `research/lineum-native-field-stress-tests.md`;
- inherited root version: `0.2.1`;
- root evidence cutoff: `2026-08-04`.

Universe-emergence map:

- report: `research/lineum-universe-emergence-evidence-map.md`;
- inherited version: `0.2.0`;
- commit: `03451e8c17872b500179aa80c0743e48b4274629`.

Question-specific anchor maps:

- Q1: `research/lineum-galactic-observational-anchor-map.md`, commit `d732e8a1aa9133bb79df16e54acbde5b05f16553`;
- Q2: `research/lineum-saturation-attractor-observational-anchor-map.md`, commit `326cc34adef607b306fdf67b40cb98a4a2fb824e`;
- Q3: `research/lineum-information-retention-observational-anchor-map.md`, commit `eea03caf8b854468669d14850e1acb7ce0f921e9`.

Immediate predecessor:

- report: `research/lineum-cross-question-emergence-synthesis.md`;
- inherited version: `0.1.0`;
- commit: `9f1b9f38b1e65e1cebd4f65cbdc769195c779448`;
- selected next lane: current-engine equal-energy label-retention sanity test.

Repository and implementation checkpoint:

- repository: `TomasTriska88/lineum-core`;
- branch: `develop`;
- branch head before this report: `9f1b9f38b1e65e1cebd4f65cbdc769195c779448`;
- current engine path: `lineum_core/math.py`;
- current engine blob SHA: `bb877021810691223a0eb960a45493a2e351112a`;
- dependency declaration path: `requirements.txt`;
- dependency declaration blob SHA: `942f2b94b3d3f8c767451ae2d847a7b17c86d81e`.

## 2. Project-owner objective

The project owner requires Lineum to progress toward generating, from its own local rules, classes of structured behaviour observed in the real universe rather than inserting target curves or endpoints directly.

The active three-question programme asks whether Lineum can develop:

1. source-sensitive long-range radial response;
2. naturally bounded or attracting regimes rather than numerical clipping;
3. recoverable information after relaxation toward a common coarse state.

Public TOLOG material may be used as attributed inspiration and comparison evidence. The privately supplied TOLOG attachment and its contents are excluded.

This test uses no observed galaxy velocity, no cosmological fit, no private external equation, and no new Lineum field.

## 3. Plain-language experiment

Two stamps contain exactly the same amount of ink.

- Stamp `A` leaves two horizontal marks.
- Stamp `B` leaves the same two marks vertically.

The marks are pressed into the same material for the same time. The visible stamp is then removed.

Two questions are asked.

1. **Passive record:** can the old orientation still be read from a deeper layer after the visible mark is gone?
2. **Causal echo:** if an identical new round mark is placed on both materials, do the two materials evolve differently because their histories differ?

In Lineum:

- the visible mark is `psi`;
- the faster distributed trace is `phi`;
- the slower accumulated trace is `mu`;
- the material geometry is a uniform `kappa = 1` grid;
- the two orientations are labels only, not physical particles or galaxies.

A nonzero `mu` value is not sufficient. The label must be recoverable above fixed null controls, and a causal claim requires an intervention showing that the retained channel changes later dynamics.

## 4. Inherited evidence and constraints

### 4.1 Default radial lane

The prior deterministic disk lane did not satisfy the preregistered radial-locking shape. Removing the implemented `phi`-gradient drift changed its outer proxy by only about `0.263` parts per million.

Therefore:

- blind tuning of the current drift is prohibited;
- history storage through `phi` or `mu` remains untested;
- a positive result here would identify a candidate history mechanism, not galactic gravity.

### 4.2 Current `mu` regression gap

Existing validation checks establish only that:

- `mu` can become nonzero;
- the numerical run can remain finite;
- a historical scenario ended below the configured cap.

They do not establish:

- recovery of a hidden initial label;
- source-off retention;
- cap-independent natural saturation;
- causal reuse of stored history;
- physical information conservation.

### 4.3 Real-physics anchors

This test adopts only general operational constraints from the following sources.

- Wojciech H. Zurek, `Decoherence, einselection, and the quantum origins of the classical`, Reviews of Modern Physics 75, 715-775 (2003), DOI `10.1103/RevModPhys.75.715`, stable URL `https://arxiv.org/abs/quant-ph/0105127`.
- Samuel L. Braunstein and Arun K. Pati, `Quantum Information Cannot Be Completely Hidden in Correlations`, Physical Review Letters 98, 080502 (2007), DOI `10.1103/PhysRevLett.98.080502`, stable URL `https://arxiv.org/abs/gr-qc/0603046`.
- Antoine Berut et al., `Experimental verification of Landauer's principle linking information and thermodynamics`, Nature 483, 187-189 (2012), DOI `10.1038/nature10872`.
- T. W. B. Kibble, `Topology of Cosmic Domains and Strings`, Journal of Physics A 9, 1387-1398 (1976), DOI `10.1088/0305-4470/9/8/029`.

These sources motivate observer-relative records, explicit erasure criteria, and possible topological storage. They do not establish that current Lineum is quantum, thermodynamic, cosmological, or topological in the corresponding physical sense.

### 4.4 Public TOLOG inspiration

The public-source inventory recovered:

- public coupled-oscillator synchronization and recovery material;
- public language describing invariant nodes and structural-information retention;
- public scalar-minimum retention claims.

The present test uses only the general idea that a perturbation may leave a recoverable structural record. It does not copy a private TOLOG file, a private equation, a reported private dataset, or the public invariant-node percentage as its metric.

## 5. What the current implementation computes

The frozen current-engine subset is deterministic NumPy evolution with:

- uniform `kappa = 1`;
- zero external `delta`;
- stochastic linons and fluctuation noise disabled;
- `physics_mode_psi = diffusion`;
- mode coupling disabled;
- `phi` baseline reaction enabled;
- `phi` diffusion explicitly scaled by `dt`;
- `mu` accumulation, decay, feedback, and cap enabled during imprint;
- zero configured drift in the primary mechanism-isolation lane.

The current implementation reads `mu` through:

`drift_multiplier = 1 + mu`.

This multiplier affects both the `psi`-`phi` interaction and the `mu` accumulation rate. Therefore `mu` is not merely an archival output; it can alter future dynamics.

The implemented deterministic primary-lane update is:

1. Interaction:

`I = [0.1 tanh(0.4 clip(phi, 0, 10) (1 + mu))] psi`

followed by the current soft normalization:

`I <- I / (1 + abs(I) / 10)`.

2. `psi` update:

`psi <- psi + I dt - 0.005 psi dt + D_psi Lap_4(psi) dt`.

3. Energy density:

`e_psi = abs(psi)^2`.

4. Baseline `phi` reaction:

`phi <- phi + alpha_N (e_psi - phi) dt`,

where:

`alpha_N = reaction_strength (128 / N)^2`.

5. `phi` diffusion:

`phi <- phi + D_phi 0.05 Lap_4(phi) dt`.

6. Dynamic `mu` floor:

`floor = mu_peak_cutoff_ratio max(e_psi)`

when the configured ratio lies strictly between zero and one.

7. `mu` update:

`mu <- clip(mu + eta max(e_psi - floor, 0) (1 + mu) dt - rho mu dt, 0, mu_cap)`.

The four-neighbour periodic Laplacian is:

`Lap_4(F) = roll_up(F) + roll_down(F) + roll_left(F) + roll_right(F) - 4F`.

The frozen reference model below includes every operation material to the primary lane. It is separate from the optional active-Core adapter comparison.

## 6. Why source removal requires an intervention

Calling the current engine once with `psi = 0` is not automatically a clean source-off test when drift is active. The current gradient term depends on `phi`, so a nonzero `phi` gradient can regenerate `psi`, which can then deposit more `phi` and `mu`.

The primary source-off phase therefore freezes the following intervention before results are seen:

- set `psi` to an exact zero array at the start of relaxation;
- keep `drift_strength = 0`;
- keep stochastic generation disabled;
- set `mu_eta = 0` so no further `mu` deposit is possible;
- continue the implemented `phi` reaction, `phi` diffusion, and `mu` decay;
- verify after every checkpoint that `max(abs(psi)) <= 1e-15`.

This lane tests passive retention only.

A separate causal-echo phase resets both histories to the same nonzero radial `psi` state and allows their retained `phi` and `mu` fields to influence future evolution.

## 7. Registered hypotheses and alternatives

### H0 — no identifying record

After source removal, neither `phi` nor `mu` contains enough robust structure to recover the initial orientation beyond the preregistered horizon.

### H1 — `phi`-only distributed record

`phi` retains the label after `psi` is removed, while `mu` adds no independent retention or causal effect.

### H2 — `mu`-only slow structural record

`mu` retains the label after `phi` falls below the declared readout floor and its retained pattern causes a later causal echo.

### H3 — joint distributed record

Neither channel alone passes, but the combined `phi` and `mu` state retains the label.

### H4 — non-identifying energy residue

The fields remain nonzero but contain only total deposited energy or radial scale, not the orientation label.

### H5 — cap-driven persistence

Apparent memory depends materially on `mu_cap` or approaches the cap closely enough that the result cannot be interpreted as unconstrained structural retention.

### H6 — grid-orientation artifact

Recovery depends on horizontal-versus-vertical alignment with the square lattice rather than the physical content of the initial state.

### H7 — slow transient mistaken for memory

The label is readable only because the source-off horizon is too short relative to the declared decay timescale.

### H8 — causal echo without passive decoding

History alters future evolution even though the selected passive observers do not decode it reliably, indicating a non-identifying observer or distributed state dependence.

### H9 — passive record without causal echo

A channel stores a readable picture but does not materially affect later current-engine evolution under the common-state intervention.

### Deferred variants

The following remain registered but are not executed in version `0.1.0`:

- active default drift during source-off;
- stochastic linon and fluctuation lanes;
- wave-mode dynamics;
- phase-winding and topological labels;
- Eq-11 bounded localized structures;
- collective-relaxation historical variants;
- a new degenerate-minimum scalar adapter;
- physical-unit, galactic, cosmological, or black-hole mappings.

## 8. Frozen initial-state family

### 8.1 Grid and coordinates

Primary grid:

- `N = 64`;
- coordinates `x, y = arange(N) - (N - 1) / 2`;
- uniform `kappa = 1`;
- periodic four-neighbour numerical stencil;
- structures remain at least `12` cells from an edge in every primary sample.

Confirmation grid, executed only after primary metric validity:

- `N = 96`;
- geometrical lengths scaled by `96 / 64`;
- identical dimensionless horizon and parameter interpretation.

### 8.2 Equal-energy orientation pair

For each nuisance tuple `(separation, width, shift_x, shift_y)`, define two real nonnegative initial amplitudes.

Horizontal label `A`:

`g_A = G(x - separation/2, y) + G(x + separation/2, y)`.

Vertical label `B`:

`g_B = G(x, y - separation/2) + G(x, y + separation/2)`.

The Gaussian is:

`G(dx, dy) = exp(-(dx^2 + dy^2) / (2 width^2))`.

Each array is translated by the declared integer shift and independently normalized so that:

`sum(abs(psi)^2) = 1`.

Required pre-run equality checks:

- relative total-energy difference between labels `<= 1e-14`;
- identical sorted amplitude values for the unshifted transpose pair within `1e-14`;
- identical initial `phi = 0` and `mu = 0`;
- no element exceeds the numerical cap.

### 8.3 Nuisance schedule

Primary nuisance family:

- separations: `10`, `12`, `14` cells;
- widths: `2.5`, `3.5` cells;
- shifts: `(-3, -2)`, `(-2, 3)`, `(0, 0)`, `(2, -3)`, `(3, 2)`.

This yields `30` paired variants and `60` labelled trajectories.

Split rule fixed before execution:

- training variants: index modulo `3` in `{0, 1}`;
- held-out variants: index modulo `3` equal to `2`;
- both labels from one nuisance tuple remain in the same split.

The analytic quadrupole observer requires no training. The independent pooled-field observer uses only the training variants to form class centroids and is scored only on held-out variants.

### 8.4 Common current state for causal echo

After imprint, both histories receive the same normalized circular Gaussian:

`psi_common = exp(-(x^2 + y^2) / (2 * 5^2))`,

normalized to unit total energy.

This state contains no horizontal-versus-vertical label by construction.

## 9. Frozen parameters and horizons

### 9.1 Primary deterministic configuration

- backend: NumPy CPU;
- seed: `20260804` for split, readout noise, and permutation controls;
- `dt = 0.1`;
- `psi_diffusion = 0.05`;
- `phi_diffusion = 0.05`;
- `reaction_strength = 0.0007`;
- fixed implemented `psi` dissipation coefficient: `0.005`;
- `drift_strength = 0`;
- `disable_quantum_noise = True`;
- `use_mode_coupling = False`;
- `phi_diffusion_scales_with_dt = True`;
- `use_mu = True`;
- `mu_eta = 0.005` during imprint and causal echo;
- `mu_rho = 0.0001` primary;
- `mu_cap = 10` primary;
- `mu_peak_cutoff_ratio = 0.1`;
- `psi_amp_cap = 1e6`;
- `phi_cap = 1e6`.

### 9.2 Imprint phase

- `120` updates;
- dimensionless horizon `T_imprint = 12`.

### 9.3 Passive source-off phase

- reset `psi` to exact zero once before relaxation;
- `mu_eta = 0`;
- checkpoints after `0`, `100`, `500`, `1000`, and `2000` updates;
- final dimensionless source-off horizon `T_off = 200`;
- retain standard `mu_rho = 0.0001`;
- high-decay sensitivity lane: `mu_rho = 0.01`;
- cap sensitivity lane: `mu_cap = 100`.

### 9.4 Causal-echo phase

- replace both labels' `psi` with the same `psi_common`;
- evolve `200` updates;
- dimensionless horizon `T_echo = 20`;
- retain normal accumulation and decay;
- compare the channel-retention and channel-erasure lanes defined below.

### 9.5 Timestep confirmation

After the primary lane passes numerical validity gates:

- repeat the representative median nuisance tuples with `dt = 0.05`;
- double all update counts to preserve the declared dimensionless horizons;
- require observable agreement within thresholds stated in Section 13.

## 10. Channel and mechanism lanes

### P0 — pristine known-answer observer audit

Apply the observers directly to the initial arrays before engine evolution.

### P1 — passive full record

Imprint with both `phi` and `mu`, remove `psi`, stop further `mu` accumulation, and measure `phi` and `mu` separately.

### P2 — passive `phi`-only readout

Same trajectory as P1, but score only `phi`.

### P3 — passive `mu`-only readout

Same trajectory as P1, but score only `mu`.

### P4 — cap-raised control

Repeat P1 with `mu_cap = 100`.

### P5 — high-decay control

Repeat P1 with `mu_rho = 0.01` during source-off.

### C0 — erased-history causal null

Before common-state continuation, set both `phi = 0` and `mu = 0` for both labels.

Expected result: the two deterministic trajectories are identical to numerical precision.

### C1 — full-history causal echo

Retain both imprinted `phi` and `mu` before common-state continuation.

### C2 — `phi`-only causal echo

Retain imprinted `phi` and set `mu = 0` before common-state continuation.

### C3 — `mu`-only causal echo

Retain imprinted `mu` and set `phi = 0` before common-state continuation.

### C4 — cap-raised causal control

Repeat C1 with `mu_cap = 100`.

### C5 — transposed and rotated-grid artifact control

Repeat representative pairs after a global `90` degree transformation and after swapping labels. The result must transform predictably rather than favour one grid axis.

## 11. Observers and metrics

### 11.1 Channel weight

For every real nonnegative channel use the channel directly.

For `psi`, use `abs(psi)^2`.

Every field is evaluated only when finite. An all-zero field is assigned no orientation and cannot count as retained information.

### 11.2 Centroid-corrected quadrupole score

For weights `F >= 0`, compute the weighted centroid `(x_c, y_c)` and:

`Q(F) = sum(F ((x - x_c)^2 - (y - y_c)^2)) / [sum(F ((x - x_c)^2 + (y - y_c)^2)) + 1e-30]`.

Interpretation:

- `Q > 0` predicts horizontal label `A`;
- `Q < 0` predicts vertical label `B`;
- `abs(Q) < 1e-6` is unclassified.

This observer is fixed before engine output is seen.

### 11.3 Independent pooled-field nearest-centroid observer

1. Recenter each field to its nearest integer weighted centroid.
2. Normalize by its `L2` norm.
3. Average non-overlapping blocks into an `8 x 8` pooled feature array.
4. Flatten to `64` features.
5. Build one class centroid per label using training variants only.
6. Classify each held-out field by smaller Euclidean distance to the two training centroids.

This path does not use `Q` and is implemented separately.

### 11.4 Readout-noise robustness

At every source-off checkpoint, score both:

- exact fields;
- fields with additive deterministic Gaussian readout noise.

Noise scale is fixed relative to the channel's median imprint RMS:

- low noise: `sigma = 1e-4 * median_imprint_RMS`;
- high noise: `sigma = 1e-3 * median_imprint_RMS`.

Negative values introduced into `phi` or `mu` readout copies are clipped to zero for the orientation observers. Dynamics are never perturbed by readout noise.

### 11.5 Balanced accuracy

For predictions in labels `A` and `B`:

`balanced_accuracy = 0.5 (accuracy_A + accuracy_B)`.

Unclassified samples count as incorrect.

### 11.6 Permutation null

Use `2000` deterministic label permutations with seed `20260804`.

The one-sided p-value is:

`p = (1 + number(null_accuracy >= observed_accuracy)) / 2001`.

### 11.7 Relative signal amplitude

For each channel:

`S(t) = median(RMS(F(t))) / median(RMS(F_at_end_of_imprint))`.

A channel below `S = 1e-6` cannot count as a robust retained record even if a normalized orientation metric remains numerically defined.

### 11.8 Pairwise causal divergence

For matched label trajectories after the common-state reset:

`D_X(t) = ||X_A(t) - X_B(t)||_2 / [0.5 (||X_A(t)||_2 + ||X_B(t)||_2) + 1e-30]`.

Record this for `psi`, `phi`, and `mu`.

The erased-history null establishes the numerical floor `D_null`.

## 12. Analytic expectations frozen before execution

### 12.1 Equal-energy construction

Independent normalization makes total initial energy equal by construction. The transpose-symmetric unshifted pair must also match element-value multisets within floating precision.

### 12.2 Passive `mu` decay after clean source removal

When:

- `psi = 0`;
- `mu_eta = 0`;
- `drift_strength = 0`;
- no cap is reached;

then the implemented pointwise update is:

`mu_(n+1) = (1 - mu_rho dt) mu_n`.

Therefore:

`mu_n = (1 - mu_rho dt)^n mu_0`.

The normalized spatial shape should remain unchanged to floating precision. A positive passive `mu` orientation result is therefore an expected implementation consequence, not a discovery of new physics.

The scientifically stronger question is whether:

- the imprint produces label-specific `mu` structure without cap dependence;
- the structure remains readable under fixed readout noise;
- retained `mu` causes a future trajectory difference after current `psi` is equalized.

### 12.3 Erased-history causal null

With identical `psi_common`, zero `phi`, zero `mu`, identical parameters, deterministic evolution, and no stochastic source, labels A and B must produce identical trajectories.

Any material divergence in C0 invalidates the execution path.

## 13. Preregistered validity and decision thresholds

### 13.1 Numerical validity gates

Every retained lane must satisfy:

- no NaN or infinity in `psi`, `phi`, or `mu`;
- no fail-safe reset;
- `max(abs(psi)) < 0.1 psi_amp_cap`;
- `max(phi) < 0.1 phi_cap`;
- primary `max(mu) < 0.25 mu_cap`;
- passive source-off `max(abs(psi)) <= 1e-15` at every checkpoint;
- exact energy-equality checks pass;
- C0 final `D_psi`, `D_phi`, and `D_mu <= 1e-12`.

Failure of any applicable gate makes the corresponding lane inconclusive rather than negative.

### 13.2 Observer validity gate P0

Both fixed observers must satisfy on pristine held-out arrays:

- balanced accuracy `>= 0.95`;
- permutation p-value `<= 0.01`;
- quadrupole transpose antisymmetry error `<= 1e-12` for unshifted pairs;
- no systematic class imbalance greater than `0.05`.

If P0 fails, no engine memory conclusion is allowed.

### 13.3 Passive retained-record criterion

A channel is `retained_within_tested_domain` at a checkpoint only when all hold:

- quadrupole held-out balanced accuracy `>= 0.90`;
- pooled-field held-out balanced accuracy `>= 0.90`;
- both permutation p-values `<= 0.01`;
- relative signal amplitude `S >= 1e-6`;
- low-noise accuracy reduction `<= 0.05`;
- high-noise balanced accuracy remains `>= 0.80`;
- horizontal and vertical class accuracies differ by no more than `0.10`;
- numerical validity gates pass.

### 13.4 Cap-independence criterion

Primary versus `mu_cap = 100` must satisfy:

- maximum primary `mu < 0.25 mu_cap`;
- held-out balanced-accuracy difference `<= 0.05`;
- median normalized field difference at matched checkpoints `<= 1e-6` when neither lane approaches its cap.

Otherwise the `mu` interpretation is `cap_confounded`.

### 13.5 Timestep and resolution criterion

For representative median nuisance tuples:

- sign of the median quadrupole score must agree;
- balanced-accuracy difference `<= 0.10`;
- median causal-divergence ratio lies within `[0.5, 2.0]` when both values exceed the numerical floor;
- the qualitative channel classification is unchanged.

Failure is recorded as numerical or scale sensitivity, not as physical falsification.

### 13.6 Causal-echo criterion

A retained channel has a causal echo only when:

- C1 final median `D_psi >= max(1e-4, 10 D_null)`;
- at least one single-channel lane C2 or C3 reaches `D_psi >= max(5e-5, 5 D_null)`;
- zeroing the identified channel reduces final median `D_psi` by at least `50%` relative to C1;
- the effect survives the cap, timestep, and representative-grid controls;
- the common-state equality check passes at echo start.

If passive decoding succeeds but this criterion fails, classify the channel as a passive record without demonstrated causal reuse.

### 13.7 Negative-result criterion

The tested current-engine structural-memory hypothesis is `unsupported_under_tested_conditions` only when:

- P0 observer validity passes;
- all numerical and null gates pass;
- neither `phi` nor `mu` meets the passive retained-record criterion at the preregistered final checkpoint;
- C1 does not exceed the causal numerical floor;
- readout, cap, timestep, and representative resolution controls are valid.

### 13.8 Inconclusive conditions

The result is inconclusive when any material conclusion depends on:

- failed P0 observer validation;
- cap proximity or fail-safe behaviour;
- source-off `psi` regeneration;
- insufficient field amplitude;
- class imbalance or grid-axis preference beyond thresholds;
- unresolved active-Core versus frozen-snapshot divergence;
- an unavailable required dependency or environment mismatch;
- post-result threshold changes.

## 14. Outcome interpretation matrix

| Result | Allowed interpretation | Prohibited interpretation |
|---|---|---|
| `mu` pass, causal echo pass | current `mu` stores and causally reuses orientation history in the tested deterministic finite-grid regime | fundamental memory, gravity, consciousness, quantum information, permanent storage |
| `mu` pass, causal echo fail | `mu` is a passive readable archive under the tested source-off observer | autonomous attractor or history-dependent force |
| `phi` pass, `mu` fail | faster distributed `phi` trace stores the tested label | long-term memory or galactic field |
| joint-only pass | record is distributed across channels under the selected observer | information hidden only in correlations in a quantum-theorem sense |
| causal echo without passive pass | selected passive observers are non-identifying or history is encoded differently | proof that no readable channel exists |
| all valid lanes fail | tested current deterministic `phi`/`mu` regime does not retain or reuse the selected structural label through the final horizon | all Lineum memory variants are impossible |
| cap-sensitive pass | persistence is numerically or algorithmically confounded | natural saturation or physical memory |
| grid-sensitive pass | square-lattice anisotropy is a credible alternative explanation | robust continuum behaviour |

## 15. Cross-programme impact matrix

| Programme item | Possible impact of this test |
|---|---|
| Q1 galactic radial response | `constrains`: history dependence becomes worth a radial assembly test only if a retained channel causes an echo |
| Q2 attraction and saturation | `constrains`: persistent feedback may create hysteresis or apparent basins; cap dependence can disqualify that interpretation |
| Q3 information retention | `supports` or `constrains` directly through observer-relative label recovery |
| Default drift negative result | `unaffected`: drift remains unsupported in the prior frozen radial lane |
| Historical Eq-11 | `not_yet_compared`: remains queued regardless of current-engine outcome |
| Collective relaxation | `reopens` if `phi` retains distributed structure; otherwise remains untested in historical equations |
| Phase/topology variants | `not_yet_compared`: amplitude-orientation failure does not test them |
| Public TOLOG information language | `constrains`: replaces invariant-node wording with explicit held-out distinguishability and causal interventions |
| Real-universe physical memory | `unaffected`: no calibrated physical bridge exists |

## 16. Independence and active-Core comparison

### 16.1 Frozen standalone model

The embedded code in Section 18 is the durable numerical source of truth for this historical lane. It does not import `lineum_core`.

### 16.2 Active-Core adapter receipt

Before interpreting a run, an optional adapter must execute the current `lineum_core.math.step_core` NumPy path with the same deterministic subset and compare it with the standalone model on:

- one horizontal initial state;
- one vertical initial state;
- one random finite toy state generated with seed `20260804`;
- one exact source-off state.

Comparison horizons:

- one update;
- ten updates.

Required maximum absolute differences:

- `psi <= 1e-12`;
- `phi <= 1e-12`;
- `mu <= 1e-12`.

If the active Core does not match, preserve both results and classify the relationship as `unresolved_divergence`. The standalone snapshot remains reproducible, but no claim about the active engine is allowed until the first differing operation is identified.

### 16.3 Independent observer path

The quadrupole and pooled-field observers must be implemented in separate functions. The pooled observer must not call or reuse the quadrupole calculation.

## 17. Environment and reproduction plan

Required runtime:

- Python `>= 3.10`;
- NumPy satisfying repository declaration `>= 1.24, < 2.0.0`;
- no SciPy or machine-learning library is required for the frozen reference run.

Before execution record:

- Python version;
- NumPy version;
- operating system and architecture;
- processor description where available;
- wall-clock runtime;
- repository commit and engine blob;
- exact command;
- SHA-256 of the executed standalone source extracted from this report.

Planned command after the executable block is promoted to a temporary local file:

`python .scratch/lineum_label_retention_snapshot.py`

The temporary path is not evidence. After execution, the complete code, machine-readable JSON result, command, environment receipt, and interpretation must remain embedded in this report.

## 18. Frozen executable reference model

```python
from __future__ import annotations

from dataclasses import asdict, dataclass, replace
import hashlib
import json
import math
import os
import platform
import sys
import time
from typing import Dict, Iterable, List, Tuple

import numpy as np


SEED = 20260804
LABEL_A = 0
LABEL_B = 1


@dataclass(frozen=True)
class Config:
    dt: float = 0.1
    psi_diffusion: float = 0.05
    phi_diffusion: float = 0.05
    reaction_strength: float = 0.0007
    drift_strength: float = 0.0
    mu_eta: float = 0.005
    mu_rho: float = 0.0001
    mu_cap: float = 10.0
    mu_peak_cutoff_ratio: float = 0.1
    psi_amp_cap: float = 1e6
    phi_cap: float = 1e6


def lap4(field: np.ndarray) -> np.ndarray:
    return (
        np.roll(field, 1, axis=0)
        + np.roll(field, -1, axis=0)
        + np.roll(field, 1, axis=1)
        + np.roll(field, -1, axis=1)
        - 4.0 * field
    )


def cap_complex_magnitude(field: np.ndarray, cap: float) -> np.ndarray:
    out = np.asarray(field, dtype=np.complex128).copy()
    magnitude = np.abs(out)
    mask = magnitude > cap
    if np.any(mask):
        out[mask] *= cap / (magnitude[mask] + 1e-30)
    return out


def step_snapshot(state: Dict[str, np.ndarray], cfg: Config) -> Dict[str, np.ndarray]:
    psi = np.asarray(state["psi"], dtype=np.complex128).copy()
    phi = np.asarray(state["phi"], dtype=np.float64).copy()
    mu = np.asarray(state["mu"], dtype=np.float64).copy()
    kappa = np.asarray(state["kappa"], dtype=np.float64)
    size = psi.shape[0]

    drift_multiplier = 1.0 + mu
    phi_int = np.clip(phi, 0.0, 10.0)
    interaction_factor = 0.1 * np.tanh(
        (0.04 * phi_int * kappa * drift_multiplier) / 0.1
    )
    interaction = interaction_factor * psi
    interaction /= 1.0 + np.abs(interaction) / 10.0

    grad_phi_y, grad_phi_x = np.gradient(phi)
    phi_flow = (
        cfg.drift_strength
        * (grad_phi_y + 1j * grad_phi_x)
        * kappa
        * drift_multiplier
    )
    phi_flow /= 1.0 + np.abs(phi_flow) / 10.0

    psi += phi_flow * cfg.dt
    psi = cap_complex_magnitude(psi, cfg.psi_amp_cap)
    psi += interaction * cfg.dt
    psi -= 0.005 * psi * cfg.dt
    psi += cfg.psi_diffusion * lap4(psi) * kappa * cfg.dt

    energy = np.abs(psi) ** 2
    dynamic_reaction = cfg.reaction_strength * (128.0 / size) ** 2
    phi += kappa * dynamic_reaction * (energy - phi) * cfg.dt
    phi += kappa * cfg.phi_diffusion * 0.05 * lap4(phi) * cfg.dt
    phi = np.clip(phi, 0.0, cfg.phi_cap)

    floor = cfg.mu_peak_cutoff_ratio
    if 0.0 < floor < 1.0:
        floor *= float(np.max(energy))
    active_energy = np.maximum(energy - floor, 0.0)
    mu += cfg.mu_eta * active_energy * kappa * drift_multiplier * cfg.dt
    mu -= cfg.mu_rho * mu * cfg.dt
    mu = np.clip(mu, 0.0, cfg.mu_cap)

    if not (
        np.all(np.isfinite(psi))
        and np.all(np.isfinite(phi))
        and np.all(np.isfinite(mu))
    ):
        raise FloatingPointError("Non-finite state")
    if float(np.max(np.abs(psi))) >= 0.99 * cfg.psi_amp_cap:
        raise FloatingPointError("Psi fail-safe threshold reached")

    return {"psi": psi, "phi": phi, "mu": mu, "kappa": kappa.copy()}


def evolve(
    state: Dict[str, np.ndarray], cfg: Config, steps: int
) -> Dict[str, np.ndarray]:
    out = {key: value.copy() for key, value in state.items()}
    for _ in range(steps):
        out = step_snapshot(out, cfg)
    return out


def coordinates(size: int) -> Tuple[np.ndarray, np.ndarray]:
    axis = np.arange(size, dtype=np.float64) - (size - 1) / 2.0
    return np.meshgrid(axis, axis, indexing="xy")


def normalize_energy(amplitude: np.ndarray) -> np.ndarray:
    energy = float(np.sum(np.abs(amplitude) ** 2))
    if energy <= 0.0:
        raise ValueError("Amplitude must carry positive energy")
    return np.asarray(amplitude, dtype=np.complex128) / math.sqrt(energy)


def make_orientation_pair(
    size: int,
    separation: float,
    width: float,
    shift_x: int,
    shift_y: int,
) -> Tuple[np.ndarray, np.ndarray]:
    x, y = coordinates(size)
    gaussian = lambda dx, dy: np.exp(-(dx * dx + dy * dy) / (2.0 * width * width))
    horizontal = gaussian(x - separation / 2.0, y) + gaussian(
        x + separation / 2.0, y
    )
    vertical = gaussian(x, y - separation / 2.0) + gaussian(
        x, y + separation / 2.0
    )
    horizontal = np.roll(horizontal, (shift_y, shift_x), axis=(0, 1))
    vertical = np.roll(vertical, (shift_y, shift_x), axis=(0, 1))
    return normalize_energy(horizontal), normalize_energy(vertical)


def make_common_state(size: int, width: float = 5.0) -> np.ndarray:
    x, y = coordinates(size)
    return normalize_energy(np.exp(-(x * x + y * y) / (2.0 * width * width)))


def make_state(psi: np.ndarray) -> Dict[str, np.ndarray]:
    size = psi.shape[0]
    zeros = np.zeros((size, size), dtype=np.float64)
    return {
        "psi": np.asarray(psi, dtype=np.complex128).copy(),
        "phi": zeros.copy(),
        "mu": zeros.copy(),
        "kappa": np.ones((size, size), dtype=np.float64),
    }


def field_weight(channel: str, value: np.ndarray) -> np.ndarray:
    if channel == "psi":
        return np.abs(value) ** 2
    return np.maximum(np.asarray(value, dtype=np.float64), 0.0)


def quadrupole_score(weight: np.ndarray) -> float:
    field = np.maximum(np.asarray(weight, dtype=np.float64), 0.0)
    total = float(np.sum(field))
    if total <= 0.0:
        return 0.0
    x, y = coordinates(field.shape[0])
    cx = float(np.sum(field * x) / total)
    cy = float(np.sum(field * y) / total)
    dx = x - cx
    dy = y - cy
    denominator = float(np.sum(field * (dx * dx + dy * dy))) + 1e-30
    return float(np.sum(field * (dx * dx - dy * dy)) / denominator)


def recenter_integer(weight: np.ndarray) -> np.ndarray:
    field = np.maximum(np.asarray(weight, dtype=np.float64), 0.0)
    total = float(np.sum(field))
    if total <= 0.0:
        return field.copy()
    x, y = coordinates(field.shape[0])
    cx = float(np.sum(field * x) / total)
    cy = float(np.sum(field * y) / total)
    return np.roll(field, (-int(round(cy)), -int(round(cx))), axis=(0, 1))


def pooled_feature(weight: np.ndarray, pooled_size: int = 8) -> np.ndarray:
    field = recenter_integer(weight)
    norm = float(np.linalg.norm(field))
    if norm <= 0.0:
        return np.zeros(pooled_size * pooled_size, dtype=np.float64)
    field = field / norm
    size = field.shape[0]
    if size % pooled_size != 0:
        raise ValueError("Grid size must be divisible by pooled_size")
    block = size // pooled_size
    pooled = field.reshape(pooled_size, block, pooled_size, block).mean(axis=(1, 3))
    return pooled.ravel()


def balanced_accuracy(labels: np.ndarray, predictions: np.ndarray) -> float:
    scores = []
    for label in (LABEL_A, LABEL_B):
        mask = labels == label
        if not np.any(mask):
            raise ValueError("Both classes are required")
        scores.append(float(np.mean(predictions[mask] == labels[mask])))
    return 0.5 * sum(scores)


def nearest_centroid_predictions(
    train_features: np.ndarray,
    train_labels: np.ndarray,
    test_features: np.ndarray,
) -> np.ndarray:
    centroids = np.stack(
        [np.mean(train_features[train_labels == label], axis=0) for label in (0, 1)]
    )
    distances = np.linalg.norm(test_features[:, None, :] - centroids[None, :, :], axis=2)
    return np.argmin(distances, axis=1)


def permutation_p_value(
    labels: np.ndarray,
    predictions: np.ndarray,
    rng: np.random.Generator,
    permutations: int = 2000,
) -> float:
    observed = balanced_accuracy(labels, predictions)
    exceed = 0
    for _ in range(permutations):
        shuffled = rng.permutation(labels)
        if balanced_accuracy(shuffled, predictions) >= observed:
            exceed += 1
    return (1.0 + exceed) / (permutations + 1.0)


def normalized_pair_distance(a: np.ndarray, b: np.ndarray) -> float:
    numerator = float(np.linalg.norm(a - b))
    denominator = 0.5 * (float(np.linalg.norm(a)) + float(np.linalg.norm(b))) + 1e-30
    return numerator / denominator


def nuisance_schedule() -> List[Tuple[float, float, int, int]]:
    return [
        (separation, width, shift_x, shift_y)
        for separation in (10.0, 12.0, 14.0)
        for width in (2.5, 3.5)
        for shift_x, shift_y in ((-3, -2), (-2, 3), (0, 0), (2, -3), (3, 2))
    ]


def split_mask(count: int) -> Tuple[np.ndarray, np.ndarray]:
    indices = np.arange(count)
    train = indices % 3 != 2
    test = ~train
    return train, test


def run_primary(size: int = 64) -> Dict[str, object]:
    rng = np.random.default_rng(SEED)
    cfg = Config()
    source_off_cfg = replace(cfg, mu_eta=0.0, drift_strength=0.0)
    high_decay_cfg = replace(source_off_cfg, mu_rho=0.01)
    cap_raised_cfg = replace(source_off_cfg, mu_cap=100.0)
    schedule = nuisance_schedule()
    train_variants, test_variants = split_mask(len(schedule))
    common = make_common_state(size)
    checkpoints = (0, 100, 500, 1000, 2000)

    labels: List[int] = []
    variant_ids: List[int] = []
    imprint_states: List[Dict[str, np.ndarray]] = []
    passive: Dict[str, Dict[int, List[np.ndarray]]] = {
        channel: {checkpoint: [] for checkpoint in checkpoints}
        for channel in ("psi", "phi", "mu")
    }
    passive_high_decay_mu: Dict[int, List[np.ndarray]] = {
        checkpoint: [] for checkpoint in checkpoints
    }
    passive_cap_raised_mu: Dict[int, List[np.ndarray]] = {
        checkpoint: [] for checkpoint in checkpoints
    }

    energy_checks = []
    for variant_id, params in enumerate(schedule):
        psi_a, psi_b = make_orientation_pair(size, *params)
        energy_a = float(np.sum(np.abs(psi_a) ** 2))
        energy_b = float(np.sum(np.abs(psi_b) ** 2))
        energy_checks.append(abs(energy_a - energy_b) / max(energy_a, energy_b))
        for label, psi in ((LABEL_A, psi_a), (LABEL_B, psi_b)):
            labels.append(label)
            variant_ids.append(variant_id)
            imprinted = evolve(make_state(psi), cfg, 120)
            imprint_states.append(imprinted)

            for lane_cfg, target in (
                (source_off_cfg, passive),
                (high_decay_cfg, passive_high_decay_mu),
                (cap_raised_cfg, passive_cap_raised_mu),
            ):
                relaxed = {key: value.copy() for key, value in imprinted.items()}
                relaxed["psi"][:] = 0.0
                previous = 0
                for checkpoint in checkpoints:
                    relaxed = evolve(relaxed, lane_cfg, checkpoint - previous)
                    previous = checkpoint
                    if target is passive:
                        for channel in ("psi", "phi", "mu"):
                            target[channel][checkpoint].append(
                                field_weight(channel, relaxed[channel])
                            )
                    else:
                        target[checkpoint].append(relaxed["mu"].copy())

    labels_array = np.asarray(labels, dtype=np.int64)
    variant_array = np.asarray(variant_ids, dtype=np.int64)
    train_mask = train_variants[variant_array]
    test_mask = test_variants[variant_array]

    imprint_rms = {
        channel: float(
            np.median(
                [
                    np.sqrt(np.mean(field_weight(channel, state[channel]) ** 2))
                    for state in imprint_states
                ]
            )
        )
        for channel in ("psi", "phi", "mu")
    }

    observer_results: Dict[str, object] = {}
    for channel in ("psi", "phi", "mu"):
        observer_results[channel] = {}
        for checkpoint in checkpoints:
            fields = np.stack(passive[channel][checkpoint])
            q_scores = np.asarray([quadrupole_score(field) for field in fields])
            q_predictions = np.full(len(fields), -1, dtype=np.int64)
            q_predictions[q_scores > 1e-6] = LABEL_A
            q_predictions[q_scores < -1e-6] = LABEL_B
            q_accuracy = balanced_accuracy(
                labels_array[test_mask], q_predictions[test_mask]
            )

            features = np.stack([pooled_feature(field) for field in fields])
            pooled_predictions = nearest_centroid_predictions(
                features[train_mask], labels_array[train_mask], features[test_mask]
            )
            pooled_accuracy = balanced_accuracy(
                labels_array[test_mask], pooled_predictions
            )

            rms = float(np.median(np.sqrt(np.mean(fields * fields, axis=(1, 2)))))
            signal_ratio = rms / (imprint_rms[channel] + 1e-30)

            noise_results = {}
            for name, scale in (("low", 1e-4), ("high", 1e-3)):
                noise_sigma = scale * imprint_rms[channel]
                noisy = np.maximum(
                    fields + rng.normal(0.0, noise_sigma, size=fields.shape), 0.0
                )
                noisy_features = np.stack([pooled_feature(field) for field in noisy])
                noisy_predictions = nearest_centroid_predictions(
                    noisy_features[train_mask],
                    labels_array[train_mask],
                    noisy_features[test_mask],
                )
                noise_results[name] = balanced_accuracy(
                    labels_array[test_mask], noisy_predictions
                )

            observer_results[channel][str(checkpoint)] = {
                "quadrupole_balanced_accuracy": q_accuracy,
                "quadrupole_permutation_p": permutation_p_value(
                    labels_array[test_mask],
                    q_predictions[test_mask],
                    np.random.default_rng(SEED + checkpoint + 1),
                ),
                "pooled_balanced_accuracy": pooled_accuracy,
                "pooled_permutation_p": permutation_p_value(
                    labels_array[test_mask],
                    pooled_predictions,
                    np.random.default_rng(SEED + checkpoint + 2),
                ),
                "relative_signal_amplitude": signal_ratio,
                "noise_balanced_accuracy": noise_results,
                "median_abs_quadrupole": float(np.median(np.abs(q_scores[test_mask]))),
            }

    causal_results: Dict[str, List[Dict[str, float]]] = {
        lane: [] for lane in ("erased", "full", "phi_only", "mu_only", "cap_raised")
    }
    for variant_id in range(len(schedule)):
        index_a = 2 * variant_id
        index_b = index_a + 1
        state_a = imprint_states[index_a]
        state_b = imprint_states[index_b]
        for lane in causal_results:
            a = {key: value.copy() for key, value in state_a.items()}
            b = {key: value.copy() for key, value in state_b.items()}
            a["psi"] = common.copy()
            b["psi"] = common.copy()
            lane_cfg = cfg
            if lane == "erased":
                a["phi"][:] = 0.0
                b["phi"][:] = 0.0
                a["mu"][:] = 0.0
                b["mu"][:] = 0.0
            elif lane == "phi_only":
                a["mu"][:] = 0.0
                b["mu"][:] = 0.0
            elif lane == "mu_only":
                a["phi"][:] = 0.0
                b["phi"][:] = 0.0
            elif lane == "cap_raised":
                lane_cfg = replace(cfg, mu_cap=100.0)
            a = evolve(a, lane_cfg, 200)
            b = evolve(b, lane_cfg, 200)
            causal_results[lane].append(
                {
                    channel: normalized_pair_distance(a[channel], b[channel])
                    for channel in ("psi", "phi", "mu")
                }
            )

    summary_causal = {
        lane: {
            channel: float(np.median([item[channel] for item in items]))
            for channel in ("psi", "phi", "mu")
        }
        for lane, items in causal_results.items()
    }

    source_off_psi_max = max(
        float(np.max(field))
        for checkpoint in checkpoints
        for field in passive["psi"][checkpoint]
    )
    max_mu_primary = max(
        float(np.max(field))
        for checkpoint in checkpoints
        for field in passive["mu"][checkpoint]
    )
    cap_differences = []
    for checkpoint in checkpoints:
        for primary, raised in zip(
            passive["mu"][checkpoint], passive_cap_raised_mu[checkpoint]
        ):
            cap_differences.append(normalized_pair_distance(primary, raised))

    return {
        "protocol": {
            "size": size,
            "config": asdict(cfg),
            "schedule": schedule,
            "checkpoints": checkpoints,
            "imprint_steps": 120,
            "echo_steps": 200,
            "seed": SEED,
        },
        "validity": {
            "max_relative_initial_energy_difference": max(energy_checks),
            "source_off_psi_max": source_off_psi_max,
            "max_mu_primary": max_mu_primary,
            "max_normalized_cap_lane_difference": max(cap_differences),
        },
        "observer_results": observer_results,
        "causal_results": summary_causal,
        "high_decay_mu_final_median_rms": float(
            np.median(
                [
                    np.sqrt(np.mean(field * field))
                    for field in passive_high_decay_mu[2000]
                ]
            )
        ),
    }


def environment_receipt() -> Dict[str, str]:
    return {
        "python": sys.version,
        "numpy": np.__version__,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }


def main() -> None:
    started = time.perf_counter()
    result = run_primary(size=64)
    result["environment"] = environment_receipt()
    result["wall_clock_seconds"] = time.perf_counter() - started
    encoded = json.dumps(result, sort_keys=True, indent=2)
    result["result_sha256_before_self_field"] = hashlib.sha256(
        encoded.encode("utf-8")
    ).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
```

## 19. Pre-execution review checklist

Before extracting or running Section 18:

- [x] Repository, branch, head, engine path, and engine blob recorded.
- [x] Root programme and all three question-specific maps re-read.
- [x] Current deterministic update independently restated.
- [x] Source-off regeneration confound identified and blocked.
- [x] Equal-energy construction and nuisance schedule frozen.
- [x] Observers, split, permutation null, and readout noise frozen.
- [x] Cap, timestep, resolution, class-balance, and causal controls frozen.
- [x] Positive, negative, cap-confounded, grid-confounded, and inconclusive outcomes defined.
- [x] Complete standalone reference model embedded.
- [ ] Extract the embedded model without editing it.
- [ ] Record extracted-source SHA-256.
- [ ] Run P0 observer audit.
- [ ] Run active-Core adapter comparison.
- [ ] Execute the primary `N = 64` lane only if P0 and adapter gates pass.
- [ ] Append complete machine-readable output and interpretation before any confirmation run.
- [ ] Execute timestep and `N = 96` confirmations only if the primary lane is valid.

## 20. Prohibited conclusions at version 0.1.0

This preregistration does not establish that:

- `phi` or `mu` retains the label;
- current Lineum possesses physical memory;
- history dependence explains galaxy rotation curves;
- a passive trace is an attractor;
- any result is independent of caps, boundaries, timestep, or grid orientation;
- information is conserved or erased fundamentally;
- Lineum is quantum mechanical;
- public TOLOG information or stability claims are correct or incorrect;
- a future positive finite-grid result exists in the real universe.

## 21. ClickUp status

Linked operational task:

- task ID: `869edcdkk`;
- workspace ID: `90121717552`.

The last attempted connector write returned `RATE_LIMIT_EXCEEDED` with a reported wait of `531` minutes. No ClickUp call was made during this preregistration checkpoint.

`ClickUp mode = unsynchronized`.

## 22. Execution log

1. Re-fetched the current `develop` branch and all applicable repository instructions.
2. Re-read the complete current engine source by immutable blob SHA.
3. Identified that an active `phi` gradient can regenerate `psi`, making naive source removal invalid.
4. Froze a passive source-off intervention that prevents new `psi` and `mu` deposit.
5. Froze a separate common-state causal-echo intervention.
6. Registered null, `phi`-only, `mu`-only, cap, decay, timestep, resolution, and grid-artifact lanes.
7. Embedded a standalone deterministic reference implementation and fixed observers.
8. No code in `lineum_core`, test suite, whitepaper, simulation output, or physical claim was changed or produced.
