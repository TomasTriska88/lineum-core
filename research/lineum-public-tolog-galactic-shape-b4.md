# Lineum Public-TOLOG Three-Question Benchmark — B4

**Status:** active; one authoritative report; complete next-thread handoff recorded  
**Version:** 0.11.2  
**Evidence cutoff:** 2026-08-07  
**Repository / branch:** `TomasTriska88/lineum-core` / `develop`  
**Base before this revision:** `48ace9c4c4d901c1120a8cb37c5012752a2e2926`  
**Scope:** exactly three public comparison questions; public TOLOG information only; no private TOLOG material; no private Lina EI implementation; no Core equation or whitepaper change

## 0. Authority, consolidation, and evidence classes

This file is the only active narrative report for the continuous public-TOLOG B4 programme. The former overlapping file `research/lineum-classical-bright-soliton-reference-preregistration.md` is intentionally absent from the active branch. Its decision-relevant conventional-reference and homogeneous-accounting content is consolidated here; its historical versions remain recoverable through Git.

Claims below are separated into:

1. implementation facts — what inspected code computes;
2. reproduced observations — what frozen executions produced;
3. cautious interpretations — the narrowest explanations supported by those facts and interventions;
4. hypotheses or analogies — possibilities not yet selected by evidence;
5. real-physics connections — none established by this report.

Negative results, failed replays, missing mechanisms, and incomplete runs are retained explicitly.

## 1. Plain conclusion

The current evidence does **not** demonstrate a cap-free, conserved, reciprocal return cycle between `psi` and `phi`.

The localized spatial screen found two `psi`-only recoveries, but both started with `phi=1` and contacted the explicit `phi=1,000,000` cap. No case recovered the full `psi`-`phi` state. Removing the cap eliminated the apparent recoveries.

The homogeneous reduction then isolated why a later rise in `psi` is not enough to call this return. The explicit mode-transfer block sends accounted quantity from `psi` to `phi`. A separate `phi`-conditioned feedback term grows `psi` without debiting `phi`; dissipation removes quantity; and the cap discards excess `phi`. The capped and cap-free homogeneous full lanes follow the same `psi` path, so the cap is not the cause of that later growth.

The strongest defensible statement is:

> The frozen implementation contains one-way accounted `psi -> phi` transfer and a separate `phi`-conditioned `psi` gain, but the tested homogeneous and localized routes do not demonstrate a cap-free, closed-ledger, reciprocal full-state return.

This does not falsify spatial Lineum, prove that `phi` is energy, identify the correct ledger, select a repair, validate TOLOG-Alpha, or establish a connection to real physics.

## 2. Controlling public questions

1. **Galaxy rotation:** Can Lineum generate held-out galaxy rotation with at least `98%` preregistered agreement from independently defensible source and initial conditions alone, without target leakage, galaxy-specific output fitting, a dark-matter component, or a renamed fitted surrogate?
2. **Bounded return:** Does Lineum possess a finite mathematical attractor that remains bounded and returns after perturbation without relying on noise, clipping, caps, resets, or ad hoc damping, including at a declared discrete analogue of `r -> 0`?
3. **Scalar fixed minimum:** Can the exact `256 x 256` system integrate a genuinely real scalar degree of freedom with an explicit fixed potential minimum that retains localized information after source removal and returns after positive and negative perturbations?

Current bounded answers:

- Question 1: descriptive curve-shape calibration exists; autonomous blind emergence is not demonstrated.
- Question 2: the tested routes do not show cap-free reciprocal full-state recovery.
- Question 3: scalar-valued auxiliary fields exist, but the required fixed-potential information-preserving scalar state is not demonstrated.

## 3. Question 1 — retained SPARC B4 shape baseline

The galaxy study is a descriptive shape calibration, not validation of Lineum or TOLOG.

```text
SPARC galaxies = 175
galaxies with at least 10 observations = 124
informative galaxies = 102
tanh best by AIC = 68 / 102
tanh within delta-AIC < 2 = 82 / 102
strongly rejecting tanh = 14 / 102
distinguishing first- from second-order shape = 32 / 102
optimization starts = 28,000
```

Established: bounded saturating shapes are useful for many curves; `tanh` is not universally preferred; some galaxies strongly reject it.

Not established: that Lineum generates the curves from source conditions; that fitted `tanh` is a physical law; that dark matter is unnecessary; that public TOLOG claims are reproduced; or that any model meets a blind `98%` held-out criterion.

Question 1 remains blocked on a mathematically explicit state-to-observable bridge and held-out evaluation.

## 4. Conventional reciprocal-exchange ruler

A non-spatial mathematical ruler was frozen before interpreting Lineum recovery:

| Lane | Meaning | Expected behaviour |
|---|---|---|
| `R0` | coherent resonant two-mode exchange | complete transfer and return |
| `R1` | coherent detuned exchange | recurrence; incomplete maximum transfer, second-mode maximum `0.5` |
| `R2` | reciprocal rate exchange | monotonic relaxation toward `0.5 / 0.5`; no return |
| `R3` | one-way accumulator | conserved total with monotonic accumulation; no return |
| `R4` | uncoupled null | no transfer |

The primary implementation and a separately written analytic checker passed with zero declared mismatches.

```text
primary JSON SHA-256 = bcfec07204869be1b8d798d1d0f4d20999a38cf132e72cbf4d31de6d0a0c5e98
checker JSON SHA-256 = 27ba9b699ec2cfaba38fd051fd80eed374ac5a072a6e8897e838c0003e86798f
```

Operational vocabulary fixed by this ruler:

- recurrence is not equilibration;
- bidirectional terms are not sufficient for coherent return;
- conservation is not sufficient for return;
- a stable localized object is not itself evidence of reservoir return.

This ruler is mathematical calibration only. It does not imply that Lineum fields are quantum amplitudes, spins, atoms, Rabi oscillators, solitons, or any particular physical system.

## 5. Localized-L1 spatial screen

### 5.1 Frozen protocol

```text
grid = 32 x 32; periodic boundary; dt = 1.0
primary updates = 5,000; recovery updates = 1,000
stencils = LAP4, LAP8
initial phi = 0, 1
kappa = 1; mu = 0; delta = 0; noise disabled
initial psi = centred Gaussian, peak 1, sigma 3 cells
lanes = baseline; no hard guards; no linear dissipation;
        no explicit tanh; no interaction denominator;
        no mode coupling; no phi cap
total cases = 28
```

Localized `psi` recovery required finite/reset-free execution, total-energy relative error at most `5%`, radial-profile L2 error at most `10%`, half-energy-radius change at most one cell, and final centre displacement at most half a cell. Full-state recovery additionally required no `phi` cap contact, `phi` radial-profile L2 error at most `10%`, and the preregistered late-`phi` slope gate.

### 5.2 Retained primary result

```text
source commit = c513a65f16a65f6f600864f55a4edcd5fdfc69a7
workflow run / job / artifact = 31048211101 / 92448891365 / 8947333992
primary JSON bytes = 228,809
primary JSON SHA-256 = 499dabf444bf442eb9c36927d67a51505166ce422f1e428794aa20def560f11d
executed cases = 28 / 28
```

Observed:

- all 28 cases retained finite states over the declared horizon;
- baseline produced `2 / 4` localized `psi` recoveries and `0 / 4` full-state recoveries;
- both partial recoveries started with `phi0=1` and held `phi` at the `1,000,000` cap;
- both baseline `phi0=0` cases decayed and failed recovery;
- removing explicit `tanh` again produced two partial `psi` recoveries and zero full recoveries;
- removing the `phi` cap or all hard guards produced zero recoveries while `phi` reached `12,852,053.348233`;
- removing linear dissipation produced zero recoveries and maximum pre-perturbation `abs(psi)=17,981.515115`;
- removing the interaction denominator caused two reset events and zero recoveries;
- LAP4 and LAP8 differed materially in some metrics, but LAP8 did not uniquely produce full-state stabilization.

Primary classification:

```json
{
  "baseline_primary_psi_recoveries": 2,
  "baseline_primary_full_state_recoveries": 0,
  "spatial_transport_resolves_phi": false,
  "lap8_specific_stabilization": false,
  "development_programme_terminal_failure": false
}
```

### 5.3 Independent checker

A separately implemented checker recomputed all 28 cases without importing the primary runner.

```text
checker source SHA-256 = 3dfe7f6aa9f4da81c523f1c207c08bc0def175f827658d73aaa83e21df035031
checker JSON bytes / SHA-256 = 673 / 6fec721c7877d0dacf781668553fa7a7910f470c12567e2ef71e2837b511d49d
numeric mismatches = 0
categorical mismatches = 0
maximum absolute difference = 4.547473508864641e-13
maximum relative difference = 9.11739763514324e-16
imports primary runner = false
recomputes all 28 cases = true
```

The localized observation is therefore `robust_within_tested_domain`. The mechanism remains unresolved.

## 6. Homogeneous Core accounting audit

### 6.1 Audited snapshot and reduction

```text
Core commit = f1bd74ec2cb62d3b8d56bda05f524c6f63ab9775
lineum_core/math.py blob = bb877021810691223a0eb960a45493a2e351112a
tests/test_physics_contract.py blob = 7acbb8a1c5ff85a5b24970d216aa2a08111b0941
```

Set spatially uniform `psi` and `phi`, `kappa=1`, `mu=0`, `delta=0`, noise disabled, and `dt=1`. Spatial terms vanish. The surviving scalar update is:

```text
phi_local = clip(phi, 0, 10)
s = 0.1 * tanh(0.4 * phi_local)
q = s * psi / (1 + abs(s * psi) / 10)
psi <- psi + q                    [feedback; no phi debit]
psi <- 0.995 * psi                [dissipation; no reservoir credit]
E_pre = abs(psi)^2
delta_e = 0.001 * E_pre
phi <- phi + delta_e              [explicit one-way mode transfer]
abs(psi) <- sqrt(max(E_pre - delta_e, 0))
phi <- clip(phi, 0, phi_cap)      [external cap]
```

Implementation facts:

- the mode-transfer block approximately conserves `abs(psi)^2 + phi`;
- feedback can increase `psi` without decreasing `phi`;
- dissipation removes quantity without crediting `phi`;
- the cap deletes excess retained `phi`;
- the homogeneous scalar reduction has no second relative-phase carrier for conventional coherent `R0` return;
- `CoreConfig` exposes `dissipation_rate`, while the inspected update uses literal `0.005`;
- the existing conservation test checks positive finite `phi_gain`, not whole-step closure, reverse debit, recurrence, or full-state return.

### 6.2 Verified lanes

| Lane | Classification | Apparent recovery | True reciprocal return | Final `Epsi` | Final `phi` | Final declared ledger |
|---|---|---:|---:|---:|---:|---:|
| `C0_full_default_cap` | apparent recovery without reciprocal ledger | step `701` | no | `2,900,150.257034308` | `1,000,000` | `3,900,150.257034308` |
| `C0b_full_cap_free` | apparent recovery without reciprocal ledger | step `701` | no | `2,900,150.257034308` | `2,359,502.643825432` | `5,259,652.90085974` |
| `C1_no_phi_feedback` | dissipative one-way accumulation | no | no | `2.650267646912908e-10` | `0.0902893517688856` | `0.09028935203391236` |
| `C2_mode_transfer_only` | one-way conserved transfer | no | no | `0.13519992446823598` | `0.8648000730057612` | `0.9999999974739973` |
| `C3_phi_feedback_only_seeded` | unpaired feedback source | no | no | `1,482,693.5590557144` | `1.0` | `1,482,694.5590557144` |
| `C4_dissipation_only` | dissipative sink | no | no | `4.427529784808337e-05` | `0` | `4.427529784808337e-05` |
| `C5_no_terms_null` | stationary null | no | no | `1.0` | `0` | `1.0` |

Additional discriminators:

```text
full-lane minimum energy = 0.23353976762645046 at step 350
phi_decrease_count = 0
first default-cap contact = step 1521
mode-transfer-only ledger drift = 2.5260027403106733e-09
homogeneous checker JSON SHA-256 = 81cb30ba92ac3848095582afadde4fb9c24ac6138928e21c1eb3553f6d023adc
checker passed = true; mismatches = []
```

A readable replay initially omitted a `1e-12` normalization epsilon and did not match exactly. That failed replay is retained as a warning against silently simplifying implementation algebra. Restoring the epsilon reduced the maximum final discrepancy to `9.779e-09`. This is a transcription check, not a new official scientific rerun.

## 7. Mechanism ledger and interpretations still open

Current evidence rejects, inside the tested routes:

- natural cap-free reciprocal return already demonstrated;
- the `phi` cap as the cause of homogeneous later `psi` growth;
- explicit `tanh` as necessary for the cap-dependent partial localized outcomes;
- LAP8 as uniquely stabilizing;
- the explicit mode-transfer block as reciprocal return;
- dissipation as cycle closure.

Still open:

1. `phi` is intended as an energy reservoir and a paired reverse debit is missing;
2. `phi` is a control, environment, potential, or gate rather than stored energy;
3. `abs(psi)^2 + phi` is the wrong ledger and the relevant quantity includes `phi^2`, gradients, interaction energy, or another state functional;
4. the tested feedback is an unpaired numerical source with no defensible physical ledger;
5. spatial transport supplies a measurable debit or incoming flux that is absent by construction in the homogeneous reduction.

No alternative is selected before the next spatial accounting experiment.

## 8. Exact next scientific gate

Do not first add a new fundamental field, write a return term, tune thresholds, alter Core equations, or edit a whitepaper.

Stay in this report and introduce existing spatial mechanisms one at a time against the verified homogeneous baseline.

```text
mechanism lanes:
  H0 homogeneous baseline
  S1 psi diffusion only
  S2 phi diffusion only
  S3 phi-gradient / drift influence only
  S4 S1 + S2
  S5 S1 + S3
  S6 S2 + S3
  S7 all three existing spatial mechanisms

dt = 0.1, 0.5, 1.0
stencil = LAP4, LAP8
psi initialization = localized normalized Gaussian
phi initialization = uniform; centred hill; centred well;
                     shuffled field with identical histogram;
                     radially flattened control
noise = disabled
caps and reset events = recorded explicitly
```

