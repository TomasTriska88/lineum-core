# Ancient Texts as Dynamic-Boundary, Protocol, Reconstruction, and Accounting Hypothesis Generators for Lineum

**Status:** active source-critical conceptual research, current-Core coupling/accounting audit, preregistration, and thread-independent missing-piece research checkpoint; FAC0 source-graph inspection is supported and independently corroborated only in an unsupported local numerical environment; no new field, Core equation, whitepaper change, numerical physical validation, or ancient-physics claim is authorized  
**Version:** 0.3.1  
**Evidence cutoff:** 2026-08-07  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Core snapshot at this checkpoint:** `eb976b97a233ac2c4d83eac53c290aab0d137e4e`  
**Current runtime source:** `lineum_core/math.py`, blob `bb877021810691223a0eb960a45493a2e351112a`  
**Current profile source:** `lineum_core/profiles.py`, blob `3a21be878bc61c7c8612c1040acf01c4d4869f90`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`  
**Recovered root version:** 0.4.14  
**Root evidence cutoff:** 2026-07-29  
**Root blob SHA:** `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`  
**Continuity version:** 0.3.0  
**Continuity evidence cutoff:** 2026-07-31  
**Continuity blob SHA:** `5304874451caf32313ad0e8e3c59e53958698d79`  
**Immediate predecessor:** `research/foundations/lineum-gnostic-enochic-dead-sea-scrolls-metaphor-audit.md`, version 0.2.0, blob `aa7895df7e66ff348159c8ecbb6d06a92f22950c`  
**Previous version of this report:** version 0.3.0, blob `f9e5cdf26a749baf9a2de4a735105830578e7a38`  
**Earlier version of this report:** version 0.2.0, blob `1691f44a88afd7414a32afc3625ef3acdb46fcf7`  
**Initial version of this report:** version 0.1.0, blob `3ec1d893e4309cb2e06b97a2fc09d658f05ab149`  
**Related collective-object report:** `research/foundations/lineum-core-envelope-wake-and-attraction-preregistration.md`, version 0.2.0, blob `621cc5f9147dde4a3819e9fc2d3febe05e387cf8`  
**Related state-reduction report:** `research/foundations/lineum-mu-branch-relative-identity-and-entanglement-hypothesis.md`, version 0.2.0, blob `b55bc1639fc8ed6efa7b8286e9113afa88ee298c`  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Scope:** Historically separated ancient texts remain hypothesis generators only. This version preserves the earlier boundary, copying, protocol, observer, synchronization, and preparation-history programme, retains the current-Core field/coupling/accounting audit, records the first FAC0 directed-coupling checkpoint, and adds a thread-independent research objective so the programme can be resumed from repository evidence alone. The governing decision remains whether apparent gaps in Lineum are better explained by missing reciprocal relationships, missing explicit source or receiving reservoirs, a supplied rather than dynamic scaffold, insufficient state history, an effective-equation/coarse-graining omission, or only after those fail, a genuinely missing state variable.  
**Central questions:** What does each current Core state variable actually do? Which directed writes are paired transfers and which are unpaired feedback, source, sink, or memory writes? Does the observed one-step response graph agree with source inspection? Is any quantity currently justified as total physical energy? Can a closed resource account be built without a new fundamental field? What intervention would make an additional state variable necessary rather than merely convenient? Could the current equations be effective dynamics of a deeper generative process, and if so, can that hypothesis make a distinct falsifiable prediction rather than merely absorb residuals? Which ancient motifs independently motivate useful comparison classes without being treated as evidence about nature?  
**Current confidence:** high that the current Core does not yet provide a demonstrated closed physical source/transfer/sink account; high from source inspection that only a subset of current writes are explicitly paired debit/credit operations; high that FAC0 source-level directed edges and same-step ordering implications are correctly identified; medium that explicit reservoirs, reciprocal closure, dynamic boundaries, and history-aware observers are the cheapest next mechanism classes; low that an additional independent state variable will be required; low and untested that a deeper generative/effective-equation layer is needed; zero evidential support that ancient religious texts encode Lineum or modern physics. The numerical FAC0 corroboration is provisional because the available local Python environment violated the repository NumPy contract.

## 1. Answer first

The strongest result is now more specific than the earlier metaphor audit.

The current scientific gap is **not yet evidence that Lineum needs more fundamental fields**. The better-supported statement is:

```text
current Core state graph != demonstrated closed physical resource graph
```

The runtime contains `Psi`, `Phi`, supplied `kappa`, optional `mu`, optional supplied `delta`, stochastic/source terms, diffusion, dissipation, caps, and boundary loss. These elements do not all participate in reciprocal accounting.

One current path is explicitly paired at the implementation level: with mode coupling enabled, a scalar quantity `delta_e` is credited to `Phi` and subtracted from `|Psi|^2` before `Psi` is rescaled. That is a real paired debit/credit in the code. It is **not yet proof that `|Psi|^2 + Phi` is physical energy**.

Several other paths are one-way:

```text
Phi -> Psi interaction feedback          without a matching Phi debit;
grad(Phi) -> Psi drift                   without a matching Phi debit;
Psi activity -> mu                       without a matching Psi debit;
mu -> strength of Phi-to-Psi feedback    without a matching mu debit;
kappa -> most update terms               while kappa itself is not evolved;
stochastic/coherent source -> Psi        without a finite source stock;
Psi dissipation / PML / caps             without an explicit receiving reservoir;
mu decay                                 without an explicit receiving reservoir.
```

FAC0 now adds an ordering result. The source-level graph is consistent with a direct reading of the implementation, but a complete **one-step** response graph contains indirect edges because the update is sequential. A `Phi` perturbation changes `Psi` and can therefore alter the later `mu` write in the same step. A `mu` perturbation changes `Psi` and can therefore alter the later mode-coupling write into `Phi`. A `kappa` perturbation can reach all dynamic outputs while `kappa` itself remains supplied. With stochastic source disabled, `delta` has no effect because it only enters the source-probability path.

Therefore phrases such as `energy transferred from Psi to mu`, `Phi gives energy back to Psi`, or `kappa stores energy` are presently too strong unless a particular experiment supplies an explicit ledger that passes.

The ancient-text research remains useful because several source-grounded motifs independently force exactly the distinctions the current implementation needs:

```text
stock versus unbounded source;
transfer versus copying or feedback;
receiver versus deletion;
return versus fresh injection;
static boundary versus stateful boundary;
visible image versus complete causal state;
local closure versus complete causal closure.
```

The correct scientific order is therefore:

```text
1. audit current state and directed couplings;
2. define implementation-level accounting candidates without calling them physical energy;
3. test reciprocal closures and explicit finite reservoirs;
4. test whether supplied kappa must become a dynamic state;
5. test whether history of existing fields closes prediction;
6. test an effective-equation/deeper-generative comparison only if it has an explicit coarse-graining map and distinct held-out prediction;
7. only then permit a genuinely new state variable to compete.
```

Ancient terminology must never become field nomenclature merely because it sounds suggestive.

## 2. Version history and continuity

Version `0.1.0` is permanently preserved as Git blob `3ec1d893e4309cb2e06b97a2fc09d658f05ab149`. It established six principal systems questions and the associated known-answer tests:

- `DB1`: active boundary versus inert wall, selective gate, finite receiving store, stabilizing boundary, and hidden pump;
- `IC1`: full causal state versus image, relational signature, generative recipe, short history, and matched nulls;
- `PH1`: different preparation histories matched on coarse present observables;
- `PI1`: exact, behaviorally equivalent, mutated, and convergent protocols under member turnover and perturbation;
- `TS1`: six mechanisms producing similar binary labels without assuming two substances;
- `EC1`: internally exact schedule versus external calibration;
- `SY1`: one-way write versus reciprocal back-reaction, finite stock, adjoint estimator, and explicit return channel;
- dynamic-scaffold gate: static supplied `kappa` versus a constructed, maintained, damaged, repaired, finite-cost scaffold.

Version `0.2.0`, preserved as Git blob `1691f44a88afd7414a32afc3625ef3acdb46fcf7`, added the current-Core state/coupling/accounting audit, the `M0` through `M7` missing-mechanism registry, and FAC0 through FAC5 preregistration.

Version `0.3.0`, preserved as Git blob `f9e5cdf26a749baf9a2de4a735105830578e7a38`, recorded the first FAC0 execution checkpoint. Source inspection supports the preregistered graph and exposes same-step indirect edges caused by update order. A separately transcribed NumPy checker reproduced the predicted response pattern and linear perturbation scaling, but the available execution environment used Python 3.13.5 with NumPy 2.3.5 while the repository requires `numpy>=1.24,<2.0.0`. A clean virtual environment could not obtain a compatible NumPy build from the available package index, and direct local repository cloning was unavailable because the execution environment could not resolve GitHub. The numerical FAC0 result is therefore retained as provisional corroboration, not as a supported-runtime Core reproduction.

Version `0.3.1` adds a self-contained research objective and resume checkpoint. It records the missing-piece search order, explicitly preserves the possibility that the current equations are effective/coarse-grained rather than fundamental, and prevents that possibility from being used as an unfalsifiable rescue. It also records that a renewed disposable local checkout attempt on 2026-08-07 again failed because the execution environment could not resolve `github.com`; this repeats the known technical blocker and is not a scientific negative result.

No negative result or source-critical restriction from versions `0.1.0` through `0.3.0` is withdrawn here.

The broad predecessor remains the source and historical registry. This successor remains the active mechanism and preregistration report.

## 3. Historical separation and media-source rule

The following source families remain separate unless a specific historical relationship is demonstrated:

```text
Stoic pneuma physics;
Sethian and related Nag Hammadi creation narratives;
Valentinian traditions and surviving Valentinian-related texts;
Pistis Sophia and its own textual tradition;
1 Enoch and related Enochic literature;
Qumran sectarian, wisdom, calendrical, and liturgical manuscripts;
modern videos, summaries, podcasts, and synthetic retellings.
```

Modern media are discovery aids, not textual witnesses.

The owner supplied an auto-generated Czech subtitle file for YouTube video `aYhko3jlQFk`. The transcript is treated as third-party media intake. It is not committed to this public repository. Decision-relevant claims from the video must be checked against named primary texts and critical scholarship before entering the source-grounded layer.

The video itself states that it assembled material into one continuous narrative. That is a useful provenance warning: apparent coherence in the video is not evidence that the ancient corpora formed one coherent cosmology.

## 4. Evidence layers

Every retained statement belongs to exactly one level:

1. **Textual or manuscript witness:** what a named source actually says.
2. **Historical interpretation:** what critical scholarship cautiously infers about the source, transmission, or context.
3. **Domain-neutral structural abstraction:** a systems pattern that does not depend on Lineum being true.
4. **Current implementation fact:** what the current Core source actually computes.
5. **Reproducible Lineum observation:** what a frozen execution actually produced.
6. **Lineum hypothesis:** a mechanism class or test inspired by the preceding layers.
7. **Physical correspondence:** a claim about nature, allowed only after independent empirical evidence.

No textual analogy may jump directly from level 1 to level 7. No green internal simulation may jump directly from level 5 to level 7.

## 5. Source-critical check of the supplied video

### 5.1 Supported or substantially source-grounded motifs

The following broad motifs have primary-text support, although the video's wording often modernizes them:

- A chief ruler is ignorant of the higher source of his own power and makes an exclusive divine claim. This is attested in the *Apocryphon of John* and related creation narratives.
- *On the Origin of the World* describes seven powers associated with seven heavens of chaos and a ruler who creates heavens for his offspring.
- The *Apocryphon of John* describes powers held by rulers contributing to the fashioned human; the human later possesses powers associated with those authorities and contains a hidden light/Epinoia motif.
- *Pistis Sophia* chapters 25–26 contain language of rulers possessing power/light, receivers removing and carrying power/light, transfer to the Treasury of the Light, weakening/exhaustion when power diminishes, and rulers consuming their own matter so as to delay exhaustion.

These are textual motifs. None of the words `power`, `light`, `matter`, `Treasury`, or `receiver` is automatically a modern physical energy term.

### 5.2 Video synthesis or claims not yet established by the cited source

The following must not be imported as primary-text facts without a precise coordinate:

- the video's assignment of one sphere each to modern psychological functions such as time, desire, fear, forgetting, habit, physiological need, and separation;
- the claim that the relevant ancient texts present a modern system-administrator model;
- the claim that the *Pistis Sophia* is the source of a simple universal pneumatic/psychic/hylic human taxonomy in the form presented by the video;
- the claim that a `false awakening` is explicitly the final weapon of an archon;
- the translation of a hidden light or power into literal `Sophia light energy` in the physical sense.

These may remain media-level hypotheses until primary-text evidence is recovered.

### 5.3 Athanasius and the destruction narrative

Athanasius' thirty-ninth Festal Letter of 367 lists canonical books and sharply rejects apocryphal writings presented as scripture. The accessible text does **not** contain the blanket quotation used in the video ordering that all other texts be destroyed.

The idea that Nag Hammadi codices were hidden in response to Athanasius or monastic canonical pressure is a historical hypothesis, not a demonstrated fact about the act of burial. Therefore the report records:

```text
Athanasius_defined_and_defended_a_canon = supported
Athanasius_blanket_destroy_all_other_texts_quote = unsupported_in_checked_letter
Nag_Hammadi_hidden_because_of_that_letter = historical_hypothesis_not_established_fact
```

## 6. Preserved mechanism family: active boundary

A functional boundary must be decomposed before any field is promoted as `the boundary`:

```text
B0 geometric separator;
B1 selective gate;
B2 receiving interface with finite state;
B3 stabilizing boundary with restoring feedback;
B4 active participant that can fail, recover, and synchronize;
B5 hidden pump that only appears stabilizing because it injects undeclared resources.
```

The inherited current-field membrane result remains negative: tested current-field candidates did not demonstrate a passive, elastic, reversible membrane with complete temporary storage and return accounting.

`DB1` remains preregistered. A boundary candidate must outperform inert and gate-only controls while preserving a declared ledger, predicting finite-capacity exhaustion where applicable, responding specifically to deformation, and surviving numerical refinement.

A successful active-boundary toy would not prove Horos, archons, a higher dimension, an organism, or a physical membrane in nature.

## 7. Preserved mechanism family: projection versus causal state

The earlier image/copy audit remains binding:

```text
full causal state      = state sufficient for held-out continuation;
projected image        = morphology/amplitude or another many-to-one observation;
relational signature   = selected invariants among components;
generative recipe      = instructions capable of growing a family of states;
activation state       = current dynamical organization omitted by recipe or image;
short history          = temporal information that may reconstruct omitted state.
```

Existing Lineum transplant evidence remains unchanged:

- exact live state plus exact future RNG state reproduced continuation exactly in the tested transplant;
- a static recipe under independent developmental history reproduced broad morphology but not the donor state;
- adding the recipe to the exact live state added no observed advantage over the live state;
- tested copying lanes did not establish content-specific descendants.

`IC1` remains queued. It is not deleted by the new accounting priority.

## 8. Preserved mechanism family: preparation history and protocol identity

`PH1` remains the test of whether states matched on coarse observables can diverge because their hidden phase, memory, correlations, boundary state, reservoir state, or basin membership differ.

`PI1` remains the test of functional protocol identity:

```text
PI0 exact state identity;
PI1 exact protocol identity;
PI2 behaviorally equivalent protocol identity;
PI3 family resemblance under bounded variants;
PI4 shared label with materially different behavior;
PI5 convergent behavior without common lineage.
```

Functional identity requires held-out intervention equivalence. Lineage requires transmission evidence. Heredity requires content-specific transfer with null controls.

## 9. Preserved mechanism family: binary labels do not imply two substances

The Two Spirits material remains a useful anti-ontology warning, not a two-field prescription.

Matched binary observations can arise from:

```text
TS0 two independent state variables;
TS1 two coupled modes of one state;
TS2 one bistable nonlinear system;
TS3 continuous state projected through a threshold;
TS4 competing attractors with history dependence;
TS5 observer or normative labels imposed on richer dynamics.
```

A second substance is justified only when simpler one-state, mixture, attractor, history, and observer models fail held-out intervention tests with comparable complexity and accounting.

## 10. Preserved mechanism family: internal exactness is not external truth

The 364-day calendrical comparison remains methodological:

```text
internal closure != empirical calibration
```

An internally exact Lineum law, ledger, oscillator, schedule, or conserved implementation quantity is not thereby a validated law of nature. `EC1` remains queued as a known-answer calibration fixture.

## 11. Preserved mechanism family: reciprocal closure before ontology

The earlier syzygy abstraction remains useful only in this domain-neutral form:

```text
one-way write;
reciprocal back-reaction;
finite-stock debit;
explicit receiving store;
return channel;
adjoint estimator with no physical feedback.
```

The rule is not `every field needs a mystical partner`. The rule is:

> Before inventing an additional substance to explain a one-way effect, compare the one-way implementation with the cheapest explicit reciprocal and resource-accounting alternatives.

This principle is now elevated from a conceptual motif to the immediate current-Core audit.

## 12. Current Core state inventory

The audited current runtime contains the following state or supplied inputs.

| Symbol / term | Current implementation role | Dynamically updated by `step_core`? | Current physical status |
|---|---|---:|---|
| `Psi` | complex active field; receives source, interaction, drift, diffusion, dissipation, and optional paired mode debit | yes | effective simulation state; no established particle or universal matter ontology |
| `Phi` | real interaction/environment field; receives mode-coupling or fallback reaction and diffusion; affects `Psi` | yes | effective simulation state; physical energy/gravity identification unproven |
| `kappa` | supplied local modulation/permissivity structure used throughout couplings and diffusion | no | external/supplied structure in current step; no demonstrated reciprocal back-reaction |
| `mu` | optional local slow reinforcement/memory state written from `Psi` activity and used to multiply `Phi`-to-`Psi` effects | yes when enabled | memory/reinforcement coordinate; independent physical ontology unproven |
| `delta` | optional supplied semantic/perturbation field entering the source-probability gradient through `amp + delta` | not returned/updated by `step_core` | external input in the current step contract, not a demonstrated physical field |
| stochastic/linon source | injects complex `Psi` increments when enabled | regenerated externally by RNG each step | source process; no finite physical reservoir demonstrated |

The deterministic `RD-0-C1` profile deliberately disables mode coupling, `mu`, and stochastic noise. It is a software/reference profile and cannot by itself establish a complete field-transfer ontology.

## 13. Current directed coupling graph

### 13.1 Explicit paired implementation-level transfer

With mode coupling enabled, the current code computes

```text
delta_e = mode_coupling_strength * |Psi|^2 * kappa * dt
Phi <- Phi + delta_e
|Psi|^2 <- max(|Psi|^2 - delta_e, 0)
Psi <- same phase with rescaled magnitude
```

This is an explicit paired debit/credit of the implementation-defined scalar `delta_e`.

Classification:

```text
paired_scalar_transfer_in_code = supported
physical_energy_transfer = not_established
physical_total_energy_function = not_established
```

### 13.2 `Phi -> Psi` interaction feedback

The current interaction factor depends on clipped `Phi`, `kappa`, and `1 + mu`, then adds a bounded complex term proportional to `Psi`.

There is no corresponding decrement of `Phi` in that operation.

Classification:

```text
Phi_affects_Psi = implemented
Phi_is_debited_by_interaction_feedback = false_in_current_update
interaction_feedback_is_physical_energy_return = unsupported
```

### 13.3 `grad(Phi) -> Psi` drift

The current drift term uses the gradient of `Phi`, multiplied by `kappa`, `1 + mu`, and the configured drift strength, then adds the result to `Psi`.

There is no corresponding local `Phi` debit.

Classification:

```text
Phi_gradient_affects_Psi = implemented
paired_Phi_debit_for_drift = not_implemented
physical_return_flux = not_established
```

### 13.4 `Psi -> Phi` fallback reaction

When mode coupling is disabled, `Phi` relaxes toward a function of `|Psi|^2`. The current operation does not rescale or debit `Psi`.

Classification:

```text
fallback_Psi_to_Phi_write = implemented
fallback_reaction_is_reciprocal_transfer = false
```

### 13.5 `Psi -> mu`

When `mu` is enabled, the code forms an active `|Psi|^2` quantity above a dynamic cutoff and adds a positive term to `mu`, followed by `mu` decay and clipping.

No corresponding quantity is removed from `Psi`.

Additionally, the `e_psi` variable used for the `mu` write is calculated before the later mode-coupling rescaling of `Psi` in the same update sequence. Therefore the current `mu` write is especially unsuitable for being casually described as a conserved transfer from the final `Psi` state.

Classification:

```text
Psi_activity_writes_mu = implemented
Psi_is_debited_by_mu_write = false
Psi_to_mu_physical_energy_conversion = unsupported
mu_as_memory_or_reinforcement_write = implementation-consistent_description
```

### 13.6 `mu -> Psi`

`mu` enters through `drift_multiplier = 1 + mu`, strengthening both the `Phi` interaction factor and `Phi`-gradient drift.

There is no corresponding `mu` debit when this feedback affects `Psi`.

Classification:

```text
mu_modulates_Psi_response = implemented
mu_depletion_during_feedback = not_implemented
mu_as_fuel = unsupported
```

### 13.7 `kappa -> dynamics`

`kappa` modulates source probability/effect, interaction, drift, diffusion, mode coupling, fallback reaction, and `mu` growth. It is returned unchanged.

Classification:

```text
kappa_is_high_causal_leverage = implemented
kappa_backreaction = not_implemented
kappa_is_dynamic_geometry_or_resource = unsupported
```

### 13.8 Open sources and sinks

The current runtime contains operations that add or remove implementation quantities without explicit finite receiving/source states:

```text
stochastic/linon source -> Psi       open source unless an external reservoir is supplied;
linear Psi dissipation               sink without receiver;
PML absorption                       boundary sink without receiver;
Psi amplitude cap / divergence reset numerical deletion without receiver;
Phi cap/fold                          numerical/stabilization operation, not a demonstrated resource cycle;
mu decay                             sink without receiver.
```

These may be completely legitimate numerical terms. They simply cannot be silently reinterpreted as a closed physical resource cycle.

## 14. Energy terminology gate

At this checkpoint, `energy` must be used with an explicit qualifier.

Allowed terms:

```text
implementation-defined scalar;
|Psi|^2 norm-like quantity;
paired scalar debit/credit;
state write;
feedback;
source injection;
sink/removal;
spatial redistribution;
receiver-store candidate;
resource-ledger candidate;
accounting residual.
```

Prohibited without a validated functional and calibration:

```text
this is the total physical energy;
Phi is stored physical energy;
mu is energy converted from Psi;
kappa contains energy;
feedback returns the same physical energy;
dissipation transfers energy somewhere known.
```

The current public-TOLOG Question-2 accounting work independently reinforces this restriction. In the verified lanes, `Psi` could recover while `Phi` did not decrease, and an implementation-defined `|Psi|^2 + Phi` ledger grew strongly. That result demonstrates that apparent component recovery must not be called reciprocal return merely from the shape of the trajectory.

This cross-programme evidence does not import TOLOG ontology into this report. It only supplies a current Lineum control against loose accounting language.

## 15. Source-grounded power/depletion motifs as accounting prompts

### 15.1 `Apocryphon of John`

The checked text describes the chief ruler as having received power from his mother and being ignorant of its source. It also describes authorities contributing powers to the fashioned human and a hidden light/Epinoia within the human.

Structural abstraction:

```text
inherited state can pass through a generator that does not fully model its origin;
appearance alone need not identify the full causal state carried by the product.
```

This supports `IC1` and source-provenance questions. It does not establish a physical soul or a modern energy transfer.

### 15.2 `Pistis Sophia` chapters 25–26

The checked G. R. S. Mead translation witness contains a stronger stock/depletion structure than the supplied video alone:

```text
rulers possess power/light;
a receiver removes or carries power/light;
light is carried to a Treasury of the Light;
rulers become diminished, exhausted, or powerless when power ceases;
rulers consume their matter in order to delay exhaustion and the end of their rule.
```

This is mythical/theological language in an ancient text. The scientifically useful abstraction is not `light = Lineum energy`. It is the following mechanism template:

```text
stock
 -> gated or scheduled release/removal
 -> delivered quantity
 -> receiver/store
 -> source depletion
 -> possible recycling/consumption
 -> measurable exhaustion condition
 -> residual account
