# Lineum Candidate Applications Registry

> **WARNING:** This registry contains strictly **unproven, exploratory hypotheses**. These are non-canonical, not part of any current API product, and make no official marketing claims. They are scheduled for future validation and may be killed pending evidence.

## Active Priority Queue
1. **Flow Vulnerability API** (STATUS: VERIFIED PRODUCT Blueprint - `lineum-topological-vulnerability-audit.md`)
2. **Resonance Vulnerability** (STATUS: IN ACTIVE RESEARCH - `lineum-resonance-vulnerability-audit.md`)
3. **Candidate Applications** (STATUS: HYPOTHESIS ONLY - see below)

---

## Candidate A: Material Stress / Fracture Risk
**Type:** Exploratory Hypothesis
**Why it makes sense:** The PDE Laplacian ($\nabla^2 \Phi$) reliably identifies geometric chokepoints where fluid pressure drastically concentrates. Statistically, physical mechanical tension flowing through a solid 2D object behaves similarly to fluid pressure crowding into a bottleneck. 
**Expected Input:** 2D CAD component profile (resistance matrix) with specifically injected "source" pixels representing the exact physical mechanical load points instead of fluid spawns.
**Expected Output:** X/Y coordinates of the Laplacian minima, geometrically representing the "snapping point" where structural tension is highest.
**Industry Baseline:** Finite Element Analysis (FEA) testing software.
**Why it is promising:** It could offer a mathematically instant, mesh-free 2D stress estimator without compiling complex FEA physical vectors.
**Why it is NOT a priority now:** The architecture vulnerability API must be fully shipped first. Physics mechanical tension models require strict real-world materials testing to prove correlation, which is heavily out-of-scope for the current sprint.

## Candidate B: Games Industry Automated Level-Design QA
**Type:** Exploratory Hypothesis
**Why it makes sense:** Level designers spend hours manually playtesting or running thousands of bot simulations to find where a multi-player map "chokes" or feels unbalanced.
**Expected Input:** A 2D top-down slice of a game level or basic structural layout.
**Expected Output:** Ranked JSON nodes highlighting the worst structural bottlenecks before the game is even compiled.
**Realistic Claim:** "Lineum instantly extracts global structural load and flow significance from raw grids, acting as an analytical geometric oracle."
**Exaggerated Claim to Strictly Avoid:** "Lineum replaces NPC pathfinding or A* logic." Lineum calculates static topological load; it does NOT steer individual NPC agents in real-time.
**Why it is promising:** Immense time-saving value for level tuning and dynamic spawn-point generation in procedural games.
**Why it is NOT a priority now:** Game engines require native plugins (Unreal/Unity). The immediate priority is completing the backend API physics core (Resonance branch), before attempting to build third-party engine wrappers.
