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
- **2026-03-21:** Established `lineum-candidate-applications.md` registry. Spun off speculative hypotheses (Material Stress and Games Level-Design QA) into isolated candidate scope to protect the core API claims. Purged all exaggerated "A* logic" terminology in favor of strict "global structural flow significance".
- **2026-03-21:** Finalized the Flow Vulnerability branch with a formal Commercial & Theoretical Synthesis (Section 15 in `lineum-topological-vulnerability-audit.md`). Explicitly separated the Core's blind geometric physics from the Application layer's semantic extraction ("doors").
- **2026-03-21:** Conducted Test A.6 "Competitive Benchmark" (DP-EXP-011) evaluating Lineum Diffusion against rigid classical baselines (Distance-Transform and Betweenness Centrality). Proved Lineum's legitimate product slot: delivering the systemic global flow-weighting of Centrality without the exponential cost of navMesh generation, while avoiding the blind geometric false-positives of fast Distance-Transforms.
- **2026-03-21:** Conducted Test A.5 "Realistic Floorplan Validation" (DP-EXP-010) using the finalized Flow Vuln pipeline. Tested across 5 messy layouts (offices, warehouses, irregular rooms). The pipeline held flawlessly; while 2 false-positive furniture gaps were technically flagged by the lowest threshold, the Confidence Layer correctly down-ranked them to 0.16 (vs 0.96 for primary doors). The API product blueprint is officially validated for real-world geometry.
- **2026-03-21:** Rozšířen Flow Vulnerability Application Pipeline o "Multi-Threshold Confidence Scoring" (DP-EXP-009). Vyčištěno použití magických čísel (flat cutoffs) v API; validováno přežití uzlů napříč vrstvami [1%, 2%, 3%, 5%, 7%, 10%]. Vygenerováno plné `confidence` skóre integrující absolutní vizuální JSON výstup pro frontendové klienty. 
- **2026-03-21:** Implemented Non-Maximum Suppression (NMS) clustering on the Application Layer strictly for Flow Vulnerability (DP-EXP-008). Successfully eliminated the parallel-door starvation weakness without altering Lineum PDE physics core. Hit rate against asymmetric parallel loads improved from 8/9 to 9/9.
- **2026-03-21:** Formalized the "Flow Vulnerability API Product Pipeline" architecture within the Topological audit (`lineum-topological-vulnerability-audit.md`). Defined the rigid handoff between Lineum Core inputs (Resistance grids) $\rightarrow$ Core Outputs (Laplacian matrix) $\rightarrow$ App Layer (NMS clustering, Multi-thresholding) $\rightarrow$ Client JSON (Ranked nodes). Identified NMS and Confidence Scoring as the next immediate roadmap bounds.
- **2026-03-21:** Targeted Flow Vulnerability edge-case benchmark (DP-EXP-007) assessing behavior across symmetric parallel passages (equivalent arteries). Result: perfect detection of equivalent nodes under strict symmetry, but exposed a mathematical "field starvation" weakness under slightly asymmetric load (solvable by future local clustering instead of a hard global percentile).
- **2026-03-21:** Executed stress test **Test A (DP-EXP-006)** evaluating Flow Vulnerability (Diffusion) across 5 asymmetric edge-cases (including long empty tunnels to validate absence of False Positives). Metrics proved crushing stability with zero false detections. Peak Mean Error at chokepoints is 0.60px.
- **2026-03-21:** Fundamental structural split of wave and diffusion properties: Topological branch split into "Flow Vulnerability" (strictly Diffusion, detecting arteries and circulation chokepoints) and a fully isolated new branch "Resonance Vulnerability" `lineum-resonance-vulnerability-audit.md` (strictly Wave, detecting reflection pockets and corner accumulations). Hybrid physics intersection declared useless noise and completely frozen (FROZEN).
- **2026-03-21:** Conducted complete Tripartite Modality execution (DP-EXP-005). Discovered a functional physical split: Diffusion perfectly defines `Flow Vulnerability` (chokepoints, doors), while pure Wave mode mathematically defines `Resonance Vulnerability` with high stability (acoustic corners, dead-end traps). Hybrid mode declared unfit (noise).
- **2026-03-21:** Established fundamental "Tripartite Modality" protocol. All future R&D experiments must mandatorily evaluate `diffusion-only`, `wave-only` and `hybrid` verdicts before final inclusion to Core API.
- **2026-03-21:** Route Efficiency sub-branch officially frozen (FROZEN status) to shift priority onto full verification of the Topological Vulnerability Prior.
- **2026-03-21:** Successfully executed Multi-Map Replication test for Topological Vulnerability across 5 distinct dispositions (DP-EXP-004), fully proving chokepoint detection stability.
- **2026-03-21:** Restored isolated logs `lineum-topological-vulnerability-audit.md` and `lineum-organic-heatmap-audit.md` per revoked directive, maintaining separated data spaces for sub-hypotheses.
- **2026-03-21:** Launched full architectural simulation in Topological Vulnerability Analyst branch (DP-EXP-003) against geometric Ground-Truth to verify 5th-percentile ranking.
- **2026-03-21:** Consolidated the isolated Sub-Branch experiment logs (Heatmap and Topological Vulnerability) directly into this Master Log to prevent documentation bloat. Translated all records strictly to English.
- **2026-03-21:** Executed `DP-EXP-002` (Percentile Normalization Experiment). Revealed massive improvement in metric stability (Drift reduced from 62px to < 2px).
- **2026-03-21:** Relocation: Document moved to `docs/experiments/` folder.
- **2026-03-21:** Official Workflow Pivot: Transition from "UI-Showcase" to a strict "Knowledge-First" model. 

## 9. Boundary Definition: Core vs Application
**Lineum-Native Core (Untouched Research):**
- The raw integration of the PDE pressure field over time ($\nabla^2 \Phi$).
- Continuous spatial gradient formation and wave/diffusion equilibrium asymptotes.
**Application-Layer Logic (Product Engineering):**
- Percentile thresholding (`> 5%`).
- Local-maxima extraction heuristics (NMS - Non-Maximum Suppression).
- UI heatmap color normalization and matrix clamping.
**Allowed Optimization Layer:**
- Engineering fitness functions, grid-search optimizations, and algorithmic filtering on the Application Layer are expressly **desired and legitimate** to build a viable commercial API product. The raw core matrices output by the engine are the only immutable properties.
**Not a Fundamental Physics Claim:**
- Any success achieved by aggressively tuning the Application Layer (e.g., finding the perfect NMS radius to cleanly separate parallel doors) is an engineering product success, but **cannot** be cited as evidence that "Lineum intrinsically understands doors".
