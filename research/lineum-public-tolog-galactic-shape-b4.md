# Lineum Public-TOLOG Galactic Shape Benchmark — B4 Execution

**Status:** validated B4 core and threshold audit; active preregistered SPARC population extension  
**Version:** 0.4.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** validated equal-flexibility radial-shape ablation on NGC 3198, completed scale-and-threshold audit of early Lineum/RNB visualizations, and preregistered all-175-SPARC population census; no Lineum-native mechanism  
**Frozen B4 classification:** `tanh_shape_preferred`  
**Threshold-audit classification:** `quantized_linear_rendering_supported`; original simulation mechanism remains `provenance_blocked`  
**Population-audit status:** `preregistered_not_executed`  
**Confidence:** high for comparative description of one galaxy and exact reconstruction of the plotted early-Lineum series; no population conclusion before the frozen census is executed

## Plain result

NGC 3198 preferred the exact `tanh` curve over four equally adjustable smooth saturating alternatives. This was not a post-hoc judgment: the functions, source conventions, starts, bounds, metrics, and strong-preference thresholds were committed before the astronomical run.

Under the unsigned fiducial SPARC convention, `tanh` gave chi-squared `28.061822168198` versus `41.952058405048` for the nearest algebraic competitor `x/sqrt(1+x^2)`. The `tanh` objective was `33.110%` lower, its chi-squared ratio was `0.668902`, and delta AIC was `13.890236`. The signed-gas fiducial lane repeated the result: `28.069707094507` versus `41.953038222856`, ratio `0.669074`, delta AIC `13.883331`.

The frozen strong-preference rule passed because `tanh` was best in both fiducial lanes, every alternative had delta AIC above `10`, `tanh` chi-squared was below `0.8` of the next best, and all required numerical checks passed.

Two limits matter. First, the best `tanh` and algebraic velocity curves differ by at most about `1.66 km/s`, never more than an individual row's stated uncertainty. Many small coherent differences create the statistical preference. Second, with historical tabulated stellar `M/L=1`, the algebraic shape is only delta AIC about `1.68` behind `tanh`. The preference is stable to gas-sign handling but depends on the fiducial stellar calibration established in B3.

The later early-Lineum visualization audit did not identify a hidden arithmetic route to this `tanh`. The historical RNB/DejaVu plots are exactly reconstructed by an equal-block quantized linear staircase. Their high raw correlations with Riemann zeros arise from normalized monotone density trends, while the plotted transition edges themselves are exactly equally spaced.

The next frozen extension tests whether the same shape remains compatible across the complete official set of `175` SPARC rotation curves. No population result has yet been inspected.

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

**Implementation:** five explicit normalized two-parameter saturation functions and three structural controls were fitted to four declared baryonic lanes. The later threshold audit generated standard number sequences, reconstructed the plotted staircase, and compared rendered values, transition positions, and gaps separately.

**Reproduced observation:** under both fiducial lanes, `tanh` passes the frozen strong-preference threshold; transition and saturation are required within this family. Separately, the historical 49- and 15-point RNB plots are exactly reproduced by equal-block quantized linear staircases.

**Interpretation:** NGC 3198 prefers `tanh`-like transition curvature over the four tested generic alternatives. The early RNB visualization does not explain that curvature; its displayed threshold positions support a linear quantization/rendering explanation.

**Hypothesis:** Lineum might generate `tanh`, approximate it through a composite/nonlocal process, or reveal that this preference is galaxy-specific. No tested prime, Fibonacci, golden-ratio, or Riemann scale supplies that mechanism here.

**Known physics:** one phenomenological galaxy fit does not identify gravity, dark matter, modified gravity, an oscillator-grid derivation, a vortex, foam, topology, attractor, memory, or a relativistic theory. Number-sequence similarity is not a physical coupling.

## Negative-result mechanism map

The preregistered broad hypothesis “any normalized smooth saturation is sufficient” is unsupported for fiducial NGC 3198. The failure is localized mainly to transition curvature, not provenance, optimization, gas sign, bounds, or reconstruction.

Open explanation classes are:

1. a genuinely `tanh`-like bounded feedback or order-parameter response;
2. a composite or nonlocal Lineum process whose radial projection approximates `tanh`;
3. source geometry or surface density selecting `tanh`-like curvature only in some systems;
4. a one-galaxy/calibration preference that weakens across a diverse panel;
5. an untested equal-flexibility family that matches the transition better.

