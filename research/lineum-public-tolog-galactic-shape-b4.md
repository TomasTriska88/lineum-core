# Lineum Public-TOLOG Galactic Shape Benchmark — B4

**Status:** validated within the declared descriptive scope  
**Version:** 0.5.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** public-formula reconstruction, NGC 3198 source-convention audit, equal-flexibility shape ablation, early-Lineum threshold audit, and complete 175-galaxy SPARC population census; no Lineum-native derivation  
**NGC 3198 classification:** `tanh_shape_preferred`  
**Early-threshold classification:** `quantized_linear_rendering_supported`; original raw-run mechanism `provenance_blocked`  
**Population classification:** `mixed_population_evidence`  
**Confidence:** high for the reported numerical comparisons inside the tested SPARC archive and five-shape family; no support for an exact universal `tanh` law or a physical cause

## Plain result

The `tanh` curve is not merely a lucky fit to NGC 3198. Across the informative SPARC population it is the most common winner and is statistically compatible with about four galaxies out of five.

It is not, however, one exact key that opens every galaxy. Fourteen informative galaxies strongly reject `tanh` in favor of another equally adjustable saturation shape. The frozen universal-support gate therefore failed, while the universal-rejection gate also failed. The correct result is mixed population evidence.

The practical picture is:

- one broad bounded-transition family appears useful across many galaxies;
- `tanh` is the leading member of the five tested shapes;
- NGC 3198 is one of the clearest `tanh` cases;
- a meaningful minority requires differently curved transitions;
- the next mechanism must explain both the common `tanh`-like behavior and the systematic exceptions rather than hard-code one exact function for every galaxy.

No private TOLOG document, code, data, or convention was used.

## Questions addressed

1. Can the public TOLOG-like NGC 3198 formula be reconstructed from public information and official SPARC data?
2. Does the public result depend materially on the stellar mass-to-light convention?
3. Is the exact `tanh` transition preferred over equally flexible normalized saturation alternatives on NGC 3198?
4. Did early Lineum DejaVu/RNB plots already contain a hidden `tanh`, Fibonacci, golden-ratio, prime, or Riemann scale?
5. Is the same exact `tanh` shape compatible with most informative galaxies in the complete official SPARC rotation-curve archive?

## Evidence lineage

B0/B1 validated the public formula and official SPARC archive. B2 reconstructed the literal public comparator on NGC 3198 with tabulated stellar `M/L=1`. B3 audited the baryonic source convention and found that standard fiducial SPARC stellar weighting changes the fit dramatically. B4 then froze and executed an equal-flexibility shape ablation before extending the same family to all 175 official SPARC rotation curves.

Earlier Git versions of this same report preserve the preregistrations and chronological capture. Version 0.5.0 consolidates the completed evidence without changing the frozen B2–B4 numerical verdicts.

## Inputs and provenance

Official SPARC rotation-model archive:

- stable source page: `http://astroweb.cwru.edu/SPARC/`;
- archive name: `Rotmod_LTG.zip`;
- archive SHA-256: `0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588`;
- `_rotmod.dat` members: `175`;
- columns used: radius, observed velocity, velocity uncertainty, gas velocity, disk velocity, bulge velocity, surface brightness, and gas surface density;
- row counts: `4` to `115` per galaxy;
- every file passed the eight-numeric-column check;
- every quoted velocity uncertainty was strictly positive.

NGC 3198 member:

- name: `NGC3198_rotmod.dat`;
- rows: `43`;
- SHA-256: `17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953`.

The SPARC table convention already includes helium in the gas contribution. Disk and bulge velocity columns correspond to stellar `M/L=1`; the fiducial analysis rescales their squared contributions by `0.5` and `0.7`, respectively.

## Common model family

For radius `r`, every candidate used:

```text
Vmodel^2(r) = Vbar^2(r) + V0^2 S(k_eff r / 5 kpc)
```

The two primary baryonic lanes were:

```text
unsigned: Vbar^2 = Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2
signed:   Vbar^2 = sign(Vgas) Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2
```

