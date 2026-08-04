# Lineum Galactic Observational Anchor Map

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** authoritative observational anchors that any Lineum-native galactic-response mechanism must confront before an empirical claim is allowed  
**Central question:** what must emerge from Lineum beyond a visually flat outer curve in one galaxy?  
**Current confidence:** high in the source provenance and target definitions; no Lineum mechanism is empirically connected by this report alone

## 1. Report lineage

Root programme:

- `research/lineum-native-field-stress-tests.md`;
- root version inherited: `0.2.1`;
- root evidence cutoff: `2026-08-04`.

Immediate predecessor:

- `research/lineum-universe-emergence-evidence-map.md`;
- predecessor version inherited: `0.2.0`;
- predecessor commit: `03451e8c17872b500179aa80c0743e48b4274629`;
- predecessor result: the first public TOLOG inventory separated oscillator dynamics, an explicitly fitted galactic `tanh` term, cosmological phenomenology, and information/stability claims. No public derivation linking those layers was recovered.

Repository checkpoint before this report:

- repository: `TomasTriska88/lineum-core`;
- branch: `develop`;
- branch head: `03451e8c17872b500179aa80c0743e48b4274629`.

## 2. Purpose

This report freezes the first real-universe target set for Q1, the emergent galactic radial-response question.

The purpose is to prevent a weak success criterion such as:

> a fitted curve looks approximately flat for NGC 3198.

A candidate Lineum mechanism must instead be tested against population-level regularities and diversity that constrain both the outer amplitude and the inner shape of galaxy rotation curves.

## 3. Source hierarchy

This batch uses primary papers and the official SPARC data site.

### Source G1 — official SPARC database

- title: `SPARC: Spitzer Photometry & Accurate Rotation Curves`;
- maintained by: Federico Lelli, Stacy McGaugh, and James Schombert;
- URL: `https://astroweb.case.edu/SPARC/`;
- access date: `2026-08-04`;
- source class: official public dataset and project page.

The official site describes SPARC as a public database of `175` late-type galaxies with:

- Spitzer `3.6 micron` photometry tracing stellar mass distribution;
- high-quality `HI` plus `H-alpha` rotation curves tracing the gravitational potential to large radii;
- Newtonian baryonic mass models;
- broad ranges of stellar mass, surface brightness, morphology, and gas fraction;
- published data products for the baryonic Tully-Fisher relation and radial acceleration relation.

Scientific use in this programme:

- population-level held-out testing;
- source profiles and observed rotation curves;
- quality flags and original-data references;
- baryonic contribution decomposition;
- explicit propagation of distance, inclination, and stellar mass-to-light uncertainty where available.

### Source G2 — SPARC master paper

- title: `SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves`;
- authors: Federico Lelli, Stacy S. McGaugh, James M. Schombert;
- journal: The Astronomical Journal `152`, 157;
- year: `2016`;
- DOI: `10.3847/0004-6256/152/6/157`;
- arXiv: `1606.09251`;
- stable paper URL: `https://arxiv.org/abs/1606.09251`;
- access date: `2026-08-04`.

The paper introduces `175` nearby galaxies spanning wide ranges in morphology, luminosity, surface brightness, and gas fraction, and supplies detailed baryonic mass models.

Scientific consequence:

- one galaxy cannot establish universality;
- a useful Lineum mechanism must be exposed to broad variation in baryonic mass, scale length, surface density, and gas fraction;
- a single fixed stellar mass-to-light assumption may be acceptable for a controlled first pass but must be varied or marginalized before a physical claim.

### Source G3 — radial acceleration relation

- title: `Radial Acceleration Relation in Rotationally Supported Galaxies`;
- authors: Stacy S. McGaugh, Federico Lelli, James M. Schombert;
- journal: Physical Review Letters `117`, 201101;
- year: `2016`;
- DOI: `10.1103/PhysRevLett.117.201101`;
- arXiv: `1609.05917`;
- stable paper URL: `https://arxiv.org/abs/1609.05917`;
- access date: `2026-08-04`.

The reported relation uses `2693` radial points in `153` galaxies and correlates observed radial acceleration with the acceleration predicted from the observed baryonic distribution. The reported scatter is small and is argued to be largely observational.

Scientific consequence:

- a candidate mechanism must predict a point-by-point relation between source distribution and total response, not only a terminal velocity;
- a successful outer plateau with incorrect inner acceleration is insufficient;
- per-galaxy free response curves can trivially obscure this constraint and therefore require strict parameter accounting.

### Source G4 — baryonic Tully-Fisher relation

