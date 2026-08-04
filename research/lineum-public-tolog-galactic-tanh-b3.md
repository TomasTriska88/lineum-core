# Lineum Public-TOLOG Galactic `tanh` Benchmark — B3 Execution

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** NGC 3198 baryonic-convention sensitivity only; no shape ablation, population fit, or Lineum replacement  
**Frozen classification:** `inconclusive`  
**Substantive result:** standard SPARC stellar scaling changes the fit by orders of magnitude; gas-sign handling is negligible for this target

## 1. Plain-language result

The missing public detail is not a small technicality. The assumed weight of the stars almost completely controls the reported fit quality.

With the literal public squaring convention and the tabulated stellar contribution at `M/L=1`, the B2 result is reproduced: reduced chi-squared is `14.770951390521`. Keeping the same data, same `tanh`, same two fitted parameters, same starts, same bounds, and same uncertainties, but applying the standard SPARC disk scaling `M/L=0.5`, reduced chi-squared falls to `0.684434687029`.

That is a `95.366%` chi-squared reduction relative to the literal `M/L=1` lane. It is not merely close to the publicly stated value near `1.5`; it is substantially lower. Preserving the sign of the six negative gas entries changes chi-squared by less than `0.001%` and does not explain the public number.

Therefore:

- the public formula is highly sensitive to an incompletely declared baryonic convention;
- a conventional SPARC stellar scaling makes the same two-parameter comparator fit NGC 3198 extremely well;
- the exact public metric near `1.5` is still not reproduced;
- the public result cannot be treated as a unique or fully specified benchmark without the missing stellar, row, uncertainty, and fitting conventions.

The formal B3 class remains `inconclusive` because one preregistered floating-point identity gate missed its `1e-12` threshold by `3.27e-13`. High-precision decimal arithmetic verifies that the underlying signed-gas identity is exact, but the threshold is not relaxed after observing the result.

## 2. Lineage and frozen protocol

Root programme: `Lineum Public-TOLOG Galactic tanh Benchmark`, version `0.1.0`, evidence cutoff `2026-08-04`.

Predecessors:

1. B0/B1 version `0.2.0`: official archive provenance and analytic gates passed.
2. B2 version `0.1.1`: literal `M/L=1` fit produced reduced chi-squared `14.770951390521` and was classified `inconclusive` under the strict all-start curve-equivalence gate.
3. B3 preregistration version `0.1.1`: froze four source conventions before fitting. A pre-fit audit corrected the negative-gas row count from four to six before any B3 fit result was inspected.

Frozen input and procedure:

- `43` NGC 3198 rows, SHA-256 `17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953`;
- no exclusions or uncertainty inflation;
- fixed `r_s=5.0 kpc`;
- fitted `V0` and `k_eff` only;
- `V0 in [0,400] km/s`, `k_eff in [1e-6,100]`;
- starts `V0=[25,75,150,250]`, `k_eff=[0.01,0.1,1,10]`;
- bounded `scipy.optimize.least_squares`, `trf`, two-point Jacobian, linear loss;
- `xtol=ftol=gtol=1e-12`, `max_nfev=100000`;
- reduced chi-squared denominator `43-2=41`;
- all-start fitted-curve equivalence tolerance `1e-6 km/s`.

No private TOLOG document, TOLOG code, post-hoc row exclusion, uncertainty inflation, parameter-bound tuning, production Lineum code, or whitepaper change entered B3.

## 3. Authoritative source accounting

The official SPARC mass-model table states that `Vgas` already includes the `1.33` helium correction and that `Vdisk` and `Vbul` are tabulated for stellar `M/L=1` at 3.6 micrometres. The SPARC master paper discusses a fiducial disk value near `M/L=0.5`, and later SPARC radial-acceleration work uses approximately `0.5` for disks and `0.7` for bulges. NGC 3198 has `Vbul=0` in all retained rows, so the bulge coefficient is numerically irrelevant here.

