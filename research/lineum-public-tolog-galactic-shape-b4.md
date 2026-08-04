# Lineum Public-TOLOG Galactic Shape Benchmark — B4 Execution

**Status:** validated  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** equal-flexibility radial-shape ablation on NGC 3198; no population fit or Lineum-native mechanism  
**Frozen classification:** `tanh_shape_preferred`  
**Confidence:** high for comparative description of this one galaxy under the two fiducial SPARC source lanes; no confidence claim about universality or physical cause

## Plain result

NGC 3198 preferred the exact `tanh` curve over four equally adjustable smooth saturating alternatives. This was not a post-hoc judgment: the functions, source conventions, starts, bounds, metrics, and strong-preference thresholds were committed before the astronomical run.

Under the unsigned fiducial SPARC convention, `tanh` gave chi-squared `28.061822168198` versus `41.952058405048` for the nearest algebraic competitor `x/sqrt(1+x^2)`. The `tanh` objective was `33.110%` lower, its chi-squared ratio was `0.668902`, and delta AIC was `13.890236`. The signed-gas fiducial lane repeated the result: `28.069707094507` versus `41.953038222856`, ratio `0.669074`, delta AIC `13.883331`.

The frozen strong-preference rule passed because `tanh` was best in both fiducial lanes, every alternative had delta AIC above `10`, `tanh` chi-squared was below `0.8` of the next best, and all required numerical checks passed.

Two limits matter. First, the best `tanh` and algebraic velocity curves differ by at most about `1.66 km/s`, never more than an individual row's stated uncertainty. Many small coherent differences create the statistical preference. Second, with historical tabulated stellar `M/L=1`, the algebraic shape is only delta AIC about `1.68` behind `tanh`. The preference is stable to gas-sign handling but depends on the fiducial stellar calibration established in B3.

## Lineage and frozen protocol

B0/B1 validated the official SPARC archive and public `tanh` formula. B2 produced reduced chi-squared about `14.77` under literal `M/L=1`. B3 found reduced chi-squared about `0.684` under the standard SPARC disk `M/L=0.5`. B4 preregistration version `0.2.0` then froze this comparison before results.

Input: official `NGC3198_rotmod.dat`, `43` rows, SHA-256 `17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953`; no exclusions, uncertainty changes, or target-value tuning; fixed `r_s=5 kpc`.

Primary source lanes:

- `literal_fiducial`: `Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2`;
- `signed_fiducial`: `sign(Vgas)Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2`.

Historical controls repeated both gas rules at stellar `M/L=1`. NGC 3198 has zero bulge contribution in all rows.

Every primary model used exactly two parameters:

`Vmodel^2 = Vbar^2 + V0^2 S(k_eff r / 5 kpc)`.

The normalized candidates all satisfy `S(0)=0`, `S'(0)=1`, `S(infinity)=1`:

- `tanh(x)`;
- `1-exp(-x)`;
- `x/(1+x)`;
- `(2/pi) atan((pi/2)x)`;
- `x/sqrt(1+x^2)`.

Bounds were `V0=[0,400] km/s`, `k_eff=[1e-6,100]`; starts were all `16` products of `V0=[25,75,150,250]` and `k_eff=[0.01,0.1,1,10]`; SciPy `least_squares`, TRF, two-point Jacobian, linear loss, all tolerances `1e-12`, `max_nfev=100000`; dof `41`; AIC `chi2+4`.

## Results

| Lane | Shape | chi-squared | reduced chi-squared | delta AIC | `V0` km/s | `k_eff` | half-radius kpc |
|---|---|---:|---:|---:|---:|---:|---:|
| unsigned fiducial | `tanh` | `28.061822` | `0.684435` | `0` | `132.386601` | `0.521986` | `5.261699` |
| unsigned fiducial | algebraic | `41.952058` | `1.023221` | `13.890236` | `135.756799` | `0.525115` | `5.497372` |
| unsigned fiducial | exponential | `51.135224` | `1.247201` | `23.073402` | `133.846974` | `0.667475` | `5.192305` |
| unsigned fiducial | arctan | `62.226443` | `1.517718` | `34.164620` | `142.375801` | `0.510522` | `6.234990` |
| unsigned fiducial | rational | `101.042285` | `2.464446` | `72.980463` | `147.880789` | `0.698421` | `7.159001` |
| signed fiducial | `tanh` | `28.069707` | `0.684627` | `0` | `132.386365` | `0.521999` | `5.261564` |
| signed fiducial | algebraic | `41.953038` | `1.023245` | `13.883331` | `135.756358` | `0.525133` | `5.497186` |
| signed fiducial | exponential | `51.124838` | `1.246947` | `23.055130` | `133.846592` | `0.667498` | `5.192130` |
| signed fiducial | arctan | `62.219914` | `1.517559` | `34.150207` | `142.375033` | `0.510545` | `6.234702` |
| signed fiducial | rational | `101.016494` | `2.463817` | `72.946786` | `147.879600` | `0.698466` | `7.158547` |

