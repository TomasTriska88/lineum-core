# Lineum Public-TOLOG Three-Question Benchmark — B4

**Status:** active authoritative report; spatial localized-L1 primary retained; homogeneous accounting independently verified; spatial independent-checker receipt not yet recovered  
**Version:** 0.11.0  
**Evidence cutoff:** 2026-08-07  
**Repository / branch:** `TomasTriska88/lineum-core` / `develop`  
**Checkpoint parent:** `0cda026b02a1f1f48813fa433b7bd73003a00a40`  
**Scope:** exactly three public comparison questions; public TOLOG information only; no private counterpart material; no whitepaper change  
**Question 1:** `descriptive_target_validated_but_no_autonomous_emergence_shown`  
**Question 2:** `localized_primary_reproduced_no_full_state_recovery_homogeneous_accounting_verified_spatial_checker_receipt_pending`  
**Question 3:** `no_explicit_scalar_potential_minimum_yet_demonstrated`

## Authoritative record and continuity

This file is the single active scientific report for the continuous public-TOLOG B4 programme. Conventional exchange calibration, the homogeneous Core accounting audit, the localized spatial screen, failures, contradictions, and the exact next gate are kept here rather than in separate active reports.

Version `0.10.1` embedded historical material and machine-readable results as opaque compressed Unicode payloads. Those payloads are no longer part of the active report because current repository rules require ordinary human-readable Markdown and separate plain-text artifacts when artifacts are needed. The exact former report remains immutable in Git as blob `8f08fe0da08751781e13f90496a928f89eae9d56`; historical detail omitted from the active narrative remains recoverable there and in earlier commits. This migration changes the storage form, not any equation, threshold, retained result, or scientific interpretation.

The accidentally separate report `research/lineum-classical-bright-soliton-reference-preregistration.md` is absent from the current `develop` parent. Its decision-relevant scientific content is consolidated below from historical blob `68b0ae44795124e13b8bccdd743a93b6a4ac3786`. Git history remains the immutable source for its earlier executable envelopes and exact raw bytes.

## Plain result

The current evidence does not show that the present Lineum implementation naturally completes a reciprocal `psi`–`phi` return cycle.

The localized spatial primary kept all 28 declared cases finite over the tested horizon, but produced only two partial `psi` recoveries. Both occurred with seeded `phi` held at the explicit cap, and no case achieved preregistered full-state recovery. Removing the cap or all hard guards remained finite over that horizon but produced no recovery. LAP8 changed some measurements but did not uniquely stabilize the state.

The independently checked homogeneous reduction explains why a rising `psi` alone is not enough: explicit mode transfer moves accounted quantity from `psi` to `phi`, while a separate feedback term can increase `psi` without decreasing `phi`. Dissipation removes quantity without crediting the reservoir, and the cap can discard excess `phi`. In the verified homogeneous full lanes, `psi` recovered while `phi` never decreased and the declared `E + phi` ledger grew by millions. That is apparent component recovery, not demonstrated reciprocal return.

This is a bounded negative result for the tested implementation and observers. It does not falsify spatial Lineum, identify the correct repair, establish the physical meaning of `phi`, or show that nature follows this simulation.

## Controlling questions

1. Can Lineum produce real-galaxy rotation with at least `98%` preregistered held-out agreement from independently defensible source and initial conditions alone, without target leakage, galaxy-specific output fitting, a dark-matter component, or a renamed fitted surrogate?
2. Does Lineum possess a finite mathematical attractor that remains bounded and returns after perturbation without noise, clipping, caps, resets, or ad hoc damping, including at a declared discrete equivalent of `r -> 0`?
3. Can the exact `256 x 256` grid integrate a genuinely real scalar degree of freedom with an explicit fixed potential minimum that retains localized information after source removal and returns after positive and negative perturbations?

Current bounded answers:

- Question 1: the descriptive curve-shape target is characterized, including the earlier SPARC B4 screen, but blind autonomous emergence has not been demonstrated.
- Question 2: the localized primary did not show full-state recovery; the homogeneous accounting audit independently verifies that apparent `psi` recovery in the reduced current Core map is not reciprocal reservoir return.
- Question 3: scalar-valued auxiliary fields exist in the implementation, but an explicit fixed-potential, information-preserving scalar state has not been demonstrated.

## Evidence separation

