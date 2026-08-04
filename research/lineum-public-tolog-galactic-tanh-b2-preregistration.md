# Lineum Public-TOLOG Galactic `tanh` Benchmark — B2 Preregistration

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** literal public-formula NGC 3198 fit only; no baryonic-convention sensitivity, shape ablation, parameter freezing, or Lineum replacement  
**Execution state:** not yet run

## 1. Decision boundary

B0 and B1 passed before this document was written. The frozen input is the `43`-row `NGC3198_rotmod.dat` extracted from the supplied SPARC archive.

Input fingerprints:

- archive MD5: `e4c8b92766026770ed35e5889064e12b`;
- archive SHA-256: `0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588`;
- target SHA-256: `17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953`.

The private TOLOG document remains excluded. No fit result, plot, or residual has been inspected before freezing the additional operational definitions below.

## 2. Literal model

Use the public literal baryonic convention:

`v_bar(r) = sqrt(v_gas(r)^2 + v_disk(r)^2 + v_bulge(r)^2)`.

Use the clean-room comparator:

`v_model(r) = sqrt(v_bar(r)^2 + V0^2 * tanh(k_eff * r / r_s))`.

Fixed quantity:

- `r_s = 5.0 kpc`.

Fitted quantities:

- `V0` in `km/s`;
- dimensionless `k_eff`.

No stellar mass-to-light rescaling, signed-gas correction, radial exclusion, uncertainty rescaling, or additional nuisance parameter is allowed in B2.

## 3. Data and objective

Use all `N = 43` rows.

For each row:

`standardized_residual_i = (v_model_i - Vobs_i) / errV_i`.

Minimize:

`chi2 = sum(standardized_residual_i^2)`.

Use deterministic bounded nonlinear least squares.

Bounds:

- `V0 in [0, 400] km/s`;
- `k_eff in [1e-6, 100]`.

Multi-start grid, in lexical product order:

- `V0 = [25, 75, 150, 250] km/s`;
- `k_eff = [0.01, 0.1, 1, 10]`.

This gives `16` starts. Retain every start's initial values, termination state, objective, fitted parameters, optimality, evaluations, and fitted curve.

## 4. Solver and determinism

Use `scipy.optimize.least_squares` with:

- method `trf`;
- the frozen bounds above;
- `xtol = 1e-12`;
- `ftol = 1e-12`;
- `gtol = 1e-12`;
- `max_nfev = 100000`;
- numerical Jacobian `2-point`;
- no robust loss and no random initialization.

A separately written scalar objective must directly recompute every reported chi-squared value from retained parameters and rows.

## 5. Metrics

For both the fitted model and baryonic null, record:

- `N`;
- fitted-parameter count;
- chi-squared;
- degrees of freedom;
- reduced chi-squared;
- unweighted RMSE in `km/s`;
- inverse-variance weighted RMSE in `km/s`, defined as `sqrt(sum(w*r^2)/sum(w))`, `w=1/errV^2`;
- standardized RMSE, `sqrt(mean((r/errV)^2))`;
- maximum absolute residual in `km/s`;
- Gaussian fixed-variance AIC up to the common additive constant: `chi2 + 2*k`;
- residuals and fitted values for every radius.

Use degrees of freedom:

- public model: `N - 2`;
- baryonic null: `N`.

## 6. Frozen regional metrics

The following boundaries are frozen before fit inspection:

- inner region: `r <= 5.0 kpc`;
- transition region: `5.0 < r <= 15.0 kpc`;
- outer region: `r > 15.0 kpc`.

For each region, report row count, chi-squared contribution, unweighted RMSE, weighted RMSE, mean residual, and maximum absolute residual.

These boundaries are independent implementation choices based on the publicly fixed `r_s = 5 kpc`; they are not recovered TOLOG conventions.

## 7. Multi-start equivalence, boundaries, and uncertainty

All converged starts count as observationally equivalent only when the maximum absolute difference between each retained fitted curve and the best fitted curve is at most `1e-6 km/s` over all `43` radii.

A parameter is classified as touching a search boundary when its distance from that boundary is at most `1e-6` times the full bound span.

Estimate a local Gauss-Newton covariance from the best standardized-residual Jacobian when `J^T J` is finite and full rank. Record:

- Jacobian singular values;
- numerical rank using NumPy's default matrix-rank tolerance;
- condition number;
- unscaled covariance `(J^T J)^-1`;
- covariance scaled by reduced chi-squared;
- parameter correlation.

If these quantities are unstable or rank-deficient, report that rather than replacing them with a confident uncertainty.

## 8. Frozen interpretation thresholds

Publicly stated comparison target for this lane:

- reduced chi-squared near `1.5`;
- reproduction window: absolute difference at most `0.15`.

Material improvement over the baryonic null is frozen as both:

- `delta_AIC = AIC_null - AIC_model >= 10`;
- model chi-squared at least `20%` below null chi-squared.

Classification:

- `public_metric_reproduced` only if all starts converge to equivalent curves, no parameter touches a boundary, and reduced chi-squared is within `0.15` of `1.5`;
- `functional_benchmark_reproduced_but_public_metric_differs` if the fit is stable and finite, materially improves over the null, but differs from `1.5` by more than `0.15`, with a relevant public convention still ambiguous;
- `not_reproduced_under_declared_conditions` if numerical and provenance gates pass but the model is unstable, does not materially improve, or differs substantially without a plausible missing convention;
- `inconclusive` if multimodality or missing public conventions prevent a fair comparison.

The `94.2%` claim remains outside B2 because no public operational definition has been recovered.

## 9. Required outputs

Retain:

- one research runner under `research/runners/`;
- one machine-readable JSON receipt under `research/results/`;
- one standalone execution report under `research/` containing input hash, complete methods, results, negative findings, machine summary, and portable verification code.

Do not modify production Lineum code, canonical equations, or whitepapers.

## 10. Prohibited claims

B2 cannot establish emergence, a population law, a unique saturator, a Lineum mechanism, a natural attractor, information retention, a black-hole model, or the absence of dark matter. A good one-galaxy fit remains a descriptive two-parameter fit to one public target.
