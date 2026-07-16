# Lineum Gate 0: Canonical-Theory Decision Brief

**Document status:** active — named deterministic and legacy time profiles implemented; stochastic time semantics remain unresolved; default physics and whitepaper changes remain gated
**Research version:** 0.6
**Evidence cutoff date:** July 16, 2026
**Language:** English
**Current confidence:** high for the source audit, RD-0 fingerprint, deterministic time-scaled candidate, and distinction between initial branch selection and ongoing stochastic forcing; medium for stochastic interpretation and sequencing; no claim of physical validation
**Decision readiness:** deterministic continuous-time profile implemented for explicit opt-in use; stochastic theory needs revision; major-discovery and fundamental-physics claims are not ready
**Standalone portability:** all decision-relevant definitions, equations, observations, calculations, executable reproduction code, and outputs are embedded in this document
**Decision boundary:** this brief records one approved software-characterization step; it does not declare a new Lineum law

## 1. Technical Summary

**Gate 0 is not yet passed.** The current Lineum corpus uses at least five incompatible canonical labels—Version 4, Eq-4′, Eq-7, Eq-10, and Eq-11.1—plus a provisional biharmonic PDE. These labels do not denote one backend-independent update law. The same public runtime option named `wave_baseline` executes a diffusive step in the NumPy backend and a spectral wave step in the PyTorch backend.

**The immediate recommendation is to freeze meaning before freezing ambitious physics.** Lineum should presently be described as a research platform for effective, open, coupled-field dynamics. Claims about fundamental spacetime, quantum mechanics, particles, gravity, or an ontic lattice should remain separate hypotheses.

**The smallest safe software step is a provisional deterministic reference lane, not promotion of Eq-11.1 or the biharmonic candidate.** A noise-free diffusive subset already agrees across NumPy and PyTorch to approximately machine precision in the tested configuration. It can serve as a ruler for later changes while the physical theory remains open. This proposed lane is named **Reference Dynamics 0 (`RD-0`)** to avoid assigning another historical `Eq-N` label prematurely.

**A fixed-physical-time refinement experiment identifies one concrete numerical inconsistency.** The legacy \(\phi\)-diffusion is applied once per update without multiplication by the time step \(h\). Halving \(h\) therefore applies nearly twice as much \(\phi\)-diffusion over the same declared time. The project owner authorized an opt-in candidate containing the missing factor; it is now implemented in both CPU backends and converges at the expected first-order rate while the default remains unchanged.

**Broader falsification supports `RD-0-C1=True` for deterministic continuous-time simulations but not yet for the entire stochastic theory.** Four Fourier modes, periodic edge coupling, nonuniform \(\kappa\), the analytic stability boundary, and cross-backend parity passed. The stochastic audit found two different effects: vacuum noise selects persistent phase branches, while fresh randomness added after a shared nonzero state shrinks as \(\sqrt h\). Current “quantum foam” therefore behaves more like stochastic branch selection than a demonstrated continuously driven quantum vacuum.

**The approved profile gate is now implemented without changing the default runtime.** `legacy-per-update-v1` fixes `phi_diffusion_scales_with_dt=False`. `rd0-c1-deterministic-continuous-time-v1` fixes the validated deterministic subset and `phi_diffusion_scales_with_dt=True`. Profile-defining values fail closed if a caller attempts to override them, while \(h\) and numerical coefficients remain adjustable for controlled refinement experiments.

**On July 16, 2026, the project owner approved this separation and the characterization-first path:**

1. **identity layer:** Lineum is currently an effective coupled-field research platform;
2. **software-reference layer:** `RD-0` is a deterministic regression baseline, not a law of nature;
3. **physics-candidate layer:** wave, Eq-11.1, biharmonic, discrete-spacetime, quantum, and gravitational models remain competing hypotheses.

In plain language: the project currently has several different engines sharing one name. One small engine has now been selected as a measuring ruler. That does not crown it as the final theory; it gives every later experiment the same starting point.

## 2. Decision to Be Made

Gate 0 asks one question:

> What exact state, update law, numerical interpretation, and claim boundary define the Lineum model being tested?

A complete answer must make the following tuple unique:

\[
\mathcal M=(\mathcal S,F,\Theta,\mathcal B,\mathcal O,\mathcal C),
\]

where:

- \(\mathcal S\) is the state space;
- \(F\) is one update map \(X_{n+1}=F(X_n;\Theta)\);
- \(\Theta\) is the versioned parameter set and unit convention;
- \(\mathcal B\) is the boundary and topology specification;
- \(\mathcal O\) is the set of observables;
- \(\mathcal C\) is the set of claims that the model is allowed to support.

Changing the backend must not change \(F\). A backend may approximate the same map with bounded numerical error; it may not silently select a different physical evolution.

## 3. Evidence Scope and Definitions

### 3.1 Audited snapshot

| Repository | Branch | Revision | Working-tree entries | Gate 0 role |
|---|---|---|---:|---|
| Lineum Core | `develop` | `350b02d4349d7c678a16daf6cd30df2a321a3952` | 76 | authority for candidate physics, whitepapers, runtime, and validation |
| Lineum Dynamics | `develop` | `9890cf3fd557717767b8a93ede00a73a36318d22` | 18 | downstream product integrations and copied runtime variants |
| OEA | `dev` | `5b3b7394e21a7bc1d01420cbefa13f4ca5c2f399` | 0 | application-specific generative-imaging algorithm |
| Lina EI | `main` | `4ea7335bb5db8c55ca11f474478acd087975c25e` | 109 | application-specific solver and canonical-Core replay controls |

Working-tree content was inspected but is not treated as committed canon. The uncommitted Core change that affects this analysis alters execution-device selection and metadata, not the mathematical branches compared below.

### 3.2 Terms used in this brief

- **Canonical physics law:** one fully specified mathematical update, independent of implementation language and hardware.
- **Reference implementation:** an executable realization of that law with stated numerical error.
- **Regression baseline:** a deliberately frozen behavior used to detect change; it may be useful before it is physically interpreted.
- **Backend:** NumPy, PyTorch CPU, CUDA, or another implementation of the same declared law.
- **Extension:** any added state, term, boundary, stochastic process, or operator that changes the law.
- **Validated:** shown to satisfy a declared mathematical or software contract; not automatically shown to describe nature.

## 4. The Present Corpus Does Not Define One Canonical Law

The conflict is structural rather than editorial.

| Source statement embedded in the current corpus | Declared identity | Why it conflicts |
|---|---|---|
| Core manuscript title and metadata | Eq-7 and Eq-10 canonical; Eq-11.1 pending | two equations are named canonical before the body is read |
| Core manuscript Equation (1) | Version 4 canonical update | differs from both the unitary pseudocode and runtime coefficients |
| Core manuscript one-step pseudocode | Eq-7 unitary Strang split | spectral propagation, not the displayed diffusive Euler update |
| Equation-history metadata | Version 10 canonical; Version 11.1 candidate | the same history later calls other phases canonical |
| Runtime entry-point description | Eq-4′ canonical physics | public aliases simultaneously describe Eq-7 / Wave Core |
| NumPy runtime | diffusive update for every `physics_mode_psi` value | a requested wave mode does not select wave propagation |
| PyTorch runtime | diffusive or spectral wave branch | the same option selects a different update from NumPy |
| Provisional continuous research | biharmonic reaction–diffusion PDE | no recoverable executable ETD2/dealiasing reference was found in the audited executable corpus |

This means a successful test can currently validate one implementation contract while a whitepaper reader reasonably believes that a different equation was tested.

## 5. Exact Reconstruction of the Deterministic Runtime Subset

This section reconstructs the audited noise-free, mode-coupling-free, \(\mu\)-free path. It is descriptive evidence, not a proposed final law.

Let \(\psi^n\in\mathbb C^{N\times N}\), \(\phi^n\in\mathbb R^{N\times N}\), and let \(\kappa\) be a static real map. For the four-neighbor stencil, define

\[
(\mathcal L_\kappa f)_{ij}
=\sum_{(p,q)\in\mathcal N_4(i,j)}
\kappa_{pq}(f_{pq}-f_{ij}),
\]

with periodic index wrapping in the diffusion operator. The gradient currently uses the backend's array-gradient operation, which applies one-sided edge differences rather than the declared periodic central difference. That boundary mismatch must be resolved before any gradient-drift law is promoted.

For \(\mu=0\), zero external input, and disabled stochastic terms, define

\[
A_{ij}=0.1\tanh(0.4\,\operatorname{clip}(\phi^n_{ij},0,10)\kappa_{ij}),
\]

\[
G_{ij}=\frac{v\kappa_{ij}(\partial_x\phi^n_{ij}+i\partial_y\phi^n_{ij})}
{1+|v\kappa_{ij}(\partial_x\phi^n_{ij}+i\partial_y\phi^n_{ij})|/10},
\]

\[
C_{ij}=\frac{A_{ij}\psi^n_{ij}}{1+|A_{ij}\psi^n_{ij}|/10}.
\]

The NumPy diffusive branch performs the ordered map

\[
\psi_a=\psi^n+hG,
\qquad
\psi_b=\psi_a+hC,
\]

\[
\psi_c=(1-0.005h)\psi_b,
\qquad
\psi^{n+1}=\psi_c+hD_\psi\kappa\mathcal L_\kappa\psi_c.
\]

With mode coupling disabled, the second field then updates as

\[
\phi_a=\phi^n+h\kappa r\left(\frac{128}{N}\right)^2
(|\psi^{n+1}|^2-\phi^n),
\]

\[
\phi^{n+1}=\phi_a+0.05D_\phi\kappa\mathcal L_\kappa\phi_a.
\]

The final diffusion term in \(\phi\) has no \(h\) multiplier in the audited update. Hard caps and resets are omitted from these equations only because the comparison remains far from their thresholds. If a cap or reset activates, the run should be classified as numerically invalid for physics inference rather than as evidence of a physical saturation mechanism.

### 5.1 The wave branch is a different map

With nonlinear operator \(\mathcal N(\psi)=G+C(\psi)\), the PyTorch wave branch applies

\[
\psi_{1/2}=\psi^n+\frac h2\mathcal N(\psi^n),
\]

\[
\widehat\psi_L=e^{iD_\psi\Lambda(\mathbf k)h}\widehat\psi_{1/2},
\]

\[
\psi^{n+1}=\psi_L+\frac h2\mathcal N(\psi_L).
\]

The linear spectral substep is unitary, but the complete update is not: nonlinear interaction, field transfer, optional projection, boundary damping, caps, resets, and \(\phi\) evolution remain outside that unitary substep. The FFT exponential also has a global real-space kernel and is not a strict finite-neighbor cellular-automaton update.

## 6. Reproduced Backend Divergence

The test uses a \(32\times32\) complex Gaussian wave packet, a smooth nonuniform \(\phi\) field, \(\kappa=1\), \(h=0.1\), LAP4, no noise, no mode coupling, no \(\mu\), and no absorbing boundary. The same initial arrays are sent through the audited NumPy and PyTorch CPU dispatches.

### 6.1 Cross-backend result

| Steps | Diffusion-mode \(\psi\) relative \(L^2\), NumPy vs PyTorch | Wave-mode \(\psi\) relative \(L^2\), NumPy vs PyTorch | Wave-mode \(\phi\) relative \(L^2\) | NumPy “wave” norm | PyTorch wave norm |
|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 0.00149034 | \(1.63518\times10^{-6}\) | 38.49524 | 38.58041 |
| 10 | \(4.36\times10^{-21}\) | 0.01493249 | \(9.07143\times10^{-5}\) | 38.59659 | 39.45731 |
| 100 | \(2.57\times10^{-17}\) | 0.15356323 | 0.00921926 | 40.04951 | 49.83494 |

