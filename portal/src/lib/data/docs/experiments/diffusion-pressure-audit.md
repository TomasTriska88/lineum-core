# Diffusion Pressure API Solutions - Master Working Audit Log

> **NOTE/WARNING:** This document is strictly an internal exploratory working audit log, not a presentation whitepaper. It is **non-canonical, non-marketing material, and contains no official core product claims**. It is subject to continuous change and raw-data-first failure modes. The conclusions drawn here are explicitly local and limited only to the *API Solutions PoC* showcase. Nothing from this document may be automatically extrapolated to wide Lineum / Wave Core claims without further evidence.

## 1. Scope
- **API Solutions Only:** This audit covers exclusively the behavior of backend functions for the spatial API (`spatial_api.py`) and the Svelte frontend showcase.
- **Diffusion Pressure PoC Only:** Branches such as Broca, Reservoir Computing, linear regression, or cosmological theoretical models of Lineum are completely out of scope.
- **Prototype-visible Validation:** The analysis is restricted to data that directly impacts the UI rendering and the heatmap visualized in the prototype.

## 2. Current Status
- **What the PoC can do today:** It can accept a topological map, run a matrix linear solver via an API endpoint, return an iteratively diffused continuous field, and extract the top lowest Laplacian bodies.
- **What it cannot do today:** It cannot iterate to a safe, stationary fixed point without arbitrary cutoffs. 
- **Active solver:** `execute_diffusion` (forcing `physics_mode_psi="diffusion"` and neglecting any stationary wave regime).
- **Active heuristic:** `rank_bottlenecks` (utilizes minimum panning where $\nabla^2 \Phi$).

## 3. Metrics Definitions
- **drift_px:** The full Euclidean distance $\sqrt{\Delta x^2 + \Delta y^2}$ separating the original position of the primary bottleneck and its new measured location after a perturbation.
- **rank_inversion:** Binary detection. Triggers `Yes` when the primary candidate shifts beyond tolerance AND the old preferred primary location drops in rank in favor of a completely new geographical area.
- **RPI:** Relative Pressure Index. An obscure UI gauge currently being phased out due to iteration dependency.

## 4. Experiment Registry

| Experiment ID | Date | Purpose | Scenarios | Parameter sweep | Run count | Verdict |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `DP-EXP-001` | 2026-03-21 | Pack-A Fixed Cutoff Sensitivity | 4 standard maps | `iters`/`-0.1 cutoff`| 20 | **FRAGILE** |
| `DP-EXP-002` | 2026-03-21 | Percentile Normalization Baseline | 4 standard maps | `iters`/`5% percentile`| 16 | **IMPROVED** |

## 5. Sub-Branch: Topological Vulnerability Prior (Continuous Bottlenecks)
> **WARNING:** Exploratory, non-core, raw-data-first. Not part of main product claim.
**Hypothesis:** The structural regions taking the absolute highest fluid pressure integrals over time represent the objectively most critical "topological vulnerabilities" of the spatial graph, natively isolating choke-points based on the massive volume of fluid attempting to traverse them.
**Baseline:** Betweenness Centrality Node Maps.
**Percentile Baseline Verification (DP-EXP-002):** Evaluates rank stability using a 5th-percentile cutoff metric rather than the failed absolute `-0.1` limits.
- Preserved Primary Bottlenecks: 0/8 (Old) -> **8/8** (New)
- Rank Inversion: 8/8 (Old) -> **0/8** (New)
- Mean Drift: 62.15 px -> **1.63 px** (Firmly anchored)
**Verdict:** The percentile normalization explicitly pins the vulnerable geometric sectors statically in spatial reality. The branch is alive and moves to next prototyping steps.

## 6. Sub-Branch: Organic Heatmap Distribution 
> **WARNING:** Exploratory, non-core, raw-data-first. Not part of main product claim.
**Hypothesis:** Deriving continuous risk/cost maps (zombie scent, radiation) from Lineum's diffusion yields structurally superior "shadows" around walls than standard radial blurs.
**Baseline:** Multi-Source Grid Flood-Fill + 2D Gaussian Blur.
**Kill Criterion:** If the resulting stationary field geometry offers less than a 5% structural variation from the Gaussian Blur baseline, the branch will be killed due to redundancy.
*(Awaiting baseline map delta generation)*

## 7. Lineum-Native Behavior Audit
**Current Question:** How do we extract product-value from the Lineum $\Phi$ matrix natively, strictly avoiding any forcing of the engine to mimic classical discrete algorithms?
**Current Hypothesis:** While absolute $\Phi$ amplitudes diverge wildly, the relative structural geometric relations (e.g. topological valleys of the 2D Laplacian $\nabla^2 \Phi$) and continuous asymmetric distributions remain mathematically bound to the permanent static topology of the map, regardless of the iteration scope.
**What was learned now:** Imposing hardcoded boundaries (e.g., `< -0.1` cutoff) strips away the topological truth of the field. Only structural relativity (e.g., 5th Percentile) correctly locks onto the continuous native features of the flow.
**What remains unknown:** How these extracted arteries will behave dynamically when wall $\kappa$ values alter mid-run (e.g. dynamic doors closing).
**Next immediate step:** Finalize the percentile extractor cleanly into the `spatial_api.py` core to purge the obsolete hardcoded `-0.1` limit, preparing the endpoint for robust UI presentation.

### 7.1 Native-Feature Diagnostic Tests
1. **Relative Topological Vulnerability:** Extract the deepest X% of the Laplacian to pin down map arteries unconditionally. Why it's native: Lineum implicitly integrates the mass of all fluid attempting to enter the funnel. 
   - **Verdict:** *(2026-03-21)* PROVEN. Tested on `complex_arch_1`. The 5% threshold perfectly nailed 4/4 explicit geometric baseline pinches with an overlap error of $\le 1.0px$. Validating branch for full implementation.
2. **Natural Influence Distribution:** Simulate hazard leaks to observe how continuous fields organically wrap around corners asymmetrically. Why it's native: Fluid mechanics diffuses non-linearly over barriers, breaking radial symmetric bounds. Raw Data: SSIM matrix delta vs standard Gaussian Blur. Kill Criterion: Differences are negligible (< 5%), rendering it a heavy redundant blur filter.
3. **Stable Pressure Interface:** Inject two competing sources to study the shape of the emergent frontier (equilibrium line). Why it's native: Lineum handles destructive interference between competing fields organically without complex collision grids. Raw Data: Interface coordinate array stability over time. Kill Criterion: The frontier oscillates violently or never grounds statistically into a line.

## 8. Changelog
- **2026-03-21:** Obnovení izolovaných dokumentů `lineum-topological-vulnerability-audit.md` a `lineum-organic-heatmap-audit.md` dle revokovaného příkazu pro separaci datového prostoru sub-hypotéz.
- **2026-03-21:** Spuštěna plná architektonická simulace ve větvi Topological Vulnerability Analyst (DP-EXP-003) oproti geometrickému Ground-Truth pro verifikaci 5th-percentilového rankování.
- **2026-03-21:** Consolidated the isolated Sub-Branch experiment logs (Heatmap and Topological Vulnerability) directly into this Master Log to prevent documentation bloat. Translated all records strictly to English.
- **2026-03-21:** Executed `DP-EXP-002` (Percentile Normalization Experiment). Revealed massive improvement in metric stability (Drift reduced from 62px to < 2px).
- **2026-03-21:** Relocation: Document moved to `docs/experiments/` folder.
- **2026-03-21:** Official Workflow Pivot: Transition from "UI-Showcase" to a strict "Knowledge-First" model. 
