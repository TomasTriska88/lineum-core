# Eq-11.1, Epsilon, and Relic-Foam Whitepaper Claim-Correction Map

**Status:** active editorial-evidence map; no whitepaper text changed  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-07-31  
**Scope:** Claim-by-claim classification of overstrong, contradictory, historical, implementation-conflicting, or potentially retainable wording in the Eq-11.1 equation history, epsilon thermodynamic-attractor extension, Relic Foam / Standard-Model extension, and quantum-foam hypothesis. This report prepares a later evidence-controlled whitepaper handoff. It is not itself a canonical correction and does not authorize edits.  
**Parent comparison:** `research/foundations/lineum-eq11-epsilon-relic-foam-provenance-comparison.md` version `0.1.0`, commit `33ae087a27913420e9fabe807db52bf52e32e69c`.  
**Current confidence:** high for internal contradiction and active-implementation classifications; medium for proposed replacement scope because historical executables remain unrecovered; no confidence claim for physical correspondence.

## 1. Answer first

The three source whitepapers contain valuable hypothesis history, but their strongest wording repeatedly outruns the evidence preserved in the repository.

The main editorial problems are:

1. candidate equations are described as validated or canonical without a recovered executable receipt;
2. finite-horizon metastability is described as indefinite or immortal;
3. amplitude return after a shock is described in language that can be mistaken for structural repair;
4. transient secondary emission is described as re-ignition even though no stable returned object was observed;
5. local node-count re-equilibration is described as self-healing without content or identity recovery;
6. locally circulating but net-dissipative dynamics are described as closed-energy conservation;
7. passive trajectory shaping is described as memory, gravity, intelligence, or computation;
8. speculative real-world mappings are stated as explanations rather than hypotheses;
9. current active-Core implementation facts are mixed with historical equation families that the code does not execute.

No sentence below is edited in its source whitepaper by this report. The map preserves the historical wording while defining the evidence-safe replacement class.

## 2. Source coordinates

| Source | Blob SHA | Main subject |
|---|---|---|
| `whitepapers/1-core/02-core-equation.md` | `64f8341551d5737a6eb4919030bbb85a4b50380c` | Eq-1 through Eq-11.1 history and later phase audits |
| `whitepapers/2-cosmology/extensions/05-cosmo-ext-thermodynamic-attractor.md` | `ce543721d92d64045b19625a78fc88ef70165df0` | epsilon environmental-cycle candidate |
| `whitepapers/2-cosmology/extensions/03-cosmo-ext-lineum-standard-model.md` | `2ee576141018173a8cc397a92ba5b066876b9d40` | particle metaphors, Relic Foam, interaction and transport claims |
| `whitepapers/2-cosmology/hypotheses/37-cosmo-hyp-quantum-foam-and-mu-emergence.md` | `e05759e8e3349cb69b7d19b709b1c89cbf97a886` | fractal quantum-foam and emergent-mu hypothesis |
| active implementation `lineum_core/math.py` | `bb877021810691223a0eb960a45493a2e351112a` | current public update law |

## 3. Classification vocabulary

Every mapped claim receives one primary editorial status.

| Status | Meaning |
|---|---|
| `implementation_fact_only` | directly supported by current source inspection, without physical interpretation |
| `bounded_negative_result` | supported only as a failure within explicit documented conditions |
| `historical_unreproduced_claim` | preserved in prose but lacking a complete executable reproduction chain |
| `hypothesis_only` | proposed interpretation or mechanism without sufficient numerical evidence |
| `internal_contradiction` | source document later records evidence incompatible with its earlier wording |
| `superseded_by_later_documented_result` | later section narrows or reverses the earlier local claim |
| `physical_analogy_only` | mathematical resemblance without demonstrated real-world mapping |
| `eligible_for_canonical_wording` | narrow statement that is consistent with active code and independently retained evidence |
| `blocked_pending_active_core_revalidation` | historical result may be meaningful but has not been compared with current implementation |

Proposed replacement wording is deliberately conservative. It is not final prose until the whitepaper edit gate is opened.

## 4. Equation-history claim map

### 4.1 Document-level status conflicts