Sources:

- Lelli, F., McGaugh, S. S., and Schombert, J. M. (2016), *SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves*, AJ 152, 157, DOI `10.3847/0004-6256/152/6/157`, arXiv `1606.09251`.
- Official table and column notes: `https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt`.
- Lelli, F., McGaugh, S. S., Schombert, J. M., and Pawlowski, M. S. (2017), *One Law to Rule Them All: The Radial Acceleration Relation of Galaxies*, ApJ 836, 152, DOI `10.3847/1538-4357/836/2/152`, arXiv `1610.08981`.

The signed-gas formula tested here is the preregistered Lineum audit convention. It is not claimed to be a recovered private TOLOG choice.

## 4. Four-lane result

| Lane | `V0` (`km/s`) | `k_eff` | chi-squared | reduced chi-squared | max all-start curve difference | strict curve gate | parameter correlation |
|---|---:|---:|---:|---:|---:|---|---:|
| `literal_m1` | `161.295568792866` | `0.095967544869` | `605.609007011362` | `14.770951390521` | `7.787e-06` | fail | `-0.992455689` |
| `signed_m1` | `161.293023949919` | `0.095971647329` | `605.607295440724` | `14.770909644896` | `8.866e-06` | fail | `-0.992454478` |
| `literal_fiducial` | `132.386601239213` | `0.521985562971` | `28.061822168198` | `0.684434687029` | `7.599e-08` | pass | `-0.689896240` |
| `signed_fiducial` | `132.386364841794` | `0.521998925203` | `28.069707094507` | `0.684627002305` | `9.589e-08` | pass | `-0.689894226` |

All `64/64` least-squares starts converged. Both fiducial-stellar lanes passed the strict fitted-curve agreement gate. Both `M/L=1` lanes narrowly failed the inherited gate, reproducing the shallow parameter coupling already seen in B2.

The best numerical lane is `literal_fiducial`, with transition scale `9.578808983799 kpc`, half-saturation radius `5.261698630203 kpc`, no boundary contact, and substantially weaker parameter coupling than B2. The signed fiducial lane is observationally almost identical.

## 5. What caused the change

| Change | delta chi-squared | fractional chi-squared change |
|---|---:|---:|
| preserve gas sign at `M/L=1` | `-0.001711570639` | `-0.000282620%` |
| preserve gas sign at fiducial stellar scaling | `+0.007884926309` | `+0.028098412%` |
| change stellar scaling to `0.5/0.7` with unsigned gas | `-577.547184843164` | `-95.366347%` |
| change stellar scaling to `0.5/0.7` with signed gas | `-577.537588346216` | `-95.365032%` |

The gas-sign effect is effectively zero for NGC 3198. Stellar scaling is the dominant cause by more than five orders of magnitude in chi-squared effect size.

## 6. Regional diagnostics

| Lane | Region | rows | chi-squared contribution | RMSE (`km/s`) | mean residual (`km/s`) |
|---|---|---:|---:|---:|---:|
| `literal_m1` | inner | 15 | `33.291280702` | `19.626892693` | `+14.826809850` |
| `literal_m1` | transition | 13 | `443.089499044` | `7.803557361` | `+3.368773039` |
| `literal_m1` | outer | 15 | `129.228227265` | `6.036460310` | `-2.451143966` |
| `literal_fiducial` | inner | 15 | `10.237595056` | `12.155296022` | `+7.816383534` |
| `literal_fiducial` | transition | 13 | `7.992270677` | `1.492663953` | `-0.819538411` |
| `literal_fiducial` | outer | 15 | `9.831956435` | `1.694262774` | `+0.120486159` |

Under `M/L=0.5`, the transition-region chi-squared falls from about `443.09` to `7.99`, and the outer contribution falls from about `129.23` to `9.83`. A reduced chi-squared below `1` can arise from conservative uncertainties, correlated data, convention choices, or model flexibility; it is not evidence by itself that the model is physically correct.

