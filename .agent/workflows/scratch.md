---
description: Convention for local disposable Codex scripts and diagnostic outputs
---

# Scratch Directory Convention

## Status and scope

`.scratch/` is a temporary, local-only Codex workspace. It is ignored by Git and is not expected to exist in the GitHub repository tree, the GitHub connector, another checkout, CI, or a later work session.

Its contents may be deleted, replaced, or lost at any time without notice.

## Binding rules

1. **Temporary helpers only.** Put diagnostics, one-off analysis scripts, debug tools, translation drafts, caches, intermediate data, terminal logs, and disposable simulation outputs in `.scratch/`, never in the project root.

2. **Never rely on scratch.** No implementation decision, scientific conclusion, provenance claim, parameter choice, negative result, reproduction chain, whitepaper statement, or task status may depend on a `.scratch/` file.

3. **Never use scratch as repository evidence.** Do not search GitHub, the GitHub connector, commit trees, or repository file listings for `.scratch/` contents. Do not count a missing `.scratch/` path, a `404`, or the absence of a scratch filename as evidence that a script did not exist or an experiment did not run. Such absence is expected and non-informative.

4. **Historical references are names only.** If committed prose mentions a `.scratch/` path, that mention proves only that an ephemeral local filename was referenced. It does not recover the file, its contents, its execution, its parameters, or its results. Classify it as `unversioned_local_reference` unless the complete decision-relevant material is independently preserved in version control.

5. **Promote retained evidence immediately.** Before a result can inform another consequential research step, copy every decision-relevant question, equation, assumption, parameter, seed, input, algorithm, executable verification code, output, uncertainty, limitation, negative result, and reopen condition into the active standalone report under `research/`. A stable reusable research tool may instead be committed to an explicitly research-scoped path outside `lineum_core/`, but the standalone report must remain independently operational.

6. **No provenance matrices for scratch paths.** Provenance and receipt matrices may include a committed document's mention of a scratch filename, but must not create repository-presence cells for `.scratch/` or treat connector fetch attempts as valid receipt checks.

7. **Permanent tests stay permanent.** Regression tests and retained validation code do not belong in `.scratch/`. Place them in the repository location required by the research and library-promotion rules.

8. **Cleanup has no evidentiary effect.** Scratch contents may be cleaned automatically at the end of a task. Cleanup neither deletes valid permanent evidence nor changes the status of a claim, because valid evidence must already exist outside `.scratch/`.

## Examples

Temporary local helper:

```python
write_to_file(".scratch/inspect_checkpoint.py", ...)
```

Incorrect root-level helper:

```python
write_to_file("inspect_checkpoint.py", ...)
```

Correct diagnostic output:

```powershell
pytest > .scratch/fail_log.txt
```

Incorrect diagnostic output:

```powershell
pytest > fail_log.txt
```

## Cleanup

```powershell
Remove-Item -Path .scratch/* -Force -ErrorAction SilentlyContinue
```
