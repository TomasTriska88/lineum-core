# Mandatory Continuous Research Report Protocol

**Status:** mandatory supplement to `.agent/rules.md`

This protocol makes the active standalone research report the live source of truth throughout a research lane, not a retrospective summary written after several experiments.

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

## Git checkpoint cadence

The report may receive several small edits within one coherent local work session, but every independently retained result or owner-approved mechanism decision must be committed to the development branch before the next research lane begins. A later polished rewrite may improve clarity but must not erase the chronological evidence, failed paths, or decision rationale.

## Hard gate

If the active report is not current enough to explain the exact next action without relying on chat history or uncommitted scratch material, stop and update the report first.
