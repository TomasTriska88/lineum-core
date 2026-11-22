# Exact P2 Source-Schedule Recovery — Retained Package Inventory

**Status:** active; bounded source-recovery checkpoint (not scientific validation)
**Version:** 0.1.25
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

## 13. Checkpoint 8 — original historical report located and byte-verified (2026-11-22)

**Version:** 0.1.8. **Major provenance correction, not a numerical replay.** The new historic target from Checkpoint 7 was fetched through the existing *read-only* Prcek bridge and hashed independently against its immutable Git blob; full source was scanned for the literal P2/C0 signatures in one pass, but only aggregate counts and line locations passed through the admin mailbox.

**Exact source:** `research/foundations/lineum-physics-philosophy-validation.md` at commit `09f59c9eaf5bb31c32b571b5c1c03f072d6240d1` (2026-07-18 16:29:22 UTC), blob `cefa63c8007667481122a2b6df7dd3fb6f5aaf0d`, **4,202,805 bytes / 98,203 lines**. **Prcek command ID:** `lineum-p2-history-blob-20261122-h7p3`; matching final `HA_RESPONSES` entry `success/executed`; nested `service_response.returncode=0`; stderr empty; **`GIT_BLOB_MATCH 1`**. The original SHA, size and historical Git commit were resolved from immutable Git history **before** the host fetch.

| Exact case-insensitive token | Matched line count | First significant line numbers |
| --- | ---: | --- |
| `20.5232` | 3 | **1993, 2013, 65002** |
| `0.941535` | 1 | **2015** |
| `0.99999892` | 1 | **2016** |
| `centered-only` | 12 | 8, 18, 41, 42, 1674, 1700, 1829, 1931, 2105, 3120, 3121, 3171 |
| `source-off` | 26 | 8, 18, 42, 44, 1295, 1300, 1338, 1383, 1674, 1700, 1702, 1904, 1909, 1935… |
| `C0` | 196 | 42, 154, 839, 1208, 1757, 1766, 1777, 1781, 1818, 1842, 1852, 1951… |
| `P2` | 174 | 8, 18, 42, 43, 44, 1674, 1699, 1902, 1903, 1909, 1913, 1941… |
| `12 paired` | 2 | 3328, 3329 |
| `source schedule` | 7 | 43825, 44111, 44129, 44212, 48119, 52071, 57358 |
| `v3` | 1,073 | 42, 92, 93, 1039, 1111, 1146… |
| `15.6667` | 0 | no literal match; may use different rounding or formatting |

**Inference:** the intended P2 centered-only C0 source-off *scientific report and its unique target metrics* have now been found **in an actual historical Git object**. The earlier 67MB `lineum-continuous-source-cosmology-validation.md` is an independent later continuous-source cosmology report, not the primary carrier of these exact P2 C0 metrics. The previous statement that only later summaries carried the numeric fingerprints is now **superseded** by this verified 2026-07-18 history. **Do not conflate** file topic/lineage or overwrite the older administrative programme hierarchy before inspecting the original report.

**Still unknown:** the presence and completeness of the *embedded runnable P2 source*, original seed/RNG contract, v3 transport observer, preserved raw outputs, exact replay commands, dependencies and output hashes. A lexical match is **not** an exact runnable-package recovery or a new physical result. Top-level A–F classification remains pending; no model run occurred.

**Next permitted action:** perform a **bounded, source-pinned section read** of the historical file around lines `1674–2140` and `3320–3340`, plus enumerated code/receipt appendices around the discovered P2 schedule references. Return only concise necessary metadata/short code excerpts, not complete raw data or private content, using the same Git-blob SHA identity and authorized read-only Prcek bridge. Preserve the findings in this active report before searching or executing anything else.

## 14. Checkpoint 9 — primary P2 Section 3.18 confirmed in historical body (2026-11-22)

**Version:** 0.1.9. The now-proven historical source `lineum-physics-philosophy-validation.md` (2026-07-18 commit `09f59c9eaf5bb31c32b571b5c1c03f072d6240d1`; blob `cefa63c8007667481122a2b6df7dd3fb6f5aaf0d`) was re-read at **bounded line windows**, rechecking `GIT_BLOB_MATCH 1`. Prcek command `lineum-p2-historical-preview-20261122-q4l7` has one claimed row and a later **final executed** HA response, nested host returncode **0**, empty stderr. This read obtained the relevant content without exporting the whole historical artifact.

**Direct first-party source evidence (not a later summary):**
- **Lines 1909–1937**, `### 3.18 P2 finds a source-off multi-defect remnant and a history-gated F0 restart, not a particle`. It explicitly distinguishes C0 centered-only noise from full F0 coherent pumping: after source shutoff C0 retains a lower-density population of positive and negative winding defects for the observed finite horizon; both frozen late windows pass aggregate transport/span criteria in **all twelve paired seeds**. The complete F0 source instead smooths away the defect population; after F0 shutdown and restart, no original-level defect recovery in 12/12 prior-state seeds, while fresh-vacuum controls do form a burst 12/12. This is **descriptive history dependence**, not object identity or closed-system resource persistence.
- **Lines 1939–1946** declare the P2 schedule contract: exact vacuum, **periodic 32×32**, **h=0.1**, end at **t=60**, **12 paired seeds**, previously defined LAP4 backbone and mode coupling, disabled `mu`, optional continuous-time `phi` correction, no production-default or canonical-equation change.
- **Lines 1950–1955** give the two tested source families C0 and F0, each with the declared noise `xi` and phase factor; the scanned source excerpt does not justify inferring an external physical fuel.
- **Lines 1931–1937** explicitly warn that the final C0 population is roughly sixteen defects **on average**, not an isolated object; the v3 observer aggregates current, assigns no identities, and passes some smooth transported nulls.
- **Historical test inventory near lines 3326–3329** states that the 13th topological-transport program, 14th source-pump audit, **15th P1 factorial**, and **16th P2 source-schedule audit** were executed **twice** with byte-identical normalized output. The 16th covers **168** trajectories. This is historical experiment provenance, **not** a present-day replay receipt.
- The root's section 3.16–3.18 protocol and appendices are **a much closer direct first-party evidence source** for the target than the later continuous-replenishment root. Historical source presence is now confirmed, but the exact executable code block, independently runnable environment, saved output and hash comparisons **still require extraction**.

**Corrected source hierarchy:** P2 C0 source claims originate in **the July 18 historical physics-philosophy source**, which the July 31 cross-branch report/ledger later summarize; the later continuous-replenishment root contains distinct P2.3–P2.8 lanes. The latter remains a valid separate report, but is not itself proof of the C0 run. This checkpoint corrects the active recovery brief's assumed carrier, **without** deleting previous history or silently changing unrelated programme lineage.

**Operational outcome:** `historical_primary_P2_source_found`; runnable package `not_yet_fully_extracted`; **no A–F top-level replay classification yet**; no simulation or engine change.

**Next permitted action:** locate the historical **16th P2 code, independent verifier, full machine-readable output, embedded expected digests, and execution/reproduction command**, ideally by source-pinned heading and code-fence indexing in the historical report; extract only bounded exact sections with line numbers and keep any original scripts in permanent readable evidence if required. Execute a baseline only after source, observer, RNG, schedule, environment and expected output are fully pinned, and after the existing tests. Do not manufacture a new P2 from the written formulas.