The cheapest broad discriminator was expanded from a small diverse panel to a deterministic census of every official SPARC rotation curve, preserving the unchanged B4 shape family and source policy. The early arithmetic-threshold route is not promoted because its plotted evidence resolves into equal-spacing quantization and its raw simulation provenance is unavailable.

## Root impact and prohibited conclusions

B4 supports a tightly specified descriptive galactic response and constrains Q2: generic saturation alone is insufficient on this target, while transition and finite saturation remain necessary. Foam loading and a central vortex remain untested. No Lineum code or whitepaper was changed.

B4 does **not** establish TOLOG's private convention, a derivation of `tanh`, physical uniqueness, a Lineum mechanism, a vortex or black-hole cause, the absence of dark matter, modified gravity, or generalization beyond NGC 3198.

The threshold extension does **not** establish a Lineum relationship with Riemann zeros, prime numbers, Fibonacci numbers, the golden ratio, Beatty sequences, or a hidden arithmetic spectrum. It does not prove that the original Lineum simulation itself was linear; it classifies the supplied plotted representation while the named raw CSV and runner remain unrecovered.

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

## Early-Lineum threshold and scale audit

### Owner idea and motivation

The project owner supplied seven early research plots comparing Lineum “DejaVu” points, later named Resonant Return Points (RNBs), with normalized Riemann zeta zeros. The owner proposed that the visible staircase may not be the physical curve: the decision-relevant objects may instead be the left edges or transition locations. The owner also asked for a critical, out-of-the-box comparison with the golden ratio, Fibonacci numbers, primes, prime gaps, Riemann-zero spacing, and scale changes, noting that an apparently linear pattern can be a local view of a nonlinear relation.

This extension does not reopen the previously closed claim that Lineum is resonant with Riemann zeros. The repository's current zeta-resonance record classifies the tested formulations as `CLOSED_NEGATIVE`: the apparent zeta match was a density/look-elsewhere artifact and did not beat random controls. The narrower question was whether early Lineum thresholds or dwell structure contain a reproducible generic scale law that could inform a composite route to `tanh`-like saturation.

### Retrieved provenance

- The visible 49-point plot reports Pearson correlation `0.9842` and Euclidean distance `0.7254` after normalization.
- The historical hypothesis names the run `spec7_true`, code `lineum_no_artefacts.py`, and data file `output_no_artefacts/spec7_true_rnb_vs_zeta.csv`.
- Current `develop` contains the hypothesis text and quarantined UI, but connector search did not locate the named raw CSV or runner. The absence of a current repository file is not evidence about the original local run.
- The quarantined UI explicitly states that Riemann-zero matching was found to be a density artifact that did not survive random controls.
- The supplied images were treated as secondary visual evidence. The plotted values became decision-safe only where an exact formula reproduced both the visible levels and the published metrics.

### Frozen representations and candidates

The preregistered analysis kept drawn values, transition indices, transition levels, dwell lengths, jump heights, and cumulative event count separate. It compared equal spacing, `tanh`, logistic, logarithmic, square-root and power axes, raw and unfolded Riemann zeros, raw and unfolded primes, prime gaps, Fibonacci numbers, `phi^n`, Beatty sequences for `phi` and `phi^2`, and random monotone or shuffled controls. Pearson correlation was secondary; primary emphasis was error, exact spacing, detrending/unfolding, and random controls.

### Exact reconstruction of both historical plots

The 49-point yellow series is exactly reconstructed as:

`y_i = floor(i/7) / 6`, for `i=0,...,48`.

This gives seven repeated values at each level `0, 1/6, 2/6, ..., 1`. Comparing it with endpoint-normalized first 49 Riemann-zero ordinates gives:

- Pearson `0.9842156096489157`;
- Euclidean distance `0.7254094546265594`.

These reproduce the displayed `0.9842` and `0.7254` to the shown precision.

The 15-point plot is independently reconstructed as:

`y_i = floor(i/7) / 2`, for `i=0,...,14`.

It gives seven zeros, seven halves, and one final one. Against the first 15 normalized Riemann zeros it produces Pearson `0.8624831263677383` and Euclidean distance `1.1669392742086542`, reproducing the displayed `0.862` and `1.167`.

A separately written scalar checker that does not import the vector scoring functions reproduced all four values to at least `1e-15` and verified transition indices `[0,7,14,21,28,35,42]`.

### The left edges answer the owner's specific question

When only the left edges are retained, their indices are:

`[0, 7, 14, 21, 28, 35, 42]`.

