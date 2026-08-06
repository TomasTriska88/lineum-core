# Lina EI Capability, Emergence, and Lineum Integration Audit

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-06  
**Target repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Target base commit:** `034f343605c1d0eac05820301fae67887c99a479`  
**Private source repository:** `TomasTriska88/osobni-pamet` (temporary Lina EI repository alias)  
**Private source snapshot:** `f62a2c547675c79a2399a76e2bf82d0d02581298`  
**Current confidence:** high for the static architecture map; medium for capability classification; low for production-runtime, deployment-parity, robustness, and emergence claims

## 1. Plain conclusion

Lina EI is currently best described as a **hybrid persistent agent prototype with field-mediated modulation and partial grid-mediated reflex behaviour**.

It is more than a stateless chat wrapper. The inspected implementation contains a persistent numerical state, sensory injection, field evolution, memory files, scheduled activity, action routing, and an LLM-based semantic and linguistic layer. These components can influence later behaviour across multiple ticks.

It is not yet supported as a fully emergent intelligence. Important meanings, locations, emotional categories, thresholds, action pools, memory routes, and decisions are still substantially assigned by configuration, fixed rules, keyword or pattern matching, and the external language model. The current grid therefore modulates and carries state, but it has not yet been shown to discover its own semantic organisation, goals, concepts, or stable identity through local Lineum dynamics alone.

The inspected Lina EI source also does not currently use the released `lineum_core` package as a direct runtime dependency. Its present numerical substrate is an independent, Lineum-inspired local solver. The accurate current statement is therefore:

> Lina EI uses a persistent local wave-grid prototype inspired by Lineum concepts; it has not yet been demonstrated as running on the current Lineum Core engine contract.

This report establishes the first public-safe baseline. It does not certify consciousness, personhood, biological equivalence, medical capability, autonomous general intelligence, or commercial readiness.

## 2. Scope and central questions

This audit asks:

1. What does the current Lina EI implementation actually compute and orchestrate?
2. Which capabilities are implemented in code, which were reproducibly observed, and which remain design proposals?
3. Which parts are genuinely stateful or locally dynamical, and which are supplied by rules, configuration, prompts, or an LLM?
4. What would need to change before stronger claims of emergence could be tested?
5. How could Lina EI depend on the public Lineum Core contract without moving private persona, memory, product policy, or deployment details into Core?
6. Which public-safe product and investor opportunities are plausible, and which claims are premature?

The report does not disclose private memories, private conversations, exact household or deployment data, credentials, network topology, device identifiers, security-sensitive prompts, or operational details that could facilitate misuse.

## 3. Source intake, rights, and confidentiality record

### 3.1 Material inspected

The audit used an owner-authorised, access-controlled snapshot of the private Lina EI repository, including:

- repository and developer rules;
- public-facing repository description;
- main chat and orchestration entry points;
- the local field simulator;
- the scheduled life-loop runner;
- sensory and thalamic routing code;
- synchronisation tooling;
- dependency manifests and container definition;
- selected tests;
- selected architecture, scaling, business, and implementation-plan documents.

Dynamic personal-memory directories, private diaries, private conversations, personal profiles, exact smart-home configuration, credentials, and deployment secrets were excluded from the evidence used in this public report.

### 3.2 Rights and permitted mode

The private repository had no public licence file at the inspected snapshot. No redistribution right is inferred from repository access. The project owner explicitly authorised inspection for this audit. The permitted mode is therefore limited to:

- factual source audit;
- original high-level architectural description;
- public-safe capability classification;
- original test-plan design;
- no copying of private source code, private prose, prompts, personal data, or operational configuration into public Core.

No private source code is reproduced here. The normalised equations and architecture diagrams below are original audit abstractions.

### 3.3 Reproduction tiers

This report supports two review tiers:

- **Public review:** challenge the definitions, criteria, causal logic, test design, claim boundaries, and commercial-readiness reasoning contained in this standalone document.
- **Authorised source verification:** independently inspect the declared private commit and verify that the normalised implementation statements match the source. This tier requires lawful access to the private snapshot and must preserve the same confidentiality boundary.

