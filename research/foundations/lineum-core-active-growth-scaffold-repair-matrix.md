# Active Growth and Spatial Scaffold Repair Matrix in Lineum Core

**Status:** active preregistered research report; first mechanism and whitepaper retrieval complete; no new experiment run yet; designated future whitepaper source

**Version:** 0.2.0

**Evidence cutoff:** 2026-07-30

**Scope:** A Core-only successor to the static-baseline transplant pilot. This lane tests whether reconstruction or repair requires a combination of an internally active growth process and an externally or spatially persistent scaffold. It does not use Lina EI, symbolic memory, private data, Lineum Dynamics, OEA, an external language model, or a product-specific identity model.

**Predecessor:** `Static Baseline and Live-State Transplant Matrix in Lineum Core`, which found that a static initializer alone is not an active repair or hereditary mechanism in the tested Core path.

**Current confidence:** High that the prior static initializer does not remain causally active after initialization; high that the active public solver contains a static `kappa` map and `psi`–`phi`–`mu` feedback but no explicit target-pattern repair controller; medium that several historical and extension mechanisms are scientifically relevant candidates; no confidence yet that any growth-plus-scaffold combination repairs a damaged pattern under a frozen factorial test.

## Intended downstream use and whitepaper handoff

The project owner designated this report as the evidence source for updating the relevant Lineum whitepapers after this research lane is complete.

Completion of the report does not automatically make every idea canonical. The final handoff must classify every material statement as one of:

- `eligible_for_canonical_wording`: independently supported within a clearly stated domain and ready to update or constrain a whitepaper claim;
- `implementation_fact_only`: verified behavior of the current software that must not be presented as a fact about nature;
- `bounded_negative_result`: evidence that rejects or constrains an exact mechanism under declared conditions without claiming universal impossibility;
- `hypothesis_only`: an owner or agent candidate that remains speculative or insufficiently tested;
- `unresolved`: contradictory, underpowered, environment-limited, or awaiting a discriminator.

As repository retrieval identifies affected documents, this report will maintain a whitepaper impact table containing the exact whitepaper path and section, current claim, evidence relationship, proposed scope-safe change, and any reason the text must not yet be changed. Whitepaper edits must be derived from this completed report rather than from chat memory, scripts, or visual impressions.

## Initial whitepaper impact registry

The current generated whitepaper map was read from `lab/src/lib/data/whitepaper_map.json` on `develop`, blob SHA `f6dad7c79b1563f796dac36fc50a140fb2a08096`. It supersedes historical paths encountered in older search indexes.

| Current whitepaper path | Potential relevance | Current relationship |
|---|---|---|
| `whitepapers/1-core/02-core-equation.md` | implemented field roles, update law, `kappa`, `mu`, coupling and boundaries | `implementation_fact_and_variant_provenance_retrieved` |
| `whitepapers/2-cosmology/extensions/03-cosmo-ext-lineum-standard-model.md` | foam, memory, transport, re-ignition and composite mechanisms | `bounded_positive_and_negative_evidence_retrieved` |
| `whitepapers/2-cosmology/extensions/05-cosmo-ext-thermodynamic-attractor.md` | active attractor or homeostatic candidate | `candidate_mechanism_and_limitations_retrieved` |
| `whitepapers/2-cosmology/hypotheses/37-cosmo-hyp-quantum-foam-and-mu-emergence.md` | `mu`, persistent medium and emergence candidate | `not_yet_compared` |
| `whitepapers/3-ontology/extensions/01-ontology-ext-ai-reservoir.md` | reservoir and sustained activity analogy or mechanism | `not_yet_compared` |
| `whitepapers/3-ontology/extensions/03-ontology-ext-identity-layer.md` | reconstruction, persistence or identity-bearing claims | `not_yet_compared` |
| `whitepapers/3-ontology/hypotheses/11-ontology-hyp-kinetic-ignition.md` | active ignition or growth candidate | `not_yet_compared` |
| `whitepapers/3-ontology/hypotheses/12-ontology-hyp-order-vs-chaos.md` | guided organization under noise | `not_yet_compared` |
| `whitepapers/3-ontology/hypotheses/16-ontology-hyp-emergent-ai.md` | prior emergence and self-organization claims | `not_yet_compared` |

Other documents remain open for registration if retrieval reveals a material equation, contradiction, or historical variant. The current list is not evidence that all listed documents will require modification.

## Retrieved implementation facts and mechanism families

### Active public Core implementation

The active source inspected is `lineum_core/math.py`, blob SHA `bb877021810691223a0eb960a45493a2e351112a`.

