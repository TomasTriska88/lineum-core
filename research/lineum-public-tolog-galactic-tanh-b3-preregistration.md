# Lineum Public-TOLOG Galactic `tanh` Benchmark — B3 Preregistration

**Status:** active  
**Version:** 0.1.1  
**Evidence cutoff:** 2026-08-04  
**Scope:** NGC 3198 baryonic-convention sensitivity only; no shape ablation, population fit, or Lineum replacement  
**Current confidence:** high that the four declared source conventions are operationally distinct; no B3 numerical fit result has been inspected

## 1. Plain purpose

B2 showed that the public `tanh` comparator strongly improves the literal baryonic curve but does not recover the publicly stated reduced chi-squared near `1.5`. B3 asks whether that numerical gap is explained by how the public SPARC component columns are combined before the `tanh` term is fitted.

The comparison is analogous to rebuilding the same machine with the same added motor while changing only how the visible load is weighed. No B2 parameter, row, uncertainty, solver tolerance, bound, or public target is changed.

## 2. Lineage and inherited evidence

Root programme: `Lineum Public-TOLOG Galactic tanh Benchmark`, version `0.1.0`, evidence cutoff `2026-08-04`.

Predecessors:

1. B0/B1 execution version `0.2.0`: official archive provenance and all analytic gates passed.
2. B2 execution version `0.1.1`: the literal convention produced reduced chi-squared `14.770951390521`, versus `294.076280481349` for literal baryons alone; all 16 starts reached the same practical basin, but the preregistered `1e-6 km/s` curve-equivalence gate failed narrowly.

The B2 classification remains `inconclusive` and is not rewritten by B3. B3 is a separately labelled sensitivity study.

## 3. Public source facts and interpretation boundary

Authoritative public facts:

- The official SPARC `MassModels_Lelli2016c.mrt` table states that `Vgas` already includes the factor `1.33` for cosmological helium.
- The same table states that `Vdisk` and `Vbul` are tabulated for stellar mass-to-light ratio `M/L = 1 M_sun/L_sun` at 3.6 micrometres.
- The SPARC master paper discusses a fiducial stellar mass-to-light ratio near `0.5 M_sun/L_sun` for disks.
- Later SPARC radial-acceleration analyses use fiducial values near `0.5` for disks and `0.7` for bulges.
- The official table contains negative `Vgas` entries, including six rows in NGC 3198. A signed-force interpretation must therefore preserve the sign in the velocity-squared contribution as `sign(Vgas) * Vgas^2` rather than silently converting every entry to a positive contribution.

Portable citations:

- Lelli, F., McGaugh, S. S., and Schombert, J. M. (2016), *SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves*, AJ 152, 157, DOI `10.3847/0004-6256/152/6/157`, arXiv `1606.09251`.
- Official SPARC mass-model table and column notes: `https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt`.
- Lelli, F., McGaugh, S. S., Schombert, J. M., and Pawlowski, M. S. (2017), *One Law to Rule Them All: The Radial Acceleration Relation of Galaxies*, ApJ 836, 152, DOI `10.3847/1538-4357/836/2/152`, arXiv `1610.08981`.

The signed formula and the four-lane factorial comparison are Lineum audit conventions frozen by the parent benchmark. They are not claimed to be unrecovered private TOLOG choices.

## 4. Frozen input and comparator

Input:

- target `NGC3198_rotmod.dat`;
- SHA-256 `17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953`;
- all `43` rows retained;
- tabulated `Vobs` and `errV` retained unchanged;
- six rows have `Vgas < 0` and three rows have `Vgas = 0`;
- no radial exclusion and no uncertainty inflation.

For every lane:

`v_model(r) = sqrt(v_bar(r)^2 + V0^2 * tanh(k_eff * r / 5.0 kpc))`.

Only `V0` and `k_eff` are fitted. The fixed B2 bounds, starts, objective, solver settings, and reduced-chi-squared denominator `N-2` remain unchanged.

## 5. Frozen 2x2 convention matrix

Let `G_abs = Vgas^2`, `G_signed = sign(Vgas) * Vgas^2`, `D_1 = Vdisk^2`, `D_05 = 0.5 * Vdisk^2`, `B_1 = Vbul^2`, and `B_07 = 0.7 * Vbul^2`.

| Lane | Gas rule | Stellar rule | Baryonic velocity squared |
|---|---|---|---|
| `literal_m1` | unsigned square | disk/bulge `1/1` | `G_abs + D_1 + B_1` |
| `signed_m1` | signed square | disk/bulge `1/1` | `G_signed + D_1 + B_1` |
| `literal_fiducial` | unsigned square | disk/bulge `0.5/0.7` | `G_abs + D_05 + B_07` |
| `signed_fiducial` | signed square | disk/bulge `0.5/0.7` | `G_signed + D_05 + B_07` |

NGC 3198 has `Vbul = 0` in every retained row, so the bulge coefficient is documented but has no numerical effect for this target.