### What the current implementation computes

For the audited homogeneous deterministic reduction with uniform fields, `kappa = 1`, `mu = 0`, `delta = 0`, disabled noise, and `dt = 1`, spatial gradients, diffusion, transport, linons, and fluctuations vanish. The surviving scalar map is:

```text
phi_local = clip(phi, 0, 10)
s = 0.1 * tanh(0.4 * phi_local)
q = s * psi / (1 + abs(s * psi) / 10)
psi <- psi + q                  [feedback; no phi debit]
psi <- 0.995 * psi              [dissipation; no reservoir credit]
E_pre = abs(psi)^2
delta_e = 0.001 * E_pre
phi <- phi + delta_e            [explicit one-way mode transfer]
abs(psi) <- sqrt(max(E_pre - delta_e, 0))
phi <- clip(phi, 0, phi_cap)     [external cap]
```

The explicit mode-transfer substep approximately conserves the declared `E + phi` ledger. The feedback substep increases `psi` without a paired `phi` debit. Dissipation removes `psi` quantity without crediting `phi`. The cap discards excess `phi`. The surviving multipliers are real and positive and provide no second relative-phase carrier, so this homogeneous scalar reduction cannot instantiate conventional coherent return.

The public configuration exposes a `dissipation_rate`, while the audited implementation snapshot used a literal `0.005` multiplier path. The existing mode-coupling contract test checked a positive finite `phi_gain`; it did not require reverse debit, closed whole-step accounting, recurrence, or full-state return.

### What was reproducibly observed

- The conventional reference ruler and its separately implemented analytic checker agreed with zero mismatches in their declared toy domain.
- The official localized-L1 primary executed all 28 preregistered cases and retained the observations below.
- The homogeneous official primary and a separately written scalar checker agreed with zero mismatches.
- No committed immutable receipt for the localized spatial checker was recovered in this checkpoint. Therefore the localized result remains at `reproduced`, not `robust_within_tested_domain`.

### Cautious interpretation

A component can fall and rise again without the complete state returning and without stored quantity flowing back from the declared reservoir. The current homogeneous evidence identifies unpaired amplification as the source of apparent `psi` recovery in that reduction. The localized result is consistent with the same concern but does not isolate every spatial contribution.

### Hypotheses still open

Spatial gradients, `phi` diffusion, `psi` diffusion, locality, nonlinear interaction, a different energy functional, or a different interpretation of `phi` could change the accounting classification. These possibilities remain hypotheses until separated by frozen interventions.

Three live conceptual alternatives remain:

1. the intended reciprocal mechanism is incomplete and lacks a paired return term;
2. `phi` is not an energy reservoir but a control, environment, or potential-like field, so “energy returns from `phi`” is the wrong interpretation;
3. `abs(psi)^2 + phi` is not the appropriate conserved ledger, and the relevant `phi` contribution may be nonlinear or include gradients.

### Connection to known physics

The conventional models below provide calibration vocabulary for coherent recurrence, dissipative relaxation, and one-way accumulation. They do not establish a laboratory, quantum, gravitational, dark-matter, cosmological, consciousness, or ontological connection for Lineum. No real-physics claim is promoted by internal agreement alone.

## Conventional exchange reference ruler

The reference programme was built before interpreting Lineum recovery so that “return” had an external mathematical meaning.

| Lane | Conventional behavior | Discriminator |
|---|---|---|
| `R0` | coherent resonant exchange | complete transfer followed by return |
| `R1` | detuned coherent exchange | recurrence with maximum transfer to `B` of `0.5`, not complete transfer |
| `R2` | reciprocal rate exchange | bidirectional terms but monotonic equilibration to `0.5 / 0.5`, no recurrence |
| `R3` | one-way accumulator | conserved total while `B` accumulates, no return |
| `R4` | uncoupled null | stationary independent components |

The primary and independent analytic checker passed with zero mismatches.

```text
executable freeze commit prefix = 42fef4
retained primary commit prefix = d77137
independent verification commit prefix = f1bd74
primary JSON SHA-256 = bcfec07204869be1b8d798d1d0f4d20999a38cf132e72cbf4d31de6d0a0c5e98
checker JSON SHA-256 = 27ba9b699ec2cfaba38fd051fd80eed374ac5a072a6e8897e838c0003e86798f
```

