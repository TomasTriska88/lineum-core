# Lineum Series: Book Layout & Data Rules

This document codifies the architectural rules for rendering Lineum Series books through the Svelte print layout engine.

## 1:1 Content Generalization Rule
The data schema `Concept` strictly respects the source material for each volume. Every book uses the universal property array `proseSegments` to render flexible body text directly from the markdown.

**Forbidden Practices:**
- Do NOT artificially invent headings.
- Do NOT force Book 2 or 3 to use "What it is", "How to solve", "Why it works" if the original source does not use them.
- Preserve legacy labels in Book 1 exactly as written to ensure backward compatibility.

### Datatype Structure
```ts
export interface Concept {
  // Frontmatter
  id: string;
  chapterNumber: number;
  chapterTitle: string;
  title: string;
  hook: string;
  explain: string;
  image: { path: string; prompt: string; };
  aha: string;
  summary: string;
  
  // The Generalized Body Array
  proseSegments: {
    label: string;
    body: string;
  }[];
}
```

## UI Integrity Guarantees
- The `PreviewToolbar.svelte` uses a fully responsive, wrapping Segmented Pill design to prevent horizontal text clipping or viewport squashing on narrow screens.
- All internal run-in headers (`<h4>`) are dynamically generated from the `proseSegment.label`.
- The Playwright E2E suite actively tests that each book renders its text without clipping and preserves original header names.
