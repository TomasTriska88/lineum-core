# Lineum Information-Retention Observational Anchor Map

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** physical and information-theoretic anchors for distinguishing local relaxation, transferred records, coarse-grained loss, topological memory, and genuine erasure in Lineum  
**Central question:** when two distinguishable initial Lineum states relax toward the same coarse-grained endpoint, which observers can still recover their initial label, from which field channel, for how long, and at what dynamical cost?  
**Current confidence:** high in the observer-relative test boundary; high that existing Lineum `mu` checks do not establish information retention; no physical information-conservation or information-destruction claim is established

## 1. Report lineage

Root programme:

- report: `research/lineum-native-field-stress-tests.md`;
- root version inherited: `0.2.1`;
- root evidence cutoff: `2026-08-04`.

Universe-emergence predecessor:

- report: `research/lineum-universe-emergence-evidence-map.md`;
- predecessor version inherited: `0.2.0`;
- predecessor commit: `03451e8c17872b500179aa80c0743e48b4274629`.

Sibling observational maps:

- `research/lineum-galactic-observational-anchor-map.md`, commit `d732e8a1aa9133bb79df16e54acbde5b05f16553`;
- `research/lineum-saturation-attractor-observational-anchor-map.md`, commit `326cc34adef607b306fdf67b40cb98a4a2fb824e`.

Repository checkpoint before this report:

- repository: `TomasTriska88/lineum-core`;
- branch: `develop`;
- branch head: `326cc34adef607b306fdf67b40cb98a4a2fb824e`;
- current engine file: `lineum_core/math.py`;
- current engine blob SHA: `bb877021810691223a0eb960a45493a2e351112a`;
- current validation file: `scripts/validation_core.py`;
- current validation blob SHA: `59818298f675e0a4789f4d4248ecc4c9fa454e48`;
- current wave and memory test file: `tests/test_wave_core.py`;
- current test blob SHA: `085e302e7c70c5dadcee45fe479bb70eaa8cd264`.

## 2. Purpose

This report prevents the following statements from being treated as equivalent:

- the visible `psi` amplitude became similar;
- the scalar field reached the same minimum;
- a weak residual trace remained;
- a field channel retained enough structure to identify the past;
- information moved into correlations or another field;
- a coarse-grained observer lost access to information;
- the complete model state became independent of the initial condition;
- information was physically erased.

The word `information` is prohibited in a decision-relevant conclusion unless the observer, candidate labels, prior distribution, accessible channels, metric, and time horizon are declared.

## 3. Plain operational picture

Consider two stamps with equal amounts of ink:

- stamp `A` draws a vertical bar;
- stamp `B` draws a horizontal bar.

Both are pressed into a material and later removed. The material then relaxes until its average height and total deposited energy are the same in both cases.

Several distinct outcomes remain possible.

1. The surface looks identical, but the subsurface still contains differently oriented stress.
2. The visible shape disappears, but another layer records which stamp was used.
3. Only the total amount of ink remains, so the two histories can no longer be distinguished.
4. A classifier appears to distinguish them only because the system has not finished relaxing.
5. A numerical grid leaves orientation artifacts that imitate memory.
6. The complete state becomes identical only because clipping or explicit resetting erased differences.

The Lineum experiment must distinguish these outcomes rather than calling every nonzero `mu` value memory.

## 4. Observer-relative definitions

Let the hidden initial label be:

`Y in {A, B}`.

Let `X_C(t)` be the state accessible at time `t` to observer `C`.

Candidate observer channels are:

- `C_psi_amp`: `abs(psi)` or `abs(psi)^2` only;
- `C_psi_phase`: phase of `psi`, with declared treatment of near-zero amplitude;
- `C_phi`: the real `phi` field;
- `C_mu`: the real `mu` field;
- `C_topology`: declared vortex, winding, domain, or defect observables;
- `C_joint`: the complete accessible tuple `(psi, phi, mu)`;
- `C_coarse`: spatially or spectrally coarse-grained subsets;
- `C_local`: a limited spatial window;
- `C_environment`: channels intentionally treated as an external record.

### 4.1 Distinguishability

Information is operationally retained for observer `C` when a frozen estimator can infer `Y` from `X_C(t)` above a preregistered null level on held-out runs.

Candidate metrics include:

- balanced classification accuracy with confidence intervals;
- area under the receiver-operating-characteristic curve;
- cross-validated log loss;
- an independently estimated mutual-information lower bound;
- direct state distance only when its invariances and null distribution are declared.

A nonzero field is not sufficient. The field must contain label-specific structure.

