# Foundations Research Instructions

These instructions apply to every file and research action under `research/foundations/`.

## Programme-scoped lineage resolution

The `research/foundations/` directory may contain multiple independent research programmes and standalone reports. Directory location, shared vocabulary, a related metaphor, or conceptual overlap is never sufficient evidence that two reports belong to the same programme.

Before loading any root report or continuity ledger, first inspect the active report's metadata, scope, central questions, declared programme membership, and declared lineage.

1. If the active report explicitly declares membership in an existing programme, follow that programme's root, ledger, and predecessor chain.
2. If a legacy report lacks an explicit declaration, use only direct evidence from the report body or preserved Git history, such as a named root, parent report, immediate predecessor, or programme identifier, to establish membership.
3. Do not infer programme membership from directory location alone.
4. If no direct lineage evidence exists, treat the report as standalone until the relationship is established and recorded explicitly.
5. A report may compare with, cite, constrain, or reopen another programme without becoming its child.
6. Never require an unrelated root SHA, programme ledger, or root-impact matrix merely because both reports are stored under `research/foundations/`.

Every new or materially revised report must declare either:

- `Programme membership: <descriptive programme name>` and its root lineage; or
- `Programme membership: standalone`.

## Continuous-source cosmology programme chain

For reports that explicitly belong to the continuous-source cosmology and particle-formation programme, the current root report is:

```text
research/foundations/lineum-continuous-source-cosmology-validation.md
```

At the 2026-07-30 continuity checkpoint, the recovered root report was version `0.4.14` with evidence cutoff `2026-07-29`. Never assume that version remains current: fetch the file or immutable blob again at the start of each new task within this programme and record the current SHA, version, and evidence cutoff.

The programme continuity and impact ledger is:

```text
research/foundations/lineum-root-programme-continuity-and-impact-ledger.md
```

Before analyzing, proposing, implementing, testing, ranking, rejecting, or resuming any child lane that belongs to this programme, read in this order:

1. the root report;
2. the continuity and impact ledger;
3. every immediate predecessor named by the active child report;
4. the active child report itself;
5. any additional report, code, output, whitepaper, or ClickUp evidence required by the specific claim.

## No latest-lane tunnel vision

Within a declared programme, a recent experiment, metaphor, equation, or child report never replaces that programme's root record.

For every consequential child-lane decision inside the continuous-source cosmology programme:

- recover all decision-relevant positive results, negative results, contradictions, open variants, deferred gates, observer limitations, accounting limits, and stop conditions from the complete programme;
- state which root branches are `supports`, `contradicts`, `constrains`, `depends_on`, `reopens`, `observationally_equivalent`, `unaffected`, or `not_yet_compared`;
- preserve all earlier equation families and mechanisms as distinct reopenable variants unless evidence with power over the exact claim changes their status;
- select the next discriminator for its value across the combined programme, not because it is nearest to the latest result;
- never promote a local success into particle, identity, heredity, life, cosmology, or nature claims without passing the corresponding programme gates.

If the applicable root report is too large for one tool response, retrieve it through its immutable blob and bounded sections. Record every relevant section actually reviewed and every material family still `not_yet_compared`. Do not substitute a ClickUp description, chat summary, whitepaper, or recent child report for the applicable programme root.

## Report hierarchy requirement

Every new or materially revised child report in a declared programme must include:

- exact programme name;
- exact root report path, version, evidence cutoff, and current SHA;
- full report lineage from the root through every immediate predecessor;
- inherited evidence and constraints required for the current decision;
- a local verdict;
- a programme-impact matrix;
- explicit open branches and reopen triggers;
- the next cross-program discriminator when one is relevant.

A standalone report must instead include its own scope, evidence cutoff, direct predecessors or provenance sources when any exist, local verdict, open branches, and relevant cross-program relationships. It must not invent a root lineage or impact matrix for an unrelated programme.

A child report may remain narrowly scoped, but its decision logic must not be narrow-minded. A standalone report may remain independent while still recording material relationships to other research.

## Permanent evidence boundary

`.scratch/` is local, temporary, non-versioned, and non-evidentiary. Never query it through GitHub, count its absence, or rely on it for a decision. Promote every retained method, input, output, negative result, and limitation into the active standalone report or another explicitly permanent research-scoped path before proceeding.

## Operational tracking

Git reports are the scientific source of truth. ClickUp records task state, priority, ownership, and operational planning. Repository `todo.md` material is historical evidence only and must not define current work.

The following task references belong specifically to the continuous-source cosmology and particle-formation programme and must not be treated as universal tasks for unrelated reports in this directory.

At the 2026-07-30 continuity checkpoint, the broad programme task was:

```text
869dpg9hb — Research: Formation and Stability of Standard Model Particles (Protons, Neutrons, Electrons) in the Lineum Wave Core
```

The active repair/provenance child task was:

```text
869ebyvpb — Research: Active Growth and Scaffold Repair (Eq-11.1 Provenance Gate)
```

Always verify their current state in ClickUp before relying on them for work inside that programme. Resolve unrelated reports against their own declared ClickUp task or operational context.
