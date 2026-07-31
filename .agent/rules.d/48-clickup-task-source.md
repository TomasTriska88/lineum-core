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

## ClickUp MCP quota protection

ClickUp MCP calls are a scarce shared workspace resource. Every tool invocation counts against the operational budget even when it returns no result, a server error, or a rate-limit response.

Until the project owner or current billing evidence explicitly confirms that the `Lineum Dynamics` workspace has purchased the ClickUp Everything AI add-on, agents MUST assume that the workspace is subject to the lowest published rolling 24-hour MCP allowance. Connector availability, ClickUp AI trial access, or ordinary paid-plan access is not evidence that Everything AI is enabled. Everything AI is a workspace billing add-on, not a locally installed program.

### Default checkpoint budget

A coherent research or engineering checkpoint has a default budget of three ClickUp calls and a hard ceiling of five calls:

1. one targeted opening read;
2. one closing comment or task update after the Git checkpoint;
3. one optional verification read only when the write response is insufficient or task state is decision-critical.

Calls four and five are reserved for one necessary task discovery or one necessary recovery from incomplete data. Exceeding five calls for one checkpoint requires explicit project-owner authorization and a recorded reason. Do not split one coherent checkpoint into artificial sub-checkpoints to evade this ceiling.

### Targeted-access rules

- When a task ID is known, use the direct task operation with that ID. Do not perform a global search first.
- Request summary detail and omit subtasks, comments, attachments, time entries, and hierarchy unless the specific decision requires them.
- Reuse a task state already retrieved during the same uninterrupted checkpoint unless there is concrete reason to believe that state changed materially.
- When a task ID is unknown, perform at most one narrowly filtered search, limited to task assets and the known workspace, list, folder, or space whenever those coordinates are available. Cache the resolved task ID in the durable report or linked task context.
- Do not search other workspaces, retrieve broad workspace hierarchies, paginate speculatively, or fetch every comment to orient routine work.
- Batch coherent Git results into one ClickUp update instead of posting progress after every small commit, document edit, or experiment step.

### Failure and rate-limit handling

- A ClickUp server error receives at most one attempted call for the requested operation. Do not immediately retry, fan out across workspaces, or substitute repeated searches.
- On `RATE_LIMIT_EXCEEDED`, record the returned reset or retry-after value, stop all ClickUp calls until that window has expired, and do not poll for recovery.
- While ClickUp is unavailable, continue only work whose scientific or engineering correctness does not depend on current task priority or mutable ClickUp state.
- Record the unsynchronized checkpoint in the active Git report or final owner-facing summary. Synchronize it with one batched ClickUp write after access returns; do not generate a burst of historical updates.
- Never use repository `todo.md` material as a fallback live backlog during a ClickUp outage.

## Repository backlog boundary

`todo.md` and any repository-local task list are historical or provenance material only. They are not active backlog authorities and must not be used to select current priorities, infer current status, assign ownership, or record new operational tasks.

Agents may read historical task files when reconstructing research provenance, but must label them as historical evidence and cross-check any current workflow conclusion against ClickUp.

## Mandatory workflow

1. Use a known task ID directly when available; otherwise use one narrowly filtered search before starting or registering material work to avoid duplicate tasks.
2. If no matching task exists, create the task in the appropriate ClickUp list at or before the first durable checkpoint, while remaining within the checkpoint call budget.
3. Keep workflow state in ClickUp and keep scientific evidence in Git. A ClickUp description or comment never substitutes for a standalone research report, test, commit, or reproducible artifact.
4. After a coherent Git checkpoint, update the linked ClickUp task once with the commit, result, limitations, and next gate when the connector supports the operation.
5. Do not mark a task complete merely because a report or commit exists; verify that the declared acceptance criteria are satisfied.
6. If ClickUp is temporarily unavailable, follow the failure and rate-limit rules above and continue only work that does not depend on current task priority.

## Scope separation

ClickUp is the operational tracker. Git remains the source of truth for code, scientific history, equations, tests, negative results, and whitepaper evidence. Neither system may silently replace the other.
