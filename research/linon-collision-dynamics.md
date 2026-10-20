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


## 11. Append-only chronology correction — exploratory Attempt C (2026-10-20)

**This section was added after discovering the already-existing report. It does not erase or rewrite Sections 5–9 as they stood before this attempt.** An additional small control pilot had been run in the local scratch workspace before this active report and the mandatory continuous-reporting protocol were re-read during this session. That was out of order: the runner was not committed before execution, the report's root/lineage inventory was unresolved, and no full Core checkout or supported full-package test environment was used. This attempt is therefore **exploratory and provenance-defective**, not an admissible scientific collision result. The act of recording it now preserves the chronology but does not retroactively preregister it.

### Setup and exact provenance

- Inspected source: lineum_core/math.py on develop, blob SHA-1 bb877021810691223a0eb960a45493a2e351112a.
- Runner: manually transcribed narrow PyTorch wave-baseline extraction, saved locally as linon_collision_reference.py; SHA-256 1ce34d01255fb85124a2d240d4cbba7cc617fba1fe163883af2a363789017ab8. The complete exact runner is embedded below so scratch is not its only remaining location.
- Execution: Python 3.13.5, NumPy 2.3.5, PyTorch 2.10.0+cpu, one CPU thread; CUDA unavailable.
- Run: 64×64 periodic FFT grid, 500 steps, κ=0.5, σ=4, amplitude=1, |kx|=0.65, centers (18,32) and (46,32), dt=1.0.
- Isolation settings: stochastic births and noise disabled, μ disabled, PML disabled, κ projection disabled; linear-null branch also disables drift, mode coupling and φ diffusion.
- The executable was run twice after it was written and produced byte-identical pilot_summary.json output. Output SHA-256 f820ac1becf88b8a6121e437f7da73757ddde850370857753fec6994b2ee82c5. This is repeatability of the frozen scratch script only; it is not a source-equivalence receipt for the complete Core package and not a canonical audit pass.

### Key retained values from the exploratory output

| Pair compared with two separate single runs | Step 250 Dψ | Step 250 Dφ | Step 500 Dψ | Step 500 Dφ |
|---|---:|---:|---:|---:|
| Linear null, coupling disabled | 0.000000000 | 0.000000000 | 0.000000000 | 0.000000000 |
| Coupled head-on, same winding | 0.019984462 | 0.260561202 | 0.066143049 | 0.217274397 |
| Coupled same-direction control | 0.001393244 | 0.004353925 | 0.030015124 | 0.024252283 |
| Coupled head-on, opposite winding | 0.020357385 | 0.281097338 | 0.069987862 | 0.255194651 |
| Opposite winding with π phase offset | 0.020287424 | 0.281074608 | 0.070022770 | 0.255101974 |

At step 250, the same-winding head-on residual is about 14.3 times the same-direction control for ψ and 59.8 times for φ. By step 500 those ratios are about 2.2 and 9.0. For the same-winding head-on pair, the absolute difference in total |ψ|² from summed single runs was 2.791878850 at step 250 and 11.159424814 at step 500; the difference in sum(φ) was 0.062417594 and 0.999429962 respectively. These values do not establish a physical energy conversion law or a stable-linon collision.

### Observer limitation reinforced

For a single imposed packet, the amplitude-gated phase-winding observer reports one vortex at step 0; zero at steps 10 and 25; one again through much of steps 50–200; zero at step 225; one at step 250; zero at step 275; one at steps 300–400; and two at steps 450–500. Meanwhile the intensity-weighted circular centre moves smoothly. The observer therefore loses and regains detected winding while the packet's intensity trace continues moving. This is a limitation of the measurement under this imposed initial condition, not a falsification of Lineum collision dynamics. The periodic torus and amplitude gate also mean the apparent lone charge is not a demonstrated globally isolated defect.

### Scope and decision impact

The result shows that this narrow coupled numerical extraction is non-additive around the encounter window and that the linear null is additive at stored checkpoints. The same-direction control also becomes nonzero later, so this is not proof that every paired difference is caused exclusively by collision. The packet initial states are analytic, imposed states—not persistent linons recovered from the actual Core solver. Consequently this attempt adds no admissible scientific verdict, must not be used for parameter tuning, and cannot be transferred to canonical Eq-4/v1 or real-world particle physics.

The previously recorded Section 9 rule remains binding: **no further consequential simulation is authorized until the complete research-report lineage is reconciled, prior Phase 8–20 claims are retrieved, and a protocol plus runner are frozen and committed before execution.** The root-report inventory remains incomplete because the available repository tools do not expose an exhaustive research-directory listing.

### Complete frozen scratch runner used by Attempt C

The code below is preserved verbatim from the scratch runner. Saving the code into this report does not retroactively make the earlier run preregistered or admissible. To reproduce only this historical pilot, save it as linon_collision_reference.py and run python linon_collision_reference.py with compatible NumPy and PyTorch CPU.

