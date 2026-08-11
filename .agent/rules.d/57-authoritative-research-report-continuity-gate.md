# Authoritative Research Report Continuity Gate

**Status:** Binding supplement to `.agent/rules.md`.

## Purpose

The active standalone Markdown report under `research/` is the authoritative continuity record for every ongoing Lineum research programme. The repository must remain sufficient for a new conversation, agent, machine, or work session to resume the exact scientific state without relying on chat history, private reasoning, terminal scrollback, temporary files, or remembered context.

This rule strengthens the continuous-reporting, permanent-history, single-report, Git-first, and checkpoint requirements already defined by `.agent/rules.md`, `.agent/continuous-research-reporting.md`, and Rules 50, 53, and 54.

## Hard report-before-progress gate

No consequential scientific or research step may begin until the immediately preceding decision-relevant state is present in the authoritative active Markdown report and committed to Git.

Decision-relevant state includes, at minimum:

- the question or hypothesis that was considered;
- source or implementation findings that change the scope;
- successful, negative, null, contradictory, inconclusive, or partially completed results;
- methodological or execution failures that affect reproducibility;
- owner corrections, constraints, hypotheses, or decisions that affect the programme;
- the narrow interpretation of the evidence;
- prohibited over-interpretations;
- affected prior conclusions or open variants;
- unresolved uncertainty and blockers;
- the exact next scientific step and why it follows from the retained evidence.

The sequence is mandatory:

```text
consequential result or decision
-> update authoritative active report
-> verify report content and Git checkpoint
-> only then begin the next consequential research step
```

Do not batch several consequential steps and document them afterward.

## Persistence failure is a research hard stop

If the authoritative report cannot be updated and safely committed for any technical reason, the scientific lane is paused immediately.

Examples include:

- connector truncation or payload limits;
- inability to obtain byte-faithful content for a large existing report;
- unavailable local Git publication path;
- branch races or uncertain current HEAD;
- write-action ambiguity or a closed GitHub write-path latch;
- inability to preserve unrelated report bytes;
- repository access, authorization, storage, or serialization failure;
- any other condition that prevents a verified durable report checkpoint.

While this gate is closed, the agent may perform only work necessary to restore durable continuity, such as read-only retrieval, repository-state verification, safe report reconstruction, write-path recovery, candidate-diff verification, or another directly related persistence repair.

The agent MUST NOT while the gate is closed:

- begin a new scientific experiment;
- select or rank a new mechanism;
- extend the interpretation into a new hypothesis lane;
- tune parameters or metrics based on the unretained result;
- modify Core equations or whitepapers from that result;
- treat chat memory as temporary scientific authority;
- move to another consequential research question merely to keep making progress.

A technical inability to write the report is therefore a blocking research-infrastructure problem, not permission to continue scientifically and document later.

## Companion artifacts never substitute for the active report

Plain companion artifacts such as `.json`, `.csv`, `.txt`, `.py`, or `.jsonl` may preserve exact machine-readable evidence as allowed by Rule 54, but they do not replace the authoritative Markdown report.

A provisional receipt may be committed when it is the safest way to prevent evidence loss during a persistence incident. However:

```text
provisional companion receipt != authoritative research checkpoint
```

Until its decision-relevant reasoning, interpretation, limitations, contradiction impact, and next gate are incorporated into the active Markdown report and committed:

- the receipt must be explicitly marked provisional or non-authoritative;
- no later scientific decision may rely on it as if the programme had advanced;
- no new consequential experiment may begin from it;
- the research programme remains paused at the last authoritative report checkpoint.

## Cross-conversation and cross-agent resume requirement

Every active research report must continuously contain enough current information that a fresh conversation can resume using only:

1. the current repository rules;
2. the current branch and Git history;
3. the authoritative active report and its declared lineage;
4. permanent companion artifacts explicitly referenced by that report when needed for exact machine-readable evidence.

A new conversation must not need the previous chat transcript to know:

- what has already been tested;
- what succeeded or failed;
- which results are authoritative;
- which interpretations are prohibited;
- what remains unresolved;
- whether an owner gate is open;
- the exact next permitted action.

If a new conversation cannot determine the exact next permitted action from the report and Git history alone, it must stop consequential research and repair the report before continuing.

## Chat-memory prohibition

Chat summaries, model memory, private scratchpads, conversation summaries, and remembered prior reasoning are navigation aids only. They may help locate the relevant repository evidence, but they are never scientific source-of-truth material.

When chat context contains a decision-relevant fact that is missing from the active report, the missing report entry is a continuity defect. The defect must be repaired and committed before that fact is used to advance the programme.

Never justify continuation by saying that the current conversation still remembers the missing information.

## Continuous checkpoint requirement

Do not wait for a conversation to become long, for a session to end, or for the owner to request a checkpoint.

After every meaningful independently reviewable research step, ensure that the authoritative report and Git history are current enough that the conversation could end immediately without losing the programme state.

At all times during active research, ask the operational question:

```text
If this conversation disappeared now, could a new thread continue correctly from Git alone?
```

If the answer is no, consequential research must stop until the answer becomes yes.

## Conflict and supersession handling

When a new result changes an older conclusion, preserve chronology. Append or clearly supersede the earlier conclusion in the same authoritative report; do not silently rewrite history into a smooth narrative.

When another report, companion artifact, task system, code comment, whitepaper, or chat summary disagrees with the active report, resolve the evidence conflict explicitly. Do not silently choose the most recent-looking source.

Git remains the durable scientific history, and the authoritative active Markdown report remains the programme-level decision and continuity record.

## Completion gate

A consequential research checkpoint is not complete until all of the following are true:

1. the authoritative active report contains the decision-relevant question, evidence, result, interpretation, limitations, contradictions, and next gate;
2. every required permanent companion artifact is referenced and its role is clear;
3. the report and artifacts are committed on the correct repository and branch;
4. the resulting commit and changed-file scope are verified;
5. a new conversation could identify the exact next permitted action without access to the previous chat.

If any item is false, the only permitted next work is to restore this continuity checkpoint.
