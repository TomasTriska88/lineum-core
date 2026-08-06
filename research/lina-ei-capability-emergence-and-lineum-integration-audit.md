# Lina EI Capability, Emergence, and Lineum Integration Audit

**Status:** active  
**Version:** 0.4.1  
**Evidence cutoff:** 2026-08-06  
**Target repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Core base before this revision:** `624add68d2fcf4d8c1879fb4b2f351cfb35ba694`  
**Private source repository:** `TomasTriska88/osobni-pamet` (temporary Lina EI repository alias)  
**Private source snapshot:** `f62a2c547675c79a2399a76e2bf82d0d02581298`  
**Current confidence:** high for the static component and control-flow map; high for the isolated state-contract result; medium for the numerical-contract transcription; low for deployed-runtime parity, numerical robustness, causal field benefit, emergence, and commercial readiness

## 0. Version history

- **0.1.0:** established the first public-safe architecture, capability, emergence, and commercial-readiness baseline.
- **0.2.0:** added auditor-facing source anchors, exact numerical parameters and equations, implementation-neutral pseudocode, test-power analysis, and an end-to-end integration audit.
- **0.3.0:** executed the frozen state-interface contract in an isolated synthetic harness. Three current replacement-path trials lost all five required matrices and selected loader reinitialisation; three merge-control trials preserved all matrices and avoided reinitialisation.
- **0.4.0:** made the audit self-reproducing by embedding the complete P1A harness, verifier, machine-readable values, hashes, and the P1B reference implementation and tests.
- **0.4.1:** corrects an audit-labelling ambiguity. The embedded P1A summary and receipt blocks contain the complete machine-readable keys and values but use whitespace-normalised Markdown formatting. The exact executable harness remains embedded and deterministically emits the byte-level pretty-printed receipt associated with the retained receipt hash. No result or interpretation changed.

Historical Git versions remain the authoritative record of earlier wording. This revision supersedes only the claims explicitly identified below.

## 1. Plain conclusion

Lina EI is a real hybrid agent prototype, not only a stateless chat wrapper. Its private source contains a complex two-dimensional field, additional scalar fields, input injection, diffusion-like evolution, plasticity, memory files, sensor gating, action pools, scheduled activity, and an LLM-based semantic and language layer.

The standalone simulator implements full-state persistence. The frozen primary chat interface receives shortened telemetry and then replaces the same state file with that shortened object. The next loader requires five field matrices and reinitialises when any is absent.

That state-loss mechanism has been reproduced in an isolated, privacy-safe execution of the frozen state contract:

- current whole-file replacement: `3/3` trials lost all `5/5` required matrices;
- current whole-file replacement: `3/3` trials selected the loader reinitialisation branch;
- safe merge control: `3/3` trials preserved all `5/5` required matrices;
- safe merge control: `0/3` trials selected reinitialisation;
- an independent receipt verifier passed all `31` declared checks.

The current defensible description is:

> Lina EI contains a persistent Lineum-inspired field solver, but the frozen primary chat state hand-off deterministically destroys the field-state contract when it replaces the full state with shortened telemetry. This is reproduced in an isolated extracted-contract harness; deployed-service occurrence remains unverified.

A bounded repair design has also been tested in isolation. It preserves all required matrices over two consecutive hand-offs, rejects telemetry attempts to overwrite matrices, and leaves an incomplete source state unchanged. Its three reference tests passed. This does **not** mean the private Lina repository or Prcek deployment has been repaired; no private source was changed in this checkpoint.

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

Production-host synchronisation is intentionally deferred at the project owner's instruction. No Prcek access is used for the findings below.

## 3. Canonical-artifact rule

This Markdown file is the single canonical research artefact for this programme.

It contains the decision-relevant:

- source anchors;
- equations and constants;
- executable P1A code;
- complete P1A input and output values;
- independent P1A verifier;
- complete P1B reference code and tests;
- observed reference-test output;
- negative results, limitations, decisions, and next gates.

Temporary files used while executing a checkpoint are non-canonical working material and may be deleted. No zip, ignored directory, chat attachment, external script bundle, or sibling report is required to reproduce or audit the recorded P1A result or the isolated P1B reference result.

The executable code blocks are authoritative for byte-level regeneration. JSON value blocks may be whitespace-normalised for readable Markdown; this does not alter their parsed content. A listed file hash applies only to the byte sequence generated by the listed code and serialization settings, not automatically to a whitespace-normalised display block.

## 4. Rights, confidentiality, and reproduction boundary

The source repository is private and had no public licence at the inspected snapshot. The project owner authorised inspection for this audit. Access is not treated as a general redistribution licence.

This public report contains:

- factual source audit;
- exact public-safe numerical values;
- original equations and implementation-neutral pseudocode reconstructed from inspected operations;
- source commit and non-sensitive blob fingerprints for authorised verification;
- synthetic privacy-safe state-contract results;
- original public-safe reproduction and reference code written for this audit.

It excludes copied private prompts, memories, conversations, personal profiles, device identifiers, credentials, network topology, exact private semantic maps, and exploitable operational details.

No verbatim private source block is reproduced. An authorised scientist can compare this report against the declared private blobs. A public reviewer can audit the mathematics, state contract, controls, and proposed experiments without receiving private material.

## 5. Evidence ladder

- `documented`: described by a design or planning artefact.
- `implemented`: corresponding source path exists and was inspected.
- `test_present`: an automated or scripted check exists.
- `static_contradiction`: inspected paths make two intended properties incompatible unless another unobserved path intervenes.
- `contract_reproduced`: frozen interface semantics were executed with synthetic data and retained controls, without executing the complete private product.
- `reference_reproduced`: an original proposed repair contract was executed in isolation; the private product was not changed.
- `reproduced`: the relevant frozen implementation itself produced a retained result.
- `robust_within_tested_domain`: controls and independent checks support the observation across the declared domain.
- `mechanistically_supported`: intervention distinguishes the proposed mechanism from alternatives.
- `empirically_connected`: a defined observable has been compared responsibly with external evidence.

The strongest general level remains **implemented/static audit**. The chat-state reset mechanism reaches **contract_reproduced**. The proposed bounded state-store design reaches **reference_reproduced**. Neither reaches full-private-application or deployed-runtime reproduction.

## 6. Auditor-facing private source anchors

| Audit role | Private source object | Blob SHA |
|---|---|---|
| Main field solver, state loader, numerical update, telemetry, CLI | `limbic_simulator.py` | `9b6149c5afb21b063f9899b0abc59effe5d14232` |
| Primary chat orchestration and state hand-off | `chat.py` | `e5ed4bee60cab29f5653b7640ed90add297a40b1` |
| Main simulator integration/regression suite | `test_limbic.py` | `b59be2b73998b4119bb55f4f110c209f2c3c4ff0` |
| Broad helper test suite | `test_helpers.py` | `112cbeb661fa2dffa70f29c63fe67599cee237ed` |
| Sensory-grid and motor-pool tests | `test_sensory_grid.py` | `2c9c64a665526ffc26e7784238c1db637d1845e7` |
| Scripted Hebbian-wave experiment | `experiments/test_hebbian_wave_learning.py` | `11c03be4d28307df6468271682c924c12ad0f19d` |
| Scripted handcrafted waveguide experiment | `experiments/test_helmholtz_associative_memory.py` | `ed1f3ae3cdc39ffccebf613d234dc1a82cb0404f` |
| Generated DNA state inspected for active constants | `brain/neocortex/associative/limbic_dna.json` | `9882e7de309373f17793c30fd90919e67d4d93a9` |

