**Title:** Lineum Appendix – Equation History
# Core Engine Dynamics and Mathematical History
**Document ID:** 02-core-equation
**Status:** Canonical Source of Truth (Eq-1 through Eq-9)
**Version:** 1.2.11 (April 2026)
**Status:** Draft
**Date:** 2026-03-31

**Relates to:** `lineum-core.md` §3  
**Equation versions:** V1–V7 (canonical: V7)  

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

### 🔹 Version 1 – Purely oscillating field

```text
ψ ← ψ + 𝛌̃ + ξ + φψ − δψ + ∇²ψ
```

The first version contained only the ψ field. It generated linons, spin, and vortices, but did not allow accumulation or emergent attraction. The φ field was not yet dynamic.

- ✅ Generated **linons** and flows
- ❌ No accumulation or emergent gravity-like behavior (in the simulation)
- ❌ φ was static, without memory

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

## 5. Versioning & Changelog

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
