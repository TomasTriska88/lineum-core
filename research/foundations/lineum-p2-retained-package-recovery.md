# Exact P2 Source-Schedule Recovery — Retained Package Inventory

**Status:** active; bounded source-recovery checkpoint (not scientific validation)
**Version:** 0.1.7
**Evidence cutoff:** 2026-11-22
**Programme membership:** continuous-source cosmology / generic particle-formation investigation
**Programme root:** `research/foundations/lineum-continuous-source-cosmology-validation.md`; verified immutable blob `3fba3925553cd5596e46c02fa35d1db91523537d`, 67,002,835 bytes. Root v0.4.14 / cutoff 2026-07-29 is **as cited** by the prior recovery brief, **not yet independently inspected within the full root body** in this checkpoint.
**Immediate provenance:** `research/foundations/lineum-root-programme-cross-branch-priority-review.md` (prior recovery decision, reviewed via the bounded `lineum-p2-retained-package-recovery-brief.md`); `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, blob `5304874451caf32313ad0e8e3c59e53958698d79`; `research/foundations/lineum-p2-retained-package-recovery-brief.md`, blob `7d2ecd83812e5c6446c694f7505839c18aa94153`.
**Branch and retrieval identity:** `TomasTriska88/lineum-core`, `develop`, source pinned at `093ec378164d190183332f6cff24023e24691f23`.
**Confidence:** high in the transport/hash verification below; **unknown** in exact P2 package completeness, replay validity, and long-term physical interpretation.
**Scope:** source retrieval only; this is the authoritative **in-progress** receipt for the existing P2 recovery lane. Do **not** assign A–F top-level outcome until the required current/historical inventory is sufficiently complete.

## 1. Question and explicitly bounded objective

Can the original P2 centered-only C0 finite-run source schedule and its **same** source-off baseline be recovered from repository-local material, and, only if complete, replayed without changing equations, observer, seeds, schedules or thresholds?

This task does not establish a persistent particle, physical energy budget, long-horizon stability, zeta-zero spacing, or any relationship between the physics solver and Lina EI. The earlier prime-grid research is an external mathematical reference and has no authority to set P2 parameters.

## 2. Historical matching coordinates, **NOT independently reproduced**

The previously retained recovery brief describes a 32×32 periodic grid, exact vacuum start, `dt=0.1`, 12 paired seeds, C0 source active through model time 20 and off to 60, common time-indexed random arrays, a frozen v3 transport observer, late-window defect population and source accounting. Historical reported late-window mean defect count `20.5232`, final-frame mean `15.6667`, minimum resolved fraction `0.941535`, and extinction `0/12` in C0 are **retrieval targets only**. The comparison F0 formation-only extinction `12/12`, mean model time `28.13`, likewise remains historical. These values have **not** been checked against original complete package or numerically reproduced in this checkpoint.

Known physical/observer cautions from the prior brief/ledger: source-off transport is not automatically object identity or long-run persistence; whole-movie population fails and stable identity was not assigned; the historical F0 source had a nonzero conditional pump rather than a closed physically debited reservoir. The exact effect of these caveats on any newly recovered P2 implementation is **not yet compared**.

## 3. Verified Git infrastructure recovery — complete immutable root blob

Previous notebook-local `git ls-remote` failed due to DNS. The existing Home Assistant operational manual and bridge annex were read **before** invoking Prcek. The existing `shell_command.chatgpt_host_exec` route was used without new host integration, service change or any production-grid write.

**Read-only command identity:** `lineum-p2-blob-stream-check-20261122-x6r5`.
**Enqueue:** one atomic append to `HA_COMMANDS`; separate `HA_RESPONSES` readback matched this exact command ID, with `command_claimed` and final `success/executed`.
**Nested host result:** `service_response.returncode=0`, stdout as follows, stderr empty:

```text
HTTP_STATUS 200 CONTENT_LENGTH 67002835
BYTES 67002835 EXPECTED 67002835
GIT_BLOB_SHA1 3fba3925553cd5596e46c02fa35d1db91523537d
MATCH 1
TERM_COUNTS {'P2': 9599, 'C0': 4961, 'source-off': 34}
```

The request streamed the raw public file from the commit-pinned URL

`https://raw.githubusercontent.com/TomasTriska88/lineum-core/093ec378164d190183332f6cff24023e24691f23/research/foundations/lineum-continuous-source-cosmology-validation.md`

