# Lineum Saturation and Attractor Observational Anchor Map

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** mathematical and real-universe anchors for distinguishing boundedness, metastability, dissipative localization, and genuine attraction in Lineum  
**Central question:** what kind of stability would Lineum need to exhibit before any connection to cosmological or compact-object attractors is scientifically meaningful?  
**Current confidence:** high in the classification boundary; moderate in the current cosmological interpretation because observational constraints remain model- and dataset-dependent; no physical Lineum attractor is established

## 1. Report lineage

Root programme:

- `research/lineum-native-field-stress-tests.md`;
- root version inherited: `0.2.1`;
- root evidence cutoff: `2026-08-04`.

Universe-emergence predecessor:

- `research/lineum-universe-emergence-evidence-map.md`;
- predecessor version inherited: `0.2.0`;
- predecessor commit: `03451e8c17872b500179aa80c0743e48b4274629`.

Most recent sibling checkpoint:

- `research/lineum-galactic-observational-anchor-map.md`;
- sibling commit: `d732e8a1aa9133bb79df16e54acbde5b05f16553`.

Repository checkpoint before this report:

- repository: `TomasTriska88/lineum-core`;
- branch: `develop`;
- branch head: `d732e8a1aa9133bb79df16e54acbde5b05f16553`.

## 2. Purpose

This report prevents the following concepts from being silently merged:

- finite numerical output;
- explicit amplitude saturation;
- a long-lived transient;
- a metastable state;
- a dissipative localized structure;
- a local attractor;
- a global attractor;
- a cosmological late-time attractor;
- a regular black-hole core.

These are different mathematical and physical statements. Similar visual behaviour does not make them equivalent.

## 3. Operational classification

### 3.1 Numerically bounded trajectory

A trajectory remains finite over the tested interval.

This can occur because of:

- a true nonlinear bound;
- explicit clipping or a cap;
- strong dissipation;
- a short observation window;
- insufficient perturbation strength;
- boundary or resolution effects.

This is the weakest useful stability statement.

### 3.2 Explicit saturation

The equation contains a term whose asymptotic form limits amplitude, for example a quintic damping term or a bounded response function such as `tanh`.

This may be mathematically legitimate, but the bound is inserted in the equation. It is not the same as discovering an unexpected attractor.

### 3.3 Metastability

A state survives for a long but finite time before leaving its apparent basin through perturbation, noise, tunnelling, slow drift, or numerical accumulation.

A long-lived state can look permanent in a short run.

### 3.4 Dissipative localized structure

A spatially localized pattern persists through a balance between drive, loss, nonlinearity, and transport.

It need not conserve charge, energy, or information. It need not be a fixed point. It may be a limit cycle, breathing state, chaotic attractor, or continuously driven structure.

### 3.5 Local attractor

A declared neighbourhood of initial conditions returns toward the same invariant set after admissible perturbations.

Required evidence includes:

- a basin estimate;
- return after perturbation;
- stability of the observer under refinement;
- exclusion of clipping and boundary recurrence;
- a declared invariant set, not only one scalar metric.

### 3.6 Global attractor

All or nearly all admissible states in a declared phase space approach the same invariant set.

This is a substantially stronger claim than local attraction and is not supported by one seed, one configuration, or one scalar time series.

### 3.7 Cosmological attractor

A cosmological attractor is defined in a reduced dynamical system derived from a physical action, matter content, and cosmological symmetry assumptions. It must describe the asymptotic behaviour of physical variables such as density fractions, the Hubble rate, or an equation of state.

An internal lattice attractor is not a cosmological attractor until a physical bridge is derived.

## 4. Primary theoretical and observational anchors

### Source A1 — scalar-field scaling attractors

- title: `Exponential Potentials and Cosmological Scaling Solutions`;
- authors: Edmund J. Copeland, Andrew R. Liddle, David Wands;
- journal: Physical Review D `57`, 4686;
- year: `1998`;
- DOI: `10.1103/PhysRevD.57.4686`;
- arXiv: `gr-qc/9711068`;
- stable URL: `https://arxiv.org/abs/gr-qc/9711068`;
- access date: `2026-08-04`.

