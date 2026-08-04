# Lineum Public-TOLOG Galactic Shape Benchmark — B4

**Status:** validated within the declared descriptive scope  
**Version:** 0.7.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** public-formula reconstruction, NGC 3198 source-convention audit, equal-flexibility shape ablation, early-Lineum threshold audit, complete 175-galaxy SPARC population census, and a preregistered source-structure discriminator on the strongest shape-identifying galaxies; no Lineum-native galactic derivation  
**NGC 3198 classification:** `tanh_shape_preferred`  
**Early-threshold classification:** `quantized_linear_rendering_supported`; original raw-run mechanism `provenance_blocked`  
**Population classification:** `mixed_population_evidence`  
**Source-structure classification:** `simple_source_separator_supported` within the selected extreme contrast  
**Confidence:** high for the reported numerical comparisons inside the tested SPARC archive and five-shape family; moderate for the source-structure association; no causal mechanism or exact universal law established

## Plain result

The public TOLOG-like `tanh` addition is not merely a lucky fit to NGC 3198. Across the informative SPARC population it is the most frequent winner and remains compatible with about four galaxies out of five.

It is not one exact key for every galaxy. Fourteen informative galaxies strongly prefer another equally adjustable saturating curve. The correct population verdict is therefore mixed evidence: a common bounded-transition family is supported, while one immutable normalized `tanh` is not.

A new preregistered comparison now supplies a concrete clue about the exceptions. Among the six strongest `tanh` wins and fourteen strongest rejections, the strongest `tanh` galaxies usually have a more centrally concentrated luminous disk relative to the measured radial extent. The median disk half-light proxy lies at about `9.78%` of the measured outer radius in the strong-`tanh` group and `16.59%` in the rejection group.

In everyday terms, `tanh` works most cleanly when the visible disk is packed into a relatively small central part of the region over which rotation is measured. More radially extended disks more often require a slower or differently curved saturation profile.

This association supports the project owner's working idea that one common mechanism may change regime when a contribution becomes weak, strong, or effectively absent. It does not yet identify that contribution, prove causation, validate a 3×3 grid mechanism, derive TOLOG, or show that Lineum generates the response emergently.

No private TOLOG document, code, data, or convention was used.

## Questions addressed

1. Can the public TOLOG-like NGC 3198 formula be reconstructed from public information and official SPARC data?
2. Does its result depend materially on the stellar mass-to-light convention?
3. Is exact `tanh` transition curvature preferred over equally flexible normalized saturation alternatives on NGC 3198?
4. Did early Lineum DejaVu/RNB plots contain a hidden `tanh`, Fibonacci, golden-ratio, prime, or Riemann scale?
5. Is exact `tanh` compatible with most informative galaxies in all 175 official SPARC rotation curves?
6. Do measured radial source properties distinguish the strongest `tanh` cases from the strongest rejections?
7. Does the evidence favor a source-geometry-dependent regime of one broad mechanism over a simple bulge, gas, data-count, or grid-resolution explanation?

## Evidence lineage

B0/B1 validated the public formula and official SPARC archive. B2 reconstructed the literal public comparator on NGC 3198 with tabulated stellar `M/L=1`. B3 audited the baryonic source convention. B4 froze and executed an equal-flexibility shape comparison on NGC 3198, audited the early Lineum stair plots, extended the same five-shape family to all 175 rotation curves, and then preregistered a source-only discriminator before inspecting the selected radial features.

Earlier Git versions preserve every preregistration and correction chronologically. Version `0.7.0` retains all earlier numerical verdicts and completes the corrected source-structure discriminator.

## Inputs and provenance

Official SPARC rotation-model archive:

- stable source page: `http://astroweb.cwru.edu/SPARC/`;
- archive: `Rotmod_LTG.zip`;
- archive SHA-256: `0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588`;
- galaxies: `175`;
- columns: radius, observed velocity, velocity uncertainty, gas velocity contribution, disk velocity contribution, bulge velocity contribution, disk surface brightness, bulge surface brightness;
- rows per galaxy: `4` to `115`;
- every file passed the eight-numeric-column check;
- every quoted velocity uncertainty was positive.

Version `0.6.0` incorrectly named the eighth column as gas surface density. Direct header inspection established that columns seven and eight are `SBdisk` and `SBbul`, both in luminosity per square parsec. This was corrected in version `0.6.1` before the source-structure calculation. Earlier B2–B4 fits are unaffected because they used columns one through six.

NGC 3198:

- rows: `43`;
- file SHA-256: `17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953`.