For every step and lane record:

- candidate global ledgers including `abs(psi)^2 + phi`, `abs(psi)^2 + phi^2`, and declared gradient terms;
- local `psi` and `phi` gains and losses;
- neighbour and boundary fluxes;
- dissipation loss, cap deletion, and reset amounts;
- whether any `psi` gain is paired with a contemporaneous local debit or incoming flux;
- return of both fields, not only `psi`;
- timestep convergence and stencil sensitivity.

A spatial mechanism counts as candidate reciprocal closure only when the full declared state returns within preregistered tolerances, no hard cap/reset/hidden source is required, `psi` gain is paired with measurable debit or flux under a declared ledger, the classification survives at least two timesteps and both stencils, and shuffled/flattened controls distinguish geometry-dependent transport from histogram-only gain.

A `psi` rebound without a paired debit remains apparent recovery, not reciprocal return.

## 9. Question 3 boundary

Current auxiliary scalar fields do not yet establish a real scalar degree of freedom with an explicit fixed potential minimum, declared kinetic/potential accounting, source-off information retention, return after positive and negative perturbations, stability on the exact `256 x 256` grid, and independence from clipping or resets.

Question 3 remains open. The spatial debit-and-flux experiment may constrain it, but is not itself the full Question 3 test.

## 10. Reproduction and publication record

Decision-relevant receipts required to continue are recorded directly above. No chat memory, second narrative report, external website, or private TOLOG/Lina material is required to understand the state.

A plain UTF-8 companion migration was prepared locally during this checkpoint: ordinary Python sources, readable JSON/JSONL rows, a manifest, and regression tests reconstructed the retained primary exactly. Local migration checks were:

```text
artifact integrity = exact 228809-byte reconstruction; retained SHA-256 matched
localized/readability regression tests = 13 passed
conventional reference tests = 13 passed
full new 28-case recomputation = not completed;
  an attempted rerun exceeded the tool time limit
```

The interrupted rerun is a technical non-result and must not be represented as a completed scientific execution.

The connector could not safely transport every large plain-text companion atomically without truncation risk. Therefore unreferenced staging blobs and local files are **not published evidence**, must be treated as nonexistent in a new thread, and are not part of this checkpoint. No archive, Base64 payload in the repository, Unicode capsule, issue, workflow, or release was used as a workaround.

At the next safe repository-hygiene checkpoint, replace the old self-extracting wrappers through authenticated local Git or another content-preserving path. Do not reintroduce encoded transport and do not change retained scientific values while migrating storage. This hygiene task is not a new scientific lane.

## 11. Claims not established

This report does not establish that:

- TOLOG-Alpha is correct or incorrect;
- any private TOLOG implementation was audited;
- Lineum reproduces blind held-out galaxy rotation;
- `phi` is physical energy;
- the candidate ledger is complete;
- a new return term is required;
- a particular repair is uniquely correct;
- Lineum describes dark matter, dark energy, quantum fields, gravity, biology, brains, consciousness, or cosmology;
- visual similarity across scales demonstrates one mechanism;
- the wider Lineum programme is falsified;
- any whitepaper statement should be upgraded.

## 12. Handoff checkpoint for the next thread

The next thread must begin from this file and the then-current `develop` commit, not from chat memory.

```text
active report = research/lineum-public-tolog-galactic-shape-b4.md
programme = public-TOLOG B4 three-question benchmark
verified localized result = 2 cap-dependent partial psi recoveries;
  0 full-state recoveries
verified homogeneous result = apparent psi recovery without reciprocal phi debit
conventional ruler = R0 through R4 passed with independent checker
current mechanism verdict = unresolved;
  tested routes do not close a reciprocal ledger
next scientific action = execute the preregistered one-spatial-term-at-a-time
  debit-and-flux discriminator in Section 8
whitepaper / Core equation change = blocked
new report = forbidden for this continuous programme
private TOLOG or private Lina material = excluded
unpublished local artifact migration = nonexistent for handoff purposes
```

Before the next write: re-fetch `develop`; reread `AGENTS.md`, `.agent/rules.md`, every `.agent/rules.d/*.md`, `.clinerules`, `.cursorrules`, `.windsurfrules`, `docs/repository-boundaries.md`, `docs/LINEUM_CODEX_v1.md`, and applicable workflows; verify this report's current blob SHA; and confirm that no concurrent change touched it.

Do not repeat the galaxy shape screen, reciprocal ruler, localized-L1 checker, or homogeneous accounting audit unless a specific integrity check fails. Proceed to the spatial debit-and-flux discriminator in Section 8. Preserve every negative result and keep implementation facts, observed executions, interpretations, hypotheses, and real-physics claims separate.