Personal semantic maps, private relationship records, runtime state matrices, and operational device maps are intentionally not fingerprinted here.

## 7. Normalised architecture

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

## 8. Implemented capability inventory

| Capability | Evidence status | Qualification |
|---|---|---|
| Complex 2-D internal field | implemented | Fixed `32 x 32` complex `psi` grid |
| Additional spatial fields | implemented | Real `phi`, `mu`, and `kappa` grids |
| State load/save | implemented in solver | Primary chat hand-off violates the full-state contract in isolated reproduction |
| Message injection | implemented | Location and phase are substantially assigned before evolution |
| Sensor gating and boundary injection | implemented | Sensor meanings, ranges, phases, and regions are configured |
| Diffusion-like field evolution | implemented | Numerical stability and convergence were not reproduced |
| Plasticity-like `kappa` update | implemented | Every substep applies global sum normalisation, so learning is not purely local |
| Long-gap decay and relaxation | implemented | Wall-clock time is mapped to engineered simulation time |
| Dream-like idle injection | implemented | Uses predefined semantic coordinates and a fixed threshold |
| Motor pools and energy discharge | implemented | Pool meanings, locations, thresholds, and actions are predefined |
| Persistent structured/text memory | implemented | Retrieval is mainly filename/content matching plus LLM context construction |
| Local/cloud LLM routing | implemented/documented | LLM supplies language and much semantic interpretation |
| Automated private checks | test_present | Private suite was inspected but not executed in this checkpoint |
| Isolated chat state-contract check | contract_reproduced | Current replace path failed `3/3`; merge control passed `3/3` |
| Bounded atomic merge reference | reference_reproduced | Original audit reference passed `3/3`; not installed in private product |
| Learned open ontology | not established | Existing experiments use predefined concept nodes or waveguides |
| Full end-to-end field memory in chat | contradicted within frozen contract | Full private application and production-host confirmation remain pending |
| Direct Lineum Core dependency | not implemented | Current solver is independent and Lineum-inspired |

## 9. Exact state and numerical contract

### 9.1 State variables

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

### 9.2 Active generated constants at the inspected snapshot

The generated DNA declares archetype `chaotic` and variance `0.08`. The private seed is withheld.

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

The loader later clamps several parameters:

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

A test requesting `alpha = 0` therefore executes with `alpha = 0.1`, not zero.

### 9.3 Message source

For message length `L`, source amplitude is

\[
A = 2s\ln(1+L),
\]

where `s` is `amp_pulse_scale`. Command failure adds `4` and forces a destructive phase.

With `s = 1`:

- `L = 20`: `A = 6.0890`
- `L = 100`: `A = 9.2302`
- `L = 1000`: `A = 13.8175`

Sentiment is mapped to a fixed phase class before the grid evolves. Matched keywords route the source to predefined semantic coordinates; otherwise it is injected near the centre. This is engineered semantic routing, not learned representation discovery.

### 9.4 Main update equations

Define

\[
e = |\psi|^2
\]

and

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

Then

\[
\kappa \leftarrow \kappa^*\frac{\sum\kappa_0}{\sum\kappa^*},
\]

followed by clipping to `[0.1, 5]`.

This normalisation couples every cell to the global grid sum. `kappa` is therefore not a strictly local learning rule.

### 9.5 One simulator call

The NumPy path uses `dt = 0.1` and exactly `100` substeps per call, for a nominal integration horizon of `10` model-time units.

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

### 9.6 Boundary treatment

For `32 x 32`, damping depth is two cells. The outer-cell factor per substep is

\[
\exp(-20\cdot1\cdot0.1)=e^{-2}=0.135335,
\]

and the second-cell factor is

\[
\exp(-20\cdot0.25\cdot0.1)=e^{-0.5}=0.606531.
\]

Across `100` substeps those factors become approximately `1.38e-87` and `1.93e-22`, before other terms. The code also enforces copied-edge Neumann values. This mixed reflecting/absorbing design requires explicit convergence and reflection tests.

### 9.7 Telemetry equations

\[
E=\sum |\psi|^2.
\]

\[
a=\tanh\left(10\frac{E}{32^2}\right).
\]

\[
t_0=\frac{\sum(|\partial_x\psi|^2+|\partial_y\psi|^2)}{E+10^{-6}},
\]

with `+1.5` on command failure, then

\[
t=\tanh(0.2t_0).
\]

\[
v_0=\operatorname{mean}(\phi)-0.2+0.3\operatorname{mean}(\mu)+b_{sentiment},
\]

then

\[
v=\operatorname{clip}_{[-1,1]}[\tanh(1.5v_0)].
\]

Vortices are counted from phase winding around `2 x 2` loops when all four amplitudes exceed `0.005` and absolute winding exceeds `0.8` turns.

These are engineered software observables. Their psychological names are interpretations, not validated biological measurements.

## 10. End-to-end integration audit

### 10.1 Full-state overwrite mechanism

The simulator saves full matrices to the declared state file, then prints only:

- arousal;
- valence;
- tension;
- fatigue;
- vortex count;
- engram summaries;
- active motor summaries.

The primary chat route parses this shortened JSON, adds action-feedback expectations, and writes the shortened object to the same state path. The solver's next load requires `psi_real`, `psi_imag`, `phi`, `mu`, and `kappa`; if any is absent, it reinitialises the state.

```text
full state saved by simulator
        -> shortened telemetry parsed by chat
        -> shortened telemetry replaces state file
        -> next solver load sees missing matrices
        -> loader selects field-state reinitialisation
```

Status: **contract_reproduced**.

### 10.2 Sentiment path is neutralised in primary chat

The primary chat invocation supplies `sentiment = neutral` for ordinary user messages. The solver's loving, positive, critical, negative, urgent, and alarm phase branches are therefore not selected by that path. Tests calling those categories directly demonstrate simulator branch behaviour, not current ordinary-chat behaviour.

### 10.3 Configuration-path mismatch

The solver's default numerical override path is a root-level `limbic_config.json`. That root file is absent at the inspected snapshot. A same-named file exists under a private associative directory but is not the default path, and primary chat does not pass it explicitly.

### 10.4 Conventional memory retrieval remains dominant

The inspected chat route scans text files for words, counts occurrences, boosts selected files with named engram summaries, inserts a small top set into LLM context, and applies direct fixed-coordinate excitation for selected matches.

This is functional conventional retrieval plus LLM prompting. It is not evidence that semantic recall emerges from wave similarity alone.

### 10.5 Existing safer pattern is later in the same chat file

A later state-write stage reloads the fresh full state from disk and merges updated metrics, thoughts, and mood before writing. This demonstrates that the codebase already contains the conceptual pattern needed for preservation. It does not repair the earlier overwrite, and both writes remain direct non-atomic JSON replacements.