The NumPy output requested as `wave_baseline` is bitwise identical to its diffusion output at all three checkpoints. PyTorch executes the spectral wave branch. After 100 steps, the two \(\psi\) states differ by 15.36% in relative \(L^2\) norm.

**Interpretation:** the diffusive path is already a backend-consistent software candidate. The wave path is not one backend-independent model and cannot yet be called canonical.

### 6.2 Coefficient audit at constant \(\kappa=0.5\)

| Quantity | Whitepaper-level value or sign | Reconstructed runtime value | Consequence |
|---|---:|---:|---|
| \(\phi\) reaction coefficient | \(\kappa\alpha=0.00035\) | 0.00035 | aligned in the non-mode-coupling branch at \(N=128\) |
| \(\phi\) diffusion coefficient | \(\kappa\beta=0.0075\) | \(0.05\times0.30\times\kappa^2=0.00375\) | runtime applies neighbor and center \(\kappa\) weighting, giving half the displayed value |
| \(\psi\) diffusion coefficient | implicit unscaled \(\nabla^2\psi\) | \(0.05\kappa^2=0.0125\) | the displayed equation does not identify the runtime coefficient |
| damping | configured 0.00462 | fixed 0.005 | runtime is 8.225% larger and does not read the configured value |
| small-gradient drift | displayed as \(+\nabla\phi\) | approximately \(-0.004\kappa\nabla\phi=-0.002\nabla\phi\) before limiting | sign and magnitude do not match the stated uphill drift |
| \(\phi\) time scaling | same step convention as the update | diffusion is not multiplied by \(h\) | changing \(h\) changes reaction/diffusion balance |

The coefficient audit does not prove which formulation is physically preferable. It proves that the displayed equation and executable update are not presently the same mathematical object.

## 7. Gate 0 Options

| Option | Executable evidence | Backend identity | Scientific claim boundary | Migration cost | Recommendation |
|---|---|---|---|---|---|
| A. Declare the entire current mixed runtime canonical | high, but for several branches | **fails** | ambiguous: diffusive, wave, stochastic, projected, and capped behaviors mix | low | **reject** |
| B. Freeze deterministic diffusion as `RD-0` software reference | high | **passes in the tested path** | honest as an effective dimensionless benchmark | low | **recommend as the next small step** |
| C. Promote the unitary wave branch | partial; PyTorch only | **fails** | linear substep unitary, full system open and nonunitary; global FFT | medium | defer until a NumPy-equivalent law and boundary contract exist |
| D. Promote Eq-11.1 | contradictory narrative and negative-result history; no single recoverable canonical implementation | unknown | plausible only as an effective open PDE, not particle physics | high | retain as research candidate |
| E. Promote the biharmonic bounded PDE | analytical promise, no audited reference implementation | unknown | effective pattern-forming PDE; finite-scale particle selection not established | high | retain as research candidate |

The recommendation does not assert that diffusion is the final Lineum physics. It identifies the only tested branch that can presently serve as a common software ruler without a large rewrite.

## 8. Proposed `RD-0` Boundary

If approved, `RD-0` should initially freeze only the following:

1. **Purpose:** deterministic implementation benchmark for effective coupled-field evolution.
2. **State:** complex \(\psi\), real \(\phi\), and a fixed declared \(\kappa\) fixture; \(\mu\), stochastic generation, and external inputs excluded.
3. **Domain:** dimensionless 2D periodic square lattice.
4. **Operator:** LAP4 finite-neighbor diffusive branch only.
5. **Numerics:** fixed step size, explicit parameter record, no hidden backend selection.
6. **Safety:** a cap or reset is a failed run, not part of the physics.
7. **Backend contract:** NumPy and PyTorch CPU must agree within a declared tolerance for the complete state, not merely aggregate metrics.
8. **Claim boundary:** no SI calibration, particle identity, quantum unitarity, Lorentz invariance, gravity, black hole, or ontic-lattice claim.

One conceptual point remains deliberately open rather than silently selected:

- whether \(\kappa\) is part of the reference law or only an externally supplied environment map;

The project owner approved freezing the exact current ordered map first, including its edge gradient and missing \(h\) on \(\phi\)-diffusion. These behaviors are frozen only as a measurement baseline, not endorsed as correct physics. Each discrepancy can now be changed separately with a measured before/after result.

## 9. Acceptance Roadmap

The complete RD-0 roadmap contains these tests:

1. same initial state and parameters produce the same complete \(\psi,\phi\) arrays on NumPy and PyTorch CPU within \(\mathrm{rtol}=10^{-12}\), \(\mathrm{atol}=10^{-13}\);
2. requesting an unsupported physics mode fails explicitly instead of silently running diffusion;
3. every configurable parameter either changes the update or is rejected as unsupported;
4. boundary behavior is explicitly periodic and tested at all four edges;
5. halving \(h\) and doubling the number of steps is measured against the original horizon;
6. caps and resets remain at zero activation in every accepted reference run;
7. the complete reference state and configuration receive reproducible fingerprints.

The approved first increment implements items 1 and 7 for one smooth fixture and confirms item 6 at all three checkpoints. The other items remain explicit future gates. Passing the complete roadmap would validate a software law. It would not validate a physical theory of nature.

## 10. Approved RD-0 Characterization Result

The owner approved the following decision on July 16, 2026:

> **Freeze the exact current deterministic diffusive behavior as a measurement baseline before correcting it. Preserve known discrepancies so that every later correction has an auditable before/after comparison.**

The first implementation increment changed no solver equation, runtime dispatch, default, or whitepaper claim. It added an independently executable regression contract around this fixed fixture:

- grid: \(32\times32\), periodic LAP4 neighbor operator;
- \(h=0.1\), \(D_\psi=D_\phi=0.05\), reaction strength \(0.0007\), drift strength \(-0.004\);
- constant \(\kappa=1\), \(\mu=0\), zero external \(\delta\);
- stochastic generation, mode coupling, and PML disabled;
- checkpoints after 1, 10, and 100 ordered updates.

The complete \(\psi\) real part, \(\psi\) imaginary part, and \(\phi\) array are multiplied by \(10^{12}\), rounded to signed integers, serialized as little-endian 64-bit arrays with component names and shapes, and hashed with SHA-256. This gives a full-state fingerprint with resolution \(10^{-12}\); it is deliberately not described as bitwise identity.

| Step | RD-0 full-state SHA-256 at \(10^{-12}\) resolution | \(\sum|\psi|^2\) | \(\sum\phi\) |
|---:|---|---:|---:|
| 1 | `b4a47af600aecced9718600330b8e618d4f6888ec2465acf2f611dcc399fd3af` | 38.495239595839806 | 255.75639466834733 |
| 10 | `e57d5a18a8ef8dbed48fe06eccc3108251ecda1afa7f1855801374092a5faf3f` | 38.59659161057613 | 253.57674659985213 |
| 100 | `211dda7f2230625c9f4f1d92982dc022c1f6b6c7e3ba3aadffe5d0c78719418f` | 40.049514813584835 | 233.01762766274334 |

The backend comparison covers every array element:

| Step | \(\psi\) relative L2 | \(\phi\) relative L2 | max \(|\Delta\psi|\) | max \(|\Delta\phi|\) |
|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 |
| 10 | \(4.3629\times10^{-21}\) | \(6.9149\times10^{-18}\) | \(2.7105\times10^{-20}\) | \(5.5511\times10^{-17}\) |
| 100 | \(2.5707\times10^{-17}\) | \(2.5947\times10^{-17}\) | \(1.1102\times10^{-16}\) | \(1.1102\times10^{-16}\) |

The contract was executed with Python 3.11.15, NumPy 1.26.4, and PyTorch 2.5.1+cu121 on CPU. Both the audited working state and an isolated clean source snapshot produced `2 passed`; no cap, reset, or non-finite value activated. The clean-snapshot check matters because execution-policy work was present in the audited working state: it demonstrates that the RD-0 result is a property of the already committed diffusive update, not an accidental dependency on that unfinished policy work.

This passes only the first **RD-0 characterization increment**. Full Gate 0 remains open until mode rejection, parameter semantics, boundary controls, time-step refinement, and broader fixtures are resolved.

## 11. Phi-Diffusion Time-Step Refinement

### 11.1 Question and two competing interpretations

The experiment asks whether a trajectory at a fixed declared physical time \(T\) approaches one result as the integration step \(h\) is reduced. The audited ordered map applies the \(\phi\) reaction with \(h\), but applies \(\phi\)-diffusion without it:

\[
\phi_{n+1}
=\phi_n+hR(\psi_n,\phi_n)
+\kappa D_\phi\mathcal L_\kappa[\phi_n].
\]

The tested hypothetical candidate is

\[
\phi_{n+1}^{\mathrm{candidate}}
=\phi_n+hR(\psi_n,\phi_n)
+h\kappa D_\phi\mathcal L_\kappa[\phi_n].
\]

The first equation can still define a discrete automaton in which `phi_diffusion` is a per-update mixing fraction. It cannot simultaneously treat \(h\) as a freely refinable physical-time step while keeping the same diffusion coefficient. The second equation is the usual explicit-Euler interpretation of a diffusion term in a continuous-time PDE.

### 11.2 Analytically checkable isolated mode

To isolate the issue, set \(\psi=0\), reaction and drift to zero, \(\kappa=1\), and initialize

\[
\phi_{ij}(0)=0.5+0.1\cos\left(\frac{2\pi i}{32}\right)
\cos\left(\frac{2\pi j}{32}\right).
\]

For this LAP4 Fourier mode,

\[
\lambda_4=4\cos\left(\frac{2\pi}{32}\right)-4
=-0.07685887838707828.
\]

With \(D_\phi=0.05\), the inner Laplace rate \(r_L=0.05\), and \(\alpha=D_\phi r_L=0.0025\), the amplitude ratios at \(T=10\) are exactly

\[
\frac{A_h^{\mathrm{current}}(T)}{A_0}
=(1+\alpha\lambda_4)^{T/h},
\qquad
\frac{A_h^{\mathrm{candidate}}(T)}{A_0}
=(1+h\alpha\lambda_4)^{T/h}.
\]

The candidate has the finite limit \(\exp(\alpha\lambda_4T)=0.9980803728857736\). For the current rule, the effective diffusion per declared unit time is proportional to \(1/h\); every nonconstant stable Fourier mode is driven toward zero as \(h\rightarrow0\).

| \(h\) | Steps to \(T=10\) | Current amplitude ratio | Candidate amplitude ratio |
|---:|---:|---:|---:|
| 0.2 | 50 | 0.9904377291366023 | 0.9980803360351589 |
| 0.1 | 100 | 0.9809668952972694 | 0.9980803544607016 |
| 0.05 | 200 | 0.9622960496691637 | 0.9980803636732973 |
| 0.025 | 400 | 0.9260136872088776 | 0.9980803682795497 |

Across the tested steps, the current amplitude ratios span `0.06442404192772477`; the candidate ratios span only `3.224439082405439e-08` and approach the analytic continuum limit. Numerical and analytic ratios agree within \(8.8818\times10^{-15}\).

