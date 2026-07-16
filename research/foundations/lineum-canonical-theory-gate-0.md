# Lineum Gate 0: Canonical-Theory Decision Brief

**Document status:** active — RD-0-C1 time-scaled phi candidate implemented and validated as opt-in; default physics and whitepaper changes remain gated
**Research version:** 0.4
**Evidence cutoff date:** July 16, 2026
**Language:** English
**Current confidence:** high for the source audit, backend-divergence result, RD-0 software fingerprint, phi time-step inconsistency, and opt-in candidate implementation; medium for the recommended sequencing; no claim of physical validation
**Standalone portability:** all decision-relevant definitions, equations, observations, calculations, executable reproduction code, and outputs are embedded in this document
**Decision boundary:** this brief records one approved software-characterization step; it does not declare a new Lineum law

## 1. Technical Summary

**Gate 0 is not yet passed.** The current Lineum corpus uses at least five incompatible canonical labels—Version 4, Eq-4′, Eq-7, Eq-10, and Eq-11.1—plus a provisional biharmonic PDE. These labels do not denote one backend-independent update law. The same public runtime option named `wave_baseline` executes a diffusive step in the NumPy backend and a spectral wave step in the PyTorch backend.

**The immediate recommendation is to freeze meaning before freezing ambitious physics.** Lineum should presently be described as a research platform for effective, open, coupled-field dynamics. Claims about fundamental spacetime, quantum mechanics, particles, gravity, or an ontic lattice should remain separate hypotheses.

**The smallest safe software step is a provisional deterministic reference lane, not promotion of Eq-11.1 or the biharmonic candidate.** A noise-free diffusive subset already agrees across NumPy and PyTorch to approximately machine precision in the tested configuration. It can serve as a ruler for later changes while the physical theory remains open. This proposed lane is named **Reference Dynamics 0 (`RD-0`)** to avoid assigning another historical `Eq-N` label prematurely.

**A fixed-physical-time refinement experiment identifies one concrete numerical inconsistency.** The legacy \(\phi\)-diffusion is applied once per update without multiplication by the time step \(h\). Halving \(h\) therefore applies nearly twice as much \(\phi\)-diffusion over the same declared time. The project owner authorized an opt-in candidate containing the missing factor; it is now implemented in both CPU backends and converges at the expected first-order rate while the default remains unchanged.

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

## 12. Limitations and Robustness

- The backend comparison isolates deterministic evolution. It does not assess stochastic equivalence across random-number generators.
- The comparison disables the absorbing boundary to isolate bulk dynamics. Boundary policy remains a separate Gate 0 choice.
- The test covers one smooth initial state and three horizons. A permanent contract should add impulses, edge-localized states, nonuniform \(\kappa\), and zero-state controls.
- The fingerprint is sensitive at \(10^{-12}\) resolution but is not a proof of bitwise portability across every future Python, NumPy, PyTorch, compiler, or CPU combination.
- The refinement experiment tests one Fourier mode and one coupled smooth fixture. Additional modes, nonuniform \(\kappa\), boundary-localized states, and stability limits should be tested before promotion.
- The hypothetical time-scaled branch tests numerical consistency only. It does not calibrate \(h\), \(D_\phi\), or any field to SI units.
- The source snapshot contained uncommitted work. Revision identifiers and working-tree counts are therefore recorded explicitly.
- The option assessment concerns readiness for canonicalization, not ultimate scientific merit.
- No chart is used because three exact time checkpoints and five discrete options are clearer as audit tables than as plots.

## 13. Decision Record and Next Gate

The approved decision is:

> **Approve the three-layer separation and authorize only an `RD-0` characterization contract. Do not promote any current equation as fundamental Lineum physics.**

This decision preserves the long-term ambition of Lineum while giving the project one reproducible software baseline. It is reversible: a later wave, Eq-11.1, biharmonic, quantum-automaton, or other candidate can replace the scientific model after it reproduces the baseline controls and passes stronger physical tests.

The approved read-only experiment and isolated non-default implementation are complete. The next proposed gate is broader falsification of `RD-0-C1` using nonuniform \(\kappa\), boundary-localized states, additional Fourier modes, and explicit stability limits. No default or canonical text should change before those controls pass and the owner reviews the results.

## 14. Further Questions

1. Should \(\kappa\) be a fixed part of the Lineum law, an environmental coefficient map, or an extension?
2. After broader falsification, should `RD-0-C1` replace legacy per-update \(\phi\)-diffusion as the default continuous-time interpretation?
3. Is locality a hard architectural requirement, or may a global spectral update remain a candidate if its nonlocal numerical kernel is declared?
4. Is the core research target an effective nonlinear medium, or must every retained candidate aim at fundamental spacetime?
5. Which single observable should be the first physical discriminator after software identity is achieved?

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

## Appendix C — Standalone Phi Time-Step Refinement Program

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

## Appendix D — Full Phi Time-Step Refinement Output

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
