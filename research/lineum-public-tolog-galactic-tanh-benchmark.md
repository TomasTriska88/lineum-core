# Lineum Public-TOLOG Galactic `tanh` Benchmark

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** public-source-only reproduction and reverse-engineering benchmark for the published TOLOG galactic hyperbolic-tangent fit, retained as an external Q1 comparator rather than Lineum physics  
**Central question:** what does the publicly described `tanh` model actually achieve on public SPARC data, which parts of its behaviour are inserted by functional form or fitting freedom, and which general response properties would an emergent Lineum foam/field/vortex mechanism need to replace?  
**Current confidence:** high in the provenance of the public equation and official SPARC source; low in the reported numerical performance until independently reproduced under declared data and parameter conventions

## 1. Root programme and inherited evidence

This report belongs to the Lineum-native three-question programme:

1. emergent galactic long-range radial response;
2. natural bounded saturation and genuine attraction;
3. information retention during relaxation toward a common coarse state.

Inherited results that remain binding:

- the first current-Lineum radial lane failed its preregistered outer-locking criteria;
- disabling the implemented `phi`-gradient drift changed the outer proxy by only about `0.263` parts per million;
- the tested default drift is therefore unsupported as the material source of the weak outer trace under those conditions;
- `mu`, historical Eq-11 saturation, distributed foam-like relaxation, phase/topology, alternative boundaries, and a central-vortex source remain untested or unresolved for Q1;
- no current Lineum field is empirically identified with gravity.

The public galactic `tanh` model was previously classified as a useful positive-shape comparator whose outer saturation is partly inserted by construction. This report does not reverse that classification. It creates a working external benchmark so that the inserted response can be measured, decomposed, and eventually replaced rather than merely discussed.

## 2. Project-owner decision and intended workflow

The project owner selected the following engineering strategy on `2026-08-04`:

> First build a machine known to work, then progressively disassemble it and determine which response properties must be reproduced emergently by Lineum.

Operational translation:

1. independently implement the exact publicly described galactic formula;
2. reproduce it on public astronomical data;
3. separate the contribution of the baryonic baseline, plateau amplitude, transition radius, saturating shape, and per-galaxy fit freedom;
4. introduce controlled ablations and alternative saturators;
5. map each necessary response property to candidate Lineum mechanisms;
6. replace the external fit term only in research lanes, never by silently inserting it into the Lineum engine;
7. require the final Lineum candidate to work after the galactic `tanh` term has been removed completely.

This benchmark is scaffolding, not the final bridge.

## 3. Strict public-source and anti-copying boundary

The privately uploaded TOLOG document is excluded completely.

This report and every later executable lane under it must not:

- read or cite the uploaded private file;
- copy or paraphrase its wording;
- import equations, parameters, datasets, plots, tables, code, result values, or conclusions from it;
- reconstruct private content from memory;
- use private terminology or numerical details as search hints unless they are independently present in the public record;
- treat similarity to private material as corroboration.

A TOLOG item may enter the benchmark only when independently recovered from a stable public source. Each imported item must record:

- public title or description;
- named author or publisher where available;
- stable public URL;
- access date;
- exact claim, equation, parameter, or procedure being imported;
- what remains missing or ambiguous.

Public availability also does not imply permission to copy prose or software. The executable benchmark will be an original clean-room implementation of the publicly stated mathematics. No TOLOG source code will be copied. If a public code release is later found, its licence and provenance must be audited before comparison.

## 4. Public source inventory used at preregistration

### Source T-G1 — public author profile and uploaded technical material

- public profile title: `Patrik Tolog - Independent Researcher`;
- author: Patrik Tolog;
- publisher: Academia.edu public profile;
- URL: `https://independent.academia.edu/PatrikTolog`;
- access date: `2026-08-04`;
- source class: author-controlled public material, not treated as independent peer review.

Publicly recovered galactic model:

`v_model(r) = sqrt(v_bar(r)^2 + V0^2 * tanh(k_eff * r / r_s))`.

Publicly recovered baryonic expression:

`v_bar(r) = sqrt(v_gas(r)^2 + v_disk(r)^2 + v_bulge(r)^2)`.

Publicly described fitting procedure and values:

- fixed example scale `r_s = 5.0`;
- fit `V0` and `k_eff` by nonlinear least squares;
- reduced chi-squared denominator stated as `N - 2`;
- claimed NGC 3198 reduced chi-squared near `1.5` in one public upload;
- claimed median reduced chi-squared near `1.8` across a broader sample in another public upload;
- claimed fitted scaling `V0 proportional to M_bar^0.25`;
- reported low-surface-brightness outliers with reduced chi-squared above `5`;
- publicly acknowledged need for refined scaling involving baryonic mass or surface density.

Publicly recovered functional interpretation:

- approximately linear added response at small argument;
- saturation at large argument;
- finite central added contribution;
- `V0` controls the saturation amplitude;
- `k_eff / r_s` controls how rapidly the plateau is approached.

Not publicly resolved at preregistration:

- complete machine-readable multi-galaxy parameter table;
- exact fit bounds and initialization policy;
- whether all public runs used identical baryonic mass-to-light conventions;
- treatment of signed gas contributions in SPARC files;
- complete outlier and exclusion policy;
- covariance treatment;
- exact definition of the separately reported `94.2%` cusp-core accuracy;
- a public derivation of this formula from the declared `3 x 3` oscillator or stabilization grid.

The `94.2%` value is therefore not an executable target in version `0.1.0`.

### Source T-G2 — public cosmology proposal

- title: `Saturation Dynamics and Grid Resonance: A Phenomenological Alternative to Dark Matter and Dark Energy`;
- author: Patrik Tolog;
- publisher: aiXiv;
- displayed version: `v1.0`;
- displayed date: `2026-03-28`;
- URL: `https://aixiv.science/abs/aixiv.260328.000002`;
- access date: `2026-08-04`;
- source class: author-submitted public proposal.

This source publicly describes a phenomenological `3 x 3` stabilizing grid involving Curvature, Energy Density, and Scalar Field components and claims phenomenological consistency with SPARC, supernova, and BAO observations. It also states that reproducing the full CMB power spectrum remains unresolved.

Allowed use here:

- provenance for the broad public saturation programme;
- evidence that the galactic formula is presented as phenomenological;
- reminder that a velocity fit is not a full cosmological or gravitational theory.

It does not supply a recovered derivation from local grid dynamics to the galactic `tanh` expression.

### Source G1 — official SPARC database

- title: `SPARC: Spitzer Photometry & Accurate Rotation Curves`;
- maintainers: Federico Lelli, Stacy McGaugh, and James Schombert;
- URL: `https://astroweb.case.edu/SPARC/`;
- access date: `2026-08-04`;
- intended dataset: official `Rotmod_LTG.zip` Newtonian mass-model archive;
- direct public archive URL to be verified and hashed at execution: `https://astroweb.case.edu/SPARC/Rotmod_LTG.zip`.

The official site describes SPARC as `175` late-type galaxies with Spitzer photometry, high-quality HI/H-alpha rotation curves, and Newtonian baryonic mass models.

### Source G2 — SPARC master paper

- title: `SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves`;
- authors: Federico Lelli, Stacy S. McGaugh, James M. Schombert;
- year: `2016`;
- journal: `The Astronomical Journal 152, 157`;
- DOI: `10.3847/0004-6256/152/6/157`;
- arXiv: `1606.09251`;
- URL: `https://arxiv.org/abs/1606.09251`;
- access date: `2026-08-04`.

## 5. Benchmark classification

The benchmark is an **external phenomenological comparator**.

It is not:

- a Lineum equation;
- a proposed replacement for Lineum Core;
- evidence that TOLOG local dynamics generate the formula;
- evidence that the formula is a unique physical explanation;
- a licence to fit Lineum directly to one target galaxy;
- a whitepaper claim.

No file under `lineum_core/` will be changed by this lane. Executable research code, if retained, belongs under `research/runners/` and remains subordinate to this standalone report.

## 6. Functional anatomy to reverse-engineer

The public formula is decomposed into five operational parts.

### Part A — baryonic baseline

`v_bar(r)` provides the visible-matter contribution from gas, disk, and bulge data.

Question for reverse engineering:

- what source information is already supplied before the added field term acts?

Lineum replacement target:

- a declared mapping from visible source distribution into initial or driven `psi`, `phi`, `mu`, foam stress, or vortex conditions without using the observed total velocity as an input.

### Part B — plateau amplitude

