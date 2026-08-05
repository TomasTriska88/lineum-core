# Owner Intuition Prompt Independence

**Status:** Binding supplement to `.agent/rules.md`.

## Purpose

This rule preserves the project owner's intuition as an independent source of candidate hypotheses at the verified negative-result gate defined by Rules 26 and 35.

## Non-leading prompt requirement

When the owner-intuition gate opens, do not provide answer choices, candidate mechanisms, example answers, implied solution categories, or a multiple-choice framing before the project owner responds.

Present only one vivid, concrete scene that communicates the observable situation:

- what happens;
- what still works;
- what fails;
- what remains unexplained;
- why the missing explanation matters for the next research step.

The scene must not conceal proposed repairs, preferred mechanisms, or answer categories inside the analogy. End with one fully open-ended question that invites the project owner to construct an independent mental model in their own words. Explicitly allow the owner to reject the offered scene and replace it with another.

Possible interpretations, alternatives, mechanisms, and formalizations may be introduced only after the owner's answer has been recorded distinctly from agent-generated hypotheses and experimental evidence.

## Contaminated-prompt handling

If answer choices, candidate solutions, or leading examples were already supplied before the owner's response, do not treat the resulting response as fully independent intuition. Preserve the exchange honestly, then repeat the intuition gate later with a neutral scene and one open-ended question before using owner intuition to select or rank a replacement mechanism.
