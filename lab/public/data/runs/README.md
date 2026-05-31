# Lab Trajectory Runs

This directory contains curated pre-generated trajectory datasets used for Svelte Lab UI visualization and scientific validation of the observer-only `ContactGraph` telemetry.

## Preservation Policy

To maintain repository hygiene and avoid wasting space, the preservation policy dictates:
*   **Keep Manifest Presets:** Preserve any runs registered in `lab/public/data/manifest.json`.
*   **Keep Referenced Artifacts:** Keep runs referenced in audits, whitepapers, or tests.
*   **Keep Test Fixtures:** Keep intentional test fixtures, even if empty/corrupted.
*   **Avoid Redundant Duplicates:** Do not keep multiple unregistered exact bitwise duplicates.

---

## Run Classification & Hygiene Notes

### 1. Intentional Quarantine Test Fixture
*   **Run ID:** `spec6_false_s41_20260306_201952`
*   **Status:** **DO NOT DELETE.**
*   **Details:** The `trajectories.json` file in this directory is a 2-byte empty array stub (`[]`). This run is intentionally empty and serves as a test fixture. It is explicitly scanned and verified by `tests/test_audit_quarantine.py` to ensure the quarantine scanning logic works correctly under corrupted or missing trajectory states.

### 2. Group A: Unregistered Collision Presets
*   **Run ID:** `spec6_false_s41_20260307_162450`
*   **Status:** **RETAINED REPRESENTATIVE.**
*   **Details:** During the Phase 78 hygiene audit, three unregistered run directories (`162450`, `211518`, and `212138`) were found to contain identical bitwise duplicates of the same trajectory dataset (SHA-256: `589d4646...`). To clean up redundant data, the duplicates `211518` and `212138` were removed via `git rm -r`, while `162450` is retained as the sole representative for historical record and offline Phase 78 reproducibility.

### 3. Group B: Manifest-Registered Duplicates
*   **Run IDs:**
    *   `spec6_false_s41_20260307_225444` (Run 3: Tangential Slips)
    *   `spec6_false_s41_20260310_130840` (Run 4: System Decay)
*   **Status:** **PRESERVED.**
*   **Details:** These two runs contain identical bitwise duplicates of the same trajectory dataset (SHA-256: `f7185ac3...`). However, both are currently preserved because they are registered as distinct preset entries under different scenario labels in `manifest.json`. Future consolidation requires a separate manifest/UI review.

---

## Guidelines for Adding New Runs

Future trajectory runs should only be added if they satisfy the following criteria:
1.  **Registry / Reference:** Must have an entry in `manifest.json` or be explicitly referenced by an active audit or whitepaper.
2.  **Scenario Labeling:** Must contain a defined scenario tag/label in `metadata.json`.
3.  **Provenance:** Must document the generation configuration and equation fingerprint (e.g. Eq-12 model settings) in `metadata.json`.
4.  **Preservation Justification:** Must have a documented reason for why this specific run represents unique scientific or UI validation value.