| ID | Location / claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| EQ-DOC-01 | Header says `Canonical Source of Truth (Eq-1 through Eq-9)` while the document also says `Draft` and covers V1-V11.1 | multiple status systems appear simultaneously | `internal_contradiction` | use one document status; classify each equation independently |
| EQ-DOC-02 | Note says Version 7 is latest while metadata says V1-V11.1 | chronology is internally inconsistent | `internal_contradiction` | state that V7 is one historical/current presentation branch and V11.1 is a separate candidate history, or update after full implementation audit |
| EQ-DOC-03 | `linon` defined as a stable localized excitation | stability is embedded in the noun before the observer gate is passed | `hypothesis_only` | define `linon` as a historical operational label for a detected localized candidate; stability must be separately measured |

### 4.2 Eq-11 dimensional-invariance claims

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| EQ11-01 | comprehensive multiscale validation confirmed stability across `dx=0.01...50` | no complete executable receipt is recovered; immediately followed by catastrophic long-horizon failure | `historical_unreproduced_claim` + `internal_contradiction` | “Historical sweeps were reported, but their executable receipt is not recovered and later long-horizon testing reported divergence.” |
| EQ11-02 | local gradients remain cleanly bounded across all verified resolutions | universal language exceeds documented scope and receipt | `historical_unreproduced_claim` | preserve only the exact tested ranges after reproduction |
| EQ11-03 | Eq-11 is a justified strong candidate | candidate ranking is a historical decision, not evidence | `hypothesis_only` | retain as historical status at that date, followed immediately by the destructive-audit downgrade |
| EQ11-04 | catastrophic divergence after long horizon | later negative claim is explicit but not independently reproduced here | `historical_unreproduced_claim` with negative priority | preserve as documented destructive result; require receipt before canonical numerical claim |

### 4.3 Eq-11.1 amplitude and persistence claims

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| EQ111-01 | Hawking stabilization layer was validated to physically bound the universe | physical and universal wording exceeds a historical PDE test | `historical_unreproduced_claim` + `physical_analogy_only` | “The historical model introduced a `Phi^2` leakage term intended to bound amplitude.” |
| EQ111-02 | 50,000+ steps proved leakage alone suppresses singularities and lateral spread | missing runner and later contradictory reconstruction | `historical_unreproduced_claim` | state as an unreproduced historical result, not proof |
| EQ111-03 | 100,000-step persistence without mutation or structural decay | later phases report metastability, decay, boiling, and missing provenance | `superseded_by_later_documented_result` | remove present-tense validation; cite the later qualification |
| EQ111-04 | completely non-fragile and free of fine tuning | absolute claim conflicts with parameter frontiers and failure regimes | `internal_contradiction` | replace with exact tested cells if recovered; otherwise hypothesis history only |
| EQ111-05 | stable bounds for every positive `lambda` down to near zero | Phase 17-18 reports delayed far-field boiling at low leakage | `internal_contradiction` | separate local peak bounding from global far-field stability |
| EQ111-06 | topology is conserved and vortex survives indefinitely | reconstructed documented baseline decayed to a scalar puddle; original receipt missing | `superseded_by_later_documented_result` | “An early survivor claim is unreproduced; a later reconstruction decayed under tested conditions.” |
| EQ111-07 | pure evaporative decay no longer occurs on impact | later interaction and fragmentation sections report multiple decay and scatter outcomes | `internal_contradiction` | specify exact initializer, interaction, and horizon or remove general claim |
| EQ111-08 | oscillatory bound states exist indefinitely and robustly across a vast space | later long-horizon phases report secular drift and metastability | `superseded_by_later_documented_result` | use “historically reported long-lived prepared pair regimes; permanent binding not established.” |
| EQ111-09 | environmental flow physically validates wake locking | measured simulation correlation does not validate physical ontology | `physical_analogy_only` | retain as model-internal wake-like observable only |
| EQ111-10 | binding is strictly thermodynamic energy minimization | no complete energy functional or conservation account is recovered | `hypothesis_only` | “Dissipation metrics were reported to correlate with prepared alignment; causal energy-minimum interpretation remains unverified.” |
| EQ111-11 | spatial invariance is robust because defect density differs by <1.55% | exact receipt missing and observer validity is separately limited | `historical_unreproduced_claim` | report only as a historical metric pending observer and runner recovery |
| EQ111-12 | amplitude mask correctly segregates physical defects | `physical` overstates a numerical observer threshold | `implementation_fact_only` only after code recovery | “The documented observer excludes low-amplitude phase winding below its declared threshold.” |