## 11. P1A isolated contract reproduction

### 11.1 Question

Does the frozen shortened-telemetry plus whole-file replacement contract preserve the five required field matrices across a chat hand-off?

### 11.2 Synthetic protocol

The audit used only anonymous synthetic data:

- `32 x 32` matrices matching the declared state shape;
- required keys `psi_real`, `psi_imag`, `phi`, `mu`, and `kappa`;
- one generic continuity sentinel and one local marker per trial;
- three deterministic trial identifiers;
- the frozen shortened simulator-output key schema;
- the frozen whole-file chat replacement consequence;
- the frozen loader missing-key predicate;
- a control that merged telemetry into full state instead of replacing it.

No private memory, prompt, relationship, device, deployment, runtime-state, or production-host data was used.

### 11.3 Results

| Path | Trials | Missing required matrices | Loader reinitialisation | Sentinel retained after loader |
|---|---:|---:|---:|---:|
| Current whole-file replacement | `3` | `5/5` every trial | `3/3` | `0/3` |
| Safe merge control | `3` | `0/5` every trial | `0/3` | `3/3` |

The local marker values were `1001`, `1002`, and `1003`. Current replacement lost each marker and the deterministic loader substitute exposed `-1`. Merge control preserved all markers unchanged.

### 11.4 Retained fingerprints

- P1A harness SHA-256: `7f7f811b7da7c1673a45e6e64292bca064da3d4b9e108145e683cfb96dd62f35`
- P1A receipt SHA-256: `0bffccd06e17ecb89e4aa01c56da1b73cd7192c3e5686d43ade607d422df2860`
- P1A verifier SHA-256: `188cae80492cdf8014bf066fddc7942c0c065c64386a3acd89812a5137f0b52e`
- P1A verification-output SHA-256: `b0bdee1c0274a8d106f836c26421c032040f1e2e0cd6df8e39f315d216612126`
- Python: `3.13.5`
- platform: `Linux-6.18.35-x86_64-with-glibc2.41`
- independent conditions checked: `31`

The receipt and verification-output hashes refer to the exact pretty-printed files generated by the embedded code. The display blocks below contain the complete parsed values but may use whitespace-normalised formatting.

### 11.5 Interpretation boundary

Observed:

- frozen extracted whole-file replacement deterministically loses full field state;
- frozen loader predicate then deterministically selects reinitialisation;
- merge control prevents the loss in the tested contract.

Not observed:

- full private application execution;
- numerical field-solver execution by this harness;
- production service;
- Git-to-Prcek parity;
- frequency with which a deployed route executes this exact path.

The conclusion is a reproduced integration-contract defect, not a live-production claim.

## 12. P1A self-contained reproduction package

### 12.1 Reconstruction instructions

Create an empty directory. Copy the block in section 12.2 to `reproduce_chat_state_contract.py` and the block in section 12.5 to `verify_receipt_independently.py`. Then execute:

```bash
python reproduce_chat_state_contract.py > summary.json
python verify_receipt_independently.py > verification_summary.json
sha256sum reproduce_chat_state_contract.py p1a_receipt.json verify_receipt_independently.py verification_summary.json
```

The harness creates `p1a_receipt.json` and disposable per-case state files under `run/`. Its `json.dumps(..., indent=2)` serialization creates the byte-level receipt associated with the listed receipt SHA-256.

### 12.2 Exact executable P1A harness

