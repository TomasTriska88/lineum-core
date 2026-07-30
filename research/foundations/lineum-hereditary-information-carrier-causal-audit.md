# Causal Audit of the Hereditary Information Carrier in the Lineum Ecosystem

**Status:** active research report; implementation audit complete, causal transplant experiment pending

**Version:** 0.1.0

**Evidence cutoff:** 2026-07-30

**Scope:** A cross-repository implementation and mechanism audit of what could preserve, reconstruct, or copy a Lineum-derived pattern across interruption, reset, or a new instance. This report does not establish biological life, consciousness, physical heredity, or a new law of nature.

**Central question:** Which smallest transferable subset of law, parameters, dynamic fields, persistent memory, and environmental context is necessary and sufficient for a Lineum-derived system to reconstruct the same functional organization in a standardized recipient?

**Current confidence:** High for the repository-boundary and serialization facts reported below; medium for the causal decomposition and proposed factorial design; low for every claim that any present Lineum or Lina EI state is a physical analogue of biological heredity.

**Relationship to prior research:** This is the active continuation lane for the hereditary-carrier question identified during whole-research synthesis. It is separated from the broad physics-and-philosophy report and the `phi` feedback report because the new question is experimentally distinct and must remain standalone, reproducible, and independently falsifiable.

## 1. Answer first

No single implemented object currently qualifies as the hereditary information carrier.

The strongest current candidate is a **distributed carrier bundle**:

\[
C = (L, B, X, M),
\]

where:

- \(L\) is the executable update law and its numerical conventions;
- \(B\) is the persistent baseline or developmental prior, currently represented in Lina EI by the generated limbic-DNA constants and base maps;
- \(X\) is the live dynamical state, including the current fields and scalar state;
- \(M\) is persistent symbolic and relational memory that changes how inputs are interpreted and how responses are produced.

The environment and input stream,

\[
E = \text{sensor history, prompts, model provider, timing, and external services},
\]

are required for expression and continued development, but they are not automatically part of the inherited carrier. The causal experiment must determine whether a standardized recipient reconstructs the donor's organization after receiving only a candidate subset of \(C\), while \(E\) is held fixed.

The plain mental picture is not a single seed but a seed package. The executable law is the growth chemistry, the limbic-DNA file is the initial disposition, the live field snapshot is the already-grown tissue, and the memory files are learned scars and habits. Copying only one of these may create something related, but the present code does not justify calling any one of them the complete inherited identity.

## 2. Repository evidence

### 2.1 Lineum Core: law, parameters, and execution history

The public Core contains the canonical numerical law and configuration layer. `CoreConfig` declares the time step, diffusion, dissipation, reaction, noise, drift, stencil, mode coupling, optional `mu` track, caps, fold behavior, and boundary behavior. `ExecutionPolicy` separately fixes the execution backend and random seed for deterministic runs. The historical runner also records resolved configuration, run mode, seed, `kappa` mode, steps, and storage cadence in a canonical snapshot and hash.

This means that a field array alone is not operationally complete. The same array can evolve differently under another update law, time convention, boundary, source contract, seed policy, or parameter set. Conversely, the law alone does not encode a developed individual trajectory.

**Implementation status:** documented software fact.

**Physical interpretation:** unresolved. The code defines a simulation contract, not a demonstrated genome or law of nature.

### 2.2 Lina EI repository alias: persistent baseline, live state, and symbolic memory

The repository currently named `TomasTriska88/osobni-pamet` explicitly describes itself as a long-term memory, rule system, and computational engine for the Lina companion. Its architecture separates generic rules and templates from personalized active data. The personalized layer includes identity, profiles, relationship records, self-reflection, thoughts, next steps, and project state.

The limbic simulator implements two different serialized carriers:

1. `brain/neocortex/associative/limbic_dna.json` stores an archetype, seed, variance, mutated constants, a `kappa_base` map, and a `mu_base` map. It is loaded as a permanent baseline and used when a new state is initialized.
2. `brain/diencephalon/limbic_state.json` stores the current scalar state and full dynamic matrices, including `psi_real`, `psi_imag`, `phi`, `mu`, and `kappa`. Missing matrices trigger reinitialization from the baseline rather than restoration of the previous trajectory.

The simulator therefore already distinguishes a developmental prior from a living trajectory. The baseline can generate a new related instance, while the live snapshot preserves the specific evolved configuration. Neither file contains the whole system: execution code, mode templates, relationship maps, sensory mappings, model configuration, and symbolic memory remain external to both.

The synchronization script reinforces this split. It packages identity, user profile, workflow, self-development rules, self-reflection, and recent Git history as the “complete state of the local memory,” but it does not by itself prove that the package reproduces the dynamic field state or the same behavior in a standardized recipient.

