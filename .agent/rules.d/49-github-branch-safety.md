# GitHub Branch Creation Safety

**Status:** Binding supplement to `.agent/rules.md`.

## Purpose

Repository discovery and verification must be read-only. Creating a branch is a repository mutation and must never be used as a probe for branch existence, connector capability, repository state, or ref resolution.

## Read-only branch discovery

Use only read-only operations when checking branches, refs, commits, or file availability, including:

- branch search or branch listing;
- repository metadata lookup;
- file fetches against an explicit ref;
- commit lookup;
- commit or ref comparison.

Never call `create_branch`, `update_ref`, `create_commit`, `create_tree`, `create_blob`, or another write operation merely to test whether a branch, ref, permission, or connector capability exists.

A failed branch-creation call such as `Reference already exists` is not an acceptable discovery method. Resolve the branch with a read-only operation instead.

## Branch-creation gate

A branch may be created only when the current deliverable genuinely requires a dedicated branch or another binding repository rule explicitly requires one.

Before any branch-creation call, record and verify all of the following:

1. exact repository;
2. exact base branch or immutable base commit SHA;
3. exact task-scoped branch name;
4. concrete reason that the change must not be committed directly to the normal development branch;
5. intended files or operations on the branch;
6. publication or merge path;
7. cleanup responsibility;
8. an available and authorized way to remove the branch if creation succeeds but the planned work is abandoned.

If any item is unknown, do not create the branch.

If the available connector or environment cannot delete an unintended or temporary branch, temporary branch creation is forbidden.

## Lineum Core default

The normal development branch for `TomasTriska88/lineum-core` is `develop` unless the project owner explicitly selects another branch.

Small, precise, reversible connector changes should be committed directly to `develop` when permitted by `.agent/rules.md`. Do not create an intermediate branch solely for verification, documentation-only edits, connector experimentation, or perceived cleanliness.

A dedicated branch is justified only by concrete risk, repository policy, required review, broad interdependent changes, or another explicit workflow requirement.

## Atomic multi-file connector fallback

Use ordinary local Git staging and committing whenever a usable local checkout and authenticated remote are available.

When local Git publication is unavailable and several interdependent files must enter history as one coherent checkpoint, use the Git Data API sequence `create_blob -> create_tree -> create_commit -> compare_commits -> update_ref`.

For this fallback:

1. fetch and freeze the current development-branch commit and base tree;
2. create one blob for each exact, already verified file content;
3. build one tree on the frozen base tree containing only the intended paths and modes;
4. create one commit whose sole parent is the frozen development-branch commit;
5. compare the candidate commit against its parent and verify the exact changed-file set, statuses, and scope before publication;
6. re-read the development ref immediately before publication and abort if it moved;
7. move the ref only as a non-force fast-forward;
8. fetch the published commit and changed files to verify the final state.

Do not use `create_file` or `update_file` sequentially for a logically atomic multi-file checkpoint when their intermediate commits would be incomplete, misleading, or non-runnable. Unreferenced blobs and trees are staging objects, not published evidence. Never use issues, comments, workflow runs, releases, or external artifacts as a transport layer for repository file content.

### Large standalone report transport

A permanent standalone report must remain one complete Markdown document even when connector payload limits make its direct blob upload unreliable.

Before changing its packaging, first try the ordinary verified blob path. If the connector rejects or corrupts the payload, preserve the readable current conclusions, protocol, failures, reproduction instructions, and exact next action directly in the Markdown file, and place the complete remaining diary and executable material in a lossless archive embedded inside that same Markdown file. The archive must use documented standard-library extraction code, a manifest of every member, cryptographic hashes for the archive and members, and a permanent test that proves both loader-based and report-only extraction paths.

Packaging may remove only redundant transport encodings or duplicated compressed wrappers. It must not remove, summarize away, or silently rewrite scientific content, chronology, negative results, equations, parameters, thresholds, metrics, source code, or machine-readable evidence. Record every failed upload, rejected blob, capsule-loader defect, and packaging correction in the active report before publication.

Prefer small convenience loaders that extract and hash the canonical executable files from the standalone report over duplicating large compressed payloads in separate `.py` mirrors. The report remains the authority; convenience files must fail closed on a hash mismatch.

## Naming and scope

Do not create generic remote branches such as:

- `tmp`;
- `test`;
- `scratch`;
- `probe`;
- `experiment` without a specific research identifier.

Every new branch must have a descriptive task-scoped name and a declared purpose before creation.

## Post-creation verification

Immediately after an authorized branch is created:

1. verify that it points to the intended base commit;
2. verify that no file or history change occurred beyond the new ref;
3. continue only with the declared branch scope.

If a branch is created unintentionally, stop unrelated repository writes, report the exact branch and cause, and remove it through an authorized safe method before resuming when deletion capability is available. Never hide, reuse, or silently repurpose an accidental branch.

## Protected history

Never force-update, repoint, or delete shared branches such as `develop` or `main`. Never use branch operations to rewrite shared history. Branch deletion outside an explicitly authorized cleanup action remains prohibited by the autonomous publication rules.