```python
from __future__ import annotations

import hashlib
import json
import platform
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

GRID_SIZE = 32
REQUIRED_MATRICES = ("psi_real", "psi_imag", "phi", "mu", "kappa")
SOURCE_COMMIT = "f62a2c547675c79a2399a76e2bf82d0d02581298"
SOLVER_BLOB = "9b6149c5afb21b063f9899b0abc59effe5d14232"
CHAT_BLOB = "e5ed4bee60cab29f5653b7640ed90add297a40b1"
SCHEMA = "lina-ei-p1a-chat-state-contract/v1"


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def matrix(value: float) -> list[list[float]]:
    return [[value for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def initial_full_state(seed_id: int) -> dict[str, Any]:
    # Synthetic and privacy-safe. The marker makes continuity loss directly observable.
    psi_real = matrix(0.0)
    psi_real[7][11] = 1000.0 + seed_id
    return {
        "arousal": 0.125,
        "valence": -0.25,
        "tension": 0.375,
        "fatigue": 0.5,
        "vortices": seed_id,
        "last_timestamp": 1_700_000_000.0 + seed_id,
        "psi_real": psi_real,
        "psi_imag": matrix(0.0),
        "phi": matrix(0.1),
        "mu": matrix(0.0),
        "kappa": matrix(1.0),
        "audit_sentinel": f"must-survive-{seed_id}",
        "engrams": {},
        "active_motors": {},
    }


def simulator_stdout_contract(full_state: dict[str, Any]) -> str:
    # Exact public output key contract of the frozen simulator CLI.
    telemetry = {
        "arousal": round(float(full_state["arousal"]), 4),
        "valence": round(float(full_state["valence"]), 4),
        "tension": round(float(full_state["tension"]), 4),
        "fatigue": round(float(full_state["fatigue"]), 4),
        "vortices": int(full_state["vortices"]),
        "engrams": deepcopy(full_state.get("engrams", {})),
        "active_motors": deepcopy(full_state.get("active_motors", {})),
    }
    return json.dumps(telemetry, ensure_ascii=False)


def current_chat_handoff(stdout: str, state_path: Path) -> dict[str, Any]:
    # Exact state-shape consequence of the frozen chat hand-off:
    # parse shortened stdout, add expectations, replace the whole state file.
    limbic_state = json.loads(stdout)
    limbic_state["active_feedback_expectations"] = []
    state_path.write_text(json.dumps(limbic_state, indent=2, ensure_ascii=False), encoding="utf-8")
    return limbic_state


def safe_merge_handoff(stdout: str, state_path: Path) -> dict[str, Any]:
    # Negative control: preserve the full saved state and merge telemetry into it.
    full_state = json.loads(state_path.read_text(encoding="utf-8"))
    telemetry = json.loads(stdout)
    full_state.update(telemetry)
    full_state["active_feedback_expectations"] = []
    state_path.write_text(json.dumps(full_state, indent=2, ensure_ascii=False), encoding="utf-8")
    return full_state


def deterministic_reinitialised_state(seed_id: int) -> dict[str, Any]:
    # Only used to expose the loader branch; no claim is made about the numerical solver.
    return {
        "arousal": 0.0,
        "valence": 0.0,
        "tension": 0.0,
        "fatigue": 0.0,
        "vortices": 0,
        "last_timestamp": 1_800_000_000.0 + seed_id,
        "psi_real": matrix(-1.0),
        "psi_imag": matrix(-1.0),
        "phi": matrix(0.1),
        "mu": matrix(0.0),
        "kappa": matrix(1.0),
        "engrams": {},
        "active_motors": {},
    }


def loader_required_key_contract(state_path: Path, seed_id: int) -> tuple[dict[str, Any], bool]:
    state = json.loads(state_path.read_text(encoding="utf-8"))
    reinitialised = any(key not in state for key in REQUIRED_MATRICES)
    if reinitialised:
        state = deterministic_reinitialised_state(seed_id)
        state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    return state, reinitialised


def matrix_presence(state: dict[str, Any]) -> dict[str, bool]:
    return {key: key in state for key in REQUIRED_MATRICES}


def run_case(root: Path, seed_id: int, handoff_name: str) -> dict[str, Any]:
    state_path = root / f"state-{handoff_name}-{seed_id}.json"
    full_before = initial_full_state(seed_id)
    state_path.write_text(json.dumps(full_before, indent=2, ensure_ascii=False), encoding="utf-8")
    stdout = simulator_stdout_contract(full_before)

    if handoff_name == "current_replace":
        after_handoff = current_chat_handoff(stdout, state_path)
    elif handoff_name == "safe_merge_control":
        after_handoff = safe_merge_handoff(stdout, state_path)
    else:
        raise ValueError(handoff_name)

    missing_after_handoff = [key for key in REQUIRED_MATRICES if key not in after_handoff]
    loaded, reinitialised = loader_required_key_contract(state_path, seed_id)

    return {
        "seed_id": seed_id,
        "handoff": handoff_name,
        "full_state_sha256": digest(full_before),
        "telemetry_sha256": hashlib.sha256(stdout.encode("utf-8")).hexdigest(),
        "post_handoff_sha256": digest(after_handoff),
        "post_loader_sha256": digest(loaded),
        "matrix_presence_before": matrix_presence(full_before),
        "matrix_presence_after_handoff": matrix_presence(after_handoff),
        "missing_required_after_handoff": missing_after_handoff,
        "loader_reinitialised": reinitialised,
        "sentinel_present_after_handoff": "audit_sentinel" in after_handoff,
        "sentinel_present_after_loader": "audit_sentinel" in loaded,
        "marker_after_handoff": (
            after_handoff.get("psi_real", [[None] * GRID_SIZE for _ in range(GRID_SIZE)])[7][11]
            if "psi_real" in after_handoff
            else None
        ),
        "marker_after_loader": loaded["psi_real"][7][11],
    }


def main() -> int:
    root = Path(__file__).resolve().parent / "run"
    root.mkdir(parents=True, exist_ok=True)
    cases = []
    for seed_id in (1, 2, 3):
        cases.append(run_case(root, seed_id, "current_replace"))
        cases.append(run_case(root, seed_id, "safe_merge_control"))

    current = [case for case in cases if case["handoff"] == "current_replace"]
    controls = [case for case in cases if case["handoff"] == "safe_merge_control"]

    assertions = {
        "current_handoff_drops_all_required_matrices": all(
            len(case["missing_required_after_handoff"]) == len(REQUIRED_MATRICES) for case in current
        ),
        "current_handoff_triggers_loader_reinitialisation": all(case["loader_reinitialised"] for case in current),
        "current_handoff_loses_sentinel": all(not case["sentinel_present_after_handoff"] for case in current),
        "safe_merge_preserves_all_required_matrices": all(
            len(case["missing_required_after_handoff"]) == 0 for case in controls
        ),
        "safe_merge_avoids_loader_reinitialisation": all(not case["loader_reinitialised"] for case in controls),
        "safe_merge_preserves_sentinel": all(case["sentinel_present_after_loader"] for case in controls),
    }

    result = "reproduced" if all(assertions.values()) else "unresolved"
    receipt = {
        "schema": SCHEMA,
        "result": result,
        "scope": "isolated extracted state-contract reproduction; not production-host execution",
        "private_source_commit": SOURCE_COMMIT,
        "source_blobs": {"solver": SOLVER_BLOB, "chat": CHAT_BLOB},
        "required_matrix_keys": list(REQUIRED_MATRICES),
        "synthetic_grid_shape": [GRID_SIZE, GRID_SIZE],
        "repetitions_per_handoff": 3,
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "harness_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "assertions": assertions,
        "cases": cases,
        "interpretation": (
            "The frozen shortened telemetry schema plus whole-file chat replacement deterministically removes "
            "all required field matrices. The frozen loader contract then selects reinitialisation. A merge control "
            "preserves the matrices and does not select reinitialisation."
        ),
        "not_established": [
            "production-host parity",
            "deployed-service execution",
            "numerical solver correctness",
            "field usefulness or emergence",
        ],
    }
    receipt_path = Path(__file__).resolve().parent / "p1a_receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "result": result,
        "receipt": str(receipt_path),
        "assertions": assertions,
        "current_missing_counts": [len(c["missing_required_after_handoff"]) for c in current],
        "current_reinitialised": [c["loader_reinitialised"] for c in current],
        "control_missing_counts": [len(c["missing_required_after_handoff"]) for c in controls],
        "control_reinitialised": [c["loader_reinitialised"] for c in controls],
    }, indent=2))
    return 0 if result == "reproduced" else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

### 12.3 Complete captured harness stdout values, whitespace-normalised

The absolute receipt path is environment-specific. Parsing this block yields the same values as the captured stdout; its display whitespace is not the subject of the receipt hash.

```json
{
  "result": "reproduced",
  "receipt": "/mnt/data/lina_p1a_contract/p1a_receipt.json",
  "assertions": {
    "current_handoff_drops_all_required_matrices": true,
    "current_handoff_triggers_loader_reinitialisation": true,
    "current_handoff_loses_sentinel": true,
    "safe_merge_preserves_all_required_matrices": true,
    "safe_merge_avoids_loader_reinitialisation": true,
    "safe_merge_preserves_sentinel": true
  },
  "current_missing_counts": [5, 5, 5],
  "current_reinitialised": [true, true, true],
  "control_missing_counts": [0, 0, 0],
  "control_reinitialised": [false, false, false]
}
```

### 12.4 Complete generated receipt values, whitespace-normalised

The harness in section 12.2 is the byte-level generator. This block contains all receipt keys and values in their generated order but compresses some arrays and objects for readability; therefore the block itself is not asserted to have receipt SHA-256 `0bff...` until regenerated with the harness serialization.

```json
{
  "schema": "lina-ei-p1a-chat-state-contract/v1",
  "result": "reproduced",
  "scope": "isolated extracted state-contract reproduction; not production-host execution",
  "private_source_commit": "f62a2c547675c79a2399a76e2bf82d0d02581298",
  "source_blobs": {
    "solver": "9b6149c5afb21b063f9899b0abc59effe5d14232",
    "chat": "e5ed4bee60cab29f5653b7640ed90add297a40b1"
  },
  "required_matrix_keys": ["psi_real", "psi_imag", "phi", "mu", "kappa"],
  "synthetic_grid_shape": [32, 32],
  "repetitions_per_handoff": 3,
  "python": "3.13.5",
  "platform": "Linux-6.18.35-x86_64-with-glibc2.41",
  "harness_sha256": "7f7f811b7da7c1673a45e6e64292bca064da3d4b9e108145e683cfb96dd62f35",
  "assertions": {
    "current_handoff_drops_all_required_matrices": true,
    "current_handoff_triggers_loader_reinitialisation": true,
    "current_handoff_loses_sentinel": true,
    "safe_merge_preserves_all_required_matrices": true,
    "safe_merge_avoids_loader_reinitialisation": true,
    "safe_merge_preserves_sentinel": true
  },
  "cases": [
    {
      "seed_id": 1,
      "handoff": "current_replace",
      "full_state_sha256": "3dcdbe3d643189f4b2a4a960026c0108dede8f8bca1f56a0f6f3d0e30e652f23",
      "telemetry_sha256": "7d9c7e3294ef7d72e2016a311c045f7de586dca8ba2f502e9f5a85f17339f8ad",
      "post_handoff_sha256": "ff84161e367231f729417ea07f23cb34c7e31a2714c76089377409bb1e1611cb",
      "post_loader_sha256": "00513b44de0f6fc8b83c802e2bcf54d730afe6870050831e9006f245cda2691c",
      "matrix_presence_before": {"psi_real": true, "psi_imag": true, "phi": true, "mu": true, "kappa": true},
      "matrix_presence_after_handoff": {"psi_real": false, "psi_imag": false, "phi": false, "mu": false, "kappa": false},
      "missing_required_after_handoff": ["psi_real", "psi_imag", "phi", "mu", "kappa"],
      "loader_reinitialised": true,
      "sentinel_present_after_handoff": false,
      "sentinel_present_after_loader": false,
      "marker_after_handoff": null,
      "marker_after_loader": -1.0
    },
    {
      "seed_id": 1,
      "handoff": "safe_merge_control",
      "full_state_sha256": "3dcdbe3d643189f4b2a4a960026c0108dede8f8bca1f56a0f6f3d0e30e652f23",
      "telemetry_sha256": "7d9c7e3294ef7d72e2016a311c045f7de586dca8ba2f502e9f5a85f17339f8ad",
      "post_handoff_sha256": "fca47ffa1eae1331a68a31be82bdebd964fa91cbcd89df21200d8c9ccb195383",
      "post_loader_sha256": "fca47ffa1eae1331a68a31be82bdebd964fa91cbcd89df21200d8c9ccb195383",
      "matrix_presence_before": {"psi_real": true, "psi_imag": true, "phi": true, "mu": true, "kappa": true},
      "matrix_presence_after_handoff": {"psi_real": true, "psi_imag": true, "phi": true, "mu": true, "kappa": true},
      "missing_required_after_handoff": [],
      "loader_reinitialised": false,
      "sentinel_present_after_handoff": true,
      "sentinel_present_after_loader": true,
      "marker_after_handoff": 1001.0,
      "marker_after_loader": 1001.0
    },
    {
      "seed_id": 2,
      "handoff": "current_replace",
      "full_state_sha256": "8c75445c540c2c5f25bfa4d6823c2f3b9ba9517455db125d1eae019d08b07215",
      "telemetry_sha256": "38aaac37680a96bb445171efe1783859f5edb51ba99d332ccd890f5bc421205b",
      "post_handoff_sha256": "99f6df871f8e852de9e31fa64353020c76dff235f5b267cfdb2933dc0b79a3e9",
      "post_loader_sha256": "87a5b92ba28c302cbe9020b5b77ae88bdb3da5678481b867bf73673fa4d348b3",
      "matrix_presence_before": {"psi_real": true, "psi_imag": true, "phi": true, "mu": true, "kappa": true},
      "matrix_presence_after_handoff": {"psi_real": false, "psi_imag": false, "phi": false, "mu": false, "kappa": false},
      "missing_required_after_handoff": ["psi_real", "psi_imag", "phi", "mu", "kappa"],
      "loader_reinitialised": true,
      "sentinel_present_after_handoff": false,
      "sentinel_present_after_loader": false,
      "marker_after_handoff": null,
      "marker_after_loader": -1.0
    },
    {
      "seed_id": 2,
      "handoff": "safe_merge_control",
      "full_state_sha256": "8c75445c540c2c5f25bfa4d6823c2f3b9ba9517455db125d1eae019d08b07215",
      "telemetry_sha256": "38aaac37680a96bb445171efe1783859f5edb51ba99d332ccd890f5bc421205b",
      "post_handoff_sha256": "6a3d42bff74e3b95cfb76e578e08dff329a5416861ab38713cd89a49c0bb4043",
      "post_loader_sha256": "6a3d42bff74e3b95cfb76e578e08dff329a5416861ab38713cd89a49c0bb4043",
      "matrix_presence_before": {"psi_real": true, "psi_imag": true, "phi": true, "mu": true, "kappa": true},
      "matrix_presence_after_handoff": {"psi_real": true, "psi_imag": true, "phi": true, "mu": true, "kappa": true},
      "missing_required_after_handoff": [],
      "loader_reinitialised": false,
      "sentinel_present_after_handoff": true,
      "sentinel_present_after_loader": true,
      "marker_after_handoff": 1002.0,
      "marker_after_loader": 1002.0
    },
    {
      "seed_id": 3,
      "handoff": "current_replace",
      "full_state_sha256": "9e9bc95071f2c5f05d7946cbefc21a36ecd310e507578396a18e86be146f5040",
      "telemetry_sha256": "1526cd9c73c69d272a8c2f921d194ea94c5cadb98cd0de54de495d417aa9d7c4",
      "post_handoff_sha256": "1f50614d0a2d92d01224dd1b8e0f7716b952975e3580591330ca2464ce39248e",
      "post_loader_sha256": "3ee8c86956958330a91818eccdae08b7411c31033a578669a423115761eab921",
      "matrix_presence_before": {"psi_real": true, "psi_imag": true, "phi": true, "mu": true, "kappa": true},
      "matrix_presence_after_handoff": {"psi_real": false, "psi_imag": false, "phi": false, "mu": false, "kappa": false},
      "missing_required_after_handoff": ["psi_real", "psi_imag", "phi", "mu", "kappa"],
      "loader_reinitialised": true,
      "sentinel_present_after_handoff": false,
      "sentinel_present_after_loader": false,
      "marker_after_handoff": null,
      "marker_after_loader": -1.0
    },
    {
      "seed_id": 3,
      "handoff": "safe_merge_control",
      "full_state_sha256": "9e9bc95071f2c5f05d7946cbefc21a36ecd310e507578396a18e86be146f5040",
      "telemetry_sha256": "1526cd9c73c69d272a8c2f921d194ea94c5cadb98cd0de54de495d417aa9d7c4",
      "post_handoff_sha256": "deae605e93b4cbe29f78b74cd224289c903fa73fe37e3127ad8effa6ea563f6f",
      "post_loader_sha256": "deae605e93b4cbe29f78b74cd224289c903fa73fe37e3127ad8effa6ea563f6f",
      "matrix_presence_before": {"psi_real": true, "psi_imag": true, "phi": true, "mu": true, "kappa": true},
      "matrix_presence_after_handoff": {"psi_real": true, "psi_imag": true, "phi": true, "mu": true, "kappa": true},
      "missing_required_after_handoff": [],
      "loader_reinitialised": false,
      "sentinel_present_after_handoff": true,
      "sentinel_present_after_loader": true,
      "marker_after_handoff": 1003.0,
      "marker_after_loader": 1003.0
    }
  ],
  "interpretation": "The frozen shortened telemetry schema plus whole-file chat replacement deterministically removes all required field matrices. The frozen loader contract then selects reinitialisation. A merge control preserves the matrices and does not select reinitialisation.",
  "not_established": [
    "production-host parity",
    "deployed-service execution",
    "numerical solver correctness",
    "field usefulness or emergence"
  ]
}
```

### 12.5 Exact independent verifier

```python
from __future__ import annotations

