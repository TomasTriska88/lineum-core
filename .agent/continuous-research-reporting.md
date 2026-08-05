# Mandatory Continuous Research Report Protocol

**Status:** mandatory supplement to `.agent/rules.md`

This protocol makes the active standalone research report the live source of truth throughout a research lane, not a retrospective summary written after several experiments.

## Durable cross-session laboratory notebook

The active standalone report is the persistent laboratory notebook and continuity record for the research programme across conversations, agents, machines, and work sessions. A later researcher must be able to resume the exact next step from the report and Git history without relying on chat memory, private reasoning, terminal scrollback, or uncommitted local files.

Record as much decision-relevant history as is needed to preserve the true research path, including:

- successful, negative, null, contradictory, inconclusive, and partially completed results;
- failed execution attempts, crashes, serialization or storage failures, environment defects, dependency problems, invalid metrics, checker defects, and lost or unretained outputs;
- implementation-audit findings, corrections to the measuring harness, and why each correction does or does not alter scientific meaning;
- owner corrections, hypotheses, analogies, constraints, and decisions, kept distinct from agent formalization and experimental evidence;
- abandoned, rejected, dormant, superseded, and reopened variants with the reason and reopen condition;
- what was not tested, what evidence was not retained, and what conclusion is therefore prohibited;
- the exact next concrete step and why it is the cheapest useful discriminator.

Do not compress the history into a smooth success narrative. Preserve chronology. When a later correction changes an earlier statement, append or clearly mark the correction and its effect instead of silently rewriting the earlier event as though the mistake never happened.

Always distinguish:

1. a technical execution failure that produced no admissible scientific evidence;
2. a methodological failure that invalidated a metric, observer, protocol, or retained result;
3. a reproducible scientific negative or null result;
4. an interpretation or hypothesis proposed after the evidence.

An execution that completed in memory but failed to retain a verifiable output is not a retained scientific result. Record the attempt, failure mode, any information that can be established safely, and the requirement for a complete rerun.

## Continuous update requirement

For every decision-relevant research lane, identify one active Markdown report under `research/` before performing the next consequential action. Update that same report continuously throughout the lane.

A consequential research step includes selecting or changing a hypothesis, mechanism, equation, parameter set, observer, metric, control, intervention, seed, boundary, execution path, interpretation, status, next discriminator, or architectural placement.

Before executing such a step, append or revise the active report to record:

- the exact question or hypothesis being tested;
- the owner idea, prior evidence, or failure that motivated it;
- the proposed mechanism in operational terms;
- all planned lanes, controls, interventions, parameters, seeds, metrics, and falsification criteria;
- what each possible outcome would mean;
- the current evidence status and unresolved risks.

After executing the step, and before beginning another consequential step, update the active report with:

- the exact command or procedure performed;
- machine-readable and human-readable results;
- independent checks and environment limitations;
- what passed, failed, remained ambiguous, or was not tested;
- the narrow interpretation and prohibited over-interpretations;
- the impact on the variant ledger, prior conclusions, and next discriminator.

## Owner decisions and failure-gate responses

Any project-owner hypothesis, analogy, correction, architectural constraint, or response at a negative-result gate must be recorded in the active report before it is translated into code or a new experiment. Preserve the owner's idea distinctly from the agent's formalization and from experimental evidence.

## Root programme and report hierarchy

A child research lane never becomes an isolated source of truth merely because it is the currently active report.

For every decision-relevant child report:

- declare the exact root or master report path, its version, and its evidence cutoff;
- declare the full report lineage from the root programme through every immediate predecessor;
- before selecting, replacing, ranking, or rejecting a mechanism, re-read the root report and recover all inherited positive results, negative results, contradictions, open variants, stop conditions, and deferred gates that can affect the decision;
- restate every decision-relevant inherited premise inside the child report or its mandatory continuity ledger so that the child remains auditable without pretending that recent work reset the programme;
- maintain both a local verdict and a root-programme impact matrix using `supports`, `contradicts`, `constrains`, `depends_on`, `reopens`, `observationally_equivalent`, `unaffected`, or `not_yet_compared`;
- choose the next discriminator by its value across the complete programme, not merely by proximity to the newest experiment, metaphor, or report;
- preserve older and incompatible equation families as separate variants rather than silently narrowing the programme to the latest candidate.

