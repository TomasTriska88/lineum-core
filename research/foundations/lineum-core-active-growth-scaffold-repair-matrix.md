# Active Growth and Spatial Scaffold Repair Matrix in Lineum Core

**Status:** active research report; first `mu × kappa` feasibility matrix completed with a reproducible bounded negative result; permanent runner and regression specification committed; exact standalone verifier embedded; supported NumPy `<2.0` execution blocked by the available host; Eq-11.1 selected only for a provenance gate, not numerical execution

**Version:** 0.8.0  
**Evidence cutoff:** 2026-07-30

**Scope:** Core-only research testing the project-owner proposal that organized reconstruction may require both an internally active process (the “yeast”) and a spatial scaffold (the “mould”). No Lina EI, private data, Dynamics, OEA, language model, or product identity model is used.

**Predecessor:** `research/foundations/lineum-core-static-baseline-live-state-transplant-matrix.md`.

**Confidence:** High for the frozen lane relationships and exact independent reproduction on Python `3.13.5` / NumPy `2.3.5`; medium for equivalence to the inspected active NumPy path; low for portability until repeated within NumPy `<2.0`. Nothing here supports heredity, identity, biology, consciousness, or physical-universe claims.

## 1. Answer first

The first operational mapping of “yeast + mould” failed its preregistered repair criterion in all eight cells.

- Maximum absolute `mu` effect on recovery: `0.00004216379362752265`; every measured effect was slightly negative.
- Maximum structured-`kappa` advantage over the mean-matched uniform map: `0.024091442639686052`.
- The same `kappa` effect appeared with and without `mu`.
- Structured-`kappa` lanes changed more outside the damaged region.
- After scaffold removal, previously scaffolded lanes retained less repaired-region energy.
- No `Y1S1` cell met the required synergy threshold.

Plain interpretation: the mould slightly redirected the dough, but the tested `mu` did not act like yeast. The combined lane was practically the mould-only lane.

## 2. Owner hypothesis and first mapping

Owner hypothesis recorded before formalization:

> Yeast makes dough from flour and water, while a mould gives it shape.

First mapping:

- material: matched weak `psi` and `phi` ring;
- yeast `Y`: active `mu` accumulation and the `1 + mu` feedback multiplier;
- mould `S`: structured static `kappa`;
- damage: erase the right-hand 90-degree ring sector from `psi` and `phi`;
- preserved during damage: `mu` and `kappa`;
- scaffold removal: replace structured `kappa` with a mean-matched uniform map.

Verdict: `unsupported_under_tested_conditions`. The broader combination hypothesis remains open for causally different mechanisms.

## 3. Delegated scientific autonomy

On 2026-07-30 the owner granted full methodological discretion. This permits conservative selection of mechanisms, controls, observers, and horizons without routine interruption. It does **not** permit relaxed thresholds, selective reporting, post-hoc target changes, relabelling failures, hiding null results, premature public-library placement, or whitepaper promotion without the evidence gates below.

Negative findings, contradictory evidence, missing scripts, unstable branches, null effects, and documentation conflicts have the same reporting priority as positive findings.

## 4. Whitepaper handoff contract

After the programme is complete, statements must be classified as:

- `eligible_for_canonical_wording`;
- `implementation_fact_only`;
- `bounded_negative_result`;
- `hypothesis_only`;
- `unresolved`.

Whitepapers must be updated from this report’s final evidence table, not from chat memory or a final summary.

| Whitepaper | Current relationship | Status |
|---|---|---|
| `whitepapers/1-core/02-core-equation.md` | `mu` is implemented as slow reinforcement but did not repair erasure | `implementation_fact_plus_bounded_negative_result` |
| `whitepapers/2-cosmology/extensions/03-cosmo-ext-lineum-standard-model.md` | Relic Foam remains a distinct environmental family; true re-ignition and infinite reuse were negative | `distinct_variant_not_yet_retested` |
| `whitepapers/2-cosmology/extensions/05-cosmo-ext-thermodynamic-attractor.md` | `epsilon` shock recovery is not spatial regrowth; cited script is not currently located | `historical_result_pending_reproduction` |
| `whitepapers/2-cosmology/hypotheses/37-cosmo-hyp-quantum-foam-and-mu-emergence.md` | this test gives no support for emergent mass or repair information | `hypothesis_only_and_implementation_conflict` |
| `whitepapers/3-ontology/extensions/01-ontology-ext-ai-reservoir.md` | existing deprecation is consistent with absent demonstrated memory repair | `bounded_negative_result_already_recorded` |
| `whitepapers/3-ontology/extensions/03-ontology-ext-identity-layer.md` | dynamic-`kappa` memory claims conflict with active code | `requires_scope_correction_after_program_completion` |
| `whitepapers/3-ontology/hypotheses/11-ontology-hyp-kinetic-ignition.md` | no verified mechanism link | `hypothesis_only` |
| `whitepapers/3-ontology/hypotheses/12-ontology-hyp-order-vs-chaos.md` | no support for psychological or moral persistence claims | `hypothesis_only` |
| `whitepapers/3-ontology/hypotheses/16-ontology-hyp-emergent-ai.md` | existing deprecation remains consistent | `bounded_negative_result_already_recorded` |

