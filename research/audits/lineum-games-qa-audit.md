# Exploratory Audit: Games QA / Automated Level-Design Analysis

> **WARNING:** Exploratory, non-canonical, non-marketing raw internal branch log. 
> Built strictly on the validated binary-layout Flow Vulnerability product. 
> This is NOT an NPC pathfinding framework. This is NOT an A* replacement.
> This is strictly a hypothesis for an automated Level-Design / Map-Analysis static tool.

## 1. Scope & Objective
**Objective:** To verify if the established Flow Vulnerability pressure equations cleanly identify intuitive layout bottlenecks, traffic choke points, and kill-zones in classic multiplayer game archetypes, without simulating a single bot or calculating path nodes.

**Hypothesis:** The mathematical geometry evaluated by Lineum PDE correlates highly with the "Designer Intuition" of where player flow naturally compresses on a map (e.g., central doorways, bridges, lane convergence nodes).

## 2. Baseline & Metrics
**Baseline Strategy:** Pure "Designer Intuition" coordinates manually defined as obvious structural control zones for the map archetypes.
**Key Metrics to Track:**
- Absolute Matched Nodes (Euclidean proximity to predefined choke regions)
- False Positives (Extracting a node that a designer would find structurally meaningless)
- False Negatives (Missing a glaring, obvious choke point)
- Mean Error Deviation (px)

## 3. Current Status & Tests
**STATUS: EXPERIMENT DP-EXP-016 CONCLUDED (FROZEN)**
Generated a 5-archetype test bed encompassing standard competitive architectural flows.

## 4. Benchmark Results (DP-EXP-016)
**Date:** 2026-03-21
**Methodology:** Placed a single Source and Sink on opposing sides of 5 game map topologies (MOBA, BR, CS-Bomb, Arena, Linear). Extracted top flow vulnerability nodes and matched against 15 predefined "designer intuition" chokepoints (e.g. all 3 lanes in a MOBA).

**Raw Statistics:**
- Total Maps: 5
- Total Intuitive Zones Expected: 15
- Successfully Detected: 4 (26.7% Match Rate)
- False Positives: 5 (Mathematically valid but tactically meaningless snapping)
- False Negatives: 11 (Completely missed intended tactical chokepoints)