```

That template is directly useful because current Core sources, feedbacks, and sinks do not yet all have those roles represented.

### 15.3 Scientific value of this motif

A process should be called a **transfer** only if intervention can distinguish it from copying or independent injection.

Minimum transfer signature:

```text
source debit covaries with receiver credit;
blocking the channel prevents both effects;
receiver perturbation can alter the transfer or return path if reciprocity is claimed;
finite stock predicts exhaustion;
restoration predicts a corresponding return/debit elsewhere;
residual stays within the preregistered tolerance.
```

If the source remains unchanged while the receiver grows, the safer description is `feedback`, `copy`, `catalytic influence`, or `open injection` until a broader ledger is demonstrated.

## 16. Missing relationship versus missing state registry

The following alternatives are frozen before any new Core field is proposed.

### `M0` — current states are sufficient; current interpretation is not

`Psi`, `Phi`, `kappa`, and optional `mu` may already be sufficient state coordinates, while the error lies in calling one-way feedback a transfer or in using the wrong observables/ledger.

### `M1` — current states need reciprocal relationships

No new state is required, but one or more one-way writes require a physically motivated back-reaction or paired debit/credit.

### `M2` — finite source reservoir is missing

Introduce a research-only stock variable `S` in a toy model:

```text
source delivery debits S;
S predicts depletion/starvation;
recharge, if permitted, has an explicit incoming flux;
no source term may exceed available stock.
```

`S` is a bookkeeping/mechanism candidate, not a new fundamental Lineum field.

### `M3` — receiving/environment reservoir is missing

Introduce a research-only receiver `R` for quantities removed by dissipation, boundary export, or another sink. Test whether accounting closes and whether any return path is causal rather than fresh injection.

Again, `R` is not automatically a fundamental field.

### `M4` — supplied `kappa` must become stateful

Current `kappa` has high causal leverage but no back-reaction. Test a dynamic-scaffold class in which a `kappa`-like state has finite construction cost, can be damaged and repaired, changes in response to the interior, and has an explicit resource account.

### `M5` — explicit flux/conjugate state may be required

A spatial flux or conjugate state `J` may be considered only if current fields plus their short history cannot close local transport prediction and accounting. A variable introduced merely because gradients appear in an equation does not pass this gate.

### `M6` — explicit `mu` may be reducible history

The existing reduction-first `mu` programme remains binding. Before treating `mu` as an independent physical ingredient, test whether its predictive and intervention effects can be reconstructed from a sufficiently rich `Psi/Phi` history.

### `M7` — genuinely new state variable

A new state `X` is the last-resort model class, not the first explanation.

It earns consideration only if:

- current state fails held-out prediction;
- current state plus relevant short/long history also fails;
- explicit source and receiver reservoirs fail;
- reciprocal closure variants fail;
- dynamic-scaffold alternatives fail where relevant;
- the remaining residual is reproducible, localizable, interventionally identifiable, and not numerical;
- `X` makes a new held-out prediction with complexity penalty and independent verification.

No ancient name may be used as `X` merely to make the mapping feel complete.

### `DG0` — current equations may be effective rather than fundamental

This is a distinct later comparison class, not permission to invent an invisible parent universe.

The current `Psi/Phi/kappa/mu` update could in principle be an effective or coarse-grained description of a deeper local generative process. `DG0` becomes scientifically admissible only if it is operationalized by:

```text
a declared lower-level state or mechanism class;
a forward coarse-graining map from lower-level state to current Lineum observables;
a derivation or independently frozen approximation showing how the effective update emerges;
a new held-out prediction, scaling law, conservation/balance relation, or intervention response;
a complexity penalty against same-layer M0-M6 alternatives;
numerical refinement and boundary controls;
independent reproduction.
```

Failure of same-layer accounting by itself does not support `DG0`. A deeper model that can fit any residual after the fact is unfalsifiable and must be rejected. Conversely, previous passive-boundary, copying, source-accounting, and local-`mu` negatives do **not** by themselves reject `DG0`, because they tested different mechanism classes.

`DG0` must remain separate from metaphysical language such as Pleroma, higher worlds, creator layers, or souls. Ancient motifs can suggest the question `effective local description versus larger causal closure`; they cannot supply evidence that such a deeper physical layer exists.

## 17. Field-Accounting Closure preregistration

The new immediate programme is `FAC` — **Field-Accounting Closure**. It is research-only and does not alter production Core.

### `FAC0` — directed coupling/intervention graph

**Question:** Does the source-level coupling graph match the observed one-step causal response graph?

Freeze a deterministic, cap-free, PML-free, finite synthetic state away from clipping and divergence. For each available state/input separately:

```text
perturb Psi only;
perturb Phi only;
perturb mu only when enabled;
perturb kappa only as an input comparison;
perturb delta only as an input comparison;
repeat with stochastic source disabled.
```

Record next-step responses in every returned state.

Primary purpose: detect hidden or misunderstood directed edges, ordering effects, and state variables that are only supplied inputs.

A source inspection prediction must be frozen before execution. Unexpected edges must be investigated, not post-hoc relabeled.

#### FAC0 source-inspection prediction

The prediction frozen before numerical evaluation was:

```text
Psi perturbation:
    direct Psi response;
    later Phi response through mode coupling;
    later mu response through the Psi-activity write;
    no kappa response;