No canonical wording is authorized yet.

## 5. Active implementation facts

Inspected source: `lineum_core/math.py`, blob `bb877021810691223a0eb960a45493a2e351112a`.

- `kappa` is supplied spatially and returned unchanged.
- `kappa` multiplies generation, interaction, drift, diffusion, `phi` evolution, and `mu` growth.
- `mu` is read through `1 + mu` and accumulates above a relative `psi`-energy threshold.
- No active term detects missing structure or compares the current state with a target.

Therefore `mu` can reinforce existing routes but does not encode where erased `psi` and `phi` should be rebuilt.

## 6. Frozen first-matrix protocol

| Lane | `mu` | structured `kappa` |
|---|---:|---:|
| `YS00` | off | off |
| `Y1S0` | on | off |
| `Y0S1` | off | on |
| `Y1S1` | on | on |

Every lane had a damaged run and a matched no-damage twin.

```text
grid = 32 x 32
ring = exp(-((r - 0.45) / 0.10)^2)
psi = 0.30 * ring * exp(i * theta)
phi = 0.02 * ring
mu = 0
kappa_structured = 0.55 + contrast * (ring - mean(ring))
kappa_uniform = 0.55
damage = (ring > 0.20) and (abs(theta) <= pi/4)
```

Frozen grid:

- formation `{20,60}` steps;
- `mu_eta {0.005,0.020}`;
- `kappa` contrast `{0.25,0.40}`;
- repair `40` steps;
- post-removal `40` steps;
- `mu_rho=0.0001`;
- `mu_peak_cutoff_ratio=0.1`;
- deterministic seed `314159`;
- stochastic generation disabled;
- Python `3.13.5`, NumPy `2.3.5`.

Combined support required recovery at least `0.10` above all competitors, outside-mask NRMSE within `0.10` of the best single factor, total `psi` energy at most `1.25×` its twin, `max(abs(psi)) < 10`, finite arrays, no reset, and valid `kappa`. No cell passed the first condition; stability conditions passed.

## 7. Complete results

| formation | `mu_eta` | contrast | `YS00` | `Y1S0` | `Y0S1` | `Y1S1` |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 0.005 | 0.25 | 0.025888249 | 0.025886804 | 0.036974175 | 0.036970988 |
| 20 | 0.005 | 0.40 | 0.025888249 | 0.025886804 | 0.043465128 | 0.043460504 |
| 20 | 0.020 | 0.25 | 0.025888249 | 0.025882428 | 0.036974175 | 0.036961318 |
| 20 | 0.020 | 0.40 | 0.025888249 | 0.025882428 | 0.043465128 | 0.043446461 |
| 60 | 0.005 | 0.25 | 0.033924417 | 0.033921008 | 0.049030842 | 0.049023558 |
| 60 | 0.005 | 0.40 | 0.033924417 | 0.033921008 | 0.058015860 | 0.058005431 |
| 60 | 0.020 | 0.25 | 0.033924417 | 0.033910669 | 0.049030842 | 0.049001418 |
| 60 | 0.020 | 0.40 | 0.033924417 | 0.033910669 | 0.058015860 | 0.057973696 |

Collateral and removal:

- uniform outside-mask NRMSE: `0.1316–0.1347`;
- structured outside-mask NRMSE: `0.1464–0.1653`;
- uniform retention after removal horizon: `0.8407–0.8950`;
- previously structured retention after replacement with uniform `kappa`: `0.7140–0.8086`.

Sanity checks passed: toy recovery signs, equal mean `kappa`, valid interval, exact repeated output, independent reconstruction, finite cells, `max(abs(psi)) < 0.142`, no fail-safe reset, and energy ratios `0.717–0.735`.

Machine receipt:

```json
{
  "original_result_sha256": "4ea006e0c29f887fd4eb46472512726909e751cb9bd3980daf5f4ec88c569de6",
  "committed_runner_sha256": "fad38b738b4f2eb68a2fe5d7732e131a599d813e48d7cd79699a3f4865440a45",
  "independent_verifier_sha256": "1771af23647838b9231476d019d3ae379aa1ba473506b54c38b8192b76a1d600",
  "independent_result_sha256": "da4c7187330379829522ed82b75934bf1fecfe2ace07d1ea1ad4cb8d4e07192c",
  "supportive_cells": [],
  "max_abs_mu_effect": 0.00004216379362752265,
  "min_kappa_effect": 0.011078889497591261,
  "max_kappa_effect": 0.024091442639686052,
  "max_abs_psi": 0.14159671954731448
}
```

Permanent research files:

- `scripts/research/active_mu_kappa_repair_matrix.py`, commit `164c989c439873de699176f937342778c7b83ced`;
- `tests/research/test_active_mu_kappa_repair_matrix.py`, commit `4b3ba06651882138c81dafa5ae003221738c100c`.