### 11.3 Coupled RD-0 refinement

The same comparison was repeated with the full deterministic RD-0 Gaussian \(\psi\) packet and smooth \(\phi\) fixture, keeping the final declared time at \(T=10\). Each row compares a coarse result with the next halved-step result; errors use the finer state as the denominator.

| Coarse/fine \(h\) | Current \(\phi\) relative L2 | Candidate \(\phi\) relative L2 | Current \(\psi\) relative L2 | Candidate \(\psi\) relative L2 |
|---:|---:|---:|---:|---:|
| 0.2 / 0.1 | 0.001788257370643413 | 0.00005472604949309865 | 0.00004983371913436278 | 0.00020154848536682308 |
| 0.1 / 0.05 | 0.003492066024134346 | 0.00002733544309864967 | 0.0002991370408839292 | 0.00010083083048908117 |
| 0.05 / 0.025 | 0.006706569703660991 | 0.000013660892239002042 | 0.0007104033537449127 | 0.000050429604214551325 |

When \(h\) is halved, the current \(\phi\) discrepancy grows by factors `1.952775971435199` and `1.9205162953136015`. The candidate discrepancy shrinks by factors `2.0020180135950105` and `2.000999833715611`, the expected signature of first-order convergence. The candidate \(\psi\) discrepancy also halves; the current \(\psi\) discrepancy grows.

### 11.4 Runtime cross-check

The standalone reconstruction was checked against the audited NumPy runtime for every tested \(h\) in both the legacy and time-scaled branches. The maximum isolated amplitude-ratio difference was exactly `0`; the maximum coupled \(\phi\) element difference was \(5.551115123125783\times10^{-17}\); and the maximum coupled \(\psi\) element difference was \(2.220446049250313\times10^{-16}\).

### 11.5 Historical-intent audit and conclusion

The source history makes the likely intent more nuanced than a simple typographical omission. Before the March 3, 2026 configuration refactor, both the baseline \(\phi\) reaction and \(\phi\)-diffusion were written as per-update increments without an explicit `DT` multiplier. Revision `ce5c855bde32dd2f0b37d247f65061ef6fba2550` then multiplied the reaction by configurable `cfg.dt` but left \(\phi\)-diffusion unchanged. The same revision already multiplied \(\psi\)-drift, interaction, damping, and \(\psi\)-diffusion by `cfg.dt`. No adjacent comment or commit rationale identifies \(\phi\)-diffusion as an intentional exception.

The canonical whitepaper also describes its main update as a per-step increment with the internal scheme step absorbed and labels at least one coefficient as a per-step quantity. That provides evidence that early Lineum semantics were closer to a discrete update rule than to a conventional method-of-lines PDE integrator.

The most defensible interpretation is therefore:

1. the original absence of an explicit \(h\) may have been compatible with a deliberate per-update automaton convention;
2. after `dt` became a configurable integration parameter and neighboring terms adopted it, retaining only \(\phi\)-diffusion in per-update units created mixed time semantics;
3. the present behavior is best classified as **legacy time-semantics migration debt**, and as a numerical defect whenever `dt` is used to refine a fixed physical-time trajectory.

The evidence supports this narrow conclusion with high confidence:

> **If `dt`/\(h\) represents physical or continuum time, the missing factor on \(\phi\)-diffusion is a numerical inconsistency. Multiplying that term by \(h\) restores the expected refinement behavior in both the isolated analytic control and the coupled RD-0 fixture.**

This does not prove that the candidate is the final Lineum law, nor does it decide the physical value or units of \(D_\phi\). If Lineum instead chooses a strictly discrete per-update automaton semantics, the legacy term may be retained, but then changing \(h\) changes the model rather than merely refining its integration.

### 11.6 Opt-in `RD-0-C1` implementation result

The implementation adds one explicit configuration value, `phi_diffusion_scales_with_dt`, whose default is `False`. Both NumPy and PyTorch CPU compute the same step scale:

\[
s_\phi=
\begin{cases}
h,&\text{if `phi_diffusion_scales_with_dt=True`,}\\
1,&\text{otherwise,}
\end{cases}
\qquad
\Delta\phi_{\mathrm{diff}}=s_\phi\kappa D_\phi\mathcal L_\kappa(\phi).
\]

The first implementation test increment verifies four properties:

1. the option is off by default;
2. legacy RD-0 full-state fingerprints at steps 1, 10, and 100 remain unchanged;
3. the opt-in isolated and coupled trajectories reproduce the analytic and standalone refinement results;
4. complete NumPy and PyTorch CPU candidate states agree within \(\mathrm{rtol}=10^{-12}\), \(\mathrm{atol}=10^{-13}\), with no cap activation.

The targeted candidate, legacy-characterization, and core-math test set produced `9 passed` in the audited working state. An isolated Git tree containing only the intended candidate changes initially produced `8 passed, 1 failed`: the failure occurred in a pre-existing generic smoke test because the base revision automatically selected a visible `sm_120` GPU unsupported by its PyTorch build. The candidate tests had already passed, and the failure occurred before candidate arithmetic was reached. Repeating the exact isolated tree with CUDA hidden produced `9 passed`; the dedicated candidate parity test still executed PyTorch explicitly on CPU, so backend comparison was not skipped. This separates candidate correctness from the independently pending execution-device policy work.

No default equation, stochastic linon/noise setting, dispatch rule, whitepaper claim, or RD-0 fingerprint changed. The new branch changes behavior only when the opt-in value is explicitly enabled.

## 12. Numerical Time, Internal Clocks, and Stochastic Semantics

### 12.1 Four distinct meanings of time

The project must not use one word, “time,” for four different structures:

1. **causal order \(n\):** the sequence stating which field state is evaluated before another;
2. **numerical step \(h\):** the resolution used to approximate a declared evolution parameter \(t\);
3. **operational or internal clocks:** repeatable processes inside the model, such as phase rotation, damping, diffusion, propagation, or a localized structure traversing a distance;
4. **time arrow:** irreversible loss of recoverable information through damping, diffusion, coarse-graining, or stochastic branching.

Setting `phi_diffusion_scales_with_dt=True` addresses only item 2. It means that increasing the temporal resolution changes the number of computational updates but not the intended trajectory. It does not assert that \(t\) is an ontologically fundamental universal clock.

The project-owner hypothesis that time may be measured by \(\psi\)-wave friction, permeability of the medium, or a linon’s interaction with its environment is compatible with this separation. Those processes can define **rates relative to \(t\)** and may later define an operational proper clock. They do not by themselves supply causal ordering; a relational reformulation would still need one dynamical variable to serve as a clock for the others.

Current deterministic rates already imply characteristic simulation-time scales. For uniform \(\kappa=1\), the lowest tested two-axis LAP4 mode has

| Process | Characteristic time in current dimensionless \(t\) units |
|---|---:|
| hard-coded global \(\psi\) damping, rate \(0.005\) | 200.0 |
| low-mode \(\psi\) diffusion, coefficient \(0.05\) | 260.2171722995434 |
| low-mode `RD-0-C1` \(\phi\) diffusion, effective coefficient \(0.0025\) | 5204.343445990867 |

These rates can be slowed or reshaped by the field state and \(\kappa\). The present solver nevertheless has one global update parameter and no derived local proper-time field. It also has no explicit velocity-dependent “linon friction” law; that phrase currently refers only to field damping, diffusion, drift, and interaction interpreted at the level of detected structures.

### 12.2 Deterministic falsification results

The opt-in candidate was challenged beyond the original smooth fixture.

**Fourier controls.** On a \(32\times32\) periodic grid at \(h=0.1\), \(T=10\), four modes matched the exact discrete LAP4 amplification law:

| Mode \((m_x,m_y)\) | LAP4 eigenvalue | Analytic amplitude ratio | Observed ratio | Absolute error |
|---:|---:|---:|---:|---:|
| (1,0) | -0.03842943919353914 | 0.9990397207685476 | 0.9990397207685489 | \(1.2212\times10^{-15}\) |
| (1,1) | -0.07685887838707828 | 0.998080354460703 | 0.9980803544607025 | \(4.4409\times10^{-16}\) |
| (2,3) | -0.4893017103723363 | 0.9878412315137362 | 0.9878412315137292 | \(6.9944\times10^{-15}\) |
| (8,8) | -4.0 | 0.9047921471137089 | 0.9047921471137096 | \(6.6613\times10^{-16}\) |

**Periodic edge control.** A \(+0.1\) impulse at the upper-left corner produced a center decrement of approximately \(-10^{-4}\) and equal \(+2.5\times10^{-5}\) increments in all four neighbors, including the two wrapped neighbors on the opposite edges.

**Nonuniform-medium control.** With smooth \(\kappa\in[0.3,0.9]\), pairwise \(\phi\) errors for \(h=0.2/0.1\), \(0.1/0.05\), and \(0.05/0.025\) were `3.4681650239936567e-09`, `1.733968527375885e-09`, and `8.669556780505624e-10`. Error reduction factors were `2.000131472537297` and `2.0000659448645504`, consistent with first-order convergence.

**Stability control.** For the highest-frequency checkerboard mode, the predicted uniform LAP4 limit is \(h_{\max}=100\). One step at \(h=99\) had amplitude factor \(-0.98\), while \(h=101\) had factor \(-1.02\) and therefore grew in magnitude. This matches the analytic explicit-Euler boundary.

The permanent falsification suite produced `8 passed`, including nonuniform-\(\kappa\) NumPy/PyTorch CPU parity. These results materially reduce the risk that the earlier success was caused by one unusually smooth mode or one backend.

### 12.3 Why stochastic time requires a separate contract

The current stochastic source is schematically

\[
\Delta\psi_n=h\left(aB_n+\sigma Z_n\right),
\]

where \(B_n\) is a Bernoulli linon-source mask and \(Z_n\) is Gaussian noise. In a frozen source-only control with probability \(p\), after \(T/h\) steps,

\[
\mathbb E[\Delta\psi(T)]=Tpa,
\qquad
\operatorname{Var}[\Delta\psi(T)]
=Th\left(a^2p(1-p)+\sigma^2\right).
\]

The mean is step-independent, but the standard deviation is proportional to \(\sqrt h\) and vanishes as \(h\rightarrow0\). A conventional finite-variance Gaussian stochastic differential equation instead uses an increment proportional to \(\sqrt h\). A Poisson jump process requires a declared rate, step-dependent event probability such as \(1-e^{-\lambda h}\), and a separately defined jump amplitude. Neither physical interpretation is currently declared for the combined linon/noise source.

The nonlinear runtime complicates the source-only result because each initial fluctuation also selects a complex phase and later linon-source terms reinforce that phase. Two ensemble experiments separate these effects.

**Vacuum branch selection.** Starting every run at exact \(\psi=0\), 128 seeds produce a persistent ensemble spread:

| \(h\) | Steps to \(T=2\) | Mean cellwise complex ensemble std. | Mean total \(\psi\) energy |
|---:|---:|---:|---:|
| 0.2 | 10 | 0.02881458225082336 | 0.07378548000540894 |
| 0.1 | 20 | 0.027996834103568465 | 0.06904762936513884 |
| 0.05 | 40 | 0.02747828967664654 | 0.06621789351723734 |
| 0.025 | 80 | 0.02720371152154367 | 0.06487020763061033 |

The spread-reduction factors when \(h\) halves are `1.0292`, `1.0189`, and `1.0101`, approaching 1 rather than \(\sqrt2\). The initial tiny perturbation therefore selects a persistent phase branch.

