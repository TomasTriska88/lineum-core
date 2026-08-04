# Lineum Public-TOLOG Galactic `tanh` Benchmark — B2 Execution

**Status:** active  
**Version:** 0.1.1  
**Evidence cutoff:** 2026-08-04  
**Scope:** literal public-formula NGC 3198 fit only; no B3 convention sensitivity, B4 shape ablation, population fit, or Lineum replacement  
**Frozen classification:** `inconclusive`

## 1. Plain-language result

The public `tanh` term helps enormously compared with the literal baryonic curve, especially in the outer galaxy, but this clean-room reproduction does **not** recover the publicly stated reduced chi-squared near `1.5`.

Best frozen fit:

- `V0 = 161.295559723831 km/s`;
- `k_eff = 0.095967558229`;
- reduced chi-squared `14.770951390521`;
- baryonic-null reduced chi-squared `294.076280481349`.

The added term reduces chi-squared by about `95.211%`, but the public numerical target is still missed by a large margin. All `16` starts converged to practically the same shallow basin, yet their maximum curve difference `1.032347748e-05 km/s` exceeds the preregistered `1e-6 km/s` equivalence limit. The frozen result is therefore `inconclusive`, not reproduced.

## 2. Frozen protocol and firewall

B0 and B1 passed and were committed before B2. B2 was separately preregistered before any fit result was inspected.

Input:

- `research/data/NGC3198_rotmod.dat`;
- SHA-256 `17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953`;
- `43` rows, no exclusions.

Literal baryonic convention:

`v_bar = sqrt(v_gas^2 + v_disk^2 + v_bulge^2)`.

Comparator:

`v_model = sqrt(v_bar^2 + V0^2 * tanh(k_eff * r / 5.0 kpc))`.

Frozen numerical protocol:

- bounds `V0 in [0,400] km/s`, `k_eff in [1e-6,100]`;
- starts `V0=[25,75,150,250]`, `k_eff=[0.01,0.1,1,10]`;
- SciPy `least_squares`, method `trf`, two-point Jacobian, linear loss;
- `xtol=ftol=gtol=1e-12`, `max_nfev=100000`;
- objective `sum(((v_model-Vobs)/errV)^2)`;
- reduced chi-squared denominator `N-2`.

The private TOLOG document was not opened or used. No TOLOG code, private data, private parameters, or private conventions entered the run. No production Lineum code, canonical equation, or whitepaper changed.

## 3. Primary metrics

| Metric | `tanh` model | baryonic null |
|---|---:|---:|
| parameters | 2 | 0 |
| chi-squared | `605.609007011365` | `12645.280060698016` |
| degrees of freedom | 41 | 43 |
| reduced chi-squared | `14.770951390521` | `294.076280481349` |
| RMSE (`km/s`) | `12.864633444553` | `37.605922387487` |
| weighted RMSE (`km/s`) | `8.190955212075` | `37.428516551819` |
| standardized RMSE | `3.752856298290` | `17.148652439225` |
| max absolute residual (`km/s`) | `40.130196501455` | `70.981268274856` |
| AIC, common constant omitted | `609.609007011365` | `12645.280060698016` |

Additional results:

- `delta_AIC(null-model) = 12035.671053686650`;
- `chi2_model / chi2_null = 0.047892099195`;
- frozen material-improvement gate passed;
- absolute difference from the public target `1.5` is `13.270951390521`;
- public `±0.15` reproduction window failed;
- no parameter touched a bound;
- transition scale `r_s/k_eff = 52.100940070740 kpc`;
- half-saturation radius `28.619366506438 kpc`.

## 4. Regional diagnostics

Frozen regions were `r<=5 kpc`, `5<r<=15 kpc`, and `r>15 kpc`.

| Region | Rows | Model chi2 | Null chi2 | Model RMSE | Null RMSE | Model mean residual |
|---|---:|---:|---:|---:|---:|---:|
| inner | 15 | `33.291281` | `26.995936` | `19.626893` | `17.548171` | `+14.826810` |
| transition | 13 | `443.089515` | `805.508655` | `7.803557` | `16.190086` | `+3.368773` |
| outer | 15 | `129.228211` | `11812.775470` | `6.036460` | `59.320717` | `-2.451144` |