## 4. Evidence ladder used in this audit

- `documented`: described in a design or planning document.
- `implemented`: corresponding code exists in the inspected snapshot.
- `test_present`: a relevant automated test exists in the repository.
- `reproduced`: a frozen execution produced a retained result in the current audit.
- `robust_within_tested_domain`: controls and independent checks support the observation.
- `mechanistically_supported`: interventions distinguish the proposed mechanism from alternatives.
- `empirically_connected`: a defined observable has been compared responsibly with external evidence.

At this checkpoint, the strongest general level reached is **implemented/static audit**. Tests were inspected but were not executed in this environment. No production-host runtime, deployment synchronisation, long-horizon behaviour, or device action was independently reproduced.

## 5. Git-to-production-host parity

The project owner expects the Git snapshot to be identical to the code running on the production mini-PC host. The private repository contains an official remote-synchronisation checker and an official deployment workflow. The checker is designed to compare selected local and remote files by hash and classify them as synchronised or diverged while excluding volatile or secret material.

No direct connection to the production host was available in this audit environment. No signed or retained synchronisation receipt was supplied. Therefore:

- **Owner expectation:** Git and production code are 1:1.
- **Audit status:** not independently verified.
- **Required next evidence:** a sanitised synchronisation receipt tied to the private commit and execution time.

A suitable public-safe receipt is:

```json
{
  "schema": "lina-ei-sync-receipt/v1",
  "source_commit": "<private-source-commit>",
  "checked_at_utc": "<ISO-8601 timestamp>",
  "checked_file_count": 0,
  "matching_file_count": 0,
  "diverged_file_count": 0,
  "missing_local_count": 0,
  "missing_remote_count": 0,
  "excluded_secret_or_volatile_count": 0,
  "result": "synced|diverged|unresolved",
  "checker_version_sha256": "<hash>",
  "receipt_sha256": "<hash>"
}
```

The receipt must not contain filenames that reveal personal data, hostnames, addresses, ports, credentials, device identifiers, or secret paths.

## 6. Public-safe normalised architecture

```text
Environment and user inputs
        |
        v
Sensor and message adapters
        |
        v
Gating / routing / safety checks
        |
        +----------------------------+
        |                            |
        v                            v
Persistent local field grid      Semantic cortex
(state, diffusion, waves,        (LLM interpretation,
noise, modulation, thresholds)    language, planning, tools)
        |                            |
        +-------------+--------------+
                      |
                      v
             Memory and state stores
                      |
                      v
             Action / notification layer
                      |
                      v
               External environment
```

This is a hybrid architecture. Neither the field grid nor the LLM alone is the complete current system.

## 7. What the implementation currently contains

| Capability | Static evidence | Current audit status | Important limitation |
|---|---|---|---|
| Persistent numerical internal state | Multiple field arrays and state are loaded, updated, and saved across ticks | implemented | Persistence alone does not establish memory semantics, agency, or consciousness |
| Local spatial field evolution | Diffusion-like, growth, damping, noise, and coupling operations are present | implemented | Numerical validity, stability domain, and equivalence to current Core were not reproduced |
| Sensory injection into a grid | External observations are converted into localised field perturbations | implemented | Sensor meanings and placements are substantially configured in advance |
| Arousal, valence, tension, fatigue, and related readouts | Scalar state and grid-derived modulation paths are present | implemented | These are engineered observables and labels, not demonstrated biological emotions |
| Thalamic-style gating and prioritisation | Routing and salience filters are present | implemented | Biological naming is an analogy unless experimentally validated at the causal level |
| Motor or action pools | Thresholded action-selection structures and external action adapters are present | implemented | Action semantics and thresholds are largely predefined |
| Persistent text and structured memory | File-backed memories, state, logs, and retrieval paths are present | implemented | Much retrieval remains rule-, keyword-, or LLM-mediated rather than emergent from the field |
| Scheduled autonomous loop | Background or periodic orchestration is present | implemented | Continuous reliable production operation was not independently observed |
| LLM-based semantic reasoning | External or local model routes are present | implemented | The LLM remains the principal source of language competence and much semantic interpretation |
| Local/cloud model fallback strategy | Multiple model-provider modes are documented and partially wired | implemented/documented | Cost, latency, privacy, and quality claims require current benchmarks |
| Automated tests | Unit and integration-oriented tests are present | test_present | The test suite was not run in this checkpoint; green tests would still not prove emergence |
| Self-modification or self-healing | Repository rules and plans describe adaptive code maintenance | documented/partly orchestrated | Safe, autonomous, production-grade self-modification was not reproduced |
| Concept-grid learning | Embedding, self-organising, and plasticity ideas are described | documented | Not established as the current semantic substrate |
| Dream or offline consolidation | Consolidation concepts and scheduled-state ideas are described | documented/partial routines | No mechanistic evidence that offline dynamics improve generalisation was reproduced |

