# Lineum Public-TOLOG Three-Question Benchmark — B4

**Status:** active authoritative report; localized-L1 negative independently verified; owner response and attributed external hypothesis recorded; cross-workspace hypothesis retrieval pending; no replacement mechanism selected  
**Version:** 0.13.0  
**Evidence cutoff:** 2026-08-07  
**Repository / branch:** `TomasTriska88/lineum-core` / `develop`  
**Checkpoint parent:** `7232b49ae2f2381d8c4c705f1da661e3de11f3b2`  
**Scope:** exactly three public comparison questions; public TOLOG information only; no private TOLOG material; no private Lina EI implementation; no Core equation or whitepaper change

## 0. Authority and continuity

This is the single active report for the continuous public-TOLOG B4 programme. It consolidates the galaxy-shape baseline, conventional exchange calibration, homogeneous accounting audit, localized spatial screen, independent verification, negative results, contradictions, and the next gate.

Versions through `0.10.1` used opaque compressed Unicode payloads. They are no longer embedded. The exact former report remains immutable as Git blob `8f08fe0da08751781e13f90496a928f89eae9d56`. The former overlapping classical-reference report is absent from the active branch; its decision-relevant content is restated here and its historical blob is `68b0ae44795124e13b8bccdd743a93b6a4ac3786`.

The concurrent `0.11.2` checkpoint at `bf768c5a3463f3d959058bf91eaf7653face1cc6` preserved a complete next-thread handoff and a detailed spatial debit-and-flux candidate protocol. Version `0.12.0` retained that protocol behind the mandatory owner-intuition gate. The owner has now answered independently, and this revision records that response plus Káťa's separately attributed hypothesis without treating either as evidence or selecting a replacement mechanism.

Every conclusion below separates implementation facts, reproduced observations, cautious interpretation, hypotheses, and real-physics claims. Internal numerical agreement is not evidence that nature uses the same ontology.

## 1. Plain conclusion

The tested Lineum implementation did **not** complete a natural reciprocal `psi`–`phi` return cycle.

The localized screen kept all 28 cases finite over the declared horizon, but produced only two partial `psi` recoveries. Both occurred with seeded `phi` held against the explicit `1,000,000` cap. No case recovered the full preregistered state. Removing the cap or all hard guards remained finite over that horizon but produced no recovery. LAP8 changed some measurements but did not uniquely stabilize the state.

A frozen independent checker recomputed all 28 cases through a separate update and metric implementation. It found zero numeric mismatches, zero categorical mismatches, maximum absolute difference `4.547473508864641e-13`, maximum relative difference `9.11739763514324e-16`, and `passed = true`. The localized negative therefore reaches `robust_within_tested_domain` for the exact frozen protocol and observers.

The independently checked homogeneous reduction explains why a later rise in `psi` is insufficient evidence of return. Explicit mode transfer moves accounted quantity from `psi` to `phi`, while a separate feedback term can increase `psi` without decreasing `phi`. Dissipation removes quantity without crediting the reservoir, and the cap can discard excess `phi`. In the verified full lanes, `psi` recovered while `phi` never decreased and the declared `abs(psi)^2 + phi` ledger grew by millions. That is apparent component recovery, not demonstrated reciprocal return.

This bounded negative does not falsify spatial Lineum, identify the correct repair, establish the physical meaning of `phi`, validate TOLOG-Alpha, or show that nature follows this simulation.

## 2. Controlling questions and current answers

1. Can Lineum produce real-galaxy rotation with at least `98%` preregistered held-out agreement from independently defensible source and initial conditions alone, without target leakage, galaxy-specific output fitting, a dark-matter component, or a renamed fitted surrogate?  
   **Current answer:** the descriptive target is characterized, but blind autonomous emergence is not demonstrated.