### 4.4 Binding, reconstruction, and ontology claims

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| EQ-BIND-01 | practical local N=2 limit | useful bounded negative, but not universal | `bounded_negative_result` | retain “within the documented equation, initializer, and open-vacuum tests” |
| EQ-BIND-02 | path memory is mathematically incapable of binding | only tested implementation/conditions are ruled out | `bounded_negative_result` | replace `incapable` with `unsupported under tested path-memory coupling` |
| EQ-REC-01 | bounded regimes reconstruct topology from 10% sparse data | may be target-constrained and receipt is missing | `historical_unreproduced_claim` | require wrong-target, shuffled, and active-causality controls before using `reconstruction` |
| EQ-REC-02 | reconstruction is an artifact of external `kappa` constraints | the negative distinction is decision-relevant but not independently replayed | `historical_unreproduced_claim` | preserve as historical classification, not current canon |
| EQ-ONT-01 | local single-field closure is fundamentally impossible | report itself says it is not a universal mathematical impossibility | `bounded_negative_result` | “No tested local candidate in this registered Eq-11 family passed the declared gates.” |
| EQ-ONT-02 | `Phi` is firmly the autonomous buffering field | role assignment is hypothesis and conflicts with active-Core semantics | `hypothesis_only` | distinguish candidate role from current implementation |
| EQ-ONT-03 | solver audit proved failures are physical | simulation solver comparison cannot establish natural physics | `physical_analogy_only` | “The tested failure persisted under the alternative numerical integrator.” |

### 4.5 Provisional bounded-backbone and later phase claims

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| EQ-BB-01 | quintic saturation and biharmonic term were validated as the current audited backbone | this is a distinct equation family mixed into Eq-11.1 chronology | `historical_unreproduced_claim` | assign a separate variant ID and equation receipt; do not call it Eq-11.1 baseline |
| EQ-BB-02 | clamps are obsolete and cleared for removal | active Core still contains caps and resets | `internal_contradiction` + `implementation_fact_only` | current implementation facts take precedence; no removal claim until code/test promotion |
| EQ-BB-03 | absolute bounded stability confirmed | later phases still describe metastable carriers and transport limitations | `internal_contradiction` | use local observable and tested horizon only |
| EQ-P6-01 | Phase 6 canonical passed level-2 rigor | no permanent standalone receipt recovered | `historical_unreproduced_claim` | historical phase label only |
| EQ-P6-02 | exceptionally long-lived carrier | potentially retainable after reproduction | `blocked_pending_active_core_revalidation` | do not map to particle or memory |
| EQ-P7-01 | no simple finite-speed law confirmed | narrow negative is appropriately scoped | `bounded_negative_result` | eligible after reproduction with exact protocol |

## 5. Epsilon thermodynamic-attractor claim map

### 5.1 Document status and mechanism language

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| EPS-DOC-01 | Status: Canonical epsilon-Field Formulation | not active Core; runner not recovered | `internal_contradiction` | `Historical candidate formulation; reproduction pending` |
| EPS-DOC-02 | universe required an active closed limit cycle | necessity is asserted before exhaustive alternatives | `hypothesis_only` | “The historical branch proposed an explicit circulation field to address the documented open-growth failure.” |
| EPS-MECH-01 | true environmental potential field | `true` implies physical ontology | `physical_analogy_only` | “additional numerical environmental state `epsilon(x,y)`” |
| EPS-MECH-02 | active metabolic engine | biological metaphor can imply demonstrated metabolism | `physical_analogy_only` | “local intake/return feedback candidate” |
| EPS-MECH-03 | permanently prevents starvation | later terminal evaporation contradicts permanence | `superseded_by_later_documented_result` | remove `permanently`; state finite-horizon effect only |
| EPS-MECH-04 | closed energy | total composite mass is documented as decreasing | `internal_contradiction` | “locally recycling but net-dissipative candidate” unless a complete conserved ledger is recovered |