### 4.2 Coarse-grained loss

Observer `C_psi_amp` may lose the initial label while `C_psi_phase`, `C_phi`, or `C_mu` retains it.

This is observer-relative information loss, not complete erasure.

### 4.3 Transfer

Information is transferred when distinguishability decreases in one channel while appearing in another under a causal coupling intervention.

Temporal succession alone is insufficient. The transfer interpretation requires an ablation or intervention that suppresses the receiving channel or its coupling.

### 4.4 Complete erasure within the model

A bounded claim of model-level erasure requires all declared accessible channels, including the joint state, to lose distinguishability after convergence and after numerical-artifact controls.

Even this would establish erasure only within the implemented dissipative model and observer set. It would not establish fundamental information destruction in nature.

### 4.5 Topological memory

A scalar or complex field may relax locally toward a vacuum or amplitude minimum while global domain, winding, defect, or boundary information remains.

Topological memory must be measured by a stable invariant or defect classification, not by visual inspection.

## 5. Primary physical anchors

### Source I1 — decoherence and environmental records

- title: `Decoherence, einselection, and the quantum origins of the classical`;
- author: Wojciech H. Zurek;
- journal: Reviews of Modern Physics `75`, 715-775;
- year: `2003`;
- DOI: `10.1103/RevModPhys.75.715`;
- arXiv: `quant-ph/0105127`;
- stable URLs: `https://arxiv.org/abs/quant-ph/0105127` and `https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.75.715`;
- access date: `2026-08-04`.

The review explains decoherence through interaction with environmental degrees of freedom. Interference can become inaccessible to a subsystem observer while stable pointer states and correlations with the environment remain.

Lineum consequence:

- disappearance of a local `psi` pattern does not imply complete information destruction;
- `phi`, `mu`, spatially distributed modes, or unresolved phase structure can act as environmental records;
- observers with different channel access must be scored separately;
- no quantum-mechanical identification is implied because current Lineum dynamics are not established as a quantum theory.

### Source I2 — no-hiding constraint in quantum information

- title: `Quantum Information Cannot Be Completely Hidden in Correlations: Implications for the Black-Hole Information Paradox`;
- authors: Samuel L. Braunstein and Arun K. Pati;
- journal: Physical Review Letters `98`, 080502;
- year: `2007`;
- DOI: `10.1103/PhysRevLett.98.080502`;
- arXiv: `gr-qc/0603046`;
- stable URLs: `https://arxiv.org/abs/gr-qc/0603046` and `https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.98.080502`;
- access date: `2026-08-04`.

The quantum no-hiding result constrains the idea that missing quantum information can reside solely in correlations between subsystems under the theorem's assumptions.

Lineum consequence:

- the theorem must not be applied directly to current dissipative Lineum dynamics;
- it supplies an adversarial warning against vague statements that information is `somewhere in correlations` without locating an accessible channel and stating the governing assumptions;
- a Lineum test must identify where distinguishability resides and whether the full update is reversible, dissipative, stochastic, or many-to-one.

### Source I3 — thermodynamic cost of erasure

- title: `Experimental verification of Landauer's principle linking information and thermodynamics`;
- authors: Antoine Berut, Artak Arakelyan, Artyom Petrosyan, Sergio Ciliberto, Raoul Dillenschneider, and Eric Lutz;
- journal: Nature `483`, 187-189;
- year: `2012`;
- DOI: `10.1038/nature10872`;
- stable URL: `https://www.nature.com/articles/nature10872`;
- access date: `2026-08-04`.

The experiment implemented a one-bit memory with a colloidal particle in a modulated double-well potential and measured dissipated heat during logically irreversible erasure, approaching the Landauer bound for slow cycles.

Lineum consequence:

- true physical erasure is stronger than fading of a numerical field;
- a dissipative Lineum update can destroy recoverable label information, but connecting that loss to thermodynamics requires a defined energy, temperature, entropy, and environment;
- current dimensionless damping cannot be interpreted as Landauer heat without a physical bridge;
- an internal erasure proxy should record norm, declared energy-like quantities, entropy proxies, and discarded channels while explicitly remaining dimensionless.

### Source I4 — vacuum topology and persistent defects

- title: `Topology of Cosmic Domains and Strings`;
- author: T. W. B. Kibble;
- journal: Journal of Physics A: Mathematical and General `9`, 1387-1398;
- year: `1976`;
- DOI: `10.1088/0305-4470/9/8/029`;
- stable DOI URL: `https://doi.org/10.1088/0305-4470/9/8/029`;
- access date: `2026-08-04`.

