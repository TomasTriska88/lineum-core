# Single Active Research Report and Readable Evidence

**Status:** Binding supplement to `.agent/rules.md`.

## One continuous programme, one active report

A continuous scientific programme with one controlling objective, one comparison target, or one decision chain must have exactly one active standalone Markdown report under `research/`.

Experiments, controls, ablations, independent checkers, negative results, owner hypotheses, cross-disciplinary comparisons, and later checkpoints within that programme are sections and versioned updates of the same active report. They must not be promoted into additional active `.md` reports merely because the mechanism, method, or execution lane changes.

A new active report is permitted only when:

1. the scientific objective is genuinely separate and can be decided indepently of the existing programme; or
2. the project owner explicitly authorizes a separate report after receiving the proposed boundary in plain language.

When an accidental second report overlaps an existing programme, merge every decision-relevant fact, result, limitation, provenance receipt, and reopen condition into the authoritative report. After explicit owner approval, remove the accidental report from the active branch while preserving its Git history and recording the reason for the merge.

## Directly readable Markdown

The active report must be directly understandable and auditable as ordinary UTF-8 Markdown without decoding, extraction, decompression, custom loaders, or hidden state.

The following are forbidden as canonical or substitute report content:

- embedded ZIP, tar, XZ, gzip, or another archive;
- Base64, Unicode payload encoding, binary blobs, or opaque capsules;
- machine-generated payloads that conceal prose, equations, source code, data, failures, or chronology;
- a short readable wrapper whose material evidence exists only inside an encoded block.

Existing capsule-based material is technical debt. It must be unpacked into ordinary readable Markdown and plain companion artifacts at the next safe coherent checkpoint. Do not add a new capsule while an old one remains.

## Plain companion artifacts

Large executable or machine-readable evidence may live beside the active report as ordinary text files when keeping every byte inline would make the Markdown impractical or exceed a repository transport limit.

Permitted companion formats include `.py`, `.json`, `.jsonl`, `.csv`, and `.txt`. Every such artifact must:

1. belong unambiguously to the same research subject;
2. be directly readable with ordinary tools and require no decoding step;
3. have a stable descriptive path and filename;
4. record provenance, schema, environment, and cryptographic hash where applicable;
5. be referenced from the active report with its exact role and verification command;
6. preserve negative and null results as faithfully as positive results;
7. remain evidence or executable support, never a second narrative or decision report.

The active report must still contain the complete scientific question, assumptions, equations, units, protocol, observables, thresholds, human-readable results, interpretation, uncertainty, limitations, contradiction ledger, and next gate. Companion files may carry bulk rows, exact JSON, or full executable implementations, but may not replace the reasoning needed to understand or challenge the conclusion.

## Publication and migration gate

Before publishing a migration away from capsules or duplicate reports:

1. verify the current authoritative report and every source blob or historical commit used;
2. inventory every capsule member or overlapping-report section;
3. prove that each decision-relevant item is represented in readable Markdown or a plain companion artifact;
4. compare hashes or exact values for retained executable and machine-readable evidence;
5. verify that no confidential or third-party-restricted material crosses repository boundaries;
6. publish the report, artifacts, and rule change atomically when they are interdependent;
7. fetch the resulting commit and verify the final changed-file set and content.

A connector limitation does not relax this gate. An incomplete migration must remain unpublished rather than entering history as a misleading halfway state.