Phi perturbation:
    direct Phi persistence/diffusion;
    direct Psi response through interaction and gradient drift;
    possible later mu response through the already changed Psi;
    no kappa response;

mu perturbation:
    direct mu persistence/decay;
    direct Psi response through the Phi-to-Psi multiplier;
    possible later Phi response through mode coupling of the changed Psi;
    no kappa response;

kappa perturbation:
    supplied kappa changes directly;
    Psi, Phi, and mu can all respond because kappa modulates their update terms;
    no back-reaction from those states alters kappa during the step;

delta perturbation with stochastic source disabled:
    no returned-state response, because delta enters only the source-probability gradient;

delta perturbation with stochastic source enabled and matched RNG:
    event-sensitive Psi response is possible when the changed probability crosses sampled linon thresholds.
```

#### FAC0 frozen synthetic state and configuration

A `10 x 10` deterministic synthetic state was used with coordinates `X,Y` spanning `[-1,1]`:

```text
Psi = (0.25 + 0.04 cos(pi X) cos(pi Y)) * exp(i (0.3 X - 0.2 Y))
Phi = 0.35 + 0.06 X + 0.04 Y + 0.015 cos(2 pi X)
kappa = 0.8 + 0.03 cos(pi X) sin(pi Y)
mu = 0.12 + 0.02 sin(pi X) cos(pi Y)
delta = 0.01 sin(2 pi X) sin(pi Y)
```

The deterministic FAC0 configuration was:

```text
dt = 0.1
psi_diffusion = 0.05
phi_diffusion = 0.05
drift_strength = -0.004
stencil_type = LAP4
physics_mode_psi = diffusion
disable_quantum_noise = true
phi_diffusion_scales_with_dt = true
use_mode_coupling = true
mode_coupling_strength = 0.001
use_mu = true
mu_eta = 0.005
mu_rho = 0.0001
mu_cap = 10
mu_peak_cutoff_ratio = 0.1
psi_amp_cap = 1e6
grad_cap = 1e6
phi_cap = 1e6
PML absent from the NumPy diffusion path and disabled as a confounder
```

The perturbation shapes were smooth localized functions. The primary reported run used amplitude `epsilon = 1e-4`. A separate linearity check used `5e-7`, `1e-6`, and `2e-6`.

#### FAC0 provisional standalone response matrix

The following `L2` differences were measured against the unperturbed one-step output at `epsilon = 1e-4`:

| Perturbed input | `Psi` response | `Phi` response | `mu` response | `kappa` response |
|---|---:|---:|---:|---:|
| `Psi` | `2.3699093963216352e-4` | `9.732383221228434e-9` | `5.4495019740789646e-8` | `0` |
| `Phi` | `2.6856982691506603e-7` | `2.8196465398990173e-4` | `6.351447894468394e-11` | `0` |
| `mu` | `8.266873915932191e-8` | `3.591654451425749e-12` | `2.8198291875753225e-4` | `0` |
| `kappa` | `1.2138729321585137e-7` | `3.2017833061649787e-9` | `1.1492058791208562e-8` | `3.255386789889278e-4` |
| `delta`, source disabled | `0` | `0` | `0` | `0` |

The response graph matches the source-inspection prediction. In particular:

- `Phi -> mu` appears within one complete step only indirectly through `Phi -> Psi -> mu`;
- `mu -> Phi` appears within one complete step only indirectly through `mu -> Psi -> mode-coupling -> Phi`;
- `kappa` reaches all dynamic outputs while nothing writes back to `kappa`;
- `delta` is inert when its only active path, stochastic/linon generation, is disabled.

#### FAC0 small-perturbation scaling check

For perturbation amplitudes `5e-7`, `1e-6`, and `2e-6`, the output response divided by `epsilon` remained stable at the reported precision. Representative slopes were:

```text
Psi input -> Psi:   approximately 2.3699093965
Psi input -> Phi:   approximately 9.73146e-5
Psi input -> mu:    approximately 5.44898e-4

