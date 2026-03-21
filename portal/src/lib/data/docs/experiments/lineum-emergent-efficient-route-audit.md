# Exploratory Audit: Emergent Route Efficiency (A→B)

> **WARNING:** This is an internal exploratory, non-core document subject to constant change and raw-data-first failure modes. It is **non-canonical, non-marketing material, and contains no official product claims**. This experiment explicitly must not be interpreted as reintroducing "shortest-path" or "A* replacement" claims back into the main Lineum product wording. The baseline comparison is strictly for objective metric calibration, not a competitive claim.

## 1. Test Methodology
### A vs B Target Definition
- **Point A (Source):** A static point where continuous mass is injected.
- **Point B (Goal/Sink):** The destination coordinate from which we attempt to extract the path backwards.
- **Travel Cost Meaning:** Defined by the terrain resistance $\kappa$. `Cost = 1.0 / kappa`. Solid walls ($\kappa=0.05$) have exorbitant cost (1000), open routes ($\kappa=1.0$) cost 1, swamps ($\kappa=0.2$) cost 5.

### Candidate Route Extraction Strategy
**Continuous Gradient Ascent** over the accumulated pressure/mass field ($\Phi$):
1. From Point B, inspect the $\Phi$ field in all 8 neighboring topological cells.
2. Select the neighbor with the highest scalar value.
3. Step to that neighbor and repeat until Point A is reached or trapped in a local minimum/plateau.

### Mode Variants Tested
- `diffusion mode`: Pure gradient-smoothed pseudo-thermal diffusion.
- `wave mode`: Normal Lineum wave mechanics (oscillation active).

## 2. Test Scenarios (64x64 micro-grids)
1. `straight_corridor`: Clean direct Line-of-sight.
2. `swamp_detour`: Short route penalized by swamp vs long route via concrete.
3. `gate_timing`: Short route with dynamic gate vs always-open detour.
4. `two_route`: Risk vs Reward. Short/narrow route vs Long/wide route.
5. `dead_end_trap`: Wide, cheap branch ending blindly.

## 3. Results Registry
### Experiment Raw Data Export
*Runs evaluated empirically via Python backend simulation, terminating path-trace strictly via 8-way neighbor gradient mapping.*

| Scenario | Mode | Success | Length | Total Cost | vs A* Cost | Failure Mode |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `straight_corridor` | Diffusion | Yes | 40 | 40.0 | 1.00x | None |
| `straight_corridor` | Wave | No | 8 | N/A | N/A | Local Min |
| `swamp_detour` | Diffusion | Yes | 41 | 202.0 | 5.05x | Entered Swamp |
| `swamp_detour` | Wave | No | 5 | N/A | N/A | Local Min |
| `gate_timing` | Diffusion | Yes | 75 | 75.0 | 1.87x | Suboptimal |
| `gate_timing` | Wave | No | 12 | N/A | N/A | Local Min |
| `two_route` | Diffusion | Yes | 42 | 42.0 | 1.05x | Suboptimal |
| `two_route` | Wave | No | 3 | N/A | N/A | Local Min |
| `dead_end_trap` | Diffusion | No | 45 | N/A | N/A | Stuck |
| `dead_end_trap` | Wave | No | 6 | N/A | N/A | Local Min |

### A. Diffusion Verdict
**Partly Works** *(but fundamentally fails on Cost Efficiency)*

### B. Wave Verdict
**Fails**

### C. Against Baselines
**Worse on cost**

### D. Main Reasons
- **Diffusion:** Pure propagation of pressure $\Phi$ favors the physically shortest ray of descending gradient regardless of deep terrain impermeability (it will run straight through a swamp/wall) if it represents the shortest Euclidean distance to the source topologically.
- **Wave:** The wave interferes and creates standing nodes and peaks of $\Psi$, so gradient ascent gets stuck in a 1px local minimum of the standing frequency almost immediately. Obtaining a continuous line is impossible.

### E. Scope Guard
This log demonstrates a massive theoretical barrier for direct filtration. The result explicitly means that for the main product claim, this behavior **remains exploratory only** and discussions regarding the replacement of any route-efficiency algorithm cannot be reopened even theoretically.

> **STATUS UPDATE:** Route-efficiency and any routing remains strictly exploratory only. It is not and will not be part of the main product claim. Given the failure of the mechanism to prove lower travel-cost (gradient trapping), **it is currently not a priority** to continue in this direction. The branch is mothballed for potential future theoretical research.

**Current Question:** Can we derive a continuous "direction desirability / avoidance" map from $\Phi$ that navigates swamps and dynamic gates organically, without drawing a discrete A* line?
**Current Hypothesis:** Lineum fails at drawing "shortest A to B arrays" but excels at creating a continuous "Decision Field" (gradient vector field) where every pixel inherently points out of danger.
**What was learned now:** Pure Gradient Ascent extraction demands a flawless 1px slope and catastrophically fails due to local minima traps. Route utilization must be volumetric and probabilistic.
**What remains unknown:** Can a dumb particle sliding down the $\nabla \Phi$ gradient organically bypass a swamp strictly by reacting to local forces?
**Next immediate step:** Branch currently paused; focus diverted to validating Topological Vulnerabilities first.

## 4. Pivot: Lineum-Native Decision Fields
**Current Question:** Can we derive a continuous "direction desirability / avoidance" map from $\Phi$ that navigates swamps and dynamic gates organically, without drawing a discrete A* line?
**Current Hypothesis:** Lineum fails at drawing "shortest A to B arrays" but excels at creating a continuous "Decision Field" (gradient vector field) where every pixel inherently points out of danger and dynamically shifts when obstacles change, preserving global traversal intent.
**What was learned now:** Pure Gradient Ascent extraction demands a flawless 1px slope and catastrophically fails due to local minima traps. Route utilization must be volumetric and probabilistic, not strictly linear.
**What remains unknown:** Can a dumb particle sliding down the $\nabla \Phi$ gradient organically bypass a swamp strictly by reacting to the local field forces, without explicit path generation?
**Next immediate step:** Map the vector field $\nabla \Phi$ as a "Corridor Preference Field" rather than a path array, assessing whether it organically funnels aggregate agent flows correctly under dynamic conditions.

### 4.1 Exploratory Directions
1. **Decision Field (Corridor Preference):** Return a vector field of local gradients. Product: Crowd/Fluid mass routing map. Risk: Agents get trapped in continuous eddies. Kill: Agent aggregates loop indefinitely.
2. **Avoidance / Escape Tendency:** Agents evaluate immediate static $\Psi$ pressure of hazards to alter their local trajectory without full graph recalculation. Product: Live aversion mechanics. Risk: Clashes with local pathfinding colliders. Kill: Evasion behavior is indistinguishable from standard boids.
3. **Dynamic Passage Desirability:** Absolute scalar heatmap indicating "Is this route open/safe right now?" that dynamically shades routes the instant a gate closes. Product: Live congestion analytics. Risk: Residual field memory makes it adapt too slowly. Kill: Map fails to update desirability before an agent crashes into the gate.