Observed implementation facts:

- `kappa` is supplied as a spatial array and returned unchanged by the NumPy step. It is not dynamically reconstructed by the solver.
- `kappa` multiplies stochastic linon generation, noise injection, `phi` interaction, `phi`-gradient drift, `psi` diffusion, `phi` accumulation and diffusion, and `mu` growth. It is therefore a broad spatial permeability or activity map, not merely a visual mask.
- `mu` is always read through the multiplier `1 + mu`, even when `use_mu=False`; the flag controls whether `mu` is updated, not whether an already supplied nonzero `mu` affects drift and interaction.
- With `use_mu=True`, `mu` accumulates above a dynamic `psi`-energy threshold and decays slowly. This is path reinforcement, not an explicit comparison against a desired target shape.
- `phi` receives energy through mode coupling or a fallback reaction and then diffuses. The active solver contains no stored target pattern, missing-region detector, or term that directly restores erased values.
- The default NumPy path includes literal linear dissipation, stochastic generation and noise, diffusion, and optional `mu` reinforcement. A visually returning pattern could therefore result from diffusion, continued forcing, confinement, or amplification rather than genuine repair; the factorial controls must distinguish these.

These are `implementation_fact_only` until a report compares them with physical evidence. They do not establish biological growth, heredity, or self-repair.

### Historical and extension mechanism families

#### Family A — active public feedback plus static `kappa`

- Candidate yeast `Y_A`: active `psi`–`phi` mode coupling, `phi`-gradient drift, stochastic generation, and optional `mu` reinforcement in the current solver.
- Candidate scaffold `S_A`: a structured static `kappa` map.
- Status: implemented and cheapest to test, but no prior evidence retrieved yet that it restores a specific damaged organization.

#### Family B — Eq-11 growth/leakage plus geometric closure

The equation-history whitepaper records `tanh`-bounded growth and leakage variants, including extensive persistence and failure audits. It also records that a weak smooth external Gaussian `kappa` well with approximately `0.05` boundary strength failed to contain the active scalar exhaust, and that explicit closure mechanisms were considered mandatory under that tested slice.

- Candidate yeast `Y_B`: Eq-11 active growth balanced by leakage.
- Candidate scaffold `S_B`: strong `kappa` walls, geometric containment, or another explicit closure.
- Status: historical/experimental equation family, not the active public NumPy law. The weak-scaffold instance is `unsupported_under_tested_conditions`; stronger and qualitatively different scaffolds remain open.

#### Family C — closed-energy epsilon attractor

The thermodynamic-attractor extension defines an active environmental `epsilon` cycle that supplies growth and returns dissipative losses to the environment. Reported tests show bounded response to amplitude shocks and convergence across randomized starts, but also long-horizon evaporation. The reported node-amputation result says the remaining subset stayed stable; it does not demonstrate regrowth of the removed node.

- Candidate yeast `Y_C`: the active closed-energy `epsilon` metabolic cycle.
- Candidate scaffold `S_C`: geometric or environmental organization coupled to the cycle.
- Status: extension mechanism with reported perturbation robustness, not current public Core behavior and not yet independently reproduced in this lane.

#### Family D — Relic Foam as stateful environment

The Lineum Standard Model extension reports that Relic Foam can absorb a raw `phi` heat shock and partially reorganize, modify trajectories, and stabilize a passing high-speed structure. It also reports that structured impacts cause transient secondary emission rather than a stable re-created particle, repeated impacts cause fatigue, and permanent clean trapping was not observed.

- Candidate active factor `Y_D`: a traveling structured excitation or another active impact.
- Candidate scaffold `S_D`: mature Relic Foam and its ambient `phi` environment.
- Status: bounded evidence for environmental shaping and co-stabilization; bounded negative evidence against permanent true re-ignition and immortal reusable repair under the recorded parameters.

## Variant ledger after retrieval step 1

