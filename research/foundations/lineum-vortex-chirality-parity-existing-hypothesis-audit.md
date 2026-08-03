# Vortex Chirality, Parity, and Existing-Hypothesis Audit

**Status:** active retrieval and decision report; no new numerical experiment executed  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-03  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Branch head before this report:** `ac1cf829b4fc87e929ef73f6fbb9c921866df68c`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`  
**Recovered root version:** 0.4.14  
**Root evidence cutoff:** 2026-07-29  
**Root blob SHA:** `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, version 0.3.0, blob `5304874451caf32313ad0e8e3c59e53958698d79`  
**Immediate predecessor:** `research/foundations/lineum-synthetic-vortex-field-causal-observer.md`, version 0.2.0, blob `aff6a5362f06b7258fe64b2234426db05d974d37`  
**Full local lineage:** `lineum-continuous-source-cosmology-validation.md` -> `lineum-gnostic-enochic-dead-sea-scrolls-metaphor-audit.md` -> `lineum-pneuma-cohesion-observer-fixture.md` -> `lineum-pneuma-cohesion-observer-adversarial-audit.md` -> `lineum-autonomous-cohesion-causal-path-discriminator.md` -> `lineum-synthetic-vortex-field-causal-observer.md` -> this report  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`, workspace `90121717552`, list `901217864718`, status re-read as `to do`  
**Scope:** Retrieval and classification of existing Lineum material relevant to mirror identity, chirality, parity, spin, spinors, oriented winding, vector gauge fields, and continuous-path identity. No Core equation, implementation, public API, whitepaper, retained P2 package, or simulation parameter is changed.  
**Central question:** Does the Lineum repository family already contain a validated mechanism or usable method for deciding whether a vortex constellation and its mirror belong to the same identity sector?  
**Current confidence:** high that current Core contains no explicit spinor, vector gauge, or chirality state; high that historical spinor language is not current validated evidence; medium that signed charge-neighbour relations plus continuous worldlines are the smallest useful observer ingredients; unresolved whether a particular mirror pair is dynamically reachable without a frozen path experiment.

## 1. Answer first

The repository contains relevant ancestors, but it does not contain a validated solution to the current chirality problem.

Three different historical ideas must not be conflated:

```text
spin aura:
    an internal phase-circulation observable;
    not Standard-Model spin and not a chirality mechanism.

rotational parity sweeps:
    same-spin versus alternating-spin initial configurations tested inside a
    strongly supporting environment;
    the environment masked internal differences, so the result was not identifying.

historical spinor / WZW / Finkelstein-Rubinstein narrative:
    a speculative Eq-8 interpretation claiming an anchored vortex acquires a pi
    phase under a 2-pi rotation;
    the same historical branch later records "Spinor falsification" and authorizes
    a vector-gauge direction;
    this branch was not merged into current `develop` and its exact executable
    proof package was not recovered.