through Python standard-library `urllib.request` on Prcek in 131,072-byte blocks, without transmitting the 67 MB contents through the Google Sheets mailbox and without altering the running Grid. SHA-1 was calculated as a **Git blob**, i.e. `SHA1(b"blob " + str(size).encode() + b"\0" + full_bytes)`, not as the bare file SHA-1. Thus byte count and exact immutable repository blob identity both match.

**Interpretation:** this definitively resolves the earlier **large-file transport/integrity access limitation** for this specific historical blob on Prcek. It does **not** identify an executable P2 runner, establish an exact P2 observer, recover the complete source schedule, verify model outputs, or prove an available Git write path. Token occurrences are lexical counts only, not evidence that a complete runnable package exists.

**Independent authority:** GitHub immutable blob SHA and complete response were compared to the pre-existing recovery brief. Only technical identities and aggregate counts, not raw research contents, entered the administrative mailbox.

## 4. Source-code / historical coverage inventory

| Required category | This checkpoint | Evidence class |
| --- | --- | --- |
| Root report bytes | Complete 67,002,835 bytes successfully streamed and Git-blob SHA verified | `exact_root_bytes_accessible`; root contents not yet scientifically reviewed |
| Source P2/C0 package | Not inventoried from root body yet | `unresolved` |
| Existing runners in `scripts/research/`, tests in `tests/research/` | Previous filename-only inventory; no exhaustive current/history content audit | `not_yet_exhaustive` |
| Root report lineage and previous verdicts | Recovery brief and continuity ledger read; complete root body still pending bounded review | `partial_documentary` |
| Historical commit branches, moves and deletions | Not exhaustively searched | `not_yet_exhaustive` |
| Exact environment and paired RNG | Not extracted from original runner | `unresolved` |
| Frozen v3 observer and source ledger | Not extracted from original runner | `unresolved` |
| Retained baseline outputs and hashes | Matching coordinates from brief only | `unresolved` |
| Baseline replay / independent verifier | Not run | `not_executed` |

This is **not** outcome `D_partial_package_only` or `E_not_located_after_exhaustive_local_search`: those are final classifications that require more evidence. No single top-level A–F verdict is asserted now.

## 5. Reproducible source integrity method

Given an immutable public raw source URL, the original file byte size `67002835` and the frozen expected blob `3fba3925553cd5596e46c02fa35d1db91523537d`, compute:

```python
import hashlib
import urllib.request

size = 67002835
expected = "3fba3925553cd5596e46c02fa35d1db91523537d"
url = ("https://raw.githubusercontent.com/TomasTriska88/lineum-core/"
       "093ec378164d190183332f6cff24023e24691f23/"
       "research/foundations/lineum-continuous-source-cosmology-validation.md")
digest = hashlib.sha1(("blob " + str(size) + "\0").encode())
count = 0
with urllib.request.urlopen(url, timeout=20) as response:
    assert response.status == 200
    while part := response.read(131072):
        digest.update(part)
        count += len(part)
assert count == size
assert digest.hexdigest() == expected
```

This exact procedure verifies Git file integrity, **not** the semantic correctness of its contents. The original experiment and observer must be independently inspected and verified separately.

## 6. Decision, programme impact, and next exact permitted step

**Local verdict:** `large_root_blob_retrievable_and_byte_verified`; `P2_package_not_yet_recovered`; `no_new_scientific_result`.

