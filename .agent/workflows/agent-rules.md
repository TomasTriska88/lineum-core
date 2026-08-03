# Agent Communication, Research Capture, and Canon Synchronization

These rules are binding for agents operating in this repository. They complement `.agent/rules.md`, `.agent/continuous-research-reporting.md`, and `.agent/workflows/model-tool-routing.md`.

## 1. Direct project-owner communication

Codex communicates directly with the project owner. There is no required external ChatGPT supervisor or handoff loop.

Put owner-facing conclusions, questions, progress updates, requested copyable text, and final checkpoint summaries directly in the chat. Do not force the owner to retrieve ordinary communication from a generated temporary file.

Permanent scientific evidence, methods, outputs, decisions, and provenance still belong in the active version-controlled report under `research/`; chat is not a substitute for the durable record.

## 2. Report-first scientific capture

The active standalone research report is the live scientific source of truth during an investigation.

Before a consequential experiment or decision, record the frozen question, assumptions, variants, equations, units, parameters, controls, observers, metrics, success and failure criteria, and outcome interpretations in the report.

After the step, record the command or procedure, machine-readable and human-readable results, independent checks, negative results, contradictions, limitations, prohibited over-interpretations, and next discriminator before beginning another consequential step.

Do not defer a sequence of decision-relevant results for later reconstruction from chat or terminal history.

## 3. Whitepaper promotion, not automatic synchronization

Whitepapers are canonical claim surfaces, not chronological scratchpads and not the first destination for new ideas.

Do not automatically copy discussions, analogies, exploratory findings, provisional mechanisms, or bounded negative results into a whitepaper merely because they were interesting or newly observed.

Update a whitepaper only when the exact bounded claim has passed the applicable evidence and promotion gates:

- the active report is current, standalone, and reproducible;
- the implementation and observations are distinguished from interpretation and hypothesis;
- independent checks and conflicting evidence are recorded;
- the claim scope, confidence, limitations, and evidence cutoff are explicit;
- the change is consistent with repository boundaries and the current implemented behavior.

When a whitepaper change is justified, derive it from the report's promotion table. Preserve earlier research history rather than rewriting it to match the new canon.

A lay or lore document may be updated only with the same evidence status clearly translated; it must not turn a hypothesis into a physical fact.

## 4. Mandatory contextual retrieval

Before programming, investigating, auditing, selecting a replacement mechanism, or interpreting a new result, search the complete relevant repository context rather than treating the newest prompt as isolated.

Retrieve the applicable rules, root and child research reports, code, tests, whitepapers, historical variants, rejected paths, open contradictions, and permanent project knowledge. Search connected Lineum repositories only when the task requires cross-repository context and respect the declared repository boundaries.

Do not use `.scratch/` as historical provenance. It is disposable and non-evidentiary.

Previously recorded ideas are provenance and candidate hypotheses, not validation. Identify contradictions, deprecated formulations, circular observers, and unsupported claims before reusing them.

## 5. Ultra lead and reviewer structure

Use the fixed Ultra configuration defined in `.agent/workflows/model-tool-routing.md`.

One lead agent owns the active question, frozen protocol, report, final synthesis, and repository diff. Supporting agents receive narrow, independently auditable checks. They must not write concurrently to overlapping paths or produce competing final edits.

Do not decide by agent voting. Preserve disagreements, identify the first technical divergence, and resolve them with the cheapest frozen discriminating check. If the evidence cannot decide, record the contradiction as unresolved.

## 6. Progress visibility for long-running execution

Long-running calculations, simulations, builds, and data-processing scripts must provide readable progress rather than acting as silent black boxes.

For Python evaluation scripts, use unbuffered execution (`python -u`) and emit periodic newline-delimited progress containing the current phase, completed and total work, percentage when meaningful, and an evidence-based ETA when one can be estimated responsibly.

Do not fabricate an ETA before enough progress exists to estimate it. When runtime is highly variable, report completed work and current phase without false precision.

Prefer coarse, stable progress intervals over terminal output based on carriage returns that may be lost in remote logs.

## 7. Diagnostic telemetry for heavy simulations

Heavy PDE, ODE, parameter-sweep, optimization, or loop-intensive runs must expose checkpoints sufficient to distinguish active computation from a hang.

Log the current lane, parameter group, step or batch, total target, and any detected numerical failure. Preserve decision-relevant failure messages and partial results in the active report when they affect interpretation.

Telemetry is operational evidence, not scientific proof. A run completing successfully does not validate its metric or interpretation.

## 8. Reproduction completeness

Every retained empirical conclusion must be reproducible from the active report without relying on hidden notebook state, chat memory, or a disposable script.

Include the evaluated equation or algorithm, full material parameters, units, grid and domain, timestep or tolerance, number of steps, seeds, boundary and initial conditions, software environment, command, outputs, metric definition, controls, and known failure conditions.

Whitepapers may summarize validated results, but essential reproduction detail remains in the standalone research report. Include sufficient localized detail in a whitepaper when the canonical claim would otherwise be ambiguous, while avoiding duplication that can drift independently.

## 9. Planning and approval

Plans must be understandable in the chat and must identify the goal, evidence required, files affected, tests or calculations, stop conditions, and expected durable artifacts.

A clear direct instruction from the project owner authorizes the described non-destructive work within existing repository rules. Do not require a second approval merely because an obsolete supervisor workflow previously existed.

Questions, negative-result owner gates, destructive operations, credential requirements, and material owner decisions remain blocking under `.agent/rules.md`.

## 10. Diff and checkpoint reporting

After a documentation or code checkpoint, summarize the actual diff in the chat at a useful level of detail. For canonical scientific changes, state the supporting report and evidence status.

Do not claim tests, builds, simulations, runtime checks, connector synchronization, or external review that did not occur.

The final checkpoint summary must include the repository, branch, commit SHA, changed files, checks performed, limitations, unresolved conflicts, and any work that remains uncommitted or unsynchronized.

## 11. English-only repository content

All code, comments, configurations, tests, logs, commit messages, and documentation written into the repository must be in English, except for deliberately localized user-visible strings or exact official terms where the repository permits them.

## 12. No external LLM API calls in tests or tooling

Do not write or run tests, utility scripts, development scripts, or Git hooks that invoke live external LLM APIs. Use deterministic offline checks or mocks for integrations. Never consume live OpenAI, Gemini, or other LLM API credentials during repository testing or automation.
