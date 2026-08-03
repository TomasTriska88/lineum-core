# Lineum-Native Field Stress-Test Programme

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** a Lineum-only research programme testing three field-dynamics questions with current and historically relevant Lineum equation families  
**Current confidence:** high in the programme structure; no new simulation result has yet been produced  
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

## 2. Programme questions

### Q1 — Galactic radial locking

Can existing Lineum `psi`–`phi`–`mu` dynamics, initialized from a visible-disk radial profile, generate a robust long-range response whose dimensionless circular-response proxy is approximately constant, without inserting a `1/r` law, fitting the outer observed curve, or adding a dark-halo term?

Active child report:

- `research/lineum-native-galactic-radial-locking-test.md`.

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

The first retained checkpoint is the already preregistered galactic radial-locking Lane A/Lane B pair. It is selected because it uses the current engine without adding a new equation and provides a cheap discriminator between active `phi`-gradient feedback and passive smoothing.

The saturation lane follows after the first radial checkpoint is permanently recorded. The scalar-minimum lane follows after its adapter, observer, and null controls are preregistered in its own report.

This order does not rank the three scientific questions by importance. It minimizes the amount of new mechanism introduced before testing existing Lineum behaviour.

## 7. Current status matrix

| Question | Protocol | Execution | Independent check | Current status |
|---|---:|---:|---:|---|
| Galactic radial locking | preregistered | not run | not run | implemented protocol only |
| Bounded saturation and attraction | programme-level scope frozen | not run | not run | unresolved |
| Scalar minimum and information retention | programme-level scope frozen | not run | not run | unresolved |
| Compute reduction | metrics frozen at programme level | no reference benchmark | not applicable yet | unresolved |

## 8. Prohibited conclusions at version 0.1.0

This programme does not establish that:

- Lineum reproduces galactic gravity or removes the need for dark matter;
- Lineum contains a proven global attractor analogous to a cosmological endpoint;
- Lineum proves information conservation or information loss in nature;
- any Lineum field is a real gravitational, quantum, cosmological, or Standard-Model field;
- Lineum accelerates an external solver by any measured percentage.

## 9. Execution log

At version 0.1.0, the programme report and the migrated galactic child protocol are the only retained outputs. No new simulation has yet been executed under this programme.