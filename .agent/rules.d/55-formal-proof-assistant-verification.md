# Formal Proof Assistant Verification

**Status:** Binding supplement to `.agent/rules.md`.

## Purpose

Formal proof assistants such as Lean may be used as an additional mathematical verification lane for Lineum. They strengthen checks of exact mathematical claims; they do not replace numerical experiments, implementation audits, independent reproduction, or empirical comparison with the observable universe.

This rule does not add Lean, Mathlib, or any other theorem-prover dependency to the repository. Actual toolchain integration requires a separate, explicit implementation checkpoint.

## Execution routing

- Use a formal proof assistant only in an environment that can actually execute and verify the proof, normally Codex, a local development environment, or declared CI.
- A chat-only environment without an executable prover may propose theorem statements or draft proof text, but it MUST NOT describe them as kernel-checked, formally verified, or proved by Lean.
- Do not require the project owner to operate the prover manually when the active Codex or repository environment can execute it.
- Do not divert an active scientific lane into formalization merely because a theorem prover is available. Prefer formalization when it is the cheapest useful independent discriminator or when an exact invariant is important enough to justify durable machine checking.

## Appropriate proof targets

Prefer formal proof for exact, implementation-relevant mathematics such as:

- algebraic identities;
- conservation or ledger identities;
- symmetry statements;
- positivity and boundedness conditions;
- discrete operator identities;
- exact limiting or known-answer cases;
- conditions under which a perturbation preserves a declared invariant;
- equivalence or non-equivalence of mathematical formulations when the statement can be made explicit.

Do not use theorem proving as a substitute for questions that are inherently numerical, statistical, empirical, or implementation-dependent.

## Evidence separation

Always keep these claims separate:

1. **Formal theorem:** the stated conclusion follows from the stated mathematical assumptions in the checked formal system.
2. **Implementation conformance:** the current Lineum code actually implements the same definitions and assumptions used by the theorem.
3. **Numerical behavior:** the executable implementation exhibits the reported finite-precision behavior under the frozen experiment.
4. **Physical connection:** observations of the real universe support the proposed mapping or physical interpretation.

A successful formal proof establishes only layer 1 unless the other layers are independently checked. It is never sufficient evidence that nature uses the proved model.

## Independence requirements

A formal proof may count as an independent scientific verification lane only when:

- the theorem statement exposes all material assumptions rather than encoding the desired conclusion indirectly;
- the proof does not merely certify a transcription of an already-disputed implementation path;
- the mapping from the theorem definitions to Lineum code is audited separately;
- finite-precision effects, discretization, numerical clipping, caps, resets, and runtime guards are tested separately when they can affect the executable behavior;
- the active research report records exactly what the proof establishes and what it does not establish.

A green prover result is subject to the same anti-green-test rule as any other automated check.

## Toolchain intake and reproducibility

Before adding Lean, Mathlib, another formal library, or any theorem-prover toolchain to the repository:

1. apply `.agent/rules.d/48-third-party-model-and-research-intake.md` to the exact versions being added;
2. verify the exact upstream license, notices, provenance, and dependency compatibility rather than relying on remembered license information;
3. pin the exact toolchain and library versions needed for reproducibility;
4. keep theorem-prover tooling outside the runtime dependency surface of `lineum_core/` unless a later explicit promotion gate establishes a genuine runtime requirement;
5. record the verification command and environment in the relevant research or engineering checkpoint;
6. ensure CI or local verification fails closed when a formally protected theorem no longer checks.

## Research-report boundary

When a formal proof informs a Lineum research conclusion, the single active report for that programme must state:

- the exact theorem in ordinary mathematical language;
- its assumptions;
- the formal source identity and prover/toolchain identity;
- the successful verification command or retained execution receipt;
- the separate implementation-conformance check;
- the scientific interpretation and prohibited over-interpretations.

Formal proof source may be retained as a readable companion artifact when justified, but it does not create a second narrative report.
