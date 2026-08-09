from __future__ import annotations

import hashlib
import json
from pathlib import Path

REPORT = Path("research/lineum-public-tolog-galactic-shape-b4.md")
MANIFEST = Path("research/lineum-public-tolog-b4/artifact-manifest.json")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one exact match, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    text = REPORT.read_text(encoding="utf-8")

    old_status = "**Status:** active authoritative report; localized-L1, `Q2-O1`, `Q2-SA1-A`, and `Q2-PV1-A` are independently checked within their frozen domains; `Q2-PV1-B` ledger-neutral radial control has a retained supported-runtime primary with `26 / 28` controls available, `0 / 26` Q2 rescues, and `0 / 26` Q2 classification changes; two reset-degenerate rows are explicitly `control_unavailable`; the PV1-B primary awaits a separately implemented checker; Q1 and Q3 remain unchanged"
    new_status = "**Status:** active authoritative report; localized-L1, `Q2-O1`, `Q2-SA1-A`, and `Q2-PV1-A` are independently checked within their frozen domains; `Q2-PV1-B` has a retained supported-runtime primary with `26 / 28` controls available and `0 / 26` Q2 rescues/classification changes; the separately implemented PV1-B checker, its tests, comparison surface, and fail-closed contract are now frozen and published; official supported-runtime checker execution is the only authorized next scientific action; Q1 and Q3 remain unchanged"
    text = replace_once(text, old_status, new_status, "status")
    text = replace_once(text, "**Version:** 0.24.0  ", "**Version:** 0.24.1  ", "version")
    text = replace_once(
        text,
        "**Checkpoint parent:** `9e65e1bd2f2ff96fed78efc89d34ed42d2b1c207`  ",
        "**Checkpoint parent:** `927c24682d1075b3fb0eb08185a14e830dfcef45`  ",
        "checkpoint parent",
    )

    old_continuity = "Version `0.24.0` records that ledger-neutral control as `Q2-PV1-B`: the protocol and harness were frozen before outcome inspection, the first supported-runtime attempt passed `23 / 23` tests but failed only at strict JSON serialization of non-finite diagnostics and is retained as a technical non-result, a serialization-only `null` representation repair was frozen without changing science, and the second supported-runtime attempt passed `26 / 26` tests and retained a primary result with 26 available neutral controls, two explicit unavailable degenerate rows, zero Q2 rescues, and zero Q2 classification changes. Independent PV1-B verification remains required before mechanism selection."
    new_continuity = old_continuity + " Version `0.24.1` freezes the post-primary independent PV1-B checker after the primary and report checkpoint, records its separate implementation boundary, exact source/test/protocol identities, `1e-8 + 1e-12 * scale` numerical comparison rule, complete decision surface, `12 / 12` unsupported-runtime helper preflight, and supported-runtime execution gate before any official checker result."
    text = replace_once(text, old_continuity, new_continuity, "continuity")

    marker = "\n## 9. Preserved failure and publication chronology"
    if text.count(marker) != 1:
        raise SystemExit("section insertion marker mismatch")
    section = r'''
### 8.22 `Q2-PV1-B` independent checker preregistration

The PV1-B primary was retained and version `0.24.0` was committed before this checker implementation was frozen. The checker is therefore **not outcome-blind**: the `26 available / 2 unavailable / 0 rescue / 0 classification-change` primary summary was already known. Its independence is computational rather than blind. It does not import the PV1-B primary runner or its decision function and does not dynamically load them.

Frozen checker checkpoint:

```text
checker commit = 927c24682d1075b3fb0eb08185a14e830dfcef45
checker Git blob = 50a26bcfc7ef16af33f192b97eb99690e8a13fea
checker test Git blob = 937e0c1e36c1bdad4a84749aec11ef19ffecb4d5
checker protocol Git blob = 54e381428d49ba8e8aa944f8072fa281bf15d43a
primary Git blob = 50d3f15d881e0665a450982053a9216f9cf5739c
report Git blob at checker freeze = bab3f46f7dffa6f1242bcb27da1c6585fcb379b3
```

The checker independently reconstructs the 32 x 32 geometry and Gaussian initializer, LAP4/LAP8 diffusion, all frozen update stages, lane semantics, reset/cap handling, 5000-step pre-state, canonical and balanced perturbations, 1000-step recovery, radial profiles, return observers, balanced-factor availability, implementation-ledger receipt, Q2 admissibility, and final comparison labels. The retained primary JSON is read only after the independent 28-case recomputation and is then used for comparison.

The exact expected key set remains all 28 frozen cases. The comparison surface is frozen before execution:

```text
top-level categorical:
  active_before_perturbation
  control_available
  comparison

top-level numeric:
  balanced_annulus_factor

per canonical and balanced branch:
  center_displacement
  energy_error
  energy_profile_error
  half_energy_radius_error
  phi_profile_error
  finite
  full_recovery
  lane
  phi0
  phi_one_sided_stationary
  primary_phi_cap_hits
  primary_psi_cap_hits
  primary_resets
  psi_recovery
  recovery_phi_cap_hits
  recovery_psi_cap_hits
  recovery_resets
  recovery_steps_completed
  reset_free
  stencil

ledger:
  delta_ledger
  epsi_after
  epsi_before
  ledger_after
  ledger_before
  ledger_tolerance
  pphi_unchanged
  neutral_within_numeric_tolerance

summary:
  every retained primary summary field
```

Ordinary numeric agreement is accepted only when

```text
abs(checker - primary)
<= 1e-8 + 1e-12 * max(abs(checker), abs(primary))
```

`null`/non-finite diagnostic representations must agree categorically. The implementation-ledger neutrality rule itself remains the already-frozen `1e-10 * max(1, |ledger_before|)` rule and is not replaced by the comparison tolerance.

The checker passes only if the primary protocol/source bindings pass, both implementations contain the exact 28-key set, all frozen numeric fields agree under the declared comparison rule, all categorical fields agree exactly, all summary fields agree, and the independently recomputed available balanced perturbations themselves contain zero ledger-neutrality failures. No field or tolerance may be removed or widened after execution to obtain agreement.

A local pure-helper preflight passed `12 / 12` under Python `3.13.5` / NumPy `2.3.5`. That environment violates the official NumPy `<2.0` scientific contract, so this is code-loading/known-answer evidence only and not a scientific checker result. The official checker must run once in Python `3.11.15`, NumPy `1.26.4`, pytest `9.1.1` after the complete canonical + PV1-A + PV1-B + JSON-safe + checker test gate passes. It must retain ordinary JSON and no ZIP/workflow artifact.

**Possible outcomes:** a clean independent match promotes the bounded PV1-B observation to `robust_within_tested_domain` and opens the mandatory owner-intuition gate before replacement-mechanism selection; any scientific disagreement is retained and investigated without averaging; a technical failure produces no scientific checker conclusion and may receive only a narrowly frozen technical repair.
'''
    text = text.replace(marker, "\n" + section.strip() + marker, 1)

    old_next = "The immediate next scientific action is a separately implemented `Q2-PV1-B` checker. It must start from the frozen canonical source/state definitions, independently reconstruct the balanced factor and recovery comparison rather than importing the PV1-B primary decision function, require the exact 28-case key set and 26/2 available/unavailable partition, compare the frozen numeric and categorical decision surface, and fail closed on any ledger-neutrality, availability, recovery, cap/reset, or classification disagreement. It must run only after its own source/test identities and comparison rules are frozen, retain ordinary JSON, and upload no ZIP. No replacement mechanism is selected by the PV1-B primary. Q1 and Q3 remain active controlling goals; after this small Q2 validity chain is closed, programme-level prioritization must return to all three questions rather than allowing Q2 to expand indefinitely."
    new_next = "The immediate next scientific action is exactly one supported-runtime execution of the frozen `Q2-PV1-B` checker from commit `927c24682d1075b3fb0eb08185a14e830dfcef45`, after exact checker/test/protocol/primary/report identity checks and the complete relevant regression gate. The checker must retain ordinary JSON and no ZIP/workflow artifact. No replacement mechanism is selected before this check. If it verifies the negative primary, the owner-intuition gate opens and research must stop for the owner's response before any replacement mechanism is chosen. Q1 and Q3 remain active controlling goals; after this small Q2 validity chain closes, programme-level prioritization returns to all three questions rather than allowing Q2 to expand indefinitely."
    text = replace_once(text, old_next, new_next, "next action")

    old_tail = "`0.24.0` records the frozen PV1-B protocol, the first serialization-only technical non-result, the narrow JSON-safe repair, and the second supported-runtime primary after `26 / 26`: 26 controls available and neutral, two explicit reset-degenerate unavailable rows, zero Q2 rescues, and zero Q2 classification changes. PV1-B independent verification remains pending. Questions 1 and 3 are unchanged; Question 2 remains negative within the tested domain."
    new_tail = old_tail[:-len(" Questions 1 and 3 are unchanged; Question 2 remains negative within the tested domain.")] + " `0.24.1` freezes the separately implemented PV1-B checker and its complete comparison contract after the primary report checkpoint; no official checker result exists yet. Questions 1 and 3 are unchanged; Question 2 remains negative within the tested domain."
    text = replace_once(text, old_tail, new_tail, "version history")

    old_handoff = "A new researcher must re-read current rules and verify the current `develop` head, this report, and `research/lineum-public-tolog-b4/artifact-manifest.json`. Treat the localized checker, `Q2-O1`, `Q2-SA1-A`, and `Q2-PV1-A` as already completed at the bounded evidence levels stated above. Preserve all technical non-results rather than rewriting history. Treat `q2-ledger-neutral-control.json` as a supported-runtime **primary only**, with the exact result `26 available / 2 unavailable / 0 neutral failures / 0 Q2 rescues / 0 classification changes`. Execute only a separately implemented PV1-B checker next; do not select a reciprocal, phase/interference, compaction, Stage-B spatial, or new-field replacement before that checker closes. Keep all subsequent work strictly mapped to Q1, Q2, or Q3 and return to programme-level prioritization after this validity chain rather than expanding Q2 indefinitely."
    new_handoff = "A new researcher must re-read current rules and verify the current `develop` head, this report, and `research/lineum-public-tolog-b4/artifact-manifest.json`. Treat the localized checker, `Q2-O1`, `Q2-SA1-A`, and `Q2-PV1-A` as already completed at the bounded evidence levels stated above. Preserve all technical non-results rather than rewriting history. Treat `q2-ledger-neutral-control.json` as a supported-runtime **primary only**, with the exact result `26 available / 2 unavailable / 0 neutral failures / 0 Q2 rescues / 0 classification changes`. The independent PV1-B checker is frozen at commit `927c24682d1075b3fb0eb08185a14e830dfcef45`, source blob `50a26bcfc7ef16af33f192b97eb99690e8a13fea`, test blob `937e0c1e36c1bdad4a84749aec11ef19ffecb4d5`, and protocol blob `54e381428d49ba8e8aa944f8072fa281bf15d43a`; execute only that supported-runtime checker next. Do not select a reciprocal, phase/interference, compaction, Stage-B spatial, or new-field replacement before the checker closes. Keep all subsequent work strictly mapped to Q1, Q2, or Q3."
    text = replace_once(text, old_handoff, new_handoff, "handoff")

    REPORT.write_text(text, encoding="utf-8")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    files = manifest.setdefault("files", {})
    files["research/runners/lineum_b4_q2_ledger_neutral_control_check.py"] = {
        "git_blob_sha": "50a26bcfc7ef16af33f192b97eb99690e8a13fea",
        "role": "frozen separately implemented Q2-PV1-B independent checker source",
    }
    files["tests/research/test_lineum_b4_q2_ledger_neutral_control_check.py"] = {
        "git_blob_sha": "937e0c1e36c1bdad4a84749aec11ef19ffecb4d5",
        "role": "frozen Q2-PV1-B independent checker regression tests",
    }
    files["research/lineum-public-tolog-b4/q2-ledger-neutral-control-check-protocol.json"] = {
        "git_blob_sha": "54e381428d49ba8e8aa944f8072fa281bf15d43a",
        "role": "Q2-PV1-B independent checker preregistration before official execution",
    }
    manifest["q2_ledger_neutral_control_checker"] = {
        "scientific_status": "frozen_before_official_execution",
        "checker_commit": "927c24682d1075b3fb0eb08185a14e830dfcef45",
        "checker_git_blob": "50a26bcfc7ef16af33f192b97eb99690e8a13fea",
        "test_git_blob": "937e0c1e36c1bdad4a84749aec11ef19ffecb4d5",
        "protocol_git_blob": "54e381428d49ba8e8aa944f8072fa281bf15d43a",
        "compare_atol": 1e-8,
        "compare_rtol": 1e-12,
        "local_preflight_tests_passed": 12,
        "local_preflight_numpy": "2.3.5",
        "local_preflight_scientific_status": "unsupported_runtime_helper_preflight_only",
        "official_result": None,
    }
    MANIFEST.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("report_sha256", hashlib.sha256(REPORT.read_bytes()).hexdigest())
    print("manifest_sha256", hashlib.sha256(MANIFEST.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