The main difference occurs in the transition region (`5<r<=15 kpc`). Unsigned-fiducial transition chi-squared is `7.992271` for `tanh` and `17.621597` for algebraic saturation. Inner contributions are `10.237595` versus `11.490045`; outer contributions are `9.831956` versus `12.840417`.

Structural controls passed both preregistered labels: `transition_needed=true` and `saturation_needed_over_range=true`. The constant-plateau AIC is about `1749.46`, the nonsaturating-linear AIC about `3999.87`, versus best primary AIC `32.06`; neither control is competitive.

## Checks and failures

All `320/320` primary starts converged; no material multimodality occurred. Every fiducial shape passed the `1e-6 km/s` all-start curve-equivalence gate. Both fiducial `tanh` results reproduce B3 within `3.1e-13` chi-squared.

A separately written scalar loop reproduced best objectives within about `2.2e-14` and residual arrays exactly. Bounded Powell reproduced every fiducial objective within `8.6e-14`. Fixed-seed differential evolution reproduced the best and second-best objectives within `1.4e-10`. Dense `41x41` local grids found no lower point. A separate checker using a three-point Jacobian reconstructed all 20 best primary fits, all `1376` curve rows, all `43` wide table rows, and the classification with maximum retained metric and curve differences exactly `0.0`.

Historical `M/L=1` tanh, algebraic, exponential, and arctan lanes narrowly missed the inherited curve-equivalence gate by `1.2e-5` to `2.3e-5 km/s`, without material multimodality. The historical rational lanes touched `V0=400`. These do not enter the fiducial verdict but remain recorded.

Environment was Python `3.13.5`, NumPy `2.3.5`, SciPy `1.17.0`, Linux x86-64. Repository requirements specify NumPy below `2.0`; independent algorithms and exact reconstruction reduce but do not erase this mismatch.

## Scientific separation

**Implementation:** five explicit normalized two-parameter saturation functions and three structural controls were fitted to four declared baryonic lanes.

**Reproduced observation:** under both fiducial lanes, `tanh` passes the frozen strong-preference threshold; transition and saturation are required within this family.

**Interpretation:** NGC 3198 prefers `tanh`-like transition curvature over the four tested generic alternatives. The preference is many small coherent differences, not dramatic curve separation.

**Hypothesis:** Lineum might generate `tanh`, approximate it through a composite/nonlocal process, or reveal that this preference is galaxy-specific.

**Known physics:** one phenomenological galaxy fit does not identify gravity, dark matter, modified gravity, an oscillator-grid derivation, a vortex, foam, topology, attractor, memory, or a relativistic theory.

## Negative-result mechanism map

The preregistered broad hypothesis “any normalized smooth saturation is sufficient” is unsupported for fiducial NGC 3198. The failure is localized mainly to transition curvature, not provenance, optimization, gas sign, bounds, or reconstruction.

Open explanation classes are:

1. a genuinely `tanh`-like bounded feedback or order-parameter response;
2. a composite or nonlocal Lineum process whose radial projection approximates `tanh`;
3. source geometry or surface density selecting `tanh`-like curvature only in some systems;
4. a one-galaxy/calibration preference that weakens across a diverse panel;
5. an untested equal-flexibility family that matches the transition better.

The cheapest broad discriminator is a preregistered small panel of structurally diverse SPARC galaxies using the unchanged B4 family and source policy. The owner intuition gate is opened before selecting a replacement mechanism or launching that lane.

## Root impact and prohibited conclusions

B4 supports a tightly specified descriptive galactic response and constrains Q2: generic saturation alone is insufficient on this target, while transition and finite saturation remain necessary. Foam loading and a central vortex remain untested. No Lineum code or whitepaper was changed.