Programme relationships: source recovery **depends_on** the continuous-source root and applies to its P2 C0 historical lane; it **constrains** subsequent C0 long-horizon design and P3/P4 intervention; existing negative observer and energy-accounting caveats remain `unaffected` and `not_yet_compared` to the complete original P2 implementation. The standalone prime-grid/zeta study remains external `unaffected`, not a subprogramme. Lina EI Grid observations are not transferred into Core.

**Next permitted work:** safely search the now-confirmed byte-accessible complete immutable root for precise P2 code, runner, observer, randomness, event/source schedule, environment, preserved outputs and hashes. Use **short read-only, bounded** source-pinned probes via the existing Prcek bridge if necessary. Include versioned `scripts/research/`, `tests/research/`, history and prior branches in the recovery matrix; distinguish executable code from prose/ephemeral names. Capture every decision-relevant new finding in this same active report **before** proceeding to the next consequential step.

Once a *single* complete candidate has been retrieved, freeze its execution environment and replay **only** the original P2 baseline with an independent checker and the prescribed negative controls. If source recovery is incomplete or multiple incompatible variants exist, preserve the uncertainty and stop rather than manufacturing a replacement.

**ClickUp:** read-only parent `869dpg9hb` in workspace `90121717552` currently reports `to do`; no ClickUp status change. **No whitepaper promotion. No solver or running Lina EI Grid change.** No physical experiment was run, and the prior "all nine Git access regressions passed" claim has not yet been reproduced from the full current checkout as part of this P2 receipt.

## 7. Checkpoint 2 — verified root outline, scope correction, and isolated access regressions (2026-11-22)

**Version:** 0.1.2. This is a bounded **index and tool-policy verification**, not recovery of the P2 C0 executable or its baseline replay.

With a second separate, source-pinned **read-only** Prcek host probe (command ID `lineum-p2-heading-index-20261122-b9k2`, HA response final `success/executed`, nested returncode **0**, empty stderr), the immutable 67 MB root file was scanned *line-by-line*, with no transfer of its contents through the mailbox. The exact header independently confirmed:

- Root title: *Continuous Replenishment, Cosmological "Fuel," and Long-Horizon Lineum Dynamics*.
- Root status: active standalone research report (its own wording, notwithstanding the later programme hierarchy).
- Root version: **0.4.14**, evidence cutoff **2026-07-29**; these metadata are now **directly inspected from the root**, not merely cited via the recovery brief.
- Text: **1,671,106 lines**; maximum raw line length **4,929,462 bytes**; **170** detected fenced-code delimiters; **38** broadly matched replay/runner mentions under the intentionally shallow lexical filter.
- The bounded heading search showed **71** P2/C0/source/observer-related headings (first 55 returned); examples are P2.3 operator-audit programs, P2.4 standalone pilots and independent verifiers, P2.5 Fountain-accounting code and output, P2.6 multilevel code/output, P2.7 energy-ledger code/verifier, and P2.8 walking-droplet tests. Their presence confirms the root **contains real self-contained code and retained outputs**, but does **not** make any of those P2.3–P2.8 programmes identical to the earlier *P2 centered-only C0 source-off* schedule under investigation.

**Important collision of labels:** `P2` appears as a generic experiment stage and as prefixes in many other named programmes (`P2.3`, `P2.4`, `P2.5`, `P2.6`, `P2.7`, `P2.8`). A filename/heading match on `P2` is **not proof of executable lineage**. Next search must target *C0 schedule through model time 20 and off through 60*, exact seeds and observer definitions. Do not replay another available P2.* pilot merely because it has code.

The prior Git-access routing regression's **byte-exact** `scripts/agent_git_access_fallback.py` module was reconstructed in an isolated assistant runtime and checked by local `git hash-object` against the repository blob `6fdcaecc09db26d7d7680c69147e3a581cd213e1`. **Eight** logic tests mirroring the eight substantive scenario tests passed in `python -m unittest`; the ninth test's literal policy assertions were instead verified directly against the actual `.agent/rules.md` and existing test file through the GitHub connector: no expected policy token was missing. This is **not** a full checkout test run and **does not** verify the GitHub Actions job executed. The earlier blanket claim that all nine tests ran as a full suite before publication remains unsubstantiated.

