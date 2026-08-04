# Lineum Public-TOLOG Galactic Shape Benchmark — B4 Preregistration

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** equal-flexibility radial-shape ablation on NGC 3198; no population fit, no Lineum-native replacement, and no tuning to the public TOLOG metric  
**Current confidence:** high in the frozen comparison design; no B4 numerical result has been inspected

## 1. Plain purpose

B2 established that an explicit two-parameter `tanh` addition can repair most of the literal outer-galaxy deficit. B3 then showed that the reported goodness of fit is dominated by the assumed stellar mass-to-light scaling: the same `tanh` model moved from reduced chi-squared about `14.77` at tabulated `M/L=1` to about `0.684` at the standard SPARC disk scaling `M/L=0.5`.

B4 asks the next narrower question: does NGC 3198 prefer the specific mathematical shape `tanh`, or does it merely require a generic smooth contribution that rises from zero and saturates to a finite plateau?

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
- source conventions must remain explicitly separated;
- no production Lineum code or whitepaper may change from B4 alone.

## 3. Frozen input

Input target:

- galaxy: `NGC 3198`;
- source member: `NGC3198_rotmod.dat` from the official SPARC `Rotmod_LTG.zip` archive;
- target SHA-256: `17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953`;
- rows: `43`;
- columns: radius, observed velocity, velocity uncertainty, gas, disk, bulge, disk surface brightness, bulge surface brightness;
- no row exclusion;
- no uncertainty floor, inflation, covariance approximation, or error rescaling;
- fixed reference radius `r_s = 5.0 kpc`.

## 4. Frozen baryonic source lanes

All five primary shapes are fitted under four separately labelled baryonic conventions inherited from B3.

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

NGC 3198 has `Vbul=0` for every retained row, so the bulge coefficient has no numerical effect for this target.

The main B4 scientific classification requires agreement across the two fiducial lanes. The `M/L=1` lanes are retained as source-sensitivity controls and cannot overrule a stable fiducial result unless they reveal a numerical or qualitative contradiction.

## 5. Frozen equal-flexibility shape family

For every primary shape:

`v_model(r)^2 = v_bar(r)^2 + V0^2 * S(k_eff * r / r_s)`.

Only `V0` and `k_eff` are fitted. Every primary shape is monotone on `x >= 0`, satisfies `S(0)=0`, has unit initial slope `S'(0)=1`, and approaches the same unit plateau `S(infinity)=1`. This normalization makes the amplitude and local transition-scale parameters comparable without asserting physical equivalence.

Primary shapes:

1. `tanh`

   `S_tanh(x) = tanh(x)`

2. `exponential`

   `S_exp(x) = 1 - exp(-x)`

3. `rational`

   `S_rat(x) = x / (1 + x)`

4. `arctan`

   `S_atan(x) = (2/pi) * atan((pi/2) * x)`

5. `algebraic`

   `S_alg(x) = x / sqrt(1 + x^2)`

The `arctan` argument is scaled so its derivative at zero is exactly one. No shape-specific third parameter, exponent, offset, central floor, or asymptotic amplitude is allowed.

## 6. Frozen structural controls

The following controls are reported separately and are not counted as equal-flexibility primary shapes:

1. `baryonic_null`, zero fitted parameters:

   `v_model^2 = v_bar^2`.

2. `constant_plateau`, one fitted amplitude parameter:

   `v_model^2 = v_bar^2 + V0^2`.

   This tests whether a radial transition is needed at all.

3. `linear_nonsaturating`, one fitted amplitude parameter:

   `v_model^2 = v_bar^2 + V0^2 * (r / r_s)`.

   This tests whether finite-range improvement requires saturation rather than only radial growth.

Controls use their true parameter count in AIC and degrees-of-freedom calculations. They cannot establish preference among the five primary shapes, but they can show whether transition or saturation is empirically useful over the retained radial range.

## 7. Frozen numerical procedure

For each primary shape in each source lane:

- `V0 in [0, 400] km/s`;
- `k_eff in [1e-6, 100]`;
- starts `V0 = [25, 75, 150, 250] km/s`;
- starts `k_eff = [0.01, 0.1, 1, 10]`;
- `16` starts per shape-lane pair;
- deterministic `scipy.optimize.least_squares`;
- method `trf`;
- two-point Jacobian;
- linear loss;
- `xtol = ftol = gtol = 1e-12`;
- `max_nfev = 100000`;
- objective `chi2 = sum(((v_model - Vobs) / errV)^2)`;
- primary-shape degrees of freedom `43 - 2 = 41`;
- primary-shape AIC with common likelihood constant omitted: `chi2 + 2*2`;
- retained all-start curve-equivalence tolerance `1e-6 km/s`;
- boundary fraction `1e-6` of each fitted interval.