B4 does **not** establish TOLOG's private convention, a derivation of `tanh`, physical uniqueness, a Lineum mechanism, a vortex or black-hole cause, the absence of dark matter, modified gravity, or generalization beyond NGC 3198.

## Reproduction and retained evidence

Readable loader: `research/runners/lineum_public_tolog_galactic_shape_b4.py`; complete source bundle: `research/runners/lineum_public_tolog_galactic_shape_b4_source.py.xz`. The exact complete evidence bundle contains the uncompressed full JSON receipt, all start receipts and curves, both CSV tables, and the independent checker.

Evidence bundle SHA-256: `e403cb963abe7c3d148df58c3a631a6ab531cd47576952ad9910beda83715bca`. Reconstruct by lexically concatenating `research/results/lineum_public_tolog_galactic_shape_b4_evidence.tar.xz.b64.part*`, base64-decoding the result, then opening the resulting `tar.xz` archive. Raw hashes inside:

- full output JSON: `47502688e3290a055124d6834e46ba73c3e669b5cad494cabc170e77cbf6a9d7`;
- curves CSV: `7d4dacef62c182435ecaec53a7d50afbfd16ad07c424d8a0ca8dd711266fb8f1`;
- rows CSV: `863b4a3fdf8b4d009076ba97f14749612ad1bc3cb6444b8b89539334da42d2e6`.

A compact summary is retained as `research/results/lineum_public_tolog_galactic_shape_b4_output.json`.

Portable input is embedded below as XZ-compressed base64. Decode base64, then XZ-decompress; expected SHA-256 is the input hash above:

```text
/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM4AgaAsFdABGIBQhyEct6omaQnwHw8aY9SM0DP6pLqF8mNdScQSUNG179cP3mj0PWLiYyoXWBE7sMue75gmThR2pvKs7dqQkFirXHboqEPXxbrmy0HGjE5pK1YRrGCO4rAiEjb42+sMR+BT0UqexYYZL6Irf7+ZiXb8fS+BdHyhXYYx1eHOZ4urKT37i/zDTwUYmd5wiyxgsfyuPAxRZn/FrlFKTBJYk548S+/KhCTYZ7HZytJoS/Pyui0XP0ABE/hruX18+6UKdLkXA7uuqcOe0+vK0VAhnoYjH6oS6sz70j7kLQ9LFXDoxIm+NMCBTb+g35nFLEhZBXMSsjn4BzqlfYcTTb90kuHF5S25lmDsCgETEGqwhjWmogQ+Ezchw0zx0rqRW/1YE/FfVMJIE8aJAHn2a7A7lS6PKdqaTQV7so5GXgUhJ0igySPenA73YTlIGRUAug5qXLJ8HCpN6ycMULuxzBvoCjtKFsNFXZZl8Cm2LTxlyxuhCtTOhInPXbn5fxzkZvv09eJOAKUaYM+z6hLYUJ/cqAIYeppLpNP8+fZnrJFHAQV3E/1Epznq+OYM0UniGD95dZAu/5OdKvDtsTHGkrPfpi48aD6+kRMjYb1uPB6eGHUSlbniylZtjpbgP0al7piGKXfibCWRC+G8Q8GMUzpqfs14rygTMIYHSnpf/dIu8KNIhIM+hnEQYWK3miCuwOtMuL+knoaJVoClUiXv7DNOcsOMuviKzd5WH84NhmKCmyUDgUP55k7K0LnWyXknruiC2JWPY4ugXzo0vivBXMut1too4xgnjlOpDkJk+c0KyVEGcpC9i/4HzuRAKtjqetJYZksZXOoHnpN14/tKUUfKvDuQRW3tlbewfnOy5OiwV9c79UhWrzLpAEkevYLqFzpI1EhaWUMsWGRifmuBeXinqLEFmwzhyFHIduuA1x1CcgWAAAAABJ3R1isDTEHgAB3QWbEAAAiZFy07HEZ/sCAAAAAARZWg==
```

Minimal reproduction uses the five functions and solver settings stated above, all 16 starts, and ranks the minimum chi-squared in each fiducial lane. Expected first two values are `tanh 28.061822168198`, algebraic `41.952058405048` unsigned; `tanh 28.069707094507`, algebraic `41.953038222856` signed.

## Version history

- `0.1.0`: frozen B4 execution and independent reconstruction; `tanh_shape_preferred`; generic saturation unsupported for this one target; owner intuition gate opened.
