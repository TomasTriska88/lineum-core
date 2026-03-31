# Print Export Pipeline

This document catalogs the node-based rendering## The Architecture Disconnect

**CRITICAL RULE:** The public-facing Web Viewer (`+page.svelte` in `spread`/`epub` modes) is structurally separated from the rigorous Print QA Mode. 
The PDF export scripts strictly bypass the interactive DOM and enforce real millimeter bounding boxes for generating print-ready `Foundations`, `Motion`, and `Structure` volumes.

### Structural Flow
1. **Multi-Book Loading**: The pipeline evaluates `?book=[id]` to compile isolated book payloads (`foundations`, `motion`, `structure`).
2. **Cover Render**: The Full Wrap Paperback format (Back Cover + Spine + Front Cover) calculates spine thickness dynamically based on total content length, rendering natively without interactive CSS rules. 
3. **Interior Iteration**: The viewer natively supports `<FrontMatter />` and `<BackMatter />` as bookends to the `<ConceptSpread />` generation array.
2. **QA Print Mode (`viewMode="qa-print"`):** An internal diagnostic debug tool for verifying page breaks, bleed zones, and explicit page numbering prior to PDF compilation.
3. **PDF Export:** The immutable, final deployment artifact generated headlessly via Playwright. **The web viewer is NOT a substitute for the printed PDF.**

## Run Architecture

The Svelte renderer functions exclusively as a live development tool or future interactive medium. The physical artifact is orchestrated sequentially via Playwright CLI:
`node scripts/export-pdf.js --target=[preset_name]`

## Export Modes (3 Fixed Outputs)

### 1. Global Print (`--target=print-global`)
Generates physical output for standard international distribution.
- **Dimensions:** 6x9 inch (Standard US Book)
- **Features:** Trimming boundaries + 3mm full bleed rendering on assets. Margin safety checks.
- **Profile:** CMYK preparation. Embedded fonts. Max Playwright quality footprint.

### 2. EU Print (`--target=print-eu`)
Generates physical output for European / Specialized distributions.
- **Dimensions:** B5 size.
- **Features:** 3mm Bleed limits. Same high-density specifications as global execution.

### 3. Digital Asset (`--target=ebook`)
Generates pure PDF or EPUB readiness.
- **Dimensions:** RGB color mapping natively parsed without press restrictions.
- **Features:** Removes 3mm physical bleeds. Assets optimized to screen/tablet DPI limits.

## Continuous Testing Pipeline
The export script does not run if CI verification fails.
Prior to any `--target` export, Playwright will run:
- **`tests/book.test.ts`**: Verifies 100% `innerText()` checksum match against source MD.
- **Layout Validation**: Computes `Element.getBoundingClientRect()` dynamically to ensure zero horizontal or vertical text/content spill outside page boundaries coordinates.
- **Mathematical Integrity**: Confirmation (`.katex` DOM presence without stray double-dollar `$$` artifacts).
