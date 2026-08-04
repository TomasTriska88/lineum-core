# Lineum Public-TOLOG Galactic `tanh` Benchmark — B0/B1 Execution Receipt

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** first execution checkpoint for public-data provenance (B0) and analytic known-answer verification (B1), with no astronomical fitting  
**Central question:** can the public SPARC archive be provenance-locked in the available runtime, and does a clean-room implementation of the public galactic `tanh` term satisfy the preregistered limiting, derivative, monotonicity, plateau, and scale checks?  
**Current confidence:** high in the B1 analytic result; high that B0 is blocked by the present runtime network rather than by a data-validation failure; no confidence yet in any astronomical fit because B2 remains prohibited

## 1. Report lineage and frozen boundary

This is the execution child of `Lineum Public-TOLOG Galactic tanh Benchmark`, version `0.1.0`, evidence cutoff `2026-08-04`. The root programme contains three connected questions: galactic long-range response, natural bounded saturation/attraction, and information retention.

The parent preregistration was committed before this execution. This child preserves the execution receipt without rewriting the preregistered protocol after observing results.

This checkpoint changes no production code, no Lineum equation, and no whitepaper. It performs no galaxy fit and does not treat an explicit `tanh` term as Lineum emergence.

## 2. Public-source-only firewall

The privately uploaded TOLOG document was not opened, cited, searched from, or used as a hint. No equation, number, parameter, wording, table, image, code, or hypothesis was taken from it.

Public inputs used:

1. Patrik Tolog public Academia.edu profile, accessed `2026-08-04`, for the publicly displayed phenomenological form:

   `v_model(r)^2 = v_bar(r)^2 + V0^2 * tanh(k_eff * r / r_s)`.

2. Official SPARC website, maintained by Federico Lelli, Stacy McGaugh, and James Schombert, accessed `2026-08-04`:

   `https://astroweb.case.edu/SPARC/`

3. Official Newtonian mass-model archive endpoint declared by the SPARC site:

   `https://astroweb.case.edu/SPARC/Rotmod_LTG.zip`

4. Zenodo archival record `10.5281/zenodo.16284118`, accessed `2026-08-04`, which publicly lists `Rotmod_LTG.zip` and the published archive MD5 `e4c8b92766026770ed35e5889064e12b`.

5. A public GitHub mirror file was used only as an auxiliary parser control after B0 had already been classified as blocked. It was not accepted as official SPARC provenance and was not used for fitting:

   - repository: `carsondowns-cte/Rotmod_LTG`;
   - file: `NGC3198_rotmod.dat`;
   - Git blob SHA: `8a4b4f4f8f6a7e874556596ea03ad13041ed645f`;
   - independently calculated file SHA-256: `17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953`.

No TOLOG code was copied. The retained runner is an original standard-library implementation of the public mathematics and provenance checks.

## 3. What the implementation computes

The runner has two isolated stages.

### B0 — provenance path

It attempts, in order:

1. the official SPARC archive URL;
2. the Zenodo archival mirror only if the official endpoint cannot be retrieved.

For any retrieved archive it records:

- byte length;
- SHA-256;
- MD5 and comparison with the public Zenodo MD5;
- ZIP integrity;
- complete member list and count;
- uniqueness of `NGC3198_rotmod.dat`;
- target-file byte length and SHA-256;
- header, row count, column count, finite-value checks, increasing radii, and positive velocity uncertainties.

The strict preregistered B0 gate passes only for the official primary archive or a pre-downloaded local archive whose provenance can be independently established. A mirror-only download is labelled separately rather than silently promoted.

### B1 — analytic known-answer path

The runner independently verifies:

- `tanh(0) = 0`;
- the small-argument approximation `tanh(x) ≈ x`;
- the large-argument limit `tanh(x) → 1`;
- the half-saturation point `x = atanh(0.5)`;
- finite central model velocity;
- monotonicity for nonnegative argument;
- positivity of the analytic derivative;
- asymptotic insertion of an added velocity-squared plateau `V0^2`;
- the central derivative of the added velocity-squared term;
- exact degeneracy under simultaneous rescaling that leaves `k_eff / r_s` unchanged.

## 4. Environment, retained artifacts, and commands

Environment:

- Python `3.13.5`;
- platform `Linux-6.12.13-x86_64-with-glibc2.41`;
- architecture `x86_64`;
- runner SHA-256 `e0e487aaebd29652d03b1f3ef224003a3d4b5d28e9d509fe57cf30e65efe2317`;
- output SHA-256 `ad689b7054613178dc7c8aaf5ef5852cc78efe08a0ab75eb15405e59d20677e2`.

Retained paths:

- `research/runners/lineum_public_tolog_tanh_b0_b1.py`;
- `research/results/lineum_public_tolog_tanh_b0_b1_output.json`.

Commands:

```text
python research/runners/lineum_public_tolog_tanh_b0_b1.py --timeout 10 --output research/results/lineum_public_tolog_tanh_b0_b1_output.json
python -m py_compile research/runners/lineum_public_tolog_tanh_b0_b1.py
```

The available runtime had no usable outbound DNS resolution for ordinary Python or shell network access. Both public archive endpoints failed before an HTTP response could be obtained.

## 5. Human-readable result

### B0 verdict — blocked by runtime network

Both archive attempts failed with:

`URLError: Temporary failure in name resolution`.

Consequences:

- no archive bytes were obtained;
- no official archive SHA-256 could be calculated;
- the member list could not be locked;
- `NGC3198_rotmod.dat` could not be extracted from the official ZIP;
- no unofficial galaxy rows were substituted;
- B0 did not pass;
- B2 astronomical fitting remains prohibited.

This is an execution-environment limitation. It is not evidence that the SPARC archive is unavailable to the public, corrupt, or scientifically unsuitable.

### B1 verdict — passed

All ten analytic gates passed.

Key values:

- half-saturation argument: `0.5493061443340548`;
- for `k_eff = 2` and `r_s = 5`, half-saturation radius: `1.3732653608351368`;
- example plateau amplitude: `V0^2 = 29929` for `V0 = 173`;
- value at argument `20`: exactly `29929` in the runtime floating-point representation;
- analytic central added-velocity-squared slope: `11971.6`;
- forward-difference slope: `11971.599999999362`;
- relative derivative error: approximately `5.33e-14`;
- simultaneous rescaling `(k_eff=2, r_s=5)` to `(k_eff=4, r_s=10)` produced a maximum response difference of exactly `0.0` on the test grid.

The last result means that the literal function identifies only the ratio `k_eff / r_s` when both quantities are treated as adjustable. They must not be counted as two independently identifiable shape parameters without an external convention fixing one of them.

## 6. Independent and adversarial controls

### 6.1 Parser control on a public mirror

The public mirror copy of `NGC3198_rotmod.dat` was parsed only to test the code path, not to satisfy B0. The parser recovered:

- `43` data rows;
- exactly `8` numeric columns per row;
- finite values throughout;
- strictly increasing radius;
- positive velocity uncertainty in every row;
- first radius `0.32 kpc`;
- last radius `44.08 kpc`.

This confirms that the parser can read the expected public table structure. It does not prove byte identity with the official ZIP member.

### 6.2 Synthetic ZIP rejection control

A synthetic ZIP containing the mirror text under the expected target name was passed through the archive inspector.

Expected behavior was observed:

- ZIP integrity passed;
- target discovery passed;
- column and finite-value checks passed;
- the published-MD5 gate failed.

This demonstrates that the runner does not mark an arbitrary structurally valid ZIP as the official archive merely because the filename and table shape look correct.

### 6.3 Independence boundary

The analytic checks share Python's standard-library `math` implementation with model evaluation, but the controls include closed-form limits, a separately evaluated derivative expression, a finite-difference comparison, and a parameter-rescaling identity. No astronomical observation or fit target was used to select thresholds after execution.

## 7. Decision-complete machine-readable receipt