**Local verdict:** root recovered and independently verifiable **as bytes and headings**; exact C0 runner/observer/schedule and versioned output **still unresolved**; no A–F recovery classification, no original baseline replay and no new physics claim. The earlier header/size access blocker is now closed. The genuine scientific recovery gate remains open.

**Next step frozen:** perform a narrowly bounded exact-text search of the now-accessible root for the C0 schedule, seed/observer and command/outcome indicators, preserving line numbers and source SHA; then inspect only relevant bounded sections. Record candidate identities and mismatches in this report before attempting any runnable-source package or historical-Git search. Observe the ~50-second host command limit. Never change the live Lina Grid, HA, source code or the proven root report during recovery.

## 8. Checkpoint 3 — exact C0-target search exposes a cross-report source mismatch (2026-11-22)

**Version:** 0.1.3. Another standalone, commit-pinned, **read-only** full-byte scan was executed on Prcek through the authorized bridge with command ID `lineum-p2-c0-locator-20261122-c7j4`. A matching final HA response reported `success/executed`, nested `returncode=0`, and empty stderr. The Python scanner simultaneously recomputed the **same Git-blob SHA** and counted all **1,671,106** source lines, so these are source-pinned lexical checks rather than results from an unverified partial fetch.

**Literal per-line presence across the entire original 67,002,835-byte root report:**

| Exact search token | Number of matching lines |
| --- | ---: |
| `20.5232` | 0 |
| `15.6667` | 0 |
| `0.941535` | 0 |
| `0.99999892` | 0 |
| `centered-only` | 0 |
| `source-off-to` | 0 |
| `v3 transport` | 0 |
| `C0` (case-insensitive) | 2,265 |
| `absolute-time` | 1 |
| `source schedule` | 2 |

The first `C0` matches were at line numbers `430,444,563,615,1972,1979,2011,2019,2020,2022,2025,2027`; `absolute-time` at line `2102`; `source schedule` at `1593291,1604679`. No same-line `C0` plus `source off`/`source-off`/`t=60` combination was found in this bounded check.

**Interpretation (important):** the root report is byte-complete and internally clearly about P2.3–P2.8 continuous-replenishment/Fountain experiments, **but does not contain the listed exact P2 centered-only C0 late-window metric strings or distinctive literal wording**. This is a source-reconciliation problem affecting the recovery brief's assumed lineage, **not** evidence that the historical C0 simulation never ran or that its reported numbers are wrong. The metrics might belong to a different programme report, a separate path, another branch, a historical commit, differently written precision, or an unversioned receipt; none is yet verified.

**Bounded negative:** `target_exact_literals_absent_from_large_root`; **not** `E_not_located_after_exhaustive_local_search`. No completed provenance matrix, no accepted candidate runner, no replay. Stop treating this root's code appendices as the sought C0 executable simply because of their P2 labels.

**Next permitted and now more discriminating step:** search the actual repository files and immutable Git history for the **unique numerical targets** `20.5232` and `0.941535` plus `centered-only`/the 12-paired-seed C0 challenge, resolving the true report and historical commit before expanding any runnable environment. The authoritative P2 recovery brief remains the goal but its root-path assumption is explicitly **under challenge**. No scientific interpretation or long-horizon experiment follows from this mismatch.

## 9. Checkpoint 4 — locating the real provenance of target P2 metrics (2026-11-22)

**Version:** 0.1.4. Following the source-pinned negative lexical scan, the exact previously cited numerical target strings were checked against the two current programme decision/continuity documents on `develop`:

- `research/foundations/lineum-root-programme-cross-branch-priority-review.md` at blob `9b1217f4757d2f0a9fb566284a91ac7e5a3c010d` **contains** `20.5232`, `15.6667`, `0.941535`, and `centered-only` in its summary of prior numerical observations. Its published version is 0.1.0, evidence cutoff 2026-07-31, and it explicitly calls itself a **decision/re-ranking report**, not original executable evidence.
- `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md` at blob `5304874451caf32313ad0e8e3c59e53958698d79` also repeats all three target numbers and `centered-only`, but is a programme **continuity synthesis**, not the source-of-truth P2 executable.
- `research/foundations/lineum-field-autonomy-observer-transfer-validation.md` at blob `a5721954847bd12ff74633f1d0bb54d2224831f1` contains **none** of these target metric strings or `centered-only`; it cannot be silently substituted.

A read-only recursive Git tree enumeration of commit `8f1b94445d34d43a4bbc1ba6930b84d229fbcbdd` returned **1,265 entries, truncated=false**. Filtering for `research/` source/plain files below 400,000 bytes gave **189** candidates for the next bounded path/content audit. This is a **candidate count**, not 189 files inspected. A subsequent broad batch content-fetch attempt was rejected by the tool-call limit **before any complete candidate search result**; no exhaustive discovery claim is made. The GitHub search connector searches the default `main` branch and yielded no matches for the numerical targets, which **cannot** be interpreted as their absence on the active `develop` branch.

**Strongest supported reconciliation:** the exact values have *decision-report/ledger provenance*, while the huge root report's full bytes do **not** contain these exact strings. Their true originating runner/observer/immutable output remains unidentified. The recovery brief's attribution to the huge root requires explicit correction or a demonstrated historical link; we have not yet proven which report or branch originally generated the C0 metrics.

**Programme verdict:** prior observational claims remain **historical/reported, not independently replayed**. No scientific negative is concluded about C0 stability. The next permitted action is a **small, pagination-safe** read-only content/history inventory of the 189 current research candidates and relevant historical commits, prioritizing `centered-only`, original seeds/observer, and numerical target values. Preserve exact paths/blobs for any genuine P2 execution artifact. Avoid a single 40-call parallel request, which already exceeded the connector's limit. Only a complete compatible candidate authorizes baseline replay; no long continuation, P4, equation or whitepaper changes follow yet.

## 10. Checkpoint 5 — first small-batch current-tree inventory finds a descendant summary, not the runner (2026-11-22)

**Version:** 0.1.5. An immutable current-tree inventory of `8f1b94445d34d43a4bbc1ba6930b84d229fbcbdd` identified 189 text candidates under `research/` (extensions Markdown, Python, JSON and TXT, each less than 400,000 bytes). **Exactly the first 32 lexically sorted candidates**, from `research/audits/lineum-ai-claims-matrix.md` through `research/foundations/lineum-core-deterministic-state-transplant-pilot.md`, were fetched successfully in **two 16-file bounded batches**, with no connector errors. This is partial current-tree coverage only: not a complete historical or runner search.

The only inspected file in this batch containing all of `20.5232`, `0.941535` and `centered-only` was `research/foundations/lineum-collective-vortex-particle-identity-preregistration.md` (blob `3c84624ed0a0bd961d7e344a3629761c2d8b2fc0`, status active preregistration v0.1.0, cutoff 2026-07-31). It labels those same values **"reproducibly observed in the retained P2 summary"** and states the continuity ledger records **168 trajectories (two source families × seven schedules × twelve seeds)**. Crucially, it also explicitly says the exact runner/observer/state package is **not recovered** and must be recovered before any intervention. This document is therefore **a descendant hypothesis and summary, not recovered executable source**. It distinguishes collective, privileged-core, and non-identifying vortex-gas hypotheses, but none may be promoted without the original package.