**Analysis (Why it failed the designer's intent):**
The physics engine is mathematically flawless at identifying the *Absolute Maximum Global Bottleneck*, but multi-lane multiplayer games rely on *Secondary and Tertiary Tactical Flanks*. Because diffusion calculates a holistic global minimum, the path of least resistance (Main Lane) handles the vast majority of the pressure. The Laplacian drop on secondary flanking routes is mathematically weaker, so they get completely masked out by the global percentile sorting.
To find *all* tactical chokepoints, the engine would need to run massive combinatorial multi-source/multi-sink passes to artificially force pressure through side-flanks. This breaks the promise of the "instant global read" and makes the product prohibitively complex for v1.

## 5. Verdict (Single-Source)
**WEAK / KILLED FOR SINGLE-SOURCE.**
Flow Vulnerability is an incredible tool for finding the single most dangerous architectural crush-point in a building. It is a poor tool for mapping all tactical multiplayer axes in a game level because physics naturally optimizes away from secondary routes. We formally killed the single-source Games QA use-case.

## 6. Restarted Exploratory Phase: Competing-Sources Interface (DP-EXP-018)
**Date:** 2026-03-21
**Rationale for Restart:** The previous fail (DP-EXP-016) was explicitly caused by *single-source starvation*. Fluid natively chose the path of least resistance (mid lane) and starved the flanks. However, a core native dynamic of Lineum is the "Stable Pressure Interface" (where two competing fields collide and neutralize). This mechanism might inherently reveal the global tactical front across *all* parallel lanes simultaneously without starving flanks, as boundary-pushing fluid naturally fills available geometric voids before colliding.

**Minimal Benchmark Design:**
**Test Maps:**
1. 3-Lane MOBA map.
2. Symmetric Arena (2 wide flanks, 1 narrow mid).
3. Asymmetric Map (slightly shorter mid lane, testing if the interface bends structurally or outright breaks flanks).
4. One Choke-Bridge + Side Flank map.

**Separation of Layers:**
- **Native Mechanism:** Two competing diffusion sources executing simultaneously (e.g., Team A injects into field $\Phi_A$, Team B injects into field $\Phi_B$). The native readout is the strict mathematical equilibrium frontier ($|\Phi_A - \Phi_B| \approx 0$).
- **Application Layer:** Interface morphological smoothing, threshold clustering, and purely visual rendering of the front-line.

**Kill Criterion:**
- If the stabilized equilibrium interface still collapses heavily into mid-lane dominance (pinching off and failing to vividly highlight the continuous front-line across the secondary tactical axes), the branch is frozen again definitively.

**Success Criterion:**
- The equilibrium interface band successfully and inherently spans multiple tactical axes/lanes, clearly outlining the structural "front line" of the map without requiring arbitrary combinatorial multi-run forcing.

## 7. Competing-Sources Benchmark Results (DP-EXP-018)
**Date:** 2026-03-21
**Execution:** 4 multi-lane game maps, evaluated under dual continuous $\Phi$ fields running symmetrically for 1600 total iterations. 

**Native vs Application Layers:**
- **Raw Lineum-Native Output:** The literal mathematical interface array spanning 700-900 continuous pixels per map where the two fields reached equilibrium ($|\Phi_A - \Phi_B| < 0.1 \times \Sigma_{\Phi}$). 
- **Application Layer Postprocessing:** Spatial proximity clustering (grouping pixels within a 12px radius) to evaluate if these bands formed clean, distinct tactical lines matching the expected lane count. 

**Results:**
- **3-Lane MOBA:** Detected 8 clusters (Expected: 3)
- **Symmetric Arena:** Detected 9 clusters (Expected: 3)
- **Asymmetric Open Field:** Detected 7 clusters (Expected: 3)
- **Choke-Bridge + Flank:** Detected 8 clusters (Expected: 2)

**Analysis of the Interface Stability:** 
The physical zero-crossing solved the *single-source starvation* (fluid did structurally populate all flanks). However, the frontline interface does not form a clean, singular coherent vector per tactical axis natively. It inherently splinters and fragments across minute geometric jaggedness, scattering the tactical line.

### Final Verdict: FAILED AND REFROZEN
The Games QA hypothesis is permanently refrozen. While the PDE solved lane-starvation natively, it failed the structural clarity metric. To force the 7-9 chaotic mathematical fragments into "3 clean tactical lanes", the system would require aggressive, rigid application-layer heuristics (curve fitting, artificial line-smoothing, and structural edge-chaining). This entirely strips the output of its natural mathematical elegance and renders it a heavily post-processed heuristic tool rather than a native API oracle.

## 8. Restarted Exploratory Phase: Dynamic Traffic Congestion (DP-EXP-019)
**Date:** 2026-03-21
**Rationale for Restart:** Test whether Lineum-native dynamic temporal friction (capacity scaling) solves the single-source starvation failure intrinsically, creating a pure geometric swarm simulation without artificial pathfinding heuristics.

**Native Mechanism:**
- Single geometric source ($\Phi$) mapped to a single sink.
- As the field diffuses, local friction (`mu` / `kappa`) structurally increases over iterations directly proportional to the local flow magnitude ($|\nabla \Phi|$).

**Results:**
- **3-Lane MOBA:** Mid lane activated at iteration 140, rapidly congested. Top/Bot flanks activated instantly at 139/140 due to simultaneous capacity mapping.
- **Symmetric Arena:** Mid activated at 138. Congestion flooded the chamber, activating Top at 179 and Bot at 178 safely spanning the arena natively.
- **Asymmetric Map (Shorter Mid):** Mid activated at 169. Native congestion beautifully pushed the flow into Top at 152 and Bot at 140 preventing direct-path domination.
- **Choke-Bridge + Flank:** Mid activated at 144, naturally spilling over into Top at 146.
- **Shorter but Narrower Mid:** The 2px narrow strip activated at 123 but instantly jammed ($0.95$ friction cap). Massive pressure subsequently burst into the wide Top at 165 and Bot at 166.

**Verdict: PROMISING EXPLORATORY SIGNAL (DEFERRED)**
**Analysis:** Native success. The mechanism proved capable of resolving single-source starvation dynamically and elegantly without any application-layer cheating, curve-fitting, or manual flank combinations. The core math simulated traffic capacity organically, generating a fully readable "overflow/congestion map" across all tactical axes natively.
**Next Steps:** This remains a *Narrow Exploratory Test*. It expands the verified capacity of the Lineum native core geometry drastically into swarm/crowd simulation territory without adding routing heuristics. It is highly promising but left entirely isolated from the current v1.0 commercial product claims.

## 9. Ablation & Robustness Phase (DP-EXP-019-R)
**Date:** 2026-03-21
**Rationale:** To brutally verify whether the DP-EXP-019 success was merely a fragile tuning artifact or a fundamentally robust native PDE mass-overflow constraint.

**Methodology:**
- Executed 112 multi-dimensional matrix simulations computing massive baseline integrations on 64x64 grid configurations.
- Swept parameters: Alpha (coupling strength 0.005 to 0.1), Max Kappa Cap (0.85 to 0.99), Source Pressure Base (1.0 to 50.0).
- Maps Tested: 7 archetypes including Symmetric, Asymmetric, Choke-Bridge, Narrow Mid, and Ultra-Wide flanks.

**Results:**
- **Baseline (Alpha = 0):** Completely confirmed the single-source starvation fail state mathematically. The narrow mid-lane flushed dynamically at iteration 145 while the flanks starved out, activating lazily at iteration ~925.
- **Adaptive Mechanism:** Mathematically solved starvation consistently. Under the adaptive constraint, mid-lane activated at 122, and its consequential structural solidifying (congestion limit) natively pushed the flanking routes to activate massively early at iterations 163/164.
- **Degeneration Check:** 0 cases of parameter degeneration. The native physical friction ceiling prevented the matrix from smearing field boundaries into unrecognizable blob noise.
- **Robustness Space:** 7 out of 7 adaptive parameter sweeps cleanly and naturally overflowed the tactical flanks globally without heuristic map-specific tuning.

**Verdict: ROBUST EXPLORATORY BRANCH**
**Limitation / Imminent Gap:** Due to computational limits, this massive scale sweep ran solely on 64x64 grids. The physical discrete gradient $| \nabla \Phi |$ geometrically decays as spatial resolution scales ($1/dx$). The mechanism is robust, but must pass a *Scale / Normalization Validation* (DP-EXP-019-S) up to 256x256 to prove mathematically pure scale-invariance before any further product elevation.

## 10. Scale & Normalization Validation (DP-EXP-019-S)
**Date:** 2026-03-21
**Rationale:** To verify whether the adaptive congestion mechanism scales geometrically or breaks apart on larger resolution topologies.

**Methodology:**
- Evaluated Baseline vs Adaptive friction across 3 multi-lane maps.
- Execution bounded to progressive scale steps: 64x64, 128x128, and testing bounds of 256x256 grids.

**Results:**
- **64x64 & 128x128:** Robust signal confirmed without degradation. The adaptive congestion natively forced side-flank activation early without heuristic tuning (e.g., side flanks opened in iteration 210 vs a starved iteration 2090 in the 128x128 baseline).
- **256x256:** Computational Python evaluation intentionally halted due to exponential runtime (each single map requiring ~22,400 iterative $O(N^2)$ scalar passes in single-thread memory).
- **Conclusion:** Scale/performance and geometric stability beyond 128x128 remains open. **No claim of full scale invariance is made.**

**Branch Classification Definition:**
- ROBUST EXPLORATORY BRANCH
- DEFERRED
- NOT IN V1 CLAIMS
- NOT INVESTOR-FACING YET