## 8. Normalised current field model

The inspected implementation can be abstracted as a bounded discrete-time field system:

\[
X_{t+1} = B\left(X_t + \Delta t\left[F(X_t;\theta) + D(X_t)\nabla^2X_t + S_t + \xi_t\right]\right),
\]

where:

- \(X_t\) is the collection of local fields, including quantities named \(\psi\), \(\phi\), \(\mu\), and \(\kappa\);
- \(F\) represents local growth, decay, coupling, and nonlinear update terms;
- \(D\nabla^2X_t\) represents neighbour-mediated spreading or diffusion;
- \(S_t\) represents externally prepared sensory or message injection;
- \(\xi_t\) represents noise or situated perturbation;
- \(B\) is numerical bounding, clipping, or normalisation;
- \(\theta\) contains fixed or configured parameters.

This abstraction captures a real dynamic substrate, but the semantic interpretation of regions and observables is currently supplied substantially outside the equation. For example, an externally defined input may be assigned a location or phase class before the field evolves. A later scalar readout may then be labelled as an emotion, urgency, or action tendency. The field can transform and propagate the injected state, but this does not by itself show that it discovered the meaning of the input or label.

## 9. What is currently pre-authored rather than emergent

The following elements materially constrain a full-emergence claim:

1. The grid resolution is fixed in the present implementation.
2. Semantic and anatomical regions are substantially assigned to predefined coordinates.
3. Several affective categories and modes are represented by fixed templates or mappings.
4. Sentiment or message class can be supplied externally rather than inferred through local adaptation.
5. Concepts and relationships can be selected through keywords, patterns, configured names, or LLM interpretation.
6. Action pools, labels, locations, thresholds, and safety gates are substantially designed in advance.
7. Memory retrieval is not yet shown to arise from field similarity and learned causal relevance without keyword or LLM mediation.
8. The LLM remains the dominant semantic executive and language generator.
9. No retained ablation demonstrates that the grid is necessary for the claimed long-horizon capabilities rather than merely a modulator.
10. No retained intervention demonstrates that learned local structure, rather than preassigned structure, causes successful behaviour.

The appropriate conclusion is not that emergence is absent everywhere. It is that the current evidence cannot distinguish strongly enough among:

- genuine useful field-mediated state integration;
- engineered dynamical modulation;
- decorative or redundant biological analogy;
- behaviour primarily generated by the LLM and conventional rules.

## 10. Operational criteria for stronger emergence

A stronger claim should require observable behaviour, not a preferred label. The following criteria are proposed.

### E1 — Persistent endogenous state

After input stops, a bounded internal state must persist for a preregistered interval and alter later behaviour. It must survive restart or checkpoint restoration when persistence is part of the claim.

### E2 — Learned semantic relocation

The system must learn where and how to represent novel concepts from experience. A successful test must prevent the evaluator from assigning the final coordinates, labels, or class-specific thresholds in advance.

### E3 — Local plasticity with causal credit

Local couplings must change from consequences or prediction errors. Intervention on the learned couplings must selectively impair the acquired behaviour.

### E4 — Decentralised action selection

At least one meaningful action-selection task must be solved by distributed field state plus generic readout rules, without the LLM choosing the action label directly.

### E5 — Open-ended concept growth

The system must add, merge, split, or reorganise concepts without a fixed closed ontology. Growth must improve a held-out behavioural measure rather than only produce visually interesting clusters.