import hashlib
import json
from pathlib import Path

REQUIRED = {"psi_real", "psi_imag", "phi", "mu", "kappa"}
EXPECTED_HARNESS_SHA256 = "7f7f811b7da7c1673a45e6e64292bca064da3d4b9e108145e683cfb96dd62f35"

root = Path(__file__).resolve().parent
receipt_path = root / "p1a_receipt.json"
harness_path = root / "reproduce_chat_state_contract.py"
receipt = json.loads(receipt_path.read_text(encoding="utf-8"))

actual_harness_hash = hashlib.sha256(harness_path.read_bytes()).hexdigest()
assert actual_harness_hash == EXPECTED_HARNESS_SHA256
assert receipt["harness_sha256"] == EXPECTED_HARNESS_SHA256
assert set(receipt["required_matrix_keys"]) == REQUIRED

current = [c for c in receipt["cases"] if c["handoff"] == "current_replace"]
control = [c for c in receipt["cases"] if c["handoff"] == "safe_merge_control"]
assert len(current) == 3 and len(control) == 3

for case in current:
    assert set(case["missing_required_after_handoff"]) == REQUIRED
    assert case["loader_reinitialised"] is True
    assert case["sentinel_present_after_handoff"] is False
    assert case["marker_after_handoff"] is None
    assert case["marker_after_loader"] == -1.0

