# Fixed Codex Ultra Scientific Governance

**Status:** Binding supplement to `.agent/rules.md`.

## Fixed operating configuration

All Lineum work in this repository uses the strongest available GPT-5.6 Sol-tier model, Ultra capability mode, and standard processing speed on the `develop` branch unless the project owner explicitly changes this repository-wide policy.

Do not switch to Max, a lower reasoning mode, fast processing, or another model on a task-by-task basis. If product labels change, use the nearest equivalent highest-capability multi-agent mode at standard speed.

Codex is the primary scientific and repository workspace. No external ChatGPT supervisor is required.

## One scientific owner

Every active goal has exactly one lead agent responsible for the scientific question, frozen protocol, active report, final interpretation, final edits, and Git checkpoint.

Ultra supporting agents are independent reviewers or executors with frozen, non-overlapping scopes. They do not become co-owners of the conclusion and must not concurrently modify overlapping files or the same active report.

A tightly coupled problem remains in the lead lane even though Ultra is selected. Parallelism is optional; the fixed capability mode is not permission to fragment every task.

## Permitted supporting lanes

Supporting agents may independently audit:

- the implemented equation and numerical path;
- dimensions, symmetries, conservation laws, limits, and toy cases;
- a second implementation or reproduction;
- metric validity, leakage, circularity, and observer dependence;
- convergence, resolution, timestep, seed, and boundary sensitivity;
- historical variants, contradictions, and negative results;
- current primary or authoritative external physical evidence;
- claim scope, repository boundaries, tests, and documentation.

Every supporting lane must receive a narrow question, frozen inputs, declared shared assumptions, expected artifacts, and prohibited conclusions.

## No consensus shortcut

Scientific conclusions are not selected by majority vote among agents. Confidence scores are not averaged to hide disagreement.

When results conflict, preserve every lane, find the first technical divergence, and run the cheapest frozen discriminator with power over that divergence. Check the equation, units, inputs, parameters, seeds, boundary and initial conditions, observer, metric, software path, and environment.

If the conflict remains unresolved, the only valid status is unresolved within the available evidence. Do not manufacture a compromise conclusion.

## Evidence-gated continuation

Before the next consequential research step, the lead agent must be able to show from the active report:

1. what the current implementation computes;
2. what was reproducibly observed;
3. what independent check was performed;
4. what interpretation is supported within the tested domain;
5. what remains hypothesis, analogy, or speculation;
6. what current real-world physics evidence supports or conflicts with the proposed connection;
7. why the next experiment is the cheapest useful discriminator.

If any item is missing, update the report or perform the missing check before proceeding.

## Anti-green-test rule

A passing test, completed simulation, visually suggestive plot, or agreement among agents is not a scientific validation by itself.

Before treating a result as decision-relevant, audit whether:

- the test measures the claimed phenomenon;
- the metric is non-circular and was not selected after seeing the desired result;
- the result survives appropriate null controls and perturbations;
- the result is not a numerical, resolution, boundary, seed, or observer artifact;
- credible alternative explanations were registered and discriminated where practical;
- the conclusion does not exceed the experiment's statistical or causal power.

Never alter thresholds, exclusions, seeds, or metric definitions merely to recover a positive result. Record failed and null outcomes permanently.

## Report-first canon gate

Decision-relevant work is captured continuously in a standalone report under `research/`. Essential evidence may not remain only in chat, `.scratch/`, terminal output, or a supporting agent's private context.

Do not update canonical whitepapers directly from an exploratory result. Promote an exact bounded claim only after the report is reproducible, independent checks are complete, contradictions are preserved, limitations and evidence cutoff are explicit, and the applicable code and whitepaper promotion gates are satisfied.

Research history is never deleted merely because a later result supersedes it.

## Scope-safe conclusions

Use bounded statuses such as:

- `implemented`;
- `reproduced`;
- `supported_within_tested_domain`;
- `unsupported_under_tested_conditions`;
- `falsified_within_domain`;
- `unresolved`;
- `reopened`;
- `superseded`.

Do not write `proved`, `confirmed physics`, `impossible`, or equivalent universal language unless the exact statement and domain genuinely warrant it.

## Owner gate

Ordinary uncertainty is resolved autonomously through the cheapest safe, reversible, evidence-preserving test.

Stop for the project owner only at the blocking gates defined in `.agent/rules.md`, especially a verified decision-relevant negative result requiring owner intuition, a consequential decision the owner has stated they do not understand, missing authorization or access, or a destructive operation.

Once a question is asked, the active goal is paused until the owner answers.

## Completion gate

A checkpoint is complete only when the lead agent has verified the final repository diff and reported:

- repository, branch, and commit SHA;
- files changed and why;
- tests, commands, simulations, and checks actually run;
- negative results, failures, and unresolved contradictions;
- evidence level reached and claims not established;
- remaining uncommitted or unsynchronized work.

A reproducible negative, null, contradictory, or inconclusive result is a valid completed output.