```

Current Core instead implements one complex scalar `psi`, real scalar `phi`, supplied real `kappa`, optional real local `mu`, and optional real `delta`. It does not implement a two-component spinor, a vector gauge connection, a branch label, a parity sector, an oriented charge-neighbour graph, or a chirality invariant.

Therefore the old spinor story must not be revived as the repair for the failed observer. The reusable parts are much smaller:

```text
integer phase winding;
charge-aware neighbourhood relations;
continuous worldlines;
causal intervention;
source and external-action accounting;
identity modulo translation and proper rotation.
```

The owner-proposed decision principle is retained: mirror identity should be decided by the existence or absence of a continuous internally generated path that preserves declared topology, continuity, and accounting, not by static image resemblance alone.

## 2. Triggering negative result

The predecessor experiment rendered a known six-vortex constellation into a complex scalar field and applied a field-only observer.

The following components passed:

```text
exact defect count and charge multiset;
plaquette-winding detection;
local causal cut discrimination;
continuous global-controller action ledger;
teleported-lookalike worldline rejection;
matched-count vortex-gas rejection;
timestep, resolution-comparison, and independent-implementation checks.
```

The following frozen relational gates failed:

```text
sub-grid translation precision;
intact-local absolute recovery threshold;
regenerated symmetry-equivalent snapshot threshold;
reflection discrimination;
charge-arrangement discrimination.
```

The frozen top-level outcome was:

```text
FAIL_RELATIONAL_DISCRIMINATION
```

The failure falsified the plaquette-centre plus unrestricted same-charge-permutation observer within the synthetic domain. It did not falsify local causal-path restoration or the broad possibility of a field observer.

## 3. Project-owner failure-gate response

The project owner asked for an out-of-the-box interpretation after the verified negative result and then authorized continuation.

The retained owner-level principle is:

> Do not decide whether a vortex configuration and its mirror are the same merely from two final pictures. Ask whether the original can become the mirror through its own continuous evolution without disintegrating, being reconstructed, changing the protected topology, or receiving external instructions.

The owner accepted continuation from this framing and asked whether the repository family already contains related work.

This statement is an owner intuition and decision constraint. It is not an implemented equation, a numerical observation, or a physical fact.

## 4. Agent formalization of the owner principle

Let `C` be an admissible configuration space and let `P` be the declared set of protected quantities and continuity conditions.

Two observed states `x0` and `x1` are path-equivalent only when there exists a continuous trajectory

```text
x : [0, 1] -> C
x(0) = x0
x(1) = x1
```

such that throughout the path:

```text
all protected topological charges remain admissible;
no prohibited birth, death, teleport, or relabeling event occurs;
worldline continuity remains declared and auditable;
the allowed local law generates the path;
external action remains within the declared autonomy class;
all source, work, and information accounts close.
```

Translation and proper rotation are pose symmetries and do not by themselves change identity.

Reflection is not automatically admitted or rejected. It is a separate component question:

```text
same orbit under translation and proper rotation:
    pose-equivalent.

connected by an admissible self-generated path:
    dynamically path-equivalent.

same static pattern but disconnected under the admissible law:
    same family or template, different dynamical sector.

newly generated matching endpoint with broken worldlines:
    same family or template, different continuing instance.