- title: `The Small Scatter of the Baryonic Tully-Fisher Relation`;
- authors: Federico Lelli, Stacy S. McGaugh, James M. Schombert;
- journal: The Astrophysical Journal Letters `816`, L14;
- year: `2016`;
- DOI: `10.3847/2041-8205/816/1/L14`;
- arXiv: `1512.04543`;
- stable paper URL: `https://arxiv.org/abs/1512.04543`;
- access date: `2026-08-04`.

The study uses `118` high-quality disk galaxies with extended rotation curves and Spitzer photometry. It reports a slope near `4` for reasonable stellar mass-to-light choices and an intrinsic scatter of about `0.1 dex` or less.

Operational target:

- the asymptotic velocity scale should approximately obey `M_bar proportional to V_flat^4`, equivalently `V_flat proportional to M_bar^(1/4)`, within a declared calibration and uncertainty model;
- a model that fits each galaxy with an independent free amplitude does not predict this relation;
- any apparent relation derived after fitting the amplitude separately to every target must be compared with a null model of the same flexibility.

### Source G5 — diversity of inner rotation curves

- title: `The Unexpected Diversity of Dwarf Galaxy Rotation Curves`;
- authors: Kyle A. Oman et al.;
- journal: Monthly Notices of the Royal Astronomical Society `452`, 3650-3665;
- year: `2015`;
- DOI: `10.1093/mnras/stv1504`;
- arXiv: `1504.01437`;
- stable paper URL: `https://arxiv.org/abs/1504.01437`;
- access date: `2026-08-04`.

The paper reports large observed diversity in inner rotation-curve shapes among dwarf galaxies even at similar maximum rotation velocity. It frames the issue more usefully as an inner mass-deficit diversity problem rather than only a cusp-versus-core density-slope label.

Scientific consequence:

- a universal response that produces nearly identical normalized inner profiles is insufficient;
- source surface density, spatial structure, feedback history, non-circular motions, or another declared state variable may need to control the inner response;
- an added saturating term that automatically gives one smooth shape can pass outer flatness while failing inner diversity.

## 4. Four mandatory observational constraints

### Constraint O1 — population coverage

The mechanism must be tested on a broad population spanning mass, scale length, surface brightness, gas fraction, and morphology.

Minimum future empirical test:

- frozen training, validation, and held-out galaxy partitions;
- no target leakage through post-hoc exclusions;
- quality-based exclusions defined before model results are inspected;
- exact accounting of nuisance parameters and per-galaxy freedoms.

### Constraint O2 — pointwise baryon-response relation

The mechanism must produce the correct relation between local baryonic source strength and total inferred acceleration across radii.

A flat terminal curve alone does not satisfy this constraint.

### Constraint O3 — global mass-velocity scaling

The same frozen mechanism must produce the population scaling between total baryonic mass and asymptotic velocity.

A separately fitted amplitude for each galaxy cannot be counted as an emergent prediction of this relation unless the amplitude itself is derived from independently measured source properties by a frozen law.

### Constraint O4 — inner-shape diversity

The mechanism must allow different inner response shapes at similar outer velocity without arbitrary curve-by-curve sculpting.

This is a crucial discriminator between:

- a universal fitted saturation profile;
- source-sensitive field dynamics;
- boundary or resolution artifacts;
- genuine environmental or history dependence.

## 5. Implication for the first public TOLOG comparator

The public TOLOG galactic expression recovered in the predecessor report has the form:

`v(r)^2 = v_bar(r)^2 + V0^2 * tanh(k_eff * r / r_s)`.

The public description fits `V0` and `k_eff`, while the `tanh` form inserts an asymptotically constant velocity-squared contribution.

Within this programme, that expression is classified as:

- a useful positive-shape comparator;
- a useful demonstration of how a model can fit outer flatness by construction;
- not yet a recovered emergence result from the public oscillator lattice;
- insufficient by itself for O2, O3, and O4 without a universal parameter law and population-level validation.

This classification does not assert that the fit is numerically wrong. It limits what the public equation can establish causally.

## 6. Consequence for Lineum experiment design

The next Lineum galactic experiment must not begin with NGC 3198 fitting. It must first ask whether the native dynamics generate the two most informative population properties on synthetic source families.

### Synthetic family requirement

Generate declared, analytic baryonic source profiles that vary independently in:

- total source mass;
- radial scale length;
- central surface density;
- gas-like extended fraction;
- optional bulge-like compact fraction.

The source family must be generated without observed velocity data.

### Candidate internal observables

No observer is frozen yet. Candidate observers to audit include:

- radial gradients of `phi`;
- radial gradients of `mu`;
- combined energy or stress redistribution;
- phase-gradient or collective-relaxation response;
- Eq-11-family field-energy response.

Each candidate must be dimensionless first and must pass known-answer and null controls before any mapping to velocity.

### First two synthetic discriminators