### 5.2 Stress, recovery, and robustness claims

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| EPS-TEST-01 | 25,000-step deep-horizon stability | cited runner missing | `historical_unreproduced_claim` | preserve reported horizon and amplitude only as prose history |
| EPS-TEST-02 | excess energy was perfectly bled back after shocks | `perfectly` is unsupported without residual and raw output | `historical_unreproduced_claim` | “The peak was reported to return toward its prior drift line.” |
| EPS-TEST-03 | topology did not shatter after `+15%` shocks | potentially useful but not spatial repair | `historical_unreproduced_claim` | label prepared-structure amplitude-shock response |
| EPS-TEST-04 | random initial coordinates prove seed independence | randomized coordinates are not arbitrary initial states; receipt missing | `historical_unreproduced_claim` | specify exact randomization and prepared topology |
| EPS-TEST-05 | timestep, stencil, and grid invariance | useful robustness categories, but receipt missing | `historical_unreproduced_claim` | restore only after exact replay |
| EPS-TEST-06 | epsilon feedback is necessary because static epsilon runs away | ablation is mechanism-specific, not universal necessity | `bounded_negative_result` | “Within the documented candidate, the static-stock ablation was reported to lose the bound.” |

### 5.3 Long-horizon and conclusion conflicts

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| EPS-LONG-01 | infinite temporal stability | explicitly falsified later in the same document | `superseded_by_later_documented_result` | preserve the falsification prominently |
| EPS-LONG-02 | 100,000-step evaporation to `0.098` | negative result is decision-relevant but unreproduced | `historical_unreproduced_claim` with negative priority | retain exact reported horizon and observable pending replay |
| EPS-LONG-03 | million-step plateau was thermal death | correctly narrows earlier attractor interpretation | `bounded_negative_result` after reproduction | distinguish uniform box saturation from localized structure |
| EPS-LONG-04 | no non-evaporating geometric particles exist | universal wording exceeds one equation family | `bounded_negative_result` | “No non-evaporating localized geometry was reported under the documented default family.” |
| EPS-CONC-01 | Particle-First programme unconditionally validated | conflicts with terminal evaporation, missing runner, and no active-Core implementation | `internal_contradiction` | remove; at most retain “historical prepared metastable carriers were reported.” |
| EPS-CONC-02 | conditional eternal attractors | conditional branch is not fully specified in a receipt | `historical_unreproduced_claim` | separate as a registered variant with exact condition and falsification test |

### 5.4 Repair and physical-mapping language

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| EPS-REP-01 | recovery after high-energy shocks | can be mistaken for rebuilding erased structure | `historical_unreproduced_claim` | explicitly say `amplitude-shock recovery; spatial regrowth untested` |
| EPS-PHY-01 | nuclear-like / Lennard-Jones interaction profile | resemblance is not particle or nuclear evidence | `physical_analogy_only` | describe measured distance-response shape only |
| EPS-PHY-02 | atom-like composites | ontology exceeds model evidence | `physical_analogy_only` | `prepared multi-defect composites` |
| EPS-PHY-03 | mass exchange with reservoir | mass is not physically calibrated and total account is incomplete | `hypothesis_only` | `model norm/capacity transfer` with explicit equation and units |

## 6. Relic Foam claim map

### 6.1 Early stability and material claims

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| FOAM-STAB-01 | 16-node foam is mathematically immortal | later aging reports 17 -> 14 -> 11 nodes | `superseded_by_later_documented_result` | “persisted through the tested `T=3000` horizon; later aging was reported.” |
| FOAM-STAB-02 | stable wake never fragments or consumes | later noise and multi-hit tests show failure/fatigue | `internal_contradiction` | state exact perturbation range and failure threshold only |
| FOAM-HEAL-01 | true self-healing metamaterial | node-count recovery does not prove identity/content repair | `historical_unreproduced_claim` | “local node-count re-equilibration after moderate `Phi` perturbation” |
| FOAM-HEAL-02 | healed the gap, restoring the 16-node topology | same count does not establish same topology | `historical_unreproduced_claim` | require phase, adjacency, lineage, and content comparison |
| FOAM-SCALE-01 | universal foam scaling | node count changes strongly with scale | `internal_contradiction` | “scale-dependent packing trend was reported” |
| FOAM-ATTR-01 | necessary attractor for decaying particles | only selected prepared parents and one grid family are documented | `historical_unreproduced_claim` | “common terminal class within the documented parent sweep” |
| FOAM-GROUND-01 | natural ground state | random-noise audit explicitly failed | `bounded_negative_result` | retain the failure: foam did not arise as the tested noise ground state |
| FOAM-ASH-01 | ashes of dead super-particles | useful metaphor but not ontology | `physical_analogy_only` | `post-collapse residual multi-node state` |

