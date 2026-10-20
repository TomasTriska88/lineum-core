# Lineum Collision Dynamics: Evidence Reconciliation and Reproducible Test Design

**Status:** active — intake and protocol-recovery stage  
**Report version:** 0.1.0  
**Evidence cutoff:** 2026-10-20  
**Research scope:** controlled interactions of localized topological excitations in Lineum, with explicit separation between the canonical Eq-4/v1 implementation and historical or experimental Eq-7/Eq-11.1 variants  
**Confidence in any collision-mechanism claim:** low / unresolved  
**Canonical audit status:** blocked; this programme is not a canonical audit and must not be represented as one

## 1. Purpose and decision

The immediate question is not whether Lineum particles behave like particles in nature. It is narrower and testable:

> Given a reproducibly initialized, individually validated localized topological excitation in a precisely pinned Lineum implementation, what changes when a second excitation approaches it, compared with matched isolated-excitation controls?

The experiment must distinguish (a) numerical or observer artifacts, (b) ordinary linear wave interference, (c) interaction mediated by the model's coupled fields, and (d) genuine persistence, scattering, fragmentation, or loss of localized topological structure within that specific model variant.

A visually compelling collision is not evidence by itself. Nor can a result from the experimental Torch/FFT wave path be transferred to the canonical Eq-4 contract path without a direct comparison. No claim about actual physical particles, antimatter, quantum-field scattering, gravity, or the Standard Model follows from this numerical experiment.

This file is a live research notebook, not a whitepaper amendment. No claim may be promoted to the canonical core whitepaper from this report until its protocol, code identity, outputs, controls, and independent checks pass the separate evidence-promotion gate.

## 2. Report lineage and root-programme status

The repository's mandatory `.agent/continuous-research-reporting.md` requires one continuously maintained standalone research report per decision chain and requires a child report to declare its master report and full lineage. The repository-boundary rules also require experiment-specific code to remain outside the installable `lineum_core/` package.

The following likely report paths were checked on branch `develop` and were not found: `research/README.md`, `research/index.md`, `research/lineum-master-report.md`, `research/eq4-canonical-research.md`, and `research/eq11-collision-dynamics.md`. A directory called `research` exists, but the currently exposed repository tools do not provide an exhaustive directory listing. **Therefore the root-report inventory is incomplete.** This report is provisionally being used as the working root for the collision-dynamics decision chain until a complete inventory can establish whether it must instead inherit from an existing master. No new consequential experiment is authorized while that lineage question remains unresolved.

This is a correction to the work chronology: two exploratory local runs were executed before a permanent report and frozen harness had been committed. That was out of order under the required research protocol. Both attempts are explicitly classified below as exploratory and provenance-defective; they cannot support a scientific verdict.

### Reported source locations

- Current development-branch core step implementation: `lineum_core/math.py`, Git blob SHA-1 `bb877021810691223a0eb960a45493a2e351112a` on `develop`.
- Current development-branch canonical/contract paper: `whitepapers/1-core/01-core-lineum.md`, blob SHA-1 `edc63b0d150b3b616ff8a108ea47a4f89b6a6c37`.
- Equation-history document: `whitepapers/1-core/02-core-equation.md`, blob SHA-1 `64f8341551d5737a6eb4919030bbb85a4b50380c`.
- Canonical audit gate: `.agent/workflows/audit.md`, blob SHA-1 `69777ecc68449b4c16799d0fa03f56dadaf5b939`.
- Research-reporting protocol: `.agent/continuous-research-reporting.md`, blob SHA-1 `54c0f02068d30900291ac605aa9b29becffa6ae1`.
- Library-boundary protocol: `docs/repository-boundaries.md`, blob SHA-1 `05b805c16c68b52c8618c564f9155e9cef913254`.

