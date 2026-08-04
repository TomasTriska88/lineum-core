# ClickUp Cross-Repository Routing

**Status:** Binding supplement to `.agent/rules.md`.
**Revision:** 1.0.0
**Effective date:** 2026-08-04

## Canonical operational source

For every ClickUp read, write, search, status report, planning update, checkpoint, or synchronization performed while working in `TomasTriska88/lineum-core`:

1. Read the current `lineum-dynamics/lineum-dynamics` `AGENTS.md` on its target branch.
2. Read the current `lineum-dynamics/lineum-dynamics/.agent/clickup-task-source-of-truth.md` on that branch.
3. Treat the Dynamics file as the sole canonical procedure for connector capability state, native actions, fallbacks, readback verification, hierarchy handling, and restoration tests.
4. Treat `.agent/rules.d/48-clickup-task-source.md` in Core as a Core-specific safety floor for the authorized workspace, Core task location, quota protection, and Git-versus-ClickUp boundary.
5. When a procedural statement in Core differs from the current Dynamics source, the current Dynamics procedure governs. Preserve the stricter Core workspace guard and call-budget limit unless the project owner explicitly changes them.

Do not copy the complete Dynamics ClickUp workflow into another Core rule file. Keep cross-repository routing here and maintain the detailed operational procedure in its canonical Dynamics source.

## Failure handling

Do not stop at `ClickUp mode = unsynchronized` merely because a native comment action is unavailable when the canonical Dynamics procedure provides a safe task-description fallback and all of its preconditions can be verified.

Every decision-relevant ClickUp write must be read back. A generic success response is insufficient when the affected object can be retrieved directly.

When neither the canonical native operation nor its documented fallback can be completed and verified, record `ClickUp mode = unsynchronized` explicitly and preserve the durable scientific or engineering evidence in Git.

## Scope boundary

This routing rule changes only operational task synchronization. It does not move scientific evidence, equations, code, research reports, or whitepaper authority out of `lineum-core`.

## Changelog

- `1.0.0` — 2026-08-04: Added explicit routing to the canonical Dynamics ClickUp procedure after a native-comment failure was incorrectly treated as the end of synchronization even though the documented description fallback was available.