The paper performs a phase-plane analysis of a scalar field with an exponential potential plus a barotropic fluid. It identifies conditions under which scaling solutions are late-time attractors.

Scientific consequence for Lineum:

- attraction is established through a derived reduced dynamical system and stability analysis;
- a scalar field sitting near a minimum is not enough;
- the relevant state variables, fixed points, eigenvalues, and basin conditions must be defined;
- Lineum would first need an internal dynamical-systems classification before any cosmological analogy.

### Source A2 — Standard Model vacuum metastability

- title: `Investigating the Near-Criticality of the Higgs Boson`;
- authors: Dario Buttazzo et al.;
- journal: Journal of High Energy Physics `2013`, 89;
- year: `2013`;
- DOI: `10.1007/JHEP12(2013)089`;
- arXiv: `1307.3536`;
- stable URL: `https://arxiv.org/abs/1307.3536`;
- access date: `2026-08-04`.

The paper studies the Standard Model Higgs potential at high scales and places the measured parameters near the boundary associated with vacuum metastability.

Scientific consequence for Lineum:

- a state can be extremely long lived without being the absolute minimum;
- finite-time numerical persistence cannot establish global stability;
- escape channels, noise sensitivity, barrier crossing, and lifetime scaling must be tested;
- a metastable Lineum state may be scientifically interesting but must not be labelled a final universal attractor.

### Source A3 — theoretical nonsingular black-hole construction

- title: `Formation and Evaporation of Nonsingular Black Holes`;
- author: Sean A. Hayward;
- journal: Physical Review Letters `96`, 031103;
- year: `2006`;
- DOI: `10.1103/PhysRevLett.96.031103`;
- arXiv: `gr-qc/0506126`;
- stable URL: `https://arxiv.org/abs/gr-qc/0506126`;
- access date: `2026-08-04`.

The paper presents a regular spacetime construction with finite density and pressure and a small-radius region behaving like a cosmological constant.

Scientific consequence for Lineum:

- a finite de Sitter-like core is a theoretical spacetime construction, not an observed black-hole interior;
- a Lineum field amplitude remaining finite does not establish curvature regularity;
- a compact-object bridge would require a metric, curvature invariants, stress-energy content, horizons, causal structure, and observational predictions;
- public TOLOG language about a stable `Dark Heart` may motivate a comparator, but not a physical identification.

### Source A4 — DESI DR2 official publication inventory

- title: `DESI DR2 Publications`;
- publisher: Dark Energy Spectroscopic Instrument collaboration data site;
- URL: `https://data.desi.lbl.gov/doc/papers/dr2/`;
- access date: `2026-08-04`;
- source class: official collaboration publication index.

The official page identifies the key DR2 cosmology papers based on the first three years of DESI data.

### Source A5 — DESI DR2 BAO and cosmological constraints

- title: `DESI DR2 Results. II. Measurements of Baryon Acoustic Oscillations and Cosmological Constraints`;
- author: DESI Collaboration et al.;
- journal: Physical Review D;
- year: `2025`;
- official publication index: `https://data.desi.lbl.gov/doc/papers/dr2/`;
- publisher page: `https://journals.aps.org/prd/abstract/10.1103/tr6y-kpc6`;
- access date: `2026-08-04`.

The collaboration reports that DR2 BAO measurements from more than `14 million` galaxies and quasars are well described by flat `LambdaCDM`. The BAO-preferred parameters show mild tension with CMB-inferred parameters, and time-evolving dark-energy parameterizations can improve the combined fit.

Scientific consequence for Lineum:

- current expansion data do not directly prove a unique dynamical dark-energy mechanism;
- a fitted `w(z)` is not itself an attractor derivation;
- background expansion can be observationally degenerate between distinct physical models;
- structure growth, CMB, supernovae, and BAO must be tested together before a cosmological mechanism is credible;
- Lineum must not infer a universal endpoint from a single fitted expansion function.

## 5. Public TOLOG relevance

The first public TOLOG inventory recovered three Q2-relevant claims:

- explicit curvature saturation as `r -> 0`;
- scalar-field retention at a potential minimum;
- oscillator synchronization and perturbation recovery.

These must be separated.

### 5.1 Explicit curvature saturation

If saturation is imposed by a bounded function or by a declared finite-core ansatz, the result demonstrates the behaviour of that ansatz. It does not establish that an attractor emerged from unconstrained local dynamics.

### 5.2 Scalar field at a potential minimum

Remaining at a minimum can mean:

- the minimum is stable;
- the field was initialized there and not displaced significantly;
- damping removed perturbations;
- a numerical cap suppressed excursions;
- the measured observer missed phase-space motion.

A minimum-retention claim requires perturbation-return and basin tests.

### 5.3 Oscillator recovery

A coupled oscillator network may recover synchrony because of:

- autonomous local coupling;
- a global controller or pulse;
- explicit damping;
- finite-size averaging;
- order-parameter insensitivity to local disorder.

A controlled recovery experiment is not equivalent to an autonomous cosmological attractor.

## 6. Lineum historical relevance

### 6.1 Eq-11 intrinsic saturation candidate

The current Lineum whitepaper records an Eq-11 family with biharmonic regularization and quintic saturation that reportedly supports bounded dissipative localized structures without algorithmic clipping.

Current classification in this programme:

- historical claim recovered;
- exact implementation and artifacts not yet independently reproduced here;
- likely explicit nonlinear saturation rather than an unexpected global attractor;
- potentially relevant to local dissipative structures;
- not yet connected to cosmology or compact objects.

### 6.2 Collective relaxation candidate

The current whitepaper records a historical interpretation in which a kick-and-receiver response was described as collective relaxation or stress redistribution rather than ballistic transport.

Current classification:

- historical interpretation recovered;
- not yet separated from ordinary diffusion and periodic-boundary effects;
- potentially relevant to basin recovery and distributed response;
- no physical attractor or cosmological mapping established.

### 6.3 Current caps and fail-safes

The current engine contains numerical caps and fail-safe behaviour. Any Q2 experiment must report whether a cap was approached or triggered.

A bounded trajectory is disqualified as evidence of natural saturation when the bound depends materially on a numerical cap.

## 7. Required Q2 tests

### Test class S0 — cap and integration audit

- remove or raise non-physical caps within safe numerical limits;
- record cap-trigger fractions;
- vary timestep and integration method;
- test whether the bound converges under refinement;
- distinguish finite arithmetic from finite dynamics.

### Test class S1 — perturbation return

- define a candidate invariant set;
- perturb amplitude, phase, position, width, and environmental fields independently;
- measure return distance and return time;
- include perturbations large enough to cross a possible basin boundary;
- preserve escape and destruction cases.

### Test class S2 — basin mapping

- sample initial conditions systematically;
- classify final invariant sets without using one scalar threshold alone;
- estimate basin fractions and uncertainty;
- test seed, boundary, and resolution dependence;
- distinguish multiple attractors from one noisy class.

### Test class S3 — local stability

Where a reduced state or fixed point can be defined:

- derive or numerically estimate the Jacobian;
- compute eigenvalues or Lyapunov indicators;
- check whether observed return agrees with local stability predictions;
- test whether the chosen observer hides unstable directions.

### Test class S4 — metastability and lifetime scaling

- extend runs by orders of magnitude where feasible;
- vary noise amplitude;
- record escape-time distributions;
- test whether lifetime grows with resolution or only with cap strength;
- avoid interpreting no escape in one window as permanence.

### Test class S5 — physical bridge

Only after S0-S4:

- declare the physical variables and units;
- derive the relevant energy, stress, or cosmological equations;
- compare with expansion history, structure growth, or compact-object observables;
- test multiple independent observables with the same frozen mapping.

## 8. Cosmological connection requirements

A Lineum cosmological attractor claim requires more than a stable lattice state.

Minimum bridge requirements:

- a declared homogeneous and isotropic limit or an explicit alternative;
- a mapping to scale factor, Hubble parameter, density, and pressure;
- a derived effective equation of state rather than a fitted label;
- consistency with energy-momentum conservation or a declared modified law;
- perturbation dynamics and structure-growth predictions;
- comparison to BAO, supernovae, CMB, and growth data;
- a frozen parameter set across datasets;
- analysis of degeneracy with other models.

The current DESI DR2 situation reinforces this requirement: background measurements can favour an evolving `w(z)` in combinations while still leaving the physical mechanism unresolved.

## 9. Compact-object connection requirements

A Lineum `Dark-Heart-like` claim would require:

- a metric or other operational geometry;
- finite curvature invariants, not only finite field amplitude;
- horizon and trapped-surface definitions;
- causal stability and well-posed evolution;
- stress-energy or modified-gravity consistency;
- compact-object observables such as lensing, orbital motion, ringdown, or shadow structure;
- separation from known regular-black-hole ansatz models.

Until then, `Dark Heart` can only be used as an external public metaphor or comparator, not as a Lineum physical object.

## 10. Current status matrix

| Candidate | Boundedness | Perturbation return | Basin evidence | Physical bridge | Current status |
|---|---:|---:|---:|---:|---|
| Current default Lineum radial lane | yes over tested interval | not tested for an invariant set | no | no | bounded numerical run only |
| Historical Eq-11 localized states | claimed | not yet recovered in this programme | not yet recovered | no | reopened historical candidate |
| Historical collective relaxation | claimed response | not yet discriminated from diffusion | no | no | reopened interpretation |
| Public TOLOG galactic `tanh` term | explicit saturation by formula | not applicable | not applicable | phenomenological velocity fit only | comparator |
| Public TOLOG oscillator recovery | publicly described | public claim of recovery | complete basin not recovered | no cosmological bridge | source recovered |
| Public TOLOG finite core | explicit finite-core claim | incomplete public operational test | no recovered basin | no recovered metric derivation | source recovered only |
| Scalar-field cosmological scaling solutions | analytic attractors in declared model | mathematically analysed | model-specific | physical cosmology model | external theoretical anchor |
| Higgs vacuum | long-lived metastability | quantum escape framework | model-specific | Standard Model field theory | external metastability anchor |

## 11. Cheapest next discriminator

The cheapest useful Q2 experiment is not a cosmology fit.

It is a frozen reproduction and classification of the historical Eq-11 bounded structure family:

1. recover the exact equation, parameters, integrator, and artifacts;
2. verify cap independence;
3. perturb the localized state in several independent directions;
4. test return, escape, and destruction;
5. sample a small declared basin;
6. classify the result as explicit saturation, metastability, limit cycle, dissipative attractor, or unresolved;
7. only then ask whether any physical bridge is worth constructing.

This experiment has direct power over the current ambiguity and does not require inventing a cosmological mapping prematurely.

## 12. Prohibited conclusions at version 0.1.0

This report does not establish that:

- Lineum has a cosmological attractor;
- Lineum contains a regular black hole;
- a finite field value implies finite spacetime curvature;
- a stable scalar minimum preserves information;
- historical Eq-11 structures are reproduced or globally attracting;
- DESI has discovered evolving dark energy conclusively;
- a fitted equation of state identifies the underlying physical mechanism;
- public TOLOG saturation claims are incorrect;
- any internal stability phenomenon is equivalent to real-universe stability.

## 13. Execution log

1. Separated numerical boundedness, explicit saturation, metastability, dissipative localization, local attraction, global attraction, cosmological attraction, and regular compact cores.
2. Retrieved primary anchors for scalar-field attractors, Higgs-vacuum metastability, theoretical nonsingular black holes, and current DESI DR2 cosmological constraints.
3. Bounded the public TOLOG Q2 claims to source-recovered comparators until their operational equations, metrics, and independent reproductions are recovered.
4. Defined Lineum test classes S0-S5 and the minimum cosmological and compact-object bridge requirements.
5. Selected reproduction and classification of historical Eq-11 localized states as the cheapest future Q2 discriminator.
6. No new simulation, production-code change, cosmology fit, or whitepaper promotion was performed in this checkpoint.