## 15. Checkpoint 10 — full original P2 audit located in historical Appendix P (2026-11-22)

**Version:** 0.1.10. The third source-pinned, **read-only** Prcek scan of `lineum-physics-philosophy-validation.md` at historical commit `09f59c9eaf5bb31c32b571b5c1c03f072d6240d1`, blob `cefa63c8007667481122a2b6df7dd3fb6f5aaf0d`, again returned `BLOB_OK 1` with nested returncode **0** (`lineum-p2-history-appendix-index-20261122-j5a2`). **The source report contains not only P2 prose and metrics but an explicitly named, standalone *P2 Source-Schedule and Recovery Audit* in `## Appendix P` starting at line `56031`.**

Direct technical anchors from the immutable source:

- `### 3.18 P2 finds a source-off multi-defect remnant and a history-gated F0 restart, not a particle` starts at **line 1909**; the original outcome-limitation subsection starts line **2098**.
- `## Appendix M — Conserved Topological-Transport Feasibility Audit` starts at **line 33837**; `## Appendix N — Pump, Fuel, and Field-Process Hypothesis Audit` at **41803**; `## Appendix O — P1 Pump-by-Randomness Factorial` at **42509**.
- **`## Appendix P — P2 Source-Schedule and Recovery Audit` begins at line 56031**; its introduction near **56070** identifies a **standalone P2 audit of source scheduling and recovery**.
- Retained P2 output near **lines 64980–65003** includes `"late_40_60": 12`, `"formation_only_sustained_extinctions": 0` in its C0 block, and `"late_40_60_mean_defects": {"mean": 20.523217247097843, ...}` at **65000–65003**. This directly explains the older rounded `20.5232` reported in decision summaries; it is a **historical embedded output**, not a new run.
- The Appendix A reproduction log **lines 3316–3332** records Python **3.11.15 / NumPy 1.26.4** for its audit environment; Python **3.12.13 / NumPy 2.3.5** for a distinct replay environment. It says the **16th P2 source-schedule audit** was executed twice with byte-identical normalized output across **168 frozen trajectories** (two families, seven schedules, twelve paired seeds), and declares **16/16** source/JSON pairs in the historical document audit. These are **historical self-reported checks** until an independent current rerun verifies them.

**Critical source correction:** This is now a substantially more complete recovery than mere narrative source location. The full original test and its machine-readable output **appear to be preserved together** in a versioned 4.2 MB historical report. Exact boundaries, extraction, code SHA, verifier pairing, output hashes and reproducing commands still need independent verification. Do not conclude replay success or top-level `A` yet.

**Next exact permitted step:** inspect the original Appendix P's bounded fence/section layout, locate the full standalone Python code, embedded JSON output and independent verifier with exact line intervals and digests. Extract byte-faithfully into *isolated* safe local files or an approved reproducibility runner, compare its declared parameters and dependency constraints with the frozen Section 3.18 contract, and run historical baseline only after existing source tests and preregistered replay gates pass. No new horizon, physics patch, output tuning or whitepaper promotion.

## 16. Checkpoint 11 — exact embedded executable and original output blocks isolated (2026-11-22)

**Version:** 0.1.11. Independent immutable source **full-blob verification** plus streamed Markdown code-fence indexing on Prcek (`lineum-p2-history-fence-index-20261122-k8q1`): final mailbox result `success/executed`, nested host `returncode=0`, empty stderr, `BLOB_OK 1` against Git blob `cefa63c8007667481122a2b6df7dd3fb6f5aaf0d` at `09f59c9eaf5bb31c32b571b5c1c03f072d6240d1`.

**Appendix P starts at line 56031 and consists of exactly two closed fenced artifacts:**

| Role | Markdown fence | Excluded delimiters / included body | Preserved exact body size | Independent SHA-256 of raw code/body bytes |
| --- | --- | --- | ---: | --- |
| Standalone P2 executable | opening `\`\`\`python` line **56069**, closing line **59026** | lines **56070–59025**, inclusive, **2,956** content lines | **100,626 bytes** | `76d99fdbedd494a1e4ee610d2b5d054d3a202dcd1ecb781a8d8ab3134174711a` |
| P2 original full machine-readable output | opening `\`\`\`json` line **59030**, closing line **98203** | lines **59031–98202**, inclusive, **39,172** content lines | **1,969,810 bytes** | `acccf7f612072739b6609e7dab3e56f60e07494d02f7893ff405b3dc511422f1` |

The scanner ran through the **same source-pinned 4,202,805-byte historical report** and counted exactly **two** closed code fences after line 56031, with **no unterminated fence**. The Python block opens with a standalone P2 source-scheduling/recovery audit docstring. The JSON block begins with a `decision` object that includes `any_population_stable_overall_transport_candidate: false`, a crucial **negative**: it is not a blanket claim that a stable particle exists.

**Major recovery milestone:** exact original executable **and** its full historical output are **present, immutable and byte-addressable in the same Git history object**. The former concern that only narrative P2 summaries survived is resolved. **This is not yet a successful replay.** Code imports, full reproducibility parameters, seed indexing, frozen observer, whether a separately executable independent checker exists, environment, and current replay comparability still require explicit inspection; the JSON output has not yet passed a present-day independent verifier.

**Portable extraction specification (do not strip whitespace or normalize line endings):** obtain the source blob at historical ref `09f59c9eaf5bb31c32b571b5c1c03f072d6240d1` and verify its Git blob hash. Extract raw bytes of exactly the numbered line ranges above using `b''.join(stream.readlines()[56069:59025])` for Python and `b''.join(stream.readlines()[59030:98202])` for JSON in one-indexed coordinates; verify the declared individual SHA-256 hashes before execution. (An implementation may stream instead of loading all lines; use the same raw ranges and no delimiter lines.) These numbers are frozen evidence identifiers, not permission to change source or fabricate missing files.

**Next execution gate:** perform a **read-only static audit** of the 100,626-byte Python content (imports, compile check, entry point, exact declared seed stream, numerical configuration, observer contracts and expected output comparison) plus JSON shape/digests. Do not execute the complete 168-trajectory numerical programme until its expected runtime/resource load, dependency requirements and baseline comparison are reviewed and frozen. The root report is a historical source archive, not new Lineum physics code. No P2 long-horizon continuation or new scientific interpretation is authorized.

## 17. Checkpoint 12 — independent static verification and dependency gate (2026-11-22)

**Version:** 0.1.12. A fourth **read-only** historical P2 source probe (`lineum-p2-historic-static-audit-20261122-m2u6`) completed via the existing Prcek mailbox with **final** `success/executed`, nested `returncode=0`, empty stderr. The historical full blob was reverified: **4,202,805 bytes**, Git blob `cefa63c8007667481122a2b6df7dd3fb6f5aaf0d`. Both inline bodies were extracted using the frozen exact line ranges and independently SHA-256-verified at the **byte** level:

- Executable Python: **100,626 bytes**, `76d99fdbedd494a1e4ee610d2b5d054d3a202dcd1ecb781a8d8ab3134174711a`.
- Historical JSON output: **1,969,810 bytes**, `acccf7f612072739b6609e7dab3e56f60e07494d02f7893ff405b3dc511422f1`.