### 6.2 Re-ignition and repeated-use claims

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| FOAM-IGN-01 | re-ignitable reservoir | later qualification found only transient fragments | `superseded_by_later_documented_result` | “structured impact triggers transient secondary emission.” |
| FOAM-IGN-02 | fresh discrete matter injected back into the field | may imply creation and stable objects; no stock ledger | `hypothesis_only` | “existing residual field redistributed into transient detected nodes.” |
| FOAM-IGN-03 | universal secondary emission in 18/18 canonical impacts | exact runner missing | `historical_unreproduced_claim` | retain exact matrix as historical result pending reproduction |
| FOAM-IGN-04 | true re-ignition | explicitly falsified by no stable returned N=1 | `bounded_negative_result` | prominently state negative verdict |
| FOAM-IGN-05 | golden impact vector may extract a particle | untested rescue hypothesis | `hypothesis_only` | keep only in reopen ledger, not narrative conclusion |
| FOAM-FAT-01 | permanent immortal re-ignition substrate | explicitly falsified by declining emission and structural fatigue | `bounded_negative_result` | “repeated impacts spent the documented residual structure.” |
| FOAM-FAT-02 | stateful material | fatigue establishes history dependence but not symbolic memory | `historical_unreproduced_claim` | `history-dependent exhaustible response` |
| FOAM-FAT-03 | remembers prior collisions | anthropomorphic shorthand | `physical_analogy_only` | “later response depends on prior impact history.” |
| FOAM-FAT-04 | generates active matter | no stable reorganization or physical matter mapping | `hypothesis_only` | `releases transient topological detections under the historical observer` |

### 6.3 Environment, gravity, and stabilization claims

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| FOAM-ENV-01 | attractive deflection / lensing | model-internal trajectory curvature, not gravity | `historical_unreproduced_claim` + `physical_analogy_only` | “foam-present trajectory differed from vacuum control under documented conditions.” |
| FOAM-ENV-02 | high-speed environmental stabilization | potentially useful co-stabilization claim; runner missing | `historical_unreproduced_claim` | retain as a precise comparative survival claim pending replay |
| FOAM-ENV-03 | localized suck effect | informal causal label | `physical_analogy_only` | report center-of-mass acceleration difference only |
| FOAM-ENV-04 | macro-gravity wells | no physical gravity mapping | `physical_analogy_only` | `additive model-internal Phi-gradient landscape` |
| FOAM-ENV-05 | permanent additive macroscopic Phi well | foam ages and permanence is not established | `internal_contradiction` | `long-lived over the documented observation window` |
| FOAM-ENV-06 | co-stabilization waveguide | valid mechanism hypothesis if reproduced | `blocked_pending_active_core_revalidation` | require energy-matched, shuffled-foam, and Phi-only controls |
| FOAM-ENV-07 | immortal field-state maps | conflicts with aging and fatigue | `superseded_by_later_documented_result` | remove `immortal` |
| FOAM-ENV-08 | clean permanent orbital localization | explicitly negative | `bounded_negative_result` | retain as tested failure |

### 6.4 Memory, logic, and intelligence claims

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| FOAM-MEM-01 | physical read-write memory substrate | later state-driven memory-cell tests fail | `internal_contradiction` | `history-dependent passive spatial imprint` |
| FOAM-MEM-02 | mechanically solves historical memory | broad explanatory closure exceeds tested controls | `hypothesis_only` | one candidate explanation for trajectory bias |
| FOAM-MEM-03 | future particles read the trail | anthropomorphic | `physical_analogy_only` | `future trajectories respond to the residual Phi gradient` |
| FOAM-LOG-01 | programmable analog circuitry | arranged geometry can shape transport, but computation language overreaches | `physical_analogy_only` | `passive geometry-dependent transport filter` |
| FOAM-LOG-02 | state-driven memory cell | explicitly failed | `bounded_negative_result` | retain failure |
| FOAM-LOG-03 | easily Turing-complete foam logic | explicitly falsified under documented conditions | `bounded_negative_result` | retain scope; do not claim universal impossibility |
| FOAM-AI-01 | emergent AI / adaptive routing | later sections correctly reclassify as passive filtering | `superseded_by_later_documented_result` | preserve only as historical misinterpretation |
| FOAM-AI-02 | no intelligence, decisions, or adaptive learning under tested canonical parameters | appropriately narrow if tied to documented mechanism | `bounded_negative_result` | eligible after reproduction; avoid universal claims about all Lineum variants |