## 8. Supported and unsupported interpretations

Supported only in the frozen available-host setup:

- structured static `kappa` modestly changes passive redistribution;
- `mu` is negligible for reconstruction;
- `Y1S1` is observationally equivalent to scaffold-only at the measured resolution;
- previously scaffolded lanes are more scaffold-dependent;
- independent reconstruction reproduced all decision metrics.

Not supported: `mu` as a repair recipe, `mu × kappa` synergy, autonomous regrowth, heredity, semantic memory, identity, life, consciousness, physical-universe claims, or NumPy `<2.0` portability.

## 9. Mechanism ranking and next gate

Ranking criteria: causal difference from failed reinforcement, equation/implementation traceability, known failure visibility, cheap falsifiability, target-copying risk, and standalone reproducibility.

| Rank | Family | Main strength | Main blocker |
|---:|---|---|---|
| 1 | `B_eq11_growth_kappa` | explicit active growth/leakage equation and extensive negative history | incomplete script and parameter provenance; contradictory historical claims |
| 2 | `C_epsilon_scaffold` | distinct closed resource cycle | cited `eval_closed_system_stress.py` not located; incomplete reproducible specification |
| 3 | `D_active_foam` | described environmental co-stabilization | cited foam scripts not located; true re-ignition and infinite reuse already failed |
| 4 | `E_dynamic_scaffold` | directly supplies a state-responsive form | no existing exact mechanism; high invention/tuning risk |
| 5 | `F_generative_controller` | can encode what should regrow | highest risk of direct target copying and leaving Core-native dynamics |

Retrieval negative: `eval_closed_system_stress.py` and `eval_foam_material.py` were not found at repository root, `scripts/`, or `scripts/research/` on `develop`. Code search also did not locate them, but its index is known to lag new commits. Status: `not_located_in_current_retrieval`, not proof they never existed.

The most explicit surviving Eq-11.1 law is:

```text
∂t Psi = D_Psi ∇²Psi + [alpha tanh(c1 Phi) - gamma - lambda Phi² - c_w |∇Psi|²] Psi
∂t Phi = D_Phi ∇²Phi + c2 |Psi|² - gamma_Phi Phi
```

The same history records missing survivor scripts, reconstructed decay, far-field boiling at low leakage, failed source-normalized composites, and failure of a weak smooth `kappa` well. These negatives require a baseline provenance gate before any repair test.

Selected next lane: `B_eq11_growth_kappa`, **provenance gate only**. Numerical execution is not authorized until:

1. all surviving parameter sets and integration conventions are recovered;
2. each is classified canonical, candidate, historical, experimental, deprecated, contradicted, or unreproducible;
3. an internally consistent set independent of missing-script claims is identified;
4. its undamaged baseline is reproduced;
5. the lane is rejected if that baseline decays below its own criterion or causes far-field boiling;
6. only then is an active-growth × scaffold erasure matrix preregistered.

## 10. Limitations

- completed runs used NumPy `2.3.5`, outside the declared `<2.0` range;
- Python 3.12 / NumPy 1.26 installation was blocked by DNS/network failure;
- isolated NumPy path only;
- one morphology and one damage geometry;
- deterministic source-off regime only;
- eight feasibility cells, not broad inference;
- `mu` preserved but not separately erased;
- no second damage after scaffold removal;
- no topology-specific node observer;
- no empirical-universe comparison;
- Eq-11.1, `epsilon`, and foam histories contain provenance gaps.

## 11. Continuous ledger

- `2026-07-30 owner hypothesis`: recorded yeast + mould before formalization.
- `protocol creation`: preregistered factorial logic before implementation.
- `whitepaper handoff`: established evidence classes.
- `repository retrieval`: separated code facts, historical variants, negative results, and analogies.
- `first-pilot freeze`: committed the eight-cell protocol before execution.
- `matrix execution`: recorded all negative and positive effects before selecting another mechanism.
- `permanent capture`: committed runner and regression specification outside `lineum_core/`.
- `delegated autonomy`: recorded discretion without waiving scientific gates.
- `independent reproduction`: matched every decision metric.
- `supported-environment blocker`: recorded as infrastructure, not validation or scientific failure.
- `verifier embedding and ranking`: embedded the exact verifier payload below; selected Eq-11.1 only for provenance reconstruction.

## 12. Complete standalone verifier payload

The exact independent verifier is embedded as gzip-compressed base64. Source SHA-256: `1771af23647838b9231476d019d3ae379aa1ba473506b54c38b8192b76a1d600`.

Save the payload as `verify_mu_kappa_frozen.py.gz.b64`, then run:

```bash
python - <<'PY'
from pathlib import Path
import base64, gzip
src = gzip.decompress(base64.b64decode(Path("verify_mu_kappa_frozen.py.gz.b64").read_text()))
Path("verify_mu_kappa_frozen.py").write_bytes(src)
PY
python verify_mu_kappa_frozen.py
```

```text
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
```