The five equally flexible shapes were frozen as:

```text
tanh:       S(x) = tanh(x)
exponential:S(x) = 1 - exp(-x)
rational:   S(x) = x / (1 + x)
arctan:     S(x) = (2/pi) atan((pi/2) x)
algebraic:  S(x) = x / sqrt(1 + x^2)
```

All satisfy `S(0)=0`, `S'(0)=1`, and `S(infinity)=1`. Every shape has exactly two fitted parameters: amplitude `V0` and transition scale parameter `k_eff`.

Frozen bounds and starts:

```text
V0 in [0, 400] km/s
k_eff in [1e-6, 100]
V0 starts = [25, 75, 150, 250]
k_eff starts = [0.01, 0.1, 1, 10]
16 Cartesian-product starts per fit
```

Primary solver: SciPy `least_squares`, TRF, two-point Jacobian, linear loss, tolerances `1e-12`, `max_nfev=100000`. The objective was quoted-error chi-squared. All two-parameter candidates used `AIC = chi2 + 4`; baryons-only used `AIC = chi2`.

## NGC 3198 source-convention audit

Literal tabulated stellar `M/L=1` gave:

```text
V0 = 161.2955688 km/s
k_eff = 0.09596754
chi2 = 605.6090070
reduced chi2 = 14.7709514
```

The standard fiducial stellar weighting gave:

```text
V0 = 132.3866012 km/s
k_eff = 0.52198556
chi2 = 28.06182217
reduced chi2 = 0.68443469
half-saturation radius = 5.26169863 kpc
```

The fiducial convention reduced chi-squared by about `95.366%` relative to literal `M/L=1`. Gas-sign handling changed the result negligibly. The public claim near reduced chi-squared `1.5` was not uniquely reproduced; the same public formula gives substantially different values under plausible source conventions.

This establishes source-policy sensitivity, not that reduced chi-squared below one is necessarily more physically truthful.

## NGC 3198 equal-flexibility shape result

Unsigned fiducial results:

| Shape | chi-squared | Reduced chi-squared | Delta AIC from best |
|---|---:|---:|---:|
| `tanh` | `28.061822` | `0.684435` | `0` |
| algebraic | `41.952058` | `1.023221` | `13.890236` |
| exponential | `51.135224` | `1.247201` | `23.073402` |
| arctan | `62.226443` | `1.517718` | `34.164620` |
| rational | `101.042285` | `2.464446` | `72.980463` |

The signed-gas lane repeated the same order and essentially the same objectives. The main discrimination occurred at `5 < r <= 15 kpc`, where `tanh` transition chi-squared was `7.992271` versus `17.621597` for the nearest algebraic alternative.

The best `tanh` and algebraic velocity curves differ by at most about `1.66 km/s`; the preference is accumulated from many small coherent residual differences rather than one dramatic point.

At historical stellar `M/L=1`, the algebraic shape was only about `1.68` AIC units behind `tanh`. Exact transition preference therefore depends on the stellar calibration even though the fiducial result is numerically strong.

Structural controls showed that both a transition and finite saturation are needed over the measured range. Constant-plateau and nonsaturating-linear additions were not competitive.

## Early-Lineum threshold and number-sequence audit

The owner supplied early DejaVu/RNB visualizations and proposed that the meaningful objects might be the left edges of the stairs rather than the horizontal stairs themselves. The analysis therefore separated plotted values, transition positions, dwell lengths, and jump heights.

The 49-point yellow series was exactly reconstructed as:

```text
y_i = floor(i / 7) / 6, i = 0,...,48
```

This reproduces the published comparison with normalized Riemann zeros:

```text
Pearson correlation = 0.9842156096489157
Euclidean distance = 0.7254094546265594
```

The historical 15-point plot was independently reconstructed as seven zeros, seven halves, and one final one, reproducing its displayed correlation and distance.

The left-edge indices are exactly:

```text
[0, 7, 14, 21, 28, 35, 42]
```