The paper studies domain structures that can form when a field undergoes spontaneous symmetry breaking. Domain walls, strings, or monopoles depend on the topology of the degenerate-vacuum manifold.

Lineum consequence:

- local relaxation into a potential minimum need not erase global history;
- different regions can select different degenerate minima, leaving domain boundaries or topological defects;
- the simplest fixed-minimum adapter with only one nondegenerate minimum cannot test this mechanism fully;
- phase, winding, and domain observers must be included before concluding that a relaxed scalar state has forgotten its origin;
- a topological analogy does not establish cosmic strings in Lineum.

## 6. Public TOLOG relevance

The first public TOLOG inventory recovered two Q3-related public claim classes.

### 6.1 Scalar field retained at a potential minimum

A field remaining at or returning to a potential minimum establishes, at most, stability of a coarse observable under the public test conditions.

It does not determine whether:

- two different approach paths remain distinguishable;
- phase or conjugate variables retain a record;
- a controller or damping term enforced the minimum;
- the complete state is reversible;
- information was transferred into another channel;
- the field was initialized exactly at the minimum;
- the public metric observed only the scalar value.

### 6.2 Invariant-node percentage

The public `9/12` invariant-node or `75%` structural-retention language is retained only as a source-recovered comparator.

Without a complete public operational definition, it does not establish:

- Shannon or mutual information;
- quantum information;
- distinguishability of two equal-energy histories;
- retention after source removal;
- robustness to node relabelling, symmetry, noise, or resolution;
- a connection to black-hole information.

Lineum will not copy the percentage metric. It will use paired-state distinguishability with declared observers.

## 7. Current Lineum implementation

### 7.1 What the code computes

The current engine has an optional `mu` channel with parameters:

- `use_mu`, default `False`;
- accumulation rate `mu_eta = 0.005`;
- decay rate `mu_rho = 0.0001`;
- numerical cap `mu_cap = 10.0`;
- relative peak threshold `mu_peak_cutoff_ratio = 0.1`.

In the current NumPy and PyTorch paths, the implemented update is operationally equivalent to:

1. compute `e_psi = abs(psi)^2`;
2. derive a dynamic floor from a fraction of the current maximum when the ratio lies between zero and one;
3. retain only energy above that floor;
4. accumulate the retained energy into `mu`, modulated by `kappa`, the current `1 + mu` multiplier, and `dt`;
5. subtract linear decay `mu_rho * mu * dt`;
6. clip `mu` into `[0, mu_cap]`.

The same `1 + mu` value also multiplies the `psi`-`phi` interaction strength. Therefore `mu` is not a passive archive; it changes subsequent dynamics.

### 7.2 What this implementation does not guarantee

The equation does not by itself guarantee that `mu` retains:

- spatial identity after source removal;
- phase information;
- topology;
- distinctions between equal-energy patterns;
- information independently of the numerical cap;
- information for arbitrarily long times;
- a reversible encoding;
- thermodynamic or quantum information.

Because accumulation is driven primarily by thresholded energy, two different patterns with the same coarse energy history can become observationally equivalent in `mu`.

The multiplicative `1 + mu` feedback can also amplify prior deposits, so cap proximity and positive-feedback effects must be audited.

## 8. Existing Lineum validation gap

### 8.1 `MU_REGRESSION_EXPECTATIONS`

The current validation accepts the memory scenario when:

- maximum `mu` in wave mode exceeds `0.1`;
- maximum `mu` in diffusion mode exceeds `0.1`;
- `psi` contains no NaN in either mode.

This verifies deposit and numerical completion. It does not test retention of a recoverable initial label.

### 8.2 Current golden test

The current `test_mu_regression_snapshot_golden` checks that the validation reports success, that the output fields exist, that `mu_wave` is finite, and that its maximum exceeds `0.1`.

This is a regression test for implemented deposit behaviour, not a scientific information-retention test.

### 8.3 Historical RA-4 check

The historical RA-4 logic labels `mu` bounded when its final maximum remains below `0.99 * mu_cap` and labels it grown when the maximum exceeds `0.01`.

This does not establish natural saturation because:

- the test includes an explicit cap;
- the source is not removed and followed through a long decay phase;
- the invariant set is not defined;
- no paired histories are decoded;
- no cap-scaling or source-off control is required.

### 8.4 Narrow implementation conclusion

Current evidence level:

- `mu` accumulation and decay: `implemented`;
- nonzero deposit under existing scenarios: covered by current regression expectations, but not newly reproduced in this programme;
- recoverable structural information: `unresolved`;
- natural saturation independent of `mu_cap`: `unresolved`;
- physical memory or information conservation: not established.

