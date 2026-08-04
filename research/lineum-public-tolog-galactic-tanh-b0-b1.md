# Lineum Public-TOLOG Galactic `tanh` Benchmark — B0/B1 Execution Receipt

**Status:** active  
**Version:** 0.2.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** public-data provenance gate B0 and analytic known-answer gate B1; no astronomical fitting  
**Central question:** is the NGC 3198 input provenance-locked strongly enough to permit the frozen fit, and does the clean-room public `tanh` comparator pass its analytic checks?  
**Current confidence:** high in B0/B1; no confidence yet in a galaxy fit because B2 has not run

## 1. Plain result

The measuring instrument and input package now pass. The supplied `Rotmod_LTG.zip` matches the publicly indexed archive MD5, is intact, contains `175` galaxy files, and contains one valid `NGC3198_rotmod.dat` with `43` rows and `8` columns.

`B0 and B1 passed; B2 is unlocked but not executed.`

This unlocks the first literal fit. It does not reproduce a claimed fit, establish physics, or add `tanh` to Lineum.

## 2. Programme and frozen boundary

This report belongs to three connected questions: emergent galactic response, natural saturation/attraction, and information retention. The strategy is to build the public phenomenological comparator, measure what its function and free parameters provide, and later replace those properties with Lineum-native foam, field, topology, or vortex dynamics. Final success requires removing the explicit galactic `tanh` completely.

The protocol was committed before execution. An earlier run passed B1 but could not download the archive. The project owner then supplied the requested archive. The unchanged runner and unchanged gates were executed. No production code, Lineum equation, or whitepaper changed.

## 3. Public-only firewall and sources

The privately uploaded TOLOG document was not opened, cited, searched, summarized, or used as a hint. No private content entered this work. The clean-room comparator implements only the independently public formula:

`v_model(r)^2 = v_bar(r)^2 + V0^2 * tanh(k_eff * r / r_s)`.

Sources:

- SPARC official site, Federico Lelli, Stacy McGaugh, and James Schombert: `https://astroweb.case.edu/SPARC/`, accessed `2026-08-04`.
- Official mass-model archive: `https://astroweb.case.edu/SPARC/Rotmod_LTG.zip`.
- Zenodo `10.5281/zenodo.16284118`, `https://zenodo.org/records/16284118`, accessed `2026-08-04`; indexed MD5 `e4c8b92766026770ed35e5889064e12b` and size about `110.7 kB`.
- Lelli, McGaugh, and Schombert, *SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves*, AJ 152, 157 (2016), DOI `10.3847/0004-6256/152/6/157`, arXiv `1606.09251`.
- Patrik Tolog public Academia.edu profile, accessed `2026-08-04`, used only for the public formula and fitting description, not as independent review.

The runtime did not observe the browser transfer. It received a user-supplied file after the official link was provided. The file matches the public MD5 and expected structure. MD5 is not a digital signature; the calculated SHA-256 below is the frozen fingerprint, but no official SPARC SHA-256 was available for comparison.

## 4. Exact receipt

| Property | Value |
|---|---|
| archive bytes | `110737` |
| public and observed MD5 | `e4c8b92766026770ed35e5889064e12b` |
| archive SHA-256 | `0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588` |
| ZIP integrity | pass |
| members | `175` |
| unique target | `NGC3198_rotmod.dat` |
| target bytes | `2075` |
| target SHA-256 | `17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953` |
| rows / columns | `43 / 8` |
| radii | `0.32–44.08 kpc`, strictly increasing |
| finite values / positive `errV` | pass / pass |

The full `175`-member list is retained in the full machine receipt. The decision does not depend on any particular non-target filename; it depends on archive checksum, integrity, member count, unique target, and target content. The exact target is retained below and as `research/data/NGC3198_rotmod.dat`.