Phi input -> Psi:   approximately 2.6857066e-3
Phi input -> Phi:   approximately 2.81964654
Phi input -> mu:    approximately 6.3515e-7

mu input -> Psi:    approximately 8.2668836e-4
mu input -> Phi:    approximately 3.59e-8
mu input -> mu:     approximately 2.81982919

kappa input -> Psi: approximately 1.2138725e-3
kappa input -> Phi: approximately 3.20173e-5
kappa input -> mu:  approximately 1.1492057e-4
kappa input -> kappa: approximately 3.25538679
```

This supports a local directed-response interpretation rather than a threshold artifact for the deterministic lanes.

#### FAC0 stochastic `delta` check

With the stochastic source re-enabled, baseline and perturbed runs were paired with the same RNG seed. Across `20` seeds:

| `delta` perturbation amplitude | seeds with changed `Psi` | maximum `Psi` difference | mean `Psi` difference |
|---:|---:|---:|---:|
| `0.01` | `1/20` | `0.00381917` | `0.000190958` |
| `0.05` | `8/20` | `0.00467209` | `0.00119379` |
| `0.2` | `20/20` | `0.00474539` | `0.00350253` |
| `0.5` | `20/20` | `0.00679585` | `0.00536665` |

This is consistent with `delta` changing a stochastic event probability rather than acting as a returned dynamical state. The nonlinearity in event counts is expected from thresholded random draws and is not evidence of a new field.

#### FAC0 independence and environment receipt

The numerical checker was separately transcribed from the audited NumPy update rather than importing `step_core`. Two local implementations, one forcing explicit input copies and one following the production-style `np.asarray` mutation semantics on a deep-copied caller state, produced identical baseline outputs for `Psi`, `Phi`, `mu`, and `kappa` to exact floating comparison in the local run.

However, this is **not** a repository-supported reproduction. Environment audit found:

```text
local Python = 3.13.5
local NumPy = 2.3.5
repository requirement = numpy>=1.24,<2.0.0
```

A clean virtual environment was created outside the repository. Installing `numpy>=1.24,<2.0.0` failed because the available package index exposed no compatible build for that Python environment. A direct `git clone --branch develop` into the disposable workspace also failed because the local execution environment could not resolve GitHub.

A renewed disposable local checkout attempt on 2026-08-07 again failed at GitHub name resolution before checkout. This repeated failure is retained only as an execution receipt. It adds no scientific evidence for or against any Lineum mechanism.

Classification:

```text
FAC0_source_graph_from_current_source = supported
FAC0_same_step_indirect_edges_from_update_order = supported
FAC0_standalone_numeric_corroboration = provisional_support
FAC0_repository_supported_runtime_reproduction = blocked_by_environment
FAC0_physical_energy_claim = not_established
FAC0_new_field_evidence = none
```

This environment limitation is a technical execution blocker, not a scientific negative result. It does not open the owner-intuition failure gate.

### `FAC1` — term-isolated paired-transfer audit

Use exact update ordering and compare:

```text
mode-coupling paired debit/credit      positive implementation control;
fallback Psi-to-Phi reaction           expected unpaired write control;
Phi interaction -> Psi                 expected unpaired feedback control;
Phi-gradient drift -> Psi              expected unpaired feedback control;
Psi -> mu                               expected unpaired memory-write control;
mu modulation -> Psi                   expected unpaired feedback control.
```

For every step record, where separable without changing the map:

```text
state before term;
state after term;
local debit candidate;
local credit candidate;
global debit/credit sums;
spatial flux where defined;
residual.
```

No quantity is called physical energy merely because the residual is small.

FAC1 remains gated until FAC0 is replayed in a repository-supported dependency environment or an explicitly justified equivalent verification environment. The provisional standalone FAC0 corroboration is not promoted across that gate.

### `FAC2` — open source and sink bookkeeping

Add diagnostic bookkeeping buckets outside the physical state for:

```text
stochastic/linon injection;
linear Psi dissipation;
PML export;
cap/reset deletion;
Phi cap/fold effects;
mu decay.
```

These diagnostic buckets must not feed back into the dynamics.

Question: can the existing implementation be described by a closed **software accounting identity** when all explicit injections, removals, and boundary exports are recorded?

A closed software identity is useful but is not yet a physical energy law.

### `FAC3` — reciprocal closure versus finite reservoirs

For each decision-relevant one-way edge, compare known-answer toy classes:

```text
A one-way baseline;
B explicit reciprocal back-reaction;
C finite source stock with debit;
D receiving store with reversible return;
E matched damping/injection null;
F hidden external pump matched on the primary observable.
```

Measure boundedness, source exhaustion, receiver growth, return after intervention, residual, and held-out response.

### `FAC4` — static versus dynamic scaffold

Compare:

```text
static supplied kappa;
state-responsive kappa-like scaffold with explicit construction cost;
finite-capacity receiving boundary;
externally pumped stabilizing boundary;
no-scaffold null.
```

A dynamic scaffold is supported only if it adds held-out causal capability that cannot be reproduced by the static mask or hidden pump while preserving the declared ledger.

### `FAC5` — new-state necessity test

Fit or construct increasingly rich model classes on training interventions and freeze them before held-out evaluation:

```text
N0 current instantaneous state;
N1 current state + short history;
N2 current state + optimized finite history embedding;
N3 N2 + explicit source/receiver accounting states;
N4 N3 + dynamic-scaffold state where applicable;
N5 N4 + one candidate additional state X.
```

Require complexity-aware held-out predictive improvement and a distinct intervention response.

Decision rule:

```text
new_state_required
    only if
