# Research Directory Instructions

All research work in this directory remains subject to the repository-wide instructions in the root `AGENTS.md`, `.agent/rules.md`, every binding supplement under `.agent/rules.d/`, and the applicable workflows under `.agent/workflows/`.

## B4 exact three-question owner scope lock

This section applies to all analysis, planning, experiments, runners, results, report edits, interpretation, and future mechanism development associated with:

- `research/lineum-public-tolog-galactic-shape-b4.md`;
- its B4 runners and retained outputs;
- any successor or superseding report that continues the same three-question programme.

The programme is controlled by exactly the following three owner questions. Their material anchors must not be weakened, silently generalized, replaced by easier proxies, or treated as already established.

### Question 1 — autonomous astrophysical emergence

How can the Lineum grid handle real astrophysical objects, including galactic rotation, without manually supplying galaxy-specific numerical output values? Can at least `98%` agreement emerge without a dark-matter component, using only independently defensible source and initial conditions?

An affirmative closure requires all of the following:

1. the meaning and metric of `98% agreement` are frozen before held-out evaluation;
2. only independently observable source and initial conditions are supplied;
3. observed rotation velocities or equivalent target information are not leaked into inputs, initialization, calibration, stopping rules, observer choice, or post-processing;
4. galaxy-specific output parameters are not fitted after seeing each target curve;
5. the tested model contains no dark-matter component or hidden fitted surrogate that merely renames one;
6. universal parameters are frozen before evaluation on held-out real galaxies;
7. the result survives appropriate baryonic, calibration, observer, resolution, and conventional-model controls;
8. an independent implementation or equivalent adversarial reproduction confirms the exact bounded claim.

A fitted macroscopic curve, a descriptive resemblance, one calibrated galaxy, or agreement measured on training data cannot close this question.

### Question 2 — natural saturation and divergence control

How does Lineum achieve natural saturation and stop divergence, including in the limit `r -> 0` or its explicitly declared discrete-grid equivalent? Does the implemented dynamics contain a fixed mathematical attractor comparable to the public Dark Heart comparison target, or does the grid enter persistent oscillation and require software noise, clipping, caps, resets, or ad hoc damping to remain bounded?

An affirmative closure requires all of the following:

1. `r -> 0` is translated into a frozen, physically and numerically meaningful test rather than avoided by grid resolution;
2. a finite fixed attractor, its basin, and its return behavior are defined mathematically;
3. the state remains bounded and returns after perturbation without requiring stochastic forcing, hard clipping, caps, emergency reset, or an absorbing software guard;
4. any dissipative term used as part of the claimed mechanism is explicit in the governing equation, physically or mathematically justified, and separated from numerical fail-safes by ablation;
5. persistent oscillation, slow drift, cap-supported stationarity, and finite-horizon survival are not mislabeled as convergence to a fixed attractor;
6. the result survives time-step, resolution, stencil, boundary, initialization, horizon, and perturbation controls;
7. independent verification reproduces the attractor and distinguishes it from inserted numerical containment.

The labels `Dark Heart` and any associated third-party performance claim are comparison targets only. They are not Lineum evidence unless lawful public material supports an independent, reproducible comparison.

### Question 3 — scalar potential memory on a 256 x 256 grid

When the Lineum `256 x 256` grid primarily evolves complex and auxiliary fields, how can it integrate a genuinely real scalar field with a fixed potential minimum that preserves information against decay?

An affirmative closure requires all of the following:

1. the test runs on the exact `256 x 256` grid, with scaling and boundary assumptions declared;
2. the scalar degree of freedom is explicitly defined and is not accepted merely because an existing array stores real numbers or because a complex magnitude can be plotted as a scalar;
3. an explicit potential and its fixed stable minimum are defined, including units or dimensionless normalization and the evolution law derived from it;
4. a localized information-bearing state persists after the writing source is completely removed;
5. after positive and negative perturbations, the state returns toward the predeclared minimum rather than merely decaying slowly, remaining frozen by a cap, or requiring continued driving;
6. information retention is measured by a frozen non-circular observable and attacked with destructive, shuffled, null, and source-off controls;
7. the result survives resolution, time-step, boundary, duration, initialization, and numerical-guard checks;
8. independent verification reproduces the persistence and return behavior.

A slowly fading trace, a continuously driven pattern, a clipped field, or a scalar-valued helper array without a demonstrated potential minimum cannot close this question.

## Positive programme destination without confirmation bias

The B4 development destination is to implement and independently validate affirmative answers to all three exact questions. The programme must not stop merely because the current implementation fails. Every verified negative result must remain visible and be converted into a bounded blocker, a missing-mechanism record, competing repair classes, and the cheapest frozen discriminator for the next repair.

This positive destination does not authorize a predetermined positive verdict. Thresholds, metrics, inputs, exclusions, observers, or interpretations must never be changed after result inspection merely to obtain a pass. A question remains open until its complete affirmative closure gate is satisfied by reproducible evidence.

## Mandatory lane mapping and anti-drift rule

Before any consequential B4 experiment or report addition, state which exact question it addresses and classify its contribution as one of:

- direct closure evidence;
- prerequisite evidence;
- blocker localization;
- candidate repair discrimination;
- independent verification;
- real-physics connection;
- scope limitation.

Work that cannot be mapped materially to at least one of the three exact questions must not be added to the B4 programme. Interesting side findings belong in a separately scoped research record.

The current localized L1 saturation lane maps directly to Question 2. It may identify prerequisites for Question 3, but it cannot close Question 3 because it does not yet demonstrate the required `256 x 256` scalar potential memory. It provides no direct closure evidence for Question 1.

The active B4 report must preserve the exact anchors `98%`, no dark matter, source-and-initial-condition-only emergence, `r -> 0`, a fixed mathematical attractor, the Dark Heart comparison boundary, oscillation and software-noise alternatives, the `256 x 256` grid, a genuinely real scalar field, a fixed potential minimum, and information survival. Shorthand may be used only when the complete scope remains explicit elsewhere in the same standalone report.

Do not declare the B4 programme complete, validated, or positively answered until all three affirmative closure gates above are satisfied. Changing these controlling questions or their material anchors requires explicit project-owner approval and a versioned scope change that preserves this history.