SPARC already includes helium in the gas contribution. Disk and bulge velocity columns correspond to stellar `M/L=1`. The fiducial lanes weight their squared contributions by `0.5` and `0.7`, respectively.

## Common descriptive model family

Every tested candidate used the same two fitted quantities: a finite amplitude and a radial transition scale. The added squared-velocity contribution was

```text
Vmodel^2(r) = Vbar^2(r) + V0^2 S(k_eff r / 5 kpc)
```

with primary baryonic lanes

```text
unsigned: Vbar^2 = Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2
signed:   Vbar^2 = sign(Vgas) Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2
```

The frozen shapes were

```text
tanh:        tanh(x)
exponential: 1 - exp(-x)
rational:    x / (1 + x)
arctan:      (2/pi) atan((pi/2) x)
algebraic:   x / sqrt(1 + x^2)
```

All begin at zero, have the same initial slope, and saturate at one. Consequently the test compares transition curvature rather than giving one function an extra amplitude, slope, or plateau.

Bounds and starts:

```text
V0 in [0, 400] km/s
k_eff in [1e-6, 100]
V0 starts = [25, 75, 150, 250]
k_eff starts = [0.01, 0.1, 1, 10]
16 starts per fit
```

The objective was quoted-error chi-squared. Every two-parameter candidate used `AIC = chi2 + 4`; baryons-only used `AIC = chi2`.

## NGC 3198 source-convention result

Literal tabulated stellar `M/L=1` gave

```text
V0 = 161.2955688 km/s
k_eff = 0.09596754
chi2 = 605.6090070
reduced chi2 = 14.7709514
```

Standard fiducial stellar weighting gave

```text
V0 = 132.3866012 km/s
k_eff = 0.52198556
chi2 = 28.06182217
reduced chi2 = 0.68443469
half-saturation radius = 5.26169863 kpc
```

The numerical fit changes dramatically under plausible stellar calibration. This establishes source-policy sensitivity, not that the lower number is automatically more physically truthful. The publicly quoted value near reduced chi-squared `1.5` was not uniquely reproduced from the under-specified public convention.

## NGC 3198 equal-flexibility result

| Shape | Chi-squared | Reduced chi-squared | Delta AIC |
|---|---:|---:|---:|
| `tanh` | `28.061822` | `0.684435` | `0` |
| algebraic | `41.952058` | `1.023221` | `13.890236` |
| exponential | `51.135224` | `1.247201` | `23.073402` |
| arctan | `62.226443` | `1.517718` | `34.164620` |
| rational | `101.042285` | `2.464446` | `72.980463` |

Inside this frozen family, `tanh` reduced chi-squared by about `33.1%` relative to the nearest algebraic competitor. Most discrimination accumulated between `5` and `15 kpc`. The best velocity curves differed by at most about `1.66 km/s`, so the evidence comes from many small coherent residuals rather than one dramatic point.

At historical `M/L=1`, the algebraic curve was only about `1.68` AIC units behind. Exact curvature preference therefore depends on stellar calibration.

## Early Lineum threshold audit

The supplied 49-point yellow staircase was exactly reconstructed as

```text
y_i = floor(i / 7) / 6, i = 0,...,48
```

This reproduces the displayed comparison with normalized Riemann zeros:

```text
Pearson correlation = 0.9842156096489157
Euclidean distance = 0.7254094546265594
```

Its transition positions are exactly

```text
[0, 7, 14, 21, 28, 35, 42]
```

The dwell lengths are all seven and the jump heights are all `1/6`. After normalization, transition positions and levels form an equally spaced linear sequence. Fibonacci numbers, powers of the golden ratio, primes, prime gaps, and Riemann-zero positions did not outperform the exact quantized-linear account. Random monotone controls frequently matched or beat the apparent arithmetic correlations.

Classification:

```text
plotted representation: quantized_linear_rendering_supported
original raw simulation mechanism: provenance_blocked
```

The original event CSV and runner were not recovered. The audit therefore classifies the supplied rendering, not the unrecovered early dynamics.

## Complete 175-galaxy population census

The test retained all archive galaxies and applied the same source lanes, five shapes, bounds, and sixteen starts. No galaxy was selected according to fit performance. The primary informative gate required at least ten rows, a best added shape improving over baryons-only by at least ten AIC units, and no winning fit on a frozen parameter boundary.

Results in both gas-sign lanes were identical among informative galaxies:

```text
official galaxies                                  175
at least 10 rows                                   124
informative                                        102
tanh compatible                         82 / 102 = 80.392%
tanh tension                             6 / 102 =  5.882%
tanh strongly rejected                  14 / 102 = 13.725%
tanh exact best                         68 / 102 = 66.667%
same label under gas-sign handling     102 / 102
same winner under gas-sign handling    102 / 102
```