N0..N4 fail reproducibly
and N5 succeeds out of sample
and X is independently identifiable.
```

If N1 or N2 succeeds, the apparent missing field was history. If N3 succeeds, the apparent missing field was bookkeeping/resource state. If N4 succeeds, it was boundary/scaffold dynamics. Only N5 supports a genuinely additional state coordinate.

## 18. Relation to the earlier known-answer programme

The prior fixtures remain valid. The immediate ordering changes to maximize information about the owner's current question:

### Stage A — implementation and accounting closure

1. `FAC0` directed coupling/intervention graph — source graph supported; exact supported-runtime replay still required.
2. `FAC1` paired versus unpaired current writes.
3. `FAC2` software source/sink accounting.

### Stage B — cheapest missing-mechanism classes

4. `FAC3` reciprocal closure and finite reservoirs.
5. `FAC4` dynamic scaffold.
6. `FAC5` new-state necessity.
7. `DG0` effective-equation/deeper-generative comparison only if it can be frozen as a distinct predictive model and not as a post-hoc hidden layer.

### Stage C — preserved observer/copying programme

8. `IC1` projection-copy versus causal-state continuation.
9. `TS1` binary-output mechanism discrimination.
10. `EC1` internal periodicity versus external calibration.
11. `DB1` active boundary.
12. `PI1` protocol identity.
13. `PH1` preparation-history equivalence failure.

This is a reprioritization, not deletion. `IC1` remains preregistered and should resume after the more basic state/accounting question is resolved.

## 19. Root-programme impact matrix

| Root branch or fact | Relation | Current impact |
|---|---|---|
| coherent software pump and open source ledger | `supports` | FAC2/FAC3 directly test stock, injection, receiver, and residual classes |
| `Phi` and `mu` do not currently close source-energy accounting | `supports` | blocks physical transfer language and motivates M0–M3 |
| supplied non-evolving `kappa` | `reopens` | FAC0 confirms high one-step causal reach with no back-reaction; FAC4 tests dynamic scaffold only as a comparison class |
| no passive reversible current-field membrane | `constrains` | exact failed candidates remain negative; only distinct active/stateful classes are reopened |
| exact live-state continuation | `supports` | IC1 and FAC5 distinguish complete state from projection/history omissions |
| static recipe not donor identity | `supports` | image/copy distinction remains active |
| copying/heredity negative results | `unaffected` | no ancient motif or accounting closure creates descendants retroactively |
| `mu` reduction-first programme | `constrains` | FAC0 shows `mu` has same-step indirect consequences but does not establish independent ontology; M6 remains mandatory |
| current public-TOLOG Q2 accounting negative | `supports` | apparent `Psi` recovery without `Phi` debit is a live example of why component recovery is not transfer |
| possible effective/deeper generative description | `open_but_unprivileged` | DG0 may compete only after an explicit lower-level model, coarse-graining map, and held-out discriminator exist |
| physical particle/gravity/quantum/soul/cosmology mappings | `unaffected` | no textual motif or internal ledger establishes physical correspondence |

## 20. Failure classification

Every negative result must be assigned to one or more of:

```text
source-text attribution failure;
media synthesis mistaken for primary witness;
observer non-identification;
mechanism not distinguishable under selected interventions;
invalid synthetic state;
insufficient hidden-state contrast;
ledger definition failure;
untracked source or sink;
finite-horizon false equivalence;
calibration target ambiguity;
boundary artifact;
parameter regime;
numerical implementation;
state-history omission;
model-class insufficiency;
interpretation overreach.
```

A failed observer or accounting candidate blocks that candidate. It does not prove a new field.

The FAC0 dependency mismatch and repeated GitHub DNS failure are classified separately as `execution_environment_not_repository_supported`; they are not model failures.

## 21. Frozen anti-overinterpretation rules

The following remain prohibited:

```text
Pleroma = hidden physical dimension;
Yaldabaoth = a physical field or conscious simulator;
archons = physical particles or field components;
Horos = proven membrane;
syzygy = mandatory paired fundamental fields;
spirit entering Adam = mu entering Psi;
light/power in an ancient text = physical energy;
Pistis Sophia Treasury of Light = Lineum energy reservoir;
Two Spirits = two fundamental fields;
364-day calendar = Lineum constant;
living temple architecture = conscious boundary;
ancient structural analogy = empirical evidence;
software ledger closure = physical energy conservation;
new state variable = new substance;
missing reciprocal debit = proof of a missing field;
FAC0 directed response = proof of physical energy transfer;
same-step indirect edge = independent fundamental coupling;
failed same-layer model = proof of a deeper universe layer;
effective-equation language = license for an unfalsifiable hidden mechanism.
```

## 22. Evidence classification at version 0.3.1

### 22.1 What the current implementation computes

Supported from current source inspection:

- dynamic `Psi` and `Phi`;
- supplied `kappa` with no update/back-reaction inside `step_core`;
- optional dynamic `mu` written from `Psi` activity and feeding back as a multiplier;
- optional supplied `delta` entering source-probability gradients;
- stochastic/source injection into `Psi`;
- one explicit paired mode-coupling debit/credit between a `|Psi|^2` quantity and `Phi`;
- several one-way writes and sinks without explicit receiving/source state;
- sequential update ordering that permits indirect one-step paths such as `Phi -> Psi -> mu` and `mu -> Psi -> Phi`.

### 22.2 What was reproducibly observed

No repository-supported new Core numerical experiment was completed in this version.

The FAC0 standalone checker provisionally corroborated the source-level directed graph, same-step ordering effects, small-perturbation linear scaling for deterministic lanes, and stochastic-only `delta` sensitivity under matched RNG. It cannot be promoted to a supported Core reproduction because the local environment used NumPy 2.3.5 while the repository requires NumPy below 2.0 and a compatible clean environment could not be constructed from the available package index.

The repeated local checkout failure on 2026-08-07 occurred before repository execution because `github.com` could not be resolved. It is an execution-environment receipt only.

Inherited verified results remain binding, including:

- open source-energy account;
- failed tested passive membrane classes;
- exact live-state transplant continuation;
- negative tested copying/heredity lanes;
- current public-TOLOG Q2 evidence that apparent `Psi` recovery can occur without a corresponding `Phi` decrease under the tested implementation.

### 22.3 Independent check

FAC0 used two separately arranged local NumPy transcriptions with different input-copy semantics. Their baseline outputs agreed exactly in the available environment. Source inspection independently predicts the same directed edges and explains the observed indirect edges from update order.

This is partial independence only. Both numerical transcriptions share the same manually reconstructed equations and the same unsupported NumPy runtime. A repository-supported replay or equivalently justified independent environment remains required.

### 22.4 Cautious interpretation

The current model is under-specified as a physical resource network. FAC0 strengthens confidence in the implementation-level dependency graph but provides no evidence that the state set is physically complete or incomplete. Missing relationships, reservoirs, dynamic boundary state, and history remain stronger and cheaper hypotheses than a missing fundamental field. An effective/deeper-generative description is a legitimate later scientific comparison class only when it is explicit enough to be falsified.

### 22.5 Hypotheses

`M0` through `M7`, `DG0`, and FAC1 through FAC5 remain preregistered research hypotheses/tests. FAC0 has partial evidence at the source-inspection level and provisional numerical corroboration; it has not passed the supported-runtime completion gate. `DG0` currently has no positive numerical evidence and is retained only as a later model class.

### 22.6 Known real physics

No correspondence between these ancient motifs and real physical fields has been established. Standard physical energy requires a well-defined model-specific conserved or balance-law quantity and empirical calibration; similar words in ancient literature do not supply that requirement. A software dependency graph is not a physical ontology. Effective theories and coarse-graining are real scientific concepts, but their existence in physics does not imply that current Lineum is an effective theory of any particular deeper physical substrate.

## 23. Current verdict

```text
ancient_texts_encode_lineum = unsupported
modern_video_is_primary_source = false
video_contains_source_grounded_motifs = true_with_source_specific_corrections
Athanasius_blanket_destroy_all_other_texts_quote = unsupported_in_checked_letter
Pistis_Sophia_contains_power_light_depletion_and_receiver_motifs = supported_as_textual_witness
those_motifs_are_physical_energy_accounting = unsupported