**Static checks executed, not inferred:** `ast.parse(...)` **PASS**; `compile(...,'exec')` **PASS**; `json.loads(original_json)` **PASS**. No original simulation was executed.

**Extracted executable dependencies:** Python standard library `hashlib`, `json`, `math`, `platform`, `dataclasses`; external `numpy`, `scipy`, `scipy.optimize.linear_sum_assignment`. The current Prcek host-default `python3` reported Python **3.12.3**, with NumPy **not importable** (`ModuleNotFoundError`); therefore full replay under that interpreter is **not executable in its observed present state**. This finding does not establish that another isolated environment on that host lacks NumPy/SciPy. **No packages were installed or environment modified**, and no Lina EI Grid process was touched.

**Original code structure:** verified module AST exposes a `Config` class, `initial_state`, `source_components`, `backbone_step`, frozen v3-related topology/transport functions (`periodic_winding`, `spacetime_current`, `minimum_toroidal_transport`, `topology_metrics`), `run_lane`, `aggregate_lane`, `unit_controls`, `build_decision`, `build_result`, `main`, plus separate `p2_schedule_is_on`, `p2_random_draw_schedule`, `p2_source_components` and P2-specific helpers. **There is a module entrypoint**; exact execution gating is pending review. Literal source line `SEEDS = tuple(2026242000 + index for index in range(12))` at extracted Python line **31**, and `DT = 0.1` at line **28**. This provides independent cross-checks of seed count and timestep against Section 3.18.

**Retained JSON envelope:** parseable top-level keys `decision`, `frozen_protocol`, `limitations`, `reconstruction_provenance`, `result_payload_sha256_before_hash_field`, `runtime`, `schema`, `source_results`, `unit_controls`. Critically, its `decision` holds `any_population_stable_overall_transport_candidate`, `any_population_stable_window_transport_signal`, `history_contrast_establishes_memory_mechanism`, `source_schedule_establishes_particle_identity`, `source_schedule_establishes_physical_fuel`, and explicit forbidden/permitted claims. This is a sophisticated **bounded negative/positive verdict structure**, not proof of a sustained individual particle.

**Evidence state:** original source and output are **fully byte-located and syntactically valid**. The earlier claim that exact P2 original executable was unavailable is **superseded**; the currently **unmet** gate is an appropriate dependency/runtime setup, retained source/provenance contract review, independently checked output and baseline rerun. The root's historical Python/NumPy audit and replay environments (3.11.15/NumPy 1.26.4; 3.12.13/NumPy 2.3.5) must be distinguished from the present Prcek host-default Python 3.12.3 missing NumPy.

**Next permitted action:** inspect **only small original JSON metadata and frozen-protocol fields**, the AST entrypoint/seed and source-schedule contracts, and environment availability of an **already existing isolated** interpreter that meets NumPy/SciPy requirements; do not install or disrupt packages on the live Grid host and do not execute a long 168-trajectory baseline without the original timing/correctness gate. If a safe local assistant runtime can receive the immutable source by a content-preserving authorized path, prefer that portable scientific environment. No A–F replay classification yet.

## 18. Checkpoint 13 — original P2 protocol, decisions and precise entrypoint (2026-11-22)

**Version:** 0.1.13. Prcek read-only command `lineum-p2-historical-protocol-20261122-p3e5` completed with matching final `HA_RESPONSES`, nested returncode **0** and empty stderr. The immutable historical root blob and both P2 Python/JSON SHA-256 body hashes were independently rechecked before this static inspection. No historical simulation execution occurred.

**Original Python module entrypoint:** extracted source lines **2932–2956** define `p2_main()`, build `p2_build_result()`, serialize with `json.dumps(..., ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)`, compute `result_payload_sha256_before_hash_field` from the **pre-hash** JSON canonical serialization, then print the resulting pretty JSON. The module `if __name__ == "__main__":` executes `p2_main()` (not the earlier P1 `main()` function). This is necessary for exact replay and for independently verifying the archived JSON's self-checksum.

**Historically reported environment in the original JSON:** `CPython 3.11.15`, `NumPy 1.26.4`, `SciPy 1.17.1` (original report `runtime` field; **not** the current host environment).

**Frozen P2 protocol in the archived JSON**:
- grid `32×32`, periodic boundary, exact-vacuum initial field, `dt=0.1`, duration `60.0`, `600` updates, observation cadence `0.1`;
- **P2-specific** paired seeds `2026245000` through `2026245011` (12). **Important:** source line 31 uses a distinct `SEEDS=2026242000..2011` for the earlier embedded **P1** programme; do not mistakenly reuse it for P2.
- source families `C0_centered_only` and `F0_full`; seven schedules `always_on`, `continuous_dose_30`, `formation_only_20`, `gap_restart_20_40`, `late_only_40`, `never_on`, `pulse_5_on_5_off`, totaling **168** trajectories;
- common random numbers fixed by paired seed and **absolute update index**; turning the source off leaves draws unused rather than shifting the future stream;
- key windows formation `0–20`, gap `20–40`, late restart `40–60`, baseline `15–20`, early late-off level `35–40`, late restart level `55–60`;
- frozen v3 thresholds: minimum consecutive span `15.0`, seed prevalence `9/12`, registered overlap `0.9`, resolved core fraction `0.9`, time orientation `1/3`; post-result tuning explicitly **forbidden**.
- source function `p2_schedule_is_on` (Python line **1592**) uses update indices `<200` for formation, `>=400` for late-on, and `(step_index // 50) % 2 == 0` for five-on/five-off pulses; these are **update-time** rules and must not be refitted from an output trace.

**Original JSON verdict fields, not assistant interpretation:** `any_population_stable_overall_transport_candidate = false`; `any_population_stable_window_transport_signal = true`; `history_contrast_establishes_memory_mechanism = false`; `source_schedule_establishes_particle_identity = false`; `source_schedule_establishes_physical_fuel = false`. The original limitations explicitly exclude identity, derived physical energy, continuum limit, open boundaries and a valid same-state memory test. A source-off window population is **not** an overall stable individual object.

**Source-quality correction:** Earlier in this report, the archived Python line **31** was quoted as if it alone defined the recovery's seeds. That value belongs to **P1**; the exact P2 seeds above are read from the original P2 JSON frozen protocol. Preserve both as distinct source families and confirm the P2 seed definition in the Python body on the next audit.

**Next frozen check:** independently recompute the original JSON's `result_payload_sha256_before_hash_field` according to source `p2_main`, inspect `unit_controls.all_pass`, and cross-check only the C0 `formation_only_20` historical metrics against the previously reported rounded numbers. This is a standalone standard-library data-integrity test; it does **not** execute the simulator. Until executable dependencies and a safe isolated runner are available, no numerical replay or A/B recovery verdict is authorized.

## 19. Checkpoint 14 — independent original-output self-hash verification (2026-11-22)

**Version:** 0.1.14. Prcek read-only `lineum-p2-original-output-hash-20261122-c2n8`: final bridge response `success/executed`, nested returncode **0**, stderr empty. The full immutable original historical report, Python source and JSON artifact passed their previously pinned byte hashes before this verification.

