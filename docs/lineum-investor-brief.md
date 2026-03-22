# Lineum: The Spatial Load Oracle

**Lineum is a physics-native spatial analysis API that cleanly extracts the structural capacity and bottlenecks of any 2D layout instantly—without requiring complex NPC pathfinding, ray-casting, or agent simulations.**

## 1. The Core Value Proposition
Every day, architects, retail planners, and facility managers design physical spaces and pray they don't bottleneck. They rely on intuition or massive, overnight crowd-simulations to find out if a design works. 

**Lineum changes this completely.**
- **Input:** Send us a raw, standard 2D image of a floorplan (Black = Walls, White = Open Space).
- **Output:** In under 1.5 seconds, we return the mathematical "crush-points"—the exact doors, hallways, and junctions that will bottleneck under human traffic.
- **The Mechanism:** We do this by treating the entire architecture as a continuous fluid dynamic field. We don't simulate a thousand tiny digital humans. We calculate the absolute geometry of the space itself.

## 2. Why We Challenge the Status Quo
Traditional spatial analysis requires **NavMeshes** or **AI Pathfinding (A* graphs)**. These are incredibly expensive to set up and slow to compute dynamically. Alternatively, classic Distance-Transforms find "narrow spaces," but they are fundamentally blind—they will highlight a narrow janitor's closet even if absolutely no one needs to walk through it.

**Lineum is fundamentally different.**
Using thermodynamic and fluid principles (Diffusion-Flow), Lineum naturally "feels" the global weight of the building. It autonomously identifies which narrow hallway will bear 90% of a stadium's evacuation traffic because it forms the singular geometric artery. **It provides the analytical intelligence of global crowd-simulation without the exponential computational cost.**

## 3. Product Features & The Unassailable Baseline
We are going to market with an iron-clad, brutally benchmarked analytical core.

- **Flow Vulnerability API (The Flagship):** 🟢 **PROVEN & TESTED.** Instantly extracts the single most dangerous architectural crush-point in the layout. Crucially, Lineum operates exclusively as a static architectural load oracle natively constrained to **Binary Layouts** (Solid Walls vs Open Space). 
- **The Organic Heatmap:** 🔵 **FREE BYPRODUCT.** The PDE pressure engine inherently generates fluid-like gradient heatmaps of structural flow. Because this visual layer is computed in the background during step 1, we acquire a frontend visualization layer entirely for free.
- **Topological Noise Resistance:** Lineum is immune to trivial geometric noise. Scattered chairs, pillars, and desk islands do not shatter the map into false micro-corridors. The physics seamlessly wrap around them.
- **The Disruption Moat:** We outperform basic Distance-Transforms (which blindly flag irrelevant closets as bottlenecks simply because they are narrow) by natively understanding **global architectural context**. We also bypass the exponential computational cost of NavMesh Betweenness Centrality by operating directly on the discrete pixel matrix.
- **Multi-Threshold Confidence Scoring:** The API does not return flat guesses. It applies rigorous statistical threshold sweeps to mathematically grade every chokepoint. Enterprise clients receive a normalized Confidence Score (e.g., 0.96 vs 0.16), allowing them to definitively filter out structural noise.
- **Dynamic Flow Reallocation:** If a floorplan layout is altered (e.g., a hallway is blocked), the fluid physics intrinsically reroute the new systemic pressure mapping instantly, without ever regenerating a pathfinding routing tree.

*> Transparent Limit:* The Core API does not steer real-time NPCs, it does not evaluate continuous grayscale friction zones, and it does not do audio acoustic bouncing. These are separate sciences. Lineum does exactly one thing: **It delivers fast, macro-scale flow analytics.**

## 4. The R&D Horizon
We maintain a strict boundary between our commercially ready Core API and our advanced laboratory research.
- **Dynamic Swarm Simulation (Adaptive Congestion):** 🟡 **PROMISING EXPLORATORY SIGNAL.** Internally we've verified that Lineum can natively simulate global traffic congestion, organically forcing fluid to overflow into alternative multi-lane flank routes without any graph heuristics (tested to 128x128 resolution). Confirmed as a robust exploratory branch, but held for future developments and entirely walled off from baseline product claims.
- **Continuous Resistance (Grayscale):** ❄️ **FROZEN.** 
- **Games Industry QA Level-Design:** ❄️ **FAILED / FROZEN.** (Original Hypothesis replaced entirely by early-stage pure Dynamic Congestion research).
- **Acoustic Resonance / Material Stress:** ❄️ **FROZEN.** (Capability explored, but entirely isolated from current SaaS commercial focus).
- **A* Route Replacement:** ❄️ **FROZEN.**

## 5. Long-Term Compute Hardware Vision
*Note: This is explicitly NOT the current product. It is NOT a physically verified prototype, and it is NOT an investor promise for near-term delivery. It is a long-horizon architecture hypothesis derived purely from internal Lineum research into continuous-wave scaling.*

While Lineum is currently implemented and benchmarked as a software API, the underlying mathematical core (`Eq-7 Wave Engine`) structurally emulates **Continuous-Wave Diffractive Optical Computing**. Internal R&D has systematically mapped how Lineum’s grid behaves mathematically, extracting robust software primitives like RAM Vaults, structural memory paths, and reusable erasure mechanisms within the mathematical sandbox.

**The Photonic Architecture Hypothesis:**
The long-horizon hypothesis scales Lineum physically into a solid-state optical substrate (such as a Phase-Change photorefractive medium). Instead of rendering architecture on a software processor, a Spatial Light Modulator (SLM) physically programs the topology onto the medium, and an edge-injected laser computes through native optical propagation inside the substrate.

The current Lineum software explicitly does **not** prove that a Turing-complete optical computer is finished today. Rather, the Eq-7 software serves as the vital digital emulator to design and test the topological bounds required for this class of spatial-compute architecture, positioning Lineum as a foundational design framework for the future of in-materio optical processing.

---
# Internal Appendix: Pitch Governance & Due Diligence
*This section governs internal pitch boundaries to ensure strict evidence-first consistency during investor conversations.*

## Risk Register (Disclosure Limits)
- **Scale Decay Error:** While the baseline flow vulnerability handles our target resolutions easily and efficiently, extremely massive discrete grid scaling (e.g. 4096x4096 without downscaling) may theoretically smear unrecognizably if scaling normalization limits are hit.
- **Visual vs Analytical Discord:** The Organic heatmap looks so good that users might naturally conflate the beautiful visuals with the actual hard analytical chokepoint extraction. We must clarify the Heatmap is just Step 1 visualization of the underlying flow field.

## Claims Matrix Checklist
| Claim Text | Status | Supporting Audit | Investor-Safe Wording | Forbidden Wording |
|---|---|---|---|---|
| Instantly extracts bottlenecks from static binary shapes | 🟢 PROVEN | `topological-vulnerability` | "Lineum delivers fast macro-scale flow analytics." | "Real-time pedestrian simulation." |
| Generates physically bounded fluid heatmaps without cost | 🟢 PROVEN | `organic-heatmap` | "Outputs premium structural gradient layer." | "Calculates perfect global fluid mass tracking." |
| Organic Dynamic Swarm Traffic Capacity Routing natively | 🟡 EXPLORATORY | `games-qa-audit` | "Lab R&D indicates swarm flow potential." | "The API handles live multidirectional crowd evasion natively." |
| Acoustic Resonance detects ambush corners automatically | ❄️ FROZEN | `resonance-vulnerability` | N/A | "Lineum accelerates acoustics for games." |
| Material Stress isolates points of structural fracture | ❄️ FROZEN | `material-stress` | N/A | "Lineum evaluates metal tension physically." |