Winner counts:

| Shape | Wins |
|---|---:|
| `tanh` | `68` |
| rational | `16` |
| algebraic | `10` |
| arctan | `5` |
| exponential | `3` |

Only `32/102` informative galaxies distinguished the best and second-best curves by at least two AIC units. Among those shape-identifying cases, `tanh` won `18`, rational `8`, arctan `3`, algebraic `2`, and exponential `1`.

The frozen support gate required at least `80%` compatibility and at most `10%` strong rejection. Compatibility narrowly passed, but strong rejection reached `13.725%`. The rejection gate also failed because the rejection fraction remained far below `30%`. Therefore:

```text
mixed_population_evidence
```

The broad bounded-transition picture survives. Exact universal `tanh` does not.

## Strongest shape-identifying contrast

Strong `tanh` wins:

```text
UGC05253, NGC5055, UGC09133, NGC2903, NGC5033, NGC3198
```

Strong rejections:

```text
UGC06787, UGC11914, NGC6015, NGC2403, NGC1003, UGC03205,
UGC02953, UGC08699, NGC0801, NGC2998, UGC06786, NGC5907,
UGC02885, UGC00128
```

The higher rejection rate previously observed in bulge-present galaxies was descriptive only. The dedicated source test below shows that the simple inner bulge fraction itself does not separate the two extreme groups.

## Source-structure discriminator

### Owner hypothesis and frozen alternatives

After the exact-universal-`tanh` failure, the project owner proposed that one mechanism may still operate in all galaxies while a term becomes absent, negligible, or dominant in specific regimes.

Two explanations remained open before execution:

1. one broad mechanism changes apparent curvature with measured source structure;
2. multiple mechanisms, stellar calibration, or measurement effects produce the classes.

The discriminator used only source properties. It did not feed the fitted winner, `delta AIC`, or the missing-response profile back into the features.

### Frozen features

Twelve source features were declared before inspection:

1. combined stellar half-light proxy radius divided by measured maximum radius;
2. combined stellar 80-percent-light proxy radius divided by measured maximum radius;
3. disk half-light radius divided by measured maximum radius;
4. disk 80-percent-light radius divided by measured maximum radius;
5. combined stellar light fraction inside the inner radial quarter;
6. disk light fraction inside the inner radial quarter;
7. radius of maximum disk velocity contribution;
8. radius of maximum absolute gas velocity contribution;
9. median inner bulge fraction of baryonic squared velocity;
10. median inner disk fraction;
11. median outer gas fraction;
12. inner-to-outer median baryonic velocity ratio.

Cumulative light proxies integrated `2 pi r Sigma(r)` over measured samples by the trapezoidal rule. The combined stellar proxy was `0.5 SBdisk + 0.7 SBbul`. No gas surface-density profile was invented.

Measurement controls were row count, maximum radius, median fractional velocity uncertainty, and radial-step irregularity.

For every feature, all `20 choose 6 = 38,760` group assignments were enumerated. A strong separator required direction-agnostic AUC at least `0.80` and Holm-adjusted probability at most `0.05` across all twelve source features.

### Result

Exactly one feature passed the full frozen gate:

```text
disk half-light proxy radius / maximum measured radius
```

Exact statistics:

```text
direction-agnostic AUC = 0.9047619048
raw exact p            = 0.0033023736
Holm-adjusted p        = 0.0396284830
pairwise order         = 76 / 84 cross-group pairs
```

The direction was smaller disk half-light radius in the strong-`tanh` group.

Group summaries:

| Group | Median | Mean | Range |
|---|---:|---:|---:|
| six strong `tanh` wins | `0.09779` | `0.10559` | `0.07869–0.15034` |
| fourteen strong rejections | `0.16589` | `0.17490` | `0.09710–0.38280` |

Thus the typical strong-`tanh` disk reached half of its measured disk light within roughly `9.8%` of the measured outer radius, versus roughly `16.6%` for the strong-rejection group. The group distributions overlap; this is a strong rank association, not a perfect threshold.

Several related features showed uncorrected signals but did not survive correction for twelve tests: combined stellar concentration, the 80-percent-light radius, the disk-velocity peak radius, inner stellar-light fraction, and inner-to-outer baryonic velocity ratio.

Features that did not discriminate meaningfully included:

```text
inner bulge fraction: AUC 0.506, p 0.998
outer gas fraction:   AUC 0.560, p 0.718
gas peak radius:      AUC 0.554, p 0.735
```

So the evidence points more specifically to radial disk concentration than to a simple “bulge present,” “more gas,” or “gas peaks elsewhere” explanation.