current_Core_fields_are_physically_complete = unproven
current_Core_full_runtime_has_demonstrated_closed_physical_resource_account = no
current_mode_coupling_has_explicit_paired_scalar_debit_credit = yes
physical_total_energy_function_defined_and_validated = no
Phi_to_Psi_feedback_has_matching_Phi_debit = no
Psi_to_mu_write_has_matching_Psi_debit = no
mu_feedback_has_matching_mu_debit = no
kappa_backreaction_is_implemented = no
explicit_finite_source_reservoir_is_implemented = no
explicit_receiving_sink_reservoir_is_implemented = no

FAC0_source_graph_from_current_source = supported
FAC0_same_step_indirect_edges_from_update_order = supported
FAC0_standalone_numeric_corroboration = provisional_support
FAC0_repository_supported_runtime_reproduction = blocked_by_environment
FAC0_new_field_evidence = none

new_fundamental_field_required = unproven
missing_relationship_or_resource_state = stronger_current_hypothesis_than_missing_field
history_as_missing_state = live_hypothesis
stateful_dynamic_scaffold = live_hypothesis
effective_or_deeper_generative_equation = live_but_unprivileged_hypothesis_with_no_positive_evidence

next_action = recover_supported_runtime_and_replay_FAC0_before_FAC1
IC1_status = preserved_and_queued_after_accounting_priority
```

## 24. Source register additions for version 0.3.1

The complete source register from version `0.1.0` remains preserved in Git blob `3ec1d893e4309cb2e06b97a2fc09d658f05ab149`. Version `0.2.0` remains preserved in Git blob `1691f44a88afd7414a32afc3625ef3acdb46fcf7`. Version `0.3.0` remains preserved in Git blob `f9e5cdf26a749baf9a2de4a735105830578e7a38`. The following sources and execution receipts are retained for this checkpoint.

### Primary / translation witnesses

- *The Secret Book of John / Apocryphon of John*, short version, translated by Michael Waldstein and Frederik Wisse, accessible witness: `https://www.gnosis.org/naghamm/apocjn-short.html`.
- *The Secret Book of John / Apocryphon of John*, Davies rendering, accessible witness used for locating power/light passages: `https://www.gnosis.org/naghamm/apocjn-davies.html`.
- *On the Origin of the World*, translated by Hans-Gebhard Bethge and Bentley Layton, accessible witness: `https://gnosis.org/naghamm/origin.html`.
- *Pistis Sophia*, G. R. S. Mead translation, chapter 25, accessible witness: `https://www.gnosis.org/library/pistis-sophia/ps029.htm`.
- *Pistis Sophia*, G. R. S. Mead translation, chapter 26, accessible witness: `https://sacred-texts.com/chr/ps/ps030.htm`.
- Athanasius, *Festal Letter 39*, accessible translation witness: `https://www.newadvent.org/fathers/2806039.htm`.

