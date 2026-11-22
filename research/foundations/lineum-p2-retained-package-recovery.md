# Exact P2 Source-Schedule Recovery — Retained Package Inventory

**Status:** active; bounded source-recovery checkpoint (not scientific validation)
**Version:** 0.1.0
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

through Python standard-library `urllib.request` on Prcek in 131,072-byte blocks, without transmitting the 67 MB contents through the Google Sheets mailbox and without altering the running Grid. SHA-1 was calculated as a **Git blob**, i.e. `SHA1(b"blob " + str(size).encode() + b"\\0" + full_bytes)`, not as the bare file SHA-1. Thus byte count and exact immutable repository blob identity both match.

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
digest = hashlib.sha1(("blob " + str(size) + "\\0").encode())
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