Each lane must fail explicitly if any baryonic velocity-squared value is negative beyond floating-point tolerance. No clipping is allowed unless a later separately preregistered lane is opened.

## 6. Frozen numerical procedure

For each of the four lanes:

- `V0 in [0, 400] km/s`;
- `k_eff in [1e-6, 100]`;
- initial `V0 = [25, 75, 150, 250] km/s`;
- initial `k_eff = [0.01, 0.1, 1, 10]`;
- deterministic bounded `scipy.optimize.least_squares`;
- method `trf`, two-point Jacobian, linear loss;
- `xtol = ftol = gtol = 1e-12`;
- `max_nfev = 100000`;
- objective `sum(((v_model - Vobs) / errV)^2)`;
- reduced chi-squared denominator `43 - 2 = 41`;
- curve-equivalence tolerance retained at `1e-6 km/s`;
- retain every start, parameter pair, objective, termination receipt, fitted curve, and residual.

No parameter bound, start, tolerance, row, target metric, or convention may be altered after inspecting results.

## 7. Metrics and attribution

Record per lane:

- chi-squared and reduced chi-squared;
- unweighted and weighted RMSE;
- maximum absolute residual;
- AIC with the shared likelihood constant omitted;
- fitted `V0`, `k_eff`, transition scale, half-saturation radius, covariance diagnostics, and boundary contact;
- inner, transition, and outer metrics using the existing B2 boundaries;
- convergence count and maximum all-start curve difference;
- direct scalar recomputation of the objective.

Factorial attribution:

- gas-sign effect at `M/L=1`: `signed_m1 - literal_m1`;
- gas-sign effect at fiducial stellar scaling: `signed_fiducial - literal_fiducial`;
- stellar-scaling effect under unsigned gas: `literal_fiducial - literal_m1`;
- stellar-scaling effect under signed gas: `signed_fiducial - signed_m1`;
- interaction: difference between the two gas-sign effects.

Effects are reported on chi-squared, reduced chi-squared, and fitted parameters. Negative metric differences indicate improvement.

## 8. Frozen decision classes

### `convention_explains_public_gap`

- the `signed_fiducial` lane is valid and numerically stable;
- its reduced chi-squared lies within `1.35` to `1.65`;
- no fitted parameter touches a bound;
- direct scalar recomputation agrees;
- all starts meet the frozen curve-equivalence tolerance.

### `convention_materially_improves_but_gap_remains`

- at least one authoritative change lowers chi-squared by at least `10%` relative to `literal_m1`;
- the best valid authoritative lane remains outside `1.35` to `1.65`;
- the result is finite and independently recomputed.

### `convention_does_not_explain_gap`

- every valid authoritative lane changes chi-squared by less than `10%` relative to `literal_m1`, or worsens it;
- the public target remains outside the window;
- numerical gates pass.

### `inconclusive`

- a declared baryonic lane is mathematically invalid for the retained rows;
- fits are materially multimodal or fail convergence;
- input or source interpretation cannot be retained unambiguously;
- independent recomputation disagrees.

A narrow failure of the inherited curve-equivalence tolerance is reported separately and remains binding for any strict reproduction claim.

## 9. Independent and adversarial checks

Required before retention:

1. a direct vector implementation;
2. a separately written scalar-loop objective recomputation for each best fit;
3. exact reproduction of the B2 `literal_m1` result within declared floating-point tolerance;
4. analytic verification that rows with `Vgas=0` are identical under signed and unsigned gas;
5. verification that the six negative-gas NGC 3198 rows differ only by `2*Vgas^2` in baryonic velocity-squared between gas rules;
6. at least one alternative optimizer or dense local cross-check for the best authoritative lane;
7. exact input, runner, output, and retained-table hashes.

## 10. Interpretation firewall

B3 may determine whether standard SPARC source accounting explains the numerical discrepancy. It cannot establish that:

- the public TOLOG value was computed with any tested convention;
- `tanh` is unique, derived, or emergent;
- a Lineum field, foam, vortex, topology, or attractor produces the curve;
- dark matter or modified gravity is supported or excluded;
- one galaxy establishes a population law.

No production Lineum code or whitepaper may be changed from B3 alone.

## 11. Planned retained artifacts

- `research/runners/lineum_public_tolog_tanh_b3_baryonic_sensitivity.py`;
- `research/results/lineum_public_tolog_tanh_b3_baryonic_sensitivity_output.json`;
- `research/results/lineum_public_tolog_tanh_b3_baryonic_sensitivity_rows.csv`;
- `research/lineum-public-tolog-galactic-tanh-b3.md`.

The result report must preserve the full protocol, all decision-relevant values, negative results, uncertainty, reproduction core, root-programme impact, and prohibited conclusions.

## 12. Version history

- `0.1.0`: initial four-lane preregistration.
- `0.1.1`: pre-fit input audit corrected the negative-gas row count from four to six and recorded three zero-gas rows; no numerical fit result had been inspected.