This ruler establishes that reciprocal terms do not automatically imply coherent return, and conservation does not automatically imply recurrence. A stable localized soliton would likewise not, by itself, prove reservoir return. The reference is a measuring ruler, not a proposed Lineum mechanism.

## Homogeneous Core accounting audit

### Immutable provenance

```text
executable checkpoint commit = 2fd4554cffcfb65ac30258c76bf41a6022ea5589
retained-primary commit = 1b7510fed36d6dc82beba65e0ba9e3cdcdf983b1
historical report blob = 68b0ae44795124e13b8bccdd743a93b6a4ac3786
primary JSON bytes / SHA-256 = 23054 / fb05d61caeb2cfa14f9a8581b73304aefd4b67ee19c6ef8a6f7a12533c55c0ba
source-audited Core commit = f1bd74ec2cb62d3b8d56bda05f524c6f63ab9775
lineum_core/math.py blob = bb877021810691223a0eb960a45493a2e351112a
physics-contract test blob = 7acbb8a1c5ff85a5b24970d216aa2a08111b0941
primary source SHA-256 = 242b6d05cef2e1026e23cabbcc0bfc0d5499f155f1c72f5229475da9f5b806e9
checker source SHA-256 = 34a0fd5583609b59d430805b3d0d048cdcdff4e311cadb45cf98f408c4233a5b
```

### Frozen lanes and criteria

- `C0`: full reduced map with the default cap.
- `C0b`: full reduced map without the `phi` cap.
- `C1`: no `phi` feedback.
- `C2`: explicit mode transfer only.
- `C3`: feedback plus dissipation without mode transfer, seeded with `phi = 1`.
- `C4`: dissipation only.
- `C5`: null lane.

Apparent recovery required `E >= 0.999 * E_initial` after a prior departure. True reciprocal return additionally required at least one `phi` decrease and return of the declared ledger within `1e-6`.

### Official verified results

| Lane | Verified classification | Apparent recovery | True return | Final `E` | Final `phi` | Final ledger |
|---|---|---:|---:|---:|---:|---:|
| `C0_full_default_cap` | apparent recovery without reciprocal ledger | step `701` | no | `2900150.257034308` | `1000000.0` | `3900150.257034308` |
| `C0b_full_cap_free` | apparent recovery without reciprocal ledger | step `701` | no | `2900150.257034308` | `2359502.643825432` | `5259652.90085974` |
| `C1_no_phi_feedback` | dissipative one-way accumulation | no | no | `2.650267646912908e-10` | `0.0902893517688856` | `0.09028935203391236` |
| `C2_mode_transfer_only` | one-way conserved transfer | no | no | `0.13519992446823598` | `0.8648000730057612` | `0.9999999974739973` |
| `C3_phi_feedback_only_seeded` | unpaired feedback source | no | no | `1482693.5590557144` | `1.0` | `1482694.5590557144` |
| `C4_dissipation_only` | dissipative sink | no | no | `4.427529784808337e-05` | `0` | `4.427529784808337e-05` |
| `C5_no_terms_null` | stationary null | no | no | `1.0` | `0` | `1.0` |

Additional discriminators:

- Full-lane minimum `E = 0.23353976762645046` occurred at step `350`.
- `phi_decrease_count = 0`.
- First default-cap contact occurred at step `1521`, after apparent recovery at step `701`.
- Cap and cap-free lanes had identical final `psi` energy, proving the cap did not cause their `psi` recovery.
- Mode-transfer-only ledger drift was `2.5260027403106733e-09`; phase drift was `0`.
- The feedback-only seeded lane held `phi = 1` while final `E` grew to `1482693.5590557144`.

### Independent checker

The checker was invoked once after the primary was committed and did not import or rerun the primary solver.

```text
started UTC = 2026-08-06T15:22:30.859836+00:00
finished UTC = 2026-08-06T15:22:31.517766+00:00
elapsed seconds = 0.6579304010010674
return code = 0
primary input SHA-256 = fb05d61caeb2cfa14f9a8581b73304aefd4b67ee19c6ef8a6f7a12533c55c0ba
checker JSON bytes / SHA-256 = 352 / 81cb30ba92ac3848095582afadde4fb9c24ac6138928e21c1eb3553f6d023adc
stdout = passed=True mismatches=0
stderr bytes = 0
primary rerun = false
```

