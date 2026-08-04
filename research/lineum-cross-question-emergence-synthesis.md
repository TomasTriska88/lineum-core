# Lineum Cross-Question Emergence Synthesis

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** synthesis of the first galactic-response, attraction, and information-retention anchor maps into one ranked Lineum experiment sequence  
**Central question:** which smallest Lineum-native intervention can constrain all three active questions without inserting the desired astrophysical, attractor, or memory outcome?  
**Current confidence:** high in the ranking logic; low in the candidate mechanism until the preregistered current-engine experiment is executed

## 1. Report lineage

Root programme:

- report: `research/lineum-native-field-stress-tests.md`;
- inherited version: `0.2.1`;
- evidence cutoff: `2026-08-04`.

Universe-emergence map:

- report: `research/lineum-universe-emergence-evidence-map.md`;
- inherited version: `0.2.0`;
- commit: `03451e8c17872b500179aa80c0743e48b4274629`.

Question-specific anchor maps:

- Q1: `research/lineum-galactic-observational-anchor-map.md`, commit `d732e8a1aa9133bb79df16e54acbde5b05f16553`;
- Q2: `research/lineum-saturation-attractor-observational-anchor-map.md`, commit `326cc34adef607b306fdf67b40cb98a4a2fb824e`;
- Q3: `research/lineum-information-retention-observational-anchor-map.md`, commit `eea03caf8b854468669d14850e1acb7ce0f921e9`.

Repository checkpoint before this report:

- repository: `TomasTriska88/lineum-core`;
- branch: `develop`;
- head: `eea03caf8b854468669d14850e1acb7ce0f921e9`.

## 2. Inherited evidence that cannot be reset

### 2.1 Current default radial result

The first deterministic disk lane failed the preregistered outer-locking criteria. Removing the current implemented `phi`-gradient drift changed the outer proxy by only about `0.263` parts per million.

Bounded conclusion:

- the tested default drift mechanism is unsupported as the material source of the weak outer trace;
- the trace is consistent with the remaining diffusion and `psi -> phi` history path under the frozen conditions;
- this does not test `mu`, Eq-11, collective relaxation, alternative observers, or all parameter regimes.

### 2.2 Historical Lineum candidates

Two distinct candidates remain open.

1. **Eq-11 intrinsic saturation** — a historical biharmonic and quintic-saturation family reported to support bounded dissipative localized structures.
2. **Collective relaxation or stress redistribution** — a historical interpretation of a kick-and-receiver experiment as distributed relaxation rather than ballistic transport.

Neither candidate has been independently reproduced in this programme.

### 2.3 Current `mu` implementation

The current engine implements an optional thresholded `abs(psi)^2` accumulator with slow linear decay, positive feedback through the `1 + mu` interaction multiplier, and explicit clipping at `mu_cap`.

Existing regression checks verify only:

- nonzero deposit above a threshold;
- absence of NaN;
- final value below the configured cap in the historical RA-4 check.

They do not verify source-off structural distinguishability, cap-independent saturation, perturbation return, or physical information retention.

### 2.4 Public TOLOG decomposition

The first public-source inventory separated at least four layers:

- a coupled-oscillator and control lattice;
- an explicitly fitted galactic `tanh` saturation formula;
- a redshift-dependent cosmological phenomenology;
- public stability and information-retention language.

No public derivation was recovered that starts from the oscillator lattice and derives all three astrophysical, cosmological, and information layers. The privately supplied attachment remains excluded.

## 3. Real-universe constraints inherited from the anchor maps

### 3.1 Galactic response

A useful mechanism must eventually address simultaneously:

- population coverage across mass, surface density, scale length, gas fraction, and morphology;
- the pointwise radial acceleration relation;
- baryonic mass versus asymptotic-velocity scaling near `M_bar proportional to V_flat^4`;
- diversity of inner rotation-curve shapes;
- parameter economy and held-out prediction;
- independent gravitational observables before a gravity claim.

Primary anchors include the SPARC database and papers with DOI values:

- `10.3847/0004-6256/152/6/157`;
- `10.1103/PhysRevLett.117.201101`;
- `10.3847/2041-8205/816/1/L14`;
- `10.1093/mnras/stv1504`.