```

This formalization is a proposed observer principle. It has not yet passed a known-answer path test.

## 5. Current implementation audit

### 5.1 Active public Core

The active implementation reviewed at this checkpoint is:

```text
path: lineum_core/math.py
blob SHA: bb877021810691223a0eb960a45493a2e351112a
branch: develop
```

The active configuration and state use:

```text
psi   : complex scalar grid
phi   : real scalar grid
kappa : real supplied grid
mu    : optional real local slow state
delta : optional real external semantic perturbation
```

The implemented operations include scalar gradients, complex diffusion, local amplitude and phase handling, local `psi`/`phi` coupling, optional local `mu` write and feedback, noise, damping, and numerical guards.

What is absent from the active file:

```text
no two-component spinor state;
no Pauli or Dirac matrices;
no SU(2) connection;
no vector gauge potential;
no covariant derivative with a gauge field;
no Wess-Zumino or Berry-phase action;
no Finkelstein-Rubinstein constraint;
no chirality or handedness variable;
no mirror-sector classifier;
no signed relational vortex graph;
no continuous-path identity observer.
```

Implementation verdict:

```text
current_Core_is_scalar_coupled_field_model = true
current_Core_has_explicit_spinor = false
current_Core_has_vector_gauge_field = false
current_Core_has_chirality_state = false
current_Core_proves_mirror_identity = false
```

### 5.2 Current Core whitepaper

The current file reviewed is:

```text
path: whitepapers/1-core/01-core-lineum.md
blob SHA: edc63b0d150b3b616ff8a108ea47a4f89b6a6c37
branch: develop
```

It explicitly warns that physics terms such as spin are analogical unless tied to operational evidence. It contains no current spinor section and no explicit chirality mechanism.

It does preserve an older environment-supported composite experiment described as a sweep over internal phase offsets and rotational parity. In that setup, the supporting environment dominated survival and no difference was observed across the tested initial alignments. The same section acknowledges that the environment could mask internal compatibility differences.

This result cannot answer the current question because:

```text
survival under a strong common environment is not mirror reachability;
same-versus-alternating spin initialization is not geometric chirality;
absence of a survival difference is not parity equivalence;
masked differences are not evidence that no intrinsic distinction exists.
```

Current-canon verdict:

```text
spinor mechanism = absent
chirality mechanism = absent
rotational-parity survival result = non-identifying for current question
```

## 6. Historical Lineum Core audit

### 6.1 Historical task inventory

A historical `todo.md` at main commit `8c4ff12af79b218fce8938497f56f75c4567195e`, blob `5000ab402aa54cc72336c339616e416270c94398`, defines `spin aura` as a time- or ensemble-averaged phase-circulation map such as `curl(grad(arg(psi)))` around localized excitations. The text explicitly requires that it not be presented as Standard-Model particle spin.

Classification:

```text
role = phase-circulation observable
useful_for = local winding and orientation diagnostics
not_sufficient_for = chirality, spinor identity, fermionic statistics, mirror sectors
status = historical backlog / terminology evidence, not active task authority
```

The same historical inventory describes composite configurations tested with relative phase offsets and identical versus alternating rotational parity under environmental support. It reports no survival distinction within that supported setup and warns about environmental masking.

Classification:

```text
role = historical initial-condition sweep
positive evidence = supported composites survived tested horizon
negative / ambiguous evidence = internal parity differences were not identified
confounder = common environment dominated or masked the tested difference
use_for_current_observer = adversarial control design only
```

### 6.2 Closed unmerged development branch

Closed pull request `#3`, titled `dev`, records 232 commits from main commit `8c4ff12af79b218fce8938497f56f75c4567195e` to head `d15e60d26e181aed39a55ab60e1ea413dba5904d`. It was closed without merge.

Its recorded commit-message list includes:

```text
Docs: Conclude Track C topology (Spinor falsification) and authorize Track D (Vector Gauge Field)
```

This is strong provenance that the project itself later classified the spinor branch as falsified and moved to a distinct vector-gauge hypothesis. It is not by itself a reproduction receipt.

The recoverable PR patch also contains historical text that had claimed, among other things:

```text
an Eq-8 vortex anchored to a mu-layer carries a Wess-Zumino boundary term;
a 2-pi rotation produces a pi Berry phase;
a Pauli spinor doublet follows;
a three-dimensional vortex is anchored to a four-dimensional bulk;
several consequences were labelled analytically proven.
```

The same patch listed essential quantities as pending proof, including the rotor moment of inertia and separation of collective modes.

Evidence classification:

```text
historical narrative exists = supported
current implementation contains that mechanism = contradicted
complete analytic derivation recovered = no
complete executable test recovered = no
independent verifier recovered = no
branch merged into current develop = no
later in-project spinor falsification label exists = supported by PR history
physical spin-1/2 correspondence = unsupported
```

The old claims must therefore be treated as a historical speculative branch with unresolved and later negative provenance, not as a dormant validated solution waiting to be re-enabled.

### 6.3 Vector-gauge successor

The historical PR record says Track D, a vector gauge field, was authorized after spinor falsification. The current audit did not recover a complete Track D equation, runner, test, threshold set, output, or independent verification package.

No vector gauge state is present in current `lineum_core/math.py`.

Classification:

```text
historical authorization = recovered
current implementation = absent
numerical evidence package = not located
current status = partial_provenance_only
reuse authorization = none
```

A future vector-gauge hypothesis may be considered only as a separate explicit variant after retrieval or fresh preregistration. It must not be inferred from the phrase "Track D".