```python
"""Exploratory interaction pilot: frozen narrow extraction of Lineum's Torch wave branch.
Source: lineum_core/math.py, Git blob bb877021810691223a0eb960a45493a2e351112a.
Not a full Core checkout; only the inspected wave_baseline path/config is represented.
"""
from __future__ import annotations
import json, time
from pathlib import Path
import numpy as np
import torch

N, T, KAPPA, SIGMA, AMP, KX, Y0, XL, XR = 64, 500, 0.5, 4.0, 1.0, 0.65, 32.0, 18.0, 46.0
CHECKS={0,1,10,25,50,100,150,200,225,250,275,300,350,400,450,500}
torch.set_num_threads(1)
y,x=np.mgrid[0:N,0:N]

def packet(x0:float,y0:float,q:int,kx:float,phase0:float=0.0)->np.ndarray:
    dx=(x-x0+N/2)%N-N/2; dy=(y-y0+N/2)%N-N/2
    r=np.hypot(dx,dy); theta=np.arctan2(dy,dx)
    return AMP*(r/SIGMA)*np.exp(-0.5*(r/SIGMA)**2)*np.exp(1j*(q*theta+kx*dx+phase0))

def diffuse(field,kappa,rate=0.05):
    ku,kd=np.roll(kappa,1,0),np.roll(kappa,-1,0)
    kl,kr=np.roll(kappa,1,1),np.roll(kappa,-1,1)
    fu,fd=np.roll(field,1,0),np.roll(field,-1,0)
    fl,fr=np.roll(field,1,1),np.roll(field,-1,1)
    return rate*(fu*ku+fd*kd+fl*kl+fr*kr-(ku+kd+kl+kr)*field)

# Exact LAP4 Fourier symbol used by the inspected source branch.
kernel=torch.zeros((N,N),dtype=torch.float64)
kernel[0,0]=-4.0; kernel[1,0]=kernel[-1,0]=kernel[0,1]=kernel[0,-1]=1.0
lap4_symbol=torch.fft.fft2(kernel).real

def step(state:dict,coupled:bool):
    psi=torch.tensor(state['psi'],dtype=torch.complex128)
    phi=torch.tensor(state['phi'],dtype=torch.float64)
    kappa=torch.tensor(state['kappa'],dtype=torch.float64)
    # This pilot disables stochastic births/noise, mu, PML and projection.
    if coupled:
        phi_int=torch.clamp(phi,0.0,10.0)
        interaction_factor=0.1*torch.tanh((0.04*phi_int*kappa)/0.1)
        grads_phi=torch.gradient(phi)
        flow=-0.004*(grads_phi[0]+1j*grads_phi[1])*kappa
        flow=flow/(1.0+torch.abs(flow)/10.0)
    else:
        interaction_factor=torch.zeros_like(phi)
        flow=torch.zeros_like(psi)
    def Nterm(curr):
        term=interaction_factor*curr
        term=term/(1.0+torch.abs(term)/10.0)
        return flow+term
    # Torch wave_baseline path: local half-step, Fourier propagation, local half-step.
    psi=psi+Nterm(psi)*0.5
    psi_hat=torch.fft.fft2(psi)
    psi_hat=psi_hat*torch.exp(1j*0.05*lap4_symbol)
    psi=torch.fft.ifft2(psi_hat)
    psi=psi+Nterm(psi)*0.5
    epsi=torch.abs(psi)**2
    if coupled:
        delta_e=0.001*epsi*kappa
        phi=phi+delta_e
        psi=(psi/(torch.sqrt(epsi)+1e-12))*torch.sqrt(torch.clamp(epsi-delta_e,min=0.0))
        phi=phi+kappa*0.05*torch.tensor(diffuse(phi.numpy(),kappa.numpy()),dtype=torch.float64)
    # Linear null sets reaction, drift and phi diffusion to zero.
    phi=torch.clamp(phi,0.0,1e6)
    return {'psi':psi.numpy(),'phi':phi.numpy(),'kappa':kappa.numpy(),
            'telemetry':{'is_nan':bool(torch.isnan(torch.sum(psi)).item() or torch.isnan(torch.sum(phi)).any().item())}}

def winding_map(psi:np.ndarray)->np.ndarray:
    ph=np.angle(psi); p00=ph; p01=np.roll(ph,-1,1); p11=np.roll(p01,-1,0); p10=np.roll(ph,-1,0)
    ds=[np.angle(np.exp(1j*(p01-p00))),np.angle(np.exp(1j*(p11-p01))),
        np.angle(np.exp(1j*(p10-p11))),np.angle(np.exp(1j*(p00-p10)))]
    wind=sum(ds)/(2*np.pi); a=np.abs(psi)
    a10=np.roll(a,-1,0); a01=np.roll(a,-1,1); a11=np.roll(a10,-1,1)
    pmax=np.maximum.reduce([a,a10,a01,a11]); pmin=np.minimum.reduce([a,a10,a01,a11])
    gate=(pmax>0.02)&(pmin<0.35*pmax)
    q=np.zeros((N,N),dtype=np.int8); q[(wind>0.5)&gate]=1; q[(wind< -0.5)&gate]=-1
    return q

def circular_com(I):
    idx=np.arange(N); zx=np.sum(I*np.exp(2j*np.pi*idx[None,:]/N)); zy=np.sum(I*np.exp(2j*np.pi*idx[:,None]/N))
    return float((np.angle(zx)*N/(2*np.pi))%N),float((np.angle(zy)*N/(2*np.pi))%N)

def run(name,psi0,coupled):
    state={'psi':psi0.copy(),'phi':np.zeros((N,N)),'kappa':np.full((N,N),KAPPA),'mu':np.zeros((N,N))}
    snaps={}; history=[]
    for t in range(T+1):
        if t in CHECKS:
            psi=state['psi']; phi=state['phi']; I=np.abs(psi)**2; cx,cy=circular_com(I); q=winding_map(psi)
            history.append({'step':t,'psi_mass':float(I.sum()),'psi_peak':float(np.abs(psi).max()),
             'phi_sum':float(phi.sum()),'phi_l2':float(np.linalg.norm(phi)),'com_x':cx,'com_y':cy,
             'vortex_count':int(np.count_nonzero(q)),'positive_vortices':int(np.count_nonzero(q>0)),
             'negative_vortices':int(np.count_nonzero(q<0))})
            snaps[t]={'psi':psi.copy(),'phi':phi.copy()}
        if t<T:
            state=step(state,coupled)
            if state['telemetry']['is_nan']: raise RuntimeError(f'NaN in {name} at step {t+1}')
    return {'snaps':snaps,'history':history}

def residual(results,pair,left,right):
    rows=[]
    for t in sorted(results[pair]['snaps']):
        p=results[pair]['snaps'][t]; a=results[left]['snaps'][t]; b=results[right]['snaps'][t]
        refpsi=a['psi']+b['psi']; refphi=a['phi']+b['phi']
        rows.append({'step':t,
         'psi_residual':float(np.linalg.norm(p['psi']-refpsi)/(np.linalg.norm(p['psi'])+1e-30)),
         'phi_residual':float(np.linalg.norm(p['phi']-refphi)/(np.linalg.norm(p['phi'])+1e-30)),
         'psi_mass':float(np.sum(np.abs(p['psi'])**2)),'psi_mass_sum_singles':float(np.sum(np.abs(refpsi)**2)),
         'phi_sum':float(p['phi'].sum()),'phi_sum_singles':float(refphi.sum())})
    return rows

plans={
 'single_left_linear':(packet(XL,Y0,+1,+KX),False),
 'single_right_linear':(packet(XR,Y0,+1,-KX),False),
 'linear_collision_same_charge':(packet(XL,Y0,+1,+KX)+packet(XR,Y0,+1,-KX),False),
 'single_left_toward_right':(packet(XL,Y0,+1,+KX),True),
 'single_right_toward_left':(packet(XR,Y0,+1,-KX),True),
 'collision_same_charge':(packet(XL,Y0,+1,+KX)+packet(XR,Y0,+1,-KX),True),
 'single_right_parallel':(packet(XR,Y0,+1,+KX),True),
 'parallel_pair_same_charge':(packet(XL,Y0,+1,+KX)+packet(XR,Y0,+1,+KX),True),
 'single_right_opposite_charge':(packet(XR,Y0,-1,-KX),True),
 'collision_opposite_charge':(packet(XL,Y0,+1,+KX)+packet(XR,Y0,-1,-KX),True),
 'single_right_minus_pi':(packet(XR,Y0,-1,-KX,np.pi),True),
 'collision_opposite_charge_pi':(packet(XL,Y0,+1,+KX)+packet(XR,Y0,-1,-KX,np.pi),True),
}
t0=time.time(); results={name:run(name,psi,coupled) for name,(psi,coupled) in plans.items()}
comparisons={
 'linear_pair_vs_singles':residual(results,'linear_collision_same_charge','single_left_linear','single_right_linear'),
 'collision_same_charge_vs_singles':residual(results,'collision_same_charge','single_left_toward_right','single_right_toward_left'),
 'parallel_pair_vs_singles':residual(results,'parallel_pair_same_charge','single_left_toward_right','single_right_parallel'),
 'collision_opposite_charge_vs_singles':residual(results,'collision_opposite_charge','single_left_toward_right','single_right_opposite_charge'),
 'collision_opposite_charge_pi_vs_singles':residual(results,'collision_opposite_charge_pi','single_left_toward_right','single_right_minus_pi'),
}
serial={'metadata':{'evidence_cutoff':'2026-10-20','grid':N,'steps':T,'kappa':KAPPA,'sigma':SIGMA,'amplitude':AMP,'kx':KX,
 'centers':[[XL,Y0],[XR,Y0]],'dt':1.0,'execution':'PyTorch CPU; manually transcribed narrow port of active develop Torch wave-baseline branch',
 'core_source_blob':'bb877021810691223a0eb960a45493a2e351112a','noise_and_stochastic_births':'disabled',
 'PML':'disabled; periodic FFT domain retained','mu':'disabled','caveat':'Imposed analytic packets are not demonstrated native stable Core linons; phase-winding observer is threshold-gated.'},'results':{},'comparisons':comparisons}
for name,item in results.items(): serial['results'][name]=item['history']
out=Path(__file__).with_name('pilot_summary.json')
out.write_text(json.dumps(serial,indent=2,allow_nan=False)+'\n',encoding='utf-8')
print('elapsed_sec',round(time.time()-t0,3),'summary',out)
for name,rows in comparisons.items():
 print('\n'+name)
 for r in rows:
  if r['step'] in (0,50,100,150,200,225,250,275,300,350,400,450,500):
   print(r['step'],round(r['psi_residual'],9),round(r['phi_residual'],9),round(r['psi_mass']-r['psi_mass_sum_singles'],9),round(r['phi_sum']-r['phi_sum_singles'],9))

```