Independent standard-library hash check: parse the archived JSON output, **remove only** `result_payload_sha256_before_hash_field`, serialize the remaining object with the **original** source's `json.dumps(..., ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)`, SHA-256 hash the UTF-8 bytes, and compare with the archived field.

```text
OUTPUT_SELF_HASH_MATCH 1
STORED      6545cdd908d879e61c8a1f4199673175e9aed445960e21ae6d230924c71b417a
RECOMPUTED  6545cdd908d879e61c8a1f4199673175e9aed445960e21ae6d230924c71b417a
CONTROL_ALL_PASS True
```

This verifies the self-consistency and current readability of the **historical result artifact**; it is **not** a fresh simulation or independent reproduction of its physics. `unit_controls.all_pass=True` is a flag **stored in the historical JSON** and was not re-evaluated by rerunning the programme.

**Source exact seed reconciliation:** the original 100,626-byte Python body declares **`P2_SEEDS = tuple(2026245000 + index for index in range(12))`** at original extracted source line **1564**, independent of P1's separate line-31 `SEEDS`. The former was used in the P2 loop starting near line **2377** and the result payload near line **2832**.

**JSON nesting:** `source_results.C0_centered_only` contains keys `cross_schedule_analysis` and `schedule_results`. The expected individual `formation_only_20` block is therefore **under** `source_results.C0_centered_only.schedule_results.formation_only_20`, **not** directly under `source_results.C0_centered_only`. A first direct lookup returned `{}`; this is a path mistake in the inspection helper, **not** a missing original baseline. It must be corrected before any numerical comparison or report promotion.

**Dependency/verification state:** the complete source, frozen P2 protocol, original 168-trajectory output, and output payload SHA-256 are now independently **integrity-verified**. **Replay remains unexecuted** because the default Prcek interpreter lacks NumPy and the safe isolated computation path has not yet been prepared. The local assistant container has Python **3.13.5**, NumPy **2.3.5**, and SciPy **1.17.0**, but does not yet have the byte-faithful original 100KB source artifact; no scientific equivalence across these versions is assumed.

**Next exact step:** read the **correctly nested** C0 formation-only schedule summary and archived independent unit-control details; compare all reported targets without refitting; then decide a safe isolated runtime for the exact original baseline. Do not launch new long-horizon or particle-claim experiments from a hash check.

## 20. Checkpoint 15 — exact C0 formation-only nested archive recovered (2026-11-22)

**Version:** 0.1.15. Read-only Prcek command `lineum-p2-c0-nested-values-20261122-f1t6` completed with final `success/executed`, nested returncode **0**, empty stderr. Before inspecting results the program verified the immutable original report's Git blob and rechecked its **archived output SHA-256 self-hash**. It performed **no numerical simulation**.

**Correct JSON path**: `source_results.C0_centered_only.schedule_results.formation_only_20`. The archived seven keys under `C0_centered_only.schedule_results` are `always_on`, `continuous_dose_30`, `formation_only_20`, `gap_restart_20_40`, `late_only_40`, `never_on`, `pulse_5_on_5_off`.

The **archived** C0 formation-only summary at the correct path contains:
- `formation_only_sustained_extinctions = 0`;
- `seeds_with_any_defect = 12`;
- `window_stable_candidates.late_40_60 = 12`;
- `window_v3_passes.late_40_60 = 12`;
- `late_40_60_mean_defects` is a summary object (not a scalar) whose `mean` appears as `20.523217247097843` in original Appendix P JSON around report line **65002**; exact calculator-level re-extraction for all other nested summary values is still pending.
- the historical `unit_controls.all_pass=True` is **stored metadata**, not proof of newly rerun controls.
- `overall_stable_candidates` and `overall_v3_passes` are separate archive fields and must **not** be inferred from a late-window pass. The archived decision explicitly says `any_population_stable_overall_transport_candidate=false`.

**Interpretation:** the late source-off C0 multi-defect signal is now anchored in an intact first-party program **and** its exact original machine-readable output, rather than secondary prose. This resolves the source-recovery part of the prior execution blocker, but does **not** reproduce or validate the old run in a modern environment. The fixed-horizon result is compatible with a decaying remnant; no single-object identity or physical energy claim follows.

**Gate and immediate next step:** check the original report's precise run-environment declaration and any already available isolated execution environment. If the required dependencies are missing, report the gap rather than installing packages or running heavy experiments on the live Prcek host. A complete baseline replay must use exact P2 source and frozen input contract, execute existing checks, preserve stdout and output hashes, compare archived output independently, and never re-use unrelated P1 seeds. No A–F verdict yet.

## 21. Checkpoint 16 — preregistered execution-route and P2 schedule check (2026-11-22)

**Report version:** 0.1.16. **Question:** Can the *unaltered original* P2 scheduler be executed in an isolated portable standard-library-only runtime and shown to match the archived seven schedule-duration and seed contracts? This is a preparatory **control/contract regression**, not replay of the 168-trajectory physics experiment.

**Frozen inputs (before this check):** Historical first-party `lineum-physics-philosophy-validation.md` blob `cefa63c8007667481122a2b6df7dd3fb6f5aaf0d`, commit `09f59c9eaf5bb31c32b571b5c1c03f072d6240d1`, embedded Python SHA-256 `76d99fdbedd494a1e4ee610d2b5d054d3a202dcd1ecb781a8d8ab3134174711a` and JSON SHA-256 `acccf7f612072739b6609e7dab3e56f60e07494d02f7893ff405b3dc511422f1`. The exact function `p2_schedule_is_on` is embedded at extracted Python source lines **1592–1608**. The archived JSON has `frozen_protocol.schedules` and P2-specific seeds `2026245000…2026245011`.

**Method to run now:** (1) copy only that complete source function *verbatim* into the local isolated assistant scratch environment and check syntax, not a translated or refitted version; (2) execute it for all steps `0…599` in each of the **seven original schedule names**; (3) independently compare each count to the archived JSON's `on_steps`, verify their stated `on_time=on_steps×0.1`, confirm the two original source families imply `2×7×12=168` declared trajectories, and check the expected boundaries `199/200, 299/300, 399/400, 49/50`. Freeze all labels and windows before seeing a result. Any discrepancy is a contract failure and **must not** trigger parameter tuning.

**Prcek environment probe, separate from science:** The existing read-only, short host route `lineum-p2-isolated-env-probe-20261122-z7t4` completed with final `HA_RESPONSES`, nested rc **0**, empty stderr. It tested explicit common interpreter locations without modifying any files: only `/usr/bin/python3` was present among the selected locations, reporting **Python 3.12.3, NumPy absent, SciPy absent**. A point-in-time OS availability probe returned **4 CPU cores** and `MemAvailable=4,460,504 KiB`. These checks **do not exhaustively rule out every venv** and are **not permission** to run CPU-heavy research on the live single-owner Lina host. No packages were installed, the running Grid and HA configuration were not touched.

**Execution safety:** Portable arithmetic/function controls belong in the assistant's isolated runtime, **not** in a new production HA service, production Lina Grid, or a 168-run experiment on Prcek. No numerical engine simulation, canonical code modification, or whitepaper promotion is permitted from this check. Subsequent original 168-trajectory replay still requires exact dependencies, resource bounds and independently compared output; preserve the existing historical negative decision `any_population_stable_overall_transport_candidate=false`.