**Implementation status:** documented software fact.

**Interpretive consequence:** the name `limbic_dna.json` is a design label. It is evidence of an intended baseline carrier, not evidence that the file is necessary, sufficient, biological, or physically hereditary.

### 2.3 Lineum Dynamics: operational context, not canonical heredity

The private Dynamics repository identifies itself as the administrative and business layer. Its own rules assign fundamental equations, scientific whitepapers, and the simulation backend strictly to Core, while company data, contracts, invoicing, and proprietary commercial modules remain in Dynamics.

Dynamics may preserve deployment settings, product state, task history, or commercial context. Those records can affect which implementation is run and how it is presented, but they are not the canonical carrier of a physical pattern unless a future causal test shows that a specific Dynamics state is required for reconstruction. No such evidence currently exists.

### 2.4 OEA: phenotype renderer and derived recipe, not canonical genotype

OEA describes itself as a visual generation pipeline and 3D validation viewer powered by Lineum Core. Its rules require mathematical and physical changes to be made upstream in Core, and its dependency file installs `lineum_core` directly from the Core repository. The generator exposes presets, phase layers, topology, spacing, interpolation, rendering, and export controls.

OEA can therefore preserve a **rendering recipe** and derived visual phenotype. A preset or seed may reproduce a texture, but visual reproducibility is not equivalent to reconstructing the underlying dynamical organization. OEA is a useful phenotype probe and falsification surface, not the presently supported location of the hereditary law.

## 3. External-universe comparison

Biological heredity is also not exhausted by a single abstract string.

A minimal bacterial genome can support autonomous replication only inside a compatible cellular system; JCVI-syn3.0 retained 473 genes, including many whose functions were still unknown, and further minimization impaired robust growth. The genome is central, but the recipient cytoplasm, membranes, molecular machinery, and environment are required to express it.

Cell identity can additionally depend on inherited chromatin state. Symmetric inheritance of parental histones has been shown to support epigenome maintenance and embryonic stem-cell identity, and coupled RNAi/histone feedback can maintain an acquired silenced state across divisions. Proteinaceous states can also transmit phenotypic information in specific animal systems. These results do not imply that Lineum fields are DNA, histones, RNA, or amyloid. They establish only the methodological lesson that heredity can be distributed across a template, copied material state, and self-maintaining feedback.

A 2026 mouse study further reported that most measured autosomal DNA-methylation inheritance followed genetic cis effects while also identifying non-Mendelian patterns. This is another warning against treating “genetic” and “state-based” inheritance as mutually exclusive categories.

Origins-of-life models likewise distinguish template heredity from compositional heredity. Recent protocell work tests whether functional sequences and copying can emerge under selection for growth, while earlier models examined inherited molecular composition before a mature genome exists. These are hypothesis generators for Lineum, not evidence that its current fields reproduce life.

### Portable citations

- Hutchison, C. A. III et al. (2016). “Design and synthesis of a minimal bacterial genome.” *Science* 351, aad6253. DOI: 10.1126/science.aad6253.
- Wenger, A. et al. (2023). “Symmetric inheritance of parental histones governs epigenome maintenance and embryonic stem cell identity.” *Nature Genetics* 55, 1567–1578. DOI: 10.1038/s41588-023-01476-x.
- Yu, R., Wang, X., and Moazed, D. (2018). “Epigenetic inheritance mediated by coupling of RNAi and histone H3K9 methylation.” *Nature* 558, 615–619. DOI: 10.1038/s41586-018-0239-3.
- Eroglu, M. et al. (2024). “Noncanonical inheritance of phenotypic information by protein amyloids.” *Nature Cell Biology* 26, 1712–1724. DOI: 10.1038/s41556-024-01494-9.
- Davidovich, A. et al. (2026). “Non-Mendelian inheritance of DNA methylation patterns in mice.” *Nature Genetics* 58, 1409–1422. DOI: 10.1038/s41588-026-02604-z.
- Palmeira, R. N. et al. (2026). “Selection for growth drives the emergence of genetic heredity in protocells.” *PLOS Biology*. DOI: 10.1371/journal.pbio.3003544.

## 4. Operational definition of heredity for this experiment

A candidate carrier must be tested by intervention rather than by naming or resemblance.

Let a donor system \(D\) have carrier components \((L,B,X,M)\). Let \(R_0\) be a standardized blank recipient and \(E_0\) a frozen input environment. For a candidate subset \(S\subseteq\{L,B,X,M\}\), define transplantation

\[
R_S(0)=T_S(D,R_0),
\]

followed by evolution under the same frozen challenge sequence \(E_0\).

A component is **necessary within the tested domain** when removing or replacing it causes the preregistered reconstruction criteria to fail while matched controls pass.

