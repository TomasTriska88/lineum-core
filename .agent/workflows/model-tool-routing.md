# Lineum Model and Execution Routing

## Purpose

Use this workflow whenever deciding whether Lineum work should remain in ChatGPT or be proposed for execution in Codex. The routing decision is based on the kind of work required, not on the assumption that a higher reasoning-effort label guarantees a more correct answer.

Use the named current models when they are available. If product names or effort labels change, preserve the role definitions below and select the nearest available equivalent.

## ChatGPT-First Hard Gate

Lineum work stays in ChatGPT by default. The agent MUST NOT recommend Codex merely because Codex would be faster, more convenient, more automated, better at repository navigation, or capable of producing a larger implementation in one pass.

Before recommending Codex, the agent must first determine whether the required result can be produced reliably inside ChatGPT by using available reasoning, Python execution, file uploads, GitHub or other connected-source tools, web research, document analysis, or a smaller repository operation performed directly by the current agent. If it can, keep the work in ChatGPT.

Recommend Codex only when a concrete required step cannot be completed reliably in ChatGPT or by the current agent with available tools. Convenience, preference, task size, the presence of code, or a desire for extra confirmation is not sufficient. When only one bounded step crosses this boundary, delegate only that smallest step and retain all scientific reasoning, interpretation, and decisions in ChatGPT.

The burden of proof is therefore on switching to Codex, not on staying in ChatGPT.

## Default Roles

- **Primary Lineum workspace and scientific lead:** ChatGPT with GPT-5.6 Sol Pro. Use GPT-5.6 Sol Extra High as the fallback when Pro is unavailable.
- **Exceptional repository executor:** Codex with GPT-5.6 Sol Max, only after the ChatGPT-first hard gate is satisfied.
- **Exceptional parallel repository executor:** Codex Ultra, only when the hard gate is satisfied and the work is safely divisible into independent lanes with frozen inputs and explicit merge criteria.
- **Do not recommend Codex merely because a task is difficult, mathematical, scientific, large, or contains code.** Recommend it only when an indispensable repository-local execution requirement cannot be met reliably in ChatGPT.

ChatGPT owns the scientific question, assumptions, falsification criteria, interpretation, evidence strength, next-step selection, and claim wording. Codex may produce narrowly scoped repository-grounded evidence, code changes, tests, reproducible runs, or Git checkpoints when those cannot be produced reliably in ChatGPT. Codex output is evidence to evaluate, not an automatic scientific verdict.

## Keep the Work in ChatGPT

Keep the task in ChatGPT Sol Pro or Extra High whenever ChatGPT can complete it with sufficient reliability, including when its primary deliverable is any of the following:

1. Defining the research question, null hypothesis, competing mechanisms, assumptions, observables, controls, or falsification criteria.
2. Scientific, mathematical, physical, ontological, causal, statistical, or cross-disciplinary reasoning.
3. Detecting a faulty premise, circular definition, confounder, alternative explanation, scope error, or claim stronger than the evidence.
4. Interpreting simulation or test output and deciding whether a result is supported, constrained, unresolved, or falsified within a declared domain.
5. Comparing Lineum with empirical evidence, established models, contested models, or external literature.
6. Selecting the next discriminating experiment or deciding whether a mechanism should be promoted, retained, reopened, or rejected.
7. Writing or auditing scientific conclusions, whitepaper claims, investor-facing scientific language, or public explanations.
8. Performing analytic checks, dimensional checks, toy cases, statistics, plots, Monte Carlo runs, numerical integration, or prototype simulations that can be executed reliably in ChatGPT's Python environment.
9. Reading, searching, comparing, or making a small precise change to repository files through available GitHub or connected-source tools when local execution is not required.
10. Reviewing a Codex result, diff, report, or raw output for scientific validity.
11. Designing code, tests, commands, experiment specifications, migration plans, or repository edits that can be handed back as text without requiring immediate local execution.

Do not suggest Codex while a reliable ChatGPT path remains. A task involving multiple files, repository knowledge, or executable code still remains in ChatGPT when connected tools and Python are sufficient for the required evidence and change.

## Recommend Codex Max Only When ChatGPT Cannot Reliably Complete the Required Step

Recommend **Codex Max** only when at least one requirement below is indispensable and cannot be satisfied reliably by ChatGPT or the current agent's available tools:

1. The task requires a local checkout and direct modification of many interdependent files where connector-based edits would be unsafe or incomplete.
2. The result depends on the exact local package graph, generated files, uncommitted workspace state, build cache, operating-system environment, or repository-specific toolchain that ChatGPT cannot access.
3. The required evidence can only be obtained by running the real test suite, build, linter, type checker, benchmark, CI reproduction, development server, runtime smoke check, or interactive local application.
4. The calculation or simulation must import Lineum modules, use repository-only datasets, reproduce a historical checkout, or execute from a clean local environment unavailable to ChatGPT.
5. The experiment exceeds the practical ChatGPT execution boundary because it requires extended runtime, large memory, GPU or external tooling, extensive repeated orchestration, or outputs too large to produce reliably in ChatGPT.
6. The required implementation cannot be safely committed through available repository tools because it needs broad refactoring, generated artifacts, conflict resolution, or immediate local validation.
7. The task requires local Git operations that available GitHub tools cannot safely perform, such as resolving merge conflicts, manipulating worktrees, or validating uncommitted changes.
8. A repository-wide factual claim remains unresolved after using available ChatGPT repository search and reading tools and requires systematic local execution or indexing.

The presence of one of these categories is not enough by itself; the agent must state why the exact current step cannot be completed reliably in ChatGPT. Codex Max is the default Codex recommendation once that necessity is established. Do not recommend Ultra merely as a stronger-sounding setting.

## Recommend Codex Ultra Only for Necessary Safe Parallelism

Recommend **Codex Ultra** only when the ChatGPT-first hard gate is satisfied and all of the following are true:

1. The indispensable repository-local work contains at least three substantial lanes that can be executed independently.
2. Every lane can receive frozen inputs, an exact scope, and an explicit output contract.
3. Failure or bias in one lane will not silently contaminate the others.
4. The outputs can be checked separately before synthesis.
5. The final synthesis uses predetermined comparison or merge criteria.
6. A single Codex Max run would be materially less reliable or impractical, not merely slower.

Appropriate examples include separately auditing implementation, tests, and documentation when all require local execution; running independent simulation families over frozen parameter grids that exceed ChatGPT limits; searching distinct historical branches or variant families in local checkouts; or reproducing the same result through genuinely separate local implementations.

Do **not** recommend Ultra for a single theoretical derivation, one tightly coupled scientific argument, interpretation of one result, ontology selection, final claim wording, ordinary repository browsing, or any task where parallel agents would merely elaborate the same uncertain premise.

## Calculation and Simulation Boundary

ChatGPT is sufficient by default for analytic derivations, dimensional and unit checks, toy models with known answers, independent recalculation, numerical integration, Monte Carlo experiments, statistical analysis, plotting, and prototype ODE or PDE simulations that fit within its execution environment.

Keep scaling the work inside ChatGPT where practical by reducing the model, freezing a representative parameter set, sampling the space, batching inputs, or first running a smaller discriminating experiment. Recommend Codex Max only after these options are inadequate and the required result genuinely needs the real repository, local dependencies, extended runtime, large memory, GPU or external tooling, broad parameter sweeps, repeated command-line orchestration, durable generated artifacts, or integration that cannot be performed safely through available tools.

Regardless of tool, no decision-relevant numerical result is accepted from a single calculation path. Require at least one independent check such as an analytic sanity check, a toy case with a known output, a second implementation, a resolution or timestep convergence check, dimensional analysis, or reproduction with frozen inputs and seeds.

## Required Owner-Facing Recommendation

Do not burden the project owner with a long workflow explanation. Give exactly one clear routing sentence first:

- `Keep this in ChatGPT Sol Pro.`
- `This exact local repository step cannot be completed reliably in ChatGPT; run it in Codex Max.`
- `These necessary independent local lanes cannot be completed reliably in ChatGPT; run them in Codex Ultra.`

Then give one sentence naming the missing capability that makes Codex necessary. Never describe Codex as merely preferable when ChatGPT can still do the work reliably.

When recommending Codex, provide one copyable execution brief containing:

- the exact Codex mode;
- repository and branch, normally `TomasTriska88/lineum-core` on `develop`;
- the exact smallest goal and scientific question it serves;
- the specific capability unavailable in ChatGPT;
- files or directories to inspect or modify;
- commands, tests, simulations, or checks to run;
- required raw outputs and permanent artifacts;
- stop conditions and failure conditions;
- conclusions Codex is not authorized to make;
- the return package: commit SHA when applicable, changed-file list, diff summary, commands executed, raw results, failed checks, limitations, and remaining uncommitted work.

Never give a vague instruction such as `try this in Codex`. Recommend only the smallest repository-local execution package that cannot be completed as reliably in ChatGPT.

## Mixed Tasks

For a mixed scientific and repository task, keep the entire task in ChatGPT unless one exact indispensable execution step crosses the hard boundary. When it does, retain the scientific reasoning and all other work in ChatGPT and delegate only that smallest repository-execution slice. Avoid repeated handoffs and do not create ceremony for small tasks. A single bounded Codex run should obtain or implement only the missing evidence, after which ChatGPT evaluates what the evidence means.

If repository work can be completed directly and safely by the current agent with available tools, follow Rule 14 in `.agent/rules.md` and do it rather than delegating it to the owner. This workflow governs owner-facing model recommendations; it does not excuse an agent from using its own available tools.