```json
{
  "anti_cheat": {
    "astronomical_fit_performed": false,
    "private_tolog_document_used": false,
    "production_lineum_code_imported_or_modified": false,
    "tolog_code_copied": false
  },
  "b0": {
    "archive": null,
    "attempts": [
      {
        "content_length_header": null,
        "content_type": null,
        "elapsed_seconds": 0.021840810775756836,
        "error": "<urlopen error [Errno -3] Temporary failure in name resolution>",
        "error_type": "URLError",
        "ok": false,
        "source_name": "official_sparc",
        "status": null,
        "url": "https://astroweb.case.edu/SPARC/Rotmod_LTG.zip"
      },
      {
        "content_length_header": null,
        "content_type": null,
        "elapsed_seconds": 5.006422996520996,
        "error": "<urlopen error [Errno -3] Temporary failure in name resolution>",
        "error_type": "URLError",
        "ok": false,
        "source_name": "zenodo_archival_mirror",
        "status": null,
        "url": "https://zenodo.org/records/16284118/files/Rotmod_LTG.zip?download=1"
      }
    ],
    "passed": false,
    "reason": "No archive bytes were retrievable; no unofficial galaxy rows were substituted.",
    "selected_source": null,
    "status": "blocked_by_runtime_network"
  },
  "b1": {
    "center": {"V0": 173.0, "model_velocity": 80.0, "v_bar": 80.0},
    "derivative": {
      "analytic_central_slope": 11971.6,
      "expression": "d(V0^2*tanh(k_eff*r/r_s))/dr = V0^2*(k_eff/r_s)*sech^2(k_eff*r/r_s)",
      "forward_difference_central_slope": 11971.599999999362,
      "relative_error": 5.3331658311720706e-14
    },
    "dimensionless_argument_requirement": "k_eff * r / r_s must be dimensionless",
    "formula": "v_model(r)^2 = v_bar(r)^2 + V0^2 * tanh(k_eff * r / r_s)",
    "gates": {
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
    "half_saturation": {
      "example_half_radius": 1.3732653608351368,
      "example_k_eff": 2.0,
      "example_r_s": 5.0,
      "tanh_x_half": 0.49999999999999994,
      "x_half": 0.5493061443340548
    },
    "passed": true,
    "plateau": {
      "V0": 173.0,
      "expected_added_velocity_squared": 29929.0,
      "observed_at_x_20": 29929.0
    },
    "scale_degeneracy": {
      "comparison": "(k_eff=2,r_s=5) versus (k_eff=4,r_s=10)",
      "max_absolute_difference": 0.0
    }
  },
  "b2_allowed": false,
  "environment": {
    "machine": "x86_64",
    "platform": "Linux-6.12.13-x86_64-with-glibc2.41",
    "python": "3.13.5"
  },
  "public_sources": {
    "official_sparc": "https://astroweb.case.edu/SPARC/Rotmod_LTG.zip",
    "zenodo_archival_mirror": "https://zenodo.org/records/16284118/files/Rotmod_LTG.zip?download=1",
    "zenodo_doi": "10.5281/zenodo.16284118",
    "zenodo_published_md5": "e4c8b92766026770ed35e5889064e12b"
  },
  "runner_scope": "B0 public-data provenance and B1 analytic known-answer audit only; no fit performed",
  "schema_version": "0.1.0",
  "verdict": "b1_passed_b0_blocked"
}
```

## 8. Portable reproduction code

The following standard-library script reproduces the decision-relevant B1 result and the B0 network probe without importing the retained runner:

```python
import hashlib
import io
import json
import math
import urllib.request
import zipfile
from pathlib import Path

OFFICIAL = "https://astroweb.case.edu/SPARC/Rotmod_LTG.zip"
ZENODO = "https://zenodo.org/records/16284118/files/Rotmod_LTG.zip?download=1"
EXPECTED_MD5 = "e4c8b92766026770ed35e5889064e12b"
TARGET = "NGC3198_rotmod.dat"


def get(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Lineum-B0-B1-reproduction/0.1"})
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read(), None
    except Exception as exc:
        return None, f"{type(exc).__name__}: {exc}"


def inspect(payload):
    names = None
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        assert archive.testzip() is None
        names = archive.namelist()
        matches = [name for name in names if Path(name).name == TARGET]
        assert len(matches) == 1
        target = archive.read(matches[0])
    rows = []
    for line in target.decode("ascii").splitlines():
        if line.strip() and not line.lstrip().startswith("#"):
            rows.append([float(item) for item in line.split()])
    return {
        "archive_sha256": hashlib.sha256(payload).hexdigest(),
        "archive_md5": hashlib.md5(payload).hexdigest(),
        "published_md5_matches": hashlib.md5(payload).hexdigest() == EXPECTED_MD5,
        "member_count": len(names),
        "target_sha256": hashlib.sha256(target).hexdigest(),
        "row_count": len(rows),
        "column_counts": sorted({len(row) for row in rows}),
        "finite": all(math.isfinite(value) for row in rows for value in row),
    }


attempts = []
archive = None
for source, url in (("official", OFFICIAL), ("zenodo", ZENODO)):
    archive, error = get(url)
    attempts.append({"source": source, "url": url, "error": error})
    if archive is not None:
        break

small = [1e-8, 1e-6, 1e-4]
large = [10.0, 20.0, 50.0]
half_x = math.atanh(0.5)
v0 = 173.0
vbar = 80.0
k = 2.0
rs = 5.0
step = 1e-6
analytic_slope = v0 * v0 * k / rs
numeric_slope = v0 * v0 * math.tanh(k * step / rs) / step
radii = [i * 0.05 for i in range(401)]
first = [math.tanh(2.0 * r / 5.0) for r in radii]
second = [math.tanh(4.0 * r / 10.0) for r in radii]

gates = {
    "tanh_zero_exact": math.tanh(0.0) == 0.0,
    "small_x_linear": max(abs(math.tanh(x) - x) / x for x in small) <= 4e-9,
    "large_x_plateau": max(abs(1.0 - math.tanh(x)) for x in large) <= 5e-9,
    "half_saturation": abs(math.tanh(half_x) - 0.5) <= 1e-15,
    "finite_center": math.sqrt(vbar * vbar + v0 * v0 * math.tanh(0.0)) == vbar,
    "positive_derivative": all(1.0 / math.cosh(i * 0.01) ** 2 > 0 for i in range(2001)),
    "plateau_v2": abs(v0 * v0 * math.tanh(20.0) - v0 * v0) <= 1e-12 * v0 * v0,
    "central_slope": abs(numeric_slope - analytic_slope) / analytic_slope <= 1e-12,
    "scale_degeneracy": max(abs(a - b) for a, b in zip(first, second)) <= 1e-15,
}

print(json.dumps({
    "b0_attempts": attempts,
    "archive": inspect(archive) if archive is not None else None,
    "b1_gates": gates,
    "b1_passed": all(gates.values()),
}, indent=2))
```

## 9. Scientific interpretation

### What is implemented

A clean-room evaluator and provenance inspector for the publicly displayed `tanh` form.

### What was observed

B1 passed every analytic gate. B0 could not obtain archive bytes because the runtime could not resolve either host.

### What may be interpreted cautiously

The public `tanh` term inserts these properties by construction:

- zero added term at the centre;
- approximately linear growth of the added velocity-squared term at small radius;
- smooth monotonic transition;
- a finite outer velocity-squared plateau;
- bounded amplitude set by `V0`;
- a transition scale controlled by the ratio `k_eff / r_s`.

These are verified properties of the mathematical comparator, not yet results about galaxies or Lineum.

### What remains hypothesis or analogy

It remains hypothetical that Lineum foam relaxation, `phi`, `mu`, `psi` topology, a central vortex, or their shared dynamics can reproduce any of these properties emergently.

### Connection to established real physics

SPARC is a real observational database of galaxy rotation curves and baryonic mass models. This checkpoint did not yet compare the public formula with any official SPARC row because the official archive provenance gate remains open.

## 10. Prohibited conclusions

This checkpoint does not establish that:

- the public TOLOG NGC 3198 fit is reproduced;
- any claimed reduced chi-square value is correct;
- `tanh` is uniquely preferred over another saturator;
- TOLOG derives the galactic formula from local grid dynamics;
- Lineum reproduces a galaxy rotation curve;
- Lineum has a natural attractor;
- Lineum stores causal information;
- a central Lineum vortex is a black hole;
- dark matter is absent or unnecessary;
- the explicit galactic `tanh` term belongs in the Lineum equation.

## 11. Narrow decision and next gate

Checkpoint verdict:

`B1 passed; B0 blocked by runtime network; B2 is not allowed.`

The next permissible action is not fitting or parameter tuning. It is to execute the exact retained runner in an environment that can retrieve the official SPARC ZIP, retain the archive and target hashes, and append the resulting B0 receipt. Only a committed `b0_b1_passed` result may unlock B2.