### 3.2 Saturation and attraction

A valid attraction claim must distinguish:

- finite numerical output;
- explicit nonlinear saturation;
- metastability;
- dissipative localization;
- local attraction;
- global attraction;
- cosmological attraction;
- regular compact-object geometry.

Required evidence includes cap independence, perturbation return, a declared invariant set, basin mapping, local stability where meaningful, lifetime scaling, and a physical bridge before cosmological interpretation.

Primary anchors include:

- Copeland, Liddle, and Wands, DOI `10.1103/PhysRevD.57.4686`;
- Buttazzo et al., DOI `10.1007/JHEP12(2013)089`;
- Hayward, DOI `10.1103/PhysRevLett.96.031103`;
- DESI DR2 official cosmology publications.

### 3.3 Information retention

A valid memory claim must state:

- the hidden initial label;
- the prior distribution;
- the observer and accessible channels;
- the estimator and null distribution;
- the source-off time horizon;
- whether the record is local, transferred, joint, coarse-grained, or topological;
- whether distinguishability survives numerical-artifact attacks.

Primary anchors include:

- Zurek, DOI `10.1103/RevModPhys.75.715`;
- Braunstein and Pati, DOI `10.1103/PhysRevLett.98.080502`;
- Berut et al., DOI `10.1038/nature10872`;
- Kibble, DOI `10.1088/0305-4470/9/8/029`.

## 4. Shared mechanism candidates

### Candidate C1 — `phi` as distributed relaxation record

Operational idea:

- `phi` integrates and diffuses response to `psi` activity;
- a spatially distributed `phi` state may outlive the visible `psi` source;
- its gradient or stress-like spatial pattern may influence subsequent dynamics.

Potential relevance:

- Q1: a distributed field could create a source-sensitive radial response;
- Q2: slow relaxation can imitate or support return toward a state;
- Q3: `phi` may retain structural labels after visible amplitude relaxes.

Main alternatives:

- ordinary diffusion without identifying memory;
- periodic-image contamination;
- short-lived residual rather than persistent record;
- observer selected after seeing the target.

Current status: `reopened`, not mechanistically supported.

### Candidate C2 — `mu` as slow structural-history channel

Operational idea:

- thresholded activity accumulates into a slowly decaying field;
- the field feeds back into later interaction strength;
- identical current sources can therefore evolve differently after different histories.

Potential relevance:

- Q1: galaxy-like response may depend on assembly history or persistent source imprint;
- Q2: feedback can generate hysteresis, apparent attraction, multiple basins, or runaway cap dependence;
- Q3: the channel may retain recoverable structural labels.

Main alternatives:

- `mu` stores only total deposited energy, not structure;
- positive feedback creates cap-driven persistence;
- slow decay is mistaken for permanent memory;
- grid orientation creates false distinguishability.

Current status: `implemented`, scientific role unresolved.

### Candidate C3 — Eq-11 bounded localized dynamics

Operational idea:

- explicit higher-order regularization and quintic saturation may support bounded dissipative localized structures.

Potential relevance:

- Q1: only if the same family produces a non-circular long-range source-response scaling;
- Q2: strongest current historical candidate for a bounded local invariant set;
- Q3: phase-sensitive dissipative structures may retain or erase labels in nontrivial ways.

Main alternatives:

- explicit saturation explains only local amplitude bounds;
- historical wording outruns artifacts;
- structures are metastable or driven rather than attracting;
- no long-range or information bridge exists.

Current status: `source_recovered` from Lineum history, not reproduced here.

### Candidate C4 — phase synchronization and topology

Operational idea:

- phase relations, winding, defects, or synchronization order may carry information invisible to amplitude-only observers.

Potential relevance:

- Q1: collective phase order could alter a long-range response, but no observer is yet justified;
- Q2: synchronization recovery provides a clear perturbation-return test;
- Q3: phase or topology may retain labels after scalar amplitude relaxation.

Main alternatives:

- arbitrary phase observer;
- numerical branch-cut artifacts;
- lattice anisotropy;
- no physical scale bridge.