Classification:

```text
simple_source_separator_supported
```

This classification applies only to the frozen contrast between six strongest `tanh` wins and fourteen strongest rejections.

### Independent verification and attacks

A second program independently rebuilt every cumulative light radius and component fraction without importing the primary functions. It computed AUC by direct positive-negative pair counting rather than the primary rank-sum path and independently enumerated all `38,760` assignments.

Checks:

```text
maximum feature difference = 4.44e-16
maximum AUC difference     = 0
maximum exact-p difference = 0
independent checker        = passed
```

Toy controls produced the expected ordering: a central component was more concentrated than an exponential disk, which was more concentrated than a uniform disk. The uniform-disk half-light radius differed from the analytic value by only `6.74e-8`.

Post-hoc robustness checks, which do not alter the preregistered label:

- normalizing within the actually measured radial span rather than by `Rmax` retained AUC `0.8571` and exact `p=0.0117`;
- removing any one galaxy retained direction-agnostic AUC of at least `0.8857` and exact `p` no worse than `0.01032`.

A relevant warning remains: median fractional velocity uncertainty also separated the selected groups, with AUC `0.8214` and raw exact `p=0.02564`; the strong-`tanh` group generally had smaller fractional errors. This control was weaker than disk concentration and therefore did not trigger the frozen measurement-first stop rule, but it remains a plausible confound that a held-out population test must address.

## What the source result means

### Reproduced observation

Within the selected extreme contrast, strong `tanh` preference is associated with a more centrally concentrated luminous disk relative to the measured rotation-curve extent.

### Cautious interpretation

This is compatible with one broad nonlocal or feedback mechanism whose apparent radial curvature depends on how compactly the source is distributed. A compact disk may drive a relatively rapid, sharply saturating response resembling `tanh`; a more extended source may spread activation over radius and produce rational, arctan, algebraic, or exponential-like tails.

This interpretation is more specific than the earlier bulge observation. It suggests that geometry or source projection may matter more than simply switching a bulge term on or off.

### Hypotheses still open

1. one common mechanism with a geometry-controlled effective curvature term;
2. one mechanism in which a transport, screening, memory, or leakage channel becomes negligible in particular disk-concentration regimes;
3. projection of one nonlocal response through different surface-brightness profiles;
4. stellar `M/L`, distance, inclination, covariance, or measurement precision creating part of the association;
5. several genuinely different mechanisms occupying different galaxy regimes.

### Known real physics and unverified links

The result is a descriptive association in SPARC data. It does not identify dark matter, modified gravity, an oscillator lattice, a Lineum foam, a vortex, a phase front, or a causal field equation.

Lineum currently supports local four-neighbor and eight-neighbor numerical stencils; the eight-neighbor option uses a 3×3 local neighborhood. This is presently an integration stencil, not evidence that a fundamental 3×3 physical cell causes galactic curves. Current Lineum code also contains an explicit `tanh` interaction term, so output from that path cannot count as emergent `tanh`.

Public TOLOG descriptions motivate `tanh` using a 3×3 stabilization picture and dynamic fields. This benchmark validates neither that derivation nor local adaptation. To establish it, the grid dynamics would need to generate the observed curvature family and predict the exceptions without fitting the final function directly.

## Numerical verification of the population census

Population execution comprised

```text
175 galaxies × 2 source lanes × 5 shapes = 1,750 fits
1,750 fits × 16 starts = 28,000 optimization starts
```

Recorded checks:

- `28,000/28,000` starts reported convergence;
- `171` flat or degenerate basins triggered a frozen differential-evolution plus Powell fallback;
- fallback changed the retained objective by at most `8.70e-9`;
- independent scalar curve reconstruction differed by at most `2.65e-12 km/s`;
- scalar chi-squared reconstruction differed by at most `1.29e-11`;
- a deterministic independent 20-galaxy refit differed by at most `3.71e-9` in chi-squared;
- an independent CSV-only summary recovered `82`, `14`, `68`, all winner counts, and `102/102` cross-lane agreement;
- NGC 3198 reproduced the frozen values exactly to declared tolerance.

The population fit environment used Python `3.13.5`, NumPy `2.3.5`, and SciPy `1.17.0`, while repository requirements declare NumPy below `2.0`. Independent checks reduce but do not erase that environment mismatch. The source-structure discriminator used only Python `3.13.5` standard-library operations and therefore did not depend on NumPy or SciPy.

## Root-programme impact