Three other inspected files contained only broad `source-off` wording rather than the unique target metric pair: `research/foundations/lineum-ancient-texts-dynamic-boundary-protocol-and-reconstruction-hypotheses.md` (blob `07f75308c45733fe68075ffca1b6517a164c2c0e`), `research/foundations/lineum-collective-member-turnover-protocol-fixture.md` (blob `25ebd303bc8ac4a66cc53439c1cfbaec8d8ba048`) and `research/foundations/lineum-core-active-growth-scaffold-repair-matrix.md` (blob `1569be5867da8377d2a09c69147d0bffd9594703`). A `source-off` mention is **not** proof of the target P2 executable.

**Result:** further corroboration that later 2026-07-31 descendants report the C0 numbers, while **none of the first 32 inspected small research files supplied an original P2 runner**. This is **not** an exhaustive absence verdict. **Next action:** continue the remaining 157 current text candidates in small, source-pinned read-only batches; then inspect version history and candidate executable references. Record each materially new source finding here before deciding on replay. No equations, code, whitepapers, Lina runtime or new simulations were modified.

## 11. Checkpoint 6 — all 189 bounded current research text candidates inventoried (2026-11-22)

**Version:** 0.1.6. The previous incomplete bulk call was replaced by **twelve bounded batches** (eleven of 16 files and one of 13), each using read-only `fetch_file` on the **immutable** source-tree commit `8f1b94445d34d43a4bbc1ba6930b84d229fbcbdd`. All **189/189** lexically sorted `research/` blob paths matching `*.md, *.py, *.json, *.txt` and `size < 400000` bytes were fetched and scanned; **0** per-file fetch failures. Tree inventory: **1,265 entries**, `truncated=false`. The large root report (67,002,835 bytes) was independently and fully hash-checked and lexically scanned through the Prcek read-only bridge in Checkpoints 1–3; it was deliberately excluded from the small-file connector inventory.

**Where exact target values are repeated among those 189 current research files:**

- Decision synthesis: `research/foundations/lineum-root-programme-cross-branch-priority-review.md` (blob `9b1217f4757d2f0a9fb566284a91ac7e5a3c010d`) and `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md` (`5304874451caf32313ad0e8e3c59e53958698d79`).
- Later hypothesis/preregistration: `research/foundations/lineum-collective-vortex-particle-identity-preregistration.md` (`3c84624ed0a0bd961d7e344a3629761c2d8b2fc0`) and `research/foundations/lineum-core-envelope-wake-and-attraction-preregistration.md` (`621cc5f9147dde4a3819e9fc2d3febe05e387cf8`).
- Recovery instructions and receipts: `research/foundations/lineum-p2-retained-package-recovery-brief.md` (`7d2ecd83812e5c6446c694f7505839c18aa94153`) and this recovery report (snapshot blob `74dd1ee2f156eae7d2515c760d490e2245ad054b`, then amended).
- Independent **later recovery audit**: `research/linon-collision-dynamics.md` (blob `79f7b4c65cd62074f3fa546219997487a482dc89`) repeats `20.5232` and the centered-only C0 story in a provenance section. It records that an intermediate root at commit `d2a144e12f077d0dd7df3c127f11ee890cfad87a` / 62,462,594 bytes had **none** of several key C0 numerical fingerprints, and that a later large root increment at `729e1f40ee268e6811e4d14f1b5efc1f0ce8b2e9` had been **unreviewed due to tool size limits**. Our new, hash-confirmed complete latest-root scan now independently resolves that older *access uncertainty* for the exact literals: they remain absent even in the current final 67MB root blob.

Other scanned files sometimes contain generic `source-off`, `C0` or `centered-only` wording without the unique target metric pair, but wording alone cannot establish execution lineage. In particular, the known `P2.3–P2.8` root experiments are different protocol families and cannot replace the target P2 C0 source-schedule.

