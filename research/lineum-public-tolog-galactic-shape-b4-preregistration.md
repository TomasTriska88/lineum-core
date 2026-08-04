# Lineum Public-TOLOG Galactic Shape Benchmark — B4 Preregistration

**Status:** active  
**Version:** 0.2.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** equal-flexibility radial-shape ablation on NGC 3198; no population fit, no Lineum-native replacement, and no tuning to the public TOLOG metric  
**Current confidence:** high in the frozen comparison design; no B4 astronomical fit result has been inspected

## 1. Plain purpose

B2 showed that an explicit two-parameter `tanh` contribution repairs most of the literal outer-galaxy deficit. B3 then showed that the numerical fit quality is dominated by the assumed stellar mass-to-light scaling: the same `tanh` model moved from reduced chi-squared about `14.77` at tabulated `M/L=1` to about `0.684` at the standard SPARC disk scaling `M/L=0.5`.

B4 asks whether NGC 3198 prefers the specific function `tanh`, or whether it merely requires a generic smooth contribution that rises from zero and saturates to a finite plateau.

The comparison is analogous to replacing one engine cam profile with several equally adjustable profiles while leaving the vehicle, load, measurements, and two control dials unchanged. B4 does not attempt to recover or tune toward the publicly stated reduced chi-squared near `1.5`.

## 2. Lineage and inherited evidence

Root programme: `Lineum Public-TOLOG Galactic tanh Benchmark`, version `0.1.0`, evidence cutoff `2026-08-04`.

Report lineage:

1. B0/B1 execution version `0.2.0`: official archive provenance and analytic known-answer gates passed.
2. B2 execution version `0.1.1`: the literal `M/L=1` `tanh` fit reduced chi-squared from about `294.08` to `14.77`, but did not reproduce the public `~1.5` metric.
3. B3 execution version `0.1.0`: the standard SPARC disk scaling `M/L=0.5` lowered the same `tanh` result to about `0.684`; signed-gas handling was negligible for NGC 3198; the public metric remained unreproduced and convention-dependent.

Inherited constraints:

- the private TOLOG document remains excluded;
- B2 and B3 are frozen and are not retroactively tuned;
- all 43 rows and tabulated velocity uncertainties remain unchanged;
- no public TOLOG metric is a fitting target;
- source conventions remain explicitly separated;
- no production Lineum code or whitepaper may change from B4 alone.

## 3. Frozen input

- galaxy: `NGC 3198`;
- source member: `NGC3198_rotmod.dat` from official SPARC `Rotmod_LTG.zip`;
- target SHA-256: `17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953`;
- rows: `43`;
- columns: radius, observed velocity, velocity uncertainty, gas, disk, bulge, disk surface brightness, bulge surface brightness;
- no row exclusion;
- no uncertainty floor, inflation, covariance approximation, or error rescaling;
- fixed reference radius `r_s = 5.0 kpc`.

## 4. Frozen baryonic source lanes

Let:

- `G_abs = Vgas^2`;
- `G_signed = sign(Vgas) * Vgas^2`;
- `D_1 = Vdisk^2`;
- `D_05 = 0.5 * Vdisk^2`;
- `B_1 = Vbul^2`;
- `B_07 = 0.7 * Vbul^2`.

| Lane | Baryonic velocity squared | Decision role |
|---|---|---|
| `literal_m1` | `G_abs + D_1 + B_1` | historical B2 control |
| `signed_m1` | `G_signed + D_1 + B_1` | signed-gas `M/L=1` sensitivity |
| `literal_fiducial` | `G_abs + D_05 + B_07` | primary public-formula-compatible fiducial lane |
| `signed_fiducial` | `G_signed + D_05 + B_07` | primary signed-force fiducial lane |

NGC 3198 has `Vbul=0` in every retained row, so the bulge coefficient has no numerical effect.

The main B4 classification requires agreement across the two fiducial lanes. The `M/L=1` lanes are source-sensitivity controls and cannot overrule a stable fiducial result unless they expose a numerical failure or a qualitative strong-preference contradiction.

## 5. Frozen equal-flexibility shape family

For every primary shape:

`v_model(r)^2 = v_bar(r)^2 + V0^2 * S(k_eff * r / r_s)`.

Only `V0` and `k_eff` are fitted. Every primary shape is monotone for `x >= 0`, satisfies `S(0)=0`, has unit initial slope `S'(0)=1`, and approaches the same unit plateau `S(infinity)=1`.

| Name | Function `S(x)` | Analytic half-saturation argument `x_50` |
|---|---|---|
| `tanh` | `tanh(x)` | `atanh(0.5)` |
| `exponential` | `1 - exp(-x)` | `ln(2)` |
| `rational` | `x / (1 + x)` | `1` |
| `arctan` | `(2/pi) * atan((pi/2) * x)` | `2/pi` |
| `algebraic` | `x / sqrt(1 + x^2)` | `1/sqrt(3)` |

The `arctan` argument is scaled so its derivative at zero is exactly one. No shape-specific third parameter, exponent, offset, central floor, or asymptotic amplitude is allowed.

## 6. Frozen structural controls