`V0` sets the asymptotic added velocity scale.

Question for reverse engineering:

- is successful fitting mostly the result of choosing an independent amplitude for each galaxy?

Lineum replacement target:

- an outer-response amplitude emerging from source mass, scale, surface density, history, foam loading, or another measured input under one frozen law rather than a free per-galaxy dial.

### Part C — transition scale

The ratio `r_s / k_eff` controls where the added response changes from approximately rising to approximately saturated.

Question for reverse engineering:

- is successful fitting mostly the result of choosing a separate transition radius for each galaxy?

Lineum replacement target:

- a transition scale generated by source geometry, collective relaxation length, foam stiffness, a central vortex, or another independently measurable property.

### Part D — saturating shape

`tanh` guarantees a smooth monotonic approach to a finite plateau.

Question for reverse engineering:

- is the exact `tanh` shape necessary, or is almost any two-parameter monotonic saturator sufficient?

Lineum replacement target:

- a radial response produced by local dynamics and boundary-independent collective behaviour, not by inserting the final saturating curve.

### Part E — fitting freedom

The public procedure fits at least `V0` and `k_eff` to each target curve.

Question for reverse engineering:

- how much of the fit quality survives when one or both quantities are predicted from baryonic inputs or frozen globally?

Lineum replacement target:

- held-out prediction with universal dynamics and tightly classified nuisance parameters.

## 7. Owner foam and central-vortex hypothesis

The project owner requested that the following existing Lineum concepts remain active candidates:

- Lineum as a foam-like, collectively deformable spatial medium;
- a galactic centre that may contain a strong Lineum vortex;
- the possibility that a central Lineum vortex is an analogue of a central black hole;
- distributed foam stress or relaxation as a source of broad radial response;
- retained field or topological history as a possible contributor to galaxy assembly dependence.

These are hypotheses, not established results.

Potential benchmark mapping:

| Public benchmark property | Candidate Lineum replacement hypothesis |
|---|---|
| baryonic baseline | visible-source loading of the Lineum foam |
| fitted plateau amplitude `V0` | total foam deformation or conserved/distributed stress set by source mass |
| fitted transition scale `r_s / k_eff` | source scale length, foam relaxation length, or central-vortex influence radius |
| monotonic saturation | nonlinear collective redistribution or bounded vortex/foam response |
| finite central behaviour | regular vortex core or intrinsic nonlinear saturation rather than numerical clipping |
| per-galaxy adaptation | source-sensitive emergent response without observed-velocity fitting |
| possible history dependence | `phi`, `mu`, phase, or topological memory of assembly |

A central-vortex lane must later distinguish:

- a vortex supplied by hand from a vortex that forms dynamically;
- the compact central contribution from the extended galactic response;
- ordinary baryonic central mass from a genuinely new field effect;
- a finite numerical core from a relativistically regular black-hole geometry;
- correlation with a central vortex from causal necessity.

No black-hole equivalence is tested by the present benchmark.

## 8. Frozen first execution stages

### B0 — public-data provenance receipt

1. Download the official SPARC `Rotmod_LTG.zip` archive from the official site.
2. Record URL, retrieval time, byte length, archive SHA-256, and member list.
3. Extract only `NGC3198_rotmod.dat` for the first fit.
4. Record the exact file bytes, SHA-256, header, row count, columns, and finite-value checks.
5. Do not substitute rows copied from a TOLOG upload when the official source is available.

Failure conditions:

- official archive unavailable;
- target member absent;
- ambiguous column interpretation;
- hash or row receipt not retained.

### B1 — analytic known-answer audit

For nonnegative `x`, verify independently that:

- `tanh(0) = 0`;
- the small-`x` response approaches `x`;
- the large-`x` response approaches `1`;
- the added velocity-squared term approaches `V0^2`;
- the characteristic half-saturation location is derived and checked numerically;
- the implementation remains finite at the centre.

Known-answer arrays must be generated without SPARC data.

### B2 — literal public-formula NGC 3198 fit

Use the publicly described literal baryonic convention:

`v_bar_literal = sqrt(v_gas^2 + v_disk^2 + v_bulge^2)`.

Use:

- fixed `r_s = 5.0 kpc` as publicly displayed;
- nonnegative `V0`;
- positive `k_eff`;
- tabulated `V_obs` and tabulated velocity uncertainty;
- deterministic bounded least-squares with a preregistered multi-start schedule;
- reduced chi-squared denominator `N - 2`.