for case in control:
    assert case["missing_required_after_handoff"] == []
    assert case["loader_reinitialised"] is False
    assert case["sentinel_present_after_loader"] is True
    assert case["marker_after_handoff"] == 1000.0 + case["seed_id"]
    assert case["marker_after_loader"] == 1000.0 + case["seed_id"]

print(json.dumps({
    "verification": "passed",
    "harness_sha256": actual_harness_hash,
    "current_cases": len(current),
    "control_cases": len(control),
    "independent_conditions_checked": 31,
}, indent=2))
```

### 12.6 Complete verifier stdout values

```json
{
  "verification": "passed",
  "harness_sha256": "7f7f811b7da7c1673a45e6e64292bca064da3d4b9e108145e683cfb96dd62f35",
  "current_cases": 3,
  "control_cases": 3,
  "independent_conditions_checked": 31
}
```

## 13. Existing private test and experiment audit

### 13.1 What inspected tests cover

The private suites contain checks for scalar ranges, selected finite values, one execution-time threshold, manually supplied sentiment branches, command-failure tension, clamping, wall-clock decay, mode contrasts, local `kappa` change and decay, sensor gating, boundary excitation, motor discharge, vortex injection, global `kappa` normalisation, optional remote coupling, DNA shapes, dream-labelled behaviour, and NumPy availability.

These are useful regression checks. They were inspected but not run in this checkpoint.

### 13.2 What they do not establish

They do not establish:

- primary chat preservation of full field state;
- behavioural benefit over scalar state;
- learned rather than assigned semantics;
- causal credit of `kappa` for held-out behaviour;
- convergence over timestep, resolution, seed, precision, or boundary mode;
- NumPy/fallback equivalence;
- equivalence to current Lineum Core;
- necessity of dreaming;
- safe autonomous action;
- consciousness or biological equivalence.

Some tests force the pure-Python fallback, which is a scalar behavioural approximation rather than a numerical equivalent of the two-dimensional solver. A decay test requests `alpha = 0`, but the loader clamps it to `0.1`.

### 13.3 Scripted associative-memory experiments

One experiment hand-draws high-conductivity waveguides between predefined concept coordinates. It demonstrates propagation through an engineered channel, not learning.

Another adds a learning-rate multiple of field amplitude to `kappa`, globally min-max normalises, and smooths the grid. It lacks conventional baselines, swaps, held-out generalisation, preregistered metrics, and retained run receipts. It is not evidence of open-ended concept emergence.

## 14. P1B repair preregistration and isolated reference validation

### 14.1 Status

- Private Lina source changed: **no**.
- Private Lina tests executed: **no**.
- Prcek inspected or deployed: **no**.
- Original public-safe reference implementation executed in isolation: **yes**.
- Reference tests: `3 passed in 0.20s`.
- Evidence level: `reference_reproduced`.

Private implementation remains blocked until the repository's current graph, test-first, duplicate-sync, full-suite, and deployment/synchronisation gates can be run in its authorised local environment.

### 14.2 Frozen repair contract

A valid P1B repair must:

1. load the solver-saved full state;
2. refuse to proceed if any required matrix is absent;
3. accept only an explicit telemetry allow-list;
4. prevent telemetry from replacing matrices or arbitrary state keys;
5. preserve unrelated state and continuity sentinels;
6. update feedback expectations;
7. write a temporary file in the same directory;
8. flush and `fsync` it;
9. atomically replace the destination with `os.replace`;
10. leave the old file unchanged on validation or write failure;
11. pass two consecutive hand-offs;
12. be called by the actual primary chat path rather than existing only as unused utility code.

### 14.3 Exact isolated reference implementation

SHA-256: `cbe125243dd6f6c8b4c9e0ba34015f2efbd3734ee334e5b64f2d10455ebaf0bf`

```python
from __future__ import annotations

import json
import os
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterable, Mapping

REQUIRED_MATRICES = ("psi_real", "psi_imag", "phi", "mu", "kappa")
TELEMETRY_KEYS = (
    "arousal",
    "valence",
    "tension",
    "fatigue",
    "vortices",
    "engrams",
    "active_motors",
)


def atomic_write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent)
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    except Exception:
        temporary_path.unlink(missing_ok=True)
        raise


def merge_limbic_telemetry_into_state(
    state_path: Path,
    telemetry: Mapping[str, Any],
    feedback_expectations: Iterable[Mapping[str, Any]],
) -> dict[str, Any]:
    state_path = Path(state_path)
    full_state = json.loads(state_path.read_text(encoding="utf-8"))
    missing = [key for key in REQUIRED_MATRICES if key not in full_state]
    if missing:
        raise ValueError(f"Refusing telemetry merge: missing matrices: {missing}")
    if not isinstance(telemetry, Mapping):
        raise TypeError("Telemetry must be a mapping")

    merged = deepcopy(full_state)
    for key in TELEMETRY_KEYS:
        if key in telemetry:
            merged[key] = deepcopy(telemetry[key])
    merged["active_feedback_expectations"] = [
        deepcopy(item) for item in feedback_expectations
    ]
    atomic_write_json(state_path, merged)
    return merged
```

### 14.4 Exact isolated reference tests

SHA-256: `eecc01afa92e101895987080d9a835238536b6e04955fbb99dc7e496280726a5`

```python
from __future__ import annotations

import json
from pathlib import Path

import pytest

from lina_p1b_reference import REQUIRED_MATRICES, merge_limbic_telemetry_into_state

