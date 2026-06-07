# Velum — Specification & Compiler Developer Guide

Velum (`.velum`) is an AI-native, semantic-geometric visual programming language. It represents user interfaces, state transitions, reactive variables, and data flows as spatial nodes and directional routes on a unified 2D coordinate canvas.

This directory contains the core compiler implementation (`velum-compiler.js`), validation schemas, and automated unit tests.

---

## 1. Design Philosophy

Traditional programming paradigms define layouts linearly (e.g., nested HTML/XML files or linear JSX code). Velum breaks from this by treating development as a **2D topological canvas**:

*   **Spatial DOM Construction**: Visual nodes are placed freely in a 2D coordinate space. The compiler determines their relative hierarchy (e.g., parent-child relationships) and order in the generated DOM by sorting their geometric positions (`[x, y]` coordinates) top-to-bottom and left-to-right.
*   **Topological Path Flow**: Interactive behaviors, event routing, and data updates are defined as directional paths (`edges` or `paths`) connecting UI nodes (`ui.`), state databases (`db.`), and network interfaces (`net.`).
*   **Strategy-Driven Architecture**: The compiler uses the **Strategy Pattern** to compile the single Velum coordinate schema into any target framework. It has built-in strategies for **Svelte 5** and **Vanilla JS (Web Components)**, and allows developers to register custom drivers at runtime.

---

## 2. File Format Specification (`.velum`)

A `.velum` file is represented as a structured JSON object containing six core blocks. The file structure is formally validated against the JSON Schema (Draft-07) defined in [velum-schema.json](./velum-schema.json).

```json
{
  "$schema": "./velum-schema.json",
  "name": "ComponentClassName",
  "target": "vanilla",
  "imports": [],
  "helpers": [],
  "states": {},
  "nodes": [],
  "paths": [],
  "custom_styles": ""
}
```

### 2.1 File Blocks Description

*   `name` *(string, required)*: The class or component name (e.g., `LangPicker`). Used for generating class declarations and registering custom elements.
*   `target` *(string, optional)*: The fallback compilation driver. Can be `"vanilla"` or `"svelte"`. Defaults to `"vanilla"`.
*   `imports` *(array of strings, optional)*: A list of ES module import statements required by the component helper functions or states.
*   `helpers` *(array of strings, optional)*: Helper functions, constants, or computed/derived states.
*   `states` *(object, optional)*: Key-value map of reactive states. Each entry defines a reactive variable and its initial value:
    ```json
    "states": {
      "isOpen": { "init": false }
    }
    ```
*   `nodes` *(array of objects, required)*: Coordinates and properties of nodes placed on the canvas.
    *   `id` *(string)*: Unique identifier. Layer prefixes:
        *   `ui.`: User interface elements (buttons, menus, text).
        *   `db.`: Database or local state variables.
        *   `net.`: External API or network calls.
    *   `pos` *(array of 2 numbers)*: `[x, y]` pixel coordinates on the visual design canvas.
    *   `type` *(string)*: Node type (e.g., `"dropdown_toggle"`, `"menu_container"`).
    *   `label` / `label_binding` *(string)*: Static or dynamic text label.
    *   `show_condition` *(string)*: Expression determining visibility.
*   `paths` *(array of objects, optional)*: Actions, events, and flows routing between nodes.
    *   `from` / `to` *(string)*: Source and target node IDs.
    *   `action` / `flow` *(string)*: Event triggers (e.g., `"click"`, `"resolve_route"`).
    *   `handler` *(string)*: Code block executed when the action fires.
*   `custom_styles` *(string, optional)*: Scoped CSS styling rules.

---

## 3. Concrete Example: Input vs. Output

Below is a complete comparison showing a Velum file and its compiled outputs.

### 3.1 Input Velum Canvas File (`LangPicker.velum`)
```json
{
  "name": "LangPicker",
  "target": "svelte",
  "imports": [
    "import { page } from \"$app/stores\";"
  ],
  "helpers": [
    "let currentLang = $derived(page.data.locale || 'en');"
  ],
  "states": {
    "isOpen": { "init": false }
  },
  "nodes": [
    {
      "id": "ui.DropdownToggle",
      "pos": [150, 20],
      "type": "dropdown_toggle",
      "label": "Language",
      "label_binding": "currentLang.toUpperCase()"
    },
    {
      "id": "ui.MenuContainer",
      "pos": [150, 70],
      "type": "menu_container",
      "show_condition": "isOpen",
      "loop_data": "langs",
      "loop_item": "lang",
      "active_condition": "lang.code === currentLang"
    }
  ],
  "paths": [
    {
      "from": "ui.DropdownToggle",
      "action": "click",
      "handler": "isOpen = !isOpen"
    }
  ]
}
```

