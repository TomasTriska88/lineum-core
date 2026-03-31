# Book Layout & Page Architecture Rules

The Svelte-based rendering engine must enforce absolute structural integrity according to traditional book publishing logic.

## 1. Page Structuring Constraints

The book renderer guarantees zero content loss. All components (Hook, Explanation, What it is, How to solve, Why it works, AHA moment, Summary) must be explicitly bound to the Svelte components matching original markdown hashes.

### 1.1 Symmetrical & Asymmetrical Variation
By default, the spread operates iteratively:
- **Left Page (Even):** Visuals + Hook focus.
- **Right Page (Odd):** Explanation + AHA + Summaries.

*Variation Matrix (Max 20% Devation)*:
To prevent an automated template feel, the `layoutVariant` property forces variations in reading rhythms:
- **Standard (70%):** Classic hook left, prose right.
- **Shifted (20%):** Prose left, trailing image/AHA right.
- **Hero-AHA (10%):** Massive bleed visuals supporting a singular AHA moment.

## 2. Page Numbering Protocol

Page numbers (folios) map purely to internal engine indexes via the CSS `.page-number` container:
- **Rule 1:** Left-page numbers must rigidly sit on the bottom left (margin edge).
- **Rule 2:** Right-page numbers must similarly align dynamically to the bottom right.
- **Rule 3:** The Title and Imprint page are blind (no numbers).
- **Rule 4:** The Front Matter (TOC, Preface) utilizes **Roman Numerals** (`I, II, III`).
- **Rule 5:** First Arabic numeral (`1`) starts on the first Concept chapter.

## 3. Typographical & Margin Rules

- Primary text (body, explanations) enforces a Serif font for prolonged print readability.
- Margins dynamically lock absolute bounding boxes via `app.css`. The *inner* margin (Spine side) must always exceed the outer margin (e.g., 25mm inner, 15mm outer) to safeguard text from physical binding cuts.
- Equations (`KaTeX` integrations) are forced into `white-space: nowrap !important;` to avoid shattering formula blocks during natural paragraph wrapping.

## 4. Universal Image Prompts

Visual continuity is required for all mathematical geometry.
1. Every `<img>` or `{placeholder}` explicitly outputs a `data-prompt` embedded attribute.
2. The UI outputs `data-variant` defining how the image was rendered.
3. This guarantees AI regeneration fidelity if future book editions require visual revamping.