**Expected outcomes by archived schedule:** `never_on=0`, `always_on=600`, `formation_only_20=200`, `continuous_dose_30=300`, `gap_restart_20_40=400`, `late_only_40=200`, `pulse_5_on_5_off=300`. These values are **predictions copied from the frozen archive**, not numbers measured by a new run. Next checkpoint must report exact pass/fail counts, interpreter identity, source-extraction limitations and blockers before any further experiment.

## 22. Checkpoint 17 — P2 frozen-schedule portable regression PASSES, full replay NOT RUN (2026-11-22)

**Version:** 0.1.17. **This is the result of the frozen Checkpoint 16 protocol, not a numerical physics validation.**

**Exact-source identity:** Extracted the **unchanged, 651-byte** `p2_schedule_is_on` function from the historical Python block lines **1592–1608**. Local `SHA-256=0612efca2fa51d897a3c40fd276fe7fcbf021ca9f3bedbda145064f3180ccaa2`. **Independent hash-on-source:** Prcek read-only command `lineum-p2-scheduler-sha-20261122-v5b6`, after verifying both the full historical Git blob and the 100,626-byte parent Python SHA-256, returned the **same** 651-byte function SHA-256 and `MATCH_LOCAL_EXPECTED 1`; final `HA_RESPONSES` success/executed, nested rc=**0**, empty stderr. This is a byte-match, **not** a hand-translated surrogate.

**Isolated runtime:** local assistant container, `CPython 3.13.5`; command `python -m unittest test_schedule -v`. **Four test methods passed** in approximately **0.001 s**; no scientific engine state was read, produced or changed. Their logic:

1. Recomputed active steps for **every original schedule** over the exact 600 indexed updates and checked against the preserved archive's `frozen_protocol.schedules[name].on_steps` and `on_time=on_steps×0.1`.
2. Checked on/off transitions around **199/200**, **299/300**, **399/400**, **49/50**, **99/100** and **549/550**; all passed.
3. Verified that an unrecognized schedule raises `ValueError`.
4. Independently checked the frozen ensemble size `2 source families × 7 schedules × 12 P2 seeds = 168`.

**Actual measured active-step counts (all equal to archived values):**

| Original schedule | Recomputed active updates / 600 | Source-on model time |
| --- | ---: | ---: |
| `never_on` | 0 | 0 |
| `always_on` | 600 | 60 |
| `formation_only_20` | 200 | 20 |
| `continuous_dose_30` | 300 | 30 |
| `gap_restart_20_40` | 400 | 40 |
| `late_only_40` | 200 | 20 |
| `pulse_5_on_5_off` | 300 | 30 |

**Exact function under test, verbatim from the source-pinned archive:**

```python
def p2_schedule_is_on(schedule: str, step_index: int) -> bool:
    """Return the frozen source state for update [t, t + dt)."""
    if schedule == "never_on":
        return False
    if schedule == "always_on":
        return True
    if schedule == "formation_only_20":
        return step_index < 200
    if schedule == "continuous_dose_30":
        return step_index < 300
    if schedule == "gap_restart_20_40":
        return step_index < 200 or step_index >= 400
    if schedule == "late_only_40":
        return step_index >= 400
    if schedule == "pulse_5_on_5_off":
        return (step_index // 50) % 2 == 0
    raise ValueError(schedule)
```

**Reproduction of independent scheduler assertions without external libraries:**

```python
expected = {
    "never_on": 0,
    "always_on": 600,
    "formation_only_20": 200,
    "continuous_dose_30": 300,
    "gap_restart_20_40": 400,
    "late_only_40": 200,
    "pulse_5_on_5_off": 300,
}
for name, count in expected.items():
    assert sum(p2_schedule_is_on(name, t) for t in range(600)) == count
    assert count * 0.1 == (count // 10)
for name, before, after in (
    ("formation_only_20", 199, 200),
    ("continuous_dose_30", 299, 300),
    ("late_only_40", 399, 400),
    ("pulse_5_on_5_off", 49, 50),
):
    assert p2_schedule_is_on(name, before) != p2_schedule_is_on(name, after)
try:
    p2_schedule_is_on("not_a_schedule", 0)
    raise AssertionError("unknown label accepted")
except ValueError:
    pass
assert 2 * len(expected) * 12 == 168
```

**Limits and contradiction impact:** This validates **only the exact schedule function and archived duration/ensemble contract**; it neither recalculates random draws nor runs the old 168-trajectory field dynamics. The source's original archived runtime `CPython 3.11.15 / NumPy 1.26.4 / SciPy 1.17.1` is not the local assistant environment `CPython 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0`. The Prcek default Python 3.12.3 lacks NumPy/SciPy; a short constrained probe of **seven explicitly named interpreter paths** found only the system interpreter, which is **not** an exhaustive host search. No packages were installed, no live Lina computations were touched, and **the complete P2 baseline was not replayed**. Prior archived numerical outcomes remain historical, including **no overall stable object**. No A–F top-level recovery success claimed.

**Next permitted step:** obtain the complete byte-faithful 100,626-byte Python source in a **non-production, isolated scientific runtime** with pinned NumPy/SciPy; run the original archived `unit_controls` and baseline with bounded resource measurements and an independent full-JSON comparison. This local scheduler PASS removes one consistency risk but does not waive execution/environment gates or authorize the longer source-off experiment.

## 23. Checkpoint 18 — preregistered original P2 absolute-time RNG stream cross-version test (2026-11-22)

**Report version:** 0.1.18, **protocol frozen before execution**. The exact archival Python in historical `lineum-physics-philosophy-validation.md` (Git blob `cefa63c8007667481122a2b6df7dd3fb6f5aaf0d`; 100,626-byte Appendix P Python SHA-256 `76d99fdbedd494a1e4ee610d2b5d054d3a202dcd1ecb781a8d8ab3134174711a`) defines `p2_random_draw_schedule` at Python lines **1611–1628** and `p2_unit_controls` at **2631–2661**. This check is explicitly **different** from the field simulator: test whether the *same* legacy `RandomState` indexed stream remains byte-identical under the current isolated NumPy environment without running the physics.

**Frozen source inputs and comparison:**
- `seed = P2_SEEDS[0] = 2026245000` (not a P1 seed), `STEPS=600`, `SIZE=32`, `Config().noise_strength=0.005`;
- use one fresh `numpy.random.RandomState(seed)`; at each absolute step obtain `uniform=rng.rand(32,32)` and then `gaussian=rng.normal(0.0,0.005,(32,32))`;
- update a **single** `hashlib.sha256()` with `uniform.tobytes()` followed immediately by `gaussian.tobytes()` for each of the 600 steps, exactly as the historical `p2_unit_controls` source;
- run twice from independently initialized RNGs and compare both hashes; **predeclared archival target** (from original `unit_controls.absolute_time_common_random_draws.first_hash/second_hash`) is `e86d4ff0c713c8d0508e77307c1d9fbaa38b6a32c7c8c6d4b4df7a8576b17a9a`.
- Run in the isolated assistant runtime (observed `Python 3.13.5 / NumPy 2.3.5`) rather than Prcek, with no package installation or Grid/HA access. Include an independent checker that uses a **different buffering strategy** for the same source-ordered byte stream; this may detect a mistaken hash framing but not prove the field equations.