After endpoint normalization they are exactly:

`[0, 1/6, 2/6, 3/6, 4/6, 5/6, 1]`.

The reached levels are the same sequence. Therefore transition location versus transition level is an exact straight line, every dwell length is `7`, every jump height is `1/6`, transition RMSE from a line is `4.2e-17`, and gap coefficient of variation is exactly `0`.

This does not show that the original simulation dynamics were linear. It shows that the plotted representation contains no recoverable nonlinear threshold spacing.

### Number-family comparisons

#### Full 49 rendered values

| Candidate | RMSE | Raw interpretation |
|---|---:|---|
| log Fibonacci | `0.056929` | nearly linear after logarithm; not unique to Fibonacci |
| unfolded Riemann count | `0.058129` | density trend explicitly removed toward uniform index |
| linear index | `0.058926` | no fitted shape parameter |
| log `phi^n` | `0.058926` | exactly linear because `log(phi^n)=n log(phi)` |
| Beatty `phi^2` | `0.059543` | near-linear floor sequence |
| Beatty `phi` | `0.059966` | near-linear floor sequence |
| unfolded primes via `li(p)` | `0.067558` | counting trend removed |
| raw primes | `0.091116` | worse than linear |
| raw Riemann zeros | `0.103630` | worse than linear and worse than most random monotone controls |
| raw `phi^n` | `0.536571` | strongly incompatible |
| raw Fibonacci | `0.536571` | strongly incompatible |

The slight numerical lead of log Fibonacci over a line is not a Fibonacci signature. Fibonacci numbers approach a constant multiple of `phi^n`, so taking a logarithm converts either—and any ordinary exponential progression—into an approximately linear sequence. Log `phi^n` is exactly identical to the linear baseline. The log-Fibonacci RMSE was beaten by `5.23%` of `200,000` random monotone controls, narrowly missing the preregistered 95% control threshold even before accounting for its mathematical dependence on the linear/exponential family.

Raw Riemann zeros were beaten by `88.465%` of random monotone controls; raw primes were beaten by `76.255%`. Their high Pearson values are therefore generic monotone similarity, not selective matching.

#### Seven transition locations

| Candidate | RMSE from observed left edges |
|---|---:|
| exact linear | approximately `0` |
| Beatty `phi^2` | `0.015749` |
| unfolded Riemann count | `0.018756` |
| unfolded primes | `0.022274` |
| Beatty `phi` | `0.025198` |
| raw Riemann zeros | `0.063485` |
| raw primes | `0.100000` |
| raw `phi^n` | `0.216707` |
| raw Fibonacci | `0.231455` |

Beatty and unfolded sequences are close because they are constructed to have an approximately uniform counting density. They do not beat the exact equal-spacing explanation.

### Smooth-curve trap

Fitting the entire rendered staircase without examining how it was generated can manufacture an apparent sigmoid:

- linear RMSE `0.058926`;
- fitted half-`tanh` RMSE `0.058776`, with `k=0.212694`, which is already near the linear limit;
- fitted power RMSE `0.058510`, with exponent `1.02537`, also nearly linear;
- fitted logistic RMSE `0.048448`;
- exact quantized-linear formula RMSE `0`.

The logistic curve can smooth the stairs visually, but the exact generator is equal-width linear quantization. This is precisely why the transition edges, dwell lengths, and jump heights had to be tested separately.

### Prime gaps versus Riemann-zero gaps

The owner's scale warning was valid, but the two densities move in opposite average directions:

- among the first 49 values used here, mean Riemann-zero gap falls from `3.1114` in the first half to `2.1798` in the second half;
- mean prime gap rises from `3.9583` to `5.4167`.

Asymptotically, the nth prime grows like `n log n`, so average prime gaps grow roughly logarithmically. The density of zeta zeros grows roughly like `log T`, so their average vertical spacing decreases roughly like `2 pi / log T`. Zeta zeros encode oscillatory information about primes through the explicit formulas, but they are not a list of increasingly separated prime decompositions.

### Classification and consequence

For the supplied plotted representation, the frozen classification is:

`quantized_linear_rendering_supported`.

For the unrecovered original simulation mechanism:

`provenance_blocked`.

The result contradicts using these images as evidence that early Lineum had already generated a `tanh`, Fibonacci, golden-ratio, prime, or Riemann curve. It does not contradict the B4 astronomical result, because the NGC 3198 `tanh` preference was obtained independently from SPARC data and frozen shape comparisons.