2. Does Lineum possess a finite mathematical attractor that remains bounded and returns after perturbation without noise, clipping, caps, resets, or ad hoc damping, including a declared discrete equivalent of `r -> 0`?  
   **Current answer:** no full-state recovery was observed in the independently verified localized screen; the homogeneous audit shows apparent `psi` recovery is not reciprocal reservoir return.
3. Can the exact `256 x 256` grid integrate a genuinely real scalar degree of freedom with an explicit fixed potential minimum that retains localized information after source removal and returns after positive and negative perturbations?  
   **Current answer:** scalar-valued auxiliary fields exist, but the required fixed-potential information-preserving scalar state is not demonstrated.

## 3. Question 1 — retained SPARC B4 shape baseline

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

Not established: that Lineum generates the curves from source conditions; that fitted `tanh` is a physical law; that dark matter is unnecessary; that public TOLOG claims are reproduced; or that any model meets a blind `98%` held-out criterion. Question 1 remains blocked on a mathematically explicit state-to-observable bridge and held-out evaluation.

## 4. Conventional reciprocal-exchange ruler

| Lane | Behaviour | Result |
|---|---|---|
| `R0` | coherent resonant exchange | complete transfer and return |
| `R1` | detuned coherent exchange | partial recurrent transfer |
| `R2` | reciprocal rate exchange | monotonic equilibration, no recurrence |
| `R3` | one-way accumulator | conserved total, no return |
| `R4` | uncoupled null | stationary components |

The primary and separately implemented analytic checker agreed with zero mismatches.

```text
primary JSON SHA-256 = bcfec07204869be1b8d798d1d0f4d20999a38cf132e72cbf4d31de6d0a0c5e98
checker JSON SHA-256 = 27ba9b699ec2cfaba38fd051fd80eed374ac5a072a6e8897e838c0003e86798f
```

This ruler fixes vocabulary only: reciprocal terms do not guarantee coherent return, conservation does not guarantee recurrence, and a stable localized object does not by itself prove reservoir return. It does not validate a physical mapping for Lineum.

## 5. Homogeneous accounting audit

For uniform fields, `kappa = 1`, `mu = 0`, `delta = 0`, disabled noise, and `dt = 1`, spatial terms vanish. The audited surviving map is:

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

The mode-transfer substep approximately conserves the declared `E + phi` ledger. The feedback substep does not. Dissipation removes `psi` without crediting `phi`; the cap discards excess `phi`. The surviving multipliers are real and positive and carry no second relative-phase variable, so this homogeneous scalar reduction cannot instantiate conventional coherent `R0` recurrence.

| Lane | Classification | Apparent recovery | True return | Final `E` | Final `phi` | Final ledger |
|---|---|---:|---:|---:|---:|---:|
| full, default cap | apparent recovery without reciprocal ledger | step `701` | no | `2900150.257034308` | `1000000.0` | `3900150.257034308` |
| full, cap-free | apparent recovery without reciprocal ledger | step `701` | no | `2900150.257034308` | `2359502.643825432` | `5259652.90085974` |
| no feedback | dissipative one-way accumulation | no | no | `2.650267646912908e-10` | `0.0902893517688856` | `0.09028935203391236` |
| mode transfer only | one-way conserved transfer | no | no | `0.13519992446823598` | `0.8648000730057612` | `0.9999999974739973` |
| feedback only, seeded | unpaired feedback source | no | no | `1482693.5590557144` | `1.0` | `1482694.5590557144` |
| dissipation only | sink | no | no | `4.427529784808337e-05` | `0` | `4.427529784808337e-05` |
| null | stationary | no | no | `1.0` | `0` | `1.0` |

```text
phi_decrease_count = 0
first default-cap contact = step 1521
mode-transfer-only ledger drift = 2.5260027403106733e-09
homogeneous checker JSON SHA-256 = 81cb30ba92ac3848095582afadde4fb9c24ac6138928e21c1eb3553f6d023adc
checker passed = true; mismatches = []
```