The audit workflow still states **BLOCKED** as of 2026-10-20. See [Issue #7](https://github.com/TomasTriska88/lineum-core/issues/7). This collision programme may perform only clearly identified exploratory research under a pinned noncanonical or historical variant until the actual executable path is reconciled. Do not run a new canonical audit or use an old false-green suite report to authorize one.

## 3. Existing claims and contradictions to reconcile

### 3.1 Canonical Eq-4 / core-v1 narrative

The current core whitepaper describes the primary collision question as open and says the half-collinear / wave-breaking-to-φ idea is a hypothesis that is not contract-validated. The same paper's later history sections describe other experiments:

- Phase 8 reports failure of non-topological Gaussian/wave-packet collisions to form stable composite modes spontaneously.
- Phase 9 reports noise-assisted defect nucleation from smooth-wave zero-crossings under a particular experimental setup, absent in the noise-disabled control.
- Phase 10 reports that any later composite formation is a multi-step post-collision process rather than an instantaneous collision product.
- Another section reports fragmentation when two *already established and spatially confined stable modes* approach each other.

These scenarios are not interchangeable. In particular, (i) smooth wave packets without pre-existing winding, (ii) a pair of initially validated vortices, and (iii) two already stabilized composite modes are different initial-value problems. Textual summary alone does not establish which exact code, profile, parameter values, source commit, and raw output produced each claimed result.

### 3.2 Experimental Eq-7 / Eq-11.1 narrative

The equation-history document contains a separate family of wave/core experiments. It reports predominantly repulsive scattering for several isolated-vacuum Eq-11.1 regimes, failure of generic spontaneous binding, and some candidate oscillatory-bound-pair outcomes when an external phase lock, spatial confinement, or other engineered condition was added. It also records prior candidate mechanisms later classified as extrinsic or artifacts of forced geometry.

These claims should not be silently merged with the canonical Eq-4 findings. The report needs one explicit variant ledger and exact source/output receipts per family. At present their exact executable runners and complete experiment artifacts have not been reconstructed in this report.

### 3.3 Older ontological claims

The draft `whitepapers/2-cosmology/hypotheses/30-cosmo-hyp-lineum-vs-standard-model.md` presents a (+1/-1) vortex annihilation narrative. It is draft/interpretive material, not a sufficient record of verified canonical collision behaviour. It cannot be treated as independent evidence merely because it states an expected outcome.

The vortex-coupling draft `whitepapers/2-cosmology/hypotheses/29-cosmo-hyp-vortex-particle-coupling.md` explicitly describes its starting patterns as visual observations requiring quantitative replication and is marked draft. Its older μ interpretation also requires reconciliation against the current implementation before it can guide a current-core claim.

### 3.4 Known observer-artifact warning

The project backlog records a prior 1000-seed search in which an alleged stable-attractor radius turned out to equal the grid's mean radial distance and the apparent topological count was consistent with random phase defects in a global noise bath. The tracked object was an artifact of a global geometric statistic. This is a direct reason to require persistent, amplitude-supported, independently checked cores rather than interpreting a radius, raw winding count, or attractive plot as a particle.

## 4. Implementation distinctions

The current `lineum_core/math.py` has materially distinct paths:

1. **NumPy / default diffusion path.** The default `CoreConfig.physics_mode_psi` is `"diffusion"`. The NumPy branch applies diffusion and a fixed `0.005` linear damping term, and by default can inject probabilistic new excitations and scalar noise. Setting `disable_quantum_noise=True` disables those two stochastic/excitation additions but does not turn the NumPy implementation into the separate FFT wave solver.
2. **PyTorch / explicit wave path.** When the configured `physics_mode_psi` string contains `"wave"`, the Torch branch performs an FFT-based propagation step. This is an explicit implementation path, not proof of the canonical Eq-4 profile. Its boundary/PML, phase and amplitude behavior must be pinned as part of the exact run definition.
3. **Historical Eq-7 / Eq-11.1 variants.** The equation history documents distinct update equations and experimental stabilizers. A result from one of these variants cannot validate a different one.

The canonical audit workflow also prohibits direct unsupported canonical launches while the audit gate is blocked. This experiment must not bypass that gate by calling the canonical runner with an improvised token or by changing the expected identity.

## 5. Chronology of the 2026-10-20 exploratory attempts

Both attempts were local, small-scale methodological probes, not approved experiment runs. The complete repository was not checked out into the local execution environment; portions of the current source were extracted into scratch copies, and the run harnesses had not been frozen in a repository commit before execution. This makes their provenance defective and prevents source equivalence from being independently verified.

### Attempt A — NumPy diffusion path

- **Intent:** See whether the proposed paired initial fields actually approached one another before designing collision metrics.
- **Custom setup:** 128×128 grid, periodic wrapping through `np.roll`, κ=0.5, stated amplitude scale 1, carrier (k_x=0.22), packet centers (x=40) and (x=88), 600 steps, quantum-noise/excitation additions disabled, mode coupling enabled, μ disabled.
- **Observed in the local custom run:** single-packet (sum |ψ|^2) decreased from about 78.53982 to 0.05321098; peak amplitude decreased from about 0.60653 to 0.01818. The pair likewise rapidly decayed and did not demonstrate opposing x-motion.
- **Classification:** **Methodological invalidity / no collision occurred.** This is not evidence against collision dynamics. It does establish that this chosen diffuse-path test cannot answer the intended question.
- **Consequence:** Do not continue tuning packet amplitude in this path. The next admissible setup must use a documented propagation mode and establish single-packet motion first.

### Attempt B — locally ported Torch/FFT wave path

- **Intent:** Verify that an explicit wave path could provide propagation and a useful isolated-control comparison on a smaller grid.
- **Custom setup:** manually ported step logic from the current Torch wave branch; 64×64 grid; 500 steps; κ=0.5; amplitude scale 1; carrier (k_x=0.65); initial centers (x=18) and (x=46), (y=32); periodic wrapping; PML disabled; noise/excitation injection disabled; isolated single-packet, equal-charge pair, opposite-charge pair and π-offset pair cases; linear-like control and coupled-field variants.
- **Tool environment:** Python, PyTorch 2.10.0+cpu, NumPy 2.3.5, SciPy 1.17; CUDA unavailable. The full repository package and its complete supported dependency environment were not run.
- **Control result:** in the *custom port*, the linear-control paired trajectory matched the sum of the isolated trajectories at stored checkpoints with a reported residual of zero; (sum |ψ|^2) remained around 100.5309548667. This is a check of the custom implementation, **not** a validated result for the repository package.
- **Coupled cases:** the local custom outputs showed non-zero φ accumulation and departure from the sum of isolated ψ trajectories. These observations are not admissible as collision evidence because the initial fields and observer failed the preconditions below.
- **Critical initial-condition defect:** a single charged vortex was put on a periodic torus without constructing a globally consistent charge-compensated/periodized state. The winding is forced to resolve at a low-amplitude seam, implicitly introducing a hidden compensating defect or discontinuity. It is not a clean isolated linon on this domain.
- **Critical observer defect:** a simple phase-winding detector used an amplitude gate and did not reliably identify the hidden seam charge in the initial frame; as the field spread, its raw defect counts could jump. Therefore counts cannot be interpreted as annihilation, fragmentation, or particle creation.
- **Additional limitations:** the packet was synthetically initialized rather than taken from a source-pinned, independently validated stable linon state; the port had not been committed before execution; the current Core package and the copied step were not independently compared; no full repository tests were run.
- **Classification:** **Methodological invalidity / inconclusive.** It is not a scientific negative, it does not prove or disprove interaction, and its numerical values must not be quoted as project findings.
- **Consequence:** Retain only the methodological lessons in this report. Do not use the local raw counts or φ changes to tune the physical model or to make an ontological claim. Any official repeat must start from a committed protocol/harness and use a domain-compatible initial state.

## 6. Formal question and preregistration requirements

The experiment is **not yet ready to execute**. Before any new consequential simulation, the following inputs must be recovered and pinned.

### 6.1 Preconditions

1. Locate the historical scripts, parameter sets, commit IDs, initial states/checkpoints, and raw outputs associated with the documented Phase 8–20 collision families, where present. Match every result to a particular equation family.
2. Recover a reproducible single-linon state from the selected engine variant. It must be shown to persist under an isolated baseline long enough to complete the intended encounter, and it must include the exact field arrays or an analytic initialization recipe whose implementation is pinned.
3. Respect the domain's topology. A single nonzero winding on a periodic two-dimensional torus is not an acceptable isolated-charge initial condition unless the setup explicitly includes a compensating charge or a rigorously periodized construction. If the selected physics requires a non-periodic domain, declare and justify that boundary instead of quietly mixing boundary regimes.
4. Compare the committed runner against the exact imported source. No manually copied step may be called “the Core implementation” until source equivalence has been shown.
5. Freeze and commit the protocol, code, dependency state, identity, observer, thresholds and controls before the run. Mark the run exploratory if the canonical audit gate or exact execution prerequisites remain unavailable.

### 6.2 Primary hypothesis

**H1 — interaction beyond linear superposition:** for a pinned nonlinear/coupled engine variant and two valid, independently persistent incoming structures, the measured paired evolution will differ from the summed independent evolution by more than the established numerical/control uncertainty in at least one preregistered field observable. This alone establishes only a model interaction, not binding, annihilation, or particle identity.

### 6.3 Separately testable outcome hypotheses

- **H2 — localized-core persistence:** after encounter, one or more valid topological cores persist above the preregistered amplitude and continuity criteria.
- **H3 — topological charge change:** the validated local winding content changes during encounter in a way consistent with the declared domain and boundary charge balance; raw detector counts alone are insufficient.
- **H4 — energy/field transfer:** the ψ/φ changes exceed the isolated and linear-control differences, with the actual conservation/non-conservation law for that variant written explicitly.
- **H5 — phase sensitivity:** changing only the relative phase shifts a preregistered metric in a reproducible way across the declared repeat/seed set.
- **H6 — fragmentation versus scattering:** the trajectory separates into many validated, persistent cores or into diffuse field structure, not just a transient cloud of threshold crossings.

These are hypotheses to be tested, not assumptions that must come true. No outcome is currently selected as “expected truth.”

### 6.4 Minimum control families

When the valid initial state and selected model are established, the frozen design must include:

- left structure alone;
- right structure alone with identical background and duration;
- both structures together;
- linear or uncoupled superposition control using the same initial fields;
- an initial-separation/no-encounter control;
- matched phase variants if phase sensitivity is in scope;
- numerical refinement or alternate stencil/boundary comparison appropriate to that variant;
- a deterministic replay check and a separate seed ensemble if stochastic sources remain enabled.

The number of seeds/repeats, time span, tolerances and exact parameter values are **not assigned yet**, because they depend on the recoverable initial condition and the selected, source-pinned variant. Inventing those numbers now would falsely suggest the test was preregistered.

### 6.5 Observer and falsification rules

The permanent observer must report at least:

- ψ amplitude and energy-like norm maps over time;
- φ field, change in field total, and near-core profile;
- local winding number per plaquette with a documented amplitude mask and periodic-neighbor convention;
- globally summed winding/charge-balance checks appropriate to the declared boundary;
- spatial trajectories and continuity/persistence of each tracked core;
- core amplitude/radius plus threshold-sensitivity analysis;
- maximum amplitude, NaN/Inf flags, cap/fold triggers, and timestep/domain identity;
- deviations from the sum of isolated trajectories, compared with the same measure on the linear-control case;
- hashes for source snapshot, run config, input state, raw outputs and observer.

Pre-register all amplitude gates, tracking radius, minimum persistence, and charge acceptance before examining paired-run results. If the verdict changes under small, defensible detector-threshold or grid changes, classify it as observer-/discretization-sensitive and inconclusive unless a stronger validated measure resolves it.

Possible outcomes and their implications must be declared before the run:

- No valid incoming pair / no actual approach: setup failure; no collision verdict.
- Paired evolution matches isolated linear control within tolerance: no resolved nonlinear interaction for that setup; do not generalize outside it.
- Significant paired-control difference but invalid or untracked cores: a field interaction was observed, but linon-specific interpretation remains unresolved.
- Robust core scattering or persistence across controls/refinements: bounded support for the specific outcome in the tested model only.
- Detector/boundary/step-size dependence, numerical overflow, or unresolved charge imbalance: invalid/inconclusive until corrected.
- Any absence of spontaneous binding in one setup does not prove universal impossibility; any one successful configuration does not prove universality.

## 7. Variant and whole-program impact ledger

| Programme/variant | Relation to current collision question | Status and impact |
|---|---|---|
| Canonical Eq-4 / v1, static κ, 2D, periodic boundary | Current audit-anchored reference family | **constrains**: audit is blocked; cannot call a new canonical run or promote claims yet |
| Current default NumPy diffusion path | Separate runtime path with fixed damping and optional noise/excitation injection | **constrains**: Attempt A is an invalid no-collision setup; do not use to judge wave-packet collision |
| Current explicit Torch/FFT wave path | Experimental propagation path, noncanonical unless contract says otherwise | **not_yet_compared** to canonical Eq-4 output and historical runs |
| Historical Eq-7 / Eq-11.1 open-vacuum collision claims | Separate equation families and boundary assumptions | **not_yet_compared**: recover source, parameter, initial state, raw data and chronology before treating as reproducible evidence |
| Claimed smooth-wave noise-assisted defect nucleation (Phase 9) | Different initial condition and stochastic regime from two pre-existing linons | **not_yet_compared**; it does not answer two-linon scattering directly |
| Claimed fragmentation of two already stabilized composite modes | Different N-body/boundary initial condition from two isolated elementary cores | **not_yet_compared**; keep as separate family |
| Draft (+1/-1) annihilation-to-radiation narrative | Interpretive hypothesis, not sufficient evidence | **constrains**: requires targeted reproduction; not validated |
| Historical radius/topology observer falsification from 1000-seed scan | Prior example of a grid/threshold artifact | **constrains** all observer design and prohibits global radius/count-only verdicts |
| Audit issue #7 | Canonical audit infrastructure | **unaffected** by exploratory collision research; must be tracked separately and remain blocked |

## 8. Current verdict

**No admissible scientific conclusion about a two-linon collision has been established by the 2026-10-20 exploratory attempts.** The first run did not produce a collision; the second used an inadmissible periodic single-charge initial condition and an unverified copied step, with a detector that missed the associated boundary/topology defect. These are methodology/setup failures, not scientific negatives.

A durable methodological lesson is established: a visually plausible vortex on a periodic grid is not sufficient to define a valid isolated linon, and a raw phase-winding count does not prove that a core survived or annihilated. The selected starting state, boundary topology, solver path and observer must be validated as one package.

## 9. Next concrete step — no new collision simulation yet

1. Complete the `research/` directory and lineage inventory and determine whether this file must inherit from an existing root/master report.
2. Search current `develop` history for the exact implementation and source artifacts behind Phase 8–20 and earlier collision claims. Retrieve relevant files by commit/path, not only by default-branch code-search snippets.
3. For each recovered result, record source commit/blob, equation family, parameter identity, initialization procedure or state, boundary scheme, command, output inventory and hashes. If code/data cannot be recovered, label the narrative claim `unreproduced / provenance missing`, not false and not verified.
4. Select exactly one variant for the next admissible replication and write down why it has the highest discriminating value across the whole programme.
5. Freeze the standalone protocol, runner and tests in a repository checkpoint before the new run. Do not use GitHub Actions as an execution workaround. Do not change canonical run output or bypass the audit gate.

Only after these steps should the first preregistered collision protocol be finalized and executed.

## 10. References

- Current core source on `develop`: [`lineum_core/math.py`](https://github.com/TomasTriska88/lineum-core/blob/develop/lineum_core/math.py)
- Current core v1 paper on `develop`: [`whitepapers/1-core/01-core-lineum.md`](https://github.com/TomasTriska88/lineum-core/blob/develop/whitepapers/1-core/01-core-lineum.md)
- Equation and variant history: [`whitepapers/1-core/02-core-equation.md`](https://github.com/TomasTriska88/lineum-core/blob/develop/whitepapers/1-core/02-core-equation.md)
- Audit gate: [`.agent/workflows/audit.md`](https://github.com/TomasTriska88/lineum-core/blob/develop/.agent/workflows/audit.md)
- Research reporting rules: [`.agent/continuous-research-reporting.md`](https://github.com/TomasTriska88/lineum-core/blob/develop/.agent/continuous-research-reporting.md)
- Repository boundary and research-code placement: [`docs/repository-boundaries.md`](https://github.com/TomasTriska88/lineum-core/blob/develop/docs/repository-boundaries.md)
- Canonical audit bug tracker: [Issue #7](https://github.com/TomasTriska88/lineum-core/issues/7)