### Media intake

- Owner-supplied auto-generated Czech subtitles for YouTube video `aYhko3jlQFk`, reviewed only as a discovery/source-claim index. The copyrighted third-party transcript is not versioned in this repository.

### Current Core implementation

- `lineum_core/math.py`, blob `bb877021810691223a0eb960a45493a2e351112a`.
- `lineum_core/profiles.py`, blob `3a21be878bc61c7c8612c1040acf01c4d4869f90`.
- `requirements.txt`, blob `942f2b94b3d3f8c767451ae2d847a7b17c86d81e`, requiring `numpy>=1.24,<2.0.0`.
- `requirements-dev.txt`, blob `7a0907e3e6c2d15400d19b536227a509910ae7e9`.
- `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, blob `5304874451caf32313ad0e8e3c59e53958698d79`.
- Core branch snapshot before the v0.3.1 write: `eb976b97a233ac2c4d83eac53c290aab0d137e4e`.

### FAC0 local execution receipt

```text
execution role: provisional standalone corroboration only
Python: 3.13.5
NumPy: 2.3.5
repository NumPy contract: >=1.24,<2.0.0
clean-venv compatible NumPy install: failed, no compatible distribution exposed by available index
local git clone of develop: failed, github.com name resolution unavailable
repeat disposable checkout attempt on 2026-08-07: failed at github.com name resolution before checkout
production Core imported: no
manual equations: transcribed from current math.py blob bb877021810691223a0eb960a45493a2e351112a
```

The exact numerical outputs needed to challenge the directed-edge conclusion are embedded in Section 17. No hidden temporary artifact is required for the scientific interpretation retained here.

## 25. Next checkpoint gate

Before modifying a Core equation, adding a Core field, changing whitepaper ontology, naming any quantity physical energy, or starting FAC1:

1. use the exact current Core implementation, not a prose reconstruction;
2. obtain a repository-supported dependency environment or an explicitly justified equivalent verification environment;
3. replay the frozen FAC0 deterministic intervention matrix without changing its state, perturbation definitions, configuration, observables, or interpretation thresholds;
4. verify the direct and indirect edge classifications against current source SHA and record any discrepancy rather than tuning the fixture;
5. preserve the exact environment, commands, outputs, and comparison receipt in this report;
6. execute FAC1 only if FAC0's source-inspection graph survives that replay or after any discrepancy is resolved and re-preregistered;
7. do not introduce a physical field to repair an accounting residual until `M0` through `M6` alternatives have been tested sufficiently to justify `M7`;
8. do not promote `DG0` merely because a same-layer candidate fails; require an explicit lower-level model, coarse-graining map, and held-out discriminator first;
9. keep the ancient-source comparison and the physical inference separate at every checkpoint;
10. leave Core code and whitepapers unchanged until a promotion gate is independently passed.

## 26. Thread-independent research objective and resume checkpoint

### 26.1 Primary research objective

This active report is the authoritative resume point for the current programme. A future conversation must be able to continue from this file without reconstructing intent from chat history.

The scientific objective is:

> Identify which genuinely missing mechanism, state description, relationship, accounting component, observer information, boundary dynamics, or effective-generative layer is required to make the current Lineum model more causally complete, while preferring the smallest falsifiable change and refusing to promote analogy, fit quality, visual resemblance, or ancient terminology into physics.

The programme is **not** trying to prove that a missing piece exists. `No additional state is required` is an acceptable and important result.

### 26.2 Mandatory evidence separation

Every future checkpoint must explicitly distinguish:

```text
A. what the current implementation actually computes;
B. what was reproducibly observed in a supported or explicitly qualified execution;
C. what cautious interpretation follows from A and B;
D. what remains a hypothesis, analogy, or model class;
E. what is known from real physics/history and whether any empirical Lineum correspondence exists.
```

Negative results, broken metrics, execution blockers, failed hypotheses, null results, and conflicts between code, tests, reports, and whitepapers must remain visible.

### 26.3 Frozen candidate hierarchy

Do not jump directly to a new field. Test the following hierarchy in order unless new evidence justifies a documented re-ranking:

```text
H0 / M0:
    present state is sufficient; interpretation, observer, or ledger is wrong;

