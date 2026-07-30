# Lineum Core Library Distribution Contract

## Scope

`lineum-core` is the reusable, application-neutral physics library shared by Lina EI and future independent Lineum applications. It owns generic field laws, solver primitives, numerical contracts, state contracts, and reproducible physics experiments. It must not import or encode Lina-specific identity, personality, prompts, cognition, memory, relationships, embodiment, devices, integrations, local state, or product policy.

The dependency direction is one-way: applications depend on a released Lineum Core contract. Lineum Core never depends on an application.

## Version Source

`lineum_core/_version.py` is the single package-version source. Package metadata, runtime `lineum_core.__version__`, wheel names, release tags, and downstream manifests must agree with it. A release tag that differs from `v<package-version>` fails the release workflow.

## Release Artifact

Every tagged release builds a pure-Python wheel and verifies that it can be installed and imported before attaching it to the GitHub release beside the scientific reference pack. A release is not a valid library update until its wheel and physics evidence gates pass.

Downstream applications pin an immutable release artifact or source commit. They must not follow a moving branch or silently select the newest available version. Updating an application means changing its one dependency manifest, running its compatibility and physics replay gates, and then intentionally accepting the new lock.

## Development Override

A developer may explicitly install a local checkout in editable mode. Local paths are machine-specific overrides and must never be stored as product defaults. Experimental behavior from an editable checkout remains development evidence until it is released, pinned, and replayed through the same public contract used by clean installations.
