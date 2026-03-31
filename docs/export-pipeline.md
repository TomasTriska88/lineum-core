# Print Export Pipeline

This document catalogs the node-based rendering orchestration script used to bridge Svelte Web DOMs into static, DTP-ready PDF distributions.

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