Most of the improvement comes from repairing the catastrophic outer baryonic deficit. The literal `tanh` model is slightly worse than the baryonic null in inner-region RMSE, and the remaining total chi-squared is dominated by the transition region, where several tabulated uncertainties are very small.

## 5. Multi-start audit

All `16/16` starts returned successful `ftol` termination. Chi-squared varied by less than `1e-10`; fitted `V0` spanned about `1.04e-4 km/s`; fitted `k_eff` spanned about `1.54e-7`.

| Start `V0,k` | Fit `V0,k` | chi-squared |
|---|---|---:|
| `25,0.01` | `161.295531222,0.095967600471` | `605.609007011400` |
| `25,0.1` | `161.295538613,0.095967589205` | `605.609007011387` |
| `25,1` | `161.295548206,0.095967575151` | `605.609007011375` |
| `25,10` | `161.295557854,0.095967560855` | `605.609007011367` |
| `75,0.01` | `161.295551075,0.095967571071` | `605.609007011372` |
| `75,0.1` | `161.295607550,0.095967486316` | `605.609007011395` |
| `75,1` | `161.295620101,0.095967467721` | `605.609007011422` |
| `75,10` | `161.295634776,0.095967446323` | `605.609007011462` |
| `150,0.01` | `161.295552869,0.095967568136` | `605.609007011370` |
| `150,0.1` | `161.295540907,0.095967586136` | `605.609007011384` |
| `150,1` | `161.295588027,0.095967515735` | `605.609007011370` |
| `150,10` | `161.295553292,0.095967567637` | `605.609007011369` |
| `250,0.01` | `161.295559724,0.095967558229` | `605.609007011365` |
| `250,0.1` | `161.295631591,0.095967450822` | `605.609007011453` |
| `250,1` | `161.295602186,0.095967494967` | `605.609007011386` |
| `250,10` | `161.295598527,0.095967499913` | `605.609007011381` |

This is practically one basin. Nevertheless, the maximum retained fitted-curve difference is `1.032347748e-05 km/s`, above the frozen `1e-6 km/s` gate. That threshold cannot be relaxed after seeing the result.

## 6. Identifiability and independent checks

The best standardized-residual Jacobian has rank `2`, singular values `746.234304242` and `0.134712393`, condition number `5539.462915`, and parameter correlation `-0.992455684542`. Scaled local standard errors are about `28.529635 km/s` for `V0` and `0.042007` for `k_eff`. The parameters are formally identifiable locally but very strongly coupled; these Gaussian errors are not robust physical uncertainties.

A separately written scalar loop reproduced chi-squared exactly:

- scalar and vector chi-squared `605.609007011365`;
- absolute chi-squared difference `0.0`;
- maximum residual-array difference `2.842e-14 km/s`.

Additional algorithmic controls reached the same objective:

- bounded Powell: `chi2≈605.609007011362`;
- bounded Nelder-Mead: same basin but hit its iteration cap, retained only as a non-converged trace;
- fixed-seed differential evolution (`20260804`) plus polishing: `chi2≈605.609007011370`.

## 7. Retained artifacts and hashes

- runner: `research/runners/lineum_public_tolog_tanh_b2_fit.py`, SHA-256 `18d0c24ca7bc1b9bdf7e6756df9e3a51b0f50dd8b26d0fac94c0047efe39fbfb`;
- decision receipt: `research/results/lineum_public_tolog_tanh_b2_fit_output.json`, SHA-256 `a06b3460bd8e1f3ddbe62f646c650e87a08b9d92184fc43537b36230739a4d52`;
- all `16 × 43` curves: `research/results/lineum_public_tolog_tanh_b2_fit_curves.csv`, SHA-256 `e0ee478b0ca248b1b58893de3e5accc7d0ce27d14d72ccf89ce8584e2d3eefe0`;
- all `43` row predictions and residuals: `research/results/lineum_public_tolog_tanh_b2_fit_rows.csv`, SHA-256 `2ee20ba343558e0f7453d77036e1af93343513c71e113d069b463434a1be6037`.