A readable replay initially omitted a `1e-12` normalization epsilon and failed exact comparison. Restoring it reduced the maximum final discrepancy to `9.779e-09`. This is a transcription warning, not a new official scientific run.

## 6. Localized spatial L1 screen

### Frozen protocol

```text
grid = 32 x 32; periodic boundary; dt = 1.0
primary updates = 5000; recovery updates = 1000
stencils = LAP4, LAP8; initial phi = 0, 1
kappa = 1; mu = 0; delta = 0; noise disabled
initial psi = normalized centered Gaussian, peak 1, sigma 3
lanes = baseline, no hard guards, no linear dissipation, no tanh,
        no denominator, no mode coupling, no phi cap
total = 28 cases
```

Localized `psi` recovery required finite/reset-free execution, energy error at most `5%`, radial-profile L2 error at most `10%`, half-energy-radius change at most one cell, and center displacement at most half a cell. Full-state recovery additionally required no `phi` cap, `phi` radial-profile L2 error at most `10%`, and the preregistered late-`phi` slope gate.

```text
source commit = c513a65f16a65f6f600864f55a4edcd5fdfc69a7
workflow run / job / artifact = 31048211101 / 92448891365 / 8947333992
primary JSON bytes / SHA-256 = 228809 / 499dabf444bf442eb9c36927d67a51505166ce422f1e428794aa20def560f11d
artifact ZIP SHA-256 = ca9a9ca05ffe0077ec15dce87ac8309a78b7f2ec114ef84d316f4202d535350c
executed cases = 28 / 28
```

Observed:

- all 28 cases retained finite states;
- baseline produced `2 / 4` localized `psi` recoveries and `0 / 4` full-state recoveries;
- both partial recoveries started with `phi0 = 1` and held `phi` at the `1,000,000` cap;
- both baseline `phi0 = 0` cases decayed and failed recovery;
- removing explicit `tanh` again produced two partial recoveries and zero full recoveries;
- removing the cap or all hard guards produced zero recoveries while `phi` reached `12852053.348233`;
- removing linear dissipation produced zero recoveries and maximum pre-perturbation `abs(psi) = 17981.515115`;
- removing the denominator caused two reset events and zero recoveries;
- LAP8 did not uniquely produce full-state stabilization.

### Independent checker receipt

The frozen checker was recovered from the immutable historical archive. Archive and source hashes matched, and its frozen suite passed `9 / 9` before execution.

```text
runner SHA-256 = 96153e37b4e10890d3a0ab52e9463153cfc614eb9a2f1fcc58f23baeafc988bd
checker SHA-256 = 3dfe7f6aa9f4da81c523f1c207c08bc0def175f827658d73aaa83e21df035031
test SHA-256 = 95a5892f140543361eaffbee311016869e780f9bd21c559757b02b427f3b19ec
checker output bytes / SHA-256 = 673 / 6fec721c7877d0dacf781668553fa7a7910f470c12567e2ef71e2837b511d49d
execution receipt SHA-256 = 64d4642c3af1e37d14b2852a748dca52e1a68ebb0bbb2c84db72b01c3e86518e
progress SHA-256 = a0241a92fbca6c488f2c703cd21644538badb677d6838820d5502605985d9e67
checker environment = Python 3.13.5 / NumPy 2.3.5 / pytest 9.0.2
```

The checker executed exactly once against the retained primary, returned code `0`, recomputed all 28 runs, did not import the primary runner, and used a separate update and metric implementation.

```json
{
  "passed": true,
  "protocol_pass": true,
  "fidelity_receipt_pass": true,
  "key_set_pass": true,
  "numeric_mismatch_count": 0,
  "categorical_mismatch_count": 0,
  "maximum_absolute_difference": 4.547473508864641e-13,
  "maximum_relative_difference": 9.11739763514324e-16
}
```

**Evidence level:** `robust_within_tested_domain` for the exact frozen equations, parameters, boundary, horizon, perturbation, observers, and thresholds. The result remains below `mechanistically_supported` and `empirically_connected`.