Controls are reported separately and do not count as equal-flexibility primary shapes.

1. `baryonic_null`, zero fitted parameters:

   `v_model^2 = v_bar^2`.

2. `constant_plateau`, one fitted amplitude:

   `v_model^2 = v_bar^2 + V0^2`.

3. `linear_nonsaturating`, one fitted amplitude:

   `v_model^2 = v_bar^2 + V0^2 * (r / r_s)`.

Controls use their true parameter count in AIC and degrees-of-freedom calculations. A linear fit over the finite observed range does not establish physically unbounded growth.

## 7. Frozen numerical procedure

For each primary shape in each source lane:

- `V0 in [0,400] km/s`;
- `k_eff in [1e-6,100]`;
- starts `V0 = [25,75,150,250] km/s`;
- starts `k_eff = [0.01,0.1,1,10]`;
- `16` starts per shape-lane pair;
- deterministic `scipy.optimize.least_squares`;
- method `trf`, two-point Jacobian, linear loss;
- `xtol = ftol = gtol = 1e-12`;
- `max_nfev = 100000`;
- objective `chi2 = sum(((v_model - Vobs) / errV)^2)`;
- degrees of freedom `43 - 2 = 41`;
- AIC with common likelihood constant omitted: `chi2 + 4`;
- retained all-start curve-equivalence tolerance `1e-6 km/s`;
- boundary fraction `1e-6` of each fitted interval.

For each one-parameter control:

- `V0 in [0,400] km/s`;
- starts `V0 = [25,75,150,250] km/s`;
- identical solver settings;
- degrees of freedom `42`;
- AIC `chi2 + 2`.

No bound, start, function, source convention, row, uncertainty, metric, or decision threshold may change after inspecting B4 astronomical fit results.

## 8. Analytic gates before astronomical fitting

Every primary shape must pass:

- finite value at zero;
- `S(0)=0` within `1e-15`;
- independently finite-differenced derivative at zero within `1e-8` of one;
- monotonic non-decrease on a frozen `10001`-point grid over `x in [0,100]`;
- values remain in `[0,1]` on that grid within `1e-14`;
- `S(100) >= 0.99`;
- finite positive analytic `x_50` and `|S(x_50)-0.5| <= 1e-14`;
- vector and separately coded scalar evaluations agree within `1e-14` on `x=[0,0.1,1,10,100]`.

The B3 `tanh` best-fit chi-squared must also be reproduced within `1e-8` in both fiducial lanes before shape ranking is accepted:

- `literal_fiducial`: `28.061822168198`;
- `signed_fiducial`: `28.069707094507`.

## 9. Recorded metrics

For every source-lane and primary-shape pair retain:

- best `V0`, `k_eff`, chi-squared, reduced chi-squared, AIC, RMSE, weighted RMSE, standardized RMSE, maximum absolute residual;
- transition scale `r_s/k_eff` and half-saturation radius `r_s*x_50/k_eff`;
- inner (`r<=5`), transition (`5<r<=15`), and outer (`r>15`) metrics;
- all 16 initialization, parameter, objective, status, termination, evaluation, optimality, and active-bound receipts;
- objective spread, parameter spans, maximum all-start curve difference, and boundary contact;
- standardized-residual Jacobian rank, singular values, condition number, covariance estimate, scaled standard errors, and parameter correlation where available;
- separately coded scalar-loop objective and residual recomputation.

Pairwise within each source lane retain:

- delta chi-squared and delta AIC from the best primary shape;
- chi-squared ratio;
- maximum and RMS difference between best fitted curves;
- number of rows where the curve difference exceeds the tabulated `errV`.

## 10. Exact operational definitions

These definitions were frozen before any B4 astronomical result was inspected.

### Stable near-best set

For each fiducial lane, define the near-best set as primary shapes with `delta AIC <= 2`. The generic-saturation stability gate passes only if at least two identical non-`tanh` shape names belong to the near-best set in both fiducial lanes. Equivalently, the intersection of the two fiducial non-`tanh` near-best sets must contain at least two members.

### Material multimodality

A primary shape-lane pair is materially multimodal only if there are two successful start solutions satisfying both:

- their chi-squared values are each within `10` of the best chi-squared;
- their fitted velocity curves differ by more than `1.0 km/s` at any retained row.

Small parameter drift on a shallow but observationally identical basin is reported but is not called material multimodality.

### Independent-optimizer acceptance

- bounded Powell must reproduce the reference best chi-squared within `1e-6`;
- fixed-seed differential evolution plus polishing must reproduce within `1e-5`;
- scalar recomputation must match chi-squared within `1e-10` and the fitted residual array within `1e-12 km/s`.

### Dense local check

For each fiducial winning shape, evaluate a `41 x 41` grid centered on the best fit, spanning `V0 ±5%` and `k_eff ±10%`, clipped to frozen global bounds and including the exact best point. The check passes if no grid point improves chi-squared by more than `1e-6` and the lowest value on every outer edge of the local grid exceeds the reference best value.

### Strong source-convention flip