**Predeclared pass criterion:** both hashes exactly equal each other **and** the predeclared historical target; mismatches are retained negatives, not tuned away. This is only a source/seed/RNG transfer control: **even PASS does not replay a single P2 field trajectory or establish physical stability**. Further full physics replay remains blocked on byte-faithful transfer of the full historical 100,626-byte source into a safe isolated scientific runtime with appropriate dependency/environment acceptance and a complete independent output comparison.

## 24. Checkpoint 19 — P2 absolute-time RNG cross-version hash MISMATCH (2026-11-22)

**Version:** 0.1.19. **Status: PREDECLARED NEGATIVE CONTROL, exact source-output replay not yet validated.** This result is the immediate outcome of the frozen Checkpoint 18 stream-hash experiment, recorded **before** a repair or alternate mechanism is selected.

**Isolated environment:** `CPython 3.13.5 / NumPy 2.3.5` (not the original reported `CPython 3.11.15 / NumPy 1.26.4`). No physical simulation, SciPy call, source change, host modification or Lina EI Grid access.

**Method actually executed:** initialize `np.random.RandomState(2026245000)`; for **600** absolute steps draw `uniform=rng.rand(32,32)` then `gaussian=rng.normal(0,0.005,(32,32))`; append each pair of raw `ndarray.tobytes()` to SHA-256 in this order. The independent checker buffered all 600 pairs and hashed their concatenated raw bytes instead. Both covered the same `600×2×32×32×8 = 9,830,400` bytes (float64 arrays).

```text
ORIGINAL_ARCHIVE_FIRST_HASH=e86d4ff0c713c8d0508e77307c1d9fbaa38b6a32c7c8c6d4b4df7a8576b17a9a
STREAMING_CURRENT_HASH=dafad62555fdc0d39788d4aa597a27b8c161ed3aee5e80c70679e7a4feb52607
BUFFERED_CURRENT_HASH=dafad62555fdc0d39788d4aa597a27b8c161ed3aee5e80c70679e7a4feb52607
STREAM_EQUALS_BUFFER=True
ARCHIVED_HASH_MATCH=False
FINAL_ASSERTION=FAILED, exit 1
```

**Interpretation limited to tested domain:** the two independent *framing strategies* agree, but the **current NumPy 2.3.5 stream hash does not match the originally published NumPy 1.26.4 stream hash**. This failure must **not** be silently tuned away or re-labelled PASS. Possible competing explanations still open: legacy NumPy normal-RNG runtime difference, a transcription difference in the test harness, a mismatched archived `unit_controls` value, or a code/output identity discrepancy. **None of these is established by the current result.** This is a reproducibility **environment/source audit negative**, not evidence that the underlying P2 field physics is wrong.

**Next frozen forensic discriminator:** (1) independently execute the *verbatim original function* `p2_random_draw_schedule` (Python lines 1611–1628) with the archived `SIZE`, `STEPS`, `Config` defaults, rather than a hand-constructed generator; (2) independently verify its byte hash against the prior current-runtime result `dafad625...`; (3) if the hashes still disagree with the archival target, inspect the actual stored historical unit-control generation and available NumPy 1.26.4 environments without installing anything into Prcek/HA; (4) preserve any negative and compare the first divergent random values only under source-pinned identical input streams before attempting full 168-run P2 baseline. **Full physics replay remains unexecuted and unqualified.**

## 25. Checkpoint 20 — mismatch persists with the original Python RNG function (2026-11-22)

**Version:** 0.1.20. This is the bounded forensic follow-up specified at Checkpoint 19; it preserves the negative rather than modifying a seed or source formula.

**Exact original algorithm check:** The locally isolated assistant runtime reproduced the original `p2_random_draw_schedule` function body *line-for-line* from the historical Appendix P Python lines **1611–1628** and the original `Config` defaults (Python lines **53–65**), with unchanged `SIZE=32`, `DT=0.1`, `TOTAL_TIME=60.0`, `STEPS=600`, `noise_strength=0.005`, `seed=2026245000`. Calling the original function generated 600 alternating 32×32 uniform/Gaussian arrays; hashing them in the **original `p2_unit_controls` byte order**, as declared at original Python lines **2653–2661**, produced exactly the same hash as the first separately written checker:

```text
PYTHON 3.13.5 NUMPY 2.3.5
EXACT_ORIGINAL_FUNC_HASH dafad62555fdc0d39788d4aa597a27b8c161ed3aee5e80c70679e7a4feb52607
HAND_WRITTEN_CHECKER_HASH dafad62555fdc0d39788d4aa597a27b8c161ed3aee5e80c70679e7a4feb52607
EXACT_AND_RECONSTRUCTED_EQUAL True
ARCHIVED_HASH_MATCH False
FIRST_UNIFORM 0.6668063946947587
FIRST_GAUSSIAN 0.00613839214944613
FRAMES 600
```

This argues **against a mistake in the first checker’s buffering or obvious schedule transcription**; it does **not** distinguish the original NumPy 1.26.4 vs current NumPy 2.3.5 normal-RNG implementation from a stale historical output/code pair. The result is `reproducibility_failed_in_current_runtime`, **not** `historical_P2_result_falsified`. There was no field simulation, no altered input, no seed sweep and no physical interpretation promoted.

**Runtime-availability check:** `uv python list --only-installed` in this isolated container exposed **only CPython 3.13.5**; no local Python 3.11/3.12 interpreter or cached NumPy 1.26.4 wheel was identified in the bounded lookup. No historical scientific environment was provisioned; this is not an exhaustive search of external mirrors or hosts. The current available `NumPy 2.3.5` and `SciPy 1.17.0` do not satisfy the archived run environment `NumPy 1.26.4` and `SciPy 1.17.1`.

**Decision:** do **not** run 168 expensive original trajectories under the mismatched environment or call the result a same-output replay. The next required discriminator is a truly isolated environment matching **Python 3.11.15 + NumPy 1.26.4** (and SciPy 1.17.1 before the full solver) or equivalent original-runtime independent checks, rerunning *only* the frozen 600-frame random-stream SHA before any physics execution. If that environment reproduces the archived `e86d4ff0...` hash, the NumPy runtime difference becomes a strong candidate and can be investigated bytewise; if it does not, audit archive/source identity and possible original generation differences, retaining both results. **Prcek's sole Lina EI Grid is excluded from heavy replay.** No A–F classification, no long-horizon extension, no code or whitepaper changes.

## 26. Checkpoint 21 — preregister controlled NumPy 1.26.4 compatibility discriminator (2026-11-22)

**Report version:** 0.1.21; **status:** pre-execution protocol. The current isolated NumPy 2.3.5 stream produces `dafad62555fdc0d39788d4aa597a27b8c161ed3aee5e80c70679e7a4feb52607`, whereas the original P2 archive reports `e86d4ff0c713c8d0508e77307c1d9fbaa38b6a32c7c8c6d4b4df7a8576b17a9a`. The original P2 RNG function agrees with the independent reconstruction in the current runtime; the discrepancy is **not yet explained**.