## 7. Cross-repository audit

### 7.1 Lineum Dynamics

The public Core relocation notice identifies a private Lineum Dynamics repository as the operational Codex source. The repository was not available through the installed GitHub connection at this checkpoint, and direct candidate fetches returned no accessible file.

Classification:

```text
repository status = inaccessible in current connector
chirality / parity content = not_yet_compared
scientific consequence = none may be inferred
```

This does not block the public Core audit because the present work modifies no operated service, access policy, or private product layer. It does prevent an exhaustive claim that no private Dynamics note exists.

### 7.2 OEA

The accessible OEA repository returned no commit-history matches for `chirality`, `spinor`, or `vortex`. The only `parity` match was a texture-processing and deletion-test commit whose `force-mirror` language referred to image tiling and generated PBR assets, not field topology or physical parity.

Classification:

```text
relevant scientific mechanism located = no
visual mirror utilities = unrelated
OEA contribution to current observer = none identified
```

### 7.3 Lina EI repository alias

The accessible Lina EI repository alias `TomasTriska88/osobni-pamet` returned no commit-history matches for `chirality`, `parity`, `spinor`, or `orientation` in the available search path.

Classification:

```text
relevant scientific mechanism located = no
identity-product semantics = not evidence for vortex identity
Lina EI contribution to current observer = none identified
```

Search-index absence is not proof of universal repository absence. No positive relevant artifact was located.

## 8. Conflict and evidence matrix

| Material | What it says | Evidence class | Current authority | Effect on current decision |
|---|---|---|---|---|
| active `lineum_core/math.py` | scalar `psi/phi/kappa/mu/delta` dynamics | implementation | high | no implemented spinor, vector gauge, or chirality state |
| active Core whitepaper | spin language is analogical; supported parity sweep was masked | current documentation with internal conflicts | medium-low for science without receipts | does not identify mirror sectors |
| historical `spin aura` task | phase circulation around localized excitations | historical observer proposal | low-to-medium | winding is reusable; spin interpretation is not |
| historical supported parity sweep | no survival difference under common support | historical observation / prose receipt | low-to-medium | environment masking becomes an adversarial control |
| historical Eq-8 spinor narrative | WZW, Berry phase, SU(2), anchored vortex | speculative historical interpretation | low | prohibited as current repair |
| PR history `Spinor falsification` | project moved away from Track C | historical decision provenance | medium | spinor revival requires new evidence, not memory |
| PR history `Vector Gauge Field` | Track D authorized | partial hypothesis provenance | low | keep as unresolved variant only |
| current synthetic observer | mirror and charge arrangement not identified | preregistered reproducible negative result | high within toy domain | requires a better relational/path observer |
| owner path principle | identity depends on admissible continuous self-path | owner intuition / design constraint | binding for next design, not evidence | motivates path-component discriminator |

## 9. Reopenable variant ledger

### V0: Reflection-equivalent null

```text
claim:
    mirror configurations are equivalent when charge multiset, unsigned geometry,
    and all other retained observables agree.

required evidence:
    no intrinsic orientation observable and an admissible continuous path between
    mirror endpoints under the local law.

current status:
    open; not supported by the failed static mirror control alone.
```

### V1: Static signed-chirality observer

```text
claim:
    a signed relational invariant separates left- and right-handed vortex patterns.

candidate observables:
    oriented charge triples;
    signed areas tied to charge order;
    charge-aware cyclic neighbourhood graphs;
    local phase-gradient orientation around labelled worldlines.

risk:
    a static sign can classify photographs while saying nothing about dynamical
    reachability or continuing identity.

current status:
    open as an observer component, not sufficient alone.
```

### V2: History-conditioned relational observer

