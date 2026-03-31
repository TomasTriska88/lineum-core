# Book Production Specification

This document defines the physical and digital output specifications for the Lineum Foundations book series. It serves as the single source of truth for the renderer engine configuration.

## 1. Global Print Formats (Trim Sizes)

The system is configured to target two primary physical dimensions. The Svelte renderer dynamically injects CSS variables to enforce these bounds:

### 1.1 Primary: US Trade (6x9 inch)
Target market: Global Distribution (Amazon KDP, Barnes & Noble).
- **Format:** 6 x 9 inches (152 x 229 mm)
- **Bleed:** 3 mm (Top, Bottom, Outer)
- **Renderer Target:** `--trim-width: 152mm`, `--trim-height: 229mm`

### 1.2 Secondary: EU Standard (B5)
Target market: European Academic/Technical Distribution.
- **Format:** 176 x 250 mm
- **Bleed:** 3 mm (Top, Bottom, Outer)
- **Renderer Target:** `--trim-width: 176mm`, `--trim-height: 250mm`

## 2. Cover Architecture & Spine Math

### Full Wrap Paperback Architecture
The cover is rendered as a **single continuous flat layout** designed strictly for Paperback Print on Demand (not a hardback wrapper or dust jacket).
It integrates:
- **Back Cover** (Left)
- **Spine** (Center)
- **Front Cover** (Right)

All three components are exported as one contiguous PDF arch.

### Spine Calculation
Because page counts will exceed 120+ pages, spine width cannot be static.
The Svelte generator calculates the spine using the standard paper thickness multiplier:
`Spine Width (mm) = Total Page Count * ~0.05 mm (paper thickness factor)`

### Back Cover Elements
The back cover requires:
- Short blurb (synopsis) extracted from `frontMatter.ts`
- Author block ("Tomáš Tříska")
- Fixed boundary placeholder for Publisher/Distributor ISBN barcodes.

## 3. Cover Design Identity

The cover abandons "technical document" or "dark void minimalism" logic in favor of premium retail aesthetics:
- **Base:** Light or neutral base (e.g., `#F8FAFC`, textured white/cream) to ensure strong thumbnail readability on Amazon and library shelves.
- **Visuals:** Thin geometric flow elements / waves deriving from the Lineum aesthetic. Subtle gradients rather than pure solid dark blocks.
- **Typography:** Minimal text. Extremely readable "FOUNDATIONS" title. 
- **Rule:** The cover must *never* look like internal dev documentation or an academic whitepaper constraint.

## 4. Book Naming Conventions & Automated Verification

All legacy development terminology has been expunged from the rendering pipeline and is strictly verified via Playwright E2E tests (`book.test.ts`).
- 🚫 **DO NOT USE:** "OEA", "Lineum Core", "Level 1"
- ✅ **USE:** "Foundations" (Book 1), "Motion" (Book 2), "Structure" (Book 3).
- **Enforcement:** The renderer pipeline explicitly searches for "FOUNDATIONS" in the front matter and will fail the build process if legacy system names leak into the physical print output.
