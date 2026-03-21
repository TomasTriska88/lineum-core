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

## 5. Next Step: The Interactive Web Demo
We do not make investors read whitepapers. The sole, immediate next step is deploying the **Lineum Live Interactive Prototype**. 

Partner executives will open a web canvas, sketch a corridor with their mouse, and watch as Lineum renders the Organic Heatmap. If they draw a brick wall across the main artery, the Lineum API will recalculate the global pressure topology and pinpoint the newly emergent secondary bottlenecks. **This sandbox demonstrates the baseline analytical capability.**

## 6. Long-Term Compute Hardware Vision: Optical / In-Materio Substrate
*Note: This is NOT the current v1 product. This is not a physically built or experimentally verified hardware prototype. This section outlines a long-horizon hardware design hypothesis derived from internal Lineum research into non-Boolean continuous-wave scaling. The present product remains entirely the SaaS Flow Vulnerability API.*

While Lineum is currently deployed as an enterprise software API, the underlying mathematical core (`Eq-7 Wave Engine`) is not a traditional digital algorithm. It is a mathematically exact emulator for **Continuous-Wave Diffractive Optical Computing**. Internal R&D has exhaustively mapped how Lineum’s 2维 grid behaves mathematically. We have mapped that our topology can form RAM Vaults, engrave permanent structural memory paths, and execute reusable erase cycles within the math. Because Lineum computes logic by allowing continuous waves to diffract off topographies rather than using discrete Boolean silicon transistors, the engine naturally aligns with future **Compute-in-Memory (In-Materio)** paradigms.

**The Photonic Architecture Hypothesis:**
The long-term vision scales Lineum out of the software GPU and into a physical, solid-state optical substrate (such as a Phase-Change photodetractive medium). Instead of rendering architecture on a processor, a Spatial Light Modulator (SLM) projects the building's walls as physical light-barriers onto the medium. An edge-injected laser then passes through this layer. Because light natively computes wave-interference and spatial congestion at $300,000$ km/s across massive macroscopic node clusters, the physical glass itself could theoretically solve the entire multi-lane flow congestion matrix instantly, in parallel, with near-zero energy consumption. 

The current Lineum software serves as the vital digital sandbox to design, test, and benchmark the wall topologies, memory paths, and routing fields required for this class of spatial-compute hardware. This positions Lineum not just as a simulation tool, but as a foundational design research framework for the next century of in-materio optical processing architectures.

---
# Internal Appendix: Pitch Governance & Due Diligence
*This section governs internal pitch boundaries to ensure strict evidence-first consistency during investor conversations.*

## Risk Register (Disclosure Limits)
- **Scale Decay Error:** While the baseline flow vulnerability handles our target resolutions easily and efficiently, extremely massive discrete grid scaling (e.g. 4096x4096 without downscaling) may theoretically smear unrecognizably if scaling normalization limits are hit.
- **Visual vs Analytical Discord:** The Organic heatmap looks so good that users might naturally conflate the beautiful visuals with the actual hard analytical chokepoint extraction. We must clarify the Heatmap is just Step 1 visualization of the underlying flow field.

## Claims Matrix Checklist
| Claim Text | Status | Supporting Audit | Investor-Safe Wording | Forbidden Wording |
|---|---|---|---|---|
| Instantly extracts bottlenecks from static binary shapes | 🟢 PROVEN | `topological-vulnerability` | "Lineum delivers fast macro-scale flow analytics." | "Lineum guarantees flawless real-time pedestrian simulation." |
| Generates physically bounded fluid heatmaps without cost | 🟢 PROVEN | `organic-heatmap` | "Outputs premium structural gradient layer." | "Calculates perfect global fluid mass tracking." |
| Organic Dynamic Swarm Traffic Capacity Routing natively | 🟡 EXPLORATORY | `games-qa-audit` | "Lab R&D indicates swarm flow potential." | "The API handles live multidirectional crowd evasion natively." |
| Acoustic Resonance detects ambush corners automatically | ❄️ FROZEN | `resonance-vulnerability` | N/A | "Lineum accelerates acoustics for games." |
| Material Stress isolates points of structural fracture | ❄️ FROZEN | `material-stress` | N/A | "Lineum evaluates metal tension physically." |