The CSV tables reconstructed every original in-memory float exactly. The JSON retains every start's initialization, fitted parameters, objective, termination, evaluation counts, optimality, and classification.

## 8. Why the result remains `inconclusive`

Two preregistered failures prevent a reproduction claim:

1. reduced chi-squared `14.770951` is far outside `1.35–1.65`;
2. the maximum multi-start curve difference exceeds the frozen equivalence threshold.

The second failure is observationally negligible and probably reflects an over-strict numerical threshold on a shallow correlated basin, but it remains binding. The public comparison is also convention-sensitive: signed-gas treatment, stellar mass-to-light scaling, row exclusions, and covariance policy are not fully recovered publicly. B3 must test these explicitly rather than guessing or tuning B2.

## 9. Scientific separation

**Implementation:** a two-parameter explicit saturating addition to the literal baryonic velocity-squared curve.

**Reproduced observation:** strong improvement over the literal baryonic null, reduced chi-squared about `14.77`, practical single-basin convergence, strong parameter correlation, and no reproduction of the public `~1.5` metric.

**Cautious interpretation:** an added amplitude and radial transition are useful for this target; most improvement corrects the outer deficit.

**Hypotheses:** no Lineum foam, `phi`, `mu`, `psi`, topology, central vortex, or emergent dynamics were tested.

**Known-physics boundary:** this one-galaxy phenomenological fit does not identify gravity, dark matter, modified gravity, or a relativistic completion.

## 10. Root-programme impact

| Question | Evidence-limited impact |
|---|---|
| Q1 galactic response | an added amplitude and transition scale help this target; no Lineum response was generated |
| Q2 saturation / attraction | `tanh` supplies saturation by construction; no natural attractor was tested |
| Q3 information retention | unaffected |

## 11. Portable reproduction core

```python
from pathlib import Path
import itertools
import numpy as np
from scipy.optimize import least_squares

rows = [[float(x) for x in line.split()]
        for line in Path("NGC3198_rotmod.dat").read_text().splitlines()
        if line.strip() and not line.startswith("#")]
a = np.asarray(rows)
r, obs, err = a[:,0], a[:,1], a[:,2]
vbar = np.sqrt(a[:,3]**2 + a[:,4]**2 + a[:,5]**2)
def curve(p):
    v0, k = p
    return np.sqrt(vbar**2 + v0**2*np.tanh(k*r/5.0))
def residual(p):
    return (curve(p)-obs)/err
fits=[]
for v0,k in itertools.product([25,75,150,250],[0.01,0.1,1,10]):
    fit=least_squares(residual,[v0,k],bounds=([0,1e-6],[400,100]),
        method="trf",jac="2-point",loss="linear",xtol=1e-12,ftol=1e-12,
        gtol=1e-12,max_nfev=100000)
    fits.append((float(np.sum(residual(fit.x)**2)),fit.x,curve(fit.x)))
fits.sort(key=lambda item:item[0])
chi2,p,best_curve=fits[0]
null_chi2=float(np.sum(((vbar-obs)/err)**2))
assert abs(chi2-605.6090070113653) < 1e-8
assert abs(chi2/41-14.770951390521105) < 1e-10
assert abs(null_chi2-12645.280060698016) < 1e-8
print(p, chi2, chi2/41, null_chi2)
```

## 12. Prohibited conclusions and next gate

B2 does not establish that the public metric is reproduced, that `tanh` is unique, that TOLOG derives the formula, that Lineum generates a galaxy curve or force, that a natural attractor or memory exists, that a central vortex is a black hole, or that dark matter is unnecessary.

The next justified checkpoint is B3 baryonic-convention sensitivity. It must separately test the literal squaring result against authoritative signed-gas and stellar mass-to-light conventions with no silent mixing. B2 must not be tuned retroactively.

## 13. Version history

- `0.1.0`: frozen B2 execution; strong null improvement, public metric not reproduced, strict multi-start equivalence gate failed narrowly, classification `inconclusive`.
- `0.1.1`: scientific result unchanged; retained a compact decision receipt plus complete row and all-start curve tables with reconstruction checks.