**Frozen next discriminator:** a *single* 600-update RandomState SHA-256 probe under **NumPy 1.26.4**, with no Lineum field solver, no SciPy, no P2 full replay, and no other seeds or adjusted parameters. The host's existing Python 3.12.3 is officially supported by NumPy 1.26.4 per upstream NumPy release notes (https://numpy.org/doc/stable/release/1.26.4-notes.html); official PyPI package is https://pypi.org/project/numpy/1.26.4/ (permissive NumPy license with wheel notices; **no package material will be copied into Git**). This is a compatibility test, not a declaration of byte-identical replay under the original CPython 3.11.15 runtime.

**Safety and plan:** first test **read-only** access to the official PyPI version metadata, availability of `venv`/`pip`, and free `/tmp` space on Prcek via the documented short `shell_command.chatgpt_host_exec` bridge. If all checks pass, an *ephemeral, isolated, disposable* Python venv wholly inside a freshly named `/tmp/lineum-p2-rng-*` directory may install `numpy==1.26.4` **into that venv only**, not system Python, live Lina modules, HA container, repositories or production paths. Bound the action with `timeout<42s`, low CPU scheduling priority, subprocess timeouts, no GPU and no persistent output, and clean only its own temporary directory. A probe cannot imply blanket host-test permission; no heavy Grid or P2 simulation runs on the sole live Prcek. If PyPI, venv or resources are inadequate, report a bounded access result **without performing an install**. The technical mailbox carries **only a short script and small SHA/version/error summary**, no private state, raw source or conversation. Reconcile the final same-ID HA response and nested host rc, as required by the current HA manual.

**Expected checks:** the frozen Python implementation `rng=np.random.RandomState(2026245000)`; repeat `600` times `uniform=rng.rand(32,32)`, `gaussian=rng.normal(0.0,0.005,(32,32))`, hash their raw float64 bytes sequentially with SHA-256. Compare the resulting hash **first** with the predeclared historical `e86d4ff0...` and **second** with current-runtime `dafad625...`, without retuning; record platform, precise version, wheel/package source, byte count, nested rc and both outcomes. Success can establish reproducibility of this RNG hash in a compatible NumPy version, **not** any field dynamics, physics or stable particle. A failed install is a technical failure, **not** a numerical negative. No code/whitepaper changes from this test.

## 27. Checkpoint 22 — PyPI availability PASS; host has no pip/ensurepip; isolated wheel method frozen (2026-11-22)

**Report version:** 0.1.22. The read-only Prcek bridge probe `lineum-p2-pypi-readonly-20261122-h9d3` completed with final HA response, nested rc **0**, empty stderr:

```text
PYTHON 3.12.3
TMP_FREE_MB 392648
HAS_MODULE venv 1
HAS_MODULE ensurepip 0 ModuleNotFoundError
HAS_MODULE pip 0 ModuleNotFoundError
PYPI_HEAD 200 83524
PROBE_END
```

**Interpretation:** official PyPI is reachable on this host and the ephemeral directory has sufficient space, but the default system interpreter lacks both `pip` and `ensurepip`. The proposed ordinary `venv + pip install numpy==1.26.4` route **must not be attempted as though it were available**. This is an environment/tooling limitation, not a defect of Lineum, Git, HA or a numerical negative. It does **not** justify installing pip into the system or live Lina environment.

**Revised, still preregistered narrow test (no package installation):** Use only an *official, SHA-256-verified PyPI wheel* for NumPy `1.26.4`, supported on CPython `3.12`, **within an ephemeral dedicated `TemporaryDirectory` under `/tmp`**. First perform a separate **read-only** PyPI JSON metadata lookup and freeze the exact `cp312` Linux wheel name, digest and size; accept only the canonical `pypi.org` JSON and `files.pythonhosted.org` wheel URL matching the local `x86_64` Linux tag. For the eventual single-seed test, download the wheel to the same temporary directory, verify SHA-256 **before** extraction, safely unpack its Python/wheel contents only there via standard-library `zipfile`, then launch a **short, low-priority isolated child interpreter** that imports `numpy` solely from that temporary directory, computes the same predeclared 600-frame RNG digest and exits. Bound all subprocess/network waits and host command to <42 seconds. The temporary contents must be deleted by its own scope cleanup (not by deleting any pre-existing host path); on timeouts or exceptions, preserve the error as a technical limitation. **No `pip`, `apt`, Docker image pull, persistent `venv`, HA/Lina installation, production import, secret, new service or 168-run P2 physics simulation** is permitted by this checkpoint.

**Third-party intake:** official NumPy `1.26.4` from https://pypi.org/project/numpy/1.26.4/ ; public source and BSD-style NumPy license with bundled wheel notices, no republication, vendoring, derivative-code import or Core dependency change. This execution would only use its binary to discriminate NumPy-runtime stream compatibility. Treat all downloaded binary code as untrusted until official checksum and filename/platform selection pass.

**Scientific outcome gate unchanged:** compare one exact raw-byte `RandomState(2026245000)` 600-frame hash against original archive `e86d4ff0...` and current NumPy2.3.5 `dafad625...`. Report **PASS**, **MISMATCH** or **TECHNICAL BLOCKER** separately; do not call the complete P2 physics replay verified. Next action: read-only wheel metadata and interpreter ABI probe, then freeze the wheel SHA in this report before any download/execution.

## 28. Checkpoint 23 — official wheel identity pre-frozen before temporary execution (2026-11-22)

**Report version:** 0.1.23. A further short, **read-only** PyPI metadata / host ABI probe completed on Prcek through the existing bridge under command `lineum-p2-numpy126-wheel-meta-20261122-m8s2` with matching final success, nested rc **0**, empty stderr. No external binary downloaded or executed yet.

```text
HOST_ABI=CPython 3.12.3, x86_64, glibc 2.39
OFFICIAL_MATCHING_NUMPY_1.26.4_WHEELS=1
FILENAME=numpy-1.26.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
WHEEL_BYTES=17950613
WHEEL_SHA256=675d61ffbfa78604709862923189bad94014bef562cc35cf61d3a07bba02a7ed
DOWNLOAD_HOST=files.pythonhosted.org
```

**Fixed execution and failure gate:** query the already read official PyPI release JSON solely to resolve the URL for this **exact unique filename**, requiring the same pre-frozen 17,950,613-byte size, SHA-256 and `files.pythonhosted.org` HTTPS host. Download into a uniquely created `TemporaryDirectory` under `/tmp` (never production paths); enforce SHA-256 before unpacking; inspect wheel path names and total expanded size; extract only there; then launch **one** isolated, low-priority `python3 -I` child with that temp directory inserted into `sys.path`. It must report `numpy.__version__ == '1.26.4'` and independently execute **only** the already declared 600-pair source-ordered RNG hash for P2 seed `2026245000`; compare against original `e86d4ff0...`, retaining mismatches. Explicitly cap the host command (<42 sec), child (<10 sec), no GPU, one BLAS thread; recover an error if import, checksum, download or resource guard fails. Cleanup applies **only to the newly created temporary directory**, even on exception. This is **no persistent pip/venv/system install, no HA or Lina write, no full P2 solver run**. On timeout do not assume that cleanup completed; verify before any replay or deletion. No project code or whitepaper modification is authorized from this runtime compatibility test.