H1 / M1:
    present states need reciprocal/back-reaction relationships;

H2 / M2-M3:
    explicit finite source and/or receiving accounting states are missing;

H3 / M4:
    supplied kappa-like structure must become a stateful, finite-cost dynamic scaffold;

H4 / M6:
    apparent missing state is recoverable history of existing fields, including a reduction-first test of mu;

H5 / M5:
    an explicit flux/conjugate transport state is required after history fails;

H6 / M7:
    a genuinely additional independent state X is required;

H7 / DG0:
    the present equations are an effective/coarse-grained layer of a deeper generative model that makes additional falsifiable predictions.
```

`H7/DG0` is not automatically more fundamental or more likely than `H0-H6`. It is simply a distinct mechanism class that previous negative tests have not ruled out.

### 26.4 Immediate execution order

The current next step remains unchanged:

```text
1. recover a repository-supported or explicitly justified equivalent runtime;
2. replay the already frozen FAC0 matrix exactly;
3. if FAC0 survives, execute FAC1 term-isolated paired-versus-unpaired accounting;
4. execute FAC2 complete software source/sink bookkeeping;
5. execute FAC3 reciprocal closure versus finite source/receiver toy classes;
6. execute FAC4 static versus dynamic scaffold;
7. execute FAC5 held-out new-state necessity ladder;
8. only after an explicit DG0 model exists, compare it against the best same-layer survivor with the same held-out data and complexity discipline;
9. resume IC1, TS1, EC1, DB1, PI1, and PH1 after the more basic accounting/state question is resolved or when dependency logic makes one of them the cheaper discriminator.
```

The current technical blocker is the absence of a supported local repository execution path in the available environment. The repeated DNS failure is not a scientific result. Do not weaken FAC0 or silently substitute a prose reconstruction to make progress appear faster.

### 26.5 Ancient-text role in the missing-piece search

The ancient-text corpus remains a **hypothesis generator and anti-confounder source**, never evidence for Lineum physics.

The most useful currently retained abstractions are:

```text
Sophia / unpaired generation:
    compare one-way generation with reciprocal closure;

Pistis Sophia power/depletion/receiver motif:
    require stock, debit, receiver, exhaustion, and residual before calling a process transfer;

Yaldabaoth / local totality:
    test whether a local observer mistakes its accessible projection for complete causal state;

Gospel of Truth / ignorance and reconstruction:
    test whether history, relation, phase, or source knowledge removes an apparent missing substance;

Pleroma / fullness:
    seek the smallest state that closes prediction and accounting, not the largest hidden ontology;

pneuma / cohesion abstraction:
    test distributed restoring organization as an eigenmode/constitutive response rather than naming another field;

Horos / boundary motifs:
    distinguish inert separator, selective gate, receiver, stabilizer, active boundary, and hidden pump;

Two Spirits / binary appearances:
    distinguish two substances from bistability, attractors, history, thresholds, and observer labels;

protocol/covenant motifs:
    distinguish persistent shape from active reconstruction of invariant relations;

body/residual motifs:
    distinguish body, envelope, passive wake, causal residual, descendant, environmental relic, and observer artifact.
```

These abstractions may generate new comparison classes only when they produce a cheaper falsifier or a distinct held-out prediction.

### 26.6 Criteria for calling a missing piece identified

A candidate may be promoted from `hypothesis` to `supported missing mechanism/state` only if:

```text
it resolves a preregistered failure rather than a post-hoc aesthetic concern;
it beats relevant simpler alternatives on held-out interventions;
its effect survives timestep, grid, horizon, boundary, and observer controls where applicable;
its resource/accounting role is explicit if it changes an implementation-defined budget;
its causal role survives ablation and cannot be reproduced by a matched hidden pump or projection;
its parameters are not merely retuned per case;
independent verification reproduces the decision-relevant effect;
negative and null controls remain visible;
physical correspondence is kept separate until external empirical evidence exists.
```

A deeper/effective model additionally requires a reproducible forward map from its lower-level dynamics to the current effective variables. Merely fitting the current trajectories with more latent variables is insufficient.

### 26.7 Completion states

This research lane may legitimately end in any of the following outcomes:

```text
C0 current state sufficient; only interpretation/observer/accounting needed correction;
C1 reciprocal relationship required;
C2 explicit finite source/receiver accounting state required;
C3 dynamic scaffold/boundary state required;
C4 history of current fields sufficient;
C5 explicit flux/conjugate state required;
C6 genuinely additional state X required;
C7 deeper generative/effective-equation model required and independently discriminated;
C8 no tested candidate closes the gap; problem remains open with the rejection ledger preserved.
```

None of these outcomes may be renamed as proof of a soul, deity, multiverse, gravity theory, quantum interpretation, dark matter mechanism, or ancient encoded science without a separate evidential programme.

### 26.8 New-thread resume protocol

At the start of any future thread that continues this research:

1. fetch the current `develop` HEAD;
2. re-read all repository rule/workflow files required by `AGENTS.md`, including `research/foundations/AGENTS.md` if present at that future snapshot;
3. fetch this report in full and verify its current blob SHA/version;
4. fetch the root scientific report and continuity ledger referenced in this header;
5. verify the current runtime/profile source SHAs and re-audit them if they moved;
6. preserve all earlier negative results and open mechanism classes;
7. continue from `Section 25` and `Section 26.4` unless newer repository evidence has explicitly changed the ordering;
8. record every material decision, negative result, execution blocker, and completed checkpoint back into this same active report before ending the work session.

No chat prompt, hidden scratchpad, local uncommitted file, ZIP artifact, or remembered conversation should be required to reconstruct the scientific objective.

### 26.9 Current resume sentence

If this work is opened in a new conversation, the operational instruction is simply:

> Continue the active missing-piece research from this report under current repository rules. First obtain a supported replay of frozen FAC0; then proceed through FAC1-FAC5, keeping DG0 as an explicit but unprivileged later comparison class, and preserve all results in this report.