For each one-parameter structural control:

- `V0 in [0, 400] km/s`;
- starts `V0 = [25, 75, 150, 250] km/s`;
- identical least-squares tolerances and loss;
- degrees of freedom `43 - 1 = 42`;
- AIC `chi2 + 2`.

No bound, start, function definition, source convention, row, uncertainty, metric, or decision threshold may be changed after inspecting B4 fit results.

## 8. Analytic and implementation gates before astronomical fitting

Every primary shape must pass:

- finite value at zero;
- `S(0)=0` within `1e-15` absolute tolerance;
- derivative at zero equal to one within `1e-8`, using an independently coded central or forward finite difference appropriate to the nonnegative domain;
- monotonic non-decrease on a frozen dense grid `x in [0,100]`;
- values remain in `[0,1]` on that grid within `1e-14` tolerance;
- `S(100) >= 0.99`;
- an independently calculated finite positive half-saturation argument solving `S(x_50)=0.5`;
- vector and scalar evaluations agree within `1e-14` absolute tolerance on frozen test points.

Expected analytic half-saturation arguments:

- `tanh`: `atanh(0.5)`;
- `exponential`: `ln(2)`;
- `rational`: `1`;
- `arctan`: `2/pi`;
- `algebraic`: `1/sqrt(3)`.

The B3 `tanh` best-fit chi-squared must also be reproduced in both fiducial source lanes within `1e-8` absolute tolerance before shape ranking is accepted.

## 9. Metrics

Record for every source-lane and shape pair:

- best `V0` and `k_eff`;
- chi-squared, reduced chi-squared, AIC, RMSE, weighted RMSE, standardized RMSE, and maximum absolute residual;
- transition scale `r_s/k_eff`;
- half-saturation radius `r_s*x_50/k_eff`;
- inner, transition, and outer metrics using `r<=5 kpc`, `5<r<=15 kpc`, and `r>15 kpc`;
- all 16 termination receipts;
- objective spread, parameter spans, and maximum all-start curve difference;
- boundary contact;
- standardized-residual Jacobian rank, singular values, condition number, covariance estimate, scaled standard errors, and parameter correlation when mathematically available;
- direct scalar-loop recomputation of the best objective and residual array.

Record pairwise primary-shape comparisons within each source lane:

- delta chi-squared relative to the best shape;
- delta AIC relative to the best shape;
- chi-squared ratio to the best shape;
- maximum absolute difference between best fitted velocity curves;
- RMS difference between best fitted velocity curves;
- number of rows where the curve difference exceeds the tabulated `errV`.

## 10. Frozen decision classes

### `generic_saturation_supported`

Assign only if all conditions hold:

- both fiducial source lanes have valid, converged primary fits;
- at least two non-`tanh` primary shapes lie within `delta AIC <= 2` of the best primary shape in each fiducial lane;
- `tanh` is not worse than the best primary shape by `delta AIC >= 10` in either fiducial lane;
- the identity of the near-best shape set is qualitatively stable across the two fiducial lanes;
- direct recomputation passes and no near-best fit touches a parameter bound.

Meaning: NGC 3198 does not identify `tanh` specifically; smooth rise plus finite saturation is sufficient within this test.

### `tanh_shape_preferred`

Assign only if all conditions hold:

- `tanh` is the best primary shape in both fiducial lanes;
- every non-`tanh` primary shape has `delta AIC >= 10` in both fiducial lanes;
- `tanh` chi-squared is at most `0.8` times the next-best primary chi-squared in both fiducial lanes;
- all numerical, boundary, and independent-recomputation gates pass.

Meaning: the exact `tanh` shape is materially preferred on this target under both fiducial source conventions. It still would not establish derivation or physical uniqueness.

### `non_tanh_shape_preferred`

Assign only if all conditions hold:

- the same non-`tanh` primary shape is best in both fiducial lanes;
- `tanh` has `delta AIC >= 10` relative to that shape in both fiducial lanes;
- the winning shape chi-squared is at most `0.8` times the `tanh` chi-squared in both fiducial lanes;
- all numerical, boundary, and independent-recomputation gates pass.