## 9. Required Q3 experiment family

### I0 — analytic known-answer observer cases

Before running Lineum:

- construct arrays where labels differ only by translation, rotation, phase, or topology;
- verify that each proposed metric is sensitive to the intended distinction and invariant to prohibited nuisance transformations;
- test identical-state and shuffled-label nulls;
- derive chance distributions for the classifiers.

### I1 — paired equal-energy histories

Construct paired initial states `A` and `B` with:

- exactly equal total `abs(psi)^2`;
- equal radial or coarse amplitude profile where possible;
- different spatial orientation, phase arrangement, or topology;
- identical `phi`, `mu`, `kappa`, boundary, seed policy, and noise distribution.

The initial label must not be recoverable from total energy alone.

### I2 — source-on and source-off phases

Use a two-stage protocol.

1. **Imprint phase:** evolve the paired states for a frozen number of updates.
2. **Relaxation phase:** remove the source or replace active `psi` by a declared common relaxed state while continuing `phi` and `mu` evolution.

Record distinguishability continuously rather than only at the final frame.

### I3 — observer-access matrix

At each preregistered time, evaluate held-out label recovery from:

- `psi` amplitude;
- `psi` phase;
- `phi`;
- `mu`;
- topology;
- joint complete state;
- coarse-grained and local subsets.

This distinguishes local forgetting from record transfer.

### I4 — causal ablations

Required lanes include:

- `mu` off;
- `mu` on with standard decay;
- `mu` on with accumulation disabled after imprint;
- altered `mu_rho` on a preregistered small grid;
- raised `mu_cap` and cap-never-reached control;
- `psi -> phi` reaction off;
- `mu` feedback into interaction off in a research-scoped extracted path;
- phase randomization after imprint;
- spatial shuffling that preserves the amplitude histogram;
- label shuffling for estimator nulls.

### I5 — convergence and artifact attacks

- at least two grid resolutions;
- at least two timesteps with matched physical or dimensionless horizon;
- periodic versus non-periodic or absorbing-boundary control where available;
- translations and rotations relative to the grid;
- multiple noise seeds or a deterministic lane;
- independent metric implementation;
- classifier complexity control to prevent memorizing numerical noise.

### I6 — degenerate-minimum topology adapter

Only after I0-I5, introduce the smallest research-scoped scalar potential with multiple degenerate minima if the current complex phase and topology cannot test the Kibble-like question adequately.

The adapter must remain outside the installable public API and must include:

- explicit potential and derivative;
- declared integration scheme;
- domain and boundary conditions;
- known-answer defect cases;
- defect annihilation and false-positive controls;
- no claim of cosmic strings or real symmetry breaking without a physical bridge.

### I7 — thermodynamic bridge

Only after robust internal distinguishability results:

- define an energy functional or explicitly state that none exists;
- quantify energy-like dissipation during erasure;
- define entropy and environment assumptions;
- compare with Landauer-type reasoning only within the declared mapping;
- prohibit SI heat or temperature claims without calibration.

## 10. Preregistered first discriminator

The cheapest useful Q3 experiment uses the current engine and adds no new physical term.

### 10.1 Candidate pair

Use two equal-energy `psi` patterns on the same grid:

- `A`: two identical localized lobes separated horizontally;
- `B`: the same lobes separated vertically.

Then include rotated-grid and random-orientation controls so that a successful classifier cannot rely only on lattice anisotropy.

A second pair should differ in phase while sharing amplitude exactly:

- `A_phase`: equal amplitude with one phase winding or declared phase patch;
- `B_phase`: equal amplitude with the opposite or topologically distinct phase arrangement.

### 10.2 Frozen first question

After an imprint phase and source-off relaxation, can a held-out frozen observer identify the initial label from `phi` or `mu` after `psi` amplitude has fallen to the same preregistered coarse state?

### 10.3 Outcome meanings

- **Only `psi` amplitude retains the label:** no evidence for transfer into memory fields.
- **`phi` retains the label and `mu` does not:** current reaction-diffusion trace is the relevant memory candidate.
- **`mu` retains the label after `phi` loses it:** current slow channel supports structural record retention within the tested domain.
- **Joint state retains the label but every single channel fails:** information is distributed across channels; interaction terms require causal testing.
- **All observers fail after convergence:** model-level erasure is supported only within the declared observer set and numerical domain.
- **Accuracy remains high only near `mu_cap`:** likely cap or positive-feedback artifact.
- **Accuracy changes strongly with grid orientation:** lattice artifact.
- **A phase label survives only in topology:** supports a topological-record interpretation, not quantum-information conservation.
- **A classifier succeeds equally on shuffled labels:** observer invalid; no result.