## 12. Append-only correction — owner intuition and recovered repository inventory (2026-10-20)

**Owner intuition (preserved verbatim):** In response to the neutral running-track scene, the owner replied: “špatná detekce?” This is recorded as the owner's tentative candidate explanation, not as a settled decision or experimental fact.

**Agent formalization, distinct from the owner's words:** The candidate is that the observer may temporarily fail to detect a continuing structure, or may split/count it inconsistently, even while a separate field-level trace remains smooth. In Attempt C, the intensity-weighted circular centre moved smoothly while the threshold-gated phase-winding count changed from one to zero and later to one, and eventually to two. This makes observer failure a plausible explanation to test; it does not prove that the underlying topological structure remained intact. A smooth intensity centre can track a wave packet even when no validated, persistent vortex core is present.

**Competing explanations retained rather than silently collapsed:**

- **O1 — observer miss or duplication:** an amplitude/plaquette gate hides a winding, then detects it again, or classifies multiple nearby cells as separate detections.
- **O2 — genuine field/topology change:** the phase field actually loses, creates, merges, or splits local winding structures while the broad intensity packet continues.
- **O3 — boundary/topology ambiguity:** the periodic torus and a low-amplitude imposed single-charge packet can contain unresolved compensation or phase structure, so a local count is not a complete global charge account.
- **O4 — no validated object was present:** the analytic packet was imposed, not extracted from a demonstrated stable native Core linon; its changing detector count may not represent disappearance and reappearance of one persistent object.
- **O5 — implementation/provenance mismatch:** Attempt C is a manually transcribed narrow Torch/FFT extraction, not the full imported Core runtime; differences from active source remain possible.

The smallest *eventual* discriminating question suggested by the owner intuition is whether a separately validated known-answer field remains correctly identified across its full trajectory under an observer-only check, with positive and negative controls. That is a candidate design direction, not a frozen protocol and not permission to run it now. It must be compared with existing observer audits and the source-pinned historical lane before any threshold, metric, or mechanism is selected.

### Repository-inventory correction

Section 2 and the final paragraph of Section 11 accurately described the limited inventory available at the time they were written, but they are superseded for current repository visibility by this checkpoint. A read-only recursive Git tree read for `develop` returned `truncated=false`, with 1,260 total tree entries, 1,126 tracked file blobs, and 84 Markdown files below `research/`. The previously named candidate files at `research/README.md`, `research/index.md`, `research/lineum-master-report.md`, `research/eq4-canonical-research.md`, and `research/eq11-collision-dynamics.md` are absent from that complete `develop` tree.

The inventory does identify an already-declared scientific root and continuity lineage:

- Root scientific report: `research/foundations/lineum-continuous-source-cosmology-validation.md`, recorded immutable blob SHA `3fba3925553cd5596e46c02fa35d1db91523537d`.
- Mandatory continuity and impact ledger: `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, blob SHA `5304874451caf32313ad0e8e3c59e53958698d79`, which names the root report.
- Cross-branch priority review: `research/foundations/lineum-root-programme-cross-branch-priority-review.md`, blob SHA `9b1217f4757d2f0a9fb566284a91ac7e5a3c010d`.
- Related active preregistration: `research/foundations/lineum-collective-vortex-particle-identity-preregistration.md`, blob SHA `3c84624ed0a0bd961d7e344a3629761c2d8b2fc0`. It concerns source-off collective identity in the retained P2 lane and explicitly forbids inventing a substitute initializer from prose.

The collision report therefore must be treated as a child research lane within that existing programme, not as a provisional root. This correction does not silently merge the distinct scientific questions or promote results between them.

### Historical collision-artifact retrieval status

The complete current `develop` file tree and an immutable older Core tree at commit `8c4ff12af79b218fce8938497f56f75c4567195e` were inspected read-only. The old tree contains legacy `spec6_false_s41` run artefacts and particle/vortex logs, but the path inventory did not identify a clearly source-pinned Phase 8–20 collision runner or its corresponding initial state and raw output. The current tree and code-search results do surface historical narrative claims in the core whitepaper and draft hypothesis 30, but a narrative excerpt is not a reproduction receipt. This is a bounded retrieval result, not proof that no collision artifacts ever existed: content search indexing and historical commits remain incompletely reconciled, and the exact Phase 8–20 packages are still marked `unreproduced / provenance missing` until source, parameters, state, boundary, command, and outputs are joined.

The repository search also surfaced existing project gates for generic source-blind localized persistence and for recovery of the exact P2 package. These constrain priority but do not turn P2 collective identity into evidence for a two-core collision. The separate canonical audit gate remains blocked by Issue #7; it was not used or bypassed in this work.

### Binding next gate

1. Continue read-only retrieval of historical collision-related code, commits, initial states, and outputs, using path-specific Git history and declared equation-family distinctions. Do not label a prose claim as reproduced.
2. Keep the owner hypothesis `poor_detection` separate from the competing O2–O5 explanations. Compare it against the existing vortex-identity, historical-vortex-migration, and synthetic-observer audits before selecting a detector or test.
3. Only after the report lineage and the exact target variant are reconciled may a standalone observer-only protocol be specified, tested against known-answer positives/negatives, and committed before execution.
4. No new simulation, parameter tuning, Core equation change, canonical audit, or whitepaper promotion is authorized by this checkpoint.


## 13. Append-only historical source and observer cross-check (2026-10-20)

This section records a read-only retrieval update. It does not claim that any historical Phase 8–20 experiment has been reproduced.

### 13.1 The numbered phases are not one collision experiment

The source documents explicitly separate different equation families and different initial-value questions:

- `whitepapers/1-core/01-core-lineum.md`, Eq-7 / unitary-wave family, 2D periodic domain with static `kappa`, appears in the history at commit `b0b21de634644ea890a93dd706cbcae025fc0ba1` (dated 2026-04-04; document version 1.0.49-core, content blob at that commit `4b86c0250175eca2cb3e771c29e10020badcb3d7`). Its Phase 8–12 narrative concerns: failure of non-topological Gaussian/wave-packet inputs to spontaneously form composite modes; noise-assisted nucleation at zero crossings; later secondary clustering of newly nucleated defects; bulk cluster-merger pathways; and survival selection of formed clusters. This is not equivalent to the interaction of two independently validated, persistent vortices.
- `whitepapers/1-core/02-core-equation.md` is a separate equation-history document. At the retrieved checkpoint `b0b21de634644ea890a93dd706cbcae025fc0ba1`, its blob is `13f292997f83fb40c9c81bc4a203cea76ed0b2c0`; the current `develop` copy is blob `64f8341551d5737a6eb4919030bbb85a4b50380c`. It documents subsequent Phase 13–20 work under the experimental Eq-11.1 survival/overgrowth line, not the same Eq-7 experiment. Phase 13–14 acknowledge invalid or under-amplitude initial vortex constructions; Phase 15 explicitly says the historic indefinite-survival claim could not be traced to its omitted script/parameters; Phases 17–19 record a finite-window survival appearance overturned by longer-horizon overgrowth/fragmentation; Phase 18–20 include collision or multi-body probes in that separate equation family.
- Draft hypothesis `whitepapers/2-cosmology/hypotheses/30-cosmo-hyp-lineum-vs-standard-model.md` still contains a narrative of opposite-charge annihilation and proposed checks through `particle_log.csv` and trajectories. It is hypothesis/proposal text, not a reproduction receipt, and must not be counted as another independent confirmed result.

The checked historical trees at the Eq-7 Phase 8–12 checkpoint (`b0b21de634644ea890a93dd706cbcae025fc0ba1`) and the later Eq-11.1 checkpoint (`4b08ab1ebac1beb287c5ecd7f74803e530e7e7ad7`) were complete recursive Git trees according to the API. They exposed `scripts/profile_linon.py` (blob `9bae0e76286cc83af0bd68e0711481bffac5f467`, 3,577 bytes) and `scripts/infrastructure_phase10.py` (blob `6f3a657f4260f864c1c8df18957ae302d04dc0e1`, 7,001 bytes), but neither is a source-pinned two-linon collision runner: the first is an isolated-linon profiling experiment; the second is an urban-ring/pathfinding infrastructure experiment. The old standard `spec6_false_s41` output files likewise do not establish that they are the Phase 8–20 collision packages. No exact collision-specific Phase 8–20 runner/state/output tuple was identified in these checked trees; this is a bounded retrieval result, not proof that no such artifact ever existed elsewhere or in an unretrieved commit.

### 13.2 Relevant observer audits already exist, but none is the same as Attempt C

Two existing reports materially constrain the detector hypothesis and must not be treated as the same experiment:

1. `research/foundations/lineum-historical-vortex-migration-provenance-audit.md`, blob `3931c7c01b0764a794d46adf21b00866b186e399`, reconstructs an older July-2025 stochastic implementation from `lineum.py` commit `ccf95dad8e61325fe675f6618264c258089da13a`. It reports that the historical `curl(gradient(angle(Psi)))` maximum was branch-cut unsafe and did not reliably identify one compact migrating core. The original stochastic seed was not preserved, so its reconstruction added an explicit seed set; this is not an exact bitwise replay of the original binary. It explicitly does not assess the retained 2026 P2 state or Attempt C's detector.
2. `research/foundations/lineum-synthetic-vortex-field-causal-observer.md`, blob `aff6a5362f06b7258fe64b2234426db05d974d37`, is a separate known-answer synthetic field observer audit. Its declared domain and fixtures are synthetic; it did not import Core or use the retained P2 state. It found that detection/topology and several causal controls worked, while the frozen relational observer was non-identifying for some tests. This is method evidence for demanding known-answer positives, negatives, continuity, and adversarial controls—not evidence for the current Core or for the particular threshold-gated observer in Attempt C.
3. `research/foundations/lineum-vortex-chirality-path-discriminator.md`, blob `0dbe638072eb3de0e2ece619e31ee9d3eca98fb1`, records a known-answer synthetic localization/path study whose frozen charge-aware achiral null failed. It is additional evidence that a flawed control fixture can look like an observer failure; it does not qualify the collision runner or identify which explanation is correct in Attempt C.

Attempt C's detector used a plaquette-winding calculation with a local amplitude/plaquette gate; it is not identical to the historical wrapped-angle-curl maximum and it is not the synthetic plaquette-centre path observer. Therefore the owner's `poor_detection` intuition is plausible, but must not be treated as already proven by either previous audit. Its main competing explanations remain a detector miss/duplication, real field/topology change, periodic-boundary ambiguity, absence of a validated initial object, and a manual-port/source-path mismatch.

### 13.3 Exact next permitted work

Continue with path-specific, read-only retrieval of the commits that introduced the Phase 8–20 narratives and the source/output files they reference; compare each proposed artifact's initializer, equation family, boundary, parameters, command, and output manifest to the claim it is supposed to support. The immediate priority is the *two-initially-validated-core interaction* question, not spontaneous formation or late-time aggregation. Use the existing observer audits as design constraints only and explicitly retain their different scopes.

No new simulation, parameter tuning, canonical audit, Core equation edit, or whitepaper promotion is authorized by this retrieval update. A known-answer observer-only test may be proposed only after its target equation family and any recoverable historical source package are reconciled, and its source, tests, observer, and protocol are committed before execution.


## 14. Append-only Eq-11.1 collision-claim retrieval (2026-10-20)

A focused read of the Eq-11.1 historical equation appendix revealed further collision claims that must be preserved as an existing variant, not combined with the Eq-7 Phase 8–12 narrative:

- The `whitepapers/1-core/02-core-equation.md` file at current `develop` blob `64f8341551d5737a6eb4919030bbb85a4b50380c` describes a dense parallel sweep of macroscopic **non-winding scalar blobs** across (N=2) to (N=20). This is not a collision of two validated topological cores.
- The same appendix separately states that Eq-11.1 N-body vortex collisions for ((+1,+1)) and ((+1,-1)) “overwhelmingly” show topological scattering like non-vortex fields, with repulsive/fragmenting behavior. It then records an advection reintroduction sweep that sheared/destroyed the phase structure and a localized bridge-suppression case that halted repulsion but did not establish generic inward binding. These are documented historical claims, not independently recovered raw results.
- The Phase 18–20 discussion in this Eq-11.1 lineage reports finite-window apparent survival being overturned by longer-horizon runaway/fragmentation, plus symmetric-pair, dipole, and triad comparisons. It therefore does not support transferring an Eq-11.1 outcome to Eq-7/current Core or treating a visually persistent finite-horizon peak as a surviving linon.
- At the preceding Eq-7 Phase 8–12 release checkpoints, the commits that published the phase narratives changed only `whitepapers/1-core/01-core-lineum.md` and `portal/package.json`; they did not commit an experiment-specific collision runner or raw Phase 8–12 output in those commits. The later Eq-11.1 documentation commit `4b08ab1ebac1beb287c5ecd7f74803e530e7e7ad7` did touch the equation appendix and many textual search/notes files, but no dedicated collision runner appeared in the complete tree inventory. This does not prove that no temporary local script was used; it means the inspected Git history does not supply a complete, source-pinned run package.
- `lineum.py` at the retrieved Eq-7 checkpoint (blob `a57171a633b85d02e4c2047d367cab5b534181aa`) is a broad historical orchestration/simulation script that imports `lineum_core.math.step_core` and writes generic `particle_log.csv`; the audited file itself does not establish the Eq-11.1 initial-value and parameter package for the collision claims. The search-transcript artifacts `found.txt` and `found2.txt` contain narrative matches, not raw collision output.
- Historical `scripts/profile_linon.py` (blob `9bae0e76286cc83af0bd68e0711481bffac5f467`) does initialize and profile an isolated vortex candidate with a plaquette-winding detector, but it is not a pair-collision runner and does not by itself establish that the selected isolated candidate is a persistent solution of the intended equation.

### Variant coverage consequence

The existing registry must keep at least these three collision questions separate:

```text
Q1 — Smooth non-topological wave/overload collision:
     Can a pair of trivial wave packets spontaneously create winding or a bound mode?
     Eq-7 Phase 8–12 narrative; reproducibility package not recovered here.