The checker reported `passed = true`, `mismatches = []`, `imports_primary = false`, `separate_scalar_replay = true`, `closed_form_dissipation_control = true`, and `active_core_runtime_adapter = false`.

The homogeneous conclusion reaches `robust_within_tested_domain` for the exact deterministic scalar snapshot and declared ledger. It does not reach `mechanistically_supported`, `empirically_connected`, or a verdict on wider spatial Lineum.

## Localized spatial L1 screen

### Frozen question

Can neighbour transport turn the homogeneous partial `psi` equilibrium into a localized perturbation-recovering full state without hard `phi` containment, and does LAP8 materially outperform LAP4?

### Frozen protocol

```text
grid = 32 x 32
dt = 1.0
primary updates = 5000
recovery updates = 1000
stencils = LAP4, LAP8
initial phi = 0, 1
kappa = 1
mu = 0
delta = 0
noise = disabled
initial psi = normalized centered Gaussian, peak 1, sigma 3
lanes = baseline, no hard guards, no linear dissipation, no tanh,
        no denominator, no mode coupling, no phi cap
total = 28 cases
```

Localized `psi` recovery required no reset or non-finite event, energy error at most `5%`, radial-profile L2 error at most `10%`, half-energy-radius change at most one cell, and final center displacement at most half a cell. Full-state recovery additionally required no `phi` cap, `phi` radial-profile L2 error at most `10%`, and the preregistered one-sided late-`phi` slope gate. Absolute slope and non-triviality were secondary only.

### Provenance

```text
canonical runner SHA-256 = 96153e37b4e10890d3a0ab52e9463153cfc614eb9a2f1fcc58f23baeafc988bd
canonical checker SHA-256 = 3dfe7f6aa9f4da81c523f1c207c08bc0def175f827658d73aaa83e21df035031
canonical test SHA-256 = 95a5892f140543361eaffbee311016869e780f9bd21c559757b02b427f3b19ec
source commit = c513a65f16a65f6f600864f55a4edcd5fdfc69a7
workflow run / job = 31048211101 / 92448891365
artifact id = 8947333992
artifact ZIP SHA-256 = ca9a9ca05ffe0077ec15dce87ac8309a78b7f2ec114ef84d316f4202d535350c
primary JSON bytes / SHA-256 = 228809 / 499dabf444bf442eb9c36927d67a51505166ce422f1e428794aa20def560f11d
source report bytes / SHA-256 = 66581 / 1c0a51921868fc76a7696e2281621c40406d800ce3367f05c032c1283ae5bcd1
Python / NumPy = 3.13.14 / 2.3.5
platform = Linux-6.17.0-1020-azure-x86_64-with-glibc2.39
frozen harness tests = 9 passed
executed cases = 28 of 28
```

The workflow artifact is provenance only. The former in-report encoded copy was removed from the active report; exact bytes remain recoverable from the recorded artifact and immutable prior Git blob.

### Reproduced observations

- All 28 cases retained finite states over the declared horizon.
- Baseline produced two localized `psi` recoveries out of four and zero full-state recoveries.
- Both partial recoveries began at `phi0 = 1` and held `phi` at the explicit `1,000,000` cap.
- Both `phi0 = 0` baseline cases decayed and failed recovery.
- Removing explicit `tanh` produced two partial `psi` recoveries and zero full recoveries. Explicit `tanh` was not individually necessary for those outcomes, but no replacement law was identified.
- Removing the `phi` cap or all hard guards remained finite during this horizon but produced zero recoveries while `phi` reached `12852053.348233`.
- Removing linear dissipation produced zero recoveries and a maximum pre-perturbation `abs(psi)` of `17981.515115`.
- Removing the interaction denominator caused two reset events and zero recoveries.
- LAP4 and LAP8 differed materially in some metrics, but LAP8 did not uniquely provide full-state stabilization.

```json
{
  "all_pair_boundedness_and_recovery_statuses_equal": false,
  "any_material_stencil_metric_advantage": true,
  "baseline_primary_full_state_recoveries": 0,
  "baseline_primary_psi_recoveries": 2,
  "baseline_secondary_nontrivial_psi_recoveries": 0,
  "baseline_secondary_nontrivial_states": 0,
  "development_programme_terminal_failure": false,
  "lap8_specific_stabilization": false,
  "phase": "localized_l1_screen_completed",
  "spatial_transport_resolves_phi": false,
  "stencil_not_decisive_in_l1": false
}
```

