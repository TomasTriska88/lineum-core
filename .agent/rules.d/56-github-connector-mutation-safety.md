# GitHub Connector Mutation Safety

**Status:** Binding supplement to `.agent/rules.md`.

## Purpose

This rule prevents repository corruption, misleading intermediate history, and reproducibility loss when GitHub connector capabilities are dynamically discovered, reloaded, routed, or partially available.

It complements `.agent/rules.d/49-github-branch-safety.md`. Rule 49 remains authoritative for branch creation, branch-race checks, atomic multi-file publication, and protected-history behavior. This rule governs connector action identity, write-path failure handling, unexpected mutations, readback verification, and byte-preserving treatment of existing files.

## Exact write-action gate

Before every GitHub connector mutation, verify in the current tool context:

1. the exact repository and target branch;
2. the exact target path or ref;
3. the current branch HEAD or immutable parent SHA;
4. the exact connector action name to be invoked;
5. the current action schema and documented side effect;
6. whether the action creates an object only, creates a commit, changes a ref, or mutates file contents;
7. the expected returned identity needed for readback verification.

Do not rely on an action schema, namespace routing, capability list, or assumed side effect remembered from an earlier tool-discovery step. If tools are rediscovered, reloaded, or dynamically re-routed before the mutation, re-verify the exact write action before calling it.

## No mutation probes

Repository-mutating actions must never be used to test connector capability, permission, branch existence, ref resolution, endpoint routing, payload behavior, or schema compatibility.

Use read-only discovery first. A write action is permitted only when its intended repository mutation is itself part of the approved deliverable.

This prohibition applies to file writes, blob creation, tree creation, commit creation, branch creation, ref updates, workflow publication, issue creation used as transport, and any equivalent mutating endpoint.

## Write-path latch

Maintain a `GITHUB_WRITE_PATH_LATCH` for each exact connector write action within a coherent checkpoint.

The latch becomes `CLOSED` immediately when any of the following occurs:

- the action performs an unexpected repository mutation;
- the returned result is inconsistent with the documented action semantics;
- the action writes to an unexpected path, branch, ref, or object type;
- a reported successful mutation cannot be confirmed by readback;
- dynamic tool routing exposes a different action than the one that was explicitly verified;
- schema or endpoint behavior becomes ambiguous after rediscovery.

After the latch closes:

1. do not invoke that write action again during the checkpoint;
2. stop unrelated repository mutations;
3. identify the exact unexpected mutation and resulting commit, object, path, or ref;
4. restore repository content through the smallest authorized non-destructive corrective commit when restoration is required;
5. verify that the resulting repository tree matches the intended pre-incident state before resuming;
6. select a different write path only after explicitly verifying its current schema and side effect.

Do not treat successful cleanup as proof that the failed write path is safe again. A later checkpoint may reconsider the path only after fresh read-only capability verification.

## Git Data object distinction

Treat `create_blob`, `create_tree`, and `create_commit` as staging-object operations until a branch or tag ref is moved to make the commit reachable.

Treat `create_file`, `update_file`, `delete_file`, and `update_ref` as repository-publication mutations because they can immediately change reachable branch history or content.

Never substitute one class for the other merely because both appear to accept file content. Before using the Git Data fallback required by Rule 49, verify that each action in the sequence is the actual Git Data endpoint expected by that protocol.

## Existing-file byte preservation

When modifying an existing repository file, preserve all unrelated bytes, including trailing spaces, line endings, blank-line structure, Unicode normalization, and other representation details that may be invisible in rendered text.

For small files, fetch the current file and blob SHA immediately before editing and preserve unrelated content exactly.

For large files or connector responses that may normalize, truncate, or reformat text:

1. obtain a byte-faithful source representation from an immutable blob, commit, or equivalent content-preserving connector read;
2. verify the reconstructed pre-edit content against the expected Git blob SHA before applying the edit when technically possible;
3. apply only the intended surgical change;
4. build the candidate commit without publishing it when the available Git Data path permits;
5. reject the candidate if the diff shows unrelated whitespace churn, normalization, truncation, reordered text, or representation-only changes.

Connector payload limits never authorize rewriting a scientific or historical record into a normalized approximation.

## Candidate-diff gate

Before publishing a connector-built candidate commit, verify the exact changed-file set and the hunk-level scope.

For a one-file contents-API write, fetch the resulting commit immediately and confirm that only the intended file and content changed.

For an atomic Git Data checkpoint, follow Rule 49 exactly: create verified blobs, build one tree, create one commit on the frozen parent, compare the candidate against that parent, re-read the branch ref, and publish only by non-force fast-forward if the branch has not moved.

Unexpected changed files, unrelated hunks, formatting churn, or a branch race are hard publication stops.

## Post-write readback

Every connector mutation must be read back through an independent read operation appropriate to the mutation.

At minimum verify:

- repository;
- branch or ref;
- resulting commit SHA;
- changed paths;
- current blob SHA for changed files where applicable;
- exact intended content or diff scope;
- absence of unrelated mutations.

A generic success response is not sufficient evidence that the intended repository state exists.

## Incident chronology

An accidental connector mutation is a technical repository event, not a scientific result.

If it materially affects reproducibility, report chronology, or published evidence, record the event factually in the applicable durable research or engineering record. Do not hide it, but do not inflate it into scientific evidence.

Unreferenced staging blobs, trees, and commits are not retained scientific evidence unless a later durable checkpoint explicitly records and makes them part of the reproduction chain.

## Completion gate

A connector-backed checkpoint is not complete until all of the following are true:

1. the final branch ref is known;
2. the final commit and changed files have been read back;
3. the exact diff scope is verified;
4. every unexpected mutation has been either safely corrected or explicitly left unresolved with publication stopped;
5. no write-path latch violation was bypassed;
6. connector limitations and any unavailable local verification are stated plainly in the owner-facing summary.
