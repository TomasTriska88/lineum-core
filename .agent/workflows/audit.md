---
description: How to execute a canonical whitepaper audit run for Lineum
---

# Canonical Whitepaper Audit Workflow

**Current gate (reviewed 2026-10-20): BLOCKED.** Do not launch a new canonical audit or report a canonical PASS until [Issue #7](https://github.com/TomasTriska88/lineum-core/issues/7) is fixed and its regression tests pass locally.

## Why the workflow is blocked

The current `tools/whitepaper_contract.py` can mark a run PASS when any matching profile passes. The `baseline` profile has empty selectors, so it matches every run and can hide a failed canonical profile. In the committed suite generated on 2026-07-15, `spec6_false_s41_20260608_041107` is included with `steps = 1), even though the canonical contract requires `steps = 2000`; the suite still reports `pass = 8` and `fail = 0`. A green overall count is therefore not currently sufficient evidence of a valid canonical audit.

The current workflow's direct `python lineum.py` launch is also stale: the audit-policy tests enforce the Lab orchestration-token guard for canonical runs. Do not bypass that guard or invent an orchestration token manually.

While Issue #7 is open:

- Do not start a new canonical simulation.
- Do not use `python tools/whitepaper_contract.py --runs-root output_wp/runs ...` to declare canonical success.
- Do not treat `summary.pass`, `summary.matched_canonical`, or a selected `baseline` profile as evidence that the canonical profile passed.
- Do not modify, overwrite, move, or clean up existing run folders. The validator has a quarantine path for locked runs that fail integrity checks, so broad verification can have side effects.

## 1. Canonical run settings

After Issue #7 is fixed and tested, launch canonical runs only through the supported Lab orchestration layer. Begin from a clean host shell and let the orchestrator inject its one-use token into the child process. Do not clear `LINEUM_*` variables after the token has been injected.

Pass exactly these canonical settings through the orchestration layer:

- `LINEUM_AUDIT_PROFILE = "whitepaper_core"`
- `LINEUM_BASE_OUTPUT_DIR = "output_wp"`
- `LINEUM_RUN_ID = "6"`
- `LINEUM_RUN_MODE = "false"`
- `LINEUM_SEED = "41"`
- `LINEUM_STEPS = "2000"`
- `LINEUM_TEST_EXHALE_MODE = "true"`
- `LINEUM_RESUME = "false"`

Only add `LINEUM_EXPECTED_KAPPA_MAP_HASH` when its expected value is independently pinned in the applicable audit specification. A canonical run must be fresh and written to a new timestamped directory under `output_wp/runs/`; existing runs are read-only.

The contract currently referenced by the whitepaper is `contracts/lineum-core-1.0.18-core.contract.json` (`contract_version = 1.1.5`). Do not change that path merely because the whitepaper header says `1.0.64.1-core`; contract versioning and whitepaper evidence mapping must be updated deliberately and verified together.

## 2. Validate one fresh run

Do this only after Issue #7 is resolved and the regression tests pass. Set `$RunDir` to the exact new timestamped run directory. First fail closed on the manifest identity:

```powershell
$manifestPath = Join-Path $RunDir "spec6_false_s41_manifest.json"
if (-not (Test-Path $manifestPath)) { throw "Canonical manifest is missing: $manifestPath" }
$m = Get-Content -Raw $manifestPath | ConvertFrom-Json
if ($m.run.run_id -ne 6 -or $m.run.seed -ne 41 -or $m.run.steps -ne 2000 -or $m.run.grid_size -ne 128 -or $m.run.time_step_s -ne 1e-21 -or $m.run.kappa_mode -ne "constant") {
    throw "Canonical manifest identity mismatch; reject this run."
}
```

Then evaluate only that run against the explicit contract:

```powershell
python tools/whitepaper_contract.py --run-dir $RunDir --contract contracts/lineum-core-1.0.18-core.contract.json --strict
if ($LASTEXITCODE -ne 0) { throw "Whitepaper contract validation failed." }
```

Inspect the generated `output_wp/runs/_whitepaper_contract/whitepaper_contract_suite.json`. Confirm that the candidate is evaluated against the intended canonical profile and that every canonical check passes. If the expected profile is absent, the profile is not the canonical one, or any identity/anchor check fails, stop and record the run as a failure or unresolved result; do not retune parameters to recover PASS.

## 3. Preserve evidence without sweeping historical runs

Never stage the entire `output_wp/` tree. After a candidate passes the repaired validator, stage only the exact new run directory and the generated contract-suite file, inspect the staged diff, and ensure no unrelated, cached, temporary, or credential files are included. Keep previous run directories immutable.

A failed or inconclusive run must not be labelled `Audit PASS`. Preserve decision-relevant failures and their provenance in the version-controlled research record. Do not publish a positive scientific claim merely because a software check returned zero.
