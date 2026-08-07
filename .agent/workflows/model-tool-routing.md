# Fixed Lineum Codex Configuration and Execution Workflow

## Purpose

This workflow is the binding source of truth for the model, reasoning effort, processing speed, and scientific verification pattern used for Lineum work in `TomasTriska88/lineum-core`.

Lineum research and repository work are performed directly in Codex. An external ChatGPT supervisor is not required for scientific reasoning, interpretation, experiment selection, repository execution, or claim review.

If product labels change, preserve the reasoning role and scientific safeguards below rather than relying on obsolete names.

## Fixed configuration

Use one configuration for all Lineum work and do not switch it task by task:

- model: the strongest available GPT-5.6 Sol-tier model;
- reasoning effort: `high`;
- processing speed: standard, not fast mode;
- repository: `TomasTriska88/lineum-core`;
- default branch: `develop`.

High is the fixed repository-wide reasoning level. Do not reduce reasoning below High or escalate to Max or Ultra merely because an individual task appears easy, difficult, tightly coupled, urgent, or inexpensive. A different reasoning level requires an explicit project-owner change to this repository-wide policy.

Do not enable fast mode. Standard speed preserves the selected model and reasoning level while avoiding the disproportionate credit cost of fast processing. Tool execution, builds, tests, and simulations may dominate wall-clock time and are not necessarily accelerated by model fast mode.

## Codex is the primary scientific workspace

Codex owns the complete Lineum research cycle:

1. repository and evidence retrieval;
2. formulation of the scientific question;
3. identification of assumptions and competing explanations;
4. preregistration of observables, controls, and falsification criteria;
5. implementation and execution;
6. independent verification;
7. adversarial interpretation;
8. permanent report capture;
9. selection of the next discriminating step;
10. bounded promotion into code or whitepapers.

Codex output is not automatically correct merely because it was produced at High reasoning effort. Every material conclusion remains subject to the repository evidence gates.

## High-reasoning scientific verification model

High reasoning is used with one lead researcher responsible for the complete scientific chain. Independent verification is mandatory, but agent count is not a validity criterion. Prefer the cheapest methodologically independent check that can actually discriminate the disputed claim.

### Lead-agent ownership

One lead agent must own the active goal from question through final synthesis. The lead agent is responsible for:

- the exact question and scope;
- the frozen protocol;
- the active research report;
- consistency with repository history;
- identifying which checks are scientifically independent;
- reconciling evidence without hiding disagreement;
- the final narrow conclusion and prohibited over-interpretations;
- the final repository diff and checkpoint.

There must never be multiple competing final editors or multiple agents independently changing the same files.

### Independent verification roles

Independent verification may use:

- an implementation audit against the declared equation;
- independent analytic or dimensional derivation;
- a second numerical implementation or reproduction;
- known-answer, limiting-case, convergence, or conservation checks;
- intervention, ablation, field freeze, shuffle, or null controls;
- test and metric validity audit;
- historical variant and contradiction retrieval;
- comparison with current primary or authoritative external evidence;
- adversarial claim-strength review;
- documentation and repository-boundary audit.

When the runtime supports supporting agents and a genuinely separable check benefits from one, the lead may use a supporting agent with frozen inputs, a narrow question, declared files or evidence, an output contract, and explicit conclusions it is not authorized to make. Supporting agents are optional; methodological independence is mandatory.

### Tightly coupled work stays in one lane

Keep a derivation, ontology decision, causal argument, single-file edit, or tightly coupled implementation in the lead lane when splitting it would destroy shared assumptions or produce artificial disagreement.

Audit the completed result afterward with a methodologically independent check. Parallel execution is optional and must never be treated as evidence by itself.

### No voting and no averaging away contradictions

Do not decide scientific truth by majority vote, confidence averaging, or stylistic consensus among agents, checks, or lanes.

When checks disagree:

1. preserve each result and its assumptions;
2. identify the first concrete point of divergence;
3. check equations, units, parameters, seeds, boundaries, observers, metrics, and environments;
4. run the cheapest frozen discriminator capable of resolving the difference;
5. record unresolved disagreement explicitly when the available evidence cannot decide it.

An unresolved contradiction is a valid result. It must not be rewritten into a smooth compromise.

## Mandatory scientific loop

For every decision-relevant lane, perform this sequence before advancing:

1. **Retrieve:** read all current applicable repository rules, the active root and child reports, relevant code, tests, whitepapers, historical variants, and recorded negative results.
2. **State:** separate what the implementation currently computes, what prior reproducible runs observed, what is interpreted, what is hypothesized, and what is known about real physics.
3. **Freeze:** record the question, assumptions, equations, units, inputs, parameters, seeds, boundaries, observables, controls, success criteria, failure criteria, and meaning of each possible outcome in the active report.
4. **Sanity-check:** perform analytic, dimensional, symmetry, limiting-case, and toy-case checks wherever applicable.
5. **Execute:** run the smallest discriminating experiment before broad sweeps or implementation expansion.
6. **Verify independently:** use at least one check that does not merely repeat the same calculation path, such as a second implementation, known-answer case, convergence study, conservation audit, intervention, ablation, or independent supporting lane.
7. **Attack the result:** search for circular metrics, leakage, observer dependence, numerical artifacts, hidden tuning, confounders, alternative explanations, and claims stronger than the test had power to establish.
8. **Record:** update the active standalone report with commands, raw and human-readable results, failures, uncertainty, environment limits, and prohibited over-interpretations before the next consequential step.
9. **Decide narrowly:** assign only a scope-safe status such as `supported`, `unsupported_under_tested_conditions`, `falsified_within_domain`, `unresolved`, or `reopened`.
10. **Promote cautiously:** modify canonical code or whitepapers only through the repository promotion gates after the report supports the exact change.

A green test proves only that the asserted test condition passed. It does not prove that the metric is valid, the mechanism is unique, or nature behaves like the simulation.

## Independence requirements

A result is not independently verified when the second check:

- imports the same unreviewed implementation for the disputed quantity;
- copies the same formula or mistaken assumption without re-derivation;
- uses the same circular observer or fitted threshold;
- differs only in formatting, wrapper code, or agent wording;
- sees the desired outcome before selecting its method when blinding was practical.

Record exactly what is independent and what remains shared.

## Claim ladder

Use the following evidence ladder and never skip levels silently:

1. `implemented`: the code contains the stated operation;
2. `reproduced`: a frozen run produced the stated output;
3. `robust_within_tested_domain`: controls and independent checks support the observation in the declared domain;
4. `mechanistically_supported`: interventions or discriminating tests support the proposed causal explanation over recorded alternatives;
5. `empirically_connected`: a defined observable has been compared responsibly with current real-world evidence;
6. `canonical`: the exact bounded claim has passed promotion into the relevant whitepaper or public contract.

Similarity of images, labels, metaphors, or internal behavior cannot by itself advance a claim up this ladder.

## Report-first and whitepaper promotion

The active standalone report under `research/` is the live scientific record during research. Update it before and after every consequential step as required by `.agent/continuous-research-reporting.md`.

Do not continuously synchronize provisional ideas, exploratory results, or bounded failures directly into whitepapers. Whitepapers are canonical claim surfaces and may be updated only after:

- the relevant report is current and reproducible;
- independent checks are recorded;
- contradictory evidence is addressed or preserved;
- the exact claim scope and confidence are stated;
- the promotion gate in `.agent/rules.md` and `docs/repository-boundaries.md` is satisfied.

Negative results remain permanently available in the research history even when they do not alter a whitepaper.

## Owner interaction and stop gates

Continue autonomously through ordinary uncertainty by using the cheapest safe discriminator and the most conservative evidence-preserving path.

Stop and ask the project owner only when required by the binding owner gates, including:

- a verified decision-relevant negative result that opens the owner intuition gate;
- a material architectural or conceptual decision the owner has stated they do not understand;
- missing authorization, credentials, access, or a destructive operation decision;
- two consequential options that remain observationally equivalent after the permitted discriminating work and require an owner preference rather than a scientific verdict.

Questions are hard stops as defined in `.agent/rules.md`. Do not ask optional questions while continuing work in parallel.

## Repository execution discipline

Before every change, verify the repository, branch, target path, current blob or commit SHA, and repository boundary. Use local Git when available. Connector writes are limited to small, precise, reversible changes permitted by `.agent/rules.md`.

Parallel workers, when used, must not write concurrently to the same branch or overlapping paths. The lead agent serializes final edits and verifies the combined diff.

For code changes, run the required tests, static checks, and runtime verification. For rule or documentation-only changes, verify exact file contents, stale conflicting instructions, branch state, and resulting commits; do not claim runtime validation that was not performed.

## Completion package

A completed checkpoint must report:

- repository and branch;
- commit SHA or an explicit statement that no commit was created;
- changed files and purpose;
- commands, tests, simulations, and checks actually performed;
- raw failures and unresolved contradictions;
- scientific evidence level reached;
- claims explicitly not established;
- remaining uncommitted or unsynchronized work;
- ClickUp mode if ClickUp was touched.

The absence of a positive discovery does not make a checkpoint incomplete. A well-scoped negative, null, contradictory, or inconclusive result is a valid completed research output when it is reproducible and honestly recorded.