Q2 — Interaction of two pre-validated topological cores:
     Given each core passes independent existence, localization, topology, and persistence gates,
     how does a same-charge or opposite-charge pair evolve against isolated and linear controls?
     This is the immediate question of the active collision report; no admissible result yet.

Q3 — Eq-11.1 historical N-body collision / overgrowth:
     Do the documented experimental Eq-11.1 controls scatter, fragment, annihilate, or bind?
     Historical claims exist, but no fully source-pinned package was recovered in this retrieval.
```

The current evidence does **not** answer Q2. Q1 narratives and Q3 claims may motivate expected controls, but cannot fill the missing Q2 initial-state and source-equivalence requirements. The owner intuition that detection is wrong remains one registered explanation, not a verdict; true field/topology change, initial-object invalidity, boundary ambiguity, and model/source mismatch remain live alternatives.

No simulation, parameter retuning, canonical audit, equation edit, or whitepaper claim change is authorized by this update.


## 15. Append-only recovery of a deprecated legacy collision matrix (2026-10-20)

An additional relevant narrative was found in `whitepapers/2-cosmology/extensions/04-cosmo-ext-vortex-rigidity.md`, current `develop` blob `938ee11afa280c16f30b3983d97f54f9f9173430`. Its header is explicit: **Legacy / Deprecated (Eq-4 Context only; ref. Eq-11)**, and it warns that the described Eq-4 iteration used continuous bridge-suppression phase mechanisms and visual alpha-thresholding logic not established for the newer minimal baseline. This legacy caveat takes precedence over any stronger language in the document's historical narrative.

### 15.1 Section 61 — reported empirical interaction matrix

The legacy appendix reports the following local run receipt:

- Target named in the document: `.scratch/eval_interaction_matrix.py` (local execution; the script is not present in the checked branch trees and no code hash/raw output/seed was recovered).
- Grid: (64 	imes 64); model label: two-layer linear (R)-inhibitor environment; (sigma=3.0).
- Geometries: homogeneous (N=3) vs (N=3), asymmetric (N=3) vs (N=2), and extreme asymmetric (N=4) vs (N=1).
- Sweeps: initial mathematical distance (d=10) or (16) pixels and spatial phase-advection gradient (k=0.2) or (0.6).

Reported table:

| Valency pair | Distance | (k) | Reported minimum distance | Reported outcome |
|---|---:|---:|---:|---|
| (N=3) vs (N=3) | 10 px | 0.2 | 15.0 px | Scatter |
| (N=3) vs (N=3) | 10 px | 0.6 | 15.0 px | Scatter |
| (N=3) vs (N=3) | 16 px | 0.2 | 21.0 px | Scatter |
| (N=3) vs (N=3) | 16 px | 0.6 | 19.6 px | Orbit / glancing deflection |
| (N=3) vs (N=2) | 10 px | 0.2 | 4.1 px | Orbit |
| (N=3) vs (N=2) | 10 px | 0.6 | 3.2 px | Absorption |
| (N=3) vs (N=2) | 16 px | 0.2 | 6.0 px | Orbit |
| (N=3) vs (N=2) | 16 px | 0.6 | 2.2 px | Absorption |
| (N=4) vs (N=1) | 10 px | 0.2 | 3.6 px | Orbit |
| (N=4) vs (N=1) | 10 px | 0.6 | 0.0 px | Storm / numerical breakdown |
| (N=4) vs (N=1) | 16 px | 0.2 | 3.0 px | Absorption |
| (N=4) vs (N=1) | 16 px | 0.6 | 0.0 px | Storm / numerical breakdown |

These are values quoted from the appendix, not independently recomputed values. The appendixed script source, exact initialization, boundary and update details, seed(s), per-step trajectories, full output, and hashes are missing from the currently inspected permanent evidence. Therefore this historical matrix is classified `reported_legacy_result_provenance_incomplete`, not a reproducible current-Core result.

### 15.2 Why it does not answer the active question

The reported valency-(N) composite structures were tested in an explicitly engineered (R)-inhibitor/bridge environment in a deprecated Eq-4 context. They cannot be equated with two independently validated current-Core topological defects, and their “scatter/orbit/absorption/storm” labels cannot be reused without reconstructing the observer and the governing equations. The legacy document also appends later Eq-11.1 phases (including RK4/comoving-metric work) under the same long appendix; those are still another model family and must not be silently merged with Section 61.

Thus the variant ledger now contains a fourth, distinct lane:

```text
Q4 — Deprecated Eq-4 two-layer R-inhibitor interaction matrix:
     a historical, quantitatively reported collision sweep exists;
     exact runner and raw result package not recovered;
     not transferable to Q2 and not promoted as current evidence.
