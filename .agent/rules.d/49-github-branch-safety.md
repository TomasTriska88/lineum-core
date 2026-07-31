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
