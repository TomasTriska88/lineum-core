# Lineum B4 Localized-L1 Independent Verification Receipt

**Status:** active; verified negative within the frozen localized-L1 numerical domain; project-owner intuition gate open  
**Version:** 1.0.0  
**Evidence cutoff:** 2026-08-06  
**Repository / branch:** `TomasTriska88/lineum-core` / `develop`  
**Root programme report:** `research/lineum-public-tolog-galactic-shape-b4.md`, version `0.10.1`, evidence cutoff `2026-08-05`  
**Lineage:** public-TOLOG benchmark -> B4 Question 2 -> localized-L1 primary screen -> independent local verification  
**Scope:** independent verification of the retained 28-case result only; no mechanism selection, parameter tuning, private TOLOG material, real-physics validation, code promotion, or whitepaper change  
**Evidence level:** `robust_within_tested_domain` for the frozen numerical observation; mechanism unresolved

## Plain conclusion

A separately implemented checker recomputed all 28 retained cases and matched the primary result with **zero numerical mismatches and zero categorical mismatches**. The tested LAP4/LAP8 neighbour transport produced two cap-dependent partial `psi` recoveries and **zero full-state recoveries**.

This verifies what the frozen software produced under the exact declared protocol. It does not identify the missing mechanism, falsify Lineum as a whole, or establish that nature behaves this way.

## Frozen protocol

```text
grid = 32 x 32; periodic boundary; dt = 1.0
primary updates = 5000; recovery updates = 1000
stencils = LAP4, LAP8; initial phi = 0, 1
kappa = 1; mu = 0; delta = 0; noise = disabled
initial psi = normalized centered Gaussian, peak 1, sigma 3
lanes = baseline, no hard guards, no linear dissipation, no tanh,
        no interaction denominator, no mode coupling, no phi cap
total = 28 cases
```

Localized `psi` recovery required no reset or non-finite event, energy error at most `5%`, radial-profile L2 error at most `10%`, half-energy-radius change at most one cell, and final centre displacement at most half a cell. Full-state recovery additionally required no `phi` cap, `phi` radial-profile L2 error at most `10%`, and the preregistered one-sided late-`phi` slope gate.

## Primary observation

```text
source commit = c513a65f16a65f6f600864f55a4edcd5fdfc69a7
workflow run / job / artifact = 31048211101 / 92448891365 / 8947333992
artifact ZIP SHA-256 = ca9a9ca05ffe0077ec15dce87ac8309a78b7f2ec114ef84d316f4202d535350c
primary JSON bytes / SHA-256 = 228809 / 499dabf444bf442eb9c36927d67a51505166ce422f1e428794aa20def560f11d
Python / NumPy = 3.13.14 / 2.3.5
executed cases = 28 of 28
```

Observed within the frozen horizon:

- all 28 cases remained finite;
- baseline produced two localized `psi` recoveries and zero full-state recoveries;
- both partial baseline recoveries began at `phi0 = 1` and held `phi` at the explicit `1,000,000` cap;
- baseline `phi0 = 0` cases decayed and failed;
- removing `tanh` again produced two partial and zero full recoveries;
- removing the `phi` cap or all hard guards produced zero recoveries while `phi` reached `12852053.348233`;
- removing linear dissipation produced zero recoveries and maximum pre-perturbation `abs(psi) = 17981.515115`;
- removing the interaction denominator caused two reset events and zero recoveries;
- LAP8 changed some metrics but did not uniquely stabilize the full state.

## Independent verification receipt

The checker does not import the primary runner and separately implements state updates and observables.

```text
checker source bytes / SHA-256 = 24247 / 3dfe7f6aa9f4da81c523f1c207c08bc0def175f827658d73aaa83e21df035031
primary input SHA-256 = 499dabf444bf442eb9c36927d67a51505166ce422f1e428794aa20def560f11d
command = python <checker> --result <primary-json> --output <checker-json>
started UTC = 2026-08-05T23:22:38Z
finished UTC = 2026-08-05T23:22:59Z
elapsed seconds = 21.544811859999754
return code = 0
Python / NumPy = 3.13.5 / 2.3.5
platform = Linux-6.18.35-x86_64-with-glibc2.41
checker JSON bytes / SHA-256 = 673 / 6fec721c7877d0dacf781668553fa7a7910f470c12567e2ef71e2837b511d49d
numeric mismatches = 0
categorical mismatches = 0
maximum absolute difference = 4.547473508864641e-13
maximum relative difference = 9.11739763514324e-16
imports primary runner = false
recomputes all 28 runs = true
separate update and metric implementation = true
```

