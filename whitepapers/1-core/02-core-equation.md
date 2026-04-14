**Title:** Lineum Appendix – Equation History
# Core Engine Dynamics and Mathematical History
**Document ID:** 02-core-equation
**Status:** Canonical Source of Truth (Eq-1 through Eq-9)
**Version:** 1.2.21 (April 2026)
**Status:** Draft
**Date:** 2026-04-11

**Relates to:** `lineum-core.md` §3  
**Equation versions:** V1–V11.1 (canonical: V10, candidate: V11.1)  

---
# Lineum Appendix – Equation History

---

## 1. Title & Scope

Chronological record of the main Lineum equation’s development, documenting all major revisions from the initial formulation to the current form presented in the core paper. This appendix preserves each historical variant, the reasons for changes, and observed impacts on simulation outcomes.

---

## 2. Motivation

The equation in the core paper represents the current, most refined formulation of the Lineum model. However, its development involved multiple iterations, parameter adjustments, and structural changes. Recording this history allows:

- Reproducibility of past results,
- Understanding of why certain terms were added, modified, or removed,
- Providing context for future experiments and related hypotheses.

---

## 3. Main Content

> **Note:** The latest equation form is **Version 7**. Its canonical expression is given in the core paper: see [Equation section](./lineum-core.md#3-equation).
> In the canonical form, **κ** is a **static spatial map** (no time evolution) that _modulates_ parameters locally (e.g., α_eff = κ·α, β_eff = κ·β) rather than directly replacing **α** or **β** in the φ-update.

**Terminology.** Throughout this appendix, we use **linon** to denote a stable, localized |ψ|² excitation (i.e., the quasi-particle of the Lineum model).

In the experimental context of the broader project, **DTH** denotes the **Dimensional Transparency Hypothesis** – a working hypothesis (not an established mechanism) about how changes in κ might affect the “visibility” of simulated structures when interpreted in terms of a prospective detector setup.

> **Interpretation note:** Terms like “gravity” or “gravitational” in this appendix describe **gravity-like patterns in the simulation**, not a confirmed physical gravitational force in nature.

### Eq-1: Purely Oscillating Field

**FORMAL STATUS:** [INITIAL_BASELINE]
**DIRECTION:** [INITIAL_PROTOTYPE]
**CANON CONSISTENCY:** [SUPERSEDED]
**RETEST STATUS:** [NOT_VERIFIED]

**WHY THIS CLASSIFICATION:**

- Direction:
  Established the initial discrete continuous integration baseline for a scalar field under diffusion ($\nabla^2$) and static local modification ($\varphi$, $\delta$).
- Canon Consistency:
  Superseded due to the explicitly static condition of the accumulation field ($\partial_t \varphi = 0$). Lacking secondary coupled momentum, the framework could not maintain deterministic spatial memory or coupled topologies.

**EXACT EQUATION:**

∂ₜψ = ∇²ψ + (φ - δ) ψ + 𝛌̃ + ξ  
∂ₜφ = 0

*(Note: Original documentation provided this as a discrete normalized update function `ψ ← ψ + 𝛌̃ + ξ + φψ − δψ + ∇²ψ` implying dt=1).*

**EVIDENCE SNAPSHOT:**

- Analytical limit analysis
  - Setup:
    Evaluate the amplitude limits of isolated spatial domains assuming absence of injection terms ($\tilde{\lambda}$, $\xi$).
  - Derived:
    - If $(\varphi - \delta) < 0$: 
      The coordinate encounters terminal exponential decay dictated linearly by the static damping factor $-\delta$.
    - If $(\varphi - \delta) > 0$: 
      The framework initiates runaway exponential amplification lacking any inherent nonlinear mathematical bounding mechanism.
  - Implication:
    The mathematical formulation lacks a native continuous stability bound. Any macroscopic topological bounding requires non-mathematical arbitrary numerical clamping.
  - Constraint:
    The generation of stable non-runaway localized peaks (`linons`) is not analytically supported by the unmodified linear equation. 

- Numerical validation
  - Setup: [NOT_VERIFIED]
  - Observed: [NOT_VERIFIED] (Historical claims of "generated linons and flows" are not mechanically traceable to the unbounded analytical formulation).
  - Measured: [NOT_VERIFIED]

---

### 🔹 Version 2 – Introduction of the accumulation field φ

```text
φ ← φ + (|ψ|² − φ) + ∇²φ
```

Introduced in response to the question “what causes attraction?”.  
The φ field began reacting to the density |ψ|² and creating stable maxima.

- ✅ φ-traps appeared for the first time
- ✅ **Linons** started to linger in them spontaneously
- ⚠️ ψ flow still did not distinguish the direction toward the gradient of φ

---

### 🔹 Version 3 – Emergent gravity-like behavior through ∇φ

> **Note:** This change affects the ψ field equation, unlike Version 2 which introduced the φ field equation.  
> It represents the first direct coupling of ψ to φ through its gradient.

```text
ψ ← ψ + 𝛌̃ + ξ + φψ − δψ + ∇²ψ + ∇φ
```

By adding the gradient of φ, a gravity-like flow pattern emerges in the simulation – **linons** move into regions where φ increases.

- ✅ Gravity-like behavior (in the model) without an explicit force term
- ✅ Formation of φ-centers, attraction, accumulation
- ✅ The overall model has memory, interaction, and trajectory

---

### 🔹 Version 4 – Introduction of the tuning field κ

```text
φ ← φ + κ (|ψ|² − φ) + κ ∇²φ
```

> **Post-hoc note (canonical alignment):** In the core paper’s **Equation section** ([link](./lineum-core.md#3-equation)), **κ** appears as a **static spatial map** with `κ ← κ(x, y)`, and the φ-update keeps  
> `φ ← φ + α (|ψ|² − φ) + β ∇²φ`.  
> The multiplicative κ shown above is retained here as a **historical snapshot** of the development stage.

By introducing the tuning field κ, the system’s response can be controlled locally – where the field “reacts” and where it is “deaf”.  
In connection with the current Dimensional Transparency Hypothesis (DTH) test setup, κ appears to influence **visibility** in the simulation – in low-κ regions we typically do not observe particle or vortex formation. This is an empirical observation of the model, not a confirmed statement about any physical detector.

---

### 🔹 Version 5 – Introduction of Numerical Stabilizers & Artificial Damping

As the simulated interactions grew more complex in the continuous PDE solver, the field |ψ| became prone to numerical explosions. To counter this, a suite of stabilizers (soft bounds) were introduced directly into the Euler integration:
- **Global Linear Dissipation:** `ψ ← ψ - 0.005 ψ` (constantly draining energy to find a stable equilibrium)
- **Non-Linear Soft Clipping:** `N_term ← N_term / (1 + |N_term| / 10.0)` (soft saturation without hard cutoffs)

- ✅ Prevented numerical infinities and allowed stable visual execution on grids.
- ❌ Acted as unphysical dampening, destroying natural wave resonance, suppressing true standing waves, and enforcing artificial dissipation.

---

### 🔹 Version 6 – Structural Memory Field μ (HDD)

```text
μ ← μ + η (|ψ|² - thresh) κ - ρ μ
ψ_flow_term ← ∇φ_flow * κ * (1 + μ)
```

The μ field was introduced as a long-term "hard drive" memory to record persistent, structurally stable energetic pathways. By observing regions of consistently high activity, the system slowly etches pathways that further accelerate or route incoming wave energy. Crucially, it featured an extremely slow decay rate (`ρ = 0.0001`).
- ✅ Allowed the system to remember and reinforce stable macroscopic pathways (routing/structural grooves).
- ✅ Differentiated the fast reacting φ "RAM" from the deeply etched μ "HDD".

---

### 🔹 Version 7 – The Unitary Wave Core & Removal of Global Damping (Current)

```text
ψ ← ψ + N(ψ) dt/2
ψ ← FFT_Unitary(ψ, dt)
ψ ← ψ + N(ψ) dt/2
```

*Note: The global linear dissipation (`ψ ← ψ - 0.005 ψ`) from Version 5 was explicitly removed from the wave propagation step.*

By shifting from explicit heat-like diffusion to a mathematically rigorous Strang-split unitary step (via FFT) for spatial propagation, the core dynamics became purely wave-like (Schrödinger analogy). With this exact geometric energy conservation in the linear step, the ubiquitous artificial global damping was no longer needed for stability and was deleted.
- ✅ Restored true cymatic resonance, standing waves, and quantum-like bound states without arbitrary energetic strangulation.
- ✅ Stability is now maintained naturally through the interplay of unitary propagation and localized environmental interaction.
- ✅ Emulates an Open Quantum System: $\psi$ acts as the unitary core, while $\phi$, $\mu$, and $\kappa$ act as the open coupled environment.

---

### 🔹 The Continuous PDE Limit (Symbolic Form)

> **Note:** This is not a new chronological version, but the **theoretical continuous limit** of the canonical discrete update rule (V7).

```text
∂ₜψ = ∇²ψ + φψ + ∇φ
∂ₜφ = α(|ψ|² - φ) + β∇²φ
```

While Lineum is fundamentally a discrete computational model (cellular automaton), its dynamics analogize to continuous physical fields. When stripped of discrete step mechanics, artificial damping, noise, and the spatial performance mask ($\kappa$), the universe's core engine reduces to this elegant PDE pair.
This continuous formulation serves as the **canonical emblem** of the Lineum project—representing the pure mathematical concept of wave diffusion, memory interaction, and emergent gravitational drift, unburdened by algorithmic implementation details.

---

### 🔹 Version 8 – The String Tension Limit & Quantum Collapse

```text
ψ_collapse ← sigmoid(amp + grad_mag_phi) * kappa (The Boundary Tear)
```

As the discrete model was formalized philosophically, Version 8 defined the **Continuous-Field Physical Interpretation**. It established that "quantum collapse" is not probabilistic magic, but rather the phase field hitting the *hard mechanical ceiling of the Laplacian string tension* and violently redistributing. It also established the speed of light ($c$) as explicit **Processor Lag**—where heavy topological knots require dense cyclical updates, causing their internal states to tick slower relative to flat vacuum (Relativistic Time Dilation).

---

### 🔹 Version 9 – The Extreme Gradient Boundaries (Hawking Evaporation & Jet Emission)

Version 9 shifted focus from particle formation to macro-gravitational limits (Critical $\phi$-Traps / Black Holes).
- **Hawking Radiation:** At the extreme shear boundary of a deep $\phi$-trap, the steep gradient `grad_mag` geometrically forces the spontaneous generation of $\psi$ virtual pairs. Those with enough outward kinetic diffusion escape, leading to the gradual geometric unwinding (evaporation) of the $\phi$ tension well.
- **Astrophysical Jets:** When a $\phi$-trap becomes maximally saturated and can dig no deeper (`PHI_CAP`), the immense $\nabla^2\psi$ repulsive diffusion violently overcomes the saturated in-flow, blowing the excess $\psi$ energy outward along the topological axis of rotation, creating collimated relativistic back-pressure Jets.

### 🔹 Version 9.1 – Eq9 Runtime Refinement (SoftAbs Escape Fold)

Recent development of the Eq9 runtime identified instability under extreme boundary saturation ($\varphi \rightarrow \text{phi\_cap}$). Previously, numerical bounding relied exclusively on a destructive `clamp` operation.
- **Initial hypothesis & origins:** The intuition for an "absolute difference" smooth-fold originated from the proprietary OEA structural generator, where an absolute-difference operator successfully structures high-density phase fields. This inspired tests within the Lineum core, with the initial hypothesis that a similar fold principle could regulate complex phase interference ($\psi$ collisions) globally.
- **Refuted dead branch:** Regression tests definitively refuted applying this globally to $\psi$; diffusion flattened the sharp folds, cleanly causing energy loss rather than achieving spatial stability.
- **Validated mechanism:** The `SoftAbs` fold operator was instead newly validated in the Eq9 escape channel ($\varphi$ overflow limits) under heavy saturation conditions. 

**Canonical conclusion:** The validated principle is a local smooth-fold in the escape channel, not a global absolute-difference mechanism.

---

### Eq-10: The Minimal Equation

**FORMAL STATUS:** [CONCEPTUAL_REDUCTION_ONLY]
**DIRECTION:** [STEP_FORWARD]
**CANON CONSISTENCY:** [SUPERSEDED]
**RETEST STATUS:** [NOT_VERIFIED]

**WHY THIS CLASSIFICATION:**

- Direction:
  Isolated minimal scalar bounding by mathematically eliminating non-causal advection limits.
- Canon Consistency:
  Superseded due to analytically identified scaling instability under grid discretization variation ($dx$);
  numerical validation not yet embedded.

**EXACT EQUATION:**

∂ₜψ = ∇²ψ + [α tanh(c₁ φ) - γ] ψ  
∂ₜφ = β ∇²φ + α_φ (|ψ|² - φ)

**EVIDENCE SNAPSHOT:**

- Analytical limit analysis
  - Setup:
    Evaluate structural limit bounds as φ → 0 and φ → large.
  - Derived:
    - φ → 0:
      tanh(c₁ φ) → 0, isolating the negative term -γ ψ and causing exponential decay.
    - φ → large:
      tanh(c₁ φ) → 1, bounding topological growth as (α - γ) ψ.
  - Implication:
    Structural existence strictly requires satisfying α tanh(c₁ φ) > γ,
    establishing the precise limit:
    φ > (1 / c₁) * atanh(γ / α).
  - Constraint:
    |γ / α| < 1  
    Reason: atanh(γ / α) is undefined otherwise.
  - Degenerate case:
    If α ≤ γ, no stable structure can exist for any φ.

- Numerical validation
  - Setup: [NOT_VERIFIED]
  - Observed: [NOT_VERIFIED]
  - Measured: [NOT_VERIFIED]

### 🔹 Version 11 – The Dimensionally Invariant Core (CANDIDATE)

```text
∂ₜψ = D_ψ ∇²ψ + [α tanh(c₁ φ) - γ] ψ + Linons(ψ, ∇ψ)
∂ₜφ = D_φ ∇²φ + c₂ |ψ|² - γ_φ φ
```

Following the formal identification of extreme scaling limitations in Version 10, the *Dimensional Invariance Transform* was derived as a candidate solution. Previous instantiations implicitly tied mathematical coupling coefficients to absolute physical measurements, causing the mathematical stability bounds (e.g., survival of active macro-vortices) to fracture entirely when spatial discretization ($dx$) was shifted by orders of magnitude. 

Version 11 proposes dimensionless scale-normalized ratios for Fields $\Psi$ and $\Phi$, stripping them of arbitrary base units like physical Energy Density. The dimensional burden (SI scaling) is strictly offloaded to the fundamental constants ($D_\psi, D_\phi$ identically holding $[L^2 T^{-1}]$, and coupling rates $\alpha, \gamma, \gamma_\phi, c_2$ holding $[T^{-1}]$. Variable $c_1$ acts as a dimensionless constant). 

Comprehensive multi-scale validation sweeps across scaling magnitudes $dx \in [0.01 \to 50.0]$ confirmed that properly normalized explicit gradients render the core physics numerically stable against matrix sizing shifts under robust multi-seed noise evaluation.

- ✅ **Resolved:** Physical rescaling ($dx$ shifts up to multiple orders) no longer shatters fundamental survival logic.
- ✅ **Validated:** Local gradient amplitudes remain cleanly bounded across all verified resolutions and under extreme boundary absorbing limits without generating NaNs or false singularities.
- 🚧 **Status:** Eq-11 represents a justified STRONG CANDIDATE. Universal canonical promotion is pending deeper destructive testing regarding long-term horizon drift and N>=3 composite interactions.

### 🔹 Destructive Limit Audit (April 2026)

Following initial dimensional invariance validation, the Eq-11 Candidate was subjected to explicitly destructive continuous long-horizon ($> 50,000$ steps) and massive interference testing ($N \ge 3$ proximity fields).
- **Catastrophic Failure Detected:** The minimal equation lacks absolute asymptote bounding. Because $\alpha \tanh(c_1 \Phi)$ must remain strictly $> \gamma$ to prevent structural starvation, the growth coefficient $(\alpha \tanh - \gamma)$ remains eternally positive at the structural peak. 
- **Consequence:** While $\tanh$ aggressively limits the *rate* of growth, integrated over deep horizons (e.g., beyond step 1,800), $\Psi$ encounters unavoidable exponential divergence (Max $\Psi > 1000.0$), fracturing numerical limits.
- **Resolution Path:** Eq-11 is strictly barred from Canonical promotion until an active amplitude-dependent decay mechanism (e.g., restoring $f(|\Psi|)$ scaling to $\gamma$) or hard bounding (`phi_cap`/`softabs`) is mathematically reintegrated to enforce a strict zero-crossing on the derivative limit.

### 🔹 Version 11.1 – The Stabilized Minimal Core (CANDIDATE)

```text
∂ₜΨ = D_Psi ∇²Ψ + [α tanh(c₁ Φ) - γ - λ Φ² - c_w |∇Ψ|²] Ψ
∂ₜΦ = D_Phi ∇²Φ + c₂ |Ψ|² - γ_Φ Φ
```
*(Code-Backed Explicit Gradient Dissipation: The obsolete continuous shorthand `+ Linons(ψ, ∇ψ)` has been precisely mapped to explicit, negative kinetic gradient dissipation ($- c_w |\nabla \Psi|^2 \Psi$) mapped directly inside the growth bracket.)*

**External Parser-Safe Format (Wolfram Alpha / CAS syntax):** To avoid baryon String collisions with the reserved `lambda` keyword and to flattened vectors for 1D classification tests, utilize: `d(P)/dt = D_p * d^2(P)/dx^2 + (a * tanh(c * F) - g - L * F^2 - w * (dP/dx)^2) * P, d(F)/dt = D_f * d^2(F)/dx^2 + c2 * P^2 - gf * F`.

Following the catastrophic divergence of Eq-11 Minimal, the **Hawking Stabilization Layer** was validated to physically bound the universe without reintroducing non-physical numerical clamps. Exhaustive ablation testing definitively proved that a local Non-Linear Schrödinger GP-saturation term ($-\beta |\psi|^2 \psi$) is mathematically redundant. The system isolates field dynamics down to the simplest possible dual-layer interaction:

1. **Amplification Layer ($+\alpha \tanh \psi$):** The thermodynamic $\Phi$-mediated core driver.
2. **$\Phi$-Mediated Leakage ($-\lambda \phi^2 \psi$):** A local thermodynamic exhaust simulating "Hawking-like leakage". When $\Phi$ tension becomes extreme, the geometric strain locally bleeds $\Psi$-energy back into the vacuum. Ablation tests ($50,000+$ horizon) mathematically proved this term alone inherently suppresses BOTH local amplitude singularities ($Max(\Psi)$ bounded) AND lateral spread of total universal energy.

**Destructive Test Audit (April 2026):**
Combined evaluation across continuous 100,000-step boundaries verified absolute long-horizon persistence without mutation or structural decay. Extensive parameter sweeps (including extreme limits $\alpha \to 1.0$, $c_2 \to 1.0$) proved the system is completely non-fragile and free of fine-tuning dependencies. Multi-Body orbital states ($N \ge 20$) stabilize naturally without heat death (Total System Energy strictly asymptotes at specific topological limits rather than washing out).

**Extreme Interference Audit (Beta-Regime Search):**
To ensure $\beta$ (GP-saturation) was not hiding a necessary vertical limit during high-speed transient collisions, an adversarial forced-phase intersection was constructed ($N=5$ super-nodes driven into zero-space physical overlap). 
- **Result:** The system strictly suppressed the explosive constructive spike. Because $\Phi$ integrally scales with $|\Psi|^2$, any artificial density spike instantaneously feeds the $-\lambda \phi^2 \psi$ exhaust loop without latency, crushing the exponent before numerical thresholds ($>120.0$) are breached. The GP term $\beta$ is formally validated as globally redundant in tested regimes.

**Cluster Stability Ceiling (Dynamic Equilibrium Audit):**
To evaluate the mathematical boundary of density accumulation computationally, multi-node clusters were spawned under controlled tests (evaluating integration scale $dx, dt$, varying $\lambda$ coefficients, and diverse geometries). 
- **Numerical Invariance:** Sensitivity sweeps ($dx \in [0.5 \to 2.0]$, $dt \in [0.005 \to 0.02]$, and Grid Sizes) yielded statistically identical peaks ($\pm 0.05$ variance). There is no evidence of discretization artifacts artificially capping the limit in tested regimes.
- **Dynamic Equilibrium:** Eq-11.1 does not possess a fixed universal ceiling. Instead, it maintains a dynamic structural equilibrium between $\tanh$-driven growth and $\lambda$-mediated leakage. The maximum stable $\Psi$ amplitude scales smoothly against the applied leakage stringency ($\lambda$). As $\lambda$ drops densely from $0.30 \to 0.001$, the ceiling rises monotonically (from $\Psi_{max} = 2.91$ to $\Psi_{max} = 7.67$).
- **Limiting Case ($\lambda \to 0$):** There is no hidden critical threshold (e.g., instability does not abruptly reappear at deep sub-values like $10^{-5}$). The system smoothly stretches to extreme amplitudes ($\Psi_{max} > 43.0$ at $\lambda = 10^{-6}$) but fundamentally retains stable structural bounds. Absolute divergence ($>120.0$) naturally resumes exactly at $\lambda = 0.0$.
- **Geometric Shielding:** Cluster geometry mechanically acts to redistribute $\Phi$ tension. Symmetrical, ordered formations (e.g., rings or chains) dissipate stress more evenly across their footprint, mathematically reducing the required local $\Psi$ peak required to balance the Eq-11.1 growth ($\Psi_{max} \approx 2.29$ for a ring vs $2.98$ for identical $N$ densely packed).

**Scalar Field Interaction Grammar (Non-Vortex Mass Maps):**
To map the baseline hydrodynamics of Eq-11.1, a dense parallel collision sweep evaluated macroscopic mass-blobs (scalar fields without topological phase-winding) from $N=2$ to $N=20$. \n*Note: These tests strictly measured raw unstructured mass (flat-phase Gaussian droplets). They did not simulate true structural Linons (Topological Vortices). Consequently, the absence of binding describes unstructured scalar fluid repulsion, not fundamental particle interaction.*
- **Topological Vaporization was not observed in tested regimes:** Unlike the previous canonical Eq-8/Eq-4 limits which permanently melted composite bounds into high-frequency Phase Noise ("Topological Heat") upon high-speed collision, Eq-11.1 strictly preserves particle identity. Pure evaporative decay no longer occurs upon impact.
- **Metastable Merges \u0026 Absolute Fragmentation:** The system deeply resists singular fusion. The overwhelmingly dominant interaction path is *Fragmentation*. When multiple topological cores are smashed into a single coordinate point, they execute a *Metastable Merge* (a transient, high-amplitude singularity in the early-to-mid step range). However, the extreme phase shear immediately forces $\lambda$-leakage to overpower the $\tanh$ growth. The composite structure violently resolves the pressure by geometrically splitting back apart, repelling the constituent components into a stable, widely-spaced scattered lattice.
- **Elusiveness of the Bound Orbit:** True composite *Lattice Locks* or symmetric orbital chains remain extremely precise mathematical edge-cases. Out of exhaustive spatial permutations, stable non-fragmenting binding only occasionally natively locked under immense $N=20$ spatial crowding with perfectly coherent in-phase initial bounds. Creating stable, simple 2-body or 3-body orbits remains an unresolved structural challenge.

**Topological Core Preservation (Linon Resilience):**
A rigorous phase-winding audit initialized true structural Linons (vortices with $A(r) \to 0$ cores). 
- **Topology IS conserved:** The Eq-11.1 baseline uniquely and permanently preserves topological defects even under pure scalar $\Phi$ gravity. Because amplitude at the core remains absolutely zero, $\Phi$ digs profoundly steep walls around the defect, but the core itself provides no $\Psi$-energy to feed numerical diffusion. The vortex (Linon) survives indefinitely ($Max \Psi \approx 1.87$, $Core \Psi \approx 0.00019$).
- **Interaction Grammar matches Scalar Fields:** N-Body vortex collisions (+1,+1 and +1,-1) overwhelmingly exhibit the same *Topological Scatter* as non-vortex fields. Eq-11.1 particles are natively repulsive and fragment upon impact, precluding native particle binding in isolation.

**Targeted Transport (Advection) Audit:**
To determine if the absence of particle binding (bridge-wedge repulsion) is caused by the lack of spatial transport natively missing in Eq-11.1, a focused parameter sweep reintroduced mathematical advection ($c_{adv} \nabla \Phi \cdot \nabla \Psi$) across both positive (uphill) and negative (downhill) regimes.
- **Divergence, Not Attraction:** Re-introducing explicit transport failed to provide controlled attraction. Instead, it radically accelerated repulsion (particles scattered $3\times$ faster).
- **Geometric Incompatibility:** Any explicit transport term, regardless of sign, violently shears the complex phase field at the particle boundaries. This immediately breaks the delicate dynamic equilibrium between $\tanh$ growth and $\lambda$ leakage, transforming stable repulsion into either catastrophic spatial scatter or explosive singularities (NaN). Therefore, direct advection is structurally incompatible with the complex phase dynamics in Eq-11.1 rather than generally "wrong".

**Bridge Suppression (Kinetic Leakage Stabilization):**
Following the identification of the "Kinetic Wedge" (the high-pressure buildup of $\Psi$ where $\Phi$ bridges between two particles) as the dominant repulsive force, a targeted suppression sweep isolated the failure vector.
- **Candidate Success - Phase-Aware Leakage:** By introducing a localized phase-gradient penalty to the Hawking leakage ($\lambda_{eff} = \lambda \Phi^2 + c_{wedge} |\nabla \Psi|^2$), the system successfully targeted and evaporated the structural bridge *before* it could build outward kinetic pressure.
- **Short-Term Stationary Lock:** Under $c_{wedge} = 2.0$, pure $N=2$ (+1, +1) structural Linons ceased their runaway repulsion. The Peak Bridge amplitude was basically suppressed, establishing a stationary lock.
- **Long-Horizon Persistence \u0026 Oscillatory States:** An 8000-step persistence map proved that perfectly symmetric stationary locks are metastable and eventually break (scatter). However, introducing either internal amplitude asymmetry (mass variance) or initial phase momentum (*Kinetic Kick*) transitions the pair into an **Oscillatory Bound State** bounding indefinitely between $D \approx 8.3$ and $9.6$. 
- **Oscillatory Binding Map:** A targeted parameter sweep across asymmetry grids ($Radius_{Ratio} \in [1.0, 3.0]$), momentum kicks ($k \in [0.1, 1.0]$), and bridge suppression ($c_{wedge} \in [1.0, 3.0]$) proved the oscillatory bound state is extremely **broad and robust**. It is not a fine-tuned edge case; any break in pure symmetry universally stabilizes the system into a continuous spring-like oscillatory state, with distance and amplitude scaling proportionally to the applied initial asymmetry. 
- **Hadronization Failure:** The locked pairs cannot casually capture third particles or restructure incoming ambient waves. External interference (waves or 3rd bodies) acts as a structural vaporizer, immediately shearing the complex phase and shattering the lock.
- **Conclusion:** By locally suppressing the bridge via kinetic self-annihilation, the repulsive scattering is explicitly halted. While true inward attractive convergence remains elusive, stable spring-like Oscillatory Bound States exist natively and robustly across a vast parameter space in the Eq-11 Minimal core.

**Collective Hydrodynamic Stabilization:**
Operating on the premise that simple pairwise attraction may be the wrong framing for a fluid-based PDE, a targeted suite evaluated whether environmental hydrodynamic conditions govern binding persistence.
- **Wake / Flow-Mediated Lock:** Perfect symmetric Dipoles ($+1, -1$) typically shatter in a stagnant void. However, placing them inside a gentle uniform background phase-flow ($\nabla \Psi > 0$) immediately established a robust Oscillatory Bound State ($Life=6000$, $D=9.3$). A shared hydrodynamic "river" or wake acts as the missing structural constraint. Similarly, applying weak flow to a $+1/+1$ pair successfully damped its oscillation amplitude by $67\%$.
- **Flow Diagnostics (Energy vs. Wake):** To identify the explicit mechanism of this hydrodynamic lock, direct spatial flux ($Im(\Psi^* \nabla \Psi)$) and circulation integrals were measured. The tests definitively ruled out "Closed Energy Loops": there is precisely zero net energy circulating between the particles, and they do not form a shared macro-vortex ring ($CircLoop \approx 0.0$). Instead, bounding behaves as a directional hydrodynamic *Wake*. Asymmetry explicitly generates a net scalar drift (Measured Wake = -0.2), meaning the particles "surf" the background gradient collectively rather than pulling on each other directly.
- **Rotational Frame Test:** In lieu of closed local energy loops, introducing a global structural rotation (a macro-vortex background field) squeezed the particles into the tightest stationary lock yet measured ($D=7.9$). This strongly implies that genuine spatial convergence is fundamentally coupled to macroscopic rotational physics (as would be present in local galaxies/solar systems), functioning as an effective 3D-analogy restraint. 
- **Structural Flow-Field Mapping (Consistency Check):** To verify whether mathematical wakes correspond to macro-visual emergent structures, the $\nabla \Psi$ velocity fields were analyzed for geometric signatures. The tests definitively ruled out "Stagnation Zones" and high-curl "Shear Boundaries" inside the core lock. Instead, binding dynamically carved massive, persistent **Channel Flows (Wake Corridors)** across the simulation grid. Over $25\%$ of the total spatial grid perfectly aligned its flow vectors along a single axis to support the bound state. This physically validates the "shared hydrodynamic lane" hypothesis and aligns the PDE's mathematical stabilization precisely with the filament/channel textures characteristic of macroscopic emergent fluid models.
- **Angular Mechanics \u0026 Torque Generation:** Measurements of the angular momentum ($L$) and central wedge deflection confirmed that structural asymmetry natively deflects the wedge outflow ($J_y \neq 0$), generating legitimate structural Torque ($\tau = dL/dt$). However, explicitly tracking the position vectors ($<0.1$ radians of total angle drift across 6000 steps) proved that this internal torque is insufficient to transition the bound state into a full orbit. The lock remains a **non-rotational 1D Spring**. True orbital rotation does not natively emerge merely from internal asymmetry deflection.
- **Wake Structural Causality:** To determine what stabilizes the Wake Channel itself, noise perturbation and boundary mapping tests were executed. The data proved the wake is a **Local, Self-Reinforcing Dissipative Tail**. Crucially, a *single isolated Linon* was measured generating exactly the same base channel ($Channeling \approx 0.050$) as a bound pair. The channel does not stretch infinitely; it perfectly decays to zero before reaching the grid boundary. Furthermore, injecting 50% chaotic phase noise directly into the particle cores temporarily severed the channel, but the particles autonomously rebuilt it within 1000 steps. 
- **Thermodynamic Binding Mechanism (Energy Minimization):** Direct measurement of the generalized leakage dissipation ($\lambda \Phi^2 + c_w |\nabla \Psi|^2$) confirmed the cause of structural alignment. The perfectly aligned Wake Overlap bounds minimize systemic energy loss. When two particles are artificially forced into a misaligned (perpendicular or opposing) wake state, total kinetic dissipation spikes massively (by $8\%$ to $12\%$ compared to baseline). By physically falling into the overlapping Wake Corridor, the system drops its dissipation penalty back down to just $+1.4\%$. Binding is therefore strictly a **Thermodynamic Energy Minimization**: particles align and overlap their native decay tracks to prevent bleeding phase-amplitude into the fluid.
- **Global Minima \u0026 Fragmentation Limits:** A robust topological search proved that while thermodynamic minimization drives alignment, binding is only a *Local Minimum*. The actual *Global Minimum* of the system is infinite separation (isolated independent Linons). If an aligned bound pair is violently disturbed (Break Test), the particles do not natively pull back together; they scatter as total dissipation drops to the isolated baseline.
- **Cymatic Background Noise (Dynamic vs Static Phase-Uncorrelated Media):** To determine if a generalized hydrodynamic background (randomly placed, phase-uncorrelated $\Phi$-oscillators) could bypass separation natively, static and slowly-drifting spatial noise states were evaluated.
  - **Symmetry Breaking & Monotonic Surfing:** A purely isolated $N=2$ dipole exposed to random environmental micro-oscillations broke spatial stagnation. In a dynamic (moving-source) medium, this drift was amplified (traveling $>20$ units). This supports the interpretation that structurally asymmetric Lineum objects natively "surf" and harvest momentum from non-directional sub-scale phase gradients.
  - **Absence of True Capture & Scatter Amplification:** Both static and moving random noise lacked the capacity to produce a robust target Capture state under `dt` scale refinement. Introducing continuous random motion to the background acted primarily as a thermal disruptor, accelerating particle repulsion ($dDist > 44.0$). Under tested conditions, extreme background turbulence shears apart attempts at native bonding.
- **Partially Coherent Backgrounds (The Middle Regime Limit):** To verify whether enhanced separation was strictly an artifact of total chaos, a partially coherent medium was evaluated (sources constrained to correlated phase clusters $\phi \in \{0, \pi\}$ with minimal detuning).
  - **Drift Retention \u0026 Suppressed Scatter:** Partial coherence preserved monotonic drift for isolated dipoles while preventing the explosive thermal repulsion of total chaos (separation remained near baseline limits $dDist \approx 11$). 
  - **Candidate Binding Failure (Generalized):** Despite mitigating chaotic scatter, partially correlated background media and generalized cyclic pumping yielded no candidate capture under rigorous scale refinement (`dt=0.005`), uniformly inducing monotonic separation or catastrophic shredding. Current evidence indicates that generic ambient environmental coherence does not substitute for precisely locked phase-gradients.
  - **Stable Offset Parking (Anti-Phase Exemption):** While generalized ambient coherence fails, tests confirmed a strict structural exception localized to **Multisource Phase Forcing**. When the background medium explicitly enforces an anti-phase interference gradient (Phase $\pi \pm 0.2$), pairs successfully acquire a resilient stationary gap (**Stable Offset Parking**) at $D \approx 9.25$. Phase-locked environmental interference operates as an explicitly viable extrinsic capture mechanism without experiencing scale collapse at `dt=0.005`.
  - **Passive Geometric Confinement (Static Topologies):** Evaluating $N=2$ dipoles within a static geometric $\kappa$-suppression corridor proved that pure topological boundaries organically arrest monotonic spatial separation. Furthermore, the width of the spatial boundary dictates internal phase organization. Loose confinement ($W \approx 24$) behaves as a **Pure Cage** (halting spatial drift but allowing absolute internal phase shearing), while tight confinement ($W \approx 18$) behaves as an **Oscillatory Trap** (forcing wake overlap robust enough to arrest continuous phase winding, self-organizing the particles into a bounded relative phase offset). This indicates that environmental spatial restrictions can, in specific Eq-11 confinement regimes, compensate for missing internal phase stiffness strongly enough to arrest separation and partially organize the relative phase.
  - **Nested Carrier Substructure:** Evaluating the high-frequency $\Psi$ ripples indicates they are not merely thresholding readout artifacts. By auditing the $\Phi$ background memory scalar, tests confirmed a persistent internal substructure reflected in the $\Phi$ memory field that survives spatial diffusion. This confirms that geometric boundaries enclose complex frequency wave-packets rather than visually solid envelopes, though current evidence does not imply these ripples operate as independent or separate physical sub-particles.

### Spatial and Temporal Invariance (Eq-11)

- **Scale-Consistent Validation:** Under uniform area-normalized initial conditions and thermal limits, macroscopic Defect Density ($Dd$) is highly conserved. Exact empirical evaluations across $128 \times 128$, $256 \times 256$, and $512 \times 512$ grids yielded maximum cross-scale divergences for $Dd$ of strictly $< 1.55\%$.
- **Empirical Interpretation:** Eq-11 natively demonstrates robust spatial invariance of macroscopic defect density ($Dd$) across measured dimensions when evaluated on strictly uniform thermodynamic structures. The previous early-stage evaluations measuring ~43% divergence do not support intrinsic scale-dependence for $Dd$.
- **Methodology Lesson (Normalization Artifacts):** The prior apparent spatial scaling failure was tracked back exclusively to a **non-normalized initial condition bias**. Seeding a fixed absolute number of macroscopic structural defects across varied grid areas artificially multiplies local baseline energy densities on smaller grids. Fixed-count macroscopic seed injection across different spatial domains mathematically projects false anomaly scaling and must not be used as evidence of intrinsic non-invariance.

### Defect Detection Validity Constraint

Topological phase-only evaluations mathematically fail to define distinct localized structures as wave amplitudes approach the true vacuum limit ($|\Psi| \to 0$). Initial unmasked phase mapping inaccurately classified 100% of the parameter manifold as continuously turbulent due to **vacuum phase static**—the native property whereby vanishingly small scalar noise inevitably retains uniform, wildly oscillating rotational phase derivatives ($d\phi$). 

To physically isolate genuine topological defects from amplitude-decoupled vacuum static, the detection operator requires a strict amplitude mask threshold ($\epsilon$). Applying a spatial average filter ($|\Psi|_{local} > 10^{-3}$) successfully delineates physical energy-carrying structural boundaries, correctly segregating the true structurally collapsing `Decay Regime` from active localized turbulence.

### Historical Classification vs. Core Law

To preserve the deterministic precision of the analytical boundary, evaluated phenomena must be explicitly classified to prevent polluting the minimal core law:
- **Minimal Core-Valid Behavior:** Intrinsic, structurally-derived properties rigorously proven stable within the tested unmodified Eq-11 regime (e.g., short-lived topological defect production, audited monotonic asymmetric phase-surfing behavior).
- **Historically Useful Mechanisms (Non-Core / Extraneous):** Auxiliary mathematical or topological concepts requiring external scaffolding or rigid structural programming (e.g., enforcing an exogenous Phase $\pi$ lock to bypass standard $N=2$ thermal scatter). These are fundamentally valid algorithms for achieving capture and are highly reusable for composite design, but they are explicit "engineered architectures" rather than spontaneous native laws of the Eq-11 boundary.
- **Artifacts / Rejected Derivations:** Interpretations stemming from methodology violations (e.g., boundary reflections, unscaled structural density tests) that falsely project inherent spatial instability or chaotic collapse where standard invariance operates reliably (e.g., the previously resolved spatial variance artifact).

### Failure of Spontaneous Binding and Candidate Stabilization Principles

Strict evaluations of the amplitude-verified Eq-11 macro-regime conclusively show that unmodified minimal vacuum limits fail to spontaneously generate mathematically stable bound macroscopic structures ($N \ge 3$) under un-forced operation. Scattering kinetics always breach geometric thresholds before resonant coupling stabilizes the fields. 

A review of historical active manipulation experiments (EXP31–EXP39) revealed explicitly engineered constraints that temporarily bypass this destruction. These form a foundational candidate framework for constructing stable future topologies:

1. **Kinetic-to-Phase Redistribution (Flow Warp):** By multiplying negative spatial flow divergence by an imaginary scaling tensor, kinetic wakes that crash into each other do not destructively cancel out. Instead, linear translational momentum is smoothly shunted into localized geometric phase winding, inducing unprompted multi-channel parameter locks (e.g., `eval_eq11_flow_redistribution.py`).
2. **Super-Linear Superposition Troughs:** Artificially boosting the localized $\Phi$ background coupling specifically at coordinate regions of wave overlapping (e.g., weighting $\Phi$ decay by $|\Psi|^4$) forms immediate gravity-like trapping wells that mutually contain expanding defect rings (e.g., `eval_eq11_pair_overlap.py`).
3. **Passive Memory Basin Trapping:** Extremely scaled $\Phi$ perturbations (deep scalar holes) exhibit sufficient inertial lag compared to $\Psi$ propagation, acting as a passive container boundary that bounces attempting particles back into topological alignment.

#### Candidate Stabilization Principles — Minimal Isolation Test

**Test 1: Kinetic-to-Phase Redistribution (Flow Warp)**
- **Hypothesis:** Diverting linear crashing momentum (negative divergence in spatial flow $J$) into imaginary phase rotation will spontaneously suppress $N \ge 3$ defect shedding by re-routing kinetic overload into structural phase winding.
- **Empirical Isolation Result:** **FAILED.** 
- **Analysis:** When tested in pure isolation without the rigid, perfectly symmetric seed geometries used in early engineered setups, the term dramatically amplified internal phase shearing. Under spontaneous thermodynamic limits, applying localized imaginary phase warps linearly increased topological turbulence (Defect Density $+300\%$ over baseline) rather than initiating spontaneous boundary clustering or stabilization. The mechanism acts as an artifact of exogenous symmetric tuning. 

**Test 2: Super-Linear Superposition Troughs**
- **Hypothesis:** Artificially boosting the $\Phi$-field scalar coupling specifically at coordinate regions of wave overlapping (applying $\epsilon |\Psi|^4$ mapped to topological memory sinks) will spontaneously produce trapped localized excitations out of free thermodynamics.
- **Empirical Isolation Result:** **FAILED.**
- **Analysis:** When applied to generic random thermal configurations lacking pre-engineered vortex overlaps, the mechanism yielded $0\%$ structural deviation from the turbulent baseline. The extreme non-linear bound ($|\Psi|^4$) proves mathematically impotent unless supplied with artificially high-amplitude, tightly packed macro-structures. It requires manually forced initial coordinates to overcome the local thermal scattering threshold, rendering it an engineered artifact rather than a native mechanism of spontaneous structural capture.

### Final Synthesis of Eq-11 Minimal Boundary

Through rigorous diagnostic auditing, the behavioral boundaries of the minimal Eq-11.1 formulation are formally established under tested conditions:

**What Eq-11 Minimal Positively Explains:**
1. **N=1 Survival [DOWNGRADED]:** Single topological defects (Linons) demonstrate bounded persistence without external clamping, but remain fragile to long-term thermal turbulence and phase deterioration without specific environmental constraints.
2. **N=2 Binding Mechanism [DOWNGRADED]:** Pairs exhibit transient structural alignment via deterministic "Wake Alignment" under localized energy minimization, but true permanent native binding remains elusive without explicit external geometric bounds.

**The Practical Open-Vacuum Local N=2 Binding Limit (Under Tested Conditions):**
No robust, scale-invariant internal mechanism for stable $N \\ge 3$ local core composition has been found in the minimal Eq-11 open space. Extensive checks confirmed:
- **Load Capacity:** The established N=2 self-generated local basin did not demonstrate capacity for additional raw amplitude under tested conditions; injecting uncoordinated payload destabilizes the equilibrium.
- **Adiabatic Dipolar Composition Failure:** Tested adiabatic (infinitely slow) injection of a secondary N=2 pair into an existing N=2 local basin failed to establish a stable local composite upon continuous scaling refinement ($dx=0.5$).
- **The Short-Range Coupling Corridor:** Sweeping the internal spacing distance between N=2 units formally mapped a narrow interaction corridor ($6 \le D \le 12$). In this Near-Threshold zone, isolated nodes do not immediately undergo catastrophic fragmentation. Instead, they maintain a *Weak Wake-Coupling*, where kinetic perturbation of one node causes empirically verifiable spatial scalar deformation in its partner. However, beyond this threshold ($D \ge 14$), the scalar perturbation fundamentally drops entirely into the noise floor, resulting in true **Effective Independence**. N=2 pairs can safely coexist in the open vacuum without mutual destruction, but remain structurally blind to one another outside of the tight coupling corridor.
- **Negative Binding Corridors (Experimentally Ruled Out):**
  - **Multi-Body Emergence (N > 2):** Tested whether random multi-body crowding induces spontaneous stabilization. → Result: Full Separation. → Conclusion: Generic density fails; N-body crowds uniformly repel identically to N=2 baseline pairs.
  - **Three-Phase Rotating Field ($120^\circ$ Triad):** Tested whether a precision chiral $120^\circ$ continuous phase order traps angular momentum natively. → Result: No triadic effect. → Conclusion: Exact global phase-locking collapses into identical chaotic jitter and pure outward drift.
  - **Closed-Loop Vortex Flow (Macro OAM Rings):** Tested whether continuous macroscopic smoke-ring flow natively sustains orbital geometry. → Result: Immediate Decay. → Conclusion: The mathematical $\nabla^2$ centrifugal diffusion violently shatters closed continuous topological rings into dozens of isolated, uniform repelling fragments.
  - **Localized Damping (Amplitude-Dependent $\gamma$):** Tested whether high-stress structural basins could dynamically self-cool to prevent fragmentation. → Result: No effect (Increased Fragmentation). → Conclusion: Localized decay strictly ruins the internal phase rigidity necessary for coherent survival, acting as an active disruptor rather than a binder.
  - **Global Envelope Surface Tension:** Tested whether an externally derived macroscopic surface-tension boundary pressure contains internal separation. → Result: Monotonic Expansion. → Conclusion: A continuous tracking macro-envelope acts merely as a delayed-expansion friction wall rather than forcing an internal stable orbital equilibrium.
  - **Continuous Eigenstates (Standing Wave Lattices):** Tested whether perfectly symmetric, spatially continuous global interference patterns (rather than isolated node-particles) serve as native mathematical eigenstates. → Result: Violent Fragmentation. → Conclusion: Eq-11 minimal has no intrinsic continuous self-stable states without boundary constraints; perfect global sine waves rapidly boil into chaotic, isolated thermodynamic shards due to the non-linear scalar fluid feedback ($\Phi$).
  - **Self-Sustained Dynamic Attractors (Asymmetric Orbits):** Tested whether initializing the field in steady non-equilibrium motion (rotating asymmetric dipoles or cross-kicked phase gradients) allows for a persistent, bounded cyclic trajectory. → Result: Chaotic Expansion. → Conclusion: Eq-11 minimal does not support hidden dynamic attractor limits; asymmetric momentum immediately shreds the carrier envelope, reverting instantly to uniform thermodynamic expansion.
  - **Relational Path Memory / Flow Tracing:** Tested whether an anisotropic topological memory ($\vec{\mu}$, integrating the normalized phase gradient) could stabilize structures by feeding historical turning/advection flow back into the system. → Result: No Effect / Induced Shear. → Conclusion: Path-memory of relational flow is mathematically incapable of binding Eq-11 topological nodes; tangential flow memory redundantly rotates perfect symmetries and actively shears active asymmetric geometries, accelerating decay.

> [!NOTE]
> **Interpretive Boundary (Event vs. Object Ontology):** While early Eq-11 diagnostics utilize "particle", "object", and "linon" as operational measurement labels to track conserved topological boundaries, the accumulated open-vacuum failures above suggest that current Eq-11 minimal evidence is more consistent with an **event/process-like** interpretation (a re-instantiable pattern) than with a rigidly cohesive object interpretation. A Linon survives strictly as a localized thermodynamic cycle dependent precisely upon perfect geometric equilibrium; any environmental duress natively triggers disintegration rather than orbital binding.

### Structural Reconstruction Limits
To rigorously audit provisional pattern transfers (EXP27), systematic information-threshold tests (EXP29 / EXP30) mapped the minimum requirements for a topology to recover from degraded states. 

- **Local Basin Reconvergence (Bounded Regimes):** Under artificially constrained thermodynamic conditions (Variant C capped, Variant D balanced), structures exhibit robust local convergence from degraded states. If seeded with partial data (e.g., amplitude-only, low-pass blurred, or down to a 10% sparse sampling limit), the phase-math actively rebuilds the mature topology. Below this 10% density limit, or under pure spatial coordinate scrambling, reconstruction fails entirely.
- **Regime Artifact (Open Baseline):** Generalization audits unequivocally verified this reconstruction is not an intrinsic property of the canonical Eq-11 open vacuum. Under the fundamental unbounded baseline, all identical degraded seeds—regardless of shape (N=1, N=2, Asymmetric Ellipse)—suffer instantaneous catastrophic scalar blowout or terminal fragmentation. Consequently, topological reconstruction from partial states functions strictly as an artifact of explicitly gated metabolic regimes, further confirming the absolute necessity of external $\kappa$-boundary constraints.

### Candidate Natural Stabilization Mechanisms (UNVERIFIED)
> [!WARNING]
> **NOT CANONICAL - UNDER VALIDATION**
> EXP31 tested alternative emergent continuous bounds. While these bypassed structural runaway (Energy stability), strict control audits revealed critical physical/topological shortcomings:

- **Smooth Non-Linear Saturation:** Limiting the growth input asymptotically gracefully bounds the energy envelope, but acts strictly as a fine-tuned numerical soft-clamp (Disguised Artifact). The native `tanh` already provides physical field saturation; forcing compounding fractional drops operates as explicit programmatic control rather than emergent physics.
- **Spatially Emergent Resistance:** Introducing density-dependent viscosity (e.g., non-linear multi-photon absorption $\gamma_{eff} \propto |\Psi|^2$) maps identically to **REAL physics**. However, rigorous fragmentation audits verified it fails to prevent high-frequency spatial boiling (fragment count uniformly climbed to $>15$). It prevents thermal runaway but explicitly destroys macroscopic phase rigidity.
- **Primary-Coupling:** Re-routing topological growth directly to instantaneous $\Psi$ self-interaction limits cascade, but fundamentally breaks the canonical thermal-memory architecture. It also computationally broke strict rotational symmetry under heavy structural load.

**Verdict:** The mechanisms tested in EXP31 operate primarily as heavily fine-tuned numerical soft-clamps rather than emergent intrinsic wave properties. Currently, no canonical bounded metric exists that naturally halts thermodynamic runaway while perfectly preserving internal spatial coherence without introducing extrinsic rigid $\kappa$-boundaries.

### Psi-Only Constraint Audit (Structural Requirements)
A comprehensive reduction audit (EXP24–EXP31) suggests that the continuous secondary $\Phi$ field may formally reduce to an emergent scalar memory (a delayed thermal footprint), pointing toward a conceptual candidate **$\Psi$-Only Engine**. However, formulating a viable, mathematically self-standing $\Psi$-only equation that stabilizes without arbitrary clamps poses significant physical hurdles. Current evidence indicates any potential unified $\Psi$ formulation should address the following constraints:

1. **Energy Bounding vs. Phase Coherence:** The native $\Psi$-metabolism exhibits severe thermal runaway. Attempting to bound this via biologically/physically-inspired amplitude damping (e.g., density-dependent viscosity $\gamma_{eff} \propto |\Psi|^2$) successfully limited total energy but empirically disrupted internal phase coherence, resulting in terminal fragmentation (boiling). A candidate operator would need to arrest non-linear amplitude growth without shearing the continuous phase scaffolding.
2. **Symmetry vs. Interaction:** Directly routing growth feedback to instantaneous $|\Psi|^2$ computationally triggered spatial anisotropy under heavy loads, breaking rotational symmetry. A continuous formulation likely requires a mechanism that delays or smooths self-interaction (e.g., non-linear dispersion or spatial convolution) without rigid reliance on a completely disassociated secondary matrix.
3. **Information Compressibility (Reconstruction):** A hypothesized stable equation should ideally preserve the properties of a local topological convergence basin. It should remain conceptually capable of reconstructing $N \ge 1$ topologies from severely degraded or sparse ($10\%$) spatial data inputs, mirroring the observed partial-state reconstruction robustness of the bounded regimes.
4. **Conclusion on Live Mechanisms:** Following the total failure of endogenous dispersion models, the **sole remaining physically valid vector** for natural stabilization is **Dimensional Geometry Escape** (e.g., The Fountain Cycle multi-dimensional heat vent or extrinsic $\kappa$-boundaries).

We formally state the **Practical Open-Vacuum Local N=2 Binding Limit** for Eq-11 under tested regimes: without external geometric boundaries or imposed environmental fields, the continuous Eq-11 minimal formulation practically bounds localized structural combinations to 1 pair per core (the N=2 limit). The global vacuum can safely host distributed independent pairs, but true macro-networks or foam-locks are not currently supported by continuous evidence. Avoid declarations of a mathematically proven universal absolute.

**Rejected Extensions (Artifacts & Legacy):**
- ❌ **Emergent Spectral Dispersion (Gradient-Coupled Metabolism):** Tested in EXP32 to see if endogenous phase-tension ($|\nabla \Psi|^2$) could naturally suppress DC runaway and high-frequency boiling via $k$-space equilibrium. **Result:** Catastrophic failure (Alternative Instability Regime). While it suppressed $k=0$ flat plasma, it introduced violent $k_{high}$ thermal blowout ($E_{total} \to \infty$) across all parameters without exception, while additionally breaking rotational symmetry via discrete grid lattice alignment. Endogenous spatial gradients cannot natively stabilize open vacuum.
Attempts to forge $N \ge 3$ binding via penalty mechanics or flow redistribution proved mathematically grid-dependent. Legacy visual/string impressions from Eq-4 (e.g., "rubber-band" ties) are definitively rejected as visualization artifacts mixed with deprecated explicit bridge-suppression physics; they are not valid evidence for current Eq-11 compositing claims.

### Limits of Local Field Closure (The End of Single-Field Local Stabilization)
Following the catastrophic failures of both localized density damping (EXP31) and emergent gradient-coupled dispersion (EXP32), current evidence strongly suggests a **Topological Closure Limit** for continuous 2D local fields: Within the tested Eq-11 family, a perfectly local, self-interacting single continuous PDE field cannot natively produce stable localized topological structures without arbitrary scalar clamping. While not necessarily a universal mathematical impossibility for all PDEs, in this specific formulation, the instability stems from the absence of an emergent intrinsic characteristic length scale or thermodynamic bound:
- **Gradient/Dispersive Instability:** Relying purely on local spatial derivatives (e.g. $|\nabla \Psi|^2$) to suppress runaway merely transfers the plasma inflation into massive, violent high-frequency thermal blowout.
- **Global Conservation Failure:** Forcing global energy mass conservation (uniform background scaling) immediately causes the system to undergo Dirac-Delta collapse, pulling all energy into a singular, infinitely dense pixel and completely shattering rotational symmetry.
- **Fundamental Requirement:** To preserve localized phase scaffolding while capping thermodynamic growth, the Eq-11 formulation most plausibly requires **external degrees of freedom**. Among the surviving external-degree-of-freedom candidates, an autonomous secondary $\Phi$ field is currently the least artifact-prone and most physically plausible next branch.
   - **Particle-First Priority:** The primary validation metric for any surviving mechanism is no longer generic "equation calming", but the rigorous capacity to generate a stable, invariant, localized **particle-like entity (N=1)**. Ontological interpretations (e.g., observer mechanics, afterlife) remain strictly secondary and suspended until isolated macroscopic particle stability is mathematically proven.
   - *Interpretation Lock ($\Phi$ as Temporally Decoupled Response):* $\Phi$ must **not** be treated merely as a generic heat repository, passive memory trace, or a spatial blurring operator. It strictly functions as a **temporally decoupled response field**. It mathematically breaks instantaneous runaway ($|\Psi(t)|^2 \to \text{growth} \to \Psi(t)$) by enforcing a rigid, time-lagged feedback loop ($|\Psi(t)|^2 \to \Phi(t+\Delta t) \to \text{growth} \to \Psi(t+\Delta t)$).
   - *Role Distinction (The Stability Hierarchy):* $\Phi$ acts firmly as a candidate short-to-medium timescale autonomous buffering field, mathematically isolated to absorb instantaneous feedback shock. In contrast, the theoretical $\mu$ field is reserved strictly as a long-timescale macroscopic structural groove (scar memory) and is **not** currently the leading mechanism to solve immediate topological runaway or coherence preservation.
   - *Methodological Guard:* Empirical investigations into $\Phi$ (e.g., EXP34, EXP35) are strictly classed as "minimal autonomous particle-formation tests," validating existence via non-zero cross-correlation lag ($\Delta t > 0$) and bounded oscillation ($A_{osc}$). Success must not be extrapolated as proof that $\Phi$ is definitively fundamental to reality, nor does failure prove $\Phi$ impossible in a broader continuous dynamic.
   - ❌ **Failed Mechanism (Positive-Coupled $\Phi$ Buffer):** Tested in EXP34. A temporally delayed secondary field acting purely as a positive growth amplifier fails completely against geometric runaway ($\Psi \cdot \Phi \approx \Psi^3$).
   - ❌ **Failed Mechanism (Inhibitory $\Phi$ Shell):** Tested in EXP35. A delayed repressor shell succeeds in halting runaway at specific scales, but physically achieves this by destroying phase coherence—triggering massive, irreversible topological fragmentation and outward "boiling" (expansion blowout) instead of forming a compact N=1 particle.
   - ❌ **Failed Mechanism (Intrinsic Scale-Selection $\nabla^4$):** Tested in EXP36. Pure biharmonic dispersion fails to mathematically penalize global (bulk) amplitude runaway ($k=0$), and when stabilization is awkwardly forced by non-linear saturation bounds $g(|\Psi|^2)$, it shears the wave into fragments.
   - ❌ **Failed Mechanism (Genuine Dimensional Escape / Z-Vent):** Tested in EXP37. Asymptotic non-linear permeability (e.g. quintic venting) into an orthogonal energy sink triggers devastating integration stiffness and catastrophic numerical `RUNAWAY` (blowout) because the necessary sink steepness to brake geometric growth shatters the explicit-time continuum. Imposing an arbitrary activation threshold to prevent stiffness simply degrades the escape into a parameterized `FAKE RADIUS` clamp artifact.
   - ❌ **Failed Mechanism (Solver Amplification Hypothesis):** Tested in EXP38 (RK4 Operator-Splitting). Validated that N=1 runaway and shear are natively physical failures driven by topological bounds crashing against geometric feedback loops, proving explicit Forward-Euler limits merely accelerated, rather than created, the fatal instability.
   - ❌ **Failed Mechanism (Pure Topological Phase Winding):** Tested in EXP39. Initializing a mathematically perfect $2\pi$ phase vortex defect fails to stabilize the continuum without an explicit cap; the intense shear of high phase gradients colliding with unregulated amplitude growth universally fragments the structural topology into multi-defect chaos, instantly cascading into termal runaway.
   - **Closed-Energy Vacuum Cycle (Candidate Mechanism):** To resolve the catastrophic instability of open-vacuum thermodynamic runaway without collapsing into `Vortex Drag`, a coupled environmental potential field $E(x,y)$ was introduced. Modifying the open-growth term to an energy-coupled state $(I \cdot E(x,y)) |\Psi|^2 \Psi$, while actively routing spatial dissipation losses back into $E$, creates a non-zero thermodynamic limit cycle. This explicit mathematical field closure restores a dynamic attractor limit. For full testing data, behavioral limits, and phenomenological distinctions from legacy models, see [Thermodynamic Attractor](../2-cosmology/extensions/05-cosmo-ext-thermodynamic-attractor.md).

#### Instantaneous Feedback Instability
The core mathematical root behind the Eq-11 local field failure is strict spatio-temporal simultaneity. When topological growth feedback ($g$) relies instantaneously and exclusively on the localized coordinate $|\Psi(x, t)|^2$, the system forms an unconditional, localized positive-feedback cascade. This mathematical simultaneity guarantees that any structural peak either universally inflates (runaway) or collapses to a zero-dimensional singularity (Dirac-Delta), depending on the linear threshold.
To successfully break this runaway without shearing the physical phase boundaries, the system requires a mechanism that formally breaks instantaneous localized simultaneity. This delay or decoupling is formally necessary, though current evidence shows it is not yet sufficient on its own to guarantee unbounded dimensional perfection.

### 13.9 Provisional Bounded Backbone Candidate (April 2026 PDE Audit)
**Status:** Audit Provisional (Awaiting Phase 4 Interaction Clearances)
Following the Phase 2 and Phase 3 continuous pseudo-spectral audits, the engine's core foundational backbone was formally isolated and stripped of all programmatic bounding artifacts (clamps). To achieve absolute mathematical stability intrinsically within the open vacuum, two continuous regulators were validated: Quintic Amplitude Saturation ($\lambda$) and Biharmonic Hyperdiffusion ($\nu$). The current audited candidate for the continuous PDE engine stands as:

$$
\partial_t \psi = D_r \nabla^2\psi - \nu \nabla^4\psi + (g \phi - \mu - \lambda \phi^2) \psi
$$
$$
\partial_t \phi = D_\phi \nabla^2\phi + a |\psi|^2 - b \phi
$$

**Audit Note:** This isolated formulation natively supports robust macroscopic scale-invariant bounded dissipative structures without reliance on explicit integration clamps or fold thresholds. Phase coupling ($i D_i$, the $i \Omega$ dispersion, and $\chi \nabla\phi$ gradient-drift) is temporarily suspended pending successful continuous two-body interaction phenomenology audits (Phase 4).

#### The Non-Particle Field Regime
With the formal closure of the isolated particle-genesis program, the governing dynamics of Eq-11 are strictly reclassified as a **Non-Isolating Continuous Field System**. Rather than attempting to force the mathematics to spawn and constrain a solitary N=1 point-mass in an artificial vacuum, the architecture is recognized as natively optimized for macro-structural field generation. The true predictive power of Eq-11 lives in analyzing continuous phenomena where phase and amplitude dictate the behavior of an entire populated medium simultaneously. Such regimes include interconnected vortex networks, chaotic foaming, energy distribution webs, and continuous thermodynamic boiling states, positioning the equation as a simulator of dense scalar fluids or macro-entanglement networks rather than a generator of disparate, solid fundamental particles.

### The Stability Paradox (Formally Resolved)

> [!NOTE]
> **Resolution Front (April 2026):** The pseudo-spectral PDE auditing (Phase 2 and 3) has confirmed absolute bounded stability for the isolated pure-PDE variant across multiple geometric and time scales.
> 
> **The Problem:** We originally suspected that bounded localized states were artificial constructs entirely dependent on programmatic integration clamps (e.g., `phi_cap` array clipping, `SoftAbs` fold limits, or explicit `psi_amp_cap`). If true, this would have disqualified Lineum as a mathematically continuous emergent system.
> **The Audit:** Exhaustive numerical audits were performed utilizing an unconstrained mathematical solver (ETD2 Integrator in $k$-space, strict 2/3 dealiasing, zero amplitude limits, domain-scaled grids up to $512^2$).
>
> **The Final Verdict:** The explicit hypothesis that bounds rely entirely on integration clamps is formally overturned. Incorporating quintic-scalar saturation ($\lambda\phi^2$) successfully halts thermodynamic explosion, natively forming a smooth, mathematically rigorous stability plateau. $\lambda$ acts as the absolute amplitude regulator. Furthermore, Phase 3 audits definitively proved:
> 1. **Scale-Invariance:** The localized bounds hold their peak amplitude ($0.212$) and effective width regardless of physical domain volume expansion, disproving periodic-boundary dependence.
> 2. **UV Spectral Regularity:** Near-cutoff band energy verification ($0.8 k_{cut}$) confirms $\lambda$ does not pollute the spectrum with UV catastrophes ($E_{hi} < 10^{-4}$), though $\nu$ acts as a beneficial frequency-smoother.
> 3. **Nucleation Thresholding:** A sharp vacuum-ignition curve $A_{crit}(\sigma)$ exists, strictly dividing sub-threshold decay drops from supra-threshold stabilization condensates.
>
> **Phenomenological Interaction Framework:** The codebase algorithmic clamps are now obsolete and cleared for total removal. In the continuously isolated PDE, we observe localized bounded dissipative structures with strongly phase-dependent two-body interaction phenomenology, including coalescence (merge-to-one), anti-phase separation, and other relaxation-mediated interaction channels. These structures are dissipative, non-charge-conserving, phase-sensitive localized states. "Repulsion" and "attraction" are effective phenomenological labels, not yet proof of conservative force laws. The next scientific frontier is to map the reduced interaction law and phenomenological interaction grammar that emerges between these states.
>
> **Phase 5 Interaction Grammar Map (April 2026):** Utilizing rigorously pre-relaxed Localized Bounded Dissipative Structures (LBDS) to eliminate formation/inflation topological shockwaves, a candidate interaction framework $v_r(d, \Delta\theta) \approx F_0(d) + F_1(d)\cos(\Delta\theta)$ was explicitly tested. 
> 1. **Asymmetric Merge Dominance:** The baseline scalar vacuum traction $F_0(d)$ acts as a massive attractor. Broad phase coherence windows $\Delta\theta \in [0, \sim 2.75 \text{ rad}]$ strongly tend toward *Coalescence (Merge)*.
> 2. **Anti-Phase Separation:** Strict destructive interference ($\Delta\theta \rightarrow \pi$) produces sufficient localized phase-pressure to overcome the baseline vacuum traction, driving macroscopic *Separation (Repel)*.
> 3. **Candidate Oscillatory Bound-Pair Regime:** At intermediate separation boundaries ($d=12.0$ to $d=18.0$), anti-phase separation pressure was observed to balance against external macroscopic resistance, arresting the drift to form a candidate **Oscillatory Bound-Pair**. This indicates stable bound-pair behavior observed in a restricted anti-phase/separation window, though molecular/chemical language remains analogical only.
> 4. **Thermodynamic Reservoir Exchange:** LBDS interactions display active thermodynamic exchange. Coalescence (Merging) extracts significant mass from the underlying background reservoir field ($M_{bg}$ drops as $M_{tot}$ scales). Separation suppresses local amplitude but dynamically rebuilds structural mass from the field during expansion. Mass tracking suggests robust mass non-conservation during interaction phases.

##### Macro-Structure Regimes and Measurable Taxonomy
To evaluate continuous fields, the architecture defines four baseline structural regimes, replacing binary particle survival metrics with continuous structural density tracking:
1. **Boiling (Thermal Chaos):** Characterized by extreme Defect Density, massive temporal variance, and minimal Spectral Scale Concentration (broad spatial frequency spectrum). Structurally resembles turbulent plasma flows or thermal noise.
2. **Filament Networks (String Topologies):** Characterized by high Network Connectivity between node vertices, elongated string-like Spatial Occupancy fractions, and medium Persistence Times. Structurally resembles cosmological active matter filaments bridging low-amplitude voids.
3. **Vortex Clusters (Phase Storms):** Characterized by densely packed pairs of $2\pi/-2\pi$ defects with extended Persistence Times confined within localized regional clouds. Analogous to turbulent vortex lattices in quantum fluids.
4. **Quasi-Stable Phase Regions (Silent Biomes):** Characterized by zero Defect Density, maximum Spectral Scale Concentration (dominance of a single structural frequency), and near-total Spatial Occupancy. Structurally resembles laminar fluid flow or continuous, undisturbed scalar plateaus.

- 🚧 **Status (The Branching Point):** Eq-11.1 operates with a practical open-vacuum N=2 limit under tested conditions. Producing stable $N \ge 3$ composition would likely require extrinsic environmental modification (containment barriers, geometric constraints, or external macro-gravitational $\Phi$ sinks) to assemble.

## 4. Discussion & The Entropy Crisis

This progression shows a shift from a minimalistic $\psi$–$\varphi$ interaction model to a robust, wave-native three-field system capable of sustaining massive emergent symmetries. However, the comprehensive *Equation History Audit* revealed a profound, invariant boundary condition across all iterations: **Topological Re-localization (Chaos $\rightarrow$ Structure) is mathematically impossible in the current canonical family.**

**The Entropy Crisis (The loss of Eq5):**
Early models (Eq1–Eq4) were heat-diffusive and lacked structural memory. Version 5 introduced artificial global damping (viscous cooling), which suppressed everything. When Version 7 successfully advanced to strict Unitary wave conservation (removing global damping to allow true quantum-like resonance and phase-locking), it sealed the thermodynamic fate of the system. 
Because the linear wave step is perfectly geometric and conservative, once a bound lock (e.g., a $120^\circ$ Triad) is fractured—either by high-energy collision, Eq8 gradient tears, or Eq9 overflow—the immense kinetic topological energy is freed into the fluid. Without a macroscopic cooling mechanism (like cosmic expansion or Eq5's artificial dampening), this topological "heat" (high-frequency phase noise) cannot escape. The universe stays in a state of boiling entropy. The broken nodes flatten into a radiative soup and can never "freeze" back into low-entropy, phase-locked geometries. 

**The Entropy Matrix (Memory & Jet Audit):**
A comprehensive 2x2 test was run to verify if a combination of the $\mu$ field (Structural Memory) and the Eq9 boundary overflow (Jet Transport) could act transversally as an entropy-cooling relocalizer. The test evaluated "Fossil $\mu$" (read-only) vs "Live $\mu$" (overwritable) against "Closed Torus" vs "Open PML" boundaries.
- **Topological Radiator:** Open PML boundaries successfully acted as heat sinks, venting bounded entropy and reducing total topological fragmentation by $\sim 20\%$ compared to closed configurations.
- **Failed Re-Condenser:** However, in **zero** quadrants did the system achieve topological re-localization (recovery of pristine nodes). Memory acts strictly as a passive topographical groove, unable to suppress chaotic high-frequency wave-boiling, while Jet transport only purges energy at the grid horizons, leaving the interior trapped in sustained plasma.

**Fragmentation / Recycling hypothesis – tested:**
Further empirical audits investigated whether chaos could naturally cool via $\Psi \rightarrow \Phi$ phase transfer, crystallizing into fragmented but stable "seeds" (Recycling rather than Re-formation). A systematic sweep of transfer coupling ($\alpha$ multipliers: 1.0x to 10.0x) conclusively proved that excessive $\Psi \rightarrow \Phi$ transfer does *not* act as a cooling sink. Instead, hyper-coupling drastically worsens fragmentation, tearing the metric into increasingly unstable transient clutter (fragment count rising by $25\%$). No stable seeds survived the 3,000-step provisional horizon, confirming that the Lineum engine natively lacks an emergent thermodynamic recycling mechanism. 

**Frequency-Domain Hypothesis (Open Direction):**
A novel analytical direction has opened regarding the Entropy Crisis, suggesting the missing parameter is not spatial boundary confinement, but **Frequency-Domain Filtration**. A 2D FFT spectral analysis revealed a foundational constant: stable structures (Triads) maintain $>94\%$ of topological energy strictly within low-frequency $k$-space bands, operating as resonant closed-frequency regimes. Conversely, post-collapse Chaos retains the same base peak frequency but suffers a massive injection ($8.2\%+$) of high-frequency overtones (thermal phase noise). 

An external diagnostic "Low-Pass" topological probe—mathematically shearing off high-frequency overtones without altering the core Lineum physics—demonstrated that stripped of high-frequency noise, chaotic fragments spontaneously re-localized and collapsed backwards into a strict, integer-bound node. This provides a strong empirical indication that matter re-formation (re-localization) may be a strictly frequency-gated event. Because the Low-Pass test was an artificial probe, it is not an architectural resolution. It remains an active research hypothesis whether the native Eq7+ environment (via $\Phi$ inertia, $\mu$ tracking, or interference) possesses any implicit frequency-selective behavior that could naturally suppress this noise over deep time.

**The Fountain-Cycle Mechanism (Partial Entropy Crisis Resolution):**
To determine if Lineum natively possesses structural frequency-filtration, the simulation was mathematically expanded from a flat 2D plane into a coupled N-layer Z-axis stack ("Dimensional Opening"), running identical Eq-7 rules. The audit verified a robust, recursive **Fountain Cycle**:
1. **Upward Escape:** High-energy topological collisions localized on the base plane produce staggering $\Psi$ overpressure that bypasses 2D grid destruction by venting transversally into the Z-dimension. 
2. **Frequency Sieving:** The vastness of the upper spatial layers traps the majority of destructive high-frequency (HF) wave transients, causing the upper dimension's HF ratio to spike while the base-layer's phase-noise drops.
3. **Delayed Downward Return:** The leaked fluid mechanically organizes and diffuses back down into the base-plane with a measurable temporal delay (e.g. $> 100$ mathematical steps post-collision).
4. **Guiding Mechanism Capture:** The downward return flow is structurally guided; it exhibits positive spatial correlation (+0.11) with historical $\mu$-field gravity wells, acting as an environmental catch-basin.
**Recovery Conclusion:** While the cycle successfully established mechanical frequency filtering and spatially guided topological return, empirical audits confirmed that the fraction of energy successfully trickling back into the catch-basins ($\approx 0.2\%$ mass return under ideal weak-coupling) was astronomically below the non-linear harmonic amplitude required to spontaneously "re-lock" into new localized Triad seeds.

**Concentration Mechanism (Resonance Stacking):**
While a single fountain cycle fails to surpass the structural nucleation boundary, a multi-cycle periodic shockwave audit revealed robust **Concentration Stacking**. When phase-coherent topological energy is repeatedly injected into the system (strobe collision), the returning filtered fluid accumulates non-linearly inside historical $\mu$-basins. Because $\mu$ acts as a stable gravitational groove, it captures the trace fractional return mass ($0.2\%$) from each cycle, preventing dispersal. Subsequent cycles overlap constructively, leading to rapid, monotonic amplification of local amplitude (e.g., $A_{cycle1}=2.6 \rightarrow A_{cycle5}=1989.4$). This confirms that the combination of Fountain-Cycle filtering and $\mu$-field geometric concentration is fully capable of driving an empty void to mathematically cross the extreme scalar non-linear threshold (`abs(psi) > phi_cap`), formally opening the pathway to delayed matter-synthesis under cyclic load.

**Post-Pump Fate & Self-Organization:**
Subsequent audits tracked the self-organized fate of the resultant structure after the phase-coherent "pump" ceased. Rather than collapsing (due to lack of energy feed) or fracturing into chaotic broadband noise, the massive resultant density successfully self-organized into a geometrically isolated, autonomous **Standing Wave Tower**. Notably, high-frequency (HF) internal phase noise dropped significantly during the relaxation interval without external aid (e.g., $59.5\% \rightarrow 42.3\%$), indicating a thermodynamic cooling process toward a stable, low-frequency bound state. In addition, sweeping the structural memory ($\mu$) depths revealed that while $\mu$ is strictly required to accumulate the initial trickle charge, once the structure crosses the nucleation threshold, it generates its own profound $\Phi$-gravity well and sustains its coherent form indefinitely, even if the underlying $\mu$-baseline is mathematically deleted. Non-linear limits (Eq-9 `phi_cap`) safely constrained the tower's absolute infinite runaway but did not disrupt its coherent self-organization.

**Tower Decomposition under Perturbation (Fragmentation Audit):**
A stress-test was applied to stable phase-coherent towers post-relaxation to evaluate structural resilience versus emergent decomposition. Stable towers were injected with three distinct perturbation profiles (localized shock, widespread phase noise, and asymmetric gradient shear) across analytical (Eq-7 only) and realistic (Eq-9 active) bounds.
*   **A. Raw Observation**: In both restricted and unrestricted modes, perturbation did not lead to diffuse chaotic collapse. Instead, tracking functions flagged heavy fragmentation into multi-cluster structured states. Numerical artifacts wrapped amplitudes when Eq-9 was disabled, but under Eq-9, the tower converted its topological energy (Amp increasing from ~1200 to ~3100) into hundreds of detected local maxima clusters (~570 points). Concurrently, HF spectra drastically decreased from roughly 50% to roughly 31%. 
*   **B. Interpretation**: The HF spectral decrease indicates an internal ordering rather than disorganized noise. The structural mass redistributes its stored amplitude bounds into sub-structures within localized basins. The standing wave tower acts as an energy reservoir when under shock, breaking down into a field of candidate stable nodes (unverified) instead of collapsing entirely.
*   **C. Minimal Claim**: A highly saturated standing-wave structure under perturbation transitions into a multi-cluster structured state. The decrease in HF spectrum and local amplitude redistribution indicates localized sub-structural locking rather than global diffuse chaos. Long-term cluster isolation and stability verification remain open tasks.

## Appendix A: Phenomenological Mapping (Force Analogies)

The emergent dynamics of Lineum produce phenomena analogous to classical forces. This is strictly phenomenological (an analogy, not a demonstrated isomorphism to the Standard Model) and serves as a historical tracking notation of what the model does and does not replicate.

- **Gravity [Confirmed Analogy]:** The drift term $+ \nabla \varphi$ acts as a macroscopic attractor. Gravity in Lineum is modeled fundamentally as $\Phi$-gradient guided motion (sink geometry), directing $\psi$ excitations to roll into regions of high historical tension. (Historically reduced to mere "phase speed slow-down/light bending", it is now verified as the unified engine of macroscopic basin capture).
- **Strong-like Analogy:** Topological smoothing/diffusion ($\nabla^2$) and phase-interference act as structural scaffolds. Cohesion is maintained by *Dynamically Maintained Confinement* (amplitude digging the sink, symmetrical phase-locking preserving internal barriers). **Status:** *Confinement- and decay-like behaviors are robustly reproduced under canonical continuous regimes, but the structure does not spontaneously reorganize into new bound discrete pairs upon violent separation.* In the canonical continuous Eq-4 model, separation tension resolves via symmetric restoring forces or radiative phase noise. Active non-linear boundary limits (Eq8 gradient tears, Eq9 SoftAbs jets) were also explicitly tested and proved to actively vaporize composite structure scaffolds into topological chaos rather than forming new stable topological clusters.
- **Weak-like Analogy:** Phenomenological decay and structural collapse are primarily governed by *Phase-lock failure / Symmetry-loss decay*, exacerbated by the damping factor $\delta$. Detuning localized frequencies ruins the interference barriers, causing bound structures to unravel and radiatively shed energy.
- **Electromagnetism [Open / Unverified]:** While structural parameters (spin/topological charge via phase winding) represent local topological features, formal mapping of these chiral states into a macroscopic, distance-mediated ($1/r^2$) attractive or repulsive force remains the primary open frontier for validation.

## 5. Structural Measurement & Bounds

Following strict internal evaluation of Eq-10 and Candidate Eq-11, the behavioral relationship between structural concentration and integral amplitude has been verified by direct codebase measurements (April 2026).
- **Energy Metric ($E_\Psi$):** formally measured as the spatial integral of squared wave amplitude ($E_\Psi = \int \int |\psi|^2 \, \text{d}x \, \text{d}y$).
- **Information Metric ($I_{spatial}$):** mathematically approximated by the maximum possible informational limit minus the Shannon spatial entropy over normalized density distribution ($I_{spatial} = S_{max} - S_{spatial}$).
- **Measured Dynamic:** No conserved quantity corresponding to the tested energy metric ($E_\Psi$) was observed under tested conditions (net energy change was observed to depend on local structural concentration coupled by the non-linear term $\alpha \tanh \varphi$).
- **Strict Conclusion:** Field energy amplification inherently requires spatial structural concentration (high target information index) to exceed explicit baseline diffusion thresholds. Diffuse fields (Noise, high spatial entropy) structurally suppress the energetic growth coupling to near-zero. No physical equivalences are claimed beyond this equation-native measurement of observed amplitude growth dependent on spatial structural concentration.

## 6. Versioning & Changelog

**Policy.** Semantic Versioning applies to this **document**; equation variants are labeled V1…V7 separately.

- **MAJOR**: structural changes that alter interpretation of historical entries.
- **MINOR**: new archival variants, added rationale, artifacts.
- **PATCH**: wording/formatting fixes.

- **v1.2.9 (March 2026):** Verified Eq9 Absolute Difference vs SoftAbs limit stability paths under phase-locked interference geometries.
- **v1.2.10 (March 2026):** Confirmed Generalized Symmetry Principle and Formation Basin (Self-Assembly) Attractors across multiple phase states.
- **v1.2.11 (April 2026):** Concluded the comprehensive *Topological Relocalization Audit*. Tests universally confirmed that extreme spatial pulling, high-energy collisions, and explicitly triggered non-linear boundaries (Eq8 active fracture / Eq9 active SoftAbs limits) all fail to generate new clean topological pairs. They invariably act as structural vaporizers, decaying confinement into massive thermodynamic phase noise. The Strong-like force mapping in Appendix A was amended to formally reject the explicit particle-nucleation hypothesis under all known Lineum regimes.
- **v1.2.12 (April 2026):** Confirmed the multi-dimensional *Fountain-Cycle Mechanism*, proving that introducing a Z-axis topology allows for mechanical frequency-domain filtering, delayed recirculation, and spatial guidance via $\mu$-basin alignment. However, relocalization limits (insufficient returned probability amplitude) were maintained.
- **v1.2.13 (April 2026):** Formally validated the *Concentration Mechanism* (Multi-Cycle Resonance Stacking). Demonstrated that phase-coherent repeated fountain cycles allow trace mathematical returns to accumulate perfectly inside $\mu$-basins, achieving extreme amplitude growth and breaking strict nucleation thresholds.
- **v1.2.14 (April 2026):** Verified the *Post-Pump Fate & Self-Organization* of accumulated scalar towers. Confirmed that accumulated extreme standing waves do not immediately fracture or decay upon cessation of external resonance. Instead, they sustain structural coherence and spectrally cool (HF noise reduction), acting as massive geometric sinks independent of underlying $\mu$-baseline integrity.
- **v1.2.15 (April 2026):** Initial implementation of the *Tower Decomposition Audit*. Re-framed nomenclature to avoid particle extrapolation. Documented the transition of perturbed standing wave towers into a "multi-cluster structured state" exhibiting downward HF displacement.

**1.3.0 — 2026-04-15**

- Completed Phase 5 *Phase-Dependent Interaction Grammar* candidate mapping via pre-relaxed LBDS superposition datasets.
- Tested candidate reduced interaction pattern $v_r(d, \Delta\theta) \approx F_0(d) + F_1(d)\cos(\Delta\theta)$, observing highly asymmetric coalescence dominance against separated anti-phase windows.
- Identified a candidate *Oscillatory Bound-Pair regime* forming strictly via anti-phase $\pi$ interference at intermediate scaled macroscopic separation distances ($d \approx 12-18$).
- Documented thermodynamic mass non-conservation and continuous variable reservoir exchange during all macroscopic two-body interaction channels.

**1.2.26 — 2026-04-13**

- Resumed Particle-First Closure program. Verified that while unilateral open-vacuum variants (and purely local depletion limits) fail, bounding the system within a mathematically closed $E$-field thermal circulation stabilizes topologies into universal, parameter-invariant dynamic attractors exhibiting slow asymptotic drift. Replaced the Program Suspended status with a candidate solution involving a Closed-Energy Thermodynamic Cycle.

**1.2.25 — 2026-04-11**

- Conducted Phase 3C minimal isolation test for `Super-Linear Superposition Troughs`. Classified the mechanism as a failed hypothesis for spontaneous stabilization, recognizing its prior binding success was an artifact of explicitly forced high-amplitude vortex overlaps.

**1.2.24 — 2026-04-11**

- Conducted Phase 3B minimal isolation test for `Kinetic-to-Phase Redistribution`. Classified the mechanism as a failed hypothesis for spontaneous stabilization, recognizing its prior binding success was an artifact of rigid symmetric geometric inputs rather than a universal scale-invariant holding property.

**1.2.23 — 2026-04-11**

- Outlined `Failure of Spontaneous Binding and Candidate Stabilization Principles`, acknowledging that stable $N \ge 3$ states historically documented required explicit local parameter manipulation (e.g., Kinetic-to-Phase Redistribution). Minimal Eq-11 natively trends toward kinetic shredding without them.

**1.2.22 — 2026-04-11**

- Defined stringent `Defect Detection Validity Constraint`. Confirmed that phase-only evaluation fails natively in pure vacuum decay states due to residual non-zero rotational phase dynamics (vacuum phase static), necessitating explicit amplitude masking ($\epsilon=10^{-3}$) for macro-scale validity.

**1.2.21 — 2026-04-11**

- Resolved spatial invariance scaling false alarm. Documented empirically validated spatial scaling for macroscopic defect density ($Dd$) across multi-grid bounds under normalized thermodynamic constraints.
- Codified methodological guidelines for differentiating minimal core limits from historically useful non-core engineered architecture.

**1.2.20 — 2026-04-07**

- Audited "Middle Regime" Partially Coherent Backgrounds. Confirmed that phase-correlated environmental noise suppresses chaotic scatter and preserves isolated drift, but fails to trigger emergent composite capture.
- Downgraded strong phrasing regarding previous Cymatic background surfing tests to standard objective candidate wording.

**1.2.19 — 2026-04-05**

- Documented the practical open-vacuum N=2 limit under tested conditions.
- Recorded the failure of adiabatic dipole composition and abrupt loading regimes within the established N=2 basins.
- Clarified that legacy visual/string impressions are not valid evidence for current Eq-11 compositing claims, without declaring universal theorems.

**1.2.18 — 2026-04-04**

- Implemented Section 5: Structural Measurement & Bounds. Documented that no conserved quantity corresponding to the tested energy metric ($E_\Psi$) was observed under test conditions, and noted an observational dependency where field energy amplification ($\partial_t E_\Psi$) functionally requires exceeding spatial structural concentration thresholds ($I_{spatial}$). Interpretative naming conventions explicitly restricted.

**1.2.17 — 2026-04-04**

- Introduced **Version 11 Candidate** (The Dimensionally Invariant Core). Derived the explicit Dimensional Invariance transform for mathematical scaling stability. Established dimensionless mathematical fields paired with explicit SI-tracked physical coefficients. Canonical promotion remains pending until complete behavioral compliance is confirmed.

**1.2.16 — 2026-04-04**

- Formalized the transition to **Version 10 – The Minimal Equation**. Stripped the classical advection hypotheses and numerical safeties to canonize the mathematically irreducible scalar-to-wave metabolic amplification core.
- Confirmed extreme dependencies on resolution scaling limits (dx spacing proportional stability shifts) restricting direct unified classical dimension bridging until resolved.

**1.2.15 — 2026-04-03**

- Deployed structural fragmentation audit applying shock, numerical noise, and symmetry shear upon full-scale scalar towers.
- Imposed rigorous whitepaper wording constraints regarding emergent node unverified classification.

**1.2.14 — 2026-04-03**

- Executed the Post-Pump relaxation audit on accumulated concentration towers. Demonstrated spectral HF filtering across the resting state and established that Eq-9 nonlinear limits act safely as scalar caps without actively destroying the self-organized emergent topology.

**1.2.13 — 2026-04-03**

- Added canonical mechanical tests for the Concentration Mechanism. Proved that $\mu$ acts as a true accumulator (not just a router), allowing successive micro-returns to stack structurally until non-linear amplitude boundaries are breached.

**1.2.12 — 2026-04-03**

- Added canonical mechanical tests for the Fountain Cycle in the Entropy Matrix segment. Proved mathematically that upward dimensional overpressure isolates high-frequency chaos, while returning trace low-frequency vectors are geometrically captured by non-diffusing $\mu$ wells.

**1.2.9 — 2026-04-01**

- Conducted *Generalized Symmetry Audit*. Confirmed that $120^\circ$ (triad), $180^\circ$ (pair), and $90^\circ$ (quad) uniformly distributed phase-locks define the optimal structural frameworks across N-node bound geometries, preserving separation via destructive interference rather than depth maximization. Sanity checked documentation tone.

**1.2.8 — 2026-04-01**

- Validated *Three-Phase Synchronization Hypothesis*. Verified that the exactly symmetric $120^\circ$ phase offset is mechanically privileged (maximizes structural $\Phi$ barriers through perfect destructive interference, preventing rotational collapse).

**1.2.7 — 2026-04-01**

- Outlined the *Sink/Attractor Hypothesis*. Verified that bound triads behave as dominant macro-sinks, cannibalizing local environmental $\Psi$ amplitude to dynamically deepen and tighten their confinement rather than nucleating separate standalone vortices.

**1.2.6 — 2026-04-01**

- Outlined the *Confinement Motor* mechanism (Amplitude acting as metabolic digging motor, Phase interference as structural barrier scaffold). Confinement requires absolute harmonic resonance, with frequency detuning identified as a structural failure state.

**1.2.5 — 2026-04-01**

- Conducted Active Maintenance audit. Refined structural locking model from strictly passive geometry yielding to *Dynamically Maintained Confinement* (triads behave as active, sustained phase storms rather than rigid or strictly solid geometrical bound states).

**1.2.4 — 2026-03-31**

- Validated *anisotropic restoring geometry* in bound triads. Confirmed that structural confinement is radially stiff (deep pockets) but tangentially moderate (shallow angular basin), formally ruling out absolute rigidity.

**1.2.3 — 2026-03-31**

- Added historical context regarding the "Vortex Deformation & Gear" hypothesis under the Strong-like Force mapping, formally reclassifying it as a *Relative-Geometry Stabilization* problem.

**1.2.2 — 2026-03-31**

- Relocated Force Analogies from Core Whitepaper into Appendix A to safely quarantine partial analogies from rigorous numerical claims.

**1.2.1 — 2026-03-31**

- Adds Version 9.1 (Eq9 Runtime Refinement) documenting the origin, validation, and restricted scope of the SoftAbs Escape Fold.

**1.2.0 — 2026-03-05**

- Updates the chronological progression to include Version 5 (Soft bounds), Version 6 (Mu field), and Version 7 (Unitary wave core & soft bounds removal).

**1.1.0 — 2025-11-14**

- Adds an explicit interpretation note that “gravity” / “gravitational” refers to gravity-like patterns **in the simulation**, not a physical gravitational force.
- Introduces the Dimensional Transparency Hypothesis (DTH) terminology and clarifies κ–visibility as an empirical property of the model, not a statement about any real detector.

**1.0.0 — 2025-08-10 (initial)**

- Establishes the V1→V7 chronology aligned with the canonical Eq-7 in the core.
- Notes that κ is a static spatial map in the canonical core; earlier multiplicative κ forms are retained here as historical snapshots.