### 6.5 Final system-classification conflicts

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| FOAM-SYS-01 | engine natively supports resilient high-speed Triads | conflicts with other documents and current implementation mismatch | `historical_unreproduced_claim` | identify exact historical equation variant and receipt |
| FOAM-SYS-02 | every structure decays into Relic Foam | universal wording exceeds selected parent tests | `historical_unreproduced_claim` | “the documented selected parent sweep produced residual foam states.” |
| FOAM-SYS-03 | framework is non-stateful | multi-hit fatigue is history-dependent; the intended meaning is no reliable logic bit | `internal_contradiction` | distinguish physical state dependence from usable discrete memory |
| FOAM-SYS-04 | non-Turing-complete | cannot prove universal computational impossibility from one tested architecture | `bounded_negative_result` | “the documented foam routing architecture did not implement the tested state-machine primitives.” |
| FOAM-SYS-05 | waves survive indefinitely under shielding | `indefinitely` exceeds finite horizon and foam aging | `historical_unreproduced_claim` | use exact tested horizon |

## 7. Quantum-foam and emergent-mu claim map

| ID | Claim fragment | Problem | Classification | Proposed evidence-safe handling |
|---|---|---|---|---|
| QF-MU-01 | mass `mu` does not mathematically exist as a fundamental input field | active Core explicitly reads and can evolve `mu` | `internal_contradiction` + `implementation_fact_only` | “A separate hypothesis asks whether an effective mass-like observable could emerge even though current Core contains an explicit optional `mu` field.” |
| QF-MU-02 | `mu` explicitly defines the emergent defect from phase overlap | no equation or intervention connects the proposal to active `mu` | `hypothesis_only` | require an operational observable and ablation |
| QF-COS-01 | pseudo-random foam flawlessly generates the Cosmic Web | no empirical comparison or executable receipt | `hypothesis_only` + `physical_analogy_only` | “may generate visually web-like patterns in a future defined model” |
| QF-COS-02 | visible and dark matter are the same phase intersections | unsupported physical claim | `hypothesis_only` | prohibit as factual wording |
| QF-OEA-01 | OEA scale traversal is equivalent to Lineum time evolution | analogy between different algorithms, not demonstrated causal equivalence | `hypothesis_only` | define and test a mapping before comparison |
| QF-HOR-01 | exactly 11 phases define the observer horizon | post-hoc numerical analogy without physical derivation | `hypothesis_only` | remove exact physical implication |
| QF-INT-01 | integer hashing resolves infinite-universe precision with near-zero memory | computational architecture proposal, not physics | `hypothesis_only` | move to an engineering hypothesis with complexity and correctness tests |

Quantum Foam remains a separate hypothesis family and must not be used as evidence for Relic Foam.

## 8. Narrow claims potentially retainable after verification

The following claim forms are scientifically useful because they are limited and falsifiable. They are not yet automatically eligible; each still needs its original reproduction status checked.

| Candidate safe claim | Current status |
|---|---|
| The active Core contains `psi`, `phi`, supplied `kappa`, and optional `mu`, but no `epsilon` state or explicit Eq-11.1 leakage law. | `eligible_for_canonical_wording` as implementation fact |
| The first current-Core `mu x kappa` repair matrix found negligible `mu` recovery effect and weak passive `kappa` shaping under its frozen conditions. | `eligible_for_canonical_wording` from permanent research receipt |
| Eq-11.1 survives as a historical explicit candidate equation, not the active public update law. | `eligible_for_canonical_wording` |
| The strongest historical Eq-11.1 survivor claims currently lack a recovered executable chain. | `eligible_for_canonical_wording` as provenance fact |
| The epsilon document describes an added environmental stock and local recycling concept. | `eligible_for_canonical_wording` as document fact, not validation |
| The same epsilon document reports terminal evaporation and a non-invariant total quantity. | `historical_unreproduced_claim` until replay, but editorially mandatory to preserve |
| The foam document later reports aging, no stable true re-ignition, and repeated-hit fatigue. | `historical_unreproduced_claim` until replay, but editorially mandatory to preserve |
| Relic Foam and Quantum Foam are scientifically different proposals. | `eligible_for_canonical_wording` |
| No current result supports Standard Model, life, cognition, or real-cosmology mapping. | `eligible_for_canonical_wording` |