### E6 — Generalisation

A learned organisation must transfer to held-out inputs, contexts, or sensors without adding task-specific coordinates, keywords, or thresholds.

### E7 — Ablation necessity

Freezing, shuffling, replacing, or removing the field must cause a predicted and selective loss. A generic random-state or scalar-state control must not perform equivalently.

### E8 — Robustness and convergence

The result must remain within declared tolerance across seeds, timesteps, grid sizes, resolutions, boundaries, and small parameter perturbations.

### E9 — Non-circular measurement

Success metrics must be fixed before observing the desired output and must not reuse the labels, coordinates, or thresholds that defined the behaviour.

Meeting these criteria would support bounded claims about emergent organisation or field-mediated cognition. It would still not prove consciousness or biological equivalence.

## 11. Current Lina grid versus Lineum Core

The inspected Lina EI runtime implements its own numerical solver and local field conventions. Its dependency manifest does not declare the current `lineum-core` package, and the audited entry points did not import the public `lineum_core` package.

Therefore the current relationship is conceptual and architectural, not a verified package integration.

The required dependency direction is:

```text
Lina EI private product and persona
        |
        v
Lina cognition adapter
        |
        v
Pinned public Lineum Core contract
```

The reverse direction is forbidden. Public Core must not import private memories, persona logic, devices, customer policy, product prompts, or deployment code.

A minimal adapter should expose only application-neutral operations such as:

- initialise a field state from a declared shape and profile;
- advance the state by a declared timestep;
- inject a generic spatial source;
- return declared field observables;
- serialise and restore state with versioned metadata;
- produce numerical receipts containing parameters, seeds, boundary conditions, and source fingerprints.

Lina-specific meanings must remain in the private adapter or product layer until a meaning-independent mechanism has passed the public-library promotion gate.

## 12. Frozen research programme

### P0 — Deployment parity receipt

Run the official synchronisation checker against the production host and retain a sanitised receipt. Success requires zero unexplained divergence among in-scope code and configuration files. Volatile memories and secrets must remain excluded and separately accounted for.

### P1 — Baseline reproduction

Freeze a generic, privacy-safe configuration and run the current grid from a known state. Retain:

- dependency versions;
- random seed or situated-entropy receipt;
- initial-state hash;
- parameters and boundary conditions;
- per-tick machine-readable observables;
- final-state hash;
- runtime and environment metadata.

Independent check: reproduce the same declared observables from a second implementation or a known-answer toy case.

### P2 — Source-off persistence

Inject a bounded stimulus, remove it, and measure persistence and later behavioural effect. Controls:

- no-field scalar state;
- shuffled spatial state;
- diffusion disabled;
- plasticity disabled;
- source never applied.

### P3 — Learned semantic relocation

Train with two or more novel anonymous categories whose final spatial organisation is not prescribed. Swap labels and initial positions. Evaluate held-out classification or action behaviour. Reject the claim if success follows labels, fixed coordinates, or task-specific thresholds.

### P4 — Causal ablation matrix

Ablate one component at a time and factorially where practical:

- LLM semantic planning;
- field dynamics;
- persistent memory;
- local plasticity;
- noise;
- sensory localisation;
- thresholded action pools.

Classify each capability as field-dependent, LLM-dependent, memory-dependent, jointly dependent, or observationally equivalent under the test.

### P5 — Scaling and convergence

Repeat the retained task across multiple grid sizes, timesteps, seeds, boundary modes, and precision levels. Record computational cost and behavioural stability. Visual similarity is not a success criterion.

### P6 — Core-adapter equivalence

Implement a research-only adapter to a pinned Core contract outside the public package. Compare the legacy Lina solver and the Core-backed solver at observable level. Classify differences as matching, expected model evolution, possible regression, or unresolved divergence.

### P7 — Embodiment sandbox

Connect the tested cognition path only to a simulated or reversible low-consequence environment. Require explicit permissions, action budgets, audit logs, rollback, and a deterministic safe fallback. Physical deployment is not evidence of intelligence and must not precede causal validation.

## 13. Public-safe investor and monetisation assessment