Meaning: `tanh` is not the strongest tested saturating descriptor for this target.

### `shape_differences_small_but_not_equivalent`

Assign if:

- no material-preference class above applies;
- fewer than two non-`tanh` shapes meet the `delta AIC <= 2` generic-saturation gate in at least one fiducial lane;
- all fits and independent checks remain valid.

Meaning: the data distinguish some shapes weakly, but do not justify a strong uniqueness claim.

### `inconclusive`

Assign if any decision-relevant condition holds:

- an analytic shape gate fails;
- a declared fiducial baryonic lane is mathematically invalid;
- direct scalar recomputation disagrees materially;
- primary fits are materially multimodal or unstable;
- a source-convention flip changes a strong preference from `tanh` to a different shape or vice versa;
- a near-best solution depends on a parameter bound;
- retained evidence is incomplete.

A narrow miss of the inherited `1e-6 km/s` all-start curve-equivalence threshold is recorded exactly and remains binding for a strict numerical-equivalence claim, but it does not alone erase an otherwise stable shape ranking unless the differing starts change pairwise classification.

## 11. Structural-control interpretation

Report, without promoting to a primary-shape verdict:

- `transition_needed` if every valid primary shape improves AIC over `constant_plateau` by at least `10` in both fiducial lanes;
- `saturation_needed_over_range` if every valid primary shape improves AIC over `linear_nonsaturating` by at least `10` in both fiducial lanes;
- `control_competitive` if either one-parameter control lies within `delta AIC <= 2` of the best primary shape in a fiducial lane.

A linear control that fits the finite observed range does not establish unbounded physical growth. A saturating fit does not establish a natural attractor.

## 12. Independent and adversarial checks

Required before retention:

1. exact input hash and 43-row parse;
2. analytic gates for every shape before astronomical fitting;
3. direct vector implementation for fitting;
4. separately written scalar-loop objective and residual recomputation for every best primary fit;
5. exact B3 `tanh` regression in both fiducial lanes;
6. bounded Powell checks for every primary best fit in both fiducial lanes;
7. fixed-seed differential evolution (`20260804`) plus polishing for the best and second-best primary shapes in each fiducial lane;
8. a dense local two-dimensional objective check around each fiducial winner;
9. reconstruction of every retained curve and row result from the machine receipt;
10. runner, input, output, curve-table, and row-table hashes.

The independent checks must not import a stored fitted curve as the expected answer.

## 13. Interpretation firewall

B4 may establish only comparative descriptive performance for this one galaxy under declared source conventions. It cannot establish that:

- TOLOG privately used any tested shape or source convention;
- `tanh` or another shape is derived from an oscillator grid;
- a smooth saturating curve is a force law;
- a Lineum field, foam, vortex, topology, attractor, or memory mechanism generates the response;
- dark matter or modified gravity is supported or excluded;
- any result generalizes to other galaxies;
- lower chi-squared proves truer physics.

## 14. Root-programme impact map before execution

| Programme item | B4 preregistered relation |
|---|---|
| Q1 galactic response | `depends_on`: compares descriptive response shapes; no Lineum response generated |
| Q2 natural saturation / attraction | `constrains`: tests whether saturation shape matters observationally; does not test an attractor mechanism |
| Q3 information retention | `unaffected` |
| foam-like source loading | `not_yet_compared` |
| central vortex | `not_yet_compared` |
| public TOLOG metric | `unaffected`: B4 does not tune toward `1.5` |
| small galaxy panel | `depends_on`: shape family and source policy should be chosen only after B4 |
| Lineum-native replacement | `depends_on`: target properties must be identified before mechanism replacement |

## 15. Planned retained artifacts

- `research/runners/lineum_public_tolog_galactic_shape_b4.py`;
- `research/results/lineum_public_tolog_galactic_shape_b4_output.json`;
- `research/results/lineum_public_tolog_galactic_shape_b4_curves.csv`;
- `research/results/lineum_public_tolog_galactic_shape_b4_rows.csv`;
- `research/lineum-public-tolog-galactic-shape-b4.md`.

The execution report must remain standalone and preserve the protocol, complete function definitions, input data or an operational embedded reproduction core, results, negative findings, independent checks, uncertainty, prohibited conclusions, and next discriminator.
