from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

REPORT = Path("research/lineum-public-tolog-galactic-shape-b4.md")
MANIFEST = Path("research/lineum-public-tolog-b4/artifact-manifest.json")
REPAIR_PROTOCOL = Path(
    "research/lineum-public-tolog-b4/q2-ledger-neutral-control-check-repair-protocol.json"
)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one exact match, found {count}")
    return text.replace(old, new, 1)


def replace_section(text: str, pattern: str, replacement: str, label: str) -> str:
    result, count = re.subn(pattern, replacement, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise SystemExit(f"{label}: expected one regex match, found {count}")
    return result


def main() -> None:
    text = REPORT.read_text(encoding="utf-8")

    old_status = "**Status:** active authoritative report; localized-L1, `Q2-O1`, `Q2-SA1-A`, and `Q2-PV1-A` are independently checked within their frozen domains; `Q2-PV1-B` has a retained supported-runtime primary with `26 / 28` controls available and `0 / 26` Q2 rescues/classification changes; the separately implemented PV1-B checker, its tests, comparison surface, and fail-closed contract are now frozen and published; official supported-runtime checker execution is the only authorized next scientific action; Q1 and Q3 remain unchanged"
    new_status = "**Status:** active authoritative report; localized-L1, `Q2-O1`, `Q2-SA1-A`, and `Q2-PV1-A` are independently checked within their frozen domains; `Q2-PV1-B` primary remains `26 / 28` controls available with `0 / 26` Q2 rescues/classification changes; the first independently implemented PV1-B checker reproduced the exact 28-case categories and complete primary summary but failed its own pass gate only on two raw floating cancellation residuals that each remain far inside the unchanged ledger-neutrality tolerance; this is a technical comparison-method failure, not independent verification and not scientific disagreement; only the frozen residual-comparison repair is authorized next; Q1 and Q3 remain unchanged"
    text = replace_once(text, old_status, new_status, "status")
    text = replace_once(text, "**Version:** 0.24.1  ", "**Version:** 0.24.2  ", "version")
    text = replace_once(
        text,
        "**Checkpoint parent:** `927c24682d1075b3fb0eb08185a14e830dfcef45`  ",
        "**Checkpoint parent:** `7c34d1a098d2c848cb2d1295799c78f154c998b4`  ",
        "checkpoint parent",
    )

    continuity = "Version `0.24.1` freezes the post-primary independent PV1-B checker after the primary and report checkpoint, records its separate implementation boundary, exact source/test/protocol identities, `1e-8 + 1e-12 * scale` numerical comparison rule, complete decision surface, `12 / 12` unsupported-runtime helper preflight, and supported-runtime execution gate before any official checker result."
    text = replace_once(
        text,
        continuity,
        continuity
        + " Version `0.24.2` records the first official PV1-B checker after a `38 / 38` supported-runtime test gate: protocol and key-set checks passed, all categorical outputs and the complete independent summary matched the primary, but the checker returned `passed = false` because two raw `delta_ledger` cancellation residuals differed across operation orderings. Both residuals are roughly one millionth of their already-frozen ledger tolerances, so the attempt is classified as a technical comparison-method failure. The only permitted repair is frozen before implementation and changes no equation, case, observer, scientific threshold, recovery metric, summary rule, or other numeric comparison field.",
        "continuity 0.24.2",
    )

    section7 = """## 7. Interpretation and failure-to-mechanism ledger

1. **Implementation:** the audited update contains unpaired feedback, one-way mode transfer, dissipation without reservoir credit, clipping, spatial transport/diffusion, and optional hard guards. `Q2-PV1-B` changes no production equation; its checker is a second implementation of the same frozen public equations, cases, perturbations, observers, and decision rules.
2. **Reproduced observations:** the homogeneous and localized checks remain negative; `Q2-O1` changes no classification; `Q2-SA1-A` is independently reproduced with all eight cases `unpaired_source_dominated`; and `Q2-PV1-A` is independently reproduced with `28` active rows, `24` ledger-non-neutral and `4` numerically neutral. The retained PV1-B primary remains `26 / 28` balanced controls available, two explicit reset-degenerate unavailable rows, zero neutral-perturbation failures, zero Q2 rescues, and zero classification changes. The first separately implemented PV1-B checker passed its `38 / 38` regression gate, reproduced the exact 28-case key set, every categorical field, and the complete primary summary, but returned `passed = false` solely because two raw `perturbation_ledger.delta_ledger` cancellation residuals failed the generic cross-implementation numeric comparison.
3. **Cautious interpretation:** the two checker mismatches are not decision disagreements. For `LAP4|no_explicit_tanh|phi0=1.0`, the independent residual is `-4.76837158203125e-07` while the primary stores `0.0`; the unchanged ledger tolerance is `0.4282901062646145`. For `LAP4|no_linear_dissipation|phi0=0.0`, the checker stores `0.0` while the primary residual is `3.814697265625e-06`; the unchanged tolerance is `3.1772686810775306`. The residual magnitudes are only about `1.11e-6` and `1.20e-6` of those respective tolerances. Because all underlying ledger values, neutrality categories, recovery metrics, cases, factors, and summaries otherwise agree, this is classified as a technical comparison-method failure caused by over-constraining a floating cancellation residual, not as scientific disagreement. PV1-B is still not independently verified until the narrowly repaired checker passes from a fresh run.
4. **Hypothesis only:** a genuinely reciprocal existing-state repair, a phase/conjugate extension, a different equation family, an additional state, or another mechanism not represented in the tested lanes might alter Q2. None is selected while the PV1-B checker remains technically unresolved.
5. **Real physics:** the declared ledger is implementation-defined only. No laboratory field, physical energy, gravity, cosmology, dark-matter, quantum, or TOLOG mapping is established by these tests.

| Audit item | Bounded finding |
|---|---|
| What failed | no full-state localized recovery; no reciprocal homogeneous return; no observer alignment rescue; no Stage A transport-accounted near-return candidate; no PV1-B balanced-control rescue in the 26 eligible primary cases; first PV1-B checker failed only an over-strict raw cancellation-residual comparison |
| What remained positive | exact Stage A and PV1-A independent reproduction; all 26 PV1-B primary controls satisfy the frozen ledger-neutrality rule; first PV1-B checker exactly reproduces all categories and the complete `28 / 26 / 2 / 0 / 0` summary; both disputed residuals independently remain far inside the unchanged ledger tolerances |
| Failure location under tested conditions | current equation/exchange-accounting semantics remain the leading demonstrated Q2 failure location; the checker disagreement is localized to comparison of a derived floating cancellation residual, not to a state, observable, decision, or mechanism |
| Current implementation status | unsupported as a natural reciprocal attractor under tested conditions |
| Wider Lineum status | unresolved; not universally falsified |
| Next consequential step | implement only the preregistered `delta_ledger` comparison repair test-first, freeze the repaired checker identities, and run a fresh supported-runtime checker from the beginning |

Registered repair families remain unselected. No reciprocal, phase/interference, compaction, Stage-B spatial, or new-field mechanism may be selected before the PV1-B independent verification chain closes."""
    text = replace_section(
        text,
        r"## 7\. Interpretation and failure-to-mechanism ledger\n.*?(?=\n## 8\.)",
        section7,
        "section 7",
    )

    marker = "\n## 9. Preserved failure and publication chronology"
    if text.count(marker) != 1:
        raise SystemExit("section 8.23 insertion marker mismatch")
    section823 = r'''
### 8.23 First official `Q2-PV1-B` independent checker — technical comparison-method failure

The first official independently implemented PV1-B checker ran from workflow source commit `19bac215d5a966560ca14962f35a1b22c0d8077c` as workflow run `31310400036`, job `93237235577`. Exact source/report/primary identities passed before execution. The workflow used Python `3.11.15`, NumPy `1.26.4`, and pytest `9.1.1`, installed the repository requirements, and passed the complete frozen pre-checker gate `38 / 38` before the scientific command ran.

The checker recomputed all 28 cases through its separate implementation and durably retained its output before the workflow deliberately propagated the nonzero checker exit code. The one-use workflow was removed in result commit `7c34d1a098d2c848cb2d1295799c78f154c998b4`; no workflow artifact or ZIP was uploaded.

```text
checker result path = research/lineum-public-tolog-b4/q2-ledger-neutral-control-check.json
checker result Git blob = 48e9a024b8988be6272526531efa476264ced791
checker result SHA-256 = 71335e17fa15eb5e5d35e564f146c3836b5b0ab4ecf1657e9815a918c2b04ac1
checker canonical payload SHA-256 = 805faa5276169faba1ced990bd8803c1ea22e6f855381fa1a05344d9f93126ce
execution receipt Git blob = fa235870fc1f40086f36db315543a2b861eb22f5
protocol_pass = true
key_set_pass = true
categorical_mismatch_count = 0
numeric_mismatch_count = 2
passed = false
```

The independent summary is exactly the retained primary summary:

```text
case_count = 28
control_available_count = 26
control_unavailable_count = 2
control_unavailable_keys =
  LAP4|no_interaction_denominator|phi0=1.0
  LAP8|no_interaction_denominator|phi0=1.0
balanced factor min / max = 0.8211962194809532 / 0.9780485627631685
neutral perturbation failures = 0
canonical Q2-positive count = 0
balanced Q2-positive count = 0
balanced rescue count = 0
Q2 classification changed count = 0
outcome = ledger_neutral_control_does_not_rescue_q2_classification
```

Every categorical comparison also agrees exactly. The only two reported numeric mismatches are the raw cancellation residual `perturbation_ledger.delta_ledger`:

| Case | Checker residual | Primary residual | Frozen ledger tolerance | Max residual / tolerance |
|---|---:|---:|---:|---:|
| `LAP4|no_explicit_tanh|phi0=1.0` | `-4.76837158203125e-07` | `0.0` | `0.4282901062646145` | `1.1133508601492564e-06` |
| `LAP4|no_linear_dissipation|phi0=0.0` | `0.0` | `3.814697265625e-06` | `3.1772686810775306` | `1.2006215553452324e-06` |

In both cases the separately computed residual is already classified ledger-neutral by the unchanged scientific rule, and the retained primary is likewise ledger-neutral. The primary and checker also agree on `epsi_before`, `epsi_after`, `ledger_before`, `ledger_after`, `ledger_tolerance`, `pphi_unchanged`, all recovery metrics, balanced factors, cap/reset states, and every decision category under the frozen comparison contract. The mismatch therefore isolates only the exact floating representation of `ledger_after - ledger_before` after different valid operation orderings.

**Classification:** technical comparison-method failure. It is neither passing independent verification nor scientific disagreement. The PV1-B primary remains unchanged and `primary_pending_independent_check` in evidentiary effect.

#### 8.23.1 Frozen narrow repair before implementation

The only permitted checker repair is:

1. remove only `perturbation_ledger.delta_ledger` from strict cross-implementation numeric equality;
2. retain both raw primary and checker `delta_ledger` values diagnostically;
3. require each implementation's residual separately to satisfy its own already-frozen `ledger_tolerance` and require the stored `neutral_within_numeric_tolerance` category to agree exactly;
4. fail closed if either raw residual exceeds its own frozen tolerance;
5. keep strict cross-implementation comparison unchanged for `epsi_before`, `epsi_after`, `ledger_before`, `ledger_after`, `ledger_tolerance`, `pphi_unchanged`, balanced factors, all recovery metrics, all cap/reset state, all categories, every summary field, and the exact 28-case key set;
6. keep `COMPARE_ATOL = 1e-8`, `COMPARE_RTOL = 1e-12`, every production/research equation, case, perturbation factor/formula, observer, recovery threshold, and ledger-neutrality threshold unchanged;
7. add permanent regression tests proving that operation-order residual differences are allowed only when both sides independently satisfy the frozen ledger tolerance, and that an excessive residual fails closed;
8. after the repaired source/test identities and this repair contract are frozen, execute a fresh supported-runtime checker from the beginning. The failed checker output may not be reclassified post hoc as a pass.

No other checker modification is authorized by this checkpoint.
'''
    text = text.replace(marker, "\n" + section823.strip() + marker, 1)

    old_next = "The immediate next scientific action is exactly one supported-runtime execution of the frozen `Q2-PV1-B` checker from commit `927c24682d1075b3fb0eb08185a14e830dfcef45`, after exact checker/test/protocol/primary/report identity checks and the complete relevant regression gate. The checker must retain ordinary JSON and no ZIP/workflow artifact. No replacement mechanism is selected before this check. If it verifies the negative primary, the owner-intuition gate opens and research must stop for the owner's response before any replacement mechanism is chosen. Q1 and Q3 remain active controlling goals; after this small Q2 validity chain closes, programme-level prioritization returns to all three questions rather than allowing Q2 to expand indefinitely."
    new_next = "The immediate next scientific action is only the frozen narrow PV1-B checker comparison repair in Section 8.23.1. It must be implemented test-first without changing the scientific update, case set, observers, thresholds, primary data, or any cross-implementation comparison except the raw `delta_ledger` residual rule. After the repaired checker and tests are committed and their identities are recorded in this report, run one fresh supported-runtime checker from the beginning. No replacement mechanism is selected before that check. The owner-intuition gate does not open from this failed checker attempt because independent verification is not yet complete. Q1 and Q3 remain active controlling goals."
    text = replace_once(text, old_next, new_next, "next action")

    old_tail = "`0.24.1` freezes the separately implemented PV1-B checker and its complete comparison contract after the primary report checkpoint; no official checker result exists yet. Questions 1 and 3 are unchanged; Question 2 remains negative within the tested domain."
    new_tail = "`0.24.1` freezes the separately implemented PV1-B checker and its complete comparison contract after the primary report checkpoint. `0.24.2` records the first official supported-runtime checker after `38 / 38`: the exact 28-case categories and full primary summary are independently reproduced, but the checker returns `passed = false` solely on two over-strict raw `delta_ledger` cancellation-residual comparisons; both residuals remain about one millionth of their unchanged scientific ledger tolerances. The attempt is retained as a technical comparison-method failure and the only permitted residual-comparison repair is frozen before implementation. Questions 1 and 3 are unchanged; Question 2 remains negative within the tested domain but PV1-B independent verification is still pending."
    text = replace_once(text, old_tail, new_tail, "version history")

    old_handoff = "A new researcher must re-read current rules and verify the current `develop` head, this report, and `research/lineum-public-tolog-b4/artifact-manifest.json`. Treat the localized checker, `Q2-O1`, `Q2-SA1-A`, and `Q2-PV1-A` as already completed at the bounded evidence levels stated above. Preserve all technical non-results rather than rewriting history. Treat `q2-ledger-neutral-control.json` as a supported-runtime **primary only**, with the exact result `26 available / 2 unavailable / 0 neutral failures / 0 Q2 rescues / 0 classification changes`. The independent PV1-B checker is frozen at commit `927c24682d1075b3fb0eb08185a14e830dfcef45`, source blob `50a26bcfc7ef16af33f192b97eb99690e8a13fea`, test blob `937e0c1e36c1bdad4a84749aec11ef19ffecb4d5`, and protocol blob `54e381428d49ba8e8aa944f8072fa281bf15d43a`; execute only that supported-runtime checker next. Do not select a reciprocal, phase/interference, compaction, Stage-B spatial, or new-field replacement before the checker closes. Keep all subsequent work strictly mapped to Q1, Q2, or Q3."
    new_handoff = "A new researcher must re-read current rules and verify the current `develop` head, this report, and `research/lineum-public-tolog-b4/artifact-manifest.json`. Treat the localized checker, `Q2-O1`, `Q2-SA1-A`, and `Q2-PV1-A` as already completed at the bounded evidence levels stated above. Preserve all technical non-results rather than rewriting history. Treat `q2-ledger-neutral-control.json` as a supported-runtime **primary only**, with the exact result `26 available / 2 unavailable / 0 neutral failures / 0 Q2 rescues / 0 classification changes`. Treat `q2-ledger-neutral-control-check.json` from run `31310400036` as a technical comparison-method failure: it exactly reproduces the key set, all categories, and complete summary but fails only two raw `delta_ledger` comparisons that are far inside the unchanged scientific neutrality tolerance. Implement only the repair frozen in Section 8.23.1, add the two required regressions, freeze repaired source/test identities, and rerun the entire supported checker. Do not select a reciprocal, phase/interference, compaction, Stage-B spatial, or new-field replacement and do not open the owner-intuition gate until a passing independent PV1-B checker closes this chain."
    text = replace_once(text, old_handoff, new_handoff, "handoff")

    REPORT.write_text(text, encoding="utf-8")

    repair = {
        "schema": "lineum-b4-q2-ledger-neutral-control-check-repair/1",
        "stage": "Q2-PV1-B-CHECK",
        "status": "repair_frozen_before_implementation",
        "failed_checker": {
            "workflow_run_id": 31310400036,
            "workflow_job_id": 93237235577,
            "source_commit": "19bac215d5a966560ca14962f35a1b22c0d8077c",
            "result_git_blob": "48e9a024b8988be6272526531efa476264ced791",
            "result_sha256": "71335e17fa15eb5e5d35e564f146c3836b5b0ab4ecf1657e9815a918c2b04ac1",
            "execution_git_blob": "fa235870fc1f40086f36db315543a2b861eb22f5",
            "tests_passed": 38,
            "protocol_pass": True,
            "key_set_pass": True,
            "categorical_mismatch_count": 0,
            "numeric_mismatch_count": 2,
            "classification": "technical_comparison_method_failure",
        },
        "mismatches": [
            {
                "case_key": "LAP4|no_explicit_tanh|phi0=1.0",
                "path": "perturbation_ledger.delta_ledger",
                "checker": -4.76837158203125e-07,
                "primary": 0.0,
                "ledger_tolerance": 0.4282901062646145,
                "max_abs_residual_over_tolerance": 1.1133508601492564e-06,
            },
            {
                "case_key": "LAP4|no_linear_dissipation|phi0=0.0",
                "path": "perturbation_ledger.delta_ledger",
                "checker": 0.0,
                "primary": 3.814697265625e-06,
                "ledger_tolerance": 3.1772686810775306,
                "max_abs_residual_over_tolerance": 1.2006215553452324e-06,
            },
        ],
        "allowed_change": {
            "remove_from_cross_implementation_numeric_equality": [
                "perturbation_ledger.delta_ledger"
            ],
            "retain_raw_values_diagnostically": True,
            "require_each_side_separately": "abs(delta_ledger) <= ledger_tolerance",
            "require_neutrality_category_exact_match": True,
            "fail_closed_if_either_side_exceeds_tolerance": True,
        },
        "must_not_change": [
            "production/research equations",
            "28-case key set",
            "primary JSON",
            "balanced factor formula",
            "central or annular regions",
            "recovery observers or thresholds",
            "ledger-neutrality threshold",
            "COMPARE_ATOL=1e-8",
            "COMPARE_RTOL=1e-12",
            "other numeric comparison fields",
            "categorical comparison fields",
            "summary comparison fields",
        ],
        "required_regressions": [
            "different raw delta_ledger residuals are accepted only when both independently satisfy their frozen ledger tolerances",
            "either primary or checker residual exceeding its own frozen ledger tolerance fails closed",
        ],
        "rerun_rule": "after repair source/test identities are frozen, execute a fresh supported-runtime checker from the beginning; do not reclassify the failed attempt post hoc",
        "scope": "Q2 only; no mechanism selection or owner-intuition gate until passing independent verification",
    }
    REPAIR_PROTOCOL.write_text(
        json.dumps(repair, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    files = manifest.setdefault("files", {})
    files["research/lineum-public-tolog-b4/q2-ledger-neutral-control-check.json"] = {
        "git_blob_sha": "48e9a024b8988be6272526531efa476264ced791",
        "sha256": "71335e17fa15eb5e5d35e564f146c3836b5b0ab4ecf1657e9815a918c2b04ac1",
        "role": "first official Q2-PV1-B independent checker technical comparison-method failure",
    }
    files["research/lineum-public-tolog-b4/q2-ledger-neutral-control-check-execution.json"] = {
        "git_blob_sha": "fa235870fc1f40086f36db315543a2b861eb22f5",
        "role": "first official Q2-PV1-B checker supported-runtime execution receipt",
    }
    files[str(REPAIR_PROTOCOL)] = {
        "role": "frozen narrow Q2-PV1-B checker residual-comparison repair before implementation"
    }
    checker = manifest.setdefault("q2_ledger_neutral_control_checker", {})
    checker.update(
        {
            "scientific_status": "attempt_1_technical_comparison_method_failure",
            "official_result": False,
            "attempt_1_workflow_run": 31310400036,
            "attempt_1_workflow_job": 93237235577,
            "attempt_1_tests_passed": 38,
            "attempt_1_protocol_pass": True,
            "attempt_1_key_set_pass": True,
            "attempt_1_numeric_mismatch_count": 2,
            "attempt_1_categorical_mismatch_count": 0,
            "attempt_1_complete_summary_match": True,
            "repair_status": "frozen_before_implementation",
            "repair_scope": "delta_ledger raw cancellation residual comparison only",
        }
    )
    MANIFEST.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print("report_sha256", hashlib.sha256(REPORT.read_bytes()).hexdigest())
    print("manifest_sha256", hashlib.sha256(MANIFEST.read_bytes()).hexdigest())
    print("repair_sha256", hashlib.sha256(REPAIR_PROTOCOL.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