After normalization, transition positions and reached levels are the same equally spaced sequence. Dwell lengths are all seven, jump heights are all `1/6`, line residual is approximately machine zero, and gap coefficient of variation is zero.

Raw Fibonacci, `phi^n`, primes, prime gaps, and Riemann-zero positions did not beat the exact quantized-linear explanation. Log-Fibonacci appears almost linear because Fibonacci numbers asymptotically scale like `phi^n`; the logarithm removes the exponential and is not a selective Fibonacci signature. Raw Riemann and prime similarities were frequently beaten by random monotone controls.

Classification:

```text
plotted representation: quantized_linear_rendering_supported
original raw simulation mechanism: provenance_blocked
```

The named original event CSV and runner were not recovered. The result therefore classifies the supplied plotted representation, not the unrecovered early simulation dynamics. It does not provide an arithmetic mechanism for the galactic `tanh` preference.

## Population census preregistration

The population test was frozen before fitting:

- all `175` archive galaxies were retained;
- no galaxy was selected or excluded according to fit performance;
- primary row-count set was fixed at at least `10` measured points, giving `124` galaxies;
- a galaxy was `informative` in a lane only when it had at least ten rows, the best added shape improved over baryons-only by at least ten AIC units, and the winning fit did not touch a frozen parameter boundary;
- sparse curves remained reported but did not determine the population label;
- no quality flag absent from the archive was invented;
- the same two baryonic lanes, five shapes, bounds, and sixteen starts were used for every galaxy.

Per-galaxy `tanh` labels:

```text
compatible:        delta AIC tanh < 2
tension:           2 <= delta AIC tanh < 10
strongly rejected: delta AIC tanh >= 10
```

Frozen population support required, in both source lanes:

- at least `80%` compatible;
- no more than `10%` strongly rejected;
- median delta AIC below two;
- at least `90%` gas-sign label agreement.

Frozen population rejection required, in either lane, fewer than `50%` compatible or more than `30%` strongly rejected. Anything between these gates was `mixed_population_evidence`.

## Complete 175-galaxy population result

The two source lanes produced identical population counts and winners among informative galaxies:

```text
official archive galaxies                         175
galaxies with at least 10 rows                    124
informative galaxies                              102
tanh compatible                                    82 / 102 = 80.392%
tanh strongly rejected                             14 / 102 = 13.725%
tanh tension                                        6 / 102 = 5.882%
tanh exact best                                    68 / 102 = 66.667%
median delta AIC tanh                               0.0
same compatibility label under gas-sign handling 102 / 102
same winning shape under gas-sign handling        102 / 102
```

Winner counts among the 102 informative galaxies:

| Shape | Wins |
|---|---:|
| `tanh` | `68` |
| rational | `16` |
| algebraic | `10` |
| arctan | `5` |
| exponential | `3` |

Only `32/102` informative galaxies distinguished the best and second-best shapes by at least two AIC units. Among these shape-identifying galaxies:

```text
tanh wins        18
rational wins     8
arctan wins       3
algebraic wins    2
exponential wins  1
```

Thus many galaxies are compatible with multiple nearby saturation curves. Among the subset that genuinely distinguishes curvature, `tanh` wins most often but not overwhelmingly.

The compatibility fraction narrowly passed the `80%` support requirement. The strong-rejection fraction failed the support gate because `13.725%` exceeds the frozen `10%` ceiling. It remained far below the `30%` universal-rejection gate. Therefore:

```text
mixed_population_evidence
```

## Strongest population discriminators

Six informative galaxies strongly preferred `tanh` over the second-best shape by at least ten AIC units:

| Galaxy | Delta AIC to second best |
|---|---:|
| UGC05253 | `71.0901` |
| NGC5055 | `39.4346` |
| UGC09133 | `22.0938` |
| NGC2903 | `18.5546` |
| NGC5033 | `17.7639` |
| NGC3198 | `13.8902` |

Fourteen informative galaxies strongly rejected `tanh`:

| Galaxy | Preferred shape | Delta AIC against `tanh` |
|---|---|---:|
| UGC06787 | arctan | `121.8213` |
| UGC11914 | rational | `88.1234` |
| NGC6015 | arctan | `72.7057` |
| NGC2403 | algebraic | `54.7531` |
| NGC1003 | rational | `32.8904` |
| UGC03205 | arctan | `31.4479` |
| UGC02953 | algebraic | `30.7209` |
| UGC08699 | rational | `23.5322` |
| NGC0801 | rational | `20.7622` |
| NGC2998 | rational | `16.9678` |
| UGC06786 | exponential | `16.3921` |
| NGC5907 | rational | `13.6927` |
| UGC02885 | rational | `13.2693` |
| UGC00128 | exponential | `11.7727` |

These exceptions are not caused by gas-sign handling: both source lanes retained the same winners and labels for all 102 informative galaxies.

## Descriptive strata

Informative row-count strata:

```text
10–19 rows: 51 galaxies; 44 compatible, 4 strongly rejected, 3 tension
20+ rows:   51 galaxies; 38 compatible, 10 strongly rejected, 3 tension
```

More strongly measured curves expose more exceptions, as expected when additional points constrain transition curvature.

Bulge strata among informative galaxies:

```text
no tabulated bulge: 77 galaxies; 65 compatible, 7 strongly rejected, 5 tension
bulge present:      25 galaxies; 17 compatible, 7 strongly rejected, 1 tension
```

The higher rejection fraction in the bulge-present group is descriptive only. The test did not establish that a bulge causes the shape change; stellar calibration, source geometry, radial coverage, covariance, or another correlated property may explain it.

Twenty-two `N>=10` galaxies were conservatively excluded from the informative set because the best fit touched a parameter boundary. All twenty-two had `tanh` as the nominal winner. Including all `N>=10` curves would therefore slightly improve the apparent `tanh` score, but the preregistered boundary exclusion was retained.

## Numerical verification

Population execution comprised:

```text
175 galaxies × 2 source lanes × 5 shapes = 1,750 fits
1,750 fits × 16 starts = 28,000 primary optimization starts
```

Checks:

- all `28,000/28,000` primary starts reported convergence;
- `1,579/1,750` shape-lane fits passed the strict all-start curve-equivalence gate directly;
- `171` flat or degenerate basins triggered the frozen differential-evolution plus Powell fallback;
- fallback changed the retained objective by at most `8.70e-9`, insufficient to alter any material ranking;
- independent scalar curve reconstruction differed by at most `2.65e-12 km/s`;
- scalar chi-squared reconstruction differed by at most `1.29e-11`;
- the deterministic independent 20-galaxy audit refitted all five shapes in both lanes and differed by at most `3.71e-9` in chi-squared;
- a separate CSV-only summarizer independently recovered `82`, `14`, `68`, all winner counts, and `102/102` cross-lane agreement;
- NGC 3198 reproduced the frozen B4 values exactly to the declared tolerance.

One monolithic execution attempt was terminated by the external command-time limit after 30 galaxies. It produced no retained scientific result. The unchanged deterministic runner was then executed in fixed index batches and merged; batching changed only process scheduling, not data, equations, starts, seeds, objectives, or classification.

Runtime environment:

```text
Python 3.13.5
NumPy 2.3.5
SciPy 1.17.0
Linux x86-64
```

Repository requirements declare NumPy below `2.0`. Independent scalar reconstruction, alternative global optimization, exact NGC reproduction, and CSV-only aggregation reduce but do not erase this environment mismatch. A repository-supported NumPy rerun remains a desirable reproduction check.

## Scientific separation

**Current implementation:** the research runner fits five explicitly declared phenomenological saturation functions to SPARC rotation curves. The current Lineum engine separately contains an explicit `tanh` in an interaction term; any `tanh`-like engine output from that path cannot count as emergence.

**Reproduced observations:** NGC 3198 strongly prefers `tanh` inside the tested family. Across 102 informative galaxies, `tanh` is best for 68 and compatible for 82, while 14 strongly reject it. Both gas-sign conventions give the same population labels and winners.