**Verdict of the bounded current research text search:** exact P2 C0 metrics survive as **later claims/summaries**; no **matching original P2 executable plus v3 observer and preserved output** has been identified by this numerical-fingerprint/terminology search. This is **not** proof that no original runner exists: a runner need not include outcome numbers, can be renamed, encoded in a historical Git object, live in `tests/` or `scripts/` outside `research/`, be larger than the selected size threshold, or be unversioned.

**Remaining A–F recovery prerequisites:** inspect all current eligible `tests/` and `scripts/` code for source schedules and observer definitions, then historical Git commits, deleted/renamed files, relevant branches, run instructions and source/output hashes. Replay only after exact code, observer, RNG, schedule, environment and saved expected output are found. There is **no completed A–F verdict**, no new Lineum physics run, and no authorization to infer particle identity or long-horizon stability.

## 12. Checkpoint 7 — first source-family origin recovered from historical commits (2026-11-22)

**Version:** 0.1.7. Read-only Git history now yields a **new concrete historical source candidate**, rather than a generic P2 text match. Direct GitHub commit inspections (not a search-result guess) confirmed:

| Source commit | UTC date | Commit message | Exact changed file | Retained blob and size |
| --- | --- | --- | --- | --- |
| `09f59c9eaf5bb31c32b571b5c1c03f072d6240d1` | 2026-07-18 16:29:22 | `research: map source-off winding persistence` | `research/foundations/lineum-physics-philosophy-validation.md` | `cefa63c8007667481122a2b6df7dd3fb6f5aaf0d`, **4,202,805 bytes** |
| `74c7be30e2b5690944581bd4f06ee5eff3775ffe` | 2026-07-18 14:23:35 | `research: separate pumping from winding maintenance` | same historic path | `5e62c39eb69e390a262d9be9a99e4c4c53b2f197`, **2,110,772 bytes** |
| `9e7c5602066299f035ce50120746618fe3a9d614` | 2026-07-18 13:26:34 | `research: distinguish source pump from physical fuel` | same historic path | history only; detailed blob not yet indexed |
| `7657f1edb6bc0cf53c4a473999dedbd7ca77d13b` | 2026-07-18 10:45:35 | `research: validate source-blind linon observer` | same historic path | history only; detailed blob not yet indexed |

**Significance:** this *historical* report is scientifically closer by its commit message and sequence to the sought centered-only, source-off, winding observer P2 experiment than the later 67MB **continuous-replenishment/P2.3–P2.8** root report. The old report is absent from the current abbreviated working-tree report list, but is present as **real immutable Git objects**. This provides a specific next retrieval target and a likely explanation for the previously observed mismatch between the later root's topic and C0 decision summaries. The candidate is not yet proved to contain the exact sought P2 runner, outputs, seeds or observer.

The GitHub connector supplied historical tree identity and exact blob metadata, but `fetch_file(start_line=1,end_line=25)` and `fetch_file(start_line=500,end_line=530)` both returned **zero text** for the 4.2 MB historical blob despite returning its correct Git blob SHA. This is a **connector read-size limitation**, not proof of empty historical content.

A small targeted sample of the current permanent `scripts/` and `tests/` source files, including `scripts/research/active_mu_kappa_repair_matrix.py`, `scripts/research/heredity_transplant_harness.py`, `tests/test_replay_compiler.py` and `scripts/validation_core.py`, contained no conclusive exact P2 C0 runner/observer identity. It is a **partial current-code sample**, not an exhaustive negative.

**Next permitted action:** retrieve the pinned **4,202,805-byte** historical source over the existing **read-only Prcek** Git/HTTPS bridge, verify the Git blob SHA exactly, locate distinctive C0 metrics and full executable/code fences by line numbers, and inspect the matching historical embedded sections. Do **not** promote the above candidate to recovered runnable package until its code, frozen observer, RNG, schedule, outputs and environment have been independently matched. Preserve the more recent continuous-replenishment root as separate programme evidence; do not silently rewrite the declared programme lineage or infer from a commit title alone. No scientific run or whitepaper change.