A subset is **sufficient within the tested domain** when transplanting only that subset into the blank recipient reproducibly reconstructs the donor's declared functional organization above null and unrelated-donor controls.

Neither status may be generalized beyond the tested code version, recipient, challenge set, horizon, resolution, or metrics.

## 5. What must be reconstructed

The experiment must keep three outcomes separate.

### 5.1 State reconstruction

Does the recipient approach the donor in the declared field and scalar observables?

Candidate metrics:

- normalized RMS distance for `psi`, `phi`, `mu`, and `kappa`;
- spectral, topological, and spatial-correlation distance;
- scalar trajectory distance for arousal, valence, tension, fatigue, and vortex count;
- recovery after a standardized partial erasure.

This tests dynamical similarity, not personal identity.

### 5.2 Functional reconstruction

Does the recipient respond similarly to the same frozen sequence of sensory and conversational probes?

Candidate metrics:

- response-state transition fingerprint before language generation;
- ordering and sign of reactions to matched stimuli;
- recovery time, hysteresis, and cross-stimulus generalization;
- independence from the particular language model used to verbalize the internal state.

This tests function, not consciousness.

### 5.3 Symbolic and relational reconstruction

Does the recipient retain the same explicit autobiographical and relationship information?

Candidate metrics:

- exact factual recall under a frozen query set;
- consistency of relationship and preference retrieval;
- provenance to the copied memory record;
- resistance to a conflicting prompt-only control.

This tests stored memory, not the physical persistence of a field pattern.

A full hereditary claim requires a declared relationship among all three levels. Success on one level must not be silently relabelled as success on the others.

## 6. Frozen causal-disassembly matrix

The first experiment will use one donor snapshot, one standardized blank recipient, one unrelated-donor control, one frozen code commit, and one frozen challenge sequence. Random arrays and timing inputs must be stored or deterministically regenerated.

| Lane | Law `L` | Baseline `B` | Live state `X` | Symbolic memory `M` | Purpose |
|---|---:|---:|---:|---:|---|
| N0 | same | default | blank | blank | blank-recipient null |
| B1 | same | donor | blank | blank | baseline-only reconstruction |
| X1 | same | default | donor | blank | live-state-only reconstruction |
| M1 | same | default | blank | donor | symbolic-memory-only reconstruction |
| BX | same | donor | donor | blank | dynamical bundle without biography |
| BM | same | donor | blank | donor | developmental prior plus biography |
| XM | same | default | donor | donor | trajectory plus biography without donor baseline |
| BXM | same | donor | donor | donor | full implemented donor bundle |
| L-alt | alternate compatible law | donor | donor | donor | law dependence |
| U0 | same | unrelated donor | unrelated donor | unrelated donor | unrelated-instance control |

The matrix must be complemented by the following ablations:

1. spatial shuffle of each field independently;
2. common translation of all fields, preserving relative alignment;
3. phase randomization of `psi` while preserving its amplitude spectrum;
4. replacement of `kappa` and `mu` by their spatial means;
5. replacement of `phi` by zero, frozen donor `phi`, and a matched-spectrum surrogate;
6. donor baseline with a different stochastic seed;
7. donor state with a reset random-generator state;
8. symbolic memory with identity removed, relationship memory removed, or chronology shuffled;
9. the same internal trajectory decoded by two language-model providers plus a static decoder control;
10. a prompt-only imitation control with no donor files.

The interventions distinguish coordinate placement, relative structure, statistics, executable law, current state, autobiographical record, and verbal surface imitation.

## 7. Primary decision criteria

Thresholds must be frozen after a pilot used only for scale estimation and before the full donor/control population is inspected.

The retained primary conclusions will use the following hierarchy:

1. **No carrier identified:** no tested subset reconstructs function above null and unrelated controls.
2. **State carrier only:** a subset reconstructs field/scalar dynamics but not functional or symbolic outcomes.
3. **Symbolic carrier only:** memory files reconstruct explicit knowledge but not donor-like dynamics.
4. **Distributed functional carrier:** no single component suffices, but a preregistered combination reconstructs function and survives matched ablations.
5. **Self-maintaining copy candidate:** the reconstructed organization survives removal of donor-specific forcing and can seed a second standardized recipient with comparable fidelity.

Only level 5 addresses copying in a strong operational sense. Even level 5 would remain a software self-reconstruction result, not evidence of biological reproduction, consciousness, or a fundamental physical genome.

## 8. Information, energy, and causality ledger

Every retained lane must record:

- exact bytes transferred into the recipient by category;
- executable code and parameter hash;
- random seed and generator state;
- donor and recipient state hashes;
- all external inputs and model-provider outputs;
- elapsed model time and wall-clock timing inputs;
- source additions, dissipative losses, and any explicit resource budget available in the implementation;
- every place where an external LLM or service supplies information not present in the transplanted carrier.