The arithmetic-threshold route must remain closed unless the original raw `spec7_true` event data and generation code are recovered and reveal information that was lost by the equal-block visualization.

### Retained extension artifacts

- runner: `research/runners/lineum_b4_early_threshold_scale_audit.py`, local verified SHA-256 `7b22024ecb64dc67236a4a0f0f3673b4b428b3227cefff0e441eee58d160c9dd`;
- independent scalar checker: `research/runners/lineum_b4_early_threshold_scale_check.py`, local verified SHA-256 `906bc3a5282ad149a4286ab1aac0e9fb1a3ebf6977efbf29cd11dc73f857d231`;
- machine output: `research/results/lineum_b4_early_threshold_scale_audit.json`, local rerun SHA-256 `ae5e2cedff687a0b675d263f38ba1096b61e24691d96ef2bef1fe84fd8897331` before connector transport.

Environment: Python `3.13.5`, NumPy `2.3.5`, SciPy `1.17.0`, SymPy `1.14.0`, mpmath `1.3.0`, Linux x86-64. A network-disabled local clone attempt failed before checkout; repository reads and writes used the GitHub connector. This limitation did not affect the standalone arithmetic reconstruction, but repository-supported dependency execution was unavailable.

Minimal independent reconstruction:

```python
import math
import mpmath as mp

zeros = [float(mp.im(mp.zetazero(n))) for n in range(1, 50)]
z = [(v-zeros[0])/(zeros[-1]-zeros[0]) for v in zeros]
y = [math.floor(i/7)/6 for i in range(49)]
mean_z, mean_y = sum(z)/49, sum(y)/49
pearson = sum((a-mean_z)*(b-mean_y) for a,b in zip(z,y)) / math.sqrt(
    sum((a-mean_z)**2 for a in z) * sum((b-mean_y)**2 for b in y)
)
distance = math.sqrt(sum((a-b)**2 for a,b in zip(z,y)))
assert abs(pearson - 0.9842156096489157) < 1e-15
assert abs(distance - 0.7254094546265594) < 1e-15
```

## SPARC population shape census — frozen before execution

### Owner question and exact scope

The project owner asked whether `tanh` might in fact be the common answer for all galaxies and then authorized continuation. This extension tests a descriptive population claim only: when every galaxy receives the same two-parameter shape family and the same baryonic conventions, is `tanh` compatible with most informative SPARC rotation curves, or was NGC 3198 exceptional?

This test cannot establish a universal physical law. Every galaxy still receives its own fitted amplitude `V0` and transition parameter `k_eff`. A physical-law claim would additionally require those parameters to be predicted from independently measured galaxy properties and would require held-out prediction.

### Frozen data census

- Input archive: official `Rotmod_LTG.zip`, SHA-256 `0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588`.
- Members: all `175` `_rotmod.dat` files, with no galaxy selected or excluded by model performance.
- Input audit before fitting: every file has eight numeric columns; row counts range from `4` to `115`; all quoted velocity uncertainties are strictly positive.
- Census set: all `175` galaxies, including sparse curves, retained for transparency.
- Primary interpretive set: galaxies with at least `10` measured rows, fixed before fitting. The input audit gives `124` such galaxies.
- Sparse galaxies remain reported but do not decide the population label because two fitted parameters leave too little independent shape information.
- No SPARC quality flag is available inside this archive. The census will therefore report row-count strata and retain this missing quality metadata as a limitation rather than inventing a quality cut.

### Frozen source lanes and shape family

The two primary lanes are unchanged from B4:

- unsigned fiducial: `Vbar^2 = Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2`;
- signed fiducial: `Vbar^2 = sign(Vgas)Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2`.

Every galaxy and every candidate uses:

`Vmodel^2(r) = Vbar^2(r) + V0^2 S(k_eff r / 5 kpc)`.

The five candidates remain exactly:

1. `tanh(x)`;
2. `1-exp(-x)`;
3. `x/(1+x)`;
4. `(2/pi) atan((pi/2)x)`;
5. `x/sqrt(1+x^2)`.

Each has the same two fitted parameters, the same zero value, the same unit initial slope, and the same asymptotic plateau. The baryons-only model is a zero-parameter structural control.

### Frozen optimizer and numerical gates