1. **Mass-scaling discriminator** — does the outer response amplitude scale systematically with total source mass, and is any exponent stable across scale length and resolution?
2. **Surface-density diversity discriminator** — at similar outer amplitude, do different source surface densities produce meaningfully different inner response shapes without retuning the equation?

These two tests jointly target O3 and O4 before observational fitting.

## 7. Parameter-freedom policy

Before any SPARC fit, every parameter must be classified as one of:

- universal Lineum parameter fixed for all runs;
- measured galaxy input;
- nuisance parameter with an external prior, such as distance or inclination;
- calibration parameter fixed on a training subset;
- prohibited per-galaxy free parameter.

A claim of universal emergence is prohibited when each galaxy receives an unconstrained amplitude and radial scale.

The number of fitted degrees of freedom, prior volume, and model-selection penalty must be reported alongside residual error.

## 8. Error and systematics policy

Future empirical tests must account for, or explicitly bracket:

- observational velocity uncertainty;
- distance uncertainty;
- inclination uncertainty;
- stellar mass-to-light uncertainty;
- beam smearing and spatial resolution;
- non-circular motions;
- asymmetric drift where relevant;
- quality flags and radial covariance when available.

A low root-mean-square velocity error calculated with only tabulated point errors is not a complete uncertainty analysis.

## 9. Staged validation ladder for Q1

### G0 — analytic and numerical toy cases

- point source, compact disk, exponential disk, uniform disk, and shuffled source;
- known symmetry and boundary expectations;
- resolution, timestep, and boundary checks;
- mechanism-off ablations.

### G1 — blind synthetic population

- source profiles generated independently of target velocities;
- freeze the equation and observer;
- test mass scaling and inner-shape diversity;
- no galaxy-specific tuning.

### G2 — SPARC calibration split

- limited training subset;
- frozen global mapping;
- validation subset used for model selection;
- untouched held-out subset for final evaluation.

### G3 — cross-observable population test

Simultaneously score:

- rotation-curve residuals;
- radial acceleration relation;
- baryonic Tully-Fisher slope and scatter;
- inner-shape diversity;
- parameter economy.

### G4 — independent gravitational observables

Only after G3, test whether the same physical bridge is compatible with lensing, vertical dynamics, satellite kinematics, and structure formation.

A velocity-only correspondence cannot establish a gravitational theory.

## 10. Current status matrix

| Item | Source status | Lineum status | Current conclusion |
|---|---|---|---|
| SPARC population data | official public source recovered | not yet ingested in this programme | suitable future empirical test bed |
| Radial acceleration relation | primary paper recovered | no Lineum population prediction | unresolved |
| Baryonic Tully-Fisher relation | primary paper recovered | no Lineum mass-scaling prediction | unresolved |
| Inner rotation-curve diversity | primary paper recovered | no Lineum diversity prediction | unresolved |
| NGC 3198 default drift lane | public galaxy data context; Lineum lane already run | failed preregistered radial shape | unsupported under tested conditions |
| Public TOLOG `tanh` formula | public source recovered | not implemented in Lineum | comparator only; outer saturation partly built in |

## 11. Cheapest next discriminator

Before returning to observed galaxy fitting, the cheapest scientifically useful Q1 step is:

1. complete the Lineum mechanism inventory for `phi`, `mu`, Eq-11 saturation, and collective relaxation;
2. select the smallest observer that is not chosen from observed galaxy results;
3. preregister a synthetic source-family test for mass scaling and surface-density-dependent inner diversity;
4. run mechanism-off and boundary controls;
5. only then decide whether any observer merits SPARC calibration.

This step has greater discriminatory power than fitting another individual galaxy because it can reject mechanisms that generate a flat shape but cannot reproduce population structure.

## 12. Prohibited conclusions at version 0.1.0

This report does not establish that:

- Lineum predicts galaxy rotation curves;
- a Lineum field is gravitational acceleration;
- the radial acceleration relation or baryonic Tully-Fisher relation selects a unique theory;
- the public TOLOG formula fails numerically;
- dark matter is unnecessary;
- one global relation eliminates the need to model inner-curve diversity and observational systematics;
- synthetic scaling automatically transfers to physical units or real galaxies.

## 13. Execution log

1. Retrieved the official SPARC database and primary source papers for the SPARC sample, radial acceleration relation, baryonic Tully-Fisher relation, and inner rotation-curve diversity.
2. Defined four mandatory observational constraints: population coverage, pointwise baryon-response relation, global mass-velocity scaling, and inner-shape diversity.
3. Classified the first public TOLOG galactic formula as a fitted saturation comparator rather than a recovered oscillator-lattice emergence derivation.
4. Defined a staged Q1 validation ladder that begins with blind synthetic populations rather than another one-galaxy fit.
5. No new simulation, production-code change, SPARC fit, or whitepaper promotion was performed in this checkpoint.