## 9. Required future edit order

When the whitepaper edit gate is opened, changes should occur in this order:

1. correct document-level status metadata and equation-family labels;
2. add an evidence legend distinguishing active implementation, independently reproduced research, historical prose, and hypothesis;
3. split Eq-11.1 intrinsic, prepared, forced, confined, epsilon, and foam variants;
4. place negative and superseding results immediately beside the claims they qualify;
5. remove or scope absolute terms such as `proven`, `verified`, `canonical`, `immortal`, `indefinite`, `perfect`, `universal`, and `unconditional`;
6. replace physical ontology with model-internal observables unless an external evidence gate exists;
7. separate amplitude recovery, spatial repair, content copying, and lineage;
8. synchronize any generated presentation copies only through the repository's declared mechanism;
9. run whitepaper contract and consistency checks;
10. record the exact source research receipts for every retained numerical statement.

No generated portal copy should be edited directly.

## 10. Edit blockers

Whitepaper edits remain blocked until all of the following are resolved for the exact affected claim:

- current source file and generated-copy relationship are verified;
- the claim is tied to an equation variant rather than a shared metaphor;
- active implementation agreement or disagreement is stated;
- historical executable status is stated;
- positive and negative evidence is presented symmetrically;
- the intended scope is no broader than the tested domain;
- physical analogy is visibly separated from numerical fact;
- an owner-facing lay summary of the consequential canonical change is provided before promotion.

Missing historical runners do not block correcting obviously contradictory status language, but they do block replacing it with a new positive numerical claim.

## 11. Local and root-programme verdict

### 11.1 Local editorial verdict

```text
Eq-11.1 whitepaper:
    preserve equation and chronology;
    split variants;
    downgrade unreproduced validation and permanence claims;
    foreground reconstructed decay and far-field failures.

Epsilon whitepaper:
    downgrade Canonical/Closed/Unconditional wording;
    preserve local-cycle hypothesis and terminal evaporation;
    distinguish shock recovery from repair.

Relic Foam whitepaper:
    preserve historical residual-state, perturbation, and transport hypotheses;
    replace immortal/self-healing/re-ignition/infinite-reuse language with the later qualified outcomes;
    distinguish history dependence from usable memory.

Quantum Foam hypothesis:
    retain as separate speculation;
    state the active-mu implementation conflict;
    remove factual cosmology language unless independently supported.
```

### 11.2 Root-programme impact

This editorial map does not change the numerical priority. P2/C0 remains the primary physical lane when its retained package can be recovered. Eq-11.1, epsilon, and foam remain bounded provenance/reconstruction families.

No whitepaper, code, equation, simulation default, claim registry, or portal copy is changed here.

## 12. Continuous ledger

- `2026-07-31 source freeze`: recorded current SHAs for all four whitepapers and active `math.py`.
- `document-status audit`: identified contradictory canonical/draft/latest-version metadata in the equation history.
- `Eq-11.1 claim audit`: mapped amplitude, topology, binding, reconstruction, and later-phase contradictions.
- `epsilon claim audit`: mapped closed-energy, shock-recovery, terminal-evaporation, and unconditional-validation conflicts.
- `foam claim audit`: mapped immortality, healing, re-ignition, fatigue, environment, memory, logic, and system-classification conflicts.
- `quantum-foam audit`: separated the fractal hypothesis from Relic Foam and recorded the active-`mu` implementation conflict.
- `safe-claim extraction`: identified narrow implementation and provenance statements suitable for later canonical wording.
- `decision`: prepared a future edit order without modifying any source whitepaper.