| Variant | Yeast factor | Scaffold factor | Implementation status | Evidence status | Cheapest next discriminator |
|---|---|---|---|---|---|
| `A_active_mu_kappa` | current `psi`–`phi` feedback with `mu` update enabled | structured static `kappa` | active public implementation | `untested_for_damage_repair` | four-lane matched damage matrix in research harness |
| `A_active_no_mu_kappa` | current feedback with `mu` frozen/zero | structured static `kappa` | active public implementation | required ablation | compare with `A_active_mu_kappa` |
| `B_eq11_growth_kappa` | Eq-11 growth/leakage | explicit `kappa` confinement | historical/experimental | weak Gaussian well failed; broader family open | reproduce weak-well negative control before stronger closure |
| `C_epsilon_scaffold` | closed-energy `epsilon` cycle | geometric/environmental scaffold | extension, not active library | shock recovery reported; missing-part regrowth unproven | node-erasure recovery versus no-`epsilon` and no-scaffold controls |
| `D_active_foam` | structured active impact | Relic Foam/ambient `phi` | extension experiment | transient emission and co-stabilization supported; true re-ignition and infinite reuse rejected | matched erasure repair rather than impact-only assay |
| `null_diffusion_only` | no active reinforcement beyond passive diffusion | no structured scaffold | control | `queued` | matched damage horizon |
| `null_scaffold_mass_shuffled` | matched active factor | shuffled or rotated scaffold with equal total magnitude | control | `queued` | tests spatial information versus total drive |

No variant is yet selected as the final mechanism. The active public `A` family is the smallest first implementation candidate because it can be tested without changing the library, but selection remains pending completion of the registered ontology and `mu` retrieval.

## 1. Owner hypothesis recorded before formalization

At the verified negative-result gate, the project owner proposed that the mechanism may be a combination rather than a single carrier:

> Yeast makes dough from flour and water, while a mould gives it shape.

This is retained as an owner-generated candidate hypothesis, not as experimental evidence.

The useful causal distinction in the analogy is:

- flour and water: available carrier material or initially weak fields;
- yeast: an internally active process that amplifies, transforms, grows, or repairs organization;
- mould: a spatial constraint, boundary, permeability map, or environment that guides where growth is allowed;
- heat and feeding conditions: energy, forcing, resources, or environmental support;
- developed dough: the live organized state;
- cutting or removing part of the dough: the perturbation used to test repair.

The owner hypothesis is specifically combinatorial: neither the active process nor the scaffold is assumed sufficient alone.

## 2. Agent formalization

The smallest testable candidate is a two-factor mechanism:

- `Y` — active growth or repair dynamics (the “yeast” factor);
- `S` — persistent spatial scaffold or shaping constraint (the “mould” factor).

The combined hypothesis is:

> A Lineum pattern may require both an active state-transforming process and a spatial scaffold; the active process supplies growth or restoration, while the scaffold constrains that process into a reproducible organization.

This formalization does not yet assign `Y` or `S` to a specific field. Candidate mappings must first be retrieved from existing Core code, research history, and whitepapers. The mapping must not be chosen merely because a field name fits the analogy.

## 3. Questions

1. Does an active Core-native process increase recovery after standardized damage?
2. Does a spatial Core-native scaffold increase recovery after the same damage?
3. Is their combination more effective than either factor alone?
4. Does any recovered organization persist after the scaffold is removed?
5. Is the result exact replay, broad morphological repair, temporary confinement, or uncontrolled amplification?

## 4. Required repository retrieval before mechanism selection

Before implementing the matrix, retrieve every recorded Core candidate relevant to:

- active attractors, homeostasis, source terms, mode coupling, hysteresis, memory, self-maintenance, growth, regeneration, or re-ignition;
- `psi`, `phi`, `kappa`, `mu`, `delta`, boundaries, gradients, reservoirs, foam, environmental transport, and spatial permeability;
- prior perturbation, source-off, field-freeze, scaffold-removal, damage-recovery, and ablation experiments;
- historical, experimental, deprecated, unsupported, and canonical equation variants.

For each retrieved candidate, record its exact implementation or equation status, causal role, assumptions, known failures, and cheapest discriminator. Retrieval is provenance, not validation.

## 5. Preregistered factorial structure

The minimum matrix contains four lanes built from the same weak or standardized starting material:

| Lane | Active growth `Y` | Scaffold `S` | Purpose |
|---|---:|---:|---|
| `YS00` | absent | absent | null: material without growth or shape guidance |
| `Y1S0` | present | absent | active process alone |
| `Y0S1` | absent | present | scaffold alone |
| `Y1S1` | present | present | combined owner hypothesis |

The experiment must not silently give one lane a more developed live state than another. Any seed, initial perturbation, resource, boundary, or challenge must be matched unless it is the declared factor under test.

## 6. Planned stages

### Stage A — formation

Start all four lanes from matched weak material and allow a frozen formation horizon. Measure whether an organized pattern forms and whether the combined lane exceeds both single-factor lanes.

### Stage B — damage and repair

Apply the same spatial erasure or attenuation mask to the formed pattern in every lane. Continue for a frozen repair horizon under matched stochastic history. Compare the state immediately before damage, immediately after damage, and after repair.