### 3.2 Output: Svelte 5 Strategy Target
```html
<script lang="ts">
    import { page } from "$app/stores";

    let currentLang = $derived(page.data.locale || 'en');

    let isOpen = $state(false);
</script>

<div class="dropdown lang-dropdown" role="menu" tabindex="0">
    <button
        class="dropdown-toggle lang-toggle"
        onclick={() => { isOpen = !isOpen }}
    >
        {currentLang.toUpperCase()}
        <svg class="chevron-icon" class:rotated={isOpen} viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="6 9 12 15 18 9"></polyline>
        </svg>
    </button>
    <div
        class="dropdown-menu"
        class:mobile-open={isOpen}
        style="min-width: max-content;"
    >
        {#each langs as lang}
            <a
                href="#"
                hreflang={lang.code}
                data-sveltekit-reload
                class="lang-btn"
                class:active={lang.code === currentLang}
            >
                {lang.label} ({lang.abbr})
            </a>
        {/each}
    </div>
</div>
```

---

## 4. Production Optimization & Minification Strategy

Developers often ask how we minimize boilerplate code, eliminate comments, and compress Velum inputs and outputs for production. The Lineum project approaches optimization through a strict separation of concerns:

### 4.1 Coordinate & Metadata Stripping (Compiler-Level)
*   **Zero Canvas Bloat at Runtime**: The coordinates (`"pos": [150, 20]`) and other visual metadata in `.velum` files are **strictly compile-time variables**. The compiler uses coordinates *only* to sort nodes geometrically (`sortNodes`), ensuring stable DOM generation. Once compilation is complete, the coordinates are completely discarded. The generated `.svelte` or `.js` component contains **zero** position vectors, grid scales, or visual editing traces.
*   **JSON Minification**: Raw `.velum` files are standard JSON. To minimize their storage size on disk, they can be minified by standard JSON minifiers (i.e. stripping all comments and formatting whitespace via `JSON.stringify(velum)`).

### 4.2 TypeScript Type Stripping (Vanilla Strategy)
*   To keep the Vanilla Custom Element driver target completely dependency-free and browser-runnable, the compiler includes a regex-based `stripTypeScript` step. This dynamically removes static TypeScript type annotations (e.g. `: string`, `: void`, `as const`) from the helpers list, preventing syntax crashes in native browsers:
    ```javascript
    // Input helper string:
    "const activeCode: string = 'en';"
    
    // Output Vanilla JS:
    "const activeCode = 'en';"
    ```

### 4.3 Code Compression & Comment Removal (Downstream Tooling)
*   **Why we don't build minification into `velum-compiler.js`**: To satisfy the core rule of **Zero Dependencies**, the compiler does not include heavy AST parsers or JavaScript minification libraries (like Terser, Uglify, or esbuild). Adding these would bloat the compiler code and restrict its browser compatibility.
*   **The Downstream Build Pipeline**: Instead, the Velum compilation chain relies on standard, industry-grade production bundlers. In the `lineum-dynamics` web portal, **Vite** and **esbuild** are used. When you run `npm run build`, these tools automatically:
    1.  Strip all comments (both JSDoc and inline comments) from the compiled outputs.
    2.  Shorten variable, function, and state class names (obfuscation).
    3.  Tree-shake unused helper modules.
    4.  Compress spacing, brackets, and line breaks into a single optimized bundle.

---

## 5. Compiler CLI & API

### CLI Usage

Execute the compiler using the command line:

```bash
# Compile to Vanilla JS Web Component (Default target)
node velum-compiler.js path/to/component.velum

# Compile with explicit target
node velum-compiler.js path/to/component.velum --target svelte
node velum-compiler.js path/to/component.velum --target vanilla

# Compile to a custom output file path
node velum-compiler.js path/to/component.velum path/to/output.js --target vanilla
```

### Extensibility (API Strategy Pattern)

You can register custom target compilation strategies on the fly. This makes the compiler highly extensible for other frameworks (React, Vue, WebGL, etc.):

```javascript
import { registerTarget } from './velum-compiler.js';

// Register a React component compiler target
registerTarget('react', (velum) => {
  const { name } = velum;
  return `
import React, { useState } from 'react';
export function ${name}() {
  // custom React compilation logic
}
  `;
});
```

---

## 6. Verification and Automated Testing

Unit tests for Velum validation, sorting, Svelte generation, and Vanilla custom elements are located in the `tests/` subdirectory.

*   **Terminal CLI**: Run the tests directly via Node.js:
    ```bash
    node tests/velum-compiler.test.js
    ```
*   **Browser Web Dashboard**: Start the development server from the compiler's root:
    ```bash
    python -m http.server 8080 --bind 127.0.0.1
    ```
    Then visit [http://127.0.0.1:8080/tests/test-runner.html](http://127.0.0.1:8080/tests/test-runner.html) to run and view the tests in a clean, visual HTML runner.
