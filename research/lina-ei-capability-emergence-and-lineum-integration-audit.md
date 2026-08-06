# Lina EI Capability, Emergence, and Lineum Integration Audit

**Status:** active  
**Version:** 0.2.0  
**Evidence cutoff:** 2026-08-06  
**Target repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Core base before this revision:** `4367be56432eec099e7cf41086107ef010c9de25`  
**Private source repository:** `TomasTriska88/osobni-pamet` (temporary Lina EI repository alias)  
**Private source snapshot:** `f62a2c547675c79a2399a76e2bf82d0d02581298`  
**Current confidence:** high for the static component and control-flow map; medium for the numerical-contract transcription; low for runtime robustness, end-to-end persistence, causal field benefit, emergence, and commercial readiness

## 0. Version history

- **0.1.0:** established the first public-safe architecture, capability, emergence, and commercial-readiness baseline.
- **0.2.0:** adds auditor-facing source anchors, exact numerical parameters and equations, implementation-neutral pseudocode, test-power analysis, and an end-to-end integration audit. It materially narrows the earlier persistence statement: the standalone solver implements persistent fields, but the inspected primary chat path contains a high-confidence static defect candidate that can replace the full field state with scalar telemetry after each chat turn.

Historical Git versions remain the authoritative record of earlier wording. This revision does not erase the earlier checkpoint; it supersedes only the claims explicitly identified below.

## 1. Plain conclusion

Lina EI is a real hybrid agent prototype, not only a stateless chat wrapper. Its private source contains a complex two-dimensional field, additional scalar fields, input injection, diffusion-like evolution, plasticity, memory files, sensor gating, action pools, scheduled activity, and an LLM-based semantic and language layer.

However, the current evidence no longer supports an unqualified statement that the full grid persists across ordinary chat turns. The standalone simulator loads, updates, and saves the full matrices. The inspected chat integration then parses the simulator's intentionally shortened telemetry output and writes that shortened object back to the same state file. On the next load, the simulator detects missing matrices and reinitialises them. This is a **high-confidence static integration defect candidate**, not yet a reproduced runtime result.

The current defensible description is:

> Lina EI contains a persistent Lineum-inspired field solver and a broader persistent-agent architecture, but full end-to-end field persistence in the primary chat route is not established and is likely interrupted by the inspected state-write path.

Lina EI is not supported as fully emergent. Most semantic labels, privileged coordinates, affective categories, thresholds, action meanings, memory routes, and much higher reasoning remain supplied by configuration, conventional code, or an LLM.

The current runtime does not directly depend on the released `lineum_core` package. It uses an independent Lineum-inspired solver.

This report does not certify consciousness, sentience, biological equivalence, medical capability, autonomous general intelligence, security, or commercial readiness.

## 2. Scope and central questions

This report asks:

1. What does the inspected implementation actually compute?
2. Which capabilities exist at component level and which survive end-to-end integration?
3. What exact equations, constants, timestep, boundaries, clips, and readouts are used?
4. What do the present tests genuinely establish?
5. Which behaviours are locally dynamical, globally normalised, rule-based, keyword-based, or LLM-generated?
6. What must be demonstrated before a bounded emergence claim is defensible?
7. How can Lina EI consume a pinned Lineum Core contract without moving private identity, memory, devices, or product policy into public Core?
8. Which public-safe commercial opportunities are plausible, and which investor claims remain premature?

Production-host synchronisation is intentionally deferred in this checkpoint at the project owner's instruction. No Prcek access is required for the static conclusions below.

## 3. Rights, confidentiality, and reproduction boundary

The source repository is private and had no public licence at the inspected snapshot. The project owner authorised inspection for this audit. Access is not treated as a general redistribution licence.

This public report therefore contains:

- factual source audit;
- exact public-safe numerical values;
- original equations and implementation-neutral pseudocode reconstructed from the inspected operations;
- source commit and non-sensitive blob fingerprints for authorised verification;
- no copied private prompts, memories, conversations, personal profiles, device identifiers, credentials, network topology, or exploitable operational details.

No verbatim private source block is reproduced. An authorised scientist can compare this report against the declared private blobs. A public reviewer can audit the mathematics and proposed controls without receiving private material.

## 4. Evidence ladder