Exact checker output:

```json
{
  "categorical_mismatch_count": 0,
  "categorical_mismatches": [],
  "environment": {
    "numpy": "2.3.5",
    "platform": "Linux-6.18.35-x86_64-with-glibc2.41",
    "python": "3.13.5"
  },
  "fidelity_receipt_pass": true,
  "independence": {
    "imports_primary_runner": false,
    "recomputes_all_28_runs": true,
    "separate_update_and_metric_implementation": true
  },
  "key_set_pass": true,
  "maximum_absolute_difference": 4.547473508864641e-13,
  "maximum_relative_difference": 9.11739763514324e-16,
  "numeric_mismatch_count": 0,
  "numeric_mismatches": [],
  "passed": true,
  "protocol_pass": true,
  "schema": "lineum-b4-saturation-localized-l1-check/1"
}
```

The checker was invoked exactly once. Afterward, exact hashes were rechecked and the archived harness tests ran without invoking it again:

```text
pytest result = 9 passed in 0.08s
pytest log SHA-256 = 8b8ddcd2e7b63fe945152ea4c56d7e74f75ec09c6df6f5afe0311439df55ede7
```

## Bounded interpretation

Within this exact grid, timestep, horizon, initial states, lanes, stencils, thresholds, and numerical environment, neighbour transport did not produce cap-free localized full-state recovery. The two partial visible recoveries depend on the explicit `phi` ceiling and therefore fail the preregistered full-state gate.

The observation advances from `reproduced` to `robust_within_tested_domain`. No causal explanation advances to `mechanistically_supported`.

No replacement law is selected. No empirical comparison with the observable universe was performed. This receipt establishes no connection to real dark matter, galactic dynamics, natural scalar fields, energy conservation, quantum physics, or another physical system.

```text
tested localized-L1 route = unsupported as cap-free full-state recovery
LAP8-specific full-state stabilization = not observed
wider Lineum programme = not falsified
real physical mechanism = not identified
```

## Root-programme impact

| Root item | Relationship | Bounded impact |
|---|---|---|
| B4 Question 1 | `unaffected` | No galaxy fitting or held-out galactic observable was tested. |
| B4 Question 2 | `constrains` | This localized-L1 route did not yield cap-free full-state recovery. |
| B4 Question 3 | `constrains` | Required information-preserving return was not demonstrated; no explicit potential was tested. |
| Replacement for `tanh` | `not_yet_compared` | Removing `tanh` retained cap-dependent partial outcomes; no replacement was selected. |
| Wider ontology and real physics | `not_yet_compared` | No empirical or ontological conclusion follows. |

## Limitations and chronology

The repository declares NumPy `<2.0`, while the frozen primary and checker use NumPy `2.3.5`. The preregistered environment was preserved; the policy mismatch remains separate.

The two implementations share the frozen protocol, comparison schema, and NumPy major version. Their independence is a separate calculation path, not proof against every shared conceptual mistake.

Earlier GitHub attempts failed before checker invocation and were technical non-results. The invalid workflow was removed in commit `e25d70754ad25ee939b34fed740bf4e0d71bd297`. During local reconstruction one connector range was accidentally retrieved twice; exact comparison removed the duplicate before archive decoding. The archive then matched its declared byte count and SHA-256 before the single checker invocation.

The exact primary JSON and frozen checker source remain losslessly embedded with cryptographic receipts in the root standalone report identified above. This file is the durable local-execution verification receipt and records the complete new output and decision boundary.

## Exact next gate

This verified negative opens the mandatory project-owner intuition gate. Before mechanism selection, parameter tuning, new simulation, variant ranking, external analogy search, or side research, present one neutral vivid scene and ask one fully open-ended question without answer choices, candidate mechanisms, or leading examples.
