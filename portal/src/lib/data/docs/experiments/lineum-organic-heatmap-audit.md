# Exploratory Audit: Organic Heatmap Distribution

> **WARNING:** Internal exploratory, non-core, raw-data-first log. **Non-canonical, non-marketing material, making no official product claims.** May be killed if evidence is weak. Subject to change.

## 1. Scope & Hypothesis
**Hypothesis:** Providing game designers with an organic, continuous risk/cost map (e.g., zombie scent, radiation) derived from Lineum's wave diffusion yields structurally superior "shadows" around walls than standard radial blur overlays.
**Scope:** Evaluation of the 2D scalar field $\Phi$ strictly as a continuous structural texture.

## 2. Baseline & Kill Criterion
**Baseline:** Multi-Source Grid Flood-Fill + 2D Gaussian Blur (classic Gamedev implementation).
**Kill Criterion:** If the stationary field yields less than 5% absolute structural variance compared to a Gaussian Blur matrix, calculating PDE physics is mathematically redundant for this use-case and the branch will be killed.

## 3. Next Step
Conduct a quantitative blur-delta comparison.
