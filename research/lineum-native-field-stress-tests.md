# Lineum-Native Field Stress-Test Programme

**Status:** active  
**Version:** 0.2.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** a Lineum-only research programme testing three field-dynamics questions with current and historically relevant Lineum equation families  
**Current confidence:** high in the programme structure; high that the default radial-drift lane is unsupported under the tested conditions; low on the replacement mechanism until historical retrieval and discriminating controls are complete  
**Operational task:** ClickUp task `869edcdkk`

## 1. Repository and ownership boundary

This is a native Lineum research programme. Its equations, runners, controls, results, negative outcomes, and interpretations belong in `TomasTriska88/lineum-core` under `research/`.

The programme does not reproduce, validate, or archive any external private theory. External conversation supplied motivation only. No external manuscript, unpublished equation, private dataset, or collaboration brief is part of the evidence chain.

Canonical Core code and whitepapers remain unchanged unless a later result independently passes the repository promotion gates.

Frozen repository state at programme creation:

- repository: `TomasTriska88/lineum-core`;
- branch: `develop`;
- commit: `adcec5f65470e90207246724280bacbb77ec0185`;
- current NumPy engine source: `lineum_core/math.py`;
- frozen source blob: `bb877021810691223a0eb960a45493a2e351112a`.

Current programme checkpoint after the first two radial lanes:

- branch head before this report revision: `41d7e16342cd2d4170ccf807f7d4dd60ae1a3aa6`;
- Lane A receipt commit: `30cdd87bce6f1596d62019eaebd979ab04292548`;
- Lane B receipt commit: `50776c0772340ea7dbf359806dfba9ef165b46db`.

## 2. Programme questions

### Q1 — Galactic radial locking

Can existing Lineum `psi`–`phi`–`mu` dynamics, initialized from a visible-disk radial profile, generate a robust long-range response whose dimensionless circular-response proxy is approximately constant, without inserting a `1/r` law, fitting the outer observed curve, or adding a dark-halo term?

Active reports:

- `research/lineum-native-galactic-radial-locking-test.md`;
- `research/lineum-native-galactic-radial-locking-lane-a.md`;
- `research/lineum-native-galactic-radial-locking-lane-b.md`.

Current bounded result:

- the default deterministic lane did not produce the preregistered outer locking shape;
- removing the implemented `phi`-gradient drift changed the outer proxy by only about `0.263` parts per million;
- the weak outer trace is therefore not evidence for the tested default gradient-feedback mechanism;
- this does not test the `mu` channel, Eq-11 families, collective-relaxation observers, alternative boundaries, or all parameter regimes.

### Q2 — Bounded saturation and genuine attraction

Do any current or historically relevant Lineum equation families exhibit a genuine attracting bounded state under declared perturbations, or do apparent stable regimes reduce to transient metastability, dissipation, numerical clipping, finite observation windows, or observer choice?

The test must distinguish:

- bounded trajectory from attracting fixed point;
- dissipative localized state from globally attracting state;
- physical-model saturation from algorithmic cap or fail-safe;
- return after perturbation from simple amplitude decay;
- a basin of attraction from a single hand-picked initial state.

Required evidence includes the implemented update, analytic or numerical local stability where meaningful, perturbation-return tests, basin sampling, cap-removal checks, timestep and resolution checks, and preserved failures.

Planned child report:

- `research/lineum-bounded-saturation-and-attractor-test.md`.

### Q3 — Scalar minimum and information retention

When the smallest explicit scalar field with a fixed potential minimum is embedded as a research-scoped Lineum adapter, does distinguishable initial information disappear, remain in the complex phase or topology of `psi`, transfer into `phi`, remain in `mu`, or only appear retained because relaxation is incomplete?

This is an information-observer experiment, not a claim about fundamental information conservation in nature.

Required lanes include paired initial states with equal energy and distinct phase or spatial labels, minimum-seeking dynamics, channel-specific readouts, phase randomization, `mu` ablation, long-time extension, resolution checks, and an independently implemented distinguishability metric.