A strong flip exists only if one fiducial lane satisfies all frozen criteria for `tanh_shape_preferred` while the other satisfies all frozen criteria for `non_tanh_shape_preferred`, or the two lanes materially prefer different non-`tanh` winners under the full `non_tanh_shape_preferred` criteria.

## 11. Frozen decision classes

### `generic_saturation_supported`

Assign only if:

- both fiducial lanes have valid converged primary fits;
- the stable near-best-set gate passes;
- `tanh` is not worse than the best shape by `delta AIC >= 10` in either fiducial lane;
- scalar and independent checks pass;
- no near-best fit touches a bound or is materially multimodal.

Meaning: this galaxy does not identify `tanh` specifically; smooth rise plus finite saturation is sufficient within the test.

### `tanh_shape_preferred`

Assign only if:

- `tanh` is best in both fiducial lanes;
- every non-`tanh` shape has `delta AIC >= 10` in both lanes;
- `tanh` chi-squared is at most `0.8` times the next-best chi-squared in both lanes;
- all numerical and independent checks pass.

### `non_tanh_shape_preferred`

Assign only if:

- the same non-`tanh` shape is best in both fiducial lanes;
- `tanh` has `delta AIC >= 10` relative to it in both lanes;
- the winner chi-squared is at most `0.8` times the `tanh` chi-squared in both lanes;
- all numerical and independent checks pass.

### `shape_differences_small_but_not_equivalent`

Assign if no strong preference class applies, the generic stable near-best-set gate fails, and all numerical and independent checks remain valid.

### `inconclusive`

Assign if any analytic gate fails, a fiducial baryonic lane is invalid, scalar recomputation disagrees, a fit is materially multimodal, a strong source-convention flip occurs, a near-best solution depends on a bound, a required independent check fails, or retained evidence is incomplete.

A narrow miss of the inherited `1e-6 km/s` all-start curve-equivalence threshold is recorded and remains binding for strict numerical equivalence, but does not alone erase a stable ranking unless start dependence changes the decision class.

## 12. Structural-control interpretation

Report separately:

- `transition_needed` if every valid primary shape improves AIC over `constant_plateau` by at least `10` in both fiducial lanes;
- `saturation_needed_over_range` if every valid primary shape improves AIC over `linear_nonsaturating` by at least `10` in both fiducial lanes;
- `control_competitive` if either one-parameter control lies within `delta AIC <= 2` of the best primary shape in a fiducial lane.

These labels do not alter the primary shape classification.

## 13. Independent and adversarial checks

Required before retention:

1. exact input hash and 43-row parse;
2. analytic gates before astronomical fitting;
3. direct vector fitting implementation;
4. separately written scalar objective and residual recomputation for every best primary fit;
5. exact B3 `tanh` regression in both fiducial lanes;
6. bounded Powell for every primary best fit in both fiducial lanes;
7. fixed-seed differential evolution (`20260804`) plus polishing for the best and second-best shapes in each fiducial lane;
8. dense local checks for each fiducial winner;
9. reconstruction of retained curves and row results from machine output;
10. runner, input, output, curve-table, and row-table hashes.

Independent checks must not import a stored fitted curve as their expected answer.

## 14. Interpretation firewall

B4 can establish only comparative descriptive performance for this one galaxy under declared source conventions. It cannot establish that:

- TOLOG privately used any tested shape or convention;
- `tanh` or another shape is derived from an oscillator grid;
- a smooth saturating curve is a force law;
- a Lineum field, foam, vortex, topology, attractor, or memory mechanism generates the response;
- dark matter or modified gravity is supported or excluded;
- the result generalizes to other galaxies;
- lower chi-squared proves truer physics.

## 15. Root-programme impact before execution

| Programme item | Relation |
|---|---|
| Q1 galactic response | `depends_on`: compares descriptive response shapes; no Lineum response generated |
| Q2 natural saturation / attraction | `constrains`: tests whether saturation shape matters observationally; no attractor mechanism tested |
| Q3 information retention | `unaffected` |
| foam-like source loading | `not_yet_compared` |
| central vortex | `not_yet_compared` |
| public TOLOG metric | `unaffected`: no tuning toward `1.5` |
| small galaxy panel | `depends_on`: choose the comparison family after B4 |
| Lineum-native replacement | `depends_on`: identify required response properties first |

## 16. Planned retained artifacts

- `research/runners/lineum_public_tolog_galactic_shape_b4.py`;
- `research/results/lineum_public_tolog_galactic_shape_b4_output.json`;
- `research/results/lineum_public_tolog_galactic_shape_b4_curves.csv`;
- `research/results/lineum_public_tolog_galactic_shape_b4_rows.csv`;
- `research/lineum-public-tolog-galactic-shape-b4.md`.

The execution report must remain standalone and preserve the protocol, complete function definitions, input or an operational reproduction core, results, negative findings, independent checks, uncertainty, prohibited conclusions, and next discriminator.

## 17. Version history

- `0.1.0`: initial B4 shape-family and source-lane preregistration; no astronomical result inspected.
- `0.2.0`: before astronomical execution, replaced qualitative numerical terms with exact stable-set, multimodality, independent-optimizer, dense-grid, and source-flip definitions; scientific question and candidate family unchanged.