## 7. Interpretation and failure-to-mechanism ledger

1. **Implementation:** the audited update contains unpaired feedback, one-way mode transfer, dissipation without reservoir credit, clipping, spatial transport/diffusion, and optional hard guards.
2. **Reproduced observations:** homogeneous and localized independent checkers agree with their primaries; neither tested route demonstrates reciprocal full-state return.
3. **Hypothesis only:** spatial gradients, diffusion, locality, a different ledger, a different interpretation of `phi`, phase-carrying state, or topology might alter the conclusion.

| Audit item | Bounded finding |
|---|---|
| What failed | no full-state localized recovery; no reciprocal homogeneous return |
| What remained positive | all localized cases finite; two cap-dependent partial `psi` recoveries; independent numerical agreement |
| Likely failure location | equation, ledger, or interpretation more than stencil choice alone |
| Current implementation status | unsupported as a natural reciprocal attractor under tested conditions |
| Wider Lineum status | unresolved; not falsified |
| Cheapest discriminator after owner gate | minimal periodic spatial accounting test, activating one existing spatial term at a time |

Registered repair families, not yet selected: paired reciprocal debit; reinterpretation of `phi`; alternative nonlinear or gradient ledger; spatial redistribution; phase-carrying or extra-state variants; and the null case that this equation family has no natural return. These are agent-generated candidates and must not lead the owner's response.

No laboratory, quantum, gravitational, dark-matter, cosmological, biological, consciousness, or ontological connection is established.

## 8. Attributed intuition and hypothesis register

The negative-result gate used the transparent-tray scene: a small whirlpool represented localized `psi`, dark fluid represented `phi`, the artificial wall represented the cap, and the earlier complete arrangement represented the preregistered full state.

### 8.1 Tomáš's owner hypothesis — rotating tray or frame

The project owner's independent response, translated from Czech, was:

> Could the tray itself be rotating?

**Provenance:** Tomáš Tříska, project owner, 2026-08-07.  
**Status:** owner-generated hypothesis; untested; not evidence.

The response introduces a class that the frozen L1 observer did not directly test. The prior screen compared amplitudes, radial profiles, center displacement, radii, and `phi` behaviour in the fixed lattice frame. It did not ask whether an apparently changed state becomes close to the earlier state after a global rotation, translation, co-moving transform, or complex-phase alignment.

Cautious formal variants, generated only after preserving the owner's wording:

| ID | Candidate interpretation | Cheapest discriminating observable | Current status |
|---|---|---|---|
| `T-F0` | null: no global frame or phase transform explains the apparent return | fixed-frame result remains unchanged after all preregistered alignments | untested |
| `T-F1` | rigid spatial-frame alias | best-fit periodic translation and lattice-compatible rotation materially reduce full-state error for both `psi` and `phi` | untested |
| `T-F2` | co-moving or advected structure | a tracked rotating/translating frame preserves the localized object while the fixed observer reports loss and reappearance | untested |
| `T-F3` | internal complex-phase rotation | phase-aligned complex `psi` returns although amplitude-only or fixed-phase observers misclassify it | untested |

The smallest candidate test is observer-first, not equation-first: freeze permitted transforms and tolerances before looking at outcomes, compare both components under the same transform, and retain a no-transform null. If the historical primary lacks the required full snapshots, only the smallest frozen cases should be rerun after the protocol and provenance search are complete. No rotating-force term, new field, or production-code change is justified at this stage.

### 8.2 Káťa's hypothesis — energy budget, phase state, compaction, and emergent gravity

The owner supplied the following hypothesis from Káťa, translated from Czech and attributed to her:

> The type or state of atoms depends on energy consumption. More available energy makes the state more gas-like; less available energy makes it more solid and requires more energy for a transition. Gravity is a manifestation rather than a primary phenomenon. Material with less energy contracts into itself in order to conserve as much energy as possible.

