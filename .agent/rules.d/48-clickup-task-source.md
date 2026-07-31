# Mandatory Active Task Source: ClickUp

**Status:** Binding supplement to `.agent/rules.md`.

## Active task authority

The Lineum Dynamics ClickUp workspace is the single operational source of truth for active tasks, priorities, owners, statuses, dates, dependencies, and workflow decisions across the Lineum project family.

- Workspace name: `Lineum Dynamics`.
- Workspace ID: `90121717552`.
- Every ClickUp read, search, lookup, create, update, or status operation performed from or for `lineum-core` MUST explicitly target workspace ID `90121717552` whenever the connector accepts a workspace identifier.
- Do not probe, search, infer from, or write to another ClickUp workspace for `lineum-core` work unless the project owner explicitly directs that specific operation elsewhere.
- If a connector omits workspace selection or returns ambiguous multi-workspace results, stop treating the result as authoritative and retry with workspace ID `90121717552` before drawing a task-state conclusion.
- For public Core research and simulation work, use `Research & Engineering -> Engine R&D -> Core Simulations` unless the task clearly belongs in another ClickUp location.
- Core Simulations list ID: `901217864718`.

## Repository backlog boundary

`todo.md` and any repository-local task list are historical or provenance material only. They are not active backlog authorities and must not be used to select current priorities, infer current status, assign ownership, or record new operational tasks.

Agents may read historical task files when reconstructing research provenance, but must label them as historical evidence and cross-check any current workflow conclusion against ClickUp.

## Mandatory workflow

1. Search ClickUp before starting or registering material work to avoid duplicate tasks.
2. If no matching task exists, create the task in the appropriate ClickUp list at or before the first durable checkpoint.
3. Keep workflow state in ClickUp and keep scientific evidence in Git. A ClickUp description or comment never substitutes for a standalone research report, test, commit, or reproducible artifact.
4. After a coherent Git checkpoint, update the linked ClickUp task with the commit, result, limitations, and next gate when the connector supports the operation.
5. Do not mark a task complete merely because a report or commit exists; verify that the declared acceptance criteria are satisfied.
6. If ClickUp is temporarily unavailable, record the access blocker in the active report or working notes and continue only work that does not depend on current task priority. Never fall back to `todo.md` as the live tracker.

## Scope separation

ClickUp is the operational tracker. Git remains the source of truth for code, scientific history, equations, tests, negative results, and whitepaper evidence. Neither system may silently replace the other.