The initial bounded search domain is frozen as:

- `V0 in [0, 400] km/s`;
- `k_eff in [1e-6, 100]`;
- logarithmic initial `k_eff` values `[0.01, 0.1, 1, 10]`;
- initial `V0` values `[25, 75, 150, 250] km/s`;
- retain the lowest objective only when all converged starts agree on the fitted curve within declared tolerance or report multimodality.

This wide numerical domain is an independent implementation choice, not a recovered TOLOG parameter bound.

### B3 — baryonic-convention sensitivity

SPARC gas contributions may carry a sign, and stellar contributions normally require a declared mass-to-light convention. The literal public expression squares all listed components and may not match every standard SPARC mass-model convention.

Before interpreting fit disagreement, run separately labelled controls:

1. literal public squaring convention;
2. signed-gas convention using `sign(v_gas) * v_gas^2`;
3. declared stellar mass-to-light scalings recovered from the SPARC documentation or master paper;
4. no silent mixing of conventions.

Any control not supported by an authoritative source remains deferred rather than guessed.

### B4 — shape ablations

Fit the same NGC 3198 data using the same baryonic convention and parameter accounting with:

1. baryons only;
2. fully saturated constant added velocity-squared term;
3. unsaturated linear small-argument approximation;
4. the public `tanh` model;
5. a two-parameter rational saturator `x / (1 + x)`;
6. a two-parameter arctangent saturator normalized to the same plateau.

Purpose:

- determine whether fit quality depends specifically on `tanh` or mainly on generic monotonic saturation plus two free dials.

Alternative saturators are independent controls, not proposed TOLOG content and not Lineum equations.

### B5 — parameter-freeze stress test

After the one-galaxy fit is understood, freeze one part at a time:

- fix the transition scale while refitting amplitude;
- fix amplitude while refitting transition scale;
- derive simple candidate predictors from baryonic properties only on a declared training subset;
- evaluate on untouched held-out galaxies;
- compare against null models with equal flexibility.

No population-emergence claim is allowed from NGC 3198 alone.

## 9. Preregistered metrics

Record for every lane:

- number of data points `N`;
- number of fitted parameters;
- chi-squared;
- reduced chi-squared using the declared degrees of freedom;
- weighted root-mean-square residual;
- unweighted root-mean-square residual;
- maximum absolute residual;
- Akaike information criterion where likelihood assumptions are declared;
- fitted values and covariance or profile uncertainty where identifiable;
- convergence count across starts;
- boundary contact;
- residuals versus radius;
- inner, transition, and outer-region metrics using boundaries frozen before fit inspection.

A visually flat curve is not a metric.

## 10. First-fit decision thresholds

### `public_metric_reproduced`

All of the following hold:

- B0 and B1 pass;
- all retained starts converge to observationally equivalent curves;
- no fitted parameter is pinned to a search boundary;
- the literal public formula produces NGC 3198 reduced chi-squared within `0.15` of the publicly stated value near `1.5`;
- the reported convention is explicitly identified.

### `functional_benchmark_reproduced_but_public_metric_differs`

All of the following hold:

- B0 and B1 pass;
- the model materially improves over the baryon-only baseline;
- the fit is stable and finite;
- reduced chi-squared differs from the public value by more than `0.15`;
- at least one public convention needed for exact replication remains ambiguous or the independently recovered data produce a different result.

### `not_reproduced_under_declared_conditions`

- provenance and numerical gates pass;
- the public model does not materially improve over the baseline, is unstable, or produces a substantially different metric under a fully declared convention;
- no unresolved missing convention plausibly explains the difference.

### `inconclusive`

- official data or column meaning cannot be verified;
- fit results are materially multimodal;
- missing mass-to-light, sign, exclusion, or uncertainty conventions prevent a fair comparison;
- the target public metric lacks an operational definition.

The `94.2%` cusp-core value remains `not_testable_from_public_definition` unless a public operational metric is recovered.

## 11. Anti-cheat and independence controls

The benchmark rejects or downgrades a result when:

- observed total velocity is used to construct the source term beyond fitting the declared comparator;
- parameters are manually altered after viewing residuals without a new preregistered lane;
- target rows are copied from TOLOG material instead of the official SPARC archive;
- a post-hoc radial exclusion improves the score;
- the public formula and an alternative control receive unequal parameter freedom;
- the same implementation is called an independent check;
- `tanh` fit success is described as emergence;
- a good one-galaxy fit is described as a population law;
- a finite central velocity is described as a regular black hole;
- Lineum is altered to reproduce the fitted curve before the comparator anatomy is measured.

Independent checks required before a retained numerical conclusion:

- one direct NumPy implementation;
- one separately written scalar or alternative-vector implementation of the public formula;
- analytic small- and large-radius checks;
- deterministic multi-start agreement;
- direct recomputation of chi-squared from retained residuals;
- exact input and output hashes.

## 12. Reverse-engineering outcome matrix

| Observed benchmark result | Allowed interpretation | Lineum consequence |
|---|---|---|
| `tanh` clearly beats baryons and simpler one-parameter plateau | a transition-scale degree of freedom is useful for this target | Lineum must generate both an amplitude and a source-sensitive radial scale |
| constant plateau performs similarly | most fit power comes from an added outer amplitude | prioritize emergent mass-amplitude scaling before exact transition shape |
| rational and arctangent saturators perform similarly | `tanh` is not uniquely selected by the fit | reverse-engineer generic saturation, not the literal function |
| only `tanh` performs well under equal freedom | its detailed transition shape carries target-specific information | identify which local Lineum dynamics could generate that shape without inserting it |
| fit depends strongly on baryonic convention | public replication is convention-sensitive | resolve source mapping before any Lineum comparison |
| per-galaxy dials dominate | fit is descriptive rather than population-predictive | freeze amplitude and scale from source properties before claiming emergence |
| public metric cannot be reproduced | either conventions are missing or the reported result differs | preserve the discrepancy; do not tune Lineum to an unverified target |

## 13. Cross-question impact matrix

| Programme item | Benchmark impact |
|---|---|
| Q1 galactic response | `supports`: supplies a functional target and decomposes inserted fit freedom |
| Q2 saturation and attraction | `constrains`: `tanh` boundedness is explicit saturation, not a demonstrated attractor |
| Q3 information retention | `unaffected`: the public galactic formula contains no declared memory observer or source-off history test |
| current `phi`/`mu` preflight | `unaffected`: remains open for full held-out and causal tests |
| historical Eq-11 | `not_yet_compared`: may later replace generic local saturation but must still produce long range |
| foam-like collective relaxation | `reopens`: candidate generator of transition scale and extended response |
| central Lineum vortex | `reopens`: candidate source of central organization or scale, not yet tested |
| default Lineum drift negative result | `unaffected`: remains unsupported under tested conditions |
| SPARC population anchors | `depends_on`: one-galaxy benchmark cannot satisfy population constraints |

## 14. Whitepaper and equation handoff

No whitepaper or equation change is authorized by this benchmark.

Future canonical wording may be considered only after:

- the public comparator is reproduced or its discrepancy is bounded;
- one or more Lineum-native mechanisms replace the external term completely;
- synthetic mass scaling and inner diversity pass without target leakage;
- held-out SPARC evaluation and parameter accounting are complete;
- the physical bridge is explicit and appropriately limited.

The benchmark may ultimately show only how a flexible fit works. That remains a valid research result.

## 15. Immediate next step

Execute only B0 and B1 first:

1. retrieve and hash the official SPARC archive and NGC 3198 member;
2. verify the public formula analytically and numerically on known-answer inputs;
3. append complete code, commands, environment, machine-readable output, failures, and narrow verdict to this report;
4. commit that checkpoint before running the first astronomical fit.

No astronomical optimization is permitted before the B0/B1 receipt is committed.

## 16. Prohibited conclusions at version 0.1.0

This report does not establish that:

- the public TOLOG fit is numerically reproduced;
- the public `94.2%`, `1.5`, or `1.8` values are independently verified;
- TOLOG derives its galactic formula from local grid dynamics;
- Lineum reproduces galaxy rotation curves;
- foam or vortex behaviour explains dark matter observations;
- a central Lineum vortex is a black hole;
- `tanh` should be inserted into the Lineum equation;
- dark matter is absent;
- any current Lineum mechanism is superior to TOLOG, MOND, dark-matter models, or general relativity.