```text
claim:
    continuous same-charge worldlines establish labels and neighbour relations,
    removing the unrestricted same-charge permutation confounder.

positive inherited evidence:
    the predecessor continuity observer rejected a teleported lookalike.

risk:
    nearest-neighbour tracking can switch labels during close encounters and may
    smuggle a sampling-dependent identity rule into the observer.

current status:
    supported as a required ingredient; needs collision and relabelling controls.
```

### V3: Dynamical path-component chirality

```text
claim:
    mirror sectors are distinct only when no admissible continuous internally
    generated path connects them while protected topology and accounting remain intact.

motivation:
    project-owner failure-gate response.

strength:
    distinguishes family resemblance, chirality sector, and continuing instance.

risk:
    finite search cannot prove global nonexistence of a path without analytic bounds;
    a failed optimizer is not a topological impossibility proof.

current status:
    selected as the governing question, not yet as a validated mechanism.
```

### V4: Historical spinor / WZW revival

```text
claim:
    vortex identity requires a spinor state or topological pi phase under 2-pi rotation.

current evidence:
    incomplete historical narrative, absent current implementation, later project
    provenance explicitly labels spinor falsification.

current status:
    deprecated historical variant; may reopen only with a complete equation,
    derivation, known-answer tests, independent verifier, and discriminating prediction.
```

### V5: Vector-gauge extension

```text
claim:
    an independent orientation connection or vector gauge field supplies the missing
    relational transport information.

current evidence:
    historical authorization phrase only; no recovered implementation or receipt.

current status:
    unresolved experimental extension; not selected.
```

### V6: Pure sub-grid measurement repair

```text
claim:
    better vortex-centre localization repairs the current observer without adding
    new topology or dynamics.

current evidence:
    refinement reduced translation error, supporting a quantization component.

limitation:
    reflection remained indistinguishable at both grids and charge scramble remained
    weak, so localization alone cannot solve the complete failure.

current status:
    necessary numerical repair, insufficient scientific repair.
```

## 10. Decision

The smallest evidence-preserving decision is:

```text
retain sub-grid localization as a separate numerical lane;
retain signed charge-neighbour structure as a separate static-observer lane;
retain worldlines as a continuity lane;
make admissible path connectivity the governing chirality question;
do not add a spinor, WZW term, Berry phase, extra dimension, or vector gauge field;
do not classify mirrors as same or different before a known-answer path test;
do not apply the revised observer to P2.
```

This choice follows emergence-first discipline. It asks whether already available topology, local dynamics, and history are sufficient before introducing a new field or ontology.

## 11. Required next discriminator

No numerical protocol is frozen in this version. Before execution, the next report revision must complete two separable audits.

### 11.1 Numerical localization lane

Question:

```text
Can a declared sub-grid estimator recover vortex centres with translation-equivariant
error low enough that identical latent geometry no longer depends materially on grid phase?
```

Required controls:

```text
known analytic single vortex at random sub-cell offsets;
opposite charges at controlled separation;
global-phase invariance;
translation and rotation equivariance;
grid refinement;
independent fit or interpolation implementation;
no latent-centre access by the tested estimator.
```

This lane must not change the chirality definition.

### 11.2 Chirality and path lane

Question:

```text
Can a deliberately chiral known-answer charge-labelled constellation be connected to
its mirror by the declared local law without prohibited topology change or external work?
```

Required construction principles:

```text
use a configuration proven chiral under charge-preserving automorphisms;
separate static signed invariants from dynamic reachability;
preserve translation and proper-rotation quotienting;
track worldlines through close approaches;
record every charge birth, death, exchange, collision, and reconnection;
include an explicitly achiral positive control;
include an externally mirrored endpoint control;
include a path that is known analytically to exist;
include a path known to require a prohibited event in the fixture;
never treat optimizer failure as proof of impossibility.
```

Before choosing equations or thresholds, the project must also perform the mandatory cross-disciplinary primary-source audit of configuration-space components, molecular or geometric chirality, topological defects, labelled-point braid constraints, and parity in scalar versus multi-component fields. External theory may constrain the fixture but cannot validate Lineum.