**Narrow interpretation:** a `tanh`-like bounded transition is a useful and common descriptive pattern, but exact transition curvature varies across the population. NGC 3198 is a favorable `tanh` target, not proof of universality.

**Hypotheses opened by the result:**

1. one underlying feedback family may have a shape parameter controlled by source structure;
2. several emergent mechanisms may occupy different galaxy regimes;
3. projection of one nonlocal mechanism through different baryonic geometries may create different apparent saturation curves;
4. unmodeled stellar calibration, radial covariance, or data-systematic structure may create part of the apparent shape diversity;
5. the five-shape family may omit a more general low-dimensional curve that subsumes the winners.

**Known real physics:** this fit census does not identify dark matter, modified gravity, a Lineum foam, a vortex, an order parameter, an oscillator grid, a relativistic completion, or a causal law. AIC preference among phenomenological curves is not a physical derivation.

## Failure-to-mechanism map

The simple hypothesis “the exact same normalized `tanh` shape describes every informative galaxy” is unsupported within the tested family.

What failed:

- the frozen maximum `10%` strong-rejection allowance was exceeded;
- fourteen informative galaxies preferred another equal-parameter shape by at least ten AIC units;
- among the 32 curves that clearly identified shape, twelve strongly rejected `tanh`.

What remained positive:

- `tanh` is the most common winner;
- it is compatible with slightly more than 80% of informative galaxies;
- its median population penalty is zero;
- it wins six very strong head-to-head cases;
- the result is insensitive to the signed-gas convention.

Failure location:

- not the NGC 3198 implementation;
- not gas-sign handling;
- not ordinary local optimizer selection;
- not a sparse-curve-only artifact;
- localized to population variation in transition curvature, with stronger exceptions among better-sampled and bulge-present curves.

Distinct repair classes:

1. **Shape-family repair:** introduce one bounded transition family with an additional physically predicted curvature parameter, then penalize the extra flexibility and test held-out galaxies.
2. **Source-projection repair:** derive apparent radial response from baryonic surface density, disk scale, bulge structure, or a nonlocal source integral rather than from radius alone.
3. **Regime-mixture repair:** identify preregistered galaxy classes before fitting and test whether each class has a stable winner.
4. **Measurement-model repair:** incorporate published SPARC quality metadata, distance/inclination uncertainties, stellar `M/L` uncertainty, and radial covariance before interpreting shape differences physically.
5. **Emergent-mechanism repair:** test bistable fronts, threshold ensembles, bounded feedback, wake/vortex projections, and other Lineum-native dynamics only after the observational target family is defined without embedding `tanh` directly.

The cheapest next discriminator is not blind tuning of an emergent Lineum mechanism. It is to compare the fourteen strong counterexamples with the six strong `tanh` wins and determine which measured source property predicts the direction of curvature change. That decision is now at the owner intuition gate because the exact-universal-shape hypothesis produced a verified negative result.

## Root-programme impact

| Programme statement | Impact |
|---|---|
| A finite saturating addition is useful for NGC 3198 | `supports` |
| Exact `tanh` transition is preferred on NGC 3198 | `supports` |
| Any smooth saturation is equivalent on NGC 3198 | `contradicts` |
| Exact normalized `tanh` is universal across galaxies | `contradicts` within tested family |
| A broad bounded-transition family may be common | `supports` descriptively |
| Early RNB plots derive the galactic response | `contradicts` for supplied rendering |
| Lineum currently derives `tanh` emergently | `not_yet_supported`; explicit engine `tanh` is a confounder |
| Foam, vortex, memory, or phase-front cause | `not_yet_compared` |
| TOLOG physical mechanism is validated | `contradicts` as an allowed conclusion |

No Lineum engine, public API, test suite, or whitepaper was changed by this research checkpoint.

## Retained artifacts and reproduction

Committed research tools:

- `research/runners/lineum_b4_sparc_population_shape_census.py` — complete all-in-one runner;
- `research/runners/lineum_b4_sparc_population_fit_batch.py` — execution-environment batch helper;
- `research/runners/lineum_b4_sparc_population_finalize.py` — deterministic merge and independent audit;
- `research/runners/lineum_b4_sparc_population_summary_check.py` — independent CSV-only aggregate checker.

Committed outputs:

- `research/results/lineum_b4_sparc_population_shape_census_summary.json` — human-readable population result and diagnostics;
- `research/results/lineum_b4_sparc_population_shape_census.csv.xz.b64` — all 350 galaxy-lane decisions, XZ-compressed then base64 encoded.

Artifact SHA-256 values before connector transport:

```text
main runner      34f2c9e6705ab00aa179f45cee0d0ca04b4da94cbc1858c17cfd4751bcb1b01f
batch helper     da4eb89a6501746460e628d1cc0413606fe131bb9dcbedf0ff440de3d86f2667
finalizer        128a23d1bdf24810fb876b7d6ba3ebba5852d7f5e0a13dee209e20f0e09333c7
summary checker  98a3907d3e5dd61bae45a3c962215ced1bf4d684edd2db53cab81ab0198e1243
summary JSON     4e5e20ff28c3ea1a9cf9612580cfdd62d6604e2fc21c4d6bad32c40f1fa46fdc
raw 350-row CSV  c28423cc6f8b935b8c6b7467966a55fe4bb91cbe5680210897365cf618e10a7d
CSV XZ           7dc6c16b469b92fc28cdfdeb59de357e1731c9fa509d8d968ac489e7fb22ba30
CSV XZ base64    2137bb95499e25f38438feb4376a398eb5d2a79b270fa764aece32e8ae62fe04
```

The complete local compressed receipt, including all 28,000 start records, had SHA-256:

```text
c12b04eaf13b2d66c5f6eee799cde1d5c3978546aea3faa1c053b02ba2bbcf19
```

It was used to derive the committed summary and row table but was too large for a safe single connector write. The durable report does not rely on that local file for its conclusions: the exact runner regenerates it, the committed summary retains all aggregate and numerical gates, and the committed row table retains every galaxy-lane decision. The absence of per-start raw records from Git is an explicit evidence-pack limitation, not hidden completeness.

Minimal execution:

```bash
python research/runners/lineum_b4_sparc_population_shape_census.py \
  --archive Rotmod_LTG.zip \
  --output population_receipt.json \
  --table population_rows.csv \
  --workers 8

python research/runners/lineum_b4_sparc_population_summary_check.py \
  population_rows.csv
```

To decode the committed row table:

```bash
base64 -d research/results/lineum_b4_sparc_population_shape_census.csv.xz.b64 \
  | xz -d > population_rows.csv
```

Expected primary result:

```text
classification = mixed_population_evidence
informative = 102
tanh compatible = 82
tanh strongly rejected = 14
tanh best = 68
same gas-sign label = 102
```

## Prohibited conclusions

This report does not establish:

- that `tanh` is a universal law of galaxies;
- that the public TOLOG mechanism is physically correct;
- that TOLOG's unpublished conventions were reproduced;
- that dark matter is absent;
- that modified gravity is established;
- that Lineum already generates the response emergently;
- that an explicit `tanh` inside current Lineum code is an emergent discovery;
- that Fibonacci numbers, the golden ratio, primes, or Riemann zeros cause the galactic response;
- that bulges cause the observed shape exceptions;
- that a lower chi-squared alone identifies true physics.

## Version history

- `0.1.0`: frozen NGC 3198 B4 execution; `tanh_shape_preferred`.
- `0.2.0`: opened and preregistered the in-report early-Lineum threshold and scale audit.
- `0.3.0`: completed the threshold audit; exact equal-block quantized-linear reconstruction; original raw mechanism remained provenance-blocked.
- `0.4.0`: preregistered the complete 175-galaxy SPARC population census before fitting.
- `0.5.0`: completed and independently checked the census; `mixed_population_evidence`; exact universal `tanh` unsupported while `tanh` remains the leading tested descriptive shape.