| Programme statement | Impact |
|---|---|
| Finite saturating addition is useful for NGC 3198 | `supports` |
| Exact `tanh` is preferred on NGC 3198 | `supports` |
| Any smooth saturation is equivalent on NGC 3198 | `contradicts` |
| Exact normalized `tanh` is universal | `contradicts` within tested family |
| Broad bounded-transition family is common | `supports` descriptively |
| Source geometry may control transition curvature | `supports` in selected extreme contrast |
| Simple bulge fraction explains exceptions | `contradicts` in selected extreme contrast |
| Simple outer gas fraction explains exceptions | `contradicts` in selected extreme contrast |
| One mechanism with a weak or absent term | `constrains`; compatible but term not identified |
| Early RNB plots derive galactic `tanh` | `contradicts` for supplied rendering |
| Lineum currently derives `tanh` emergently | `not_yet_supported`; explicit `tanh` is a confounder |
| TOLOG 3×3 dynamics are physically validated | `not_yet_supported` |
| Foam, vortex, memory, screening, or phase-front cause | `not_yet_compared` |

No Lineum engine, public API, production test, or whitepaper was changed.

## Next discriminator

The extreme-group result must not be promoted directly into a galactic law. The next cheapest decisive test is a preregistered held-out population analysis across all `102` informative galaxies:

- compute disk concentration without using the winning shape;
- test whether concentration predicts continuous `tanh` penalty and transition-tail direction;
- preserve measurement uncertainty, row count, radial coverage, bulge presence, and stellar calibration as competing explanations;
- freeze any threshold or regression form before evaluating outcomes;
- require out-of-sample or cross-validated performance rather than reusing the twenty extremes.

Only if that association generalizes should Lineum mechanism experiments prioritize source geometry and compare `LAP4`, `LAP8`, and isotropic propagation after removing or bypassing the explicit `tanh` term.

## Retained artifacts and reproduction

Population tools and outputs remain retained from version `0.5.0`.

New source-structure artifacts:

- `research/runners/lineum_b4_source_structure_discriminator.py` — primary standard-library implementation;
- `research/runners/lineum_b4_source_structure_check.py` — independently written scalar checker and toy controls;
- `research/results/lineum_b4_source_structure_discriminator.json` — exact decision summary, all feature statistics, controls, per-galaxy winning feature, robustness, and limits.

Git blob identifiers at this checkpoint:

```text
primary source runner  6c9fcd236a67dafd074ef07a819d10c5b0eb19d1
independent checker    bf8f13a36c9381d2ecc1e31c6c6b243af1667bed
result summary         1c3447e366d6353f0fca9c26d4dc43534e00c5b3
```

Minimal execution after extracting the official archive to a directory:

```bash
python research/runners/lineum_b4_source_structure_discriminator.py \
  --data-dir /path/to/Rotmod_LTG \
  --output source_structure_result.json

python research/runners/lineum_b4_source_structure_check.py \
  --data-dir /path/to/Rotmod_LTG \
  --result source_structure_result.json
```

Expected source result:

```text
classification = simple_source_separator_supported
winning feature = disk_half_light_r_over_rmax
AUC = 0.9047619048
raw exact p = 0.0033023736
Holm-adjusted p = 0.0396284830
independent checker = passed
```

## Prohibited conclusions

This report does not establish:

- that `tanh` is a universal galactic law;
- that disk concentration causes a particular response curve;
- that the twenty extreme galaxies define a validated classifier for all SPARC galaxies;
- that public TOLOG dynamics derive the fit function;
- that TOLOG's unpublished conventions were reproduced;
- that a 3×3 numerical or physical grid is uniquely required;
- that dark matter is absent;
- that modified gravity is established;
- that Lineum generates the response emergently;
- that explicit `tanh` inside current Lineum code is an emergent discovery;
- that Fibonacci numbers, the golden ratio, primes, or Riemann zeros cause the response;
- that a lower chi-squared or AIC alone identifies true physics.

## Version history

- `0.1.0`: frozen NGC 3198 equal-flexibility execution; `tanh_shape_preferred`.
- `0.2.0`: opened the early-Lineum threshold and scale audit.
- `0.3.0`: completed the threshold audit; quantized-linear rendering supported; original mechanism provenance-blocked.
- `0.4.0`: preregistered the complete 175-galaxy population census.
- `0.5.0`: completed and independently checked the census; `mixed_population_evidence`.
- `0.6.0`: recorded the owner's one-mechanism-with-weak-or-absent-term intuition and preregistered a source-only discriminator.
- `0.6.1`: corrected `SBdisk`/`SBbul` column provenance before execution; earlier fit results unchanged.
- `0.7.0`: completed and independently checked the source-structure discriminator; disk concentration passed the frozen strong-separator gate within the selected extreme contrast.