Current status: `reopened` by Lineum topology history, public TOLOG oscillator material, and real symmetry-breaking physics.

## 5. Cross-question discrimination matrix

| Proposed experiment | Q1 power | Q2 power | Q3 power | New equation required | Cost | Main risk |
|---|---:|---:|---:|---:|---:|---|
| Repeat another one-galaxy radial fit | low | none | none | no | low | target-shape chasing and per-galaxy tuning |
| Broad blind parameter sweep of current drift | low after Lane B | low | low | no | medium/high | blind tuning after a mechanism-off null result |
| Reproduce Eq-11 localized structures | low initially | high | medium | historical family recovery | medium | local saturation may not address long range |
| Current-engine equal-energy memory test | medium indirect | medium | high | no | low | classifier or grid artifacts |
| Radial assembly-history test with `mu` ablation | high mechanistic | medium/high | high | no | low/medium | history dependence may not imply observed gravity |
| Add a new scalar potential immediately | low | medium | high | yes | medium | unnecessary new mechanism before testing current fields |
| SPARC population fit now | high empirical but low causal | low | none | observer bridge required | high | premature mapping and leakage |

## 6. Ranked experiment sequence

### Rank 1 — current-engine label-retention sanity test

Purpose:

- validate non-circular observers and null controls using two equal-energy histories;
- establish whether `phi` or `mu` contains recoverable structural information after visible `psi` amplitude relaxes;
- quantify cap, orientation, and source-off dependence.

Why first:

- no new equation is introduced;
- the current implementation is directly tested;
- the same result constrains Q2 hysteresis and Q1 history dependence;
- failure would cheaply eliminate `mu` as a rich structural-memory mechanism under the tested regime.

This rank does not claim that the non-radial stamp pair is a galaxy model. It is a metric and mechanism sanity gate.

### Rank 2 — radial assembly-history discriminator

Purpose:

Compare two histories that end with the same declared radial source profile:

- history `A`: source assembled from inside outward;
- history `B`: source assembled from outside inward or deposited simultaneously under an equal integrated-energy schedule.

After the common final source is reached:

- freeze or remove active driving according to the preregistered protocol;
- compare `phi`, `mu`, the candidate radial response, and return dynamics;
- ablate `mu` and its feedback;
- test whether history dependence converges away or persists.

Cross-question meaning:

- Q1: determines whether the current fields can create assembly-history-dependent radial response;
- Q2: distinguishes convergence to one state from hysteresis or multiple basins;
- Q3: locates the retained history channel.

A positive result would not establish galactic gravity. It would identify one Lineum-native mechanism worth testing on blind synthetic galaxy families.

### Rank 3 — Eq-11 reproduction and attractor classification

Purpose:

- recover the exact historical equation and receipts;
- reproduce bounded localized structures;
- audit cap independence;
- perturb and map a small basin;
- classify explicit saturation, metastability, limit cycle, dissipative attraction, or unresolved behaviour.

This remains essential for Q2 and may later provide a stronger common dynamics than current `mu`.

### Rank 4 — blind synthetic galaxy family

Only mechanisms surviving the earlier gates may be tested on analytic disk families for:

- mass scaling of outer response;
- surface-density-dependent inner diversity;
- observer stability;
- no per-target free amplitude;
- boundary and resolution robustness.

### Rank 5 — population data and physical bridge

Only after synthetic success:

- preregister SPARC training, validation, and held-out splits;
- score rotation curves, radial acceleration, baryonic Tully-Fisher scaling, inner diversity, and parameter economy jointly;
- defer lensing and cosmology until a consistent dimensional bridge exists.

## 7. Selected next consequential lane

The selected next lane is **Rank 1: current-engine label-retention sanity test**.

Selection rule:

- maximize discrimination across all three questions;
- introduce no new equation before current fields are identified;
- avoid target data and astrophysical fitting;
- preserve reversibility and low execution cost;
- fail cheaply before radial or cosmological interpretation.

This is a mechanism-identification lane, not an empirical universe test.

## 8. Mandatory child-report gate before execution

A new standalone child report must preregister:

- exact current engine blob and extracted or imported execution path;
- grid sizes, timesteps, update counts, seeds, and boundaries;
- equal-energy initial arrays and analytic equality checks;
- imprint and source-off operations;
- observer channels and independent metric paths;
- training, validation, and held-out samples for any classifier;
- chance and shuffled-label nulls;
- orientation and translation controls;
- `mu` off, accumulation off, feedback off, cap-raised, and reaction-off interventions;
- cap-trigger and fail-safe telemetry;
- success, failure, and inconclusive thresholds;
- outcome interpretation matrix;
- complete executable code and machine-readable outputs after execution.

No simulator run is allowed before this child report is committed.

## 9. What a positive Rank-1 result would mean

A robust positive result would support only this statement:

> Under the declared finite-grid Lineum conditions, at least one current field channel retains enough structure after source relaxation to distinguish two equal-energy histories above the preregistered null level.

It would not establish:

- permanent memory;
- fundamental information conservation;
- quantum unitarity;
- a galactic force law;
- a cosmological attractor;
- black-hole information recovery;
- a physical `mu` field in nature.

## 10. What a negative Rank-1 result would mean

A robust negative result would support only this statement:

> Under the declared current-engine regime and observer set, the tested `phi` and `mu` channels do not retain recoverable labels beyond the chosen source-off horizon.

It would constrain:

- `mu` as a rich structural-memory explanation for Q3;
- history-dependent radial response through the tested current channel;
- hysteretic attraction through the tested current feedback.

It would not falsify:

- all parameter regimes;
- phase or topology observers not included;
- Eq-11;
- a future degenerate-minimum adapter;
- collective relaxation under a different equation family.

A verified decision-relevant negative result will reopen the project-owner intuition gate before a replacement mechanism is selected.

## 11. Root-programme impact matrix

| Root item | Synthesis impact |
|---|---|
| Default radial drift lane | `unaffected`; remains unsupported under tested conditions |
| `phi` distributed history | `reopens`; tested through label retention and reaction ablation |
| `mu` memory channel | `reopens`; promoted from implemented deposit to the first scientific discriminator |
| Eq-11 saturation | `not_yet_compared`; retained at Rank 3, not discarded |
| Collective relaxation | `reopens`; observer and source-off results may constrain it |
| Public TOLOG galactic `tanh` formula | `unaffected`; remains a comparator, not a mechanism to insert |
| Public TOLOG oscillator recovery | `constrains`; motivates perturbation and synchronization metrics |
| Q1 real-universe anchors | `depends_on`; no empirical test before synthetic mechanism gates |
| Q2 real-universe anchors | `depends_on`; no cosmological or compact-object bridge before attraction classification |
| Q3 real-universe anchors | `supports`; observer-relative protocol is now selected |

## 12. ClickUp status

The linked operational task remains `869edcdkk` in workspace `90121717552`.

A prior connector call returned `RATE_LIMIT_EXCEEDED` with a reported wait of `531` minutes. No recovery polling or additional ClickUp call was performed during this synthesis checkpoint.

`ClickUp mode = unsynchronized`.

Git remains complete for the scientific decision.

## 13. Prohibited conclusions at version 0.1.0

This synthesis does not establish that:

- the current `mu` channel retains structural information;
- assembly history explains galaxy rotation curves;
- history dependence is gravity;
- Lineum has an attractor;
- Eq-11 is less important than the current engine;
- public TOLOG mechanisms are valid or invalid;
- one future positive result will connect Lineum to the real universe;
- the selected ranking is permanent after new evidence.

## 14. Execution log

1. Re-read the root programme and all three question-specific anchor maps.
2. Preserved the Lane A/B negative result, historical Eq-11 and collective-relaxation candidates, and the incomplete current `mu` evidence.
3. Identified `phi` distributed relaxation, `mu` structural history, Eq-11 saturation, and phase/topology as the four shared candidate classes.
4. Ranked candidate experiments by cross-question discrimination, mechanism novelty, cost, circularity risk, and readiness.
5. Selected a current-engine equal-energy label-retention sanity test as Rank 1 and a radial assembly-history discriminator as Rank 2.
6. No simulation, production-code change, parameter sweep, observational fit, or whitepaper promotion was performed.