**Provenance:** Káťa, supplied by Tomáš Tříska, 2026-08-07.  
**Status:** Káťa-generated hypothesis; untested; not evidence; attribution must be retained if any later result uses or supports it.

For scientific testing, the statement is separated into distinguishable variants rather than accepted as one bundle:

| ID | Testable core | Operational reading for this programme | Current status |
|---|---|---|---|
| `K-E1` | net energy budget controls mobility | positive local surplus predicts greater spreading or transport; deficit predicts reduced mobility | untested |
| `K-E2` | deficit promotes compaction | lower available energy relative to maintenance cost predicts a smaller localization radius or inward flux | untested |
| `K-E3` | state transition has memory or hysteresis | equal instantaneous energy can produce different compactness depending on prior history | untested |
| `K-G1` | gravity-like attraction is emergent | inward drift or contraction appears as an effective consequence of the energy-budget dynamics rather than an inserted fundamental force | untested |
| `K-N0` | null | compactness and mobility do not track the proposed energy budget after controls | untested |

The literal claims about atomic identity and melting point are not adopted as established physics. In standard thermodynamics, atomic identity is fixed primarily by nuclear composition, and a melting point is a material- and pressure-dependent transition property rather than a simple function in which possessing more energy universally lowers the melting point. The scientifically usable candidate here is narrower: a driven system may change mobility, compactness, and transition threshold according to its stored energy, incoming energy, dissipation, binding, pressure, and history. That narrower interpretation must still be tested and must not be retroactively attributed to Káťa as though she supplied the formalization.

External terminology boundary: IUPAC defines atomic number as the number of protons in the nucleus; defines a phase transition through changes driven by imposed conditions such as temperature and pressure; and defines melting as solid-to-liquid conversion by heat and/or pressure. Portable references: IUPAC Gold Book, 5th ed. (2025), `atomic number`, DOI `10.1351/goldbook.A00499`; `phase transition`, DOI `10.1351/goldbook.P04537`; `melting`, DOI `10.1351/goldbook.M03821`; `melting temperature`, DOI `10.1351/goldbook.12788`. NIST Technical Note 2312 (D. Burgess, 2025), DOI `10.6028/NIST.TN.2312`, documents element-specific phase-transition temperatures at atmospheric pressure. These references constrain the literal physical wording; they do not validate or falsify the narrower Lineum candidate.

A possible relation to the B4 failure is only an agent interpretation: the reappearing `psi` object might be a new localization or compaction caused by a background energy imbalance, not restoration of the original `psi`–`phi` arrangement. This must be distinguished from Tomáš's rotating-frame hypothesis, conventional transport, reciprocal exchange, numerical caps, and the null.

No experiment or mechanism ranking has yet been performed from either attributed hypothesis.

## 9. Preserved failure and publication chronology

Technical non-results retained from history include a stalled checkout; five fail-closed archive-locator attempts (`31051766659`, `31052012351`, `31052264959`, `31052349446`, `31052454245`); one unretained full-screen recomputation that exceeded the command limit; one unretained migration replay; an accidental temporary branch; and a checker workflow rejected before job creation. None is scientific evidence.

The concurrent `0.11.2` checkpoint reconstructed the exact `228809`-byte primary and matched its SHA-256; `13` localized/readability tests and `13` conventional-reference tests passed; an attempted fresh 28-case rerun exceeded the tool limit and remained a technical non-result.

In this checkpoint, an initial staging used renamed source paths and failed test collection before scientific execution. A later connector attempt could not safely publish the recovered large plain Python sources within the payload boundary. No truncated source was published. The ordinary readable checker output, progress stream, execution receipt, and manifest are retained as companion files. Exact source republishing remains explicit reproducibility debt; immutable historical blobs and source hashes remain recorded.

