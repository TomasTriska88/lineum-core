# Local Scientific Execution First

**Status:** Binding supplement to `.agent/rules.md`.

## Purpose

This rule keeps scientific execution close to the active research workspace and prevents GitHub Actions from becoming a general-purpose remote calculator, transport workaround, or iterative debugging shell.

## Default execution location

Run calculations, simulations, tests, checkers, data transformations, and report-generation steps locally whenever a suitable local checkout, container, notebook runtime, or execution tool is available.

Use GitHub for version control, review, durable evidence, release automation, and genuine continuous integration. Do not create or repeatedly revise workflows merely to execute an ordinary calculation that can run in the active workspace.

## GitHub Actions exception gate

GitHub Actions may execute scientific or verification work only when at least one of these conditions is explicitly satisfied:

1. the task is genuinely a CI regression check triggered by repository changes;
2. the claim depends on reproducing behavior in the declared GitHub-hosted environment;
3. the local environment cannot perform the frozen execution and the limitation is recorded before the workflow is created;
4. an independently justified remote environment is part of the preregistered verification design.

Convenience, connector payload limits, absence of a local Git remote, or a desire to avoid moving a small input locally are not sufficient reasons.

Before publishing an execution workflow, validate its YAML and embedded scripts locally or with a non-executing parser whenever the available environment permits. Freeze its inputs, expected outputs, dependency versions, failure behavior, and cleanup path before the first official run.

## Evidence and publication boundary

The active workspace performs the computation. Git records the frozen inputs, executable method, machine-readable output, hashes, environment receipt, interpretation, and reproduction instructions.

Do not use commits, workflow definitions, issues, comments, releases, or Actions artifacts as an improvised transport layer for temporary code or data. Temporary execution material belongs in `.scratch/`; every retained decision-relevant result must be copied into the active standalone report before the next consequential research step.

A workflow created for an exceptional one-use verification must be narrowly scoped, fail closed, and be removed in the same coherent checkpoint as its retained result, unless it has lasting CI value documented in the repository.

## Failure handling

A workflow rejected before job creation is a technical execution failure and not a scientific run. Record it only when it affects reproducibility or chronology, remove the invalid workflow promptly, and return to local execution instead of iterating through speculative workflow commits.

Do not claim that a checker, simulation, or test ran merely because a workflow commit or run record exists. Verify that the scientific command was actually invoked and that a retained output passed its declared integrity checks.