### 10.4 Initial success criteria to freeze before execution

Exact numerical thresholds will be preregistered in the child execution report after known-answer null distributions are calculated. They must include:

- held-out balanced accuracy confidence interval excluding chance;
- predefined minimum effect duration after source removal;
- low cap-trigger fraction;
- orientation-artifact ceiling;
- reproduction across a second resolution and independent metric;
- label-shuffle false-positive control;
- no threshold changes after observing the target result.

## 11. Relation to the real universe

A robust Lineum memory result could connect only to a general class of real phenomena:

- environmental records after local decoherence;
- hysteretic or structural memory in open nonlinear systems;
- persistence of defects after symmetry breaking;
- thermodynamic cost of logically irreversible reset.

It would not by itself establish:

- quantum unitarity;
- black-hole information recovery;
- cosmic strings;
- universal conservation of information;
- consciousness, soul, or observer ontology;
- a physical temperature or entropy for Lineum.

The real-universe bridge requires a concrete physical implementation, calibrated observables, and independent empirical predictions.

## 12. Root-programme impact matrix

| Root question or candidate | Q3 anchor-map impact |
|---|---|
| Q1 galactic radial response | `constrains`: a memory field may create history-dependent radial response, but any such role must be identified by source-off and `mu`-off interventions |
| Q2 saturation and attraction | `constrains`: persistent `mu` can produce apparent attraction or hysteresis; cap and feedback artifacts must be separated |
| Q3 scalar minimum and information retention | `supports`: supplies an observer-relative, falsifiable protocol using current fields before adding a new scalar adapter |
| Historical Eq-11 saturation | `not_yet_compared`: dissipative structures may destroy or redistribute labels; requires its own observer matrix |
| Historical collective relaxation | `reopens`: distributed stress may act as an environmental record, but must be separated from diffusion |
| Current `mu` channel | `reopens`: implemented deposit exists, scientific retention remains unresolved |
| Public TOLOG scalar-minimum claim | `constrains`: minimum retention is not information retention without paired-state distinguishability |
| Public TOLOG invariant-node percentage | `observationally_equivalent` only to a coarse persistence score; not an information metric without operational details |
| Real-universe information conservation | `unaffected`: no physical bridge exists yet |

## 13. Cheapest next discriminator

The cheapest useful next experiment across the complete programme is a small preregistration and known-answer metric audit for the current `psi-phi-mu` pair protocol.

It is preferable to immediately adding a new scalar-potential adapter because it can determine whether the already implemented memory channels retain structural labels and can also constrain Q1 history dependence and Q2 apparent attraction.

Before execution, the active child report must contain:

- exact grid, timestep, update counts, initial arrays, and source-off operation;
- exact observer implementations and null distributions;
- seed and orientation schedule;
- cap and telemetry checks;
- success, failure, and inconclusive thresholds;
- complete executable verification code;
- an independent metric path.

## 14. Prohibited conclusions at version 0.1.0

This report does not establish that:

- current `mu` retains recoverable information;
- nonzero `mu` is memory in an information-theoretic sense;
- Lineum conserves or destroys fundamental information;
- a scalar field at a minimum remembers its history;
- quantum no-hiding or Landauer's principle applies directly to current Lineum dynamics;
- topological defects observed in a future run would be cosmic defects;
- black-hole information is represented by any current Lineum channel;
- public TOLOG information claims are correct or incorrect;
- old green memory tests validate the new Q3 question.

## 15. Execution log

1. Retrieved primary physical anchors for decoherence and environmental records, quantum no-hiding constraints, experimentally measured Landauer erasure, and topological defect formation after symmetry breaking.
2. Re-read the current Lineum engine, validation logic, and current memory regression test at immutable blob SHAs.
3. Classified current `mu` as an implemented thresholded energy accumulator with slow decay, positive feedback into interaction, and an explicit cap.
4. Determined that current and historical memory checks verify deposit, finiteness, and cap avoidance only; they do not measure paired-state distinguishability or source-off retention.
5. Defined observer-relative information, coarse-grained loss, transfer, model-level erasure, and topological memory.
6. Defined test classes I0-I7 and selected a current-engine equal-energy paired-history protocol as the cheapest discriminator.
7. No simulation, production-code change, scalar adapter, black-hole analogy test, or whitepaper promotion was performed in this checkpoint.