- `documented`: described by a design or planning artefact.
- `implemented`: corresponding source path exists and was inspected.
- `test_present`: an automated or scripted check exists.
- `static_contradiction`: inspected paths make two intended properties incompatible unless another unobserved path intervenes.
- `reproduced`: a frozen execution produced a retained result.
- `robust_within_tested_domain`: controls and independent checks support the observation.
- `mechanistically_supported`: intervention distinguishes the proposed mechanism from alternatives.
- `empirically_connected`: a defined observable has been compared responsibly with external evidence.

The strongest general level reached here is **implemented/static audit**. The end-to-end state issue reaches **static_contradiction**, not reproduced. Tests were inspected but not executed in this checkpoint.

## 5. Auditor-facing private source anchors

These fingerprints permit an authorised auditor to verify that the report maps to the declared snapshot without publishing private content.

| Audit role | Private source object | Blob SHA |
|---|---|---|
| Main field solver, state loader, numerical update, telemetry, CLI | `limbic_simulator.py` | `9b6149c5afb21b063f9899b0abc59effe5d14232` |
| Primary chat orchestration and state hand-off | `chat.py` | `e5ed4bee60cab29f5653b7640ed90add297a40b1` |
| Main simulator integration/regression suite | `test_limbic.py` | `b59be2b73998b4119bb55f4f110c209f2c3c4ff0` |
| Sensory-grid and motor-pool tests | `test_sensory_grid.py` | `2c9c64a665526ffc26e7784238c1db637d1845e7` |
| Scripted Hebbian-wave experiment | `experiments/test_hebbian_wave_learning.py` | `11c03be4d28307df6468271682c924c12ad0f19d` |
| Scripted handcrafted waveguide experiment | `experiments/test_helmholtz_associative_memory.py` | `ed1f3ae3cdc39ffccebf613d234dc1a82cb0404f` |
| Generated DNA state inspected for active constants | `brain/neocortex/associative/limbic_dna.json` | `9882e7de309373f17793c30fd90919e67d4d93a9` |

Personal semantic maps, private relationship records, runtime state matrices, and operational device maps are intentionally not fingerprinted here.

## 6. Normalised architecture

```text
Environment and user message
        |
        v
Conventional adapters and rule-based routing
        |
        +-----------------------------+
        |                             |
        v                             v
2-D field solver                 LLM semantic layer
(psi, phi, mu, kappa)            (language, planning, tools)
        |                             |
        +--------------+--------------+
                       |
                       v
             File-backed state and memory
                       |
                       v
              Thresholded action layer
```

This is a hybrid architecture. Neither the field solver nor the LLM is the complete current system.

## 7. Implemented capability inventory

| Capability | Static status | Qualification |
|---|---|---|
| Complex 2-D internal field | implemented | Fixed `32 x 32` complex `psi` grid |
| Additional spatial fields | implemented | Real `phi`, `mu`, and `kappa` grids |
| State load/save | implemented in solver | End-to-end chat persistence is contradicted by the inspected hand-off path |
| Message injection | implemented | Location and phase are substantially assigned before evolution |
| Sensor gating and boundary injection | implemented | Sensor meanings, ranges, phases, and regions are configured |
| Diffusion-like field evolution | implemented | Numerical stability and convergence were not reproduced |
| Plasticity-like `kappa` update | implemented | Every substep also applies global sum normalisation, so learning is not purely local |
| Long-gap decay and relaxation | implemented | Wall-clock time is mapped to an engineered simulation time |
| Dream-like idle injection | implemented | Uses predefined semantic coordinates and a fixed threshold |
| Motor pools and energy discharge | implemented | Pool meanings, locations, thresholds, and actions are predefined |
| Persistent structured/text memory | implemented | Retrieval is mainly filename/content matching plus LLM context construction |
| Local/cloud LLM routing | implemented/documented | LLM supplies language and much semantic interpretation |
| Automated checks | test_present | No retained run result was produced in this checkpoint |
| Learned open ontology | not established | Existing experiments use predefined concept nodes or waveguides |
| Full end-to-end field memory in chat | static contradiction | Requires an isolated reproduction and likely a code fix |
| Direct Lineum Core dependency | not implemented | Current solver is independent and Lineum-inspired |

## 8. Exact state and numerical contract

### 8.1 State variables