The primary used Python `3.13.14` and NumPy `2.3.5`; the checker used Python `3.13.5` and NumPy `2.3.5`. Their agreement survives the Python patch-version difference. Because the repository historically declared NumPy below `2.0`, promotion into a currently supported runtime claim still requires a supported-dependency rerun.

## 10. Claims explicitly not established

This report does not establish a universal galactic `tanh` law; autonomous `98%` emergence; absence of dark matter; modified gravity; a mathematical bridge to TOLOG; a physical `3 x 3` elementary cell; TOLOG Dark Heart; an emergent `tanh` replacement; a natural bound-free attractor; a complete `psi`–`phi` energy cycle; scalar-potential memory; a causal disk mechanism; any replacement mechanism; or a laboratory, quantum, gravitational, cosmological, consciousness, or ontological interpretation.

## 11. Exact next gate after the attributed responses

The attributed responses are now recorded. Before execution, the same report must:

1. retrieve existing frame, advection, rotation, phase, return, reservoir, saturation, compaction, gravity-like, topology, and alternative-ledger hypotheses across the connected Lineum workspace;
2. compare Tomáš's, Káťa's, historical, conventional, null, and agent-generated variants in the reopenable ledger without merging distinct claims;
3. preregister an observer-first frame/phase discriminator because it can test Tomáš's proposal without changing the equation;
4. preregister the smallest periodic spatial accounting discriminator, introducing one existing spatial mechanism at a time;
5. add energy-budget, compactness, mobility, and history observables only where they discriminate Káťa's variants from transport, frame aliasing, reciprocal exchange, cap artefacts, and the null.

The retained `0.11.2` candidate matrix is:

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
phi initialization = uniform; centered hill; centered well;
                     shuffled field with identical histogram;
                     radially flattened control
noise = disabled
caps and reset events = recorded explicitly
```

Each lane must freeze boundaries, initial state, coefficients, runtime, source/sink accounting, local/global ledgers, `phi` debit counts, recurrence, flux, and outcome meanings. Record candidate ledgers including `abs(psi)^2 + phi`, `abs(psi)^2 + phi^2`, declared gradient terms, local gains/losses, neighbour and boundary fluxes, dissipation, cap deletion, resets, full-state return, timestep convergence, and stencil sensitivity.

A spatial mechanism may count as candidate reciprocal closure only if full state returns within preregistered tolerances without a hard cap, reset, or hidden source; `psi` gain has a contemporaneous measurable debit or incoming flux; the classification survives at least two timesteps and both stencils; and shuffled or flattened controls distinguish geometry-dependent transport from histogram-only gain.

Do not add a field, insert a reciprocal repair, tune parameters, run a soliton candidate, change production Core, or edit a whitepaper before the cross-workspace provenance search and frozen discriminators are recorded.

## 12. Version history and handoff

Versions `0.1.0`–`0.9.7` remain in Git history. `0.9.8`–`0.10.1` introduced and repaired opaque archive transport without changing science. `0.11.0` restored readable narrative and consolidated conventional and homogeneous audits. `0.11.2` preserved a complete handoff and detailed spatial candidate protocol. `0.12.0` recovered and hash-verified the frozen localized sources, passed nine tests, executed the independent checker exactly once, promoted the localized negative to `robust_within_tested_domain`, retained readable outputs and receipts, recorded connector publication limitations, preserved the `0.11.2` protocol behind the owner gate, opened that gate, and changed neither production code nor whitepapers. `0.13.0` recorded Tomáš's rotating-tray response and Káťa's separately attributed energy-budget/compaction hypothesis, translated both into explicitly untested variants, identified an observer-first candidate discriminator, and made no numerical, production-code, or whitepaper change.

A new researcher must re-read current rules, verify the active report blob and `research/lineum-public-tolog-b4/artifact-manifest.json`, treat the localized checker as already executed exactly once, preserve both attributions, retrieve the complete connected-workspace hypothesis registry, freeze the observer-first and spatial discriminators, and continue only in this report.