When the root report is too large to re-read as one tool response, retrieve it by immutable blob or bounded sections, identify the sections relevant to the current decision, and explicitly register every material family that remains `not_yet_compared`. A ClickUp task, chat summary, child report, or whitepaper is not a substitute for the root scientific record.

A child lane is not ready for a consequential experiment while its report chain cannot explain how the proposed action follows from the complete inherited programme rather than only from recent work.

## Whitepaper handoff

When the project owner designates an active report as the future source for whitepaper updates, record that purpose in the report immediately. Maintain a live whitepaper handoff section that separates:

- validated statements eligible for canonical wording;
- bounded negative results that constrain or supersede prior claims;
- hypotheses and analogies that must remain explicitly non-canonical;
- implementation facts that describe software behavior but not physical reality;
- unresolved contradictions, limitations, evidence cutoffs, and required citations;
- exact whitepaper sections or claims likely to be affected, once repository retrieval identifies them.

Do not update a whitepaper from chat memory, a script, or a final summary while the designated report is incomplete. On completion, derive every whitepaper change from the report's evidence and promotion table, preserve scope and uncertainty, and never promote a research hypothesis merely because the report is finished.

## No deferred batching

Do not run a sequence of consequential experiments and plan to document them afterward. Do not allow code, chat, `.scratch/`, terminal history, or an external task system to become temporarily more authoritative than the active report.

Mechanical actions that do not change scientific meaning—such as reading a file, listing paths, formatting unchanged text, or verifying that a committed file exists—do not require a separate report revision. However, any discovery from those actions that changes scope, assumptions, protocol, interpretation, or the next step must be recorded immediately.

## Scratch is local and non-evidentiary

`.scratch/` is a temporary local Codex workspace, ignored by Git and not expected to be visible through GitHub, repository connectors, CI, another checkout, or a later session.

Therefore:

- never query GitHub or a repository connector for `.scratch/` contents as part of provenance reconstruction;
- never count a `.scratch/` `404`, missing path, or absent filename as a receipt, negative result, or evidence that an experiment did not occur;
- treat a committed mention of a `.scratch/` filename only as an `unversioned_local_reference`, not as recovered code or output;
- exclude repository-presence cells for `.scratch/` from provenance matrices and receipt totals;
- correct any prior report that counted scratch-path absence as evidence, preserving the methodological correction in the report history;
- promote all retained evidence into the active standalone report or another explicitly permanent research-scoped path before the next consequential lane.

The binding operational details are in `.agent/workflows/scratch.md`.

## Git checkpoint cadence and chronology

Git is the durable timeline of the research lane. Create a checkpoint immediately after every meaningful, independently reviewable step and before beginning the next consequential step. Do not postpone all commits until the end of a long session.

Meaningful checkpoints include, when applicable:

- scope lock, intake, or preregistration;
- implementation audit and identified measurement defects;
- frozen runner, checker, tests, equations, metrics, thresholds, and source snapshot before official execution;
- every failed or aborted execution whose cause, lost evidence, or repair affects reproducibility;
- each technical or methodological correction made after an attempted execution;
- the primary retained result before interpretation-driven mechanism changes;
- the independent verification, including a failed checker and its correction;
- the narrow interpretation, variant-ledger update, owner decision, and next frozen discriminator.

Do not combine distinct steps into one final commit when doing so would erase their true temporal or decision sequence. Code, raw outputs, tests, and the updated report should be committed together when they form one coherent experiment checkpoint. A commit must not mix an equation or threshold change with the result produced under a different version unless the report and diff preserve the exact boundary unambiguously.

An official retained execution must begin from a committed protocol and committed executable harness. If execution occurs from uncommitted files, classify it as exploratory or provenance-defective, do not promote it as final evidence, record the lapse, commit the frozen materials, and rerun from the initial state when reproducibility requires it.

Commit a retained result before using it to select a replacement mechanism, tune parameters, alter a metric, or begin the next research lane. A later polished rewrite may improve clarity but must not erase chronological evidence, failed paths, technical failures, or decision rationale.

If checkpoints were missed, stop further consequential research. Reconstruct the chronology from available hashes, files, timestamps, commands, outputs, and chat only to the extent supportable; state what cannot be proven; do not fabricate that a commit existed before an execution; then restore normal checkpoint cadence before continuing.

## Hard gate

If the active report and Git history are not current enough to explain the exact next action without relying on chat history or uncommitted scratch material, stop and update and commit them first.