## 12. What is explicitly not authorized

```text
no P2 observer application;
no retained-P2 reconstruction;
no Core equation change;
no public-library module;
no spinor or vector-gauge implementation;
no whitepaper update;
no Standard-Model spin claim;
no fermion, particle, antiparticle, handedness, weak-interaction, or quantum claim;
no claim that a finite simulation proves global topological impossibility;
no claim that historical prose is a recovered experiment.
```

## 13. Root-programme impact matrix

| Root branch | Relation | Result |
|---|---|---|
| retained P2 recovery | `unaffected` | Exact package recovery remains mandatory before any P2 continuation or observer application. |
| P2 vortex-gas remnant | `constrains` | Static count and geometry remain insufficient for object assignment. |
| minimum-flux observer audit | `supports` | Observer non-identification again requires adversarial controls. |
| source accounting | `supports` | Path identity must retain external-work and regeneration ledgers. |
| causal-path point fixture | `supports` | Internal causal dependence remains a useful known-answer component. |
| synthetic vortex-field observer | `depends_on` | This report directly classifies its reflection and charge-arrangement failure. |
| deterministic transplant | `supports` | Endpoint equality does not establish continuing identity. |
| copying and heredity | `unaffected` | No copying mechanism or inherited content was tested. |
| `mu x kappa`, membrane, Eq-11.1, epsilon, Relic Foam | `not_yet_compared` | No mechanism from those lanes was used to repair chirality. |
| branch-relative `mu` | `unaffected` | History labels here are ordinary observed worldlines, not branch or quantum histories. |
| particle, life, soul, entanglement, cosmology | `unaffected` | No correspondence claim advances. |
| historical spinor branch | `constrains` | It is preserved as deprecated partial provenance, not revived. |

## 14. Retrieval limitations

```text
complete `.agent/rules.d/` directory enumeration was not available through the connector;
known binding supplements 48 and 49 were fetched directly;
Lineum Dynamics was inaccessible;
OEA and Lina EI lacked code-search indexing, so commit-history searches were used;
the exact commit SHA and complete file package for historical Track C / Track D were not recovered;
the closed PR was not merged and mixed hundreds of unrelated changes;
no historical simulation output or verifier for the spinor claims was recovered;
no local checkout or complete Git-history execution was available;
no new simulation was executed in this audit.
```

These limitations prohibit universal absence claims. They do not change the current implementation fact that no spinor, vector gauge field, or chirality state exists in active Core.

## 15. Reopen triggers

Reopen the historical spinor or vector-gauge variants only when at least one of the following is recovered:

```text
exact immutable commit and path;
complete equation and unit conventions;
standalone executable runner;
frozen controls and thresholds;
raw machine-readable output;
independent verifier;
explicit negative-result analysis;
a prediction not reproducible by the scalar-history alternatives.
```

Reopen mirror equivalence only when an admissible continuous path is produced or analytically established.

Reopen mirror-sector separation only when a signed static invariant and a dynamic path obstruction survive known-answer positives, achiral nulls, grid refinements, relabelling attacks, and source-accounting controls.

## 16. Current verdict

```text
existing_relevant_material = yes
validated_existing_chirality_solution = no
current_Core_spinor = absent
current_Core_vector_gauge = absent
historical_spinor_claims = deprecated_partial_provenance
historical_spinor_falsification_marker = recovered
historical_vector_gauge_authorization = partial_provenance_only
spin_aura_reuse = winding_observable_only
historical_rotational_parity_result = environment_masked_and_non_identifying
owner_path_principle = recorded
selected_governing_question = admissible_continuous_path_connectivity
selected_new_field = none
new_experiment = not_yet_preregistered
P2_application = prohibited
Core_change = none
whitepaper_change = none
next_action = primary_source_path_chirality_audit_then_separate_localization_and_path_preregistration
```