```text
# Distance = 13.8 Mpc
# Rad	Vobs	errV	Vgas	Vdisk	Vbul	SBdisk	SBbul		
# kpc	km/s	km/s	km/s	km/s	km/s	L/pc^2	L/pc^2
0.32	24.40	35.90	0.00	63.28	0.00	1084.92	0.00
0.64	43.30	16.30	0.00	73.66	0.00	590.57	0.00
0.96	45.50	16.10	0.00	78.98	0.00	410.97	0.00
1.28	58.50	15.40	0.35	82.70	0.00	329.34	0.00
1.61	68.80	7.61	0.15	84.22	0.00	268.62	0.00
1.93	76.90	10.30	-0.05	83.17	0.00	247.67	0.00
2.24	82.00	8.09	-0.47	87.04	0.00	227.56	0.00
2.57	86.90	7.60	-0.95	88.91	0.00	205.02	0.00
2.89	97.60	3.03	-1.43	88.98	0.00	200.20	0.00
3.21	100.00	5.31	-1.14	93.81	0.00	208.58	0.00
3.54	107.00	7.51	-0.39	101.22	0.00	208.47	0.00
3.85	113.00	7.32	0.36	108.53	0.00	196.07	0.00
4.17	117.00	5.21	1.52	115.51	0.00	179.96	0.00
4.50	119.00	5.67	3.07	120.51	0.00	164.19	0.00
4.82	127.00	5.39	4.63	125.42	0.00	150.99	0.00
5.15	132.00	4.34	6.02	129.40	0.00	138.08	0.00
5.46	134.00	2.36	7.16	133.15	0.00	126.00	0.00
5.78	137.00	0.89	8.31	136.45	0.00	113.63	0.00
6.10	140.00	2.84	9.46	139.41	0.00	101.19	0.00
6.43	142.00	0.88	10.61	141.85	0.00	86.52	0.00
6.74	144.00	1.23	11.77	142.32	0.00	70.23	0.00
7.06	146.00	1.57	12.87	140.94	0.00	57.67	0.00
8.04	147.00	3.00	16.39	135.68	0.00	40.74	0.00
9.04	148.00	3.00	20.03	130.79	0.00	31.83	0.00
10.04	152.00	2.00	23.68	128.10	0.00	26.64	0.00
11.04	155.00	2.00	27.08	126.67	0.00	21.02	0.00
12.05	156.00	2.00	30.11	124.98	0.00	15.42	0.00
14.05	157.00	2.00	34.48	118.12	0.00	6.42	0.00
16.07	153.00	2.00	36.43	108.22	0.00	2.95	0.00
18.13	153.00	2.00	37.76	101.10	0.00	2.39	0.00
20.05	154.00	2.00	39.83	96.40	0.00	1.44	0.00
22.12	153.00	2.00	40.92	91.56	0.00	0.72	0.00
24.03	150.00	2.00	41.77	87.03	0.00	0.28	0.00
26.10	149.00	2.00	43.71	82.67	0.00	0.16	0.00
28.16	148.00	2.00	45.41	79.06	0.00	0.08	0.00
30.08	146.00	2.00	45.29	76.07	0.00	0.04	0.00
32.14	147.00	2.00	44.56	73.27	0.00	0.02	0.00
34.06	148.00	2.00	44.81	70.91	0.00	0.01	0.00
36.12	148.00	2.00	45.90	68.62	0.00	0.01	0.00
38.19	149.00	2.00	46.75	66.59	0.00	0.00	0.00
40.10	150.00	2.00	47.48	64.84	0.00	0.00	0.00
42.17	150.00	3.00	48.93	63.10	0.00	0.00	0.00
44.08	149.00	3.00	47.84	61.63	0.00	0.00	0.00
```

## 5. What was computed and checked

B0 hashes the archive, validates ZIP integrity, enumerates members, requires one target, hashes and parses it, and checks shape, finiteness, radius ordering, and uncertainty positivity.

B1 checks zero, small-argument linearity, large-argument saturation, half-saturation, finite centre, monotonicity, positive derivative, the inserted `V0^2` plateau, a finite-difference derivative, and the exact `k_eff/r_s` degeneracy.

Execution:

```text
cd /mnt/data
python lineum_public_tolog_tanh_b0_b1.py --archive Rotmod_LTG.zip --output lineum_public_tolog_tanh_b0_b1_output_b0_passed.json
python -m py_compile lineum_public_tolog_tanh_b0_b1.py
```

Environment: Python `3.13.5`, `Linux-6.12.13-x86_64-with-glibc2.41`, `x86_64`. Runner SHA-256 `da60ac5c24990f4b0b4a35c93f972a3ab32d9db8d179330eccf41ff09e9cdf1a`. Full successful output SHA-256 `fa48e74a512555d5e7f5e9f1a8278202226192788ee831f4490d311150164b42`.

A second implementation independently rehashed, reopened, extracted, parsed, and asserted all B0 conditions without importing the runner; it also parsed the JSON and required all B0/B1 gates, `b0_b1_passed`, and `b2_allowed=true`. Result: `passed`.

## 6. Results

All seven B0 and ten B1 gates passed. Key B1 values:

- half-saturation argument `0.5493061443340548`;
- example half-radius `1.3732653608351368` for `k_eff=2`, `r_s=5`;
- example plateau `V0^2=29929` for `V0=173`;
- analytic versus finite-difference central slopes `11971.6` and `11971.599999999362`;
- relative difference about `5.33e-14`;
- zero response difference when `(2,5)` is rescaled to `(4,10)`, proving only `k_eff/r_s` sets the shape.

## 7. Scientific separation

**Implementation:** validates the input and evaluates an explicit phenomenological `tanh`; it does not solve Lineum dynamics.

**Reproduced observation:** archive, target, and analytic gates passed; no fit occurred.

**Interpretation:** the comparator is ready for a literal fit. Its smooth rise and plateau are largely guaranteed by its functional form, and `k_eff` and `r_s` are not independently identifiable when both vary.

**Hypotheses:** foam, `phi`, `mu`, `psi` topology, and a central vortex remain untested candidates for later replacement.

**Real physics:** SPARC is empirical rotation-curve and baryonic-model data. A future fit would show descriptive performance only; it would not identify the cause, disprove dark matter, validate modified gravity, or prove Lineum ontology.

## 8. Programme impact

| Question | Impact |
|---|---|
| galactic response | comparator and target are ready; no Lineum response tested |
| natural saturation | `tanh` inserts saturation; no Lineum attractor established |
| information retention | unaffected |

## 9. Machine-readable summary

```json
{
  "anti_cheat": {
    "astronomical_fit_performed": false,
    "private_tolog_document_used": false,
    "production_lineum_code_imported_or_modified": false,
    "tolog_code_copied": false
  },
  "archive_bytes": 110737,
  "archive_md5": "e4c8b92766026770ed35e5889064e12b",
  "archive_sha256": "0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588",
  "b0_gates": {
    "published_md5_matches": true,
    "target_has_eight_columns": true,
    "target_member_unique": true,
    "target_radius_strictly_increasing": true,
    "target_uncertainties_positive": true,
    "target_values_finite": true,
    "zip_integrity": true
  },
  "b1_gates": {
    "analytic_derivative_positive": true,
    "central_slope_matches_derivative": true,
    "finite_center": true,
    "half_saturation": true,
    "k_over_rs_degeneracy": true,
    "large_x_plateau": true,
    "monotonic_nonnegative_domain": true,
    "plateau_velocity_squared": true,
    "small_x_linear": true,
    "tanh_zero_exact": true
  },
  "b2_allowed": true,
  "member_count": 175,
  "target": {
    "all_values_finite": true,
    "all_velocity_uncertainties_positive": true,
    "column_counts": [
      8
    ],
    "expected_column_count": 8,
    "expected_columns": [
      "Rad",
      "Vobs",
      "errV",
      "Vgas",
      "Vdisk",
      "Vbul",
      "SBdisk",
      "SBbul"
    ],
    "first_row": [
      0.32,
      24.4,
      35.9,
      0.0,
      63.28,
      0.0,
      1084.92,
      0.0
    ],
    "header_lines": [
      "# Distance = 13.8 Mpc",
      "# Rad\tVobs\terrV\tVgas\tVdisk\tVbul\tSBdisk\tSBbul",
      "# kpc\tkm/s\tkm/s\tkm/s\tkm/s\tkm/s\tL/pc^2\tL/pc^2"
    ],
    "last_row": [
      44.08,
      149.0,
      3.0,
      47.84,
      61.63,
      0.0,
      0.0,
      0.0
    ],
    "radius_strictly_increasing": true,
    "row_count": 43
  },
  "target_bytes": 2075,
  "target_member": "NGC3198_rotmod.dat",
  "target_sha256": "17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953",
  "verdict": "b0_b1_passed"
}
```