## 7. Independent and adversarial checks

- Exact B2 reproduction: B3 `literal_m1` differed from retained B2 chi-squared by `3.183e-12`.
- A separately written scalar loop reproduced every best-lane chi-squared and residual array.
- Bounded Powell found chi-squared `28.061822168197772`, differing from the reference by `4.974e-14`.
- Fixed-seed differential evolution (`20260804`) plus polishing found chi-squared `28.061822168282390`, differing by `8.457e-11`.
- A separate `scipy.optimize.curve_fit` audit reached the same parameter basin and chi-squared.
- All three rows with `Vgas=0` were exactly identical under signed and unsigned gas.
- For six negative rows, binary `float64` evaluation of `(Vgas^2)-(-Vgas^2)=2*Vgas^2` had maximum error `1.3271606036369121e-12`, narrowly above the frozen `1e-12` tolerance. A separate 50-digit decimal calculation using original decimal table strings produced exactly zero error.

The binary threshold remains binding for formal classification even though the underlying identity and primary result are independently verified.

## 8. Scientific separation

**Implementation:** four explicit baryonic-accounting variants feeding the same two-parameter `tanh` comparator.

**Reproduced observation:** the fiducial stellar scaling changes reduced chi-squared from about `14.77` to about `0.684`; gas-sign handling is negligible; all starts and independent optimizers agree.

**Cautious interpretation:** fit quality is dominated by source calibration, so the public `~1.5` value is not a convention-independent benchmark.

**Hypotheses:** no Lineum foam, field, vortex, topology, attractor, or memory mechanism was tested.

**Known-physics boundary:** this is a phenomenological one-galaxy fit and does not identify gravity, dark matter, modified gravity, or a relativistic completion.

## 9. Failure-to-mechanism record

What failed: neither authoritative source convention reproduced the public target near `1.5`; `M/L=1` gave `14.77`, while fiducial `M/L=0.5` gave `0.684`.

What remained positive: provenance, formula implementation, deterministic fitting, scalar recomputation, all-start convergence, and independent optimizers passed. The explicit comparator can fit NGC 3198 extremely well under conventional SPARC stellar scaling.

Failure location: source calibration and incomplete public reporting, not archive provenance, formula transcription, optimizer convergence, or gas-sign handling.

Distinct next discriminator classes are: a preregistered one-dimensional stellar `M/L` profile; a statistical-policy audit of exclusions, uncertainty floors and covariance; a data-version audit; or equal-flexibility shape ablations. No repair is selected inside B3, and blind tuning to `1.5` is prohibited.

## 10. Consequence for Lineum

TOLOG remains useful, but in a narrower role:

- it supplies a simple two-dial saturating comparator;
- it demonstrates that an amplitude and transition scale can describe the target curve;
- it does not supply a fully specified, convention-independent numerical benchmark;
- its reported fit quality is dominated by how visible stellar matter is weighted.

Lineum should not be tuned to reproduce `1.5`. A stronger future target is to predict galaxy curves from declared source observables with no fitted per-galaxy amplitude or transition dial, and to remain stable across source conventions and held-out galaxies.

## 11. Root-programme impact

| Programme item | B3 impact |
|---|---|
| Q1 galactic response | `supports`: a source-sensitive amplitude and radial transition can fit this target; no Lineum response was generated |
| Q2 saturation / attraction | `constrains`: excellent fit quality does not distinguish `tanh` from generic saturation or prove attraction |
| Q3 information retention | `unaffected` |
| foam-like source loading | `reopens`: stellar source calibration must be explicit before any foam mapping |
| central vortex | `not_yet_compared` |
| public TOLOG metric | `contradicts`: neither literal nor fiducial authoritative convention reproduces `~1.5` |
| B4 shape ablation | `depends_on`: use explicitly separated source conventions rather than silently inheriting one |