Any adapter remains outside the installable `lineum_core/` public API unless later promotion gates are passed.

Planned child report:

- `research/lineum-scalar-minimum-information-retention-test.md`.

## 3. Cross-cutting compute question

For every lane, record:

- backend and hardware;
- grid size and update count;
- wall-clock runtime;
- convergence or stopping criterion;
- number of expensive reference runs avoided, if any;
- false positive and false negative classifications where a screening task exists;
- uncertainty and unclassified boundary cases.

No acceleration percentage is allowed without an authoritative reference calculation and a blind comparison on held-out cases.

## 4. Common scientific rules

Every child lane must state separately:

1. what the current implementation computes;
2. what the frozen run reproducibly observed;
3. what independent check was performed;
4. what narrow interpretation is supported;
5. what remains hypothesis or analogy;
6. what is and is not connected to real physics.

A visually impressive plot, a green test, a low fit error, or agreement between related observers is not sufficient. Metrics and thresholds must be frozen before the result is seen. Negative, null, contradictory, and inconclusive results remain permanent.

## 5. Shared control requirements

Where applicable, child reports must include:

- mechanism-off ablations;
- shuffled or symmetry-preserving null inputs;
- known-answer toy cases;
- timestep and grid convergence;
- boundary-condition sensitivity;
- seed and noise sensitivity;
- cap and fail-safe audits;
- an independently implemented observer or second numerical path;
- explicit checks for leakage from target data into initialization or metric selection.

## 6. Programme sequencing

The first retained checkpoint was the preregistered galactic radial-locking Lane A/Lane B pair. It used the current engine without adding a new equation and discriminated between active `phi`-gradient feedback and passive smoothing.

Because Lane B reproduced Lane A almost exactly, blind local parameter tuning of the default drift is now prohibited. The next step is mandatory existing-hypothesis retrieval before choosing a replacement mechanism.

The saturation lane and scalar-minimum lane remain active programme questions. Their exact order after retrieval will be selected by the cheapest test that discriminates across the complete inherited mechanism set, not merely by proximity to the latest galaxy result.

## 7. Historical retrieval ledger

### Batch 1 — current canonical whitepaper, retrieved 2026-08-04

Source examined:

- `whitepapers/1-core/01-core-lineum.md` on `develop`;
- source blob SHA: `edc63b0d150b3b616ff8a108ea47a4f89b6a6c37`;
- document title: `Lineum: Eq-7/10 Canonical Stability Audit`;
- document status: Draft;
- document version: `1.0.64.1-core`.

Two scientifically distinct historical candidates were recovered.

#### Candidate H1 — Eq-11 intrinsic saturation

The whitepaper states that an Eq-11 Minimal PDE family used biharmonic regularization and quintic saturation and reported bounded dissipative localized structures without algorithmic clipping. It also states that the amplitude bound was controlled by a saturation parameter and that the structures were dissipative, non-charge-conserving, and phase-sensitive.

Provenance status:

- recorded historical/canonical-document claim;
- not yet independently verified in this programme;
- not the same update family as the current Lane A/B NumPy path;
- directly relevant to Q2 and potentially relevant to Q1 only if a declared radial observer can be derived without fitting the target curve.

Required checks before reuse:

- recover the exact implemented or embedded Eq-11 equation and parameters;
- locate the actual run receipts and cap-removal evidence;
- distinguish bounded localized states from a global or cosmological attractor;
- test whether the saturation term creates any long-range radial scaling rather than only local amplitude control;
- preserve the possibility that the whitepaper wording outruns the available artifacts.

#### Candidate H2 — collective relaxation or stress redistribution

The whitepaper records a Phase 7 kick-and-receiver observation in which the response was described as more consistent with collective relaxation or stress redistribution than with simple ballistic wave transport. The proposed interpretation is an elastic-like spatial medium rather than an empty carrier of isolated traveling fronts.