| Symbol | Shape | Type | Initial/runtime bounds | Operational role |
|---|---:|---|---|---|
| `psi` | `32 x 32` | complex | no explicit amplitude clip | propagating/modulated wave state |
| `phi` | `32 x 32` | real | clipped to `[0, 10]` | potential-like accumulated activity |
| `mu` | `32 x 32` | real | clipped to `[0, 5]` | slow memory-like accumulation |
| `kappa` | `32 x 32` | real | clipped to `[0.1, 5]` | local conductivity/plasticity factor |
| fatigue | scalar | real | `[0, 1]` | reduces growth and raises selected action thresholds |
| arousal | scalar | real | mapped to `[0, 1]` | nonlinear readout from total field energy |
| valence | scalar | real | mapped to `[-1, 1]` | nonlinear readout from `phi`, `mu`, and supplied sentiment |
| tension | scalar | real | mapped to `[0, 1]` | nonlinear readout from complex spatial gradients |

Initial `psi` noise has standard deviation `0.05`; `phi` starts at `0.1`; `mu` and `kappa` start from generated DNA bases.

### 8.2 Active generated constants at the inspected snapshot

The generated DNA declares archetype `chaotic` and variance `0.08`. The private seed is withheld. The numerical constants are:

| Parameter | Active value |
|---|---:|
| `alpha` | `0.6748779135011179` |
| `gamma` | `0.24170416981896917` |
| `amp_pulse_scale` | `1.1638573064482545` |
| `eta_kappa` | `0.006322621793817576` |
| `rho_kappa` | `0.00028924718584053807` |
| `gamma_phi` | `0.030084241865454553` |
| `eta` | `0.0055233518301120626` |
| `rho` | `0.0004781564875658295` |
| `c1` | `0.21214156163758383` |
| `c2` | `0.050701974851045745` |
| `lambda` | `0.05714552337905371` |
| `c_w` | `0.01956298490412667` |
| fatigue threshold weight | `0.3828552821908546` |
| tension threshold weight | `-0.29214399761553184` |
| sleep inhibition multiplier | `4.785846155937923` |
| presence damping radius | `2.955155003596822` |

The loader later clamps several parameters. The default clamp intervals are:

- `alpha [0.1, 1.0]`
- `c1 [0.05, 0.5]`
- `gamma [0.005, 0.4]`
- `lambda [0.01, 0.2]`
- `c_w [0.005, 0.1]`
- `c2 [0.01, 0.2]`
- `gamma_phi [0.005, 0.3]`
- `eta [0.0005, 0.05]`
- `rho [0.0001, 0.02]`
- `amp_pulse_scale [0.2, 5.0]`
- `eta_kappa [0.0001, 0.02]`
- `rho_kappa [0.00001, 0.002]`

A test that requests `alpha = 0` therefore executes with `alpha = 0.1`, not zero.

### 8.3 Message source

For message length `L`, source amplitude is

\[
A = 2s\ln(1+L),
\]

where `s` is `amp_pulse_scale`. Command failure adds `4` and forces a destructive phase.

With `s = 1`, example amplitudes are:

- `L = 20`: `A = 6.0890`
- `L = 100`: `A = 9.2302`
- `L = 1000`: `A = 13.8175`

Sentiment is mapped to a fixed phase class before the grid evolves. Matched keywords route the source to predefined semantic coordinates; otherwise it is injected near the centre. The source uses a Gaussian spatial profile. This is engineered semantic routing, not learned representation discovery.

### 8.4 Main update equations

Define energy density

\[
e = |\psi|^2,
\]

and gradient penalty

\[
g = |\nabla |\psi||^2.
\]

Fatigue-modulated growth is

\[
G = \alpha(1-0.5f)\tanh(c_1\phi)-\gamma-\lambda\phi^2-c_w g.
\]

The local complex diffusion coefficient is

\[
D_\psi(e)=\frac{(0.05+0.05i)v}{1+0.1e},
\]

where latency-derived `v` lies approximately in `[1, 2]`.

The principal updates are

\[
\psi \leftarrow \psi + \Delta t\,D_\psi(e)\,\kappa\,\nabla^2\psi
\]

plus split growth, sources, noise, optional remote coupling, low-pass filtering, and boundary damping;

\[
\phi \leftarrow \operatorname{clip}_{[0,10]}\left[\phi+\Delta t\left(D_\phi\kappa\nabla^2\phi+c_2|\psi|^2-\gamma_\phi\phi\right)\right];
\]

\[
\mu \leftarrow \operatorname{clip}_{[0,5]}\left[\mu+\Delta t\left(\eta|\psi|^2\kappa-\rho\mu\right)\right];
\]