## 12. Retained artifacts and hashes

- runner: `research/runners/lineum_public_tolog_tanh_b3_baryonic_sensitivity.py`, SHA-256 `417382b84b5918e4891cb6e52d1a8b36c4930661f6e7104a0218b8cafd68972f`;
- compressed machine receipt: `research/results/lineum_public_tolog_tanh_b3_baryonic_sensitivity_output.json`, SHA-256 `70f0aef8539f3e974c93e6134c3f9516f2ee7287d941895fa37be984da583808`;
- all-start fitted curves, shape `4 × 16 × 43`: `research/results/lineum_public_tolog_tanh_b3_baryonic_sensitivity_curves.json`, SHA-256 `b32714f71a6df84ed38eb09ea4543ae548eec1e1c72115b397fd7d0a4a1cc92c`;
- row table: `research/results/lineum_public_tolog_tanh_b3_baryonic_sensitivity_rows.csv`, SHA-256 `6ebac0f547c0507f53949f6b2adfedc05a5367502f57c3c183232bc630508f40`.

Environment: Python `3.13.5`, NumPy `2.3.5`, SciPy `1.17.0`, Linux x86-64. Repository requirements declare NumPy `<2.0.0`, while the runtime supplied NumPy `2.3.5`. Independent scalar, Powell, differential-evolution, `curve_fit`, and reconstruction checks reduce but do not erase that mismatch.

## 13. Portable reproduction core

```python
from pathlib import Path
import itertools
import numpy as np
from scipy.optimize import least_squares

rows = [[float(x) for x in line.split()]
        for line in Path("NGC3198_rotmod.dat").read_text().splitlines()
        if line.strip() and not line.startswith("#")]
a = np.asarray(rows, float)
r, obs, err = a[:,0], a[:,1], a[:,2]
lanes = {
    "literal_m1": (False, 1.0, 1.0),
    "signed_m1": (True, 1.0, 1.0),
    "literal_fiducial": (False, 0.5, 0.7),
    "signed_fiducial": (True, 0.5, 0.7),
}
for name, (signed, disk_ml, bulge_ml) in lanes.items():
    gas = np.sign(a[:,3])*a[:,3]**2 if signed else a[:,3]**2
    vbar2 = gas + disk_ml*a[:,4]**2 + bulge_ml*a[:,5]**2
    def residual(p):
        v0, k = p
        model = np.sqrt(vbar2 + v0*v0*np.tanh(k*r/5.0))
        return (model-obs)/err
    fits=[]
    for v0,k in itertools.product([25,75,150,250],[0.01,0.1,1,10]):
        fit=least_squares(residual,[v0,k],bounds=([0,1e-6],[400,100]),
            method="trf",jac="2-point",loss="linear",xtol=1e-12,
            ftol=1e-12,gtol=1e-12,max_nfev=100000)
        fits.append((float(np.sum(residual(fit.x)**2)),fit.x))
    chi2,p=min(fits,key=lambda x:x[0])
    print(name,p,chi2,chi2/41)
```

Expected reduced chi-squared values, allowing normal last-digit library variation:

```text
literal_m1        14.770951390521
signed_m1         14.770909644896
literal_fiducial   0.684434687029
signed_fiducial    0.684627002305
```

The exact 43-row input is retained in `research/data/NGC3198_rotmod.dat` and all row-level predictions and residuals are retained in the B3 CSV.

## 14. Prohibited conclusions

B3 does not establish the private or unpublished TOLOG convention, reproduce the public `~1.5` metric, select `tanh` over equal-flexibility alternatives, derive a force law, demonstrate Lineum emergence, validate a central vortex, eliminate dark matter, or establish a population law.

## 15. Version history

- `0.1.0`: four-lane frozen B3 execution; dominant stellar-scaling sensitivity retained; formal class `inconclusive` due one narrowly failed binary identity tolerance; public metric remains unreproduced.
