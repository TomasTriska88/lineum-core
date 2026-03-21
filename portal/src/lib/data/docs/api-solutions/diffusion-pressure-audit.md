# Diffusion Pressure API Solutions - Working Audit Log

> **NOTE:** This document is strictly an internal working audit log, not a presentation whitepaper. The conclusions drawn here are explicitly local and limited only to the *API Solutions PoC* showcase. Nothing from this document may be automatically extrapolated to wide Lineum / Wave Core claims without further evidence.

## 1. Scope
- **API Solutions Only:** This audit covers exclusively the behavior of backend functions for the spatial API (`spatial_api.py`) and the Svelte frontend showcase.
- **Diffusion Pressure PoC Only:** Branches such as Broca, Reservoir Computing, linear regression, or cosmological theoretical models of Lineum are completely out of scope.
- **Prototype-visible Validation:** The analysis is restricted to data that directly impacts the UI rendering and the heatmap visualized in the prototype.

## 2. Current Status
- **What the PoC can do today:** It can accept a topological map, run a matrix linear solver via an API endpoint, return an iteratively diffused continuous field, and extract the top lowest Laplacian bodies.
- **What it cannot do today:** It cannot iterate to a safe, stationary fixed point. It cannot dynamically adapt to large fields, complex structures, or generalize to unknown data (lack of external baseline validation).
- **Active solver:** `execute_diffusion` (which uses `step_core` internally, forcing `physics_mode_psi="diffusion"` and neglecting any stationary wave regime).
- **Active heuristic:** `rank_bottlenecks` (utilizes static limiters and local minimum panning where $\nabla^2 \Phi < -0.1$).

## 3. Metrics Definitions
- **Reference Setting:** The baseline standard against which perturbations are compared. Fixed at `iterations = 1500`, `cutoff = -0.1`.
- **drift_px:** The full Euclidean distance $\sqrt{\Delta x^2 + \Delta y^2}$ separating the original position of the primary bottleneck and its new measured location.
- **primary_preserved:** Binary `Yes`/`No`. Marks `No` if the primary candidate shifts beyond a hard pixel offset tolerance limit.
- **rank_inversion:** Binary detection. Triggers `Yes` when `primary_preserved == No` AND the old preferred primary location hasn't physically disappeared, but the heuristic lowered its rating in favor of a completely new geographical area. This indicates a priority inversion.
- **RPI:** Relative Pressure Index. An obscure UI gauge currently calculated as a capped $0-100\%$ fraction of the maximal field value.
- **Current Hardcoded Constants:** Baseline `iters=1500`, heuristic Laplacian threshold `lap_cutoff=-0.1`, and a fixed max-denominator for field normalization `max_phi_denominator=2000000.0`.

## 4. Experiment Registry

| Experiment ID | Date | Purpose | Scenarios | Parameter sweep | Run count | Result | Verdict |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `DP-EXP-001` | 2026-03-21 | Pack-A Sensitivity Audit | `narrow_tunnel`, `wide_corridor`, `branching`, `pegs` | `iters`/`cutoff`| 20 | Mean drift 62.15 px | **FRAGILE** |

## 5. Findings
- **Proven Evidence:** The physical rendering API runs technically well on limited sets of micro-maps. The JSON payload delivers the float32 maps reliably without server collapse in the demo.
- **Hypothesis Only:** The claim that UI bottleneck rings currently correlate with real continuous choke-points is hypothetical and unsupported by generalist testing.
- **Failures:** Severe positional shift of ranked candidates. The engine significantly fails to anchor and topologically fixate the sought anomalies under trivial changes to the solver iteration count.
- **Open Problems:** Missing stop-condition metric $\Delta \Phi$; absence of scaling topographic convergence for the Laplacian filter.

## 6. Open Problems
- **Solver divergence / no stationary stopping condition:** The engine exhibits a mathematically unbounded $\Phi$ field that ignores natural steady-states and accumulates errors.
- **Fixed absolute cutoff in `rank_bottlenecks`:** Hardcoded threshold limits for the minimum filter behave illogically and asymmetrically against the ever-growing quantity of fluid mass/flux.
- **RPI hardcoded scaling issue:** Dividing the metric `max_phi` by a fictitious number is an unsustainable state that ignores any physical grounding.
- **Dependence on iteration count:** Both the proxy solver and the heuristic currently stand and fall based strictly on a fixed iteration count taken from the demo presets.

## 7. Next Immediate Step
**Action:** Implement a convergence safeguard (**PACK-B**), shifting to an iteration limit that stops at $t \to \infty$ via a stationary derivative asymptote, rather than a blind stop at 1500 steps.

## 8. Changelog
- **2026-03-21:** Vyjasnění hierarchie: Tento dokument slouží jako **Master Experiment Log** pro celou API Solutions větev Diffusion Pressure. Sdružuje zastřešující zjištění o solveru, zatímco izolované hypotézy (Route Efficiency, Heatmaps) dostávají dedikované sub-soubory ve složce `docs/experiments/`.
- **2026-03-21:** Oficiální Workflow Pivot: Přechod z "UI-Showcase" na striktní "Knowledge-First" model. Veškerý vývoj API je plně podřízen pracovním auditním repozitářovým dokumentům. Nalezení izolovaných a konkurenceschopných asymetrických use-cases má přednost před feature-driven zobrazením.
- **2026-03-21:** Dokončena exekuce A→B testu s tvrdým fail/partly-works verdiktem (Lineum čistou gradient ascent metodou nerespektuje travel-cost resistance terénu). Završeno založení zástupných API use case kandidátů se zaměřením off-path.
- **2026-03-21:** Založen izolovaný experiment `docs/experiments/lineum-emergent-efficient-route-audit.md` k otestování nejzákladnější hypotézy o možném vytažení A→B efektivní trasy (Travel Cost / Route Efficiency) skrze topografický spád $\Phi$ metodou gradient ascent.
- **2026-03-21:** Document established. First audit log DP-EXP-001 inserted.

---
### Audit Records: DP-EXP-001 
- **Total runs:** 20
- **Scenarios:** `narrow_tunnel`, `wide_corridor`, `branching`, `pegs`
- **Reference setting:** `iterations=1500`, `cutoff=-0.1`
- **Iteration perturbation runs:** 8
- **Preserved under iteration perturbation:** 0/8
- **Rank inversion under iteration perturbation:** 8/8
- **Mean drift under iteration perturbation:** 62.15 px
- **Median drift:** 57.72 px
- **Max drift:** 128.32 px
- **Cutoff perturbation runs:** 8
- **Stable cutoff runs:** 7/8
- **No-detection case under cutoff:** 1/8 
- **Preliminary verdict:** FRAGILE