### 13.1 Potential value propositions

The current architecture points to several plausible product categories:

1. **Privacy-first local personal agent:** persistent state and local integration may offer continuity and data control beyond stateless cloud chat.
2. **Embodied home or workspace agent:** integration of sensors, state, and actions could support context-aware orchestration when safety boundaries are strong.
3. **Persistent-agent runtime:** developers may value a framework combining model routing, memory, scheduled activity, local state, and auditable tools.
4. **Research sandbox for hybrid field/LLM systems:** the project could support controlled experiments on persistent dynamical substrates coupled to language models.
5. **Private or enterprise deployment:** local operation, explicit state ownership, and configurable model backends may be useful where data residency matters.

### 13.2 Potential differentiator

The strongest defensible differentiator would not be a claim that Lina is conscious. It would be a demonstrated combination of:

- persistent local internal state;
- measurable field-mediated behaviour;
- useful embodiment;
- inspectable causal traces;
- privacy-preserving deployment;
- graceful operation across local and cloud model tiers.

This differentiator remains a hypothesis until benchmarks show that the field layer improves retention, adaptation, robustness, energy use, latency, safety, or user outcomes over simpler alternatives.

### 13.3 Current commercial blockers

- production parity is not independently evidenced;
- the grid is not yet integrated with a pinned public Core contract;
- many semantics remain hand-authored;
- emergence metrics and causal ablations are absent;
- model cost, latency, reliability, and privacy trade-offs are not currently benchmarked in this audit;
- personal-agent products carry substantial privacy, security, dependency, and emotional-reliance risk;
- the present codebase mixes research concepts, product behaviour, biological analogy, and operational tooling more tightly than an investable product should;
- a narrow first customer problem and measurable product wedge are not yet validated.

### 13.4 Readiness classification

| Dimension | Current status |
|---|---|
| Technical prototype | present |
| Static architecture audit | present in this report |
| Reproducible scientific baseline | not yet retained |
| Mechanistic emergence evidence | not established |
| Public Core integration | not established |
| Privacy-safe deployable product | not audited end to end |
| Product-market fit | not established |
| Defensible unit economics | not established |
| Investor-grade technical diligence package | early; this report is the first baseline |

Detailed pricing, revenue projections, market sizing, proprietary go-to-market strategy, investor targeting, and private intellectual-property decisions belong in the private company repository rather than public Core.

## 14. Prohibited near-term claims and product uses

The present evidence does not support marketing Lina EI as:

- conscious or sentient;
- biologically equivalent to a nervous system;
- a therapist, psychiatrist, medical device, or diagnostic system;
- a safety-critical controller;
- an autonomous authority for financial, legal, medical, employment, or similarly consequential decisions;
- an artificial general intelligence;
- a validated scientific proof of Lineum cognition.

Human-readable biological names may be retained as interface metaphors, but every public technical claim must state the exact operational observable behind the label.

## 15. Privacy and security publication boundary

This report intentionally excludes:

- names, birthdays, relationships, addresses, and personal histories;
- private conversations, diaries, profiles, and memories;
- exact sensors, devices, entity identifiers, cameras, or household layout;
- IP addresses, ports, hostnames, keys, tokens, account identifiers, and provider credentials;
- complete system prompts or safety-sensitive behavioural instructions;
- deployment commands that expose infrastructure;
- vulnerability details or bypass instructions;
- filenames or hashes whose disclosure would reveal confidential content.

Future public receipts must use generic labels, counts, hashes, and bounded aggregate metrics. Detailed security findings, monetisation plans, and operating procedures belong in private controlled records.

## 16. Comparison with external evidence

Current research provides useful constraints but does not validate Lina EI by analogy.