**Ongoing stochastic branching.** Starting all seeds from the same nonzero complex wave removes the singular phase choice and measures only new randomness added over \(T=1\):

| \(h\) | Steps | Mean cellwise complex ensemble std. | Energy of ensemble-mean \(\psi\) |
|---:|---:|---:|---:|
| 0.2 | 5 | 0.007258234066983663 | 0.08529647704710092 |
| 0.1 | 10 | 0.005179413153950338 | 0.084696643068043 |
| 0.05 | 20 | 0.0036780697661307803 | 0.0845031895276381 |
| 0.025 | 40 | 0.002604566167739291 | 0.08428553361262872 |

Here the reduction factors are `1.4014`, `1.4082`, and `1.4122`, close to \(\sqrt2\). A 1,000-resample bootstrap gives the following 95% intervals: `[1.3801, 1.4218]`, `[1.3875, 1.4309]`, and `[1.3888, 1.4349]`. The result is therefore not explained by an unusually convenient set of 128 seeds.

The standalone stochastic reconstruction matched the audited NumPy runtime exactly for the selected seed, step-size, vacuum, and nonzero-state cross-checks; maximum elementwise difference was `0`.

The narrow supported interpretation is:

- vacuum noise can select persistent emergent branches;
- fresh stochastic forcing after a shared nonzero state vanishes as \(\sqrt h\) under the current increment convention;
- the present mechanism is therefore closer to stochastic initial-branch selection plus an increasingly deterministic mean source than to a demonstrated continuously driven quantum vacuum.

### 12.4 Canonical recommendation

The validation assessment is split:

| Decision layer | Assessment | Recommendation |
|---|---|---|
| deterministic continuous-time Lineum | **explicit profile implemented** | use `rd0-c1-deterministic-continuous-time-v1` only for the validated deterministic lane |
| historical reproducibility | **explicit profile implemented** | use `legacy-per-update-v1`; the unnamed default also remains unchanged |
| stochastic linon/foam dynamics | **needs revision before canonical promotion** | define whether randomness is initial branch selection, Gaussian SDE forcing, Poisson events, or a specified combination |
| fundamental physical time | **unverified** | treat \(t\) as an evolution parameter; test internal clocks before any proper-time or gravitational interpretation |

Thus `RD-0-C1=True` is supported for every simulation claiming refinement of the same continuous-time trajectory. It is necessary but insufficient for a canonical stochastic Lineum model. The unresolved stochastic contract is not evidence that legacy `False` is preferable; it is a separate time-semantics problem.

### 12.5 Named-profile implementation gate

On July 16, 2026, the project owner authorized the next small code gate. Two stable names now make the time convention explicit rather than requiring callers to know a hidden Boolean:

| Stable profile name | Fixed identity | Adjustable values | Intended use |
|---|---|---|---|
| `legacy-per-update-v1` | `phi_diffusion_scales_with_dt=False` | all non-identity `CoreConfig` values | historical reproduction and unchanged default behavior |
| `rd0-c1-deterministic-continuous-time-v1` | `phi_diffusion_scales_with_dt=True`; noise disabled; diffusive \(\psi\); LAP4; mode coupling off; \(\mu\) off; PML off | \(h\), diffusion coefficients, reaction, drift, dissipation, and numerical safety values | deterministic refinement of one declared continuous-time trajectory |

The continuous-time profile defaults to \(h=0.1\), the characterized RD-0 value, but deliberately permits \(h\) to change. Preventing a change in \(h\) would make refinement testing impossible. Attempts to change any fixed identity value raise an error instead of silently creating a third, mislabeled model. An unknown profile name also raises an error; the generic word `canonical` is intentionally not accepted because it is ambiguous in the historical corpus.

The verification matrix contained 27 passing cases:

| Verification group | Cases | Result |
|---|---:|---|
| named-profile discovery, defaults, adjustable refinement values, rejected identity changes, and unknown-name rejection | 13 | passed |
| RD-0 legacy characterization and backend comparison | 2 | passed |
| original C1 time-refinement candidate tests | 4 | passed |
| broader Fourier, boundary, nonuniform-medium, stability, and backend falsification using the named continuous-time profile | 8 | passed |

The broader eight-case suite now obtains its configuration through the named profile rather than reconstructing the Boolean choice by hand. This is the physical enforcement point: future drift in profile identity will fail the same tests that support the deterministic recommendation.

This gate does **not** switch the historical simulator, audit run, stochastic linon dynamics, or any unnamed default to the new convention. It creates an explicit opt-in lane only. It also does not establish that the RD-0 subset is fundamental physics.

## 13. Limitations and Robustness

- The backend comparison isolates deterministic evolution. It does not assess stochastic equivalence across random-number generators.
- The comparison disables the absorbing boundary to isolate bulk dynamics. Boundary policy remains a separate Gate 0 choice.
- The initial characterization used one smooth state, but the later deterministic suite adds an impulse, periodic edges, four Fourier modes, nonuniform \(\kappa\), and an analytic stability boundary.
- The fingerprint is sensitive at \(10^{-12}\) resolution but is not a proof of bitwise portability across every future Python, NumPy, PyTorch, compiler, or CPU combination.
- The stochastic ensemble uses an \(8\times8\) source-isolation control, 128 seeds, and short horizons. It distinguishes branch selection from ongoing forcing but does not validate long-lived linon counts, collisions, or macroscopic observables.
- The hypothetical time-scaled branch tests numerical consistency only. It does not calibrate \(h\), \(D_\phi\), or any field to SI units.
- The source snapshot contained uncommitted work. Revision identifiers and working-tree counts are therefore recorded explicitly.
- The option assessment concerns readiness for canonicalization, not ultimate scientific merit.
- No chart is used because three exact time checkpoints and five discrete options are clearer as audit tables than as plots.

## 14. Decision Record and Next Gate

The approved decision is:

> **Approve the three-layer separation and authorize only an `RD-0` characterization contract. Do not promote any current equation as fundamental Lineum physics.**

This decision preserves the long-term ambition of Lineum while giving the project one reproducible software baseline. It is reversible: a later wave, Eq-11.1, biharmonic, quantum-automaton, or other candidate can replace the scientific model after it reproduces the baseline controls and passes stronger physical tests.

The approved read-only experiment, opt-in implementation, broader deterministic falsification, and named-profile gate are complete. The historical default remains legacy, while deterministic continuous-time experiments now have an explicit fail-closed lane. The next material physics decision is the stochastic contract: initial-condition branching, Gaussian \(\sqrt h\) forcing, Poisson-rate events, or a declared hybrid must be chosen and falsified before stochastic canonical promotion. No fundamental-time, quantum-foam, particle, or gravitational whitepaper claim follows from this software decision.

## 15. Further Questions

1. Should \(\kappa\) be a fixed part of the Lineum law, an environmental coefficient map, or an extension?
2. Should continuous stochastic forcing use Gaussian \(\sqrt h\) increments, Poisson-rate linon events, initial-condition randomness only, or an explicitly tested hybrid?
3. Is locality a hard architectural requirement, or may a global spectral update remain a candidate if its nonlocal numerical kernel is declared?
4. Is the core research target an effective nonlinear medium, or must every retained candidate aim at fundamental spacetime?
5. Which single observable should be the first physical discriminator after software identity is achieved?

## 16. Preliminary Novelty Boundary

The broad idea “simple local rules generate autonomous particle-like structures” is established prior art, not a Lineum-exclusive discovery:

| Prior result | Demonstrated scope | Portable citation |
|---|---|---|
| Lenia | continuous cellular automata with more than 400 catalogued autonomous pattern species | Bert Wang-Chak Chan, “Lenia: Biology of Artificial Life,” *Complex Systems* 28(3), 2019, DOI [10.25088/ComplexSystems.28.3.251](https://doi.org/10.25088/ComplexSystems.28.3.251) |
| dissipative reaction-diffusion solitons | localized structures in two and three dimensions with particle-like motion and interaction | M. Bode, A. W. Liehr, C. P. Schenk, H.-G. Purwins, “Interaction of dissipative solitons: particle-like behaviour of localized structures in a three-component reaction-diffusion system,” *Physica D* 161, 2002, DOI [10.1016/S0167-2789(01)00360-8](https://doi.org/10.1016/S0167-2789(01)00360-8) |
| discrete Lorentz-covariant quantum automata | exact or controlled discrete Lorentz covariance in specified quantum-walk/automaton models | P. Arrighi, S. Facchini, M. Forets, “Discrete Lorentz covariance for quantum walks and quantum cellular automata,” *New Journal of Physics* 16, 2014, DOI [10.1088/1367-2630/16/9/093007](https://doi.org/10.1088/1367-2630/16/9/093007) |
| quantum-cellular-automaton electrodynamics | Maxwell behavior and composite-photon interpretation in a relativistic low-wave-vector regime | A. Bisio, G. M. D’Ariano, P. Perinotti, “Quantum cellular automaton theory of light,” *Annals of Physics* 368, 2016, DOI [10.1016/j.aop.2016.02.009](https://doi.org/10.1016/j.aop.2016.02.009) |

Lineum may still become scientifically novel through its **specific** coupled complex-field, memory-field, medium-map, optional long-memory, and stochastic-branch architecture, or through an unexpected verified result produced by that architecture. At present, however, uniqueness of the combination is not yet a demonstrated scientific discovery; a new combination of known ingredients and a substantial software system are not by themselves a new physical law.

A strong Lineum novelty claim would require at least one of the following:

1. a new mathematically characterized dynamical class or universality result;
2. linon candidates that retain localization, identity, conserved structure, dispersion, and collision behavior across \(h\), grid spacing, domain size, boundary controls, and independent implementations;
3. recovery of a nontrivial symmetry or known low-energy equation from fewer or different assumptions than existing models;
4. a quantitative falsifiable prediction not fitted into the model after observation;
5. independent reproduction and external technical review.

The present assessment is therefore **promising original research platform, not yet a major physical discovery**. The project has passed the “nontrivial dynamics exist” threshold and no longer resembles an immediate dead end. The possible size of the discovery cannot be assessed responsibly until particle criteria, stochastic time semantics, symmetry, scaling, and at least one discriminating prediction are resolved.

---

## Appendix A — Standalone Reproduction Program

The following NumPy program reconstructs the deterministic diffusive and spectral-wave maps used in the comparison and derives the RD-0 fingerprints above. It requires no Lineum repository or data file. It was executed with Python 3.11.15 and NumPy 1.26.4. Two consecutive runs produced bitwise-identical LF-normalized output. The program SHA-256 is `7027b161c9fdf263428fd4437d426b51d11f9575dc4e30d7d7d7e9ebda4242ac`.

```python
"""Standalone numerical reproduction for the Lineum Gate 0 decision brief."""

import hashlib
import json

import numpy as np


SIZE = 32
DT = 0.1
D_PSI = 0.05
D_PHI_CONFIG = 0.05
REACTION = 0.0007
DRIFT = -0.004
FINGERPRINT_SCALE = 10**12


def make_state(size=SIZE):
    y, x = np.mgrid[:size, :size]
    center = (size - 1) / 2
    radius2 = (x - center) ** 2 + (y - center) ** 2
    envelope = np.exp(-radius2 / (2 * 3.5**2))
    phase = 0.17 * x - 0.11 * y
    psi = envelope * np.exp(1j * phase)
    phi = 0.25 + 0.08 * np.cos(2 * np.pi * x / size) * np.cos(
        2 * np.pi * y / size
    )
    kappa = np.ones((size, size), dtype=np.float64)
    return psi.astype(np.complex128), phi.astype(np.float64), kappa


def weighted_laplace(field, kappa, rate):
    k_up = np.roll(kappa, 1, axis=0)
    k_down = np.roll(kappa, -1, axis=0)
    k_left = np.roll(kappa, 1, axis=1)
    k_right = np.roll(kappa, -1, axis=1)
    f_up = np.roll(field, 1, axis=0)
    f_down = np.roll(field, -1, axis=0)
    f_left = np.roll(field, 1, axis=1)
    f_right = np.roll(field, -1, axis=1)
    neighbors = (
        f_up * k_up
        + f_down * k_down
        + f_left * k_left
        + f_right * k_right
    )
    active = k_up + k_down + k_left + k_right
    return rate * (neighbors - active * field)


def common_terms(psi, phi, kappa):
    phi_clipped = np.clip(phi, 0.0, 10.0)
    interaction_factor = 0.1 * np.tanh(0.4 * phi_clipped * kappa)
    grad_phi_x, grad_phi_y = np.gradient(phi)
    flow = DRIFT * (grad_phi_x + 1j * grad_phi_y) * kappa
    flow = flow / (1.0 + np.abs(flow) / 10.0)

    def nonlinear(current_psi):
        interaction = interaction_factor * current_psi
        return flow + interaction / (1.0 + np.abs(interaction) / 10.0)

    return nonlinear


def update_phi(phi, psi, kappa):
    scale_ratio = (128.0 / SIZE) ** 2
    phi = phi + kappa * REACTION * scale_ratio * (np.abs(psi) ** 2 - phi) * DT
    # This term intentionally has no DT multiplier: it reproduces the audited update.
    phi = phi + kappa * D_PHI_CONFIG * weighted_laplace(
        phi, kappa, rate=0.05
    )
    return phi


def diffusion_step(psi, phi, kappa):
    phi_clipped = np.clip(phi, 0.0, 10.0)
    interaction_factor = 0.1 * np.tanh(0.4 * phi_clipped * kappa)
    interaction = interaction_factor * psi
    interaction = interaction / (1.0 + np.abs(interaction) / 10.0)
    grad_phi_x, grad_phi_y = np.gradient(phi)
    flow = DRIFT * (grad_phi_x + 1j * grad_phi_y) * kappa
    flow = flow / (1.0 + np.abs(flow) / 10.0)

    psi += flow * DT
    psi += interaction * DT
    psi -= 0.005 * psi * DT
    psi += weighted_laplace(psi, kappa, rate=D_PSI) * kappa * DT
    return psi, update_phi(phi, psi, kappa)


def lap4_fft_symbol(size):
    kernel = np.zeros((size, size), dtype=np.float64)
    kernel[0, 0] = -4.0
    kernel[1, 0] = kernel[-1, 0] = 1.0
    kernel[0, 1] = kernel[0, -1] = 1.0
    return np.fft.fft2(kernel).real


def wave_step(psi, phi, kappa):
    nonlinear = common_terms(psi, phi, kappa)
    psi = psi + nonlinear(psi) * (DT / 2.0)
    symbol = lap4_fft_symbol(SIZE)
    psi_hat = np.fft.fft2(psi)
    psi = np.fft.ifft2(psi_hat * np.exp(1j * D_PSI * symbol * DT))
    psi = psi + nonlinear(psi) * (DT / 2.0)
    return psi, update_phi(phi, psi, kappa)


def evolve(stepper, steps):
    psi, phi, kappa = make_state()
    for _ in range(steps):
        psi, phi = stepper(psi, phi, kappa)
    return psi, phi


def relative_l2(left, right):
    return float(np.linalg.norm(left - right) / (np.linalg.norm(left) + 1e-30))


def state_fingerprint(psi, phi):
    digest = hashlib.sha256()
    for name, component in (
        ("psi.real", psi.real),
        ("psi.imag", psi.imag),
        ("phi", phi),
    ):
        quantized = np.rint(component * FINGERPRINT_SCALE).astype("<i8")
        digest.update(name.encode("ascii"))
        digest.update(np.asarray(quantized.shape, dtype="<i8").tobytes())
        digest.update(np.ascontiguousarray(quantized).tobytes())
    return digest.hexdigest()


comparisons = []
for count in (1, 10, 100):
    diffusion_psi, diffusion_phi = evolve(diffusion_step, count)
    wave_psi, wave_phi = evolve(wave_step, count)
    comparisons.append(
        {
            "steps": count,
            "psi_relative_l2_diffusion_vs_wave": relative_l2(
                diffusion_psi, wave_psi
            ),
            "phi_relative_l2_diffusion_vs_wave": relative_l2(
                diffusion_phi, wave_phi
            ),
            "diffusion_norm": float(np.sum(np.abs(diffusion_psi) ** 2)),
            "diffusion_phi_sum": float(np.sum(diffusion_phi)),
            "rd0_quantized_state_sha256": state_fingerprint(
                diffusion_psi, diffusion_phi
            ),
            "wave_norm": float(np.sum(np.abs(wave_psi) ** 2)),
        }
    )

print(
    json.dumps(
        {
            "configuration": {
                "size": SIZE,
                "dt": DT,
                "noise_disabled": True,
                "mode_coupling": False,
                "mu": False,
                "pml": False,
                "stencil": "LAP4",
            },
            "constant_kappa_0_5_coefficients": {
                "runtime_phi_reaction": 0.5 * 0.0007,
                "whitepaper_phi_reaction": 0.5 * 0.0007,
                "runtime_phi_diffusion": 0.05 * 0.30 * 0.5**2,
                "whitepaper_phi_diffusion": 0.5 * 0.015,
                "runtime_psi_diffusion": 0.05 * 0.5**2,
                "runtime_damping_fixed": 0.005,
                "configured_damping": 0.00462,
                "damping_relative_difference": (0.005 - 0.00462) / 0.00462,
                "runtime_small_phi_drift_coefficient": -0.004 * 0.5,
            },
            "comparisons": comparisons,
            "dispatch_observation": (
                "The audited NumPy wave-mode dispatch executes diffusion_step; "
                "the PyTorch wave-mode dispatch executes wave_step."
            ),
            "rd0_fingerprint": {
                "algorithm": "SHA-256 over little-endian signed int64 arrays",
                "components": ["psi.real", "psi.imag", "phi"],
                "quantization_scale": FINGERPRINT_SCALE,
                "resolution": 1 / FINGERPRINT_SCALE,
            },
        },
        indent=2,
        sort_keys=True,
    )
)

```

## Appendix B — Full Reference Output

The output SHA-256 after normalizing line endings to LF and including the final newline is `f8ec27fd30717bf20d8eada9cfc67f6db34f8dc3d1a629e1815a043a74cb3775`.

```json
{
  "comparisons": [
    {
      "diffusion_norm": 38.495239595839806,
      "diffusion_phi_sum": 255.75639466834733,
      "phi_relative_l2_diffusion_vs_wave": 1.6351787835780562e-06,
      "psi_relative_l2_diffusion_vs_wave": 0.001490341110681058,
      "rd0_quantized_state_sha256": "b4a47af600aecced9718600330b8e618d4f6888ec2465acf2f611dcc399fd3af",
      "steps": 1,
      "wave_norm": 38.580413360465
    },
    {
      "diffusion_norm": 38.59659161057613,
      "diffusion_phi_sum": 253.57674659985213,
      "phi_relative_l2_diffusion_vs_wave": 9.071425004146495e-05,
      "psi_relative_l2_diffusion_vs_wave": 0.014932486520446023,
      "rd0_quantized_state_sha256": "e57d5a18a8ef8dbed48fe06eccc3108251ecda1afa7f1855801374092a5faf3f",
      "steps": 10,
      "wave_norm": 39.45731115125693
    },
    {
      "diffusion_norm": 40.049514813584835,
      "diffusion_phi_sum": 233.01762766274334,
      "phi_relative_l2_diffusion_vs_wave": 0.009219264698111216,
      "psi_relative_l2_diffusion_vs_wave": 0.1535632259025071,
      "rd0_quantized_state_sha256": "211dda7f2230625c9f4f1d92982dc022c1f6b6c7e3ba3aadffe5d0c78719418f",
      "steps": 100,
      "wave_norm": 49.83494026441414
    }
  ],
  "configuration": {
    "dt": 0.1,
    "mode_coupling": false,
    "mu": false,
    "noise_disabled": true,
    "pml": false,
    "size": 32,
    "stencil": "LAP4"
  },
  "constant_kappa_0_5_coefficients": {
    "configured_damping": 0.00462,
    "damping_relative_difference": 0.08225108225108228,
    "runtime_damping_fixed": 0.005,
    "runtime_phi_diffusion": 0.00375,
    "runtime_phi_reaction": 0.00035,
    "runtime_psi_diffusion": 0.0125,
    "runtime_small_phi_drift_coefficient": -0.002,
    "whitepaper_phi_diffusion": 0.0075,
    "whitepaper_phi_reaction": 0.00035
  },
  "dispatch_observation": "The audited NumPy wave-mode dispatch executes diffusion_step; the PyTorch wave-mode dispatch executes wave_step.",
  "rd0_fingerprint": {
    "algorithm": "SHA-256 over little-endian signed int64 arrays",
    "components": [
      "psi.real",
      "psi.imag",
      "phi"
    ],
    "quantization_scale": 1000000000000,
    "resolution": 1e-12
  }
}
```

## Appendix C — Standalone Canonical-Time Decision Suite

The following program reproduces the broader deterministic falsification, internal-rate examples, stochastic branch-selection experiment, ongoing-forcing experiment, and bootstrap intervals. It requires only NumPy and no Lineum repository or data file. It was executed with Python 3.11.15 and NumPy 1.26.4. Two consecutive runs produced bitwise-identical LF-normalized output. The embedded program SHA-256 is `2208d7c491173e24aa3d552527f221a268b59d29f333c79cabe6454fdf9dcc7e`.

```python
"""Standalone deterministic and stochastic time-semantics decision suite."""

import json

import numpy as np


SIZE = 32
PHYSICAL_TIME = 10.0
TIME_STEPS = (0.2, 0.1, 0.05, 0.025)
D_PHI = 0.05
PHI_LAPLACE_RATE = 0.05
PHI_ALPHA = D_PHI * PHI_LAPLACE_RATE

STOCHASTIC_SIZE = 8
STOCHASTIC_TIME = 2.0
STOCHASTIC_SEEDS = 128
NOISE_SIGMA = 0.005


def weighted_laplace(field, kappa, rate):
    k_up = np.roll(kappa, 1, axis=0)
    k_down = np.roll(kappa, -1, axis=0)
    k_left = np.roll(kappa, 1, axis=1)
    k_right = np.roll(kappa, -1, axis=1)
    f_up = np.roll(field, 1, axis=0)
    f_down = np.roll(field, -1, axis=0)
    f_left = np.roll(field, 1, axis=1)
    f_right = np.roll(field, -1, axis=1)
    neighbors = (
        f_up * k_up
        + f_down * k_down
        + f_left * k_left
        + f_right * k_right
    )
    active = k_up + k_down + k_left + k_right
    return rate * (neighbors - active * field)


def mode(mode_x, mode_y, size=SIZE):
    y, x = np.mgrid[:size, :size]
    return np.cos(2 * np.pi * mode_x * x / size) * np.cos(
        2 * np.pi * mode_y * y / size
    )


def mode_amplitude(phi, spatial_mode):
    centered = phi - np.mean(phi)
    return float(
        np.sum(centered * spatial_mode) / np.sum(spatial_mode**2)
    )


def evolve_phi(phi, kappa, dt, physical_time=PHYSICAL_TIME):
    phi = phi.copy()
    for _ in range(round(physical_time / dt)):
        phi += (
            dt
            * kappa
            * D_PHI
            * weighted_laplace(phi, kappa, PHI_LAPLACE_RATE)
        )
    return phi


def relative_to_reference(estimate, reference):
    return float(
        np.linalg.norm(estimate - reference)
        / (np.linalg.norm(reference) + 1e-30)
    )


multiple_modes = []
for mode_x, mode_y in ((1, 0), (1, 1), (2, 3), (8, 8)):
    spatial_mode = mode(mode_x, mode_y)
    initial_phi = 0.5 + 0.05 * spatial_mode
    final_phi = evolve_phi(initial_phi, np.ones_like(initial_phi), 0.1)
    observed = mode_amplitude(final_phi, spatial_mode) / 0.05
    eigenvalue = (
        2 * np.cos(2 * np.pi * mode_x / SIZE)
        + 2 * np.cos(2 * np.pi * mode_y / SIZE)
        - 4
    )
    expected = float(
        (1 + 0.1 * PHI_ALPHA * eigenvalue)
        ** round(PHYSICAL_TIME / 0.1)
    )
    multiple_modes.append(
        {
            "mode": [mode_x, mode_y],
            "lap4_eigenvalue": float(eigenvalue),
            "observed_amplitude_ratio": observed,
            "analytic_amplitude_ratio": expected,
            "absolute_error": abs(observed - expected),
        }
    )


edge_phi = np.full((SIZE, SIZE), 0.5, dtype=np.float64)
edge_phi[0, 0] += 0.1
edge_after = evolve_phi(edge_phi, np.ones_like(edge_phi), 0.1, 0.1)
edge_delta = edge_after - edge_phi
periodic_edge = {
    "center_delta": float(edge_delta[0, 0]),
    "down_neighbor_delta": float(edge_delta[1, 0]),
    "up_wrapped_neighbor_delta": float(edge_delta[-1, 0]),
    "right_neighbor_delta": float(edge_delta[0, 1]),
    "left_wrapped_neighbor_delta": float(edge_delta[0, -1]),
}


y, x = np.mgrid[:SIZE, :SIZE]
nonuniform_phi = 0.5 + 0.08 * mode(2, 1)
nonuniform_kappa = 0.6 + 0.3 * np.cos(2 * np.pi * x / SIZE) * np.cos(
    2 * np.pi * y / SIZE
)
nonuniform_states = {
    dt: evolve_phi(nonuniform_phi, nonuniform_kappa, dt)
    for dt in TIME_STEPS
}
nonuniform_errors = []
for coarse, fine in zip(TIME_STEPS, TIME_STEPS[1:]):
    nonuniform_errors.append(
        {
            "coarse_dt": coarse,
            "fine_dt": fine,
            "phi_relative_l2": relative_to_reference(
                nonuniform_states[coarse], nonuniform_states[fine]
            ),
        }
    )


checkerboard = mode(SIZE // 2, SIZE // 2)
stability = []
for dt in (99.0, 101.0):
    initial_phi = 0.5 + 0.1 * checkerboard
    final_phi = evolve_phi(initial_phi, np.ones_like(initial_phi), dt, dt)
    stability.append(
        {
            "dt": dt,
            "amplitude_ratio_after_one_step": mode_amplitude(
                final_phi, checkerboard
            )
            / 0.1,
        }
    )


def stochastic_run(dt, seed, initial_psi, physical_time):
    np.random.seed(seed)
    psi = initial_psi.astype(np.complex128).copy()
    kappa = np.ones((STOCHASTIC_SIZE, STOCHASTIC_SIZE), dtype=np.float64)
    for _ in range(round(physical_time / dt)):
        amplitude = np.abs(psi)
        grad_x, grad_y = np.gradient(amplitude)
        grad_magnitude = np.sqrt(grad_x**2 + grad_y**2)
        probability = 1.0 / (
            1.0 + np.exp(-5.0 * (amplitude + grad_magnitude))
        )
        linons = (
            np.random.rand(STOCHASTIC_SIZE, STOCHASTIC_SIZE) < probability
        ).astype(np.float64)
        linon_effect = (0.03 + 0.02 * amplitude) * linons
        phase = np.exp(1j * np.angle(psi))
        linon_complex = linon_effect * phase
        fluctuation = np.clip(
            np.random.normal(
                0.0,
                NOISE_SIGMA,
                (STOCHASTIC_SIZE, STOCHASTIC_SIZE),
            ),
            -1.0,
            1.0,
        ) * phase
        psi += (linon_complex + fluctuation) * kappa * dt
        psi -= 0.005 * psi * dt
    return psi


stochastic_rows = []
vacuum_ensembles = {}
vacuum = np.zeros(
    (STOCHASTIC_SIZE, STOCHASTIC_SIZE), dtype=np.complex128
)
for dt in TIME_STEPS:
    ensemble = np.stack(
        [
            stochastic_run(dt, seed, vacuum, STOCHASTIC_TIME)
            for seed in range(STOCHASTIC_SEEDS)
        ]
    )
    vacuum_ensembles[dt] = ensemble
    per_seed_spatial_mean = np.mean(ensemble.real, axis=(1, 2))
    cellwise_ensemble_std = np.std(ensemble.real, axis=0, ddof=1)
    cellwise_complex_std = np.sqrt(
        np.var(ensemble.real, axis=0, ddof=1)
        + np.var(ensemble.imag, axis=0, ddof=1)
    )
    stochastic_rows.append(
        {
            "dt": dt,
            "steps": round(STOCHASTIC_TIME / dt),
            "ensemble_mean_spatial_mean_real_psi": float(
                np.mean(per_seed_spatial_mean)
            ),
            "ensemble_std_spatial_mean_real_psi": float(
                np.std(per_seed_spatial_mean, ddof=1)
            ),
            "mean_cellwise_ensemble_std_real_psi": float(
                np.mean(cellwise_ensemble_std)
            ),
            "mean_cellwise_ensemble_std_complex_psi": float(
                np.mean(cellwise_complex_std)
            ),
            "ensemble_mean_total_psi_energy": float(
                np.mean(np.sum(np.abs(ensemble) ** 2, axis=(1, 2)))
            ),
        }
    )


branch_y, branch_x = np.mgrid[:STOCHASTIC_SIZE, :STOCHASTIC_SIZE]
branch_initial = 0.02 * np.exp(1j * (0.2 * branch_x - 0.1 * branch_y))
branch_rows = []
branch_ensembles = {}
for dt in TIME_STEPS:
    ensemble = np.stack(
        [
            stochastic_run(dt, seed, branch_initial, 1.0)
            for seed in range(STOCHASTIC_SEEDS)
        ]
    )
    branch_ensembles[dt] = ensemble
    cellwise_complex_std = np.sqrt(
        np.var(ensemble.real, axis=0, ddof=1)
        + np.var(ensemble.imag, axis=0, ddof=1)
    )
    ensemble_mean = np.mean(ensemble, axis=0)
    branch_rows.append(
        {
            "dt": dt,
            "steps": round(1.0 / dt),
            "mean_cellwise_ensemble_std_complex_psi": float(
                np.mean(cellwise_complex_std)
            ),
            "ensemble_mean_total_psi_energy": float(
                np.sum(np.abs(ensemble_mean) ** 2)
            ),
        }
    )


def mean_cellwise_complex_std(ensemble):
    return float(
        np.mean(
            np.sqrt(
                np.var(ensemble.real, axis=0, ddof=1)
                + np.var(ensemble.imag, axis=0, ddof=1)
            )
        )
    )


bootstrap_rng = np.random.default_rng(20260716)
bootstrap_repetitions = 1000
vacuum_bootstrap_factors = [[], [], []]
branch_bootstrap_factors = [[], [], []]
for _ in range(bootstrap_repetitions):
    indices = bootstrap_rng.integers(
        0, STOCHASTIC_SEEDS, size=STOCHASTIC_SEEDS
    )
    vacuum_spreads = [
        mean_cellwise_complex_std(vacuum_ensembles[dt][indices])
        for dt in TIME_STEPS
    ]
    branch_spreads = [
        mean_cellwise_complex_std(branch_ensembles[dt][indices])
        for dt in TIME_STEPS
    ]
    for index in range(3):
        vacuum_bootstrap_factors[index].append(
            vacuum_spreads[index] / vacuum_spreads[index + 1]
        )
        branch_bootstrap_factors[index].append(
            branch_spreads[index] / branch_spreads[index + 1]
        )


def bootstrap_intervals(samples):
    return [
        {
            "lower_95": float(np.percentile(values, 2.5)),
            "upper_95": float(np.percentile(values, 97.5)),
        }
        for values in samples
    ]


source_only_control = []
probability = 0.5
linon_amplitude = 0.03
source_variance = (
    linon_amplitude**2 * probability * (1 - probability)
    + NOISE_SIGMA**2
)
for dt in TIME_STEPS:
    source_only_control.append(
        {
            "dt": dt,
            "expected_final_mean": STOCHASTIC_TIME
            * probability
            * linon_amplitude,
            "expected_final_std_current_dt_scaling": float(
                np.sqrt(STOCHASTIC_TIME * dt * source_variance)
            ),
            "expected_final_std_sde_sqrt_dt_scaling": float(
                np.sqrt(STOCHASTIC_TIME) * NOISE_SIGMA
            ),
        }
    )


low_mode_eigenvalue = 4 * np.cos(2 * np.pi / SIZE) - 4
output = {
    "configuration": {
        "deterministic_grid_size": SIZE,
        "deterministic_physical_time": PHYSICAL_TIME,
        "time_steps": list(TIME_STEPS),
        "stochastic_grid_size": STOCHASTIC_SIZE,
        "stochastic_physical_time": STOCHASTIC_TIME,
        "stochastic_seed_count": STOCHASTIC_SEEDS,
    },
    "deterministic_candidate": {
        "multiple_fourier_modes": multiple_modes,
        "periodic_edge": periodic_edge,
        "nonuniform_kappa_pairwise_refinement": nonuniform_errors,
        "nonuniform_kappa_error_reduction_factors": [
            nonuniform_errors[0]["phi_relative_l2"]
            / nonuniform_errors[1]["phi_relative_l2"],
            nonuniform_errors[1]["phi_relative_l2"]
            / nonuniform_errors[2]["phi_relative_l2"],
        ],
        "uniform_checkerboard_stability": stability,
        "predicted_uniform_lap4_max_stable_dt": 2
        / (8 * PHI_ALPHA),
    },
    "stochastic_current_runtime_semantics": {
        "ensemble_results": stochastic_rows,
        "cellwise_std_reduction_factors_when_dt_halves": [
            stochastic_rows[0]["mean_cellwise_ensemble_std_complex_psi"]
            / stochastic_rows[1]["mean_cellwise_ensemble_std_complex_psi"],
            stochastic_rows[1]["mean_cellwise_ensemble_std_complex_psi"]
            / stochastic_rows[2]["mean_cellwise_ensemble_std_complex_psi"],
            stochastic_rows[2]["mean_cellwise_ensemble_std_complex_psi"]
            / stochastic_rows[3]["mean_cellwise_ensemble_std_complex_psi"],
        ],
        "common_nonzero_state_branching": branch_rows,
        "branching_std_reduction_factors_when_dt_halves": [
            branch_rows[0]["mean_cellwise_ensemble_std_complex_psi"]
            / branch_rows[1]["mean_cellwise_ensemble_std_complex_psi"],
            branch_rows[1]["mean_cellwise_ensemble_std_complex_psi"]
            / branch_rows[2]["mean_cellwise_ensemble_std_complex_psi"],
            branch_rows[2]["mean_cellwise_ensemble_std_complex_psi"]
            / branch_rows[3]["mean_cellwise_ensemble_std_complex_psi"],
        ],
        "branching_std_reduction_factor_bootstrap_95": bootstrap_intervals(
            branch_bootstrap_factors
        ),
        "vacuum_std_reduction_factor_bootstrap_95": bootstrap_intervals(
            vacuum_bootstrap_factors
        ),
        "bootstrap_repetitions": bootstrap_repetitions,
        "source_only_analytic_control": source_only_control,
    },
    "internal_rate_examples": {
        "global_psi_damping_time_constant": 1 / 0.005,
        "low_mode_psi_diffusion_time_constant_at_kappa_1": float(
            1 / (0.05 * abs(low_mode_eigenvalue))
        ),
        "low_mode_phi_diffusion_time_constant_at_kappa_1": float(
            1 / (PHI_ALPHA * abs(low_mode_eigenvalue))
        ),
    },
}

print(json.dumps(output, indent=2, sort_keys=True))
```

## Appendix D — Full Canonical-Time Decision Output

The output SHA-256 after normalizing line endings to LF and including the final newline is `a2d508368032cea8ba25c9970e0dc37a83d597101ce844005bf8d5a6515b9e6e`.

```json
{
  "configuration": {
    "deterministic_grid_size": 32,
    "deterministic_physical_time": 10.0,
    "stochastic_grid_size": 8,
    "stochastic_physical_time": 2.0,
    "stochastic_seed_count": 128,
    "time_steps": [
      0.2,
      0.1,
      0.05,
      0.025
    ]
  },
  "deterministic_candidate": {
    "multiple_fourier_modes": [
      {
        "absolute_error": 1.2212453270876722e-15,
        "analytic_amplitude_ratio": 0.9990397207685476,
        "lap4_eigenvalue": -0.03842943919353914,
        "mode": [
          1,
          0
        ],
        "observed_amplitude_ratio": 0.9990397207685489
      },
      {
        "absolute_error": 4.440892098500626e-16,
        "analytic_amplitude_ratio": 0.998080354460703,
        "lap4_eigenvalue": -0.07685887838707828,
        "mode": [
          1,
          1
        ],
        "observed_amplitude_ratio": 0.9980803544607025
      },
      {
        "absolute_error": 6.994405055138486e-15,
        "analytic_amplitude_ratio": 0.9878412315137362,
        "lap4_eigenvalue": -0.4893017103723363,
        "mode": [
          2,
          3
        ],
        "observed_amplitude_ratio": 0.9878412315137292
      },
      {
        "absolute_error": 6.661338147750939e-16,
        "analytic_amplitude_ratio": 0.9047921471137089,
        "lap4_eigenvalue": -3.9999999999999996,
        "mode": [
          8,
          8
        ],
        "observed_amplitude_ratio": 0.9047921471137096
      }
    ],
    "nonuniform_kappa_error_reduction_factors": [
      2.000131472537297,
      2.0000659448645504
    ],
    "nonuniform_kappa_pairwise_refinement": [
      {
        "coarse_dt": 0.2,
        "fine_dt": 0.1,
        "phi_relative_l2": 3.4681650239936567e-09
      },
      {
        "coarse_dt": 0.1,
        "fine_dt": 0.05,
        "phi_relative_l2": 1.733968527375885e-09
      },
      {
        "coarse_dt": 0.05,
        "fine_dt": 0.025,
        "phi_relative_l2": 8.669556780505624e-10
      }
    ],
    "periodic_edge": {
      "center_delta": -9.999999999998899e-05,
      "down_neighbor_delta": 2.5000000000052758e-05,
      "left_wrapped_neighbor_delta": 2.5000000000052758e-05,
      "right_neighbor_delta": 2.5000000000052758e-05,
      "up_wrapped_neighbor_delta": 2.5000000000052758e-05
    },
    "predicted_uniform_lap4_max_stable_dt": 99.99999999999999,
    "uniform_checkerboard_stability": [
      {
        "amplitude_ratio_after_one_step": -0.9799999999999994,
        "dt": 99.0
      },
      {
        "amplitude_ratio_after_one_step": -1.0199999999999994,
        "dt": 101.0
      }
    ]
  },
  "internal_rate_examples": {
    "global_psi_damping_time_constant": 200.0,
    "low_mode_phi_diffusion_time_constant_at_kappa_1": 5204.343445990867,
    "low_mode_psi_diffusion_time_constant_at_kappa_1": 260.2171722995434
  },
  "stochastic_current_runtime_semantics": {
    "bootstrap_repetitions": 1000,
    "branching_std_reduction_factor_bootstrap_95": [
      {
        "lower_95": 1.380100685682375,
        "upper_95": 1.421757148019419
      },
      {
        "lower_95": 1.387459161864581,
        "upper_95": 1.4308822629478066
      },
      {
        "lower_95": 1.3887844422350775,
        "upper_95": 1.4349241478590746
      }
    ],
    "branching_std_reduction_factors_when_dt_halves": [
      1.4013622492053581,
      1.408187849410732,
      1.4121621526410548
    ],
    "cellwise_std_reduction_factors_when_dt_halves": [
      1.0292085935227464,
      1.0188710590442107,
      1.0100934078383172
    ],
    "common_nonzero_state_branching": [
      {
        "dt": 0.2,
        "ensemble_mean_total_psi_energy": 0.08529647704710092,
        "mean_cellwise_ensemble_std_complex_psi": 0.007258234066983663,
        "steps": 5
      },
      {
        "dt": 0.1,
        "ensemble_mean_total_psi_energy": 0.084696643068043,
        "mean_cellwise_ensemble_std_complex_psi": 0.005179413153950338,
        "steps": 10
      },
      {
        "dt": 0.05,
        "ensemble_mean_total_psi_energy": 0.0845031895276381,
        "mean_cellwise_ensemble_std_complex_psi": 0.0036780697661307803,
        "steps": 20
      },
      {
        "dt": 0.025,
        "ensemble_mean_total_psi_energy": 0.08428553361262872,
        "mean_cellwise_ensemble_std_complex_psi": 0.002604566167739291,
        "steps": 40
      }
    ],
    "ensemble_results": [
      {
        "dt": 0.2,
        "ensemble_mean_spatial_mean_real_psi": 0.01787051141925871,
        "ensemble_mean_total_psi_energy": 0.07378548000540894,
        "ensemble_std_spatial_mean_real_psi": 0.0035329295364034887,
        "mean_cellwise_ensemble_std_complex_psi": 0.02881458225082336,
        "mean_cellwise_ensemble_std_real_psi": 0.02881458225082336,
        "steps": 10
      },
      {
        "dt": 0.1,
        "ensemble_mean_spatial_mean_real_psi": 0.017066526935238868,
        "ensemble_mean_total_psi_energy": 0.06904762936513884,
        "ensemble_std_spatial_mean_real_psi": 0.0034087546062588786,
        "mean_cellwise_ensemble_std_complex_psi": 0.027996834103568465,
        "mean_cellwise_ensemble_std_real_psi": 0.027996834103568465,
        "steps": 20
      },
      {
        "dt": 0.05,
        "ensemble_mean_spatial_mean_real_psi": 0.016603226985407026,
        "ensemble_mean_total_psi_energy": 0.06621789351723734,
        "ensemble_std_spatial_mean_real_psi": 0.0033186245019622956,
        "mean_cellwise_ensemble_std_complex_psi": 0.02747828967664654,
        "mean_cellwise_ensemble_std_real_psi": 0.02747828967664654,
        "steps": 40
      },
      {
        "dt": 0.025,
        "ensemble_mean_spatial_mean_real_psi": 0.01641395396640176,
        "ensemble_mean_total_psi_energy": 0.06487020763061033,
        "ensemble_std_spatial_mean_real_psi": 0.003285649392178308,
        "mean_cellwise_ensemble_std_complex_psi": 0.02720371152154367,
        "mean_cellwise_ensemble_std_real_psi": 0.02720371152154367,
        "steps": 80
      }
    ],
    "source_only_analytic_control": [
      {
        "dt": 0.2,
        "expected_final_mean": 0.03,
        "expected_final_std_current_dt_scaling": 0.01,
        "expected_final_std_sde_sqrt_dt_scaling": 0.007071067811865476
      },
      {
        "dt": 0.1,
        "expected_final_mean": 0.03,
        "expected_final_std_current_dt_scaling": 0.007071067811865475,
        "expected_final_std_sde_sqrt_dt_scaling": 0.007071067811865476
      },
      {
        "dt": 0.05,
        "expected_final_mean": 0.03,
        "expected_final_std_current_dt_scaling": 0.005,
        "expected_final_std_sde_sqrt_dt_scaling": 0.007071067811865476
      },
      {
        "dt": 0.025,
        "expected_final_mean": 0.03,
        "expected_final_std_current_dt_scaling": 0.0035355339059327377,
        "expected_final_std_sde_sqrt_dt_scaling": 0.007071067811865476
      }
    ],
    "vacuum_std_reduction_factor_bootstrap_95": [
      {
        "lower_95": 1.0237213486317018,
        "upper_95": 1.0353375308393835
      },
      {
        "lower_95": 1.0144254432593718,
        "upper_95": 1.0234777396838273
      },
      {
        "lower_95": 1.007380788718166,
        "upper_95": 1.0128752595785082
      }
    ]
  }
}
```

## Appendix E — Standalone Phi Time-Step Refinement Program

The following independent program reproduces the isolated analytic control and the coupled RD-0 refinement tables. It requires only NumPy and no Lineum repository or data file. It was executed with Python 3.11.15 and NumPy 1.26.4. Two consecutive runs produced bitwise-identical LF-normalized output. The embedded program SHA-256 is `12c10b6f9d6e72f43b283c324d683701dcdfa05bf19207499de6c11c9a1975d1`.

```python
"""Standalone time-step refinement study for the Lineum phi diffusion term."""

import json

import numpy as np


SIZE = 32
PHYSICAL_TIME = 10.0
TIME_STEPS = (0.2, 0.1, 0.05, 0.025)
D_PSI = 0.05
D_PHI_CONFIG = 0.05
PHI_LAPLACE_RATE = 0.05
REACTION = 0.0007
DRIFT = -0.004


def weighted_laplace(field, kappa, rate):
    k_up = np.roll(kappa, 1, axis=0)
    k_down = np.roll(kappa, -1, axis=0)
    k_left = np.roll(kappa, 1, axis=1)
    k_right = np.roll(kappa, -1, axis=1)
    f_up = np.roll(field, 1, axis=0)
    f_down = np.roll(field, -1, axis=0)
    f_left = np.roll(field, 1, axis=1)
    f_right = np.roll(field, -1, axis=1)
    neighbors = (
        f_up * k_up
        + f_down * k_down
        + f_left * k_left
        + f_right * k_right
    )
    active = k_up + k_down + k_left + k_right
    return rate * (neighbors - active * field)


def make_phi_mode(size=SIZE):
    y, x = np.mgrid[:size, :size]
    mode = np.cos(2 * np.pi * x / size) * np.cos(2 * np.pi * y / size)
    phi = 0.5 + 0.1 * mode
    kappa = np.ones((size, size), dtype=np.float64)
    return phi.astype(np.float64), kappa, mode


def mode_amplitude(phi, mode):
    centered = phi - np.mean(phi)
    return float(np.sum(centered * mode) / np.sum(mode**2))


def evolve_phi_mode(dt, diffusion_scales_with_dt):
    phi, kappa, mode = make_phi_mode()
    initial_amplitude = mode_amplitude(phi, mode)
    multiplier = dt if diffusion_scales_with_dt else 1.0
    steps = round(PHYSICAL_TIME / dt)
    for _ in range(steps):
        phi += (
            kappa
            * D_PHI_CONFIG
            * weighted_laplace(phi, kappa, PHI_LAPLACE_RATE)
            * multiplier
        )
    return mode_amplitude(phi, mode) / initial_amplitude


def analytic_mode_ratio(dt, diffusion_scales_with_dt):
    wave_number = 2 * np.pi / SIZE
    lap4_eigenvalue = 4 * np.cos(wave_number) - 4
    alpha = D_PHI_CONFIG * PHI_LAPLACE_RATE
    multiplier = dt if diffusion_scales_with_dt else 1.0
    per_step_factor = 1 + alpha * lap4_eigenvalue * multiplier
    return float(per_step_factor ** round(PHYSICAL_TIME / dt))


def make_coupled_state(size=SIZE):
    y, x = np.mgrid[:size, :size]
    center = (size - 1) / 2
    radius_squared = (x - center) ** 2 + (y - center) ** 2
    envelope = np.exp(-radius_squared / (2 * 3.5**2))
    phase = 0.17 * x - 0.11 * y
    psi = (envelope * np.exp(1j * phase)).astype(np.complex128)
    phi = (
        0.25
        + 0.08
        * np.cos(2 * np.pi * x / size)
        * np.cos(2 * np.pi * y / size)
    ).astype(np.float64)
    return psi, phi, np.ones((size, size), dtype=np.float64)


def coupled_step(psi, phi, kappa, dt, diffusion_scales_with_dt):
    phi_clipped = np.clip(phi, 0.0, 10.0)
    interaction_factor = 0.1 * np.tanh(0.4 * phi_clipped * kappa)
    interaction = interaction_factor * psi
    interaction = interaction / (1.0 + np.abs(interaction) / 10.0)
    grad_phi_x, grad_phi_y = np.gradient(phi)
    flow = DRIFT * (grad_phi_x + 1j * grad_phi_y) * kappa
    flow = flow / (1.0 + np.abs(flow) / 10.0)

    psi += flow * dt
    psi += interaction * dt
    psi -= 0.005 * psi * dt
    psi += weighted_laplace(psi, kappa, D_PSI) * kappa * dt

    scale_ratio = (128.0 / SIZE) ** 2
    phi += kappa * REACTION * scale_ratio * (np.abs(psi) ** 2 - phi) * dt
    phi_diffusion_multiplier = dt if diffusion_scales_with_dt else 1.0
    phi += (
        kappa
        * D_PHI_CONFIG
        * weighted_laplace(phi, kappa, PHI_LAPLACE_RATE)
        * phi_diffusion_multiplier
    )
    return psi, phi


def evolve_coupled(dt, diffusion_scales_with_dt):
    psi, phi, kappa = make_coupled_state()
    for _ in range(round(PHYSICAL_TIME / dt)):
        psi, phi = coupled_step(
            psi, phi, kappa, dt, diffusion_scales_with_dt
        )
    return psi, phi


def relative_to_reference(estimate, reference):
    return float(
        np.linalg.norm(estimate - reference)
        / (np.linalg.norm(reference) + 1e-30)
    )


isolated = {"current_missing_dt": [], "hypothetical_with_dt": []}
for dt in TIME_STEPS:
    for label, scaled in (
        ("current_missing_dt", False),
        ("hypothetical_with_dt", True),
    ):
        numerical = evolve_phi_mode(dt, scaled)
        analytic = analytic_mode_ratio(dt, scaled)
        isolated[label].append(
            {
                "dt": dt,
                "steps": round(PHYSICAL_TIME / dt),
                "numerical_amplitude_ratio": numerical,
                "analytic_amplitude_ratio": analytic,
                "absolute_numerical_error": abs(numerical - analytic),
            }
        )


coupled_states = {"current_missing_dt": {}, "hypothetical_with_dt": {}}
for label, scaled in (
    ("current_missing_dt", False),
    ("hypothetical_with_dt", True),
):
    for dt in TIME_STEPS:
        coupled_states[label][dt] = evolve_coupled(dt, scaled)


coupled_pairwise = {"current_missing_dt": [], "hypothetical_with_dt": []}
for label in coupled_pairwise:
    for coarse, fine in zip(TIME_STEPS, TIME_STEPS[1:]):
        coarse_psi, coarse_phi = coupled_states[label][coarse]
        fine_psi, fine_phi = coupled_states[label][fine]
        coupled_pairwise[label].append(
            {
                "coarse_dt": coarse,
                "fine_dt": fine,
                "psi_relative_l2": relative_to_reference(
                    coarse_psi, fine_psi
                ),
                "phi_relative_l2": relative_to_reference(
                    coarse_phi, fine_phi
                ),
            }
        )


lap4_eigenvalue = 4 * np.cos(2 * np.pi / SIZE) - 4
alpha = D_PHI_CONFIG * PHI_LAPLACE_RATE
output = {
    "configuration": {
        "grid_size": SIZE,
        "physical_time": PHYSICAL_TIME,
        "time_steps": list(TIME_STEPS),
        "phi_diffusion_config": D_PHI_CONFIG,
        "inner_laplace_rate": PHI_LAPLACE_RATE,
        "effective_alpha": alpha,
        "lap4_mode_eigenvalue": float(lap4_eigenvalue),
    },
    "isolated_phi_mode": isolated,
    "isolated_summary": {
        "current_ratio_spread": max(
            row["numerical_amplitude_ratio"]
            for row in isolated["current_missing_dt"]
        )
        - min(
            row["numerical_amplitude_ratio"]
            for row in isolated["current_missing_dt"]
        ),
        "hypothetical_ratio_spread": max(
            row["numerical_amplitude_ratio"]
            for row in isolated["hypothetical_with_dt"]
        )
        - min(
            row["numerical_amplitude_ratio"]
            for row in isolated["hypothetical_with_dt"]
        ),
        "hypothetical_continuous_limit": float(
            np.exp(alpha * lap4_eigenvalue * PHYSICAL_TIME)
        ),
    },
    "coupled_rd0_pairwise_refinement": coupled_pairwise,
}

print(json.dumps(output, indent=2, sort_keys=True))
```

## Appendix F — Full Phi Time-Step Refinement Output

The output SHA-256 after normalizing line endings to LF and including the final newline is `e90f66e55d27345a4221b5cedc5c945b8912365355431e7a94b231ed602993d5`.

```json
{
  "configuration": {
    "effective_alpha": 0.0025000000000000005,
    "grid_size": 32,
    "inner_laplace_rate": 0.05,
    "lap4_mode_eigenvalue": -0.07685887838707828,
    "phi_diffusion_config": 0.05,
    "physical_time": 10.0,
    "time_steps": [
      0.2,
      0.1,
      0.05,
      0.025
    ]
  },
  "coupled_rd0_pairwise_refinement": {
    "current_missing_dt": [
      {
        "coarse_dt": 0.2,
        "fine_dt": 0.1,
        "phi_relative_l2": 0.001788257370643413,
        "psi_relative_l2": 4.983371913436278e-05
      },
      {
        "coarse_dt": 0.1,
        "fine_dt": 0.05,
        "phi_relative_l2": 0.003492066024134346,
        "psi_relative_l2": 0.0002991370408839292
      },
      {
        "coarse_dt": 0.05,
        "fine_dt": 0.025,
        "phi_relative_l2": 0.006706569703660991,
        "psi_relative_l2": 0.0007104033537449127
      }
    ],
    "hypothetical_with_dt": [
      {
        "coarse_dt": 0.2,
        "fine_dt": 0.1,
        "phi_relative_l2": 5.472604949309865e-05,
        "psi_relative_l2": 0.00020154848536682308
      },
      {
        "coarse_dt": 0.1,
        "fine_dt": 0.05,
        "phi_relative_l2": 2.7335443098649967e-05,
        "psi_relative_l2": 0.00010083083048908117
      },
      {
        "coarse_dt": 0.05,
        "fine_dt": 0.025,
        "phi_relative_l2": 1.3660892239002042e-05,
        "psi_relative_l2": 5.0429604214551325e-05
      }
    ]
  },
  "isolated_phi_mode": {
    "current_missing_dt": [
      {
        "absolute_numerical_error": 1.3322676295501878e-15,
        "analytic_amplitude_ratio": 0.990437729136601,
        "dt": 0.2,
        "numerical_amplitude_ratio": 0.9904377291366023,
        "steps": 50
      },
      {
        "absolute_numerical_error": 2.55351295663786e-15,
        "analytic_amplitude_ratio": 0.9809668952972669,
        "dt": 0.1,
        "numerical_amplitude_ratio": 0.9809668952972694,
        "steps": 100
      },
      {
        "absolute_numerical_error": 4.6629367034256575e-15,
        "analytic_amplitude_ratio": 0.962296049669159,
        "dt": 0.05,
        "numerical_amplitude_ratio": 0.9622960496691637,
        "steps": 200
      },
      {
        "absolute_numerical_error": 8.881784197001252e-15,
        "analytic_amplitude_ratio": 0.9260136872088687,
        "dt": 0.025,
        "numerical_amplitude_ratio": 0.9260136872088776,
        "steps": 400
      }
    ],
    "hypothetical_with_dt": [
      {
        "absolute_numerical_error": 8.881784197001252e-16,
        "analytic_amplitude_ratio": 0.9980803360351598,
        "dt": 0.2,
        "numerical_amplitude_ratio": 0.9980803360351589,
        "steps": 50
      },
      {
        "absolute_numerical_error": 1.3322676295501878e-15,
        "analytic_amplitude_ratio": 0.998080354460703,
        "dt": 0.1,
        "numerical_amplitude_ratio": 0.9980803544607016,
        "steps": 100
      },
      {
        "absolute_numerical_error": 3.3306690738754696e-16,
        "analytic_amplitude_ratio": 0.9980803636732977,
        "dt": 0.05,
        "numerical_amplitude_ratio": 0.9980803636732973,
        "steps": 200
      },
      {
        "absolute_numerical_error": 9.992007221626409e-16,
        "analytic_amplitude_ratio": 0.9980803682795507,
        "dt": 0.025,
        "numerical_amplitude_ratio": 0.9980803682795497,
        "steps": 400
      }
    ]
  },
  "isolated_summary": {
    "current_ratio_spread": 0.06442404192772477,
    "hypothetical_continuous_limit": 0.9980803728857736,
    "hypothetical_ratio_spread": 3.224439082405439e-08
  }
}
```