## 10. Portable independent verifier

```python
from pathlib import Path
import hashlib, io, math, zipfile

payload = Path("Rotmod_LTG.zip").read_bytes()
assert hashlib.md5(payload).hexdigest() == "e4c8b92766026770ed35e5889064e12b"
assert hashlib.sha256(payload).hexdigest() == "0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588"
with zipfile.ZipFile(io.BytesIO(payload)) as z:
    assert z.testzip() is None
    names = z.namelist()
    matches = [n for n in names if Path(n).name == "NGC3198_rotmod.dat"]
    assert len(names) == 175 and len(matches) == 1
    target = z.read(matches[0])
assert hashlib.sha256(target).hexdigest() == "17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953"
rows = [[float(x) for x in line.split()] for line in target.decode().splitlines() if line.strip() and not line.startswith("#")]
assert len(rows) == 43 and {len(row) for row in rows} == {8}
assert all(math.isfinite(x) for row in rows for x in row)
assert all(a[0] < b[0] for a, b in zip(rows, rows[1:]))
assert all(row[2] > 0 for row in rows)
small = [1e-8, 1e-6, 1e-4]
large = [10.0, 20.0, 50.0]
assert math.tanh(0.0) == 0.0
assert max(abs(math.tanh(x)-x)/x for x in small) <= 4e-9
assert max(abs(1-math.tanh(x)) for x in large) <= 5e-9
assert abs(math.tanh(math.atanh(0.5))-0.5) <= 1e-15
v0, k, rs = 173.0, 2.0, 5.0
assert abs(v0*v0*math.tanh(20)-v0*v0) <= 1e-12*v0*v0
h=1e-6
analytic=v0*v0*k/rs
numeric=v0*v0*math.tanh(k*h/rs)/h
assert abs(numeric-analytic)/analytic <= 1e-12
radii=[i*0.05 for i in range(401)]
assert max(abs(math.tanh(2*r/5)-math.tanh(4*r/10)) for r in radii) <= 1e-15
print("B0 and B1 passed; B2 allowed")
```

## 11. Prohibited conclusions

This does not reproduce the public TOLOG fit or any claimed reduced chi-square; prefer `tanh` over alternatives; derive the formula from local dynamics; show a Lineum rotation curve, force, attractor, memory, or black hole; remove the need for dark matter; or justify placing `tanh` in Lineum. The MD5 match is not a digital signature of the server or downloader.

## 12. Next frozen gate

B2 may now run as a separate checkpoint with the already frozen protocol: literal baryonic squaring, fixed `r_s=5.0 kpc`, `V0 in [0,400] km/s`, `k_eff in [1e-6,100]`, starts `V0=[25,75,150,250]` and `k_eff=[0.01,0.1,1,10]`, tabulated `Vobs`/`errV`, reduced chi-square denominator `N-2`, all starts and residuals retained, baryonic null comparison, and no post-result tuning.

## 13. Version history

- `0.1.0`: B1 passed; B0 network-blocked; B2 prohibited.
- `0.1.1`: corrected archive classification; verdict unchanged.
- `0.2.0`: unchanged runner passed the supplied archive, all B0/B1 gates passed, and B2 was unlocked but not executed.