### Verification boundary and unresolved receipt

The retained localized primary reaches `reproduced`. A later session summary described the spatial result as independently agreed, but this checkpoint did not recover a committed checker output, immutable checker hash, or complete command receipt proving that execution. That statement is therefore preserved as an unresolved provenance claim, not promoted as evidence.

The spatial result remains below `robust_within_tested_domain` until the frozen checker is executed against the committed primary JSON and its plain-text output is committed. No mechanism selection, tuning, or replacement-law promotion may rely on an unretained checker claim.

## SPARC B4 descriptive context for Question 1

The earlier public SPARC B4 shape study used 175 galaxies. Of these, 124 had at least 10 observations and 102 were classified as informative for the declared comparison. Within those 102:

- `tanh` was the best tested shape in `68`;
- `tanh` lay within `Delta AIC < 2` in `82`;
- `14` strongly rejected `tanh`;
- `32` distinguished the first and second tested shape families;
- the optimization used approximately `28,000` starts and retained a SPARC source checksum.

This supports only a descriptive statement about the tested curve-shape family. It does not show that Lineum generates those curves from independently defensible initial conditions, does not establish a universal `tanh` law, and does not validate TOLOG, dark-matter removal, or a Lineum–TOLOG mathematical bridge.

## Cross-lane synthesis

| Question | Supporting evidence | Contradiction or limitation | Current status |
|---|---|---|---|
| Galactic shape | broad SPARC descriptive fit comparison | no blind autonomous Lineum generator or held-out mechanism bridge | descriptive target only |
| Bounded return | 28 localized cases finite; two partial `psi` recoveries | zero full-state recoveries; partial recoveries cap-dependent | unsupported under tested conditions |
| Reciprocal reservoir cycle | homogeneous mode-transfer lane nearly conserves ledger | full-map recovery occurs with zero `phi` decreases and huge ledger growth | contradicted for audited homogeneous interpretation |
| LAP8 stabilization | material stencil differences in some metrics | no unique full-state stabilization | not supported |
| `tanh` necessity | removing `tanh` preserved two partial recoveries | no natural replacement law identified | explicit `tanh` not individually necessary in tested lane |
| Fixed scalar memory | scalar auxiliary fields exist | no explicit fixed-potential memory and return demonstration | not demonstrated |
| Real physics | conventional reference supplies terminology | no empirical observable comparison | not connected |

The localized result and homogeneous audit agree on one narrow warning: `psi` recovery is not an identifying observable for reciprocal return. They do not prove the same complete spatial causal mechanism, because the homogeneous reduction removes the spatial terms that may redistribute or alter the ledger.

## Preserved technical and methodological failures

These events produced no admissible new scientific evidence but affect reproducibility and are retained:

1. An initial full-repository checkout stalled before archive extraction, harness tests, or scientific execution.
2. Checker-interface preflight `31051766659` / job `92460317601` selected a heading token inside example code; it stopped before checker invocation or write.
3. Correction run `31052012351` / job `92461095095` assumed the wrong Markdown block order and stopped before a write.
4. Workflow revision `31052264959` failed YAML validation before any job existed.
5. Run `31052349446` / job `92462178617` found regex block matching ambiguous and stopped.
6. Run `31052454245` / job `92462509372` exposed that heading selection still matched text inside an example rather than the standalone heading.
7. During the 2026-08-06 to 2026-08-07 readable-report migration, a one-shot attempt to recompute the complete 28-case spatial screen exceeded the available command limit. It is not a retained rerun and changes no scientific status.
8. The same migration session reported 15 passing local tests and homogeneous replay agreement of approximately `9.779e-9`, but no permanent command transcript or plain-text result artifact was committed with that attempt. Treat this only as an operational note, not as new evidence.
9. A temporary branch named `codex-rule-fix` was accidentally created during Git Data API discovery. It contained no intended scientific change at creation. Its existence or later cleanup is repository housekeeping, not evidence.

The former capsule transport repeatedly created extraction ambiguity and connector failures. Current rules now prohibit using compressed or encoded payloads as the active scientific record.

## Environment limitations

