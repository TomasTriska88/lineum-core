# Active Growth and Spatial Scaffold Repair Matrix in Lineum Core

**Status:** active preregistered research report; current whitepaper and mechanism retrieval in progress; no experimental result yet; designated future whitepaper source

**Version:** 0.1.2

**Evidence cutoff:** 2026-07-30

**Scope:** A Core-only successor to the static-baseline transplant pilot. This lane tests whether reconstruction or repair requires a combination of an internally active growth process and an externally or spatially persistent scaffold. It does not use Lina EI, symbolic memory, private data, Lineum Dynamics, OEA, an external language model, or a product-specific identity model.

**Predecessor:** `Static Baseline and Live-State Transplant Matrix in Lineum Core`, which found that a static initializer alone is not an active repair or hereditary mechanism in the tested Core path.

**Current confidence:** High that the prior static initializer does not remain causally active after initialization; no confidence yet that the combined growth-plus-scaffold candidate repairs a damaged pattern, because the exact Core-native mechanisms and frozen intervention have not yet been selected or run.

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

The following current documents are registered for retrieval. Registration means only that their subject could bear on the experiment; every relationship remains `not_yet_compared` until the exact text and implementation evidence are inspected.

| Current whitepaper path | Potential relevance | Current relationship |
|---|---|---|
| `whitepapers/1-core/02-core-equation.md` | implemented field roles, update law, `kappa`, `mu`, coupling and boundaries | `not_yet_compared` |
| `whitepapers/2-cosmology/extensions/03-cosmo-ext-lineum-standard-model.md` | foam, memory, transport, re-ignition and composite mechanisms | `not_yet_compared` |
| `whitepapers/2-cosmology/extensions/05-cosmo-ext-thermodynamic-attractor.md` | active attractor or homeostatic candidate | `not_yet_compared` |
| `whitepapers/2-cosmology/hypotheses/37-cosmo-hyp-quantum-foam-and-mu-emergence.md` | `mu`, persistent medium and emergence candidate | `not_yet_compared` |
| `whitepapers/3-ontology/extensions/01-ontology-ext-ai-reservoir.md` | reservoir and sustained activity analogy or mechanism | `not_yet_compared` |
| `whitepapers/3-ontology/extensions/03-ontology-ext-identity-layer.md` | reconstruction, persistence or identity-bearing claims | `not_yet_compared` |
| `whitepapers/3-ontology/hypotheses/11-ontology-hyp-kinetic-ignition.md` | active ignition or growth candidate | `not_yet_compared` |
| `whitepapers/3-ontology/hypotheses/12-ontology-hyp-order-vs-chaos.md` | guided organization under noise | `not_yet_compared` |
| `whitepapers/3-ontology/hypotheses/16-ontology-hyp-emergent-ai.md` | prior emergence and self-organization claims | `not_yet_compared` |

Other documents remain open for registration if retrieval reveals a material equation, contradiction, or historical variant. The current list is not evidence that all listed documents will require modification.

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

Created this report before repository retrieval or implementation. Preregistered the two-factor `Y × S` matrix, damage stage, scaffold-removal stage, minimum controls, observables, and outcome interpretation. Exact Core-native mappings remain pending and no result has been generated.

### 2026-07-30 — whitepaper handoff designation

The project owner designated this report as the source for later whitepaper updates after completion. Added an explicit claim-promotion classification and required whitepaper impact table so validated implementation observations, bounded negative results, and remaining hypotheses cannot be merged into one canonical claim.

### 2026-07-30 — current whitepaper manifest retrieval

Read the generated current whitepaper map on `develop` and registered nine potentially affected current documents as `not_yet_compared`. Historical extension paths returned by the stale code-search index were not treated as current sources. No whitepaper claim has yet been selected for modification.