- Adaptive-intelligence research emphasises online learning, environmental feedback, and generalisation. This supports testing those properties, not assuming them from neuroscience-inspired naming. See Mackenzie Weygandt Mathis, “Leveraging insights from neuroscience to build adaptive artificial intelligence,” *Nature Neuroscience* (2026), https://www.nature.com/articles/s41593-025-02169-w.
- Small-language-model research supports the feasibility of some on-device language tasks, while documenting capability and efficiency trade-offs. It does not establish Lina EI performance. See Nguyen et al., “A Survey on Small Language Models,” RANLP 2025, https://aclanthology.org/2025.ranlp-1.93/.
- Research on parasocial AI indicates both demand and material user risks. It is a market and safety signal, not proof of beneficial outcomes. See Qian et al., “Mapping the Parasocial AI Market: User Trends, Engagement and Risks,” arXiv:2507.14226 (2025), https://arxiv.org/abs/2507.14226.
- Physical collective oscillations and programmable active media demonstrate that distributed local interactions can create macroscopic patterns. They do not imply cognition. Examples include “Large-scale-integration and collective oscillations of 2D artificial cells,” *Nature Communications* (2024), https://www.nature.com/articles/s41467-024-54098-0, and “Programming gel automata shapes using DNA instructions,” *Nature Communications* (2024), https://www.nature.com/articles/s41467-024-51198-9.
- AI transparency obligations and related guidance are relevant to product design in the European Union. This report is not legal advice. Authoritative starting points include Regulation (EU) 2024/1689 and European Commission transparency guidance.

The scientifically relevant shared structure is local interaction, persistent state, feedback, adaptation, and collective dynamics. The important mismatch is that biological and physical systems have experimentally grounded carriers, conservation or exchange ledgers, and intervention evidence, while Lina EI currently uses engineered software variables whose cognitive interpretation remains under test.

## 17. Decision ledger

| Decision | Evidence | Status |
|---|---|---|
| Treat Lina EI as a hybrid persistent agent prototype | Static architecture and implementation audit | supported at implementation level |
| Claim full emergence | No causal, relocation, ablation, or generalisation evidence retained | unsupported under current evidence |
| Claim consciousness or sentience | No operational test with power over the claim | prohibited |
| Describe current grid as Lineum-inspired | Local multi-field solver and Lineum terminology are present | supported |
| Describe current runtime as using current Lineum Core | No direct package dependency or audited import path | unsupported |
| Move private Lina implementation into public Core | Violates repository boundary and lacks general promotion evidence | rejected |
| Build a private adapter consuming pinned Core | Preserves dependency direction and enables equivalence testing | selected next integration path |
| Publish detailed monetisation and security strategy in Core | Public/private boundary and confidentiality risk | rejected |
| Use a public-safe high-level commercial assessment | Useful for research prioritisation without exposing private strategy | supported |

## 18. Claims explicitly not established

This checkpoint does not establish that:

- the private Git snapshot exactly matches production;
- the inspected tests pass;
- the current solver is numerically stable across its intended operating domain;
- field dynamics are necessary for Lina’s useful behaviour;
- semantics emerge from the grid;
- the system learns online in a robust, generalisable way;
- sleep or dream routines improve cognition;
- autonomous self-modification is safe or reliable;
- current hardware performance, latency, energy, or cost claims are accurate;
- the system is secure against realistic adversaries;
- Lina EI is conscious, alive, sentient, or biologically equivalent;
- Lineum describes real cognition in nature;
- any business model is profitable or investable.

## 19. Exact next checkpoint

The next coherent checkpoint is **P0 plus P1**:

1. obtain and retain a sanitised Git-to-production synchronisation receipt;
2. freeze a privacy-safe baseline configuration;
3. execute the current simulator and selected tests in an isolated environment;
4. retain raw machine-readable outputs, hashes, environment metadata, and failures;
5. independently verify at least one toy or known-answer case;
6. append the results without rewriting this historical baseline.

No whitepaper or public product claim should be changed from this report alone.

## 20. Checkpoint receipt

- Source inspection type: static, read-only private-source audit.
- Private source commit: `f62a2c547675c79a2399a76e2bf82d0d02581298`.
- Core base commit: `034f343605c1d0eac05820301fae67887c99a479`.
- Runtime commands executed: none.
- Tests executed: none.
- Production-host access: unavailable.
- Personal or secret data retained in this report: none intentionally.
- Scientific evidence level: `implemented/static audit`.
- Primary unresolved issue: runtime and deployment parity, followed by causal necessity of the field grid.