### Stage C — scaffold removal

For lanes containing `S`, replace or neutralize the scaffold after the repair horizon while preserving the current live fields. Continue under a matched challenge. This distinguishes:

- autonomous persistence: organization remains without the scaffold;
- scaffold dependence: organization degrades when the scaffold is removed;
- mechanical confinement: apparent repair existed only while the mould constrained the state;
- delayed collapse or adaptation: an intermediate dependence requiring a longer horizon.

## 7. Minimum controls

The retained protocol must include:

- no-damage controls for every lane;
- identical-noise comparisons to isolate deterministic causal differences;
- independent-noise repeats to distinguish exact replay from robust organization;
- scaffold shuffling or spatial rotation when meaningful, to test whether location-specific structure matters;
- active-process freeze or zero-strength ablation;
- matched energy, amplitude, or source accounting where the candidate mechanism changes available drive;
- at least one null morphology with the same total scaffold magnitude but no organized spatial pattern.

## 8. Observables

No single image or amplitude correlation is sufficient. At minimum record:

- exact array equality and cryptographic hashes for replay controls;
- normalized RMS error relative to the undamaged lane-specific reference;
- amplitude-shape correlation;
- recovered fraction inside the damaged region;
- unintended change outside the damaged region;
- localization or concentration statistics;
- total `psi`, `phi`, `mu`, and other relevant field ledgers;
- survival after scaffold removal;
- growth without bound, clipping, numerical saturation, or collapse;
- dependence on seed and horizon.

Additional topology or functional metrics may be added only after their causal meaning and failure cases are declared.

## 9. Frozen decision logic before results

The combined mechanism receives provisional support only if `Y1S1` repairs the damaged organization materially better than `Y1S0`, `Y0S1`, and `YS00` under matched controls, without merely injecting more unconstrained amplitude or copying the erased values directly.

- If only `Y1S0` succeeds, the scaffold is unnecessary under the tested conditions.
- If only `Y0S1` appears to succeed while the active state does not regenerate, the result is confinement or passive shaping, not active repair.
- If `Y1S1` succeeds only while the scaffold remains, the mechanism is distributed between system and environment.
- If `Y1S1` persists after scaffold removal, the scaffold may act developmentally rather than continuously; further damage after removal is then required to test retained autonomous repair.
- If no lane succeeds, this implementation of the owner hypothesis is unsupported under the frozen conditions; the broader combination idea remains open unless the test has power over all plausible active-process and scaffold mappings.

Exact byte reconstruction is not required for morphological repair, but any relaxed success threshold must be preregistered before results are inspected.

## 10. Current unresolved choices

The following are intentionally unresolved pending repository retrieval:

- which existing Core variable or equation variant best represents `Y`;
- which existing Core field, boundary, or permeability structure best represents `S`;
- whether the standard material should be blank, weakly seeded, or donor-derived;
- the damage geometry and severity;
- formation, repair, and scaffold-removal horizons;
- success thresholds and topology metrics;
- whether the first run should use the active Core adapter, a frozen standalone model, or both.

No code change or numerical result is authorized until these choices are recorded here with their provenance and falsification rationale.

## 11. Continuous-report ledger

### 2026-07-30 — owner failure-gate response

Recorded the owner proposal that active transformation and spatial shaping may be jointly necessary, using yeast, flour and water, and a mould as the causal analogy.

### 2026-07-30 — protocol creation

Created this report before repository retrieval or implementation. Preregistered the two-factor `Y × S` matrix, damage stage, scaffold-removal stage, minimum controls, observables, and outcome interpretation. Exact Core-native mappings remained pending and no result was generated.

### 2026-07-30 — whitepaper handoff designation

The project owner designated this report as the source for later whitepaper updates after completion. Added an explicit claim-promotion classification and required whitepaper impact table so validated implementation observations, bounded negative results, and remaining hypotheses cannot be merged into one canonical claim.

### 2026-07-30 — current whitepaper manifest retrieval

Read the generated current whitepaper map on `develop` and registered nine potentially affected current documents. Historical extension paths returned by the stale code-search index were not treated as current sources.

### 2026-07-30 — mechanism retrieval step 1

Inspected the active public Core NumPy law, the canonical equation-history appendix, the thermodynamic-attractor extension, and the Relic Foam sections of the Lineum Standard Model extension. Registered four scientifically distinct growth/scaffold families and their known failures. No mechanism was promoted and no new simulation was run. The active public `mu × kappa` family remains the cheapest first test, pending the remaining registered retrieval.