Provenance status:

- recorded historical interpretation;
- not yet independently verified in this programme;
- mechanistically distinct from the default `phi`-gradient drift that Lane B ruled out under the tested conditions;
- potentially relevant to Q1 because a nonlocal-looking radial response could be an observer of distributed relaxation rather than particle drift;
- potentially relevant to Q3 because information may survive in a distributed stress pattern even when local amplitude relaxes.

Required checks before reuse:

- locate the Phase 7 report, equation, initial conditions, boundary conditions, and raw observables;
- determine whether the response was genuinely collective or merely diffusive smoothing on a periodic grid;
- identify an intervention that separates stress redistribution from ordinary diffusion;
- define a non-circular radial observable before applying it to galaxy-shaped input;
- test finite-size and periodic-image contamination.

### Batch 1 impact matrix

| Programme item | H1 Eq-11 saturation | H2 collective relaxation |
|---|---|---|
| Q1 radial locking | `not_yet_compared`; local saturation alone is insufficient | `reopens`; distinct from failed drift mechanism |
| Q2 bounded attraction | `reopens`; strongest retrieved candidate so far | `constrains`; relaxation is not automatically attraction |
| Q3 information retention | `not_yet_compared`; dissipative loss may be expected | `reopens`; distributed state may retain labels |
| Lane A/B negative result | `unaffected`; different equation family | `supports retrieval`; motivates a different observer/mechanism |
| Physical gravity claim | `unaffected`; no mapping established | `unaffected`; no mapping established |

No candidate in Batch 1 is promoted to a current Lineum mechanism or physical claim.

## 8. Current status matrix

| Question | Protocol | Execution | Independent check | Current status |
|---|---:|---:|---:|---|
| Galactic radial locking | preregistered | Lane A and Lane B complete | two extracted-path reproductions; drift-off intervention | `unsupported_under_tested_conditions` for default drift lane |
| Bounded saturation and attraction | programme-level scope frozen | not run in this programme | historical Eq-11 claim retrieved only | `reopened`, unverified here |
| Scalar minimum and information retention | programme-level scope frozen | not run | no independent check | unresolved |
| Compute reduction | metrics frozen at programme level | no reference benchmark | not applicable yet | unresolved |

## 9. Prohibited conclusions at version 0.2.0

This programme does not establish that:

- Lineum reproduces galactic gravity or removes the need for dark matter;
- Lineum contains a proven global attractor analogous to a cosmological endpoint;
- Eq-11 historical claims are reproduced by the current programme;
- collective relaxation is distinct from diffusion under the relevant conditions;
- Lineum proves information conservation or information loss in nature;
- any Lineum field is a real gravitational, quantum, cosmological, or Standard-Model field;
- Lineum accelerates an external solver by any measured percentage.

## 10. Execution log

1. Programme and galactic protocol created and migrated into Core.
2. Lane A default deterministic run recorded in commit `30cdd87bce6f1596d62019eaebd979ab04292548`; the preregistered radial-locking shape failed.
3. Lane B drift-off intervention recorded in commit `50776c0772340ea7dbf359806dfba9ef165b46db`; removing drift changed the outer response by only about `0.263` parts per million.
4. ClickUp fallback checkpoint for Lane A/B was verified before the connector later reached its rolling limit.
5. ClickUp routing governance was corrected in commit `41d7e16342cd2d4170ccf807f7d4dd60ae1a3aa6`.
6. A later ClickUp checkpoint attempt returned `RATE_LIMIT_EXCEEDED` with a reported wait of `531` minutes. No retry or polling was performed. The rule-governance checkpoint is therefore operationally unsynchronized while Git remains complete.
7. Historical retrieval Batch 1 recovered Eq-11 intrinsic saturation and collective-relaxation candidates from the current canonical whitepaper. No new simulation was run and no replacement mechanism was selected.
