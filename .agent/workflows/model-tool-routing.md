# Lineum Model and Execution Routing

## Purpose

Use this workflow whenever deciding whether Lineum work should remain in ChatGPT or be proposed for execution in Codex. The routing decision is based on the kind of work required, not on the assumption that a higher reasoning-effort label guarantees a more correct answer.

Use the named current models when they are available. If product names or effort labels change, preserve the role definitions below and select the nearest available equivalent.

## Default Roles

- **Scientific lead:** ChatGPT with GPT-5.6 Sol Pro. Use GPT-5.6 Sol Extra High as the fallback when Pro is unavailable.
- **Repository executor:** Codex with GPT-5.6 Sol Max.
- **Parallel repository executor:** Codex Ultra, but only when the work is safely divisible into independent lanes with frozen inputs and explicit merge criteria.
- **Do not recommend Codex merely because a task is difficult, mathematical, scientific, or contains code.** Recommend it only when repository-local execution materially improves the evidence or delivery.

ChatGPT owns the scientific question, assumptions, falsification criteria, interpretation, evidence strength, and claim wording. Codex produces repository-grounded evidence, code changes, tests, reproducible runs, and Git checkpoints. Codex output is evidence to evaluate, not an automatic scientific verdict.

## Keep the Work in ChatGPT

Keep the task in ChatGPT Sol Pro or Extra High when its primary deliverable is any of the following:

1. Defining the research question, null hypothesis, competing mechanisms, assumptions, observables, controls, or falsification criteria.
2. Scientific, mathematical, physical, ontological, causal, statistical, or cross-disciplinary reasoning.
3. Detecting a faulty premise, circular definition, confounder, alternative explanation, scope error, or claim stronger than the evidence.
4. Interpreting simulation or test output and deciding whether a result is supported, constrained, unresolved, or falsified within a declared domain.
5. Comparing Lineum with empirical evidence, established models, contested models, or external literature.
6. Selecting the next discriminating experiment or deciding whether a mechanism should be promoted, retained, reopened, or rejected.
7. Writing or auditing scientific conclusions, whitepaper claims, investor-facing scientific language, or public explanations.
8. Performing analytic checks, dimensional checks, toy cases, statistics, plots, moderate Monte Carlo runs, or moderate prototype simulations that can be executed reliably in ChatGPT's Python environment without repository-local dependencies.
9. Reviewing a Codex result, diff, report, or raw output for scientific validity.

For these tasks, do not suggest a switch to Codex unless a concrete repository-local requirement from the next section is present.

## Recommend Codex Max

Recommend **Codex Max** when one or more of these requirements materially applies:

1. The task requires direct inspection or modification of many repository files, dependency tracing, refactoring, migration, or synchronization across code, tests, and documentation.
2. The answer depends on the exact current implementation, local package graph, build system, configuration, generated schema, or repository-specific command-line environment.
3. The task requires running the real test suite, build, linter, type checker, benchmark, CI reproduction, development server, or runtime smoke checks.
4. The calculation or simulation must import Lineum modules, use repository datasets, reproduce a historical commit, or run from a clean checkout.
5. The experiment needs long runtime, large memory, many parameter combinations, repeated seeds, extensive file outputs, or tools unavailable in the ChatGPT Python environment.
6. The result must be integrated into permanent repository code, tests, standalone research reports, machine-readable outputs, or Git history.
7. The task requires branch, commit, diff, merge-conflict, release, or other Git operations.
8. A repository-wide factual claim cannot be supported by the files accessible in the current ChatGPT context and must be established by systematic local search or execution.

Codex Max is the default Codex recommendation for Lineum. Do not recommend Ultra merely as a stronger-sounding setting.

## Recommend Codex Ultra Only for Safe Parallelism

Recommend **Codex Ultra** only when all of the following are true:

1. The work contains at least three substantial lanes that can be executed independently.
2. Every lane can receive frozen inputs, an exact scope, and an explicit output contract.
3. Failure or bias in one lane will not silently contaminate the others.
4. The outputs can be checked separately before synthesis.
5. The final synthesis uses predetermined comparison or merge criteria.

Appropriate examples include separately auditing implementation, tests, and documentation; running independent simulation families over frozen parameter grids; searching distinct historical branches or variant families; or reproducing the same result through genuinely separate implementations.

Do **not** recommend Ultra for a single theoretical derivation, one tightly coupled scientific argument, interpretation of one result, ontology selection, final claim wording, or any task where parallel agents would merely elaborate the same uncertain premise.

## Calculation and Simulation Boundary

ChatGPT is sufficient by default for analytic derivations, dimensional and unit checks, toy models with known answers, independent recalculation, moderate numerical integration, moderate Monte Carlo experiments, statistical analysis, plotting, and prototype ODE or PDE simulations.

Recommend Codex Max only when the calculation requires the real repository, local dependencies, extended runtime, large memory, GPU or external tooling, broad parameter sweeps, repeated command-line orchestration, durable artifacts, or integration into tests and reports.

Regardless of tool, no decision-relevant numerical result is accepted from a single calculation path. Require at least one independent check such as an analytic sanity check, a toy case with a known output, a second implementation, a resolution or timestep convergence check, dimensional analysis, or reproduction with frozen inputs and seeds.

## Required Owner-Facing Recommendation

Do not burden the project owner with a long workflow explanation. Give exactly one clear routing sentence first:

- `Keep this in ChatGPT Sol Pro.`
- `Run this repository step in Codex Max.`
- `Run these independent lanes in Codex Ultra.`

Then give one sentence explaining the concrete reason.

When recommending Codex, provide one copyable execution brief containing:

- the exact Codex mode;
- repository and branch, normally `TomasTriska88/lineum-core` on `develop`;
- the exact goal and scientific question it serves;
- files or directories to inspect or modify;
- commands, tests, simulations, or checks to run;
- required raw outputs and permanent artifacts;
- stop conditions and failure conditions;
- conclusions Codex is not authorized to make;
- the return package: commit SHA when applicable, changed-file list, diff summary, commands executed, raw results, failed checks, limitations, and remaining uncommitted work.

Never give a vague instruction such as `try this in Codex`. Recommend only the smallest repository-local execution package that ChatGPT cannot perform as reliably itself.

## Mixed Tasks

For a mixed scientific and repository task, keep the scientific reasoning in ChatGPT and recommend only the exact repository-execution slice for Codex. Avoid repeated handoffs and do not create ceremony for small tasks. A single Codex run should gather or implement the required evidence, after which ChatGPT evaluates what the evidence means.

If the repository work can be completed directly and safely by the current agent with available tools, follow Rule 14 in `.agent/rules.md` and do it rather than delegating it to the owner. This workflow governs owner-facing model recommendations; it does not excuse an agent from using its own available tools.