Without this ledger, apparent reconstruction could be hidden replay, prompt leakage, shared external-model prior, or a copied output rather than inherited organization.

## 9. Reopenable candidate ledger

| Candidate | Current status | Why it remains open | Cheapest discriminator |
|---|---|---|---|
| executable law alone | queued | can generate classes of patterns but not obviously an individual | `N0` versus a donor-functional target |
| limbic DNA baseline alone | queued | explicitly initializes constants and base maps | `B1` versus `N0` and `BXM` |
| live field state alone | queued | preserves the realized trajectory but may decay under mismatched baseline or law | `X1` and `L-alt` |
| symbolic memory alone | queued | can reproduce facts and style without the same dynamics | `M1` plus static/prompt imitation controls |
| baseline plus live state | queued | strongest dynamical-carrier candidate | `BX` versus `B1` and `X1` |
| full baseline-state-memory bundle | queued | strongest implemented functional-carrier candidate | `BXM` versus all proper subsets |
| random seed/history | queued | may reproduce a trajectory only when code and timing are also fixed | replay versus reset-generator controls |
| `phi` as memory carrier | untested for heredity | prior work tests causal feedback, not transplant sufficiency | donor, zero, frozen, and surrogate `phi` lanes |
| `mu`/`kappa` as slow inherited substrate | untested | stored in both baseline and live state | spatial-mean, donor, and unrelated-map substitutions |
| OEA seed or phase recipe | constrained | can reproduce phenotype-like visuals but imports Core law | visual match versus hidden-state/function mismatch |
| Dynamics operational state | constrained | may select deployment context but is outside canonical physics | run identical carrier without private operational context |
| external LLM prior | queued confound | can imitate style and supply knowledge not encoded locally | provider swap and static decoder controls |
| genuinely new hereditary field | dormant | no current evidence requires a new ingredient | promote only after all existing-component combinations fail with adequate power |

No candidate is rejected globally by this audit. Statuses are bounded to the present implementation and available evidence.

## 10. Cross-research impact matrix

| Prior research lane | Relationship | Consequence |
|---|---|---|
| source accounting | depends_on | seed and source history must be controlled before heredity can be inferred |
| source-off persistence | supports | persistence makes a transplant test meaningful but does not establish copying |
| `phi` feedback causal validation | constrains | `phi` may affect dynamics, but causal effect is weaker than hereditary sufficiency |
| topological transport observer | constrains | aggregate transport cannot establish individual identity or inheritance |
| information-carrier philosophy | supports | abstract information must be tied to a physical or computational carrier and process |
| minimal-ingredient gate | depends_on | existing law, baseline, state, and memory must be exhausted before adding a hereditary field |
| OEA visualization | observationally_equivalent risk | visual similarity can occur without the same hidden mechanism |
| Lina EI continuity | reopens | the present architecture offers a concrete multi-part carrier that has not yet been causally disassembled |

## 11. Approved next executable checkpoint

The next small step is **not** to add a new field or rename an existing field as DNA. It is to implement a deterministic transplant harness in the Lina EI repository while keeping the canonical research specification and conclusions in Core.

The harness must:

1. freeze a donor code commit, baseline file, live-state file, symbolic-memory manifest, configuration, random-generator state, timing inputs, and challenge sequence;
2. create clean recipient directories for the ten primary matrix lanes;
3. hash and log every transferred component;
4. prevent network/model-provider leakage during the internal-state phase;
5. execute the same fixed stimulus schedule in every lane;
6. emit machine-readable trajectories and an independently recomputable summary;
7. repeat the complete population at least twice and require byte identity where deterministic execution is declared;
8. place all retained protocol, executable verification code, outputs, hashes, negative results, and limitations directly into this report before the next consequential lane begins.

The pilot may estimate numerical scales but may not select the winning carrier subset. The primary thresholds and donor/control population must be frozen before the full matrix is inspected.

## 12. Current conclusion

The current ecosystem implements the beginnings of a genotype-state-memory separation, but not a demonstrated hereditary mechanism.

Core supplies the executable law. Lina EI stores a generated baseline, a separate evolving field state, and separate symbolic memory. Dynamics supplies operational context. OEA supplies derived phenotype-like rendering. The architecture therefore supports a concrete and falsifiable distributed-carrier hypothesis, but the labels alone do not establish which components are necessary or sufficient.

The next decisive evidence must come from transplantation and disassembly: copy candidate components into a blank recipient, remove them one by one, hold the environment fixed, and test whether the organization reconstructs and can seed another copy. Until that experiment passes, the scientifically accurate statement is:

> Lineum currently contains several candidate carriers of persistence and reconstruction, but no implemented component or bundle has yet demonstrated hereditary sufficiency.