```

The immediate owner intuition about possible detection failure remains plausible for Attempt C, but the historical collision matrix has its own provenance and model-identity defects; it cannot be used to confirm or refute that intuition. The permitted next step remains source recovery and variant reconciliation. No new simulation, parameter tuning, canonical audit, or equation/whitepaper change is authorized.


## 16. Append-only scan of additional legacy and successor collision claims (2026-10-20)

A further read-only scan examined all 14 explicitly inspected branch trees below. Every tree request returned `truncated=false`. The inspected refs were:

```text
develop
main
backup
agent/priority-f-prereg
agent/priority-f-result
agent/priority-f-result-v2
agent/gnostic-e-main-report
codex/root-research-continuity
codex/q2-m30-endogenous-balance-20260830
codex-rule-fix
debug-v1.1.6-ci
staging
feature/diffusion-api-poc
TomasTriska88-patch-1
```

None of these inspected tree snapshots contains the locally named scripts `.scratch/eval_interaction_matrix.py`, `.scratch/eval_interaction_sweep.py`, `.scratch/eval_phase68_algebra.py`, `.scratch/eval_phase69_deuteron_orbitals.py`, or `.scratch/eval_phase70_meson_shell.py`. GitHub path-history lookups also returned no commits for those exact `.scratch/...` paths. This is a bounded result for the inspected branches and path names, not proof that the scripts never existed outside Git or under other names. The branch-search connector paginated inconsistently, so this section deliberately reports an explicitly inspected set rather than claiming an exhaustive registry of every branch that has ever existed.

### 16.1 Additional legacy Eq-4 sweep narrative

The same deprecated `whitepapers/2-cosmology/extensions/04-cosmo-ext-vortex-rigidity.md` (blob `938ee11afa280c16f30b3983d97f54f9f9173430`) contains Section 62, which refers to a local `.scratch/eval_interaction_sweep.py` run of 250 configurations using 10 valency pairings across initial distances (d in [6,10,14,18,22]) and advection multipliers (k in [0.1,0.3,0.5,0.7,0.9]). The appendix's reported summary includes the following percentages in the order scatter / orbit / absorb / storm:

| Pair | Reported percentages |
|---|---|
| (1) vs (1) | (16 / 64 / 0 / 20) |
| (2) vs (1) | (0 / 84 / 0 / 16) |
| (2) vs (2) | (28 / 52 / 0 / 20) |
| (3) vs (1) | (0 / 80 / 0 / 20) |
| (3) vs (2) | (20 / 60 / 0 / 20) |
| (3) vs (3) | (68 / 16 / 0 / 16) |
| (4) vs (1) | (0 / 72 / 8 / 20) |
| (4) vs (2) | (0 / 80 / 0 / 20) |
| (4) vs (3) | (44 / 40 / 0 / 16) |
| (4) vs (4) | (76 / 16 / 4 / 4) |

These are quoted from the legacy appendix; the exact script, initial fields, per-configuration raw outcomes, seed policy, execution command, source fingerprint, and hashes remain unavailable in the inspected permanent Git history. The table therefore remains `reported_legacy_result_provenance_incomplete`, not a reproducible simulation result and not evidence for Q2. It also uses the older N-valency/engineered R-inhibitor setup, not two validated native Core linons.

### 16.2 The same long appendix crosses into a different successor equation family

Later in the same file, the narrative explicitly changes to a successor architecture labelled Eq-12, with an Aegis (S)-boundary and nematic registry/scaffold field (U). Sections 68–70 cite other untracked local scripts:

- `eval_phase68_algebra.py`: orientation/contact matrix under candidate-V boundary coupling, with aligned, anti-aligned, wedge, same-type, and multi-body controls; narrative reports orientation-dependent slip/drift/merger outcomes.
- `eval_phase69_deuteron_orbitals.py`: initialized isolated dipole/quadrupole/octupole-like states and A+B contact pairs; the narrative says A+B pairs slipped/separated under tested alignments, while A+A/B+B controls merged.
- `eval_phase70_meson_shell.py`: added a short-range boundary-localized mediator to the Eq-12 successor; the narrative says it did not produce a stable A+B near-contact trap and A+B pairs separated, while A+A merged.

The scripts and accompanying raw result bundles were not found in the inspected trees. These claims therefore remain narrative/provenance-incomplete. They are also **not one continuous equation lineage with Section 61**: the file header calls the appendix legacy/deprecated Eq-4 context, its middle sections report Eq-11.1 and its later sections add an Eq-12 successor. Do not combine these outcomes into one universal “Lineum collision law.” The changing equations and initial-value problems must be retained as separate variants, and the contradictory same-type/opposite-type results across these families must remain visible rather than resolved by storytelling.

### 16.3 Retrieval status and next gate

The currently recovered collision-related material now includes:
- Eq-7 Phases 8–12 as whitepaper narrative, without their collision-specific pinned runner/state/output package;
- Eq-11.1 Phases 13–20 and related N-body narratives, with explicit historical missing-provenance cautions;
- a deprecated Eq-4 R-inhibitor matrix and sweep whose local scripts/raw receipts are missing from the inspected trees;
- an Eq-12 successor contact/orientation family whose local scripts/raw receipts are also missing;
- an isolated-linon profiling script which is not a collision runner;
- separate, scoped observer audits that caution against treating a track or raw detector count as proof of one continuing core.

The immediate Q2 problem remains unresolved: **no recovered permanent package currently establishes two individually validated, persistent current-Core topological cores and their interaction with matched isolated controls.** The next permitted work is read-only recovery of the exact source, initialization, parameters, and raw outputs for one candidate lineage, with the equation family named first. If no such package can be recovered, the record must say so and propose a new frozen Q2 model/protocol as a new model, never as a direct reproduction of the legacy run.

No new simulation, parameter tuning, canonical audit, equation edit, or whitepaper promotion is authorized by this retrieval step.


## 17. Append-only cross-repository retrieval receipt (2026-10-20)

To check whether the absent legacy runners had been retained outside Core, exact filename/content searches were run against the default searchable content of these connected repository families:

- `TomasTriska88/lineum-core`
- `lineum-dynamics/lineum-dynamics`
- `TomasTriska88/oea`
- `TomasTriska88/lina-personal` (the declared current alias for Lina EI)

The exact searches for `eval_interaction_matrix.py`, `eval_interaction_sweep.py`, `eval_phase68_algebra.py`, `eval_phase69_deuteron_orbitals.py`, `eval_phase70_meson_shell.py`, `eval_phase8 collision`, `eval_phase10 collision`, and `04-cosmo-ext-vortex-rigidity` returned no indexed code-search results across these repositories. This is evidence that the exact named files were not found in those indexed current contents; it is not an exhaustive Git-history proof, because the search connector indexes current default-branch content and cannot establish that an untracked/local file never existed. The separate Core recursive-tree scan provides the stronger file-path check for the inspected refs listed in Section 16.

No cross-repository runner or raw collision evidence was recovered. The source-lineage status is consequently unchanged:

```text
Q1 Eq-7 smooth-wave formation: narrative present; dedicated source/output package unrecovered
Q2 two independently validated current-Core cores: no admissible collision result
Q3 Eq-11.1 N-body collision/overgrowth: historical narrative present; exact package unrecovered
Q4 deprecated Eq-4 R-inhibitor matrices: numerical summaries quoted in appendix; local scripts/raw outputs unrecovered
Q5 Eq-12 successor contact/orientation matrices: narrative present; local scripts/raw outputs unrecovered
```

**Next allowed action:** continue source/provenance retrieval only if a new, concrete artifact lead appears. If no exact historical Q2 package can be recovered, do not keep searching indefinitely or retrofit any of Q1/Q3/Q4/Q5 as Q2 evidence. Close the retrieval phase with those bounded provenance classifications and prepare a *new*, explicitly named Q2 protocol only after all applicable report, observer, equation-family, and precommit gates pass. Any future runner must begin with independently validated single-core states, preserve matched isolated controls and the linear null, state periodic-domain charge accounting, include known-answer detection controls, and be committed before execution. These are design constraints, not an authorized run or frozen parameter specification.

No new simulation, parameter tuning, canonical audit, Core equation edit, or whitepaper promotion is authorized by this retrieval receipt.


## 18. Append-only current-Core initialization and equation-family gate (2026-10-20)

A read-only inspection of `lineum_core/math.py` at `develop`, blob `bb877021810691223a0eb960a45493a2e351112a`, exposed a concrete gate before any new Q2 design:

- `step_core(state, cfg)` is an update function for an already constructed state. It asserts that `psi`, `phi`, and `kappa` are present and then invokes the selected NumPy or PyTorch step. This file does not provide a verified initializer that creates an isolated, persistent native linon; the phase/topology state is supplied from outside the step function.
- The frozen `CoreConfig` defaults include `physics_mode_psi="diffusion"`, `disable_quantum_noise=False`, `use_mode_coupling=True`, `use_mu=False`, and CFL/cap settings. The Torch path separately branches for `wave_baseline`, `wave_projected`, and `wave_projected_soft` through the `"wave"` mode check. A result cannot be named merely “Core collision” without pinning the actual backend and mode, all parameters and noise settings, and the initialization and observer.
- The same file's `step_core` docstring calls it the single source for “Canonical Eq-4' Physics,” while its trailing compatibility comments say that `Eq4Config/step_eq4` are legacy names and the conceptual mode is now “Eq-7 / Wave Core.” Those labels are not an adequate, self-consistent source contract for Q2 on their own; the intended implementation snapshot and equation lineage have to be resolved and frozen.

This means the prior Attempt C did not solve the missing initial-state problem: it injected analytic phase-winding packets into a manually transcribed wave path, not two isolated states demonstrated to survive under the selected current Core solver. The old `scripts/profile_linon.py` is a historical isolated-candidate profiler and is not a verified current-Core initializer or pair-collision harness. Its existence cannot authorize reusing the manually imposed Attempt C packets as physical linons.

### Binding consequence

Before freezing a new pair-interaction protocol, perform one final read-only source/test inventory of the current Core initialization and existing tests. Establish whether any tracked initializer plus an exact solver configuration can independently pass an isolated-core localization, winding, numerical boundedness, and persistence gate. If not, classify “two validated current-Core cores” as a missing prerequisite, and do not invent or tune an initializer until the exact model and permitted starting-state method have been explicitly formalized. The independent primary root-programme queue also remains the exact retained P2/C0 source-off package recovery, not a reason to relabel collective-state evidence as pair-collision evidence.

No Core source was edited or executed for this checkpoint. No new simulation or test run occurred. The canonical audit remains blocked; no equation or whitepaper promotion is authorized.


## 19. Append-only tracked-test and official-observer audit (2026-10-20)

A targeted read-only audit checked the current development branch's existing Core tests, validation harness, package interface, and main Core whitepaper:

| File | Blob | Scope observed in this inspection |
|---|---|---|
| `tests/test_wave_core.py` | `085e302e7c70c5dadcee45fe479bb70eaa8cd264` | Gaussian real-amplitude packets and general boundedness/reversibility checks in explicit `wave_baseline` mode; no known-answer charge-(+1/-1) vortex initializer or two-core collision fixture was identified. |
| `tests/test_wave_core_contract.py` | `54227e2393928c40de8a6b318a75476a877977a9` | Wave-mode contract checks; no explicit vortex/collision fixture was identified in the inspected file. |
| `tests/test_lineum_core_math.py` | `d1f097c6ef54b04aece7d2ff65e5409757ed6a99` | Shape/finiteness and generic field update tests, including uniform/random test states; no isolated winding-core existence test was identified. |
| `tests/test_physics_contract.py` | `7acbb8a1c5ff85a5b24970d216aa2a08111b0941` | Mock state, field/coupling accounting and stencil comparisons; no isolated vortex initialization fixture was identified. |
| `scripts/validation_core.py` | `59818298f675e0a4789f4d4248ecc4c9fa454e48` | Validation modes built from Gaussian packets, excited Hermite-like states and general field tests. A search of the full file for `vortex`, `winding`, `arctan2`, and `inject` did not find a vortex initializer or winding-charge validator; it extracts phase arrays in a few checks but does not itself validate topological winding. |
| `whitepapers/1-core/01-core-lineum.md` | `edc63b0d150b3b616ff8a108ea47a4f89b6a6c37` | Defines a linon as a stable localized excitation; identifies vortex formation/motion as observations but explicitly says the half-collinear/wave-breaking collision idea requires targeted runs and is not contract-validated. Its detector notes say amplitude gating is visualization-only and that topology metrics use raw values. |

These are bounded file-level findings, not a proof that no experimental initializer exists elsewhere. They do show that the currently inspected automated unit/contract tests do **not** establish the key precondition for Q2: a known-answer, localized, bounded, persistent current-Core topological core with a validated charge observer. Ordinary Gaussian packets or uniform states are not substitutes for that precondition.

### The Attempt C observer is not the stated Core metric observer

Attempt C used a custom phase-winding plus local amplitude/plaquette gate. The current whitepaper's stated convention, by contrast, says amplitude gating is visualization-only and raw phase-winding values are used for CSV/metrics. The earlier count drop in Attempt C therefore identifies a failure/limitation of that *custom pilot observer under its imposed packet conditions*, not a demonstrated failure of the official current-Core metric pipeline. It remains possible that other observer failures exist, but they must be demonstrated independently rather than inferred by treating the two detectors as identical.

### Binding next-step order

1. Pin the exact intended Core equation/backend/mode and resolve the Eq-4' versus Eq-7/Wave-Core label conflict in the source contract before any model result is named.
2. Recover or explicitly define (as a new and clearly labeled protocol) a known-answer isolated topological-core state and independent charge observer. The fixture must demonstrate its own winding, localization, numerical boundedness and survival before a second copy can be used.
3. Audit the detector against known-answer positive and negative fields, with the official raw-metric convention separated from optional visualization masks.
4. Only if the individual-core gate passes, freeze a pair-interaction matrix with matched isolated controls, a linear null where mathematically applicable, boundary/charge accounting, predeclared outcomes and source fingerprints; commit the exact runner and protocol before running it.

The root programme's higher-priority retained P2/C0 continuation gate remains separate and unresolved. The present read-only audit did not create a new initialization, edit Core code, execute any test, or authorize a collision simulation.


## 20. Append-only P2 recovery-brief and oversized-root retrieval receipt (2026-10-20)

The exact recovery instructions are preserved in research/foundations/lineum-p2-retained-package-recovery-brief.md, blob 7d2ecd83812e5c6446c694f7505839c18aa94153. Its scope is deliberately limited to recovering and replaying the retained centered-only C0 baseline: a 32×32 periodic grid, exact-vacuum initialization, dt=0.1, 12 paired seeds, source active through t=20, then source off through t=60, with absolute-time-indexed common random arrays and the frozen v3 transport observer. The target metrics are stated in Section 6 of that brief. It explicitly prohibits reconstructing the source code by tuning to those target metrics.

### What could be recovered through the ChatGPT GitHub connector

- The pinned current root report blob 3fba3925553cd5596e46c02fa35d1db91523537d has a Git tree size of 67,002,835 bytes. A direct blob fetch fails at the connector's 64-MiB decoded-message limit. fetch_file with small start_line/end_line ranges also returns an empty body for this oversized file; it does not supply the requested line ranges.
- An earlier immutable version at commit 26d8726d7f9c5ac371554d1d1b6edddc3a6425bd, blob abbd04b3ab91387241fda09fbcf251fc163f3ea9 (61,166,351 bytes according to its tree) was retrievable. Its header identifies version 0.4.1 and evidence cutoff 2026-07-29. It contains separate P2.3/P2.4 source/transport/replenishment studies and their embedded scripts/receipts; these are not the target 12-seed, T=60 schedule experiment. For example, its C0_CONT lane uses a different lane registry, a single frozen seed (2026263000), and a model-time endpoint of 200. That is a distinct scientific protocol and cannot fill the retained P2 package.
- An intermediate version at commit d2a144e12f077d0dd7df3c127f11ee890cfad87a, blob d399957ea59a0b94ba0a35099d5a373bcda33476 (62,462,594 bytes in its tree) was also retrievable. Target-specific terms and numerical fingerprints from the recovery brief—such as 20.5232, 0.974687, 12 paired seeds, and the 40–60 target window—were not present in that version.
- The final report-increasing commit is 729e1f40ee268e6811e4d14f1b5efc1f0ce8b2e9 (“research: audit current-core copying prerequisite”). The GitHub comparison API identifies the root Markdown as the only changed file, with 48,432 additions and 13 deletions, but the patch body is omitted by the connector. The later root blob is larger than the connector's one-message limit. Therefore the possible presence of the target package in that final addition remains unverified.

This establishes a retrieval limitation and a version-matching problem, not that the target package never existed. The bounded ChatGPT-connector search cannot claim outcome E_not_located_after_exhaustive_local_search, because it did not perform the brief's required exhaustive local repository-history search and could not inspect the full current root. It also cannot claim package recovery outcome A or B. No baseline replay occurred.

### Binding next gate

The exact P2 Retained Source-Schedule Package Recovery Brief calls for repository-local Codex Max work on develop, with the full history/tree and clean-worktree checks. That local-checkout operation is not available through the present oversized-file connector path. Until a supported local repository execution path completes that brief, the retained P2/C0 package remains blocked_by_current_execution_access. Do not use the earlier P2.3/P2.4 continuous-source pilots, the exploratory collision Attempt C, or any legacy Eq-4/Eq-11.1/Eq-12 collision narrative as a substitute.

No simulation, baseline replay, parameter tuning, Core edit, or whitepaper change occurred during this retrieval attempt.


## 21. Append-only local repository-access probe result (2026-10-20)

A read-only attempt was made to test whether the available container could reach the public repository directly, using:

```text
git ls-remote --heads https://github.com/TomasTriska88/lineum-core.git develop
```

The command exited with status 128 and reported:

```text
fatal: unable to access 'https://github.com/TomasTriska88/lineum-core.git/': Could not resolve host: github.com
```

No clone, file checkout, repository change, test, or simulation occurred. This confirms that the present container cannot provide the local repository path required by the recovery brief. Combined with the 64-MiB single-response ceiling for the current root blob and the empty line-range fetches, the current ChatGPT connector/runtime cannot complete the required exhaustive local-history recovery. This is not outcome E: the brief reserves that result for an exhaustive local repository search, which has not happened.

The scientifically and operationally correct stop point is therefore:

```text
retained_P2_recovery = blocked_by_current_execution_access
historical_collision_Q2 = no admissible result
next action = run the exact bounded recovery brief in an authorized local Codex Max checkout
no long-horizon continuation, collision simulation, source tuning, or Core/whitepaper edit authorized
```

The detailed execution protocol and its mandatory search coverage, provenance matrix, replay authorization, outcome labels, and copyable instruction remain in research/foundations/lineum-p2-retained-package-recovery-brief.md (blob 7d2ecd83812e5c6446c694f7505839c18aa94153). The recovery output must be committed in research/foundations/lineum-p2-retained-package-recovery.md before ChatGPT resumes scientific decisions.
