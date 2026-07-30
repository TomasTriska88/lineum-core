# Mandatory Library Promotion Gate

**Status:** mandatory supplement to `.agent/rules.md`

**Binding source:** `docs/repository-boundaries.md`, section `Public Library Promotion Gate`

This rule exists to prevent experimental research architecture from being published prematurely as part of the reusable `lineum_core/` package.

## Required classification before writing code

Before creating or moving any file under `lineum_core/`, classify the proposed change as exactly one of:

1. established library behavior or a verified defect fix;
2. general application-neutral infrastructure required by multiple validated use cases;
3. research hypothesis, provisional decomposition, experiment-specific helper, initializer, metric, lane, adapter, or runner.

Category 3 is forbidden under `lineum_core/`.

If the classification is ambiguous, treat the change as category 3 and keep it outside the installable package.

## Correct destinations

- Disposable exploration, intermediate scripts, and diagnostic output belong in `.scratch/`.
- Decision-relevant methods, executable verification code, inputs, and outputs belong in the standalone Markdown report under `research/`.
- A permanent separately executable research tool may exist outside `lineum_core/` only when it has a clear research scope, stable provenance, documented purpose, and independent justification beyond avoiding code in the report.
- Regression tests belong under `tests/`, but a passing test does not make experiment code suitable for the public library.

## Promotion requirements

Research code may move into `lineum_core/` only after an explicit promotion checkpoint establishes all of the following:

- a concrete public-library use case independent of the originating experiment;
- application-neutral naming and semantics;
- no unvalidated ontology, scientific interpretation, or provisional research decomposition encoded as architecture;
- reviewed API and compatibility consequences;
- supported-environment regression tests;
- a durable record explaining why the capability belongs in the installable package;
- explicit project-owner approval when the change introduces a new interpretation-bearing public concept.

Technical reusability alone is insufficient. "This helper could be imported elsewhere" is never a promotion argument by itself.

## Mandatory pre-commit check

For every new or moved path under `lineum_core/`, the agent must state in its internal scope check:

- the category assigned above;
- the validated non-experimental use cases;
- why a research-scoped location is insufficient;
- which promotion evidence and tests authorize public-package placement.

If any answer is missing, do not commit the file under `lineum_core/`.

## Accidental-placement response

If experiment-specific code is discovered inside `lineum_core/`:

1. stop extending or depending on that placement;
2. preserve the research record and Git history;
3. remove or relocate the module in the next coherent checkpoint;
4. retain it in the package only if it independently passes the full promotion gate.