**Interpretation:** An exact NumPy 1.26.4 match would show that the *legacy RNG test's* archived SHA is reproducible under CPython 3.12.3, without proving the old complete simulator or explaining which individual software/library change causes the NumPy 2.3.5 mismatch. Failure remains a result and blocks premature physics replay.

## 29. Checkpoint 24 — original NumPy 1.26.4 compatibility test MISMATCHES archive AND NumPy 2.3.5 (2026-11-22)

**Report version:** 0.1.24. This is the executed result of the frozen Checkpoint 23 isolated-wheel test, recorded **before** selecting another explanation or numeric run. **Not a physics-solver replay.**

**Live-host safety and exact outcome:** Prcek bridge command `lineum-p2-np126-isolated-rng-20261122-q6w9` was executed once. A matching final `HA_RESPONSES` result captured **nested host returncode 7**, which is the *intentional comparison-failed exit status from the child* and therefore **not PASS**. stderr empty. The response was:

```text
WHEEL_IDENTITY_OK 1
WHEEL_SHA_OK 1 BYTES 17950613
CHILD_RC 7
CHILD_STDOUT NUMPY 1.26.4;RNG_SHA256 fffdcf960b5593cbb484d175c6d7f8d825eedfd24fd1b133cac52b9242e7579c;ARCHIVED_MATCH 0;NUMPY2_MATCH 0
TEMP_CLEANED 1
```

**External source and package boundary:** official PyPI NumPy `1.26.4` CPython **3.12** / x86_64 / glibc≥2.17 wheel named `numpy-1.26.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl`; **17,950,613 bytes**; verified wheel SHA-256 `675d61ffbfa78604709862923189bad94014bef562cc35cf61d3a07bba02a7ed` (match to predeclared official PyPI metadata before unpacking). The binary was **not installed into system Python, any venv, Lina EI, HA, or the repository**: it was unpacked to a uniquely created, self-cleaning `TemporaryDirectory` under `/tmp`; child CPython 3.12.3 used `python3 -I` and explicit temporary `sys.path`, one BLAS thread, low host priority. It only generated and hashed the predeclared **600** pairs of 32×32 NumPy RandomState arrays from the same P2 seed, with no field simulation. The host reported `TEMP_CLEANED 1` and no production service or Grid change was issued.

**All three immutable audit hash comparisons now differ:**

| Runtime | SHA-256 over 600 uniform/Gaussian pairs | Comparison |
| --- | --- | --- |
| Historical Appendix P **reported** CPython **3.11.15**, NumPy **1.26.4** | `e86d4ff0c713c8d0508e77307c1d9fbaa38b6a32c7c8c6d4b4df7a8576b17a9a` | **archive reference, not current rerun** |
| Isolated assistant CPython **3.13.5**, NumPy **2.3.5** | `dafad62555fdc0d39788d4aa597a27b8c161ed3aee5e80c70679e7a4feb52607` | **not equal to archive** |
| Isolated official-wheel CPython **3.12.3**, NumPy **1.26.4** | `fffdcf960b5593cbb484d175c6d7f8d825eedfd24fd1b133cac52b9242e7579c` | **not equal to either** |

**Inference strictly limited:** the source-ordered current NumPy 2.3.5 stream is reproducible within its own tested runtime (two independent buffering variants, plus original function), but the SHA also fails to match the certified official NumPy 1.26.4 wheel under CPython3.12.3. Therefore **NumPy 1.26.4 version alone is not sufficient** to reproduce the historic archive in the current CPython 3.12 / Linux host test. The cause is not yet identified; differences may arise from Python/NumPy binary builds, distribution-specific floating-point behavior, a historical source-versus-output mismatch, or another provenance condition. A SHA mismatch alone does **not quantify** how much the underlying random numbers differ, and does not falsify historical P2 field physics. The archive's historical `unit_controls.all_pass=True` remains *historical metadata*, not confirmed by a present-day binary environment.

**Hard gate:** do **not** execute the 168-trajectory original P2 field simulator or extend its source-off horizon while the original RNG receipt is irreconcilable. The next bounded discriminator should inspect the first uniform and Gaussian floating-point samples (separately and with original code) under the two current runtimes to determine whether discrepancies begin at the very first values or arise from microscopic float rounding; then, only if necessary, obtain the actual archived CPython **3.11.15** environment or an independently SHA-verified wheel/runtime provenance. Any necessary Prcek check must remain isolated, short and non-persistent; no heavy solver or live Grid action. **No A–F replay classification**, no code/whitepaper promotion, ClickUp read-only/unsynchronized.

## 30. Checkpoint 25 — preregister first-divergence location and RNG-component audit (2026-11-22)

**Version:** 0.1.25; **protocol frozen before running this differential check.** Previous frozen full-stream hashes differ across the archived CPython3.11.15+NumPy1.26.4 receipt and two current interpreters. The required next step is to discriminate **where** the two current interpreters disagree without sweeping seeds, source settings, RNG method or NumPy version.

**Inputs retained verbatim:** original Appendix P source `p2_random_draw_schedule`, `P2_SEEDS[0]=2026245000`, `STEPS=600`, `SIZE=32`, `noise_strength=0.005`, `rng=RandomState(seed)`, uniform `rand(32,32)` immediately followed by Gaussian `normal(0,0.005,(32,32))` for every absolute frame. No source-state evolution or output tuning.

**Frozen independent comparison measures:** Under local NumPy2.3.5 and a new, separate **official-wheel, temp-only** NumPy1.26.4 CPython3.12.3 child, record (i) the first **three** `repr(float(...))` values from each **first-frame** uniform/Gaussian array; (ii) SHA-256 of first-frame uniform bytes and first-frame Gaussian bytes **separately**; (iii) whole-stream SHA-256 over **all 600 uniform arrays only** and **all 600 Gaussian arrays only**; (iv) the already expected interleaved-stream SHA-256, as a consistency control; (v) first-value pairs at fixed frame indices `0, 1, 199, 599` only. All values are purely numerical, no live HA or Lina state.

**Match logic:** uniform-only matching / Gaussian-only mismatch indicates the deviation is in Gaussian generation/representation rather than the uniformly generated bytes; first-frame mismatches show immediate divergence; matching first frame but later whole-stream mismatch requires a later-frame discriminator. The precise cause remains **undetermined** until independently justified (possible NumPy version/build/CPU math, archive provenance). The original archival `e86d4ff0...` remains a **third reference digest**, not a callable runtime. Do not call a mismatch proof of invalid physics or a stable particle.

**Host safety:** check the official **pre-frozen** NumPy 1.26.4 wheel SHA-256 `675d61ffbfa78604709862923189bad94014bef562cc35cf61d3a07bba02a7ed` and size **17,950,613 bytes** before use; isolated `TemporaryDirectory`, low priority, bounded <42 sec, one BLAS thread, no persistent install or full P2 run, cleanup readback. If the wheel or runtime fails, classify technical failure, not scientific. Source control remains Git; the HA manual governs host and bridge execution.
