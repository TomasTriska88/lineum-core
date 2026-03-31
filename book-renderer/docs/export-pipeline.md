# PDF Export Pipeline

## General Outline

The export pipeline is designed to transform the live UI layout of the `book-renderer` Svelte app into physical print-ready PDFs using **Puppeteer Headless Chrome**.

### 1. Requirements
Ensure the development server is actively running (`npm run dev`) before generating PDF bundles, because the script actively pings `http://localhost:5173`. 

### 2. Execution Loop
The `scripts/export-pdf.js` operates the following tasks iteratively for each registered book (`foundations`, `motion`, `structure`):
1. Navigate Playwright/Puppeteer blindly to `/?book=<id>&exportMode=true`.
2. Generate the **Title sequence** (`<id>_title.pdf`).
3. Generate the **TOC & Preface sequence** (`<id>_intro.pdf`).
4. Generate the **Core Spreads** by targeting `/?book=<id>&printTarget=spreads` mapping (`<id>_spreads.pdf`).
5. Generates the final **Cover Print** passing generic ISBN blocks (`<id>_cover.pdf`).

### 3. ZIP Archiving
*DEPRECATED*: The pipeline previously archived files into a single ZIP. It now directly outputs PDF sets cleanly to the root execution dir with no packaging overhead.

### Validation Parameters
All headless exports MUST run with `timeout: 10000` to avoid orphaned browser instances.
