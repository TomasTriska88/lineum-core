# Exploratory Audit: Material Stress / Fracture Risk Hypothesis

> **WARNING:** Exploratory, non-canonical, non-marketing raw internal branch log.
> This is NOT an FEA (Finite Element Analysis) replacement claim.
> This is NOT a canonical materials science physics claim.
> This is strictly an exploratory hypothesis to verify if the 2D Diffusion + Laplacian core can reliably highlight intuitive, geometry-based weak points in solid shapes.

## 1. Scope & Objective
**Objective:** Evaluate if the scalar diffusion mathematical gradient ($\nabla^2 \Phi$) acts as a reliable geometry-only stress-like hotspot proxy when conducting synthetic diffusion-driven geometric probing on 2D silhouettes. 
**Focus:** Structural weak-zone highlighting under simplified probe conditions, extracted as a byproduct of the validated binary-layout flow vulnerability core.

## 2. Non-Goals / Exclusions
- Not predicting true physical fracture thresholds, tensile strength, or material properties (e.g., Young's Modulus).
- Not claiming to model real mechanical load forces or replace rigorous industry FEA simulation software.
- Not a core SaaS focus for Pipeline v1. This remains a strictly distinct exploratory direction.

## 3. Boundary Definition: Core vs Application
### A) Lineum-Native Core
- **Diffusion Core:** Bounded PDE injection inside the 2D shape boundaries acting as a synthetic geometric probe.
- **Laplacian-Based Reading:** Raw continuous extraction of steepest spatial gradients ($\nabla^2 \Phi$).

### B) Application Layer
- **Thresholding:** Percentile or absolute clipping limits for the hotspot map.
- **Ranking:** Sorting negative Laplacian peaks by severity to find the "weakest topological point".
- **Clustering / NMS (Non-Maximum Suppression):** Filtering out adjacent coordinate noise along the same fracture line to yield one clean coordinate per zone.

## 4. Benchmark Shapes & Setup Specification
**Global Setup:**
- **Resolution:** Tested simultaneously at 64x64 and 128x128 bounding boxes.
- **Binary Mask Convention:** `kappa = 0.05` represents the solid material body (conductive geometric medium). `kappa = 1.0` represents the empty void / outside air (absolute resistance).
- **Execution:** 100% deterministic (seed=42).

**Shape 1: Hourglass / Dumbbell**
- **Orientation:** Vertical. Wide top and bottom blocks connected by a central neck.
- **Probing Setup:** Source line injected uniformly at the top interior margin. Sink line extracted uniformly at the bottom margin.
- **Expected Weak-Zone Mask:** The designated constricted neck region `y \in [26, 38], x \in [26, 38]`.

**Shape 2: Notched Bar**
- **Orientation:** Vertical rectangular bar with sharp V-notches cut into its left and right flanks at the exact midpoint `y=32`.
- **Probing Setup:** Source top, Sink bottom.
- **Expected Weak-Zone Mask:** The structural interior immediate tips of the notches `y \in [30, 34], x \in [26, 31]` and `x \in [33, 38]`.

**Shape 3: Plate with Circular Hole**
- **Orientation:** Vertical continuous plate featuring a perfectly circular void punched through the center `(32, 32)`.
- **Probing Setup:** Source top, Sink bottom.
- **Expected Weak-Zone Mask:** The narrow remaining material bands located horizontally parallel to the void's equator: `y \in [28, 36]`, flanking the hole radius.

**Shape 4: Key Neck / Narrow Shaft**
- **Orientation:** Vertical. An abrupt 90-degree step-down where a massive upper block suddenly drops into a narrow vertical shaft.
- **Probing Setup:** Source top block, Sink bottom shaft.
- **Expected Weak-Zone Mask:** The sharp interior 90-degree transition corners bridging the wide and narrow sections.

**Shape 5: L-Bracket Inner Corner**
- **Orientation:** An asymmetrical "L" shape.
- **Probing Setup:** Source injected at the far top tip of the vertical leg. Sink located at the far right tip of the horizontal leg.
- **Expected Weak-Zone Mask:** The sharp internal 90-degree elbow joint.

## 5. Proposed Metrics
To evaluate sanity and usefulness, we measure the following non-fragile region targets:
- **Top-1 in Expected Mask:** Does the `#1` strongest hotspot fall cleanly inside the expected weak-zone mask? (Yes/No)
- **Top-3 Contains Expected Mask:** Is the expected choke point reliably found within the Top-3 hotspots? (Yes/No)
- **Minimum Distance:** Minimum Euclidean distance (px) from the strongest hotspot to the boundary of the expected mask.
- **Rank Match:** The absolute rank of the first hotspot that successfully intersects the mask.
- **Runtime:** Processing latency for 64x64 and 128x128.
- **Stability:** Observation of whether the signal vanishes under threshold modifications.

## 6. Acceptance Framing & Interpretation Guardrails
**Guardrails:**
- *This benchmark does not evaluate physical correctness.*
- *This benchmark does not validate fracture prediction.*
- *This benchmark only evaluates whether the method consistently highlights intuitive geometry-induced weak zones under simplified synthetic conditions.*
- **Positive result** = promising exploratory signal only.
- **Negative result** = this direction may be weak or not worth elevating.

**Final Output Verdict must clearly separate into:**
- `promising exploratory signal`
- `mixed / inconclusive`
- `failed sanity benchmark`

## 7. Raw Evidence (DP-EXP-017)
**Date:** 2026-03-21
**Execution:** 5 synthetic geometric shapes probed sequentially at 64x64 and 128x128 resolution.

**Resolution: 64x64**
- **Hourglass / Dumbbell:** Top-1 in Mask: NO (7,42) | Min Distance: 19.0 px
- **Notched Bar:** Top-1 in Mask: NO (7,21) | Min Distance: 23.1 px
- **Plate with Circular Hole:** Top-1 in Mask: NO (7,46) | Min Distance: 21.0 px
- **Key Neck / Narrow Shaft:** Top-1 in Mask: NO (7,17) | Min Distance: 23.0 px
- **L-Bracket Inner Corner:** Top-1 in Mask: NO (7,18) | Min Distance: 25.0 px

**Resolution: 128x128**
- **Hourglass / Dumbbell:** Top-1 in Mask: NO (7,106) | Min Distance: 19.9 px
- **Notched Bar:** Top-1 in Mask: NO (7,42) | Min Distance: 23.0 px
- **Plate with Circular Hole:** Top-1 in Mask: NO (7,46) | Min Distance: 21.0 px
- **Key Neck / Narrow Shaft:** Top-1 in Mask: NO (7,17) | Min Distance: 23.0 px
- **L-Bracket Inner Corner:** Top-1 in Mask: NO (7,18) | Min Distance: 25.0 px

**Summary Note:** Every single #1 Top Hotspot snapped rigidly to `Y=7` across all shapes and scales.

## 8. Failure Mechanism / Why It Failed
- **Ranked Signal:** The application layer explicitly ranked the steepest negative spatial gradients (the lowest Laplacian $\nabla^2 \Phi$ values).
- **Source-Edge Dominance:** The Top-1 node consistently anchored at `Y=7` because this is the exact geometric boundary where the synthetic source constantly injects new fluid pressure (`+10.0` per iteration) into a baseline `0.0` environment.
- **Internal Geometry Overwritten:** The mathematical pressure drop at the injection boundary is orders of magnitude steeper than any passive constriction drop caused later by a structural neck or notch. The injection singularity completely blinds the global extraction metric to subtle internal geometry.
- **Application-Layer Intervention Risk:** To fix this, the Application Layer would have to explicitly "know" where the sources are and aggressively mask/exclude the source-edges from the ranking. This would be a heavy, manual semantic intervention that destroys the integrity and elegance of Lineum as a simple, autonomous global solver.
- *Current evidence supports freeze under current setup; root-cause classification beyond that remains limited.*

## 9. Reproducibility Notes
To ensure physical and mathematical clarity for this specific test setup:
- **Role of Kappa:** `kappa = 0.05` was explicitly treated as the solid **material** (the conductive medium through which tension/flow travels). `kappa = 1.0` was treated as the empty **void** (absolute boundary / air).
- **Source/Sink Forcing Setup:** Bounded injection at `y=6:8` adding `+10.0` per iteration. Bounded sink at opposite edge acting with `*0.1` dampening per iteration.
- **Boundary Handling:** Outer 4 pixels of the entire matrix mathematically stripped from evaluation to prevent edge-of-world artifacts.
- **Extraction Rule for Hotspot Ranking:** Non-Maximum Suppression (radius=5.0px) layered over the 5th and 10th percentile lowest Laplacian severity filter.

## 10. Final Verdict
**FAILED SANITY BENCHMARK (FROZEN)**
- Tento exploratory směr neprokázal robustní geometric weak-zone highlighting.
- Aktuální setup je těžce dominován source-injection boundary artifact / singularity.
- Bez těžkých application-layer filtrací (maskování zdroje) není výsledek produktově ani metodicky čistý.
- Tento směr se nepovyšuje na canonical status, ani to nedefinuje active product direction. Branch is frozen.