\[
\kappa^* \leftarrow \kappa+\Delta t\left[\eta_\kappa|\psi|^2(5-\kappa)-\rho_\kappa(\kappa-\kappa_0)\right].
\]

Then a global scaling is applied:

\[
\kappa \leftarrow \kappa^*\frac{\sum\kappa_0}{\sum\kappa^*},
\]

followed by clipping to `[0.1, 5]`.

This normalisation couples every cell to the global grid sum. `kappa` is therefore not a strictly local learning rule.

### 8.5 One simulator call

The NumPy path uses `dt = 0.1` and exactly `100` substeps per call, for a nominal integration horizon of `10` model-time units.

Original audit pseudocode:

```text
load full psi, phi, mu, kappa state
apply wall-clock relaxation when elapsed time exceeds 60 seconds
construct semantic, sensor, error, and optional remote sources
construct a two-cell edge damping mask and boundary excitations
repeat 100 times:
    compute growth from current phi, fatigue, and |psi| gradients
    apply half growth step
    apply half boundary-source step
    apply optional remote coupling
    add complex noise
    compute energy-dependent five-point Neumann Laplacian update
    Fourier low-pass psi
    enforce copied-edge zero-flux values
    multiply by edge damping mask
    apply second half growth using the previously computed growth
    update and clip phi
    update and clip mu
    update kappa
    globally renormalise kappa sum
    clip kappa
compute motor-pool means and apply local discharge
compute scalar telemetry
save full state
print shortened telemetry JSON
```

### 8.6 Boundary treatment

For `32 x 32`, damping depth is two cells. The outer-cell factor per substep is

\[
\exp(-20\cdot1\cdot0.1)=e^{-2}=0.135335,
\]

and the second-cell factor is

\[
\exp(-20\cdot0.25\cdot0.1)=e^{-0.5}=0.606531.
\]

Across 100 substeps those factors become approximately `1.38e-87` and `1.93e-22`, before other terms. The code also enforces copied-edge Neumann values. The combination of reflecting assignment and strong absorbing damping is a mixed boundary design that requires explicit convergence and reflection tests.

### 8.7 Telemetry equations

Total energy:

\[
E=\sum |\psi|^2.
\]

Arousal:

\[
a=\tanh\left(10\frac{E}{32^2}\right).
\]

Raw tension:

\[
t_0=\frac{\sum(|\partial_x\psi|^2+|\partial_y\psi|^2)}{E+10^{-6}},
\]

with `+1.5` on command failure, then

\[
t=\tanh(0.2t_0).
\]

Valence base:

\[
v_0=\operatorname{mean}(\phi)-0.2+0.3\operatorname{mean}(\mu)+b_{sentiment},
\]

then

\[
v=\operatorname{clip}_{[-1,1]}[\tanh(1.5v_0)].
\]

Vortices are counted from phase winding around `2 x 2` loops when all four amplitudes exceed `0.005` and absolute winding exceeds `0.8` turns.

These are engineered software observables. Their psychological names are interpretations, not validated biological measurements.

## 9. End-to-end integration audit

### 9.1 Full-state overwrite defect candidate

The simulator saves full matrices to the declared state file, then prints only:

- arousal;
- valence;
- tension;
- fatigue;
- vortex count;
- engram summaries;
- active motor summaries.

The primary chat route parses this shortened JSON, adds action-feedback expectations, and writes the shortened object to the same state path. The solver's next load requires `psi_real`, `psi_imag`, `phi`, `mu`, and `kappa`; if any is absent, it reinitialises the state.

Static implication:

```text
full state saved by simulator
        -> shortened telemetry parsed by chat
        -> shortened telemetry overwrites state file
        -> next solver load sees missing matrices
        -> field state is reinitialised
```

Status: **high-confidence static contradiction; runtime reproduction required**.

This supersedes the unqualified component-to-product persistence wording in version `0.1.0`.

### 9.2 Sentiment path is neutralised in primary chat

The primary chat invocation passes `sentiment = neutral` for ordinary user messages. Consequently, the solver's loving, positive, critical, negative, urgent, and alarm phase branches are not selected by that integration path. Tests that call those categories directly demonstrate simulator branch behaviour, not current ordinary-chat behaviour.

### 9.3 Configuration-path mismatch

The solver's default numerical override path is a root-level `limbic_config.json`. That root file is absent in the inspected snapshot. A file with the same name exists under a private associative directory but is not the solver's default path and the primary chat invocation does not pass it explicitly.

