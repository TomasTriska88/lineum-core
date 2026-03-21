# Evidence-First Mechanism Gap Audit

> **WARNING:** This is a strictly internal, non-marketing analytical registry. It breaks down the failure vectors of frozen/killed Lineum branches. The goal is to isolate whether a branch failed strictly due to fundamental Lineum physics, or simply because we used an overly naive, constrained readout/forcing setup that artificially masked the native math.

## A) Material Stress / Fracture Risk
**1. Current evaluated mechanism**
- **Native Core:** Pure Diffusion. Scalar $\Phi$ only. Driven by a single uniform injection source boundary (`+10`) and a uniform sink boundary (`*0.1`).
- **Application Layer:** Extracted standard Laplacian ($\nabla^2 \Phi$) local minima via percentile thresholding and NMS.

**2. Unused native mechanisms**
- Wave dynamics (`psi`), viscosity (`mu`), internal uniform dissipation, flux vector fields ($|\nabla \Phi|$).

**3. Failure classification**
- **FAILED UNDER CURRENT SETUP (Source-Edge Forcing Dominance).** The boundary injection of `+10` dwarfed passive constrictions. Root-cause classification beyond that remains limited, so we cannot claim a definitive native physical failure of the concept itself, merely a breakdown of this specific probe design.

**4. Salvage hypothesis**
- Instead of forcing flow from edge to edge (which breaks scalar reading), initialize the entire solid `kappa` shape with a perfectly uniform internal pressure (e.g., `phi = 1.0` everywhere uniformly), and let it dissipate passively outward. Measure the internal regions of highest dissipation curvature.

**5. Minimal experiment design**
- **Input:** 5 standard shapes (Dumbbell, Notch, etc.).
- **Native Setup:** Uniform `phi` filling. No continuous source injector. Sink is the entire void exterior. Let run for $X$ frames.
- **Readout:** Laplacian of the dissipating field.
- **Success Criterion:** Top-3 hotspots reliably hit expected weak masks without boundary artifacts.
- **Kill Criterion:** Highest pressure drop just snaps rigidly to the outermost hull universally.

**6. Priority recommendation**
- **REOPEN ONLY AS NARROW EXPLORATORY TEST**

---

## B) Games / Level-Design QA
**1. Current evaluated mechanism**
- **Native Core:** Pure Diffusion. Scalar $\Phi$ only. Strict Single-Source (Team A base) to Single-Sink (Team B base) mapping.
- **Application Layer:** Deepest negative Laplacian peak extraction via Percentile sorting and NMS. 

**2. Unused native mechanisms**
- Competing multi-sources (destructive geometric interference), spatial equilibrium / interface extraction, vector routing.

**3. Failure classification**
- **Failed under current forcing setup only.** The physics engine perfectly found the path of least resistance (the global minimum choke), but because fluid natively avoids high resistance, it naturally starved all secondary/tertiary flanking lanes, which are critical to multiplayer level design.

**4. Salvage hypothesis**
- Instead of a single source-sink draining the map, inject multiple competing sources natively (e.g., Team A pours Red fluid, Team B pours Blue fluid). Wait for the fields to clash and read the *Emergent Interface* (the equilibrium front line where opposing pressures neutralize). This organically reveals the global tactical front across ALL lanes simultaneously without starvation.

**5. Minimal experiment design**
- **Input:** The 5 Game topologies (MOBA, CS-Bomb, etc).
- **Native Setup:** Two competing `psi` sources expanding simultaneously.
- **Readout:** The geometric line/zone where the competing fields cancel/collide.
- **Kill Criterion:** Interface is unstable, entirely random, or identical to primitive Voronoi distance partitioning.

**6. Priority recommendation**
- **WORTH ONE MORE NATIVE-MECHANISM PASS** 

---

## C) Resonance Vulnerability
**1. Current evaluated mechanism**
- **Native Core:** Pure Wave Dynamics (`psi`).
- **Application Layer:** Temporal envelope averaging. Top-1 Absolute amplitude extraction (peaks).

**2. Unused native mechanisms**
- Diffusion dampening, phase-persistence tracking, vorticity / curl.

**3. Failure classification**
- **Failed under current readout only.** Wave interference naturally spawns chaotic antinodes. Reading raw absolute peak amplitudes traps the application layer in temporal noise.

**4. Salvage hypothesis**
- Do not read absolute scalar peaks. Read temporal phase-persistence (e.g., which specific isolated pockets bounded by high `kappa` maintain continuous localized oscillation states without radiating away).

**5. Minimal experiment design**
- Not proposed for v1. The engineering effort required to build a persistent phase-state tracker surpasses the immediate commercial payout.

**6. Priority recommendation**
- **FROZEN / NOT A PRIORITY**. The wave premise inherently works and temporal stability of isolated pockets is proven excellent, but raw standalone outputs suffer from too many interference-driven false positives. It is a weak branch, not a definitively dead one.

---

## D) Emergent Route / Decision Field
**1. Current evaluated mechanism**
- **Native Core:** Pure Diffusion pressure gradients.
- **Application Layer:** Gradient descent extraction to generate a singular geometric array (A-to-B line).

**2. Unused native mechanisms**
- Vector-field "desirability mapping" for swarm behavior.

**3. Failure classification**
- **Failed more fundamentally.** Using a globally integrated PDE field just to trace a single discrete moving path is phenomenally slow and uncompetitive against standard graph $A^*$ matrix math.

**4. Salvage hypothesis**
- None as a singular pathfinder. (Only viable as a generic concept-only "Influence Map" for flocking AI, but not for direct discrete routing).

**5. Minimal experiment design**
- Kill.

**6. Priority recommendation**
- **DO NOT REOPEN**

---

## E) Continuous Resistance / Permeability
**1. Current evaluated mechanism**
- **Native Core:** Pure Diffusion with grayscale `kappa` mapping.
- **Application Layer:** Pure Laplacian $\nabla^2 \Phi$ extraction (finding the sheerest drop in pressure).

**2. Unused native mechanisms**
- Flux Vector Fields $|\nabla \Phi|$ (measuring fluid volume velocity).

**3. Failure classification**
- **Failed under current readout only.** The Laplacian perfectly identifies where pressure drops most violently (inside high-friction swamps). However, the fluid actually avoids these swamps, so there is almost zero real fluid there. The Laplacian acts as a blind friction edge-detector, entirely ignoring how much traffic actually uses that pixel.

**4. Salvage hypothesis**
- Multiply the Laplacian by the local Flux Magnitude: $\text{Bottleneck} = |\nabla \Phi| \times |\nabla^2 \Phi|$. 
- This mathematically filters out high-friction swamps holding zero traffic (because local Flux = 0, so the product = 0), and exclusively isolates high-friction zones that are forced to carry massive global passing volume.

**5. Minimal experiment design**
- **Input:** The 5 continuous maps from DP-EXP-015 (Swamps vs Clear lanes).
- **Native Setup:** Single source-sink continuous diffusion.
- **Readout:** Extract the Flux-Weighted Laplacian array.
- **Success Criterion:** The topological node completely ignores the heavy swamp and successfully snaps back to the narrow, highly-trafficked clear highway.
- **Kill Criterion:** Mathematical instability or failure to separate edge-friction from volume-friction.

**6. Priority recommendation**
- **WORTH ONE MORE NATIVE-MECHANISM PASS**