GRID_SIZE = 32


def matrix(value: float) -> list[list[float]]:
    return [[value for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def full_state() -> dict:
    psi_real = matrix(0.0)
    psi_real[7][11] = 1001.0
    return {
        "psi_real": psi_real,
        "psi_imag": matrix(0.0),
        "phi": matrix(0.1),
        "mu": matrix(0.0),
        "kappa": matrix(1.0),
        "audit_sentinel": "must-survive",
        "arousal": 0.1,
        "valence": 0.2,
        "tension": 0.3,
        "fatigue": 0.4,
        "vortices": 0,
        "engrams": {},
        "active_motors": {},
    }


def write_state(path: Path, state: dict) -> None:
    path.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")


def test_two_consecutive_chat_handoffs_preserve_full_state(tmp_path: Path) -> None:
    state_path = tmp_path / "limbic_state.json"
    write_state(state_path, full_state())

    first = merge_limbic_telemetry_into_state(
        state_path,
        {"arousal": 0.5, "active_motors": {"generic": {"energy": 1.0}}},
        [{"motor_name": "generic"}],
    )
    second = merge_limbic_telemetry_into_state(
        state_path,
        {"arousal": 0.6, "tension": 0.7, "engrams": {"anonymous": 1.1}},
        [],
    )

    persisted = json.loads(state_path.read_text(encoding="utf-8"))
    assert all(key in first and key in second and key in persisted for key in REQUIRED_MATRICES)
    assert persisted["audit_sentinel"] == "must-survive"
    assert persisted["psi_real"][7][11] == 1001.0
    assert persisted["arousal"] == 0.6
    assert persisted["tension"] == 0.7
    assert persisted["active_feedback_expectations"] == []


def test_untrusted_matrix_fields_cannot_replace_solver_state(tmp_path: Path) -> None:
    state_path = tmp_path / "limbic_state.json"
    write_state(state_path, full_state())
    merge_limbic_telemetry_into_state(
        state_path,
        {"psi_real": [[-999.0]], "arousal": 0.9},
        [],
    )
    persisted = json.loads(state_path.read_text(encoding="utf-8"))
    assert persisted["psi_real"][7][11] == 1001.0
    assert persisted["arousal"] == 0.9


def test_malformed_or_incomplete_state_is_not_replaced(tmp_path: Path) -> None:
    state_path = tmp_path / "limbic_state.json"
    incomplete = {"arousal": 0.1, "audit_sentinel": "original"}
    write_state(state_path, incomplete)
    before = state_path.read_bytes()

    with pytest.raises(ValueError):
        merge_limbic_telemetry_into_state(state_path, {"arousal": 0.9}, [])

    assert state_path.read_bytes() == before
```

### 14.5 Exact isolated execution command and output

```bash
python -m py_compile lina_p1b_reference.py test_lina_p1b_reference.py
pytest -q test_lina_p1b_reference.py
```

```text
...                                                                      [100%]
3 passed in 0.20s
```

Environment:

- Python `3.13.5`
- Linux kernel `6.18.35`
- architecture `x86_64`

### 14.6 Interpretation boundary

Actually observed:

- the original allow-listed atomic-merge reference preserved matrices and a marker over two calls;
- an attempted telemetry matrix overwrite did not alter solver matrix state;
- incomplete state caused a validation failure and its bytes remained unchanged;
- all three reference tests passed.

Cautious interpretation:

- this is a viable bounded design candidate for P1B;
- it is stronger than unrestricted `dict.update()` because it has an explicit telemetry allow-list and fail-closed matrix validation.

Not established:

- compatibility with the complete private call graph;
- compatibility with concurrent private writers;
- Windows-specific replace and permission behaviour in the target environment;
- full private-suite success;
- actual primary-chat use;
- Prcek deployment or parity;
- preservation of a numerically evolved perturbation in the real solver.

## 15. Contradiction and numerical-risk ledger

| Finding | Evidence level | Why it matters |
|---|---|---|
| Whole-file chat hand-off drops full matrices and selects loader reinitialisation | contract_reproduced | Long-horizon field memory cannot be evaluated through this contract until repaired |
| Bounded allow-listed atomic merge preserves the synthetic state contract | reference_reproduced | Provides a testable repair candidate, not a private-product fix |
| Primary chat always supplies neutral sentiment | implemented | Several tested sentiment branches are not used by ordinary chat |
| Root numerical override file is absent | implemented/static | Runtime and test configuration paths differ |
| FFT stencil symbol is computed but not used in main diffusion | implemented/static | Selected stencil does not control the actual main Laplacian |
| Main diffusion is a five-point Neumann stencil | implemented | Diagonal/isotropic claims need separate evidence |
| Growth is computed once before both half steps | implemented/static | Formal Strang accuracy is not established |
| Neumann copying and strong PML damping are combined | implemented/static | Reflection and absorption may be resolution-dependent |
| `kappa` is globally renormalised each substep | implemented | Plasticity is not purely local |
| NumPy and fallback paths implement different models | implemented | Fallback success cannot validate the field solver |
| Multiple state writes are direct JSON replacements | implemented | Interrupted/concurrent writes can corrupt state |
| Psychological labels are engineered formulas | implemented | Names are not validated affective observables |

## 16. Operational criteria for stronger emergence

A bounded emergence claim requires:

1. persistent endogenous state across the complete product route;
2. learned representation placement without assigned final coordinates;
3. local plasticity with causal credit and selective intervention effects;
4. decentralised action selection without LLM label selection;
5. open concept growth;
6. held-out generalisation;
7. predicted selective loss under field ablation;
8. robustness across seed, timestep, resolution, boundary, and precision;
9. non-circular preregistered measurement.

Meeting these criteria would support field-mediated organisation within a tested domain. It would not prove consciousness.

## 17. Relationship to Lineum Core

The current Lina solver is independent and does not import released `lineum_core`.

```text
private Lina EI product
        -> private cognition adapter
        -> pinned public Lineum Core contract
```

Public Core must not import private identity, memory, prompts, devices, customer policy, or deployment code.

A future research adapter should expose application-neutral operations to initialise fields, advance by declared timestep, inject generic sources, return declared observables, serialise/restore versioned state, and emit seeds, parameters, boundaries, source fingerprints, and hashes.

The legacy contract must first be stable and covered by known-answer tests.

## 18. Revised research programme

### P1A — Chat-state contradiction

**Status:** complete at `contract_reproduced` level. Full reproduction code and complete output values are embedded in this audit; byte-level receipt regeneration is defined by the embedded serialization code.

### P1B — Preserve full state

**Status:** repair contract and isolated reference frozen; private implementation pending.

Required private-product sequence:

1. run current `graphitlive` and inspect direct and transitive dependants;
2. add a failing two-turn regression before production code;
3. introduce a bounded allow-listed atomic state merge at the graph-approved location;
4. route actual primary chat through it;
5. retain pre-fix failure and post-fix pass;
6. test malformed telemetry and interrupted writes;
7. run focused tests and full `pytest -q`;
8. run duplicate-sync guard;
9. verify official Git/Prcek synchronisation procedure before deployment;
10. update this same audit with exact private commit, commands, outputs, and interpretation boundary.

### P1C — Frozen numerical baseline

After P1B, retain dependency versions, fixed seed, active parameters, initial/final hashes, per-step energy and extrema, finite checks, `kappa` sum, runtime, environment receipt, and one independent toy calculation.

### P2 — Numerical validity

Test timestep, resolution, seed, boundary, reflection, damping, clipping frequency, and sensitivity to global `kappa` normalisation.

### P3 — Causal field ablation

Compare full field, frozen field, shuffled field, scalar replacement, random control, and LLM plus ordinary memory only.

### P4 — Learned anonymous categories

Use anonymous labels, random initial locations, label swaps, held-out examples, and generic readouts.

### P5 — Core-adapter equivalence

After the legacy contract is stable, compare it with a research-only Core-backed adapter.

## 19. Public-safe investor and monetisation assessment

Plausible categories remain privacy-first local personal agents, embodied home/workspace agents with reversible action limits, persistent-agent runtime, hybrid field/LLM research platform, and private deployment where local state ownership matters.

The strongest defensible differentiator would be measured continuity and adaptation from an inspectable local dynamical substrate, not a consciousness claim.

Current blockers include the broken frozen chat-state contract, unmeasured causal benefit, hand-authored semantics, missing convergence and ablation evidence, no pinned Core adapter, absent compute/latency/privacy/unit-economics benchmarks, no validated first customer problem, and privacy/security/emotional-reliance risks.

Detailed pricing, forecasts, market sizing, go-to-market strategy, investor targeting, and IP decisions belong in private Lineum Dynamics records, not public Core.

## 20. Prohibited near-term claims

Current evidence does not support marketing Lina EI as conscious, sentient, biologically equivalent to a brain, AGI, therapist, psychiatrist, diagnostic system, medical device, safety-critical controller, validated proof that Lineum produces cognition, or production/investor validated.

Biological labels may remain interface metaphors only when accompanied by exact operational observables.

## 21. Privacy and security boundary

This report excludes personal identities, birthdays, relationships, histories, conversations, diaries, private prompts, persona instructions, exact devices, household layout, addresses, IPs, ports, hostnames, credentials, provider identifiers, private semantic coordinate maps, exploitation instructions, and confidential commercial strategy.

Public receipts use generic labels, aggregate metrics, hashes, and synthetic configurations.

## 22. External scientific context

Relevant external research can motivate tests of online adaptation, feedback, local interaction, persistent state, and on-device execution. It does not validate Lina EI by analogy.

Reference points:

- Mackenzie Weygandt Mathis, “Leveraging insights from neuroscience to build adaptive artificial intelligence,” *Nature Neuroscience* (2026), https://www.nature.com/articles/s41593-025-02169-w.
- Nguyen et al., “A Survey on Small Language Models,” RANLP 2025, https://aclanthology.org/2025.ranlp-1.93/.
- Qian et al., “Mapping the Parasocial AI Market: User Trends, Engagement and Risks,” arXiv:2507.14226 (2025), https://arxiv.org/abs/2507.14226.
- “Large-scale-integration and collective oscillations of 2D artificial cells,” *Nature Communications* (2024), https://www.nature.com/articles/s41467-024-54098-0.
- “Programming gel automata shapes using DNA instructions,” *Nature Communications* (2024), https://www.nature.com/articles/s41467-024-51198-9.

Distributed physical pattern formation is not evidence of cognition. Lina variables are engineered software quantities whose cognitive interpretation remains under test.

## 23. Decision ledger

| Decision | Status |
|---|---|
| Keep one canonical audit only | required and satisfied |
| Treat Lina as a hybrid persistent-agent research prototype | supported at architecture level |
| Treat standalone solver as capable of saving full fields | implemented |
| Treat frozen whole-file chat replacement as preserving fields | rejected by contract reproduction |
| Treat isolated bounded atomic merge as a viable repair candidate | supported at reference level |
| Treat private Lina as repaired | unsupported |
| Treat defect as confirmed in deployed production | unsupported |
| Claim full emergence | unsupported |
| Claim consciousness | prohibited |
| Describe current grid as Lineum-inspired | supported |
| Describe current runtime as using Lineum Core | unsupported |
| Repair persistence before long-horizon field tests | selected next gate |
| Build private adapter consuming pinned Core contract | retained after legacy stabilisation |
| Publish private code, memories, devices, or commercial strategy in Core | rejected |
| Continue public-safe isolated research without Prcek parity | selected for this checkpoint |

## 24. Claims explicitly not established

This report does not establish that:

- Git exactly matches production;
- the private test suite currently passes;
- the full private application has reproduced the reset under an isolated checkout;
- the private Lina source contains the reference repair;
- the deployed service executes the frozen hand-off unchanged;
- the current solver is stable or convergent;
- field dynamics are necessary for useful behaviour;
- semantic meaning emerges from the grid;
- `kappa` performs biologically meaningful learning;
- dreaming improves memory or generalisation;
- fallback equals NumPy solver;
- Lineum Core reproduces the current Lina solver;
- autonomous actions are secure or reliable;
- any business model is profitable or investable;
- Lina is alive, conscious, sentient, or biologically equivalent;
- Lineum describes cognition in nature.

## 25. Exact next checkpoint

The next coherent checkpoint is **P1B private test-first implementation** in an authorised local Lina environment:

- obtain current graph evidence;
- add the failing two-turn test;
- apply the smallest graph-consistent atomic merge;
- run focused and full private tests;
- preserve before/after evidence;
- verify official synchronisation gates;
- append all exact results to this same audit.

Until those gates are available, the scientifically valid stopping point is the frozen and independently testable repair contract above. No whitepaper, public product claim, or investor claim should be changed from this report alone.

## 26. Checkpoint receipt

- Canonical research artefacts: exactly one, this Markdown audit.
- Core branch before revision: `develop` at `624add68d2fcf4d8c1879fb4b2f351cfb35ba694`.
- Private source commit: `f62a2c547675c79a2399a76e2bf82d0d02581298`.
- Production-host access: deliberately deferred.
- Full private application executed: no.
- Private source modified: no.
- Private test suite executed: no.
- P1A synthetic trials: `6` total.
- P1A independent conditions: `31`.
- P1A result: all five matrices lost and reinitialisation selected in `3/3` replacement trials; all matrices preserved in `3/3` merge controls.
- P1A JSON blocks: complete parsed values, whitespace-normalised for display; exact receipt bytes are generated by embedded harness.
- P1B original reference tests: `3/3` passed in `0.20s`.
- P1B reference implementation SHA-256: `cbe125243dd6f6c8b4c9e0ba34015f2efbd3734ee334e5b64f2d10455ebaf0bf`.
- P1B reference tests SHA-256: `eecc01afa92e101895987080d9a835238536b6e04955fbb99dc7e496280726a5`.
- Personal or secret data retained: none intentionally.
- General evidence level: `implemented/static audit`.
- State-loss mechanism: `contract_reproduced`.
- Repair design: `reference_reproduced`.
- Principal negative result: frozen whole-file chat hand-off cannot preserve required field state.
- Principal next discriminator: failing pre-fix and passing post-fix two-turn integration tests in the private product environment.