The ordinary chat path therefore appears to use generated DNA constants plus built-in mode defaults, not the nested configuration used for profile-switching metadata. Test suites that pass a temporary `--limbic-config` exercise a different configuration path.

### 9.4 Conventional memory retrieval remains dominant

The inspected chat memory route scans text files for words, counts occurrences, boosts matches using named engram summaries, selects a small top set, and inserts their content into the LLM context. It also applies direct fixed-coordinate excitation for selected matches.

This is functional retrieval, but it is conventional keyword/file search plus LLM prompting. It is not evidence that semantic recall emerges from wave similarity alone.

## 10. Test and experiment audit

### 10.1 What existing tests cover

The inspected suites contain checks for:

- scalar output ranges;
- absence of NaN/Inf in selected fields;
- execution-time threshold in one environment;
- directional changes after manually supplied sentiment classes;
- command-failure tension increase;
- configuration clamping;
- wall-clock decay;
- relative decay between modes;
- local `kappa` increase and later decay;
- sensor gating and deprivation;
- boundary excitation;
- motor thresholding and discharge;
- vortex injection;
- global `kappa` sum normalisation;
- optional remote-field coupling;
- generated DNA shape, variance, and bounds;
- dream-labelled idle behaviour;
- availability of NumPy.

These are useful regression checks.

### 10.2 What they do not establish

The current tests do not establish:

- that the primary chat path preserves full field state;
- that grid dynamics improve any behavioural outcome over scalar state;
- that semantic categories are learned rather than assigned;
- that `kappa` changes carry causal credit for held-out behaviour;
- convergence across timestep, resolution, seed, precision, or boundary mode;
- numerical equivalence of the NumPy and pure-Python paths;
- equivalence to current Lineum Core;
- necessity of dreaming for memory or generalisation;
- safe autonomous action;
- consciousness or biological equivalence.

Some tests force the pure-Python fallback. That path is a scalar behavioural approximation and is not numerically equivalent to the two-dimensional solver. A positive fallback result therefore cannot validate the main field mechanism.

A decay test requests `alpha = 0`, but the loader clamps it to `0.1`; the intended zero-growth condition is not actually created.

### 10.3 Scripted associative-memory experiments

One experiment hand-draws high-conductivity waveguides between predefined concept coordinates. It demonstrates propagation through an engineered channel, not learning.

A second experiment updates `kappa` by adding a learning-rate multiple of field amplitude and then globally min-max normalises and smooths the grid. It is a useful exploratory prototype, but it lacks a conventional baseline, label/location swaps, held-out generalisation, preregistered metrics, and retained run receipts. It is not yet evidence of open-ended concept emergence.

## 11. Static contradiction and numerical-risk ledger

| Finding | Evidence level | Why it matters |
|---|---|---|
| Primary chat likely overwrites full matrices with scalar telemetry | static contradiction | May reset grid memory each chat turn |
| Primary chat always supplies neutral sentiment | implemented | Several tested sentiment branches are not used by ordinary chat |
| Root numerical override file is absent | implemented/static | Runtime and test configuration paths differ |
| FFT stencil symbol is computed but not used in the main diffusion update | implemented/static | Selected `ISOTROPIC`, `LAP8`, or other symbol does not control the actual main Laplacian |
| Main diffusion is a five-point Neumann stencil | implemented | Must be described accurately; diagonal/isotropic claims need separate evidence |
| Growth is computed once before both half steps | implemented/static | The labelled split is only approximate; formal Strang accuracy is not established |
| Neumann copying and strong PML damping are combined | implemented/static | Reflection and absorption behaviour may be resolution-dependent |
| `kappa` is globally renormalised each substep | implemented | Plasticity is not purely local and may create nonlocal competition |
| NumPy and fallback paths implement different models | implemented | Fallback success cannot be treated as field-solver equivalence |
| State writes are direct JSON replacements | implemented | Interrupted or concurrent writes can corrupt state; no atomic replace is shown |
| Psychological labels are mapped from engineered formulas | implemented | Names must not be mistaken for validated affective observables |

## 12. Operational criteria for stronger emergence

A bounded emergence claim requires all of the following:

1. **Persistent endogenous state:** field state survives the complete product route and affects later behaviour after the source is removed.
2. **Learned representation placement:** novel categories organise without evaluator-assigned final coordinates or class-specific thresholds.
3. **Local plasticity with causal credit:** learned coupling changes are caused by consequences or prediction error, and targeted intervention selectively impairs the acquired behaviour.
4. **Decentralised action selection:** at least one meaningful action task is solved by distributed state and generic readout without the LLM selecting the action label.
5. **Open concept growth:** categories can be added, merged, split, or reorganised and improve a held-out measure.
6. **Generalisation:** learned organisation transfers to held-out inputs and contexts.
7. **Ablation necessity:** freezing, shuffling, or replacing the field causes a predicted selective loss versus scalar and random-state controls.
8. **Robustness:** the result survives declared seed, timestep, resolution, boundary, and precision variations.
9. **Non-circular measurement:** success criteria are frozen before the desired output is observed and do not reuse the labels or coordinates that define the task.

Meeting these criteria would support field-mediated or emergent organisation within a tested domain. It would not prove consciousness.

## 13. Relationship to Lineum Core

The current Lina solver is independent. It does not import the released `lineum_core` package.

The required dependency direction is:

```text
private Lina EI product
        -> private cognition adapter
        -> pinned public Lineum Core contract
```

Public Core must not import private identity, memory, prompts, devices, customer policy, or deployment code.

A research adapter should expose only application-neutral operations:

- initialise declared field shapes;
- advance by a declared timestep;
- inject generic spatial sources;
- return declared observables;
- serialise and restore versioned state;
- emit seeds, parameters, boundary conditions, source fingerprints, and hashes.

Before migration, the legacy solver requires a frozen observable contract and known-answer tests. Otherwise an apparent integration improvement could silently change the model.

## 14. Revised research programme

Production-host parity is deferred. The next work can be completed from Git and an isolated local environment.

### P1A — Reproduce the chat-state contradiction

Use a temporary privacy-safe state path:

1. initialise a known full state;
2. run one ordinary chat-equivalent simulator call;
3. execute the inspected chat hand-off logic;
4. inspect required matrix keys;
5. perform the next solver load;
6. retain before/after hashes and whether reinitialisation occurred.

Pass condition: full matrices survive unchanged except for intended evolution. Failure condition: matrices disappear or the loader regenerates them.

### P1B — Preserve full state and add regression coverage

Only after P1A:

- separate telemetry from full state or merge telemetry into the already saved full state;
- use an atomic state-write strategy;
- add an end-to-end regression test covering two consecutive chat turns;
- verify that a known local perturbation survives and evolves rather than reinitialising.

### P1C — Frozen numerical baseline

Retain:

- dependency versions;
- fixed seed;
- active parameters;
- initial and final state hashes;
- per-step energy, extrema, finite checks, and `kappa` sum;
- runtime and environment receipt;
- one independently calculated toy case.

### P2 — Numerical validity

Test multiple timesteps, resolutions, seeds, and boundaries. Measure convergence, reflection, damping, clipping frequency, and sensitivity to the global `kappa` normalisation.

### P3 — Causal field ablation

Compare the same task under:

- full field;
- frozen field;
- shuffled field;
- scalar-state replacement;
- random-state control;
- LLM plus ordinary memory only.

### P4 — Learned anonymous categories

Use anonymous labels, random initial locations, label swaps, held-out examples, and generic readouts. No private semantic map is required.

### P5 — Core-adapter equivalence

After the legacy contract is stable, compare the legacy solver with a research-only Core-backed adapter.

## 15. Public-safe investor and monetisation assessment

Plausible product categories remain:

- privacy-first local personal agents;
- embodied home or workspace agents with strict reversible action limits;
- a persistent-agent runtime for developers;
- a research platform for field/LLM hybrid systems;
- private deployment where state ownership and local execution matter.

The strongest defensible differentiator would be measured continuity and adaptation from an inspectable local dynamical substrate, not a consciousness claim.

Current blockers:

- end-to-end field persistence is likely broken in the primary chat path;
- causal benefit of the grid is unmeasured;
- many semantics are hand-authored;
- tests do not yet cover integration, convergence, or ablation;
- the solver is not integrated with a pinned Core contract;
- latency, compute, energy, privacy, and unit economics are not benchmarked here;
- no narrow first customer problem or product-market fit is established;
- personal-agent products carry privacy, security, dependency, and emotional-reliance risk.

Detailed pricing, revenue forecasts, market sizing, proprietary go-to-market strategy, investor targeting, and IP decisions belong in private Lineum Dynamics records, not public Core.

