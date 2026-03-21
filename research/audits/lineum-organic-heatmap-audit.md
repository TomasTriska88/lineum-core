# Exploratory Audit: Organic Heatmap Distribution

> **WARNING:** Internal exploratory, non-core, raw-data-first log. **Non-canonical, non-marketing material, making no official product claims.** May be killed if evidence is weak. Subject to change.

## 1. Scope & Hypothesis
**Hypothesis:** Providing game designers with an organic, continuous risk/cost map (e.g., zombie scent, radiation) derived from Lineum's wave diffusion yields structurally superior "shadows" around walls than standard radial blur overlays.
**Scope:** Evaluation of the 2D scalar field $\Phi$ strictly as a continuous structural texture.

## 2. Baseline & Kill Criterion
**Baseline:** Multi-Source Grid Flood-Fill + 2D Gaussian Blur (classic Gamedev implementation).
**Kill Criterion:** If the stationary field yields less than 5% absolute structural variance compared to a Gaussian Blur matrix, calculating PDE physics is mathematically redundant for this use-case and the branch will be killed.

## 3. Next Step / Current Status
**STATUS: PREPARED**
The branch is ready for execution, but currently paused pending the Vulnerability branches validation completion. Next assigned action is to conduct a quantitative blur-delta comparison strictly avoiding the frozen Hybrid mode (evaluating pure Diffusion vs pure Wave signatures only).

## 4. Boundary Definition: Core vs Application
**Lineum-Native Mechanisms Actually Used:**
- Continuous field distribution operating on asymmetric maps.
- Diffusion "bleeding" and shadow-casting organically resolving around sharp topological barriers (unlike strict 2D radial distance blurs).
**Application-Layer Logic:**
- Structural SSIM image delta calculations against standard Gaussian matrices.
- Heatmap gradient coloring, opacity thresholds, and RGBA UI rendering.
- Source injection absolute limits.
**Allowed Optimization Layer:**
- Aggressive visual smoothing, clamping the visual gradient opacity, and scaling the point-source weights to make the map look "right" to a user.
**Not a Fundamental Physics Claim:**
- Creating a visually stunning "Zombie Scent" map or "Radiation Zone" by clamping opacities is UI product engineering, not a new cosmological discovery of the Lineum core's behavior.