Earlier retained calculations used Python `3.13.5` and NumPy `2.3.5`. The official localized-L1 primary used Python `3.13.14` and NumPy `2.3.5`, while the repository declared NumPy below `2.0`. The exact historical environment is retained, but the mismatch remains a limitation until a repository-supported rerun is completed.

The homogeneous checker did not use an active-Core runtime adapter; it independently replayed the frozen scalar map. That is valuable independence from the primary solver but does not prove that a later Core revision still computes the identical map.

## Prohibited conclusions

This report does not establish:

- a universal galactic `tanh` law;
- autonomous `98%` galactic emergence;
- absence of dark matter or a modified-gravity replacement;
- a validated mathematical bridge to TOLOG;
- a physical `3 x 3` elementary cell or TOLOG Dark Heart derivation;
- an emergent replacement for `tanh`;
- a natural attractor independent of inserted bounds;
- a complete `psi`–`phi` energy cycle;
- a stable scalar-potential memory state;
- a causal disk-concentration mechanism;
- a laboratory, quantum, gravitational, cosmological, consciousness, or ontological interpretation;
- a terminal limitation of the wider Lineum programme.

A green test proves only its asserted software condition. A reproduced numerical pattern does not by itself establish the metric, mechanism, uniqueness, or behavior of nature.

## Exact next scientific gate

Do not insert a reciprocal repair, add a field, tune parameters, run a soliton candidate, change production Core, or edit a whitepaper yet.

The next checkpoint must stay in this report and proceed in two ordered stages:

1. **Recover or execute the frozen localized checker.** Inspect its interface against the committed primary JSON, run it exactly once, retain ordinary plain-text JSON, and commit the checker output before using the localized result to select a mechanism.
2. **Preregister the smallest spatial accounting discriminator.** On a minimal periodic toy domain, activate one term at a time against the homogeneous baseline:
   - `phi` gradient forcing;
   - `phi` diffusion;
   - `psi` diffusion or the existing spatial transport term;
   - local nonlinear interaction.

For each lane, freeze boundaries, initial state, term coefficients, runtime, source and sink accounting, local and global ledger observers, `phi` debit counts, recurrence criteria, transport-flux measurements, and the meaning of every possible outcome.

The discriminator must separate:

- genuine local debit from `phi` paired with `psi` gain;
- spatial redistribution without reciprocal conversion;
- continued unpaired feedback amplification;
- dissipation or cap loss;
- failure of the declared `E + phi` ledger, implying that a different energy functional must be derived before interpreting return.

Before execution, reopen the repository hypothesis registry for spatial-return, reservoir, saturation, phase-carrying, and alternative-ledger variants. Record provenance and a root-programme impact matrix. No variant may be silently discarded merely because the homogeneous result is negative.

## New-thread handoff

A new researcher can resume without chat history by following this order:

1. Read all current repository rules from the then-current `develop` branch.
2. Re-fetch this report and verify its current blob SHA.
3. Verify that no second active report has been created for this programme.
4. Confirm the current Core commit before treating the audited homogeneous map as current implementation behavior.
5. Recover the localized primary using its recorded workflow/artifact/hash, not the former encoded report payload.
6. Recover or execute the frozen localized checker and commit its readable output.
7. Update this same report before and after the next consequential experiment.
8. Keep implementation facts, retained observations, interpretation, hypotheses, and real-physics claims separate.
9. Preserve negative results and unresolved contradictions.
10. Do not modify a whitepaper or production Core until the exact bounded claim passes its promotion gate.

## Version history

Versions `0.1.0` through `0.9.7` remain recoverable from Git history.

- `0.9.8`: converted the active report into a short control layer plus a compressed embedded history archive; no scientific equation, parameter, gate, or retained result changed.
- `0.9.9`: changed the embedded archive transport after connector truncation; no scientific result changed.
- `0.10.0`: embedded the exact official 28-case localized primary as a second encoded payload and recorded its bounded interpretation.
- `0.10.1`: corrected only payload heading and fence locators after fail-closed preflight revisions; no scientific result changed.
- `0.11.0`: restored an ordinary human-readable active report; removed opaque embedded payloads from the active record while preserving their exact prior Git blob; consolidated the conventional reference and independently checked homogeneous accounting audit into B4; preserved the spatial primary, negative results, technical failures, provenance contradiction, prohibited conclusions, and exact continuation gate. No production code, whitepaper, equation, threshold, or retained numerical result changed.