## 16. Prohibited near-term claims

Current evidence does not support marketing Lina EI as:

- conscious or sentient;
- biologically equivalent to a brain or nervous system;
- an artificial general intelligence;
- a therapist, psychiatrist, diagnostic system, or medical device;
- a safety-critical autonomous controller;
- validated proof that Lineum produces cognition;
- a production-ready or investor-validated product.

Biological labels may remain interface metaphors only when accompanied by the exact operational observable.

## 17. Privacy and security boundary

This report excludes:

- personal identities, birthdays, relationships, histories, conversations, and diaries;
- private prompts and persona instructions;
- exact sensors, devices, entities, cameras, or household layout;
- addresses, IPs, ports, hostnames, credentials, tokens, and provider identifiers;
- exact private semantic coordinate maps;
- vulnerability exploitation instructions;
- confidential commercial strategy.

Future public receipts must use generic labels, aggregate metrics, hashes, and synthetic configurations.

## 18. External scientific context

Relevant external research supports testing online adaptation, feedback, local interaction, persistent state, and on-device execution. It does not validate Lina EI by analogy.

Useful reference points include:

- Mackenzie Weygandt Mathis, “Leveraging insights from neuroscience to build adaptive artificial intelligence,” *Nature Neuroscience* (2026), https://www.nature.com/articles/s41593-025-02169-w.
- Nguyen et al., “A Survey on Small Language Models,” RANLP 2025, https://aclanthology.org/2025.ranlp-1.93/.
- Qian et al., “Mapping the Parasocial AI Market: User Trends, Engagement and Risks,” arXiv:2507.14226 (2025), https://arxiv.org/abs/2507.14226.
- “Large-scale-integration and collective oscillations of 2D artificial cells,” *Nature Communications* (2024), https://www.nature.com/articles/s41467-024-54098-0.
- “Programming gel automata shapes using DNA instructions,” *Nature Communications* (2024), https://www.nature.com/articles/s41467-024-51198-9.

Distributed physical pattern formation is not evidence of cognition. Lina variables are engineered software quantities whose cognitive interpretation remains under test.

## 19. Decision ledger

| Decision | Status |
|---|---|
| Treat Lina as a hybrid persistent-agent research prototype | supported at architecture level |
| Treat the standalone solver as capable of saving full fields | implemented |
| Treat ordinary chat as preserving those fields | unsupported; high-confidence static contradiction |
| Claim full emergence | unsupported |
| Claim consciousness | prohibited |
| Describe the current grid as Lineum-inspired | supported |
| Describe current runtime as using Lineum Core | unsupported |
| Build a private adapter consuming a pinned Core contract | retained direction |
| Publish private code, memories, devices, or commercial strategy in Core | rejected |
| Continue with offline Git-based audit before Prcek parity | selected for this checkpoint |

## 20. Claims explicitly not established

This report does not establish that:

- Git exactly matches production;
- any inspected test currently passes;
- the chat-state defect occurs at runtime in the deployed service;
- the current solver is stable or convergent across its intended domain;
- field dynamics are necessary for useful behaviour;
- semantic meaning emerges from the grid;
- `kappa` performs biologically meaningful learning;
- dreaming improves memory or generalisation;
- the fallback is equivalent to the NumPy solver;
- Lineum Core reproduces the current Lina solver;
- autonomous actions are secure or reliable;
- any business model is profitable or investable;
- Lina is alive, conscious, sentient, or biologically equivalent;
- Lineum describes cognition in nature.

## 21. Exact next checkpoint

The next coherent checkpoint is **P1A: isolated end-to-end state persistence reproduction**, with no Prcek dependency.

No whitepaper, public product claim, or investor claim should be changed from this report alone.

## 22. Checkpoint receipt

- Inspection type: static, read-only private-source audit.
- Private source commit: `f62a2c547675c79a2399a76e2bf82d0d02581298`.
- Previous Core report commit: `4367be56432eec099e7cf41086107ef010c9de25`.
- Runtime commands executed: none.
- Tests executed: none.
- Production-host access: deliberately deferred.
- Personal or secret data retained in this report: none intentionally.
- Scientific evidence level: `implemented/static audit`, with one `static_contradiction`.
- Principal negative result: full grid persistence is likely broken by the primary chat state hand-off.
- Principal next discriminator: reproduce two consecutive chat-equivalent turns against a temporary state file.