- Bounds: `V0=[0,400] km/s`, `k_eff=[1e-6,100]`.
- Starts: all `16` products of `V0=[25,75,150,250]` and `k_eff=[0.01,0.1,1,10]`.
- Solver: SciPy `least_squares`, TRF, two-point Jacobian, linear loss, `xtol=ftol=gtol=1e-12`, `max_nfev=100000`.
- Objective: quoted-error chi-squared; AIC is `chi2+4` for every two-parameter candidate and `chi2` for baryons-only.
- All starts, convergence flags, parameter-boundary contacts, objective spread, and maximum fitted-curve disagreement are retained.
- A lane is numerically stable when all starts converge and all fitted curves lie within `1e-5 km/s` of the best curve. Failures remain reported and are not silently discarded.
- Any galaxy/shape/lane that fails this stability gate receives a frozen differential-evolution check with seed `20260804`, followed by bounded Powell refinement. The lower verified objective is retained, and the original multistart failure remains visible.
- NGC 3198 must reproduce the existing B4 objectives within `1e-8`; otherwise the population execution is invalid.

### Frozen per-galaxy labels

Within each source lane:

- `delta_AIC_tanh = AIC_tanh - min(AIC_all_five_shapes)`;
- `tanh_best`: `delta_AIC_tanh <= 1e-8`;
- `tanh_compatible`: `delta_AIC_tanh < 2`;
- `tanh_tension`: `2 <= delta_AIC_tanh < 10`;
- `tanh_strongly_rejected`: `delta_AIC_tanh >= 10`;
- `shape_identified`: the best and second-best shapes differ by at least `2` AIC units;
- `added_component_needed`: the best two-parameter shape improves over baryons-only by at least `10` AIC units;
- `informative`: at least `10` rows, `added_component_needed=true`, and the best fit does not place `V0` or `k_eff` on a frozen parameter boundary.

The primary population percentages are calculated over informative galaxies separately for unsigned and signed gas. Counts over all `175` and over the fixed `N>=10` set are also retained.

### Frozen population classifications

The result is `tanh_population_supported_within_tested_family` only if, in both source lanes:

- at least `80%` of informative galaxies are `tanh_compatible`;
- no more than `10%` are `tanh_strongly_rejected`;
- the median `delta_AIC_tanh` is below `2`;
- and at least `90%` of galaxies informative in both lanes retain the same compatibility label under gas-sign handling.

The result is `tanh_population_unsupported_within_tested_family` if, in either source lane:

- fewer than `50%` of informative galaxies are `tanh_compatible`;
- or more than `30%` are `tanh_strongly_rejected`.

All other outcomes are `mixed_population_evidence`.

These thresholds are descriptive decision rules, not probabilities that `tanh` is true. A supported result would justify mechanism research and held-out parameter prediction; a mixed result would require grouping galaxies by structure before mechanism selection; an unsupported result would falsify the simple universal-shape hypothesis within this five-shape family.

### Frozen independent checks and prohibited interpretations

- A separately written scalar evaluator will reconstruct every retained best curve and objective without importing the main residual function.
- A deterministic audit subset of `20` galaxy names, selected by sorting SHA-256 hashes of the names, will receive independent differential-evolution plus Powell fits for all five shapes in both lanes.
- Aggregate counts will be recomputed from the machine-readable row table by an independent summarizer.
- Results will be stratified by row-count band (`4-9`, `10-19`, `20+`), bulge present/absent, and whether gas-sign handling changes the winning shape. These strata are descriptive and cannot replace the frozen overall classification.

The census does not establish dark-matter absence, modified gravity, TOLOG's mechanism, a Lineum mechanism, a universal law, or causation. It tests only whether `tanh` remains a comparatively adequate two-parameter radial saturation shape across this archive under the declared source conventions.

## Version history

- `0.1.0`: frozen B4 execution and independent reconstruction; `tanh_shape_preferred`; generic saturation unsupported for this one target; owner intuition gate opened.
- `0.2.0`: B4 core retained unchanged; opened and preregistered an in-report early-Lineum threshold/scale audit after the owner supplied historical DejaVu/RNB plots and requested critical comparisons with primes, Fibonacci, the golden ratio, Riemann spacing, and nonlinear scales.
- `0.3.0`: completed the in-report audit; exactly reconstructed both historical plots as equal-block quantized linear staircases; classified the plotted representation as `quantized_linear_rendering_supported`; retained original simulation mechanism as `provenance_blocked`; no arithmetic route to B4 `tanh` established.
- `0.4.0`: preregistered the all-175-SPARC population shape census before fitting; fixed the primary `N>=10` set, source lanes, optimizer, numerical fallbacks, per-galaxy labels, population thresholds, independent checks, and prohibited interpretations.