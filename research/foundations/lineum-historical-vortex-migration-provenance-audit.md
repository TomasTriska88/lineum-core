# Historical Vortex Migration Provenance Audit

**Status:** validated negative-result audit  
**Version:** 1.0.0  
**Evidence cutoff:** 2026-07-31  
**Repository:** TomasTriska88/lineum-core  
**Target branch:** develop  
**Historical implementation commit:** `ccf95dad8e61325fe675f6618264c258089da13a`  
**Historical source blob:** `f3a94fd1b1e2df876d1053fe1d822dd3b33117d9`  
**Historical migration-claim commit:** `7082286caef4f8defaf3627fe682742d90d7a410`  
**Scope:** This standalone audit reconstructs the July 2025 stochastic field run that wrote `output/frames_curl.npy`, tests the historical phase-curl migration observer against a phase-safe plaquette-winding observer, and determines whether that artifact can serve as provenance for the current broad transported Lineum remnant. It does not test the later P2 source-off package, current Core behavior, physical gravity, or a universal vortex ontology.  
**Central questions:** Was the historical run localized and numerically bounded over its declared 200-step horizon? Did the maximum of `curl(gradient(angle(Psi)))` reliably identify a true phase winding? Can its apparent trajectory support a claim that a vortex core migrated? May this historical artifact be reused as the P0 source for the current core-envelope-wake programme?  
**Current confidence:** high that the seeded reconstruction faithfully preserves the historical update order and post-step `Phi` injection; high that the historical maximum-curl observer is branch-cut unsafe; high that the reconstructed lane becomes global and rapidly unbounded; high that this artifact must not be used as evidence for a localized migrating vortex; no implication for the independently retained 2026 P2 transported multi-defect result.

## 1. Answer first

The historical animation does not provide trustworthy evidence that one compact vortex core migrated.

A simple picture is a compass painted on a sheet. The direction can rotate smoothly, but the written angle jumps from `+pi` to `-pi` whenever it crosses the chosen numbering seam. The historical observer differentiated that wrapped number directly. It therefore produced sharp apparent curls along the bookkeeping seam even when the underlying phase was smooth and contained no vortex.

The seeded reconstruction also did not remain a compact object. In all eight runs, cells above the historical broad-mask threshold covered more than 99 percent of the `128 x 128` grid by step 24 or 25. The maximum `|Psi|` exceeded `1,000` by step 44-46 and reached a median of approximately `5.13e25` by step 199.

The durable verdict is:

```text
historical localized migrating vortex = not supported
historical maximum wrapped-phase curl observer = invalid for core tracking
historical run numerically bounded over 200 steps = false
historical artifact eligible as current wake P0 source = no
later P2 transported multi-defect result affected by this audit = no
```

## 2. Historical provenance

The audited source was the repository file `lineum.py` at commit:

```text
commit: ccf95dad8e61325fe675f6618264c258089da13a
source blob: f3a94fd1b1e2df876d1053fe1d822dd3b33117d9
grid: 128 x 128
steps: 200
historical output: output/frames_curl.npy
historical output blob: 7c4726cd46e5c924e80e588658e96f523909c49f
```

A later commit recorded a high-confidence migration interpretation:

```text
commit: 7082286caef4f8defaf3627fe682742d90d7a410
claim family: apparent vortex migration from curl-frame centroid or peak motion
```

The binary `frames_curl.npy` artifact is not required by this report. The complete decision-relevant historical update and observer are independently transcribed below.

The original script did not freeze a random seed. Therefore the exact original binary artifact cannot be reconstructed bit-for-bit from the repository alone. This audit uses the explicit seed set `0..7` while preserving the legacy NumPy random-draw order. The seed insertion is the only intended stochastic-control change.

## 3. Evidence layers

### 3.1 What the historical implementation computed

For each step, the implementation:

1. computed amplitude `A = |Psi|`;
2. generated stochastic linon events from a sigmoid of amplitude plus gradient magnitude;
3. added phase-aligned Gaussian fluctuation;
4. added a `Phi` interaction term and a gradient-derived `Phi` flow;
5. applied dissipation and periodic four-neighbour diffusion to `Psi`;
6. updated `Phi` from clipped `|Psi|^2`, reaction, and two diffusion writes;
7. detected local amplitude maxima above `0.12`;
8. injected `0.2` into a `3 x 3` `Phi` neighbourhood around every detected maximum;
9. wrapped phase with `phase = angle(Psi)`;
10. computed ordinary finite differences of that wrapped scalar phase;
11. called the antisymmetric second-difference result `curl`.

The observer was:

```python
phase = np.angle(psi)
grad_x, grad_y = np.gradient(phase)
dFy_dx = np.gradient(grad_y, axis=1)
dFx_dy = np.gradient(grad_x, axis=0)
curl = dFy_dx - dFx_dy
```

This is not equivalent to a branch-safe circulation of phase differences around a plaquette.

### 3.2 What was reproducibly observed

Across seeds `0..7`:

```text
first step at which |Psi| > 0.15 covered more than 99% of cells:
minimum 24
median 25
maximum 25

first step at which max(|Psi|) exceeded 1000:
minimum 44
median 45
maximum 46
```

Median maximum amplitude across the eight runs:

```text
step 0:   8.264850792300878e-01
step 25:  3.564055418134655e+00
step 50:  5.320612429203005e+03
step 75:  1.907221628845719e+07
step 100: 8.878313888513936e+10
step 125: 4.483535156907661e+14
step 150: 2.321336501179645e+18
step 175: 1.278013608111376e+22
step 199: 5.132663624604731e+25
```

The location of the maximum historical curl jumped by more than 30 cells between consecutive frames between 21 and 44 times per run. The largest one-frame jump was between `136.74` and `171.17` cells on a `128 x 128` grid. Exact co-location of the maximum historical curl with a branch-safe nonzero plaquette winding occurred in only `0.0%` to `3.5%` of frames, with a median of `0.25%`.

### 3.3 Cautious interpretation

The run is a rapidly global stochastic excitation with strong positive feedback. The reported maximum-curl trajectory is dominated by a non-identifying observer and cannot be interpreted as a material track of one core.

This does not prove that no vortex-like structures existed anywhere in the run. The branch-safe winding detector found many positive and negative plaquette windings. It shows that the selected maximum of the historical curl array was not a valid identifier for one of them.

### 3.4 Hypotheses not selected

The audit does not decide whether a better-bounded historical equation could support:

- a compact vortex;
- a coherent vortex gas;
- a transported topological defect;
- a core plus envelope;
- a wake;
- a gravity-like interaction.

Those require separate frozen runs and observers.

### 3.5 Correspondence with real physics

No physical units were validated. The historical assignments of one pixel to one picometre and one update to one zeptosecond were declarations, not derived calibrations. No laboratory or astronomical observable was fitted. This audit is numerical and informational only.

## 4. Why the historical curl is branch-cut unsafe

A complex phase is periodic. The represented angle returned by `angle` lies on a selected interval and jumps by approximately `2*pi` at its branch cut. Ordinary differentiation treats that representational jump as a large spatial change.

A phase-safe plaquette observer instead wraps every neighbour difference before summing around a cell:

```text
w = wrap(p01 - p00)
  + wrap(p11 - p01)
  + wrap(p10 - p11)
  + wrap(p00 - p10)

topological charge = w / (2*pi)
```

The registered smooth-phase negative control used:

```text
theta(x, y) = 0.15 x + 0.07 y
phase = angle(exp(i theta))
```

The underlying phase has no interior singularity. Results:

```text
historical curl maximum magnitude: 4.71238898038469
historical curl cells with |curl| > 0.1: 847
phase-safe winding maximum magnitude: 1.4135798584282297e-16
phase-safe cells with |winding| > 0.5: 0
```

The historical observer therefore produces a strong false signal on a known no-vortex field.

## 5. Localization and boundedness gates

The following gates are applied retrospectively but without fitting them to individual seeds.

### Gate H1: compact support

```text
fail if more than 99% of cells exceed |Psi| > 0.15
```

All eight runs failed by step 25.

### Gate H2: numerical boundedness

```text
fail if max(|Psi|) exceeds 1000 within 200 steps
```

All eight runs failed by step 46.

The threshold `1000` is deliberately generous relative to the initial maximum near one. It is not a physical amplitude limit. It is sufficient to show that the state amplified by many orders of magnitude and that apparent geometric motion cannot be separated cleanly from runaway growth.

### Gate H3: phase-safe identity

```text
a claimed curl-core track must map to a registered phase-safe defect
```

The maximum historical curl had near-zero exact co-location with a phase-safe winding across the matrix. The gate failed.

### Gate H4: no-vortex negative control

```text
a vortex observer must remain quiet on a smooth, nonsingular phase field
```

The historical curl generated 847 supra-threshold cells. The gate failed.

## 6. Failure-to-mechanism classification

### What failed

A specific 2025 stochastic implementation plus a specific wrapped-phase curl observer failed as evidence for a localized migrating vortex.

### What remained positive or unexplained

The simulation generated many branch-safe plaquette windings and rich spatial activity. Those facts are not erased, but they do not identify one stable object.

### Failure location

```text
equation or parameter regime:
    positive feedback becomes rapidly unbounded;

initial state:
    stochastic and unseeded in the historical artifact;

observer:
    branch-cut unsafe and non-identifying;

interpretation:
    peak or centroid motion was promoted to core migration without identity controls.
```

### Repair classes

1. **Observer repair:** use wrapped neighbour differences, topological charge, connected defect tracks, and explicit birth/death matching.
2. **Dynamical repair:** use a bounded current implementation and frozen source-off continuation.
3. **Identity repair:** require core persistence, local sensitivity, transplantation, removal, and regeneration controls.
4. **Support repair:** distinguish compact core, near envelope, wake, and far environment rather than tracking one global maximum.

The current P2 programme already belongs to a later, separate lane and must be audited on its own retained package.

## 7. Decision and programme impact

This report supersedes only the historical interpretation that the 2025 curl artifact confirmed a migrating vortex core.

It does not supersede or weaken:

- the current Core implementation;
- the retained P2 source-off result;
- the `12/12` transported multi-defect or vortex-gas classification;
- the new core-envelope-wake preregistration.

The correct provenance rule is:

```text
Do not cite ccf95dad... or 7082286... as evidence for the current broad remnant.
Use the retained P2 package and its own observer as the P0 source.
```

No code or whitepaper claim is changed by this audit.

## 8. Limitations

1. The original script did not record an RNG seed.
2. The historical binary `frames_curl.npy` was not decoded in this environment.
3. The audit reconstructs the source from its immutable Git blob and freezes eight new seeds.
4. The environment used Python `3.13.5`, NumPy `2.3.5`, and SciPy `1.17.0`; the historical dependency versions were not recorded.
5. Exact floating-point values may vary across library versions, but the failures span many orders of magnitude and every frozen seed.
6. The exact-colocation check is intentionally strict. A looser neighbourhood match could raise the percentage, but it would not repair the smooth-phase false positive or runaway global support.
7. No current P2 code was executed here.
8. No claim about nature follows.

## 9. Reopen triggers

Reopen this audit only if one of the following becomes available:

- the exact original RNG state and supported dependency environment;
- a documented alternative observer actually used for the historical migration claim;
- evidence that the stored artifact was generated from a different source blob;
- an independent phase-safe analysis showing a persistent connected defect with registered identity controls.

Absent such evidence, the historical migration claim remains unsupported.

## 10. Complete executable verifier

Requirements:

```text
Python 3
NumPy
SciPy
CPU
```

Run:

```bash
python historical_vortex_migration_audit.py
```

The script prints the complete machine-readable receipt.

```python
import json
import platform
import sys

import numpy as np
import scipy
from scipy.ndimage import gaussian_filter, maximum_filter

SIZE = 128
STEPS = 200
SEEDS = tuple(range(8))
CHECKPOINTS = (0, 25, 50, 75, 100, 125, 150, 175, 199)


def diffuse_complex(field, rate=0.05):
    return rate * (
        np.roll(field, 1, axis=0)
        + np.roll(field, -1, axis=0)
        + np.roll(field, 1, axis=1)
        + np.roll(field, -1, axis=1)
        - 4 * field
    )


def old_curl(phase):
    grad_x, grad_y = np.gradient(phase)
    d_fy_dx = np.gradient(grad_y, axis=1)
    d_fx_dy = np.gradient(grad_x, axis=0)
    return d_fy_dx - d_fx_dy


def winding_mask(phase):
    p00 = phase[:-1, :-1]
    p01 = phase[:-1, 1:]
    p11 = phase[1:, 1:]
    p10 = phase[1:, :-1]

    def wrap(delta):
        return np.angle(np.exp(1j * delta))

    winding = (
        wrap(p01 - p00)
        + wrap(p11 - p01)
        + wrap(p10 - p11)
        + wrap(p00 - p10)
    ) / (2 * np.pi)

    mask = np.zeros_like(phase, dtype=bool)
    mask[:-1, :-1] = np.abs(winding) > 0.5
    return mask, winding


def run(seed):
    # The historical script used the legacy global NumPy RNG and did not
    # declare a seed. This audit freezes one explicitly before the same draw
    # sequence so that the reconstruction is reproducible.
    np.random.seed(seed)

    amp = np.random.normal(0.0, 0.1, (SIZE, SIZE))
    phase = np.random.uniform(0, 2 * np.pi, (SIZE, SIZE))
    amp[SIZE // 2, SIZE // 2] += 1.0
    psi = amp * np.exp(1j * phase)

    noise = np.random.normal(0.0, 1.0, (SIZE, SIZE))
    blurred = gaussian_filter(noise, sigma=10)
    delta = blurred / np.max(np.abs(blurred)) * 0.05
    phi = np.zeros((SIZE, SIZE), dtype=np.complex128)

    broad_step = None
    amplitude_step = None
    checkpoints = {}
    old_peak_locations = []
    old_peak_at_winding = 0
    winding_counts = []
    old_peak_values = []

    for step in range(STEPS):
        amp_before = np.abs(psi)
        grad_x, grad_y = np.gradient(amp_before + delta)
        grad_mag = np.sqrt(np.clip(grad_x**2 + grad_y**2, 0, 1e4))

        probability = 1 / (1 + np.exp(-5 * (amp_before + grad_mag)))
        linons = (np.random.rand(SIZE, SIZE) < probability).astype(float)
        linon_effect = (0.03 + 0.02 * amp_before.clip(min=0)) * linons
        linon_complex = linon_effect * np.exp(1j * np.angle(psi))
        fluctuation = np.random.normal(0.0, 0.01, (SIZE, SIZE)) * np.exp(
            1j * np.angle(psi)
        )

        interaction_term = 0.04 * np.clip(phi, -10, 10) * psi
        grad_phi_x, grad_phi_y = np.gradient(np.abs(phi))
        psi += -0.004 * (grad_phi_x + 1j * grad_phi_y)
        psi += linon_complex + fluctuation + interaction_term
        psi -= 0.001 * psi
        psi += diffuse_complex(psi)

        local_input = np.clip(np.abs(psi) ** 2, 0, 1e4)
        phi += 0.06 * (local_input - phi)
        phi += 0.02 * diffuse_complex(phi)
        phi += 0.015 * diffuse_complex(phi)

        amplitude = np.abs(psi)
        phase = np.angle(psi)

        # Preserve the historical post-step particle-triggered Phi injection.
        local_max = amplitude == maximum_filter(amplitude, size=3)
        particles = (amplitude > 0.12) & local_max
        for cy, cx in np.argwhere(particles):
            y_min = max(cy - 1, 0)
            y_max = min(cy + 2, SIZE)
            x_min = max(cx - 1, 0)
            x_max = min(cx + 2, SIZE)
            phi[y_min:y_max, x_min:x_max] += 0.2

        broad_fraction = float(np.mean(amplitude > 0.15))
        if broad_step is None and broad_fraction > 0.99:
            broad_step = step

        maximum_amplitude = float(np.max(amplitude))
        if amplitude_step is None and maximum_amplitude > 1e3:
            amplitude_step = step
        if step in CHECKPOINTS:
            checkpoints[str(step)] = maximum_amplitude

        curl = old_curl(phase)
        old_peak = np.unravel_index(np.argmax(np.abs(curl)), curl.shape)
        old_peak_locations.append(old_peak)
        old_peak_values.append(float(np.abs(curl[old_peak])))

        true_mask, _ = winding_mask(phase)
        winding_counts.append(int(np.sum(true_mask)))
        if true_mask[old_peak]:
            old_peak_at_winding += 1

    jumps = [
        float(
            np.linalg.norm(
                np.asarray(old_peak_locations[index])
                - np.asarray(old_peak_locations[index - 1])
            )
        )
        for index in range(1, len(old_peak_locations))
    ]

    return {
        "seed": seed,
        "broad_fraction_gt_0_99_first_step": broad_step,
        "max_amp_gt_1e3_first_step": amplitude_step,
        "max_amp_checkpoints": checkpoints,
        "broad_fraction_final": float(np.mean(np.abs(psi) > 0.15)),
        "old_curl_peak_jump_gt_10_count": sum(jump > 10 for jump in jumps),
        "old_curl_peak_jump_gt_30_count": sum(jump > 30 for jump in jumps),
        "old_curl_peak_max_jump": max(jumps),
        "old_curl_peak_winding_exact_colocation_fraction": (
            old_peak_at_winding / STEPS
        ),
        "true_winding_count_median": float(np.median(winding_counts)),
        "true_winding_count_min": min(winding_counts),
        "true_winding_count_max": max(winding_counts),
        "old_curl_peak_abs_median": float(np.median(old_peak_values)),
        "old_curl_peak_abs_max": max(old_peak_values),
    }


def smooth_phase_negative_control():
    y, x = np.indices((SIZE, SIZE))
    unwrapped = 0.15 * x + 0.07 * y
    wrapped = np.angle(np.exp(1j * unwrapped))

    curl = old_curl(wrapped)
    _, winding = winding_mask(wrapped)
    return {
        "old_curl_abs_max": float(np.max(np.abs(curl))),
        "old_curl_cells_abs_gt_0_1": int(np.sum(np.abs(curl) > 0.1)),
        "phase_safe_winding_abs_max": float(np.max(np.abs(winding))),
        "phase_safe_winding_cells_abs_gt_0_5": int(
            np.sum(np.abs(winding) > 0.5)
        ),
    }


def summarize(runs):
    broad_steps = [run["broad_fraction_gt_0_99_first_step"] for run in runs]
    amplitude_steps = [run["max_amp_gt_1e3_first_step"] for run in runs]
    checkpoint_medians = {
        str(step): float(
            np.median([run["max_amp_checkpoints"][str(step)] for run in runs])
        )
        for step in CHECKPOINTS
    }
    maximum_jumps = [run["old_curl_peak_max_jump"] for run in runs]
    colocations = [
        run["old_curl_peak_winding_exact_colocation_fraction"] for run in runs
    ]
    return {
        "seeds": list(SEEDS),
        "first_step_mask_gt_0_15_covers_gt_99pct": {
            "min": min(broad_steps),
            "median": float(np.median(broad_steps)),
            "max": max(broad_steps),
            "values": broad_steps,
        },
        "first_step_max_abs_psi_gt_1e3": {
            "min": min(amplitude_steps),
            "median": float(np.median(amplitude_steps)),
            "max": max(amplitude_steps),
            "values": amplitude_steps,
        },
        "median_max_abs_psi_by_step": checkpoint_medians,
        "old_curl_peak_jump_gt_10_per_run": [
            run["old_curl_peak_jump_gt_10_count"] for run in runs
        ],
        "old_curl_peak_jump_gt_30_per_run": [
            run["old_curl_peak_jump_gt_30_count"] for run in runs
        ],
        "old_curl_peak_max_jump": {
            "min": min(maximum_jumps),
            "median": float(np.median(maximum_jumps)),
            "max": max(maximum_jumps),
        },
        "old_curl_peak_exact_winding_colocation_fraction": {
            "min": min(colocations),
            "median": float(np.median(colocations)),
            "max": max(colocations),
            "values": colocations,
        },
        "true_winding_count_median_across_time_per_run": [
            run["true_winding_count_median"] for run in runs
        ],
    }


def main():
    runs = [run(seed) for seed in SEEDS]
    receipt = {
        "environment": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "platform": platform.platform(),
        },
        "summary": summarize(runs),
        "smooth_phase_negative_control": smooth_phase_negative_control(),
        "runs": runs,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
```

## 11. Machine-readable receipt

```json
{
  "environment": {
    "numpy": "2.3.5",
    "platform": "Linux-6.12.13-x86_64-with-glibc2.41",
    "python": "3.13.5",
    "scipy": "1.17.0"
  },
  "runs": [
    {
      "broad_fraction_final": 1.0,
      "broad_fraction_gt_0_99_first_step": 25,
      "max_amp_checkpoints": {
        "0": 0.7732120777033731,
        "100": 81655815657.27553,
        "125": 407159611806117.06,
        "150": 2.150288726031911e+18,
        "175": 1.1895417773311438e+22,
        "199": 4.775547602041418e+25,
        "25": 3.32374652225799,
        "50": 4823.545641983737,
        "75": 17940684.05239907
      },
      "max_amp_gt_1e3_first_step": 46,
      "old_curl_peak_abs_max": 8.490957133825106,
      "old_curl_peak_abs_median": 5.080748344766458,
      "old_curl_peak_jump_gt_10_count": 25,
      "old_curl_peak_jump_gt_30_count": 22,
      "old_curl_peak_max_jump": 148.51935900750448,
      "old_curl_peak_winding_exact_colocation_fraction": 0.02,
      "seed": 0,
      "true_winding_count_max": 4554,
      "true_winding_count_median": 134.0,
      "true_winding_count_min": 68
    },
    {
      "broad_fraction_final": 1.0,
      "broad_fraction_gt_0_99_first_step": 25,
      "max_amp_checkpoints": {
        "0": 0.7878693615492364,
        "100": 80712284308.64769,
        "125": 380975560058599.2,
        "150": 1.9333173851164186e+18,
        "175": 1.0726866856546551e+22,
        "199": 4.277664708178492e+25,
        "25": 3.571681138406603,
        "50": 5614.5873508067,
        "75": 18991078.148709457
      },
      "max_amp_gt_1e3_first_step": 45,
      "old_curl_peak_abs_max": 8.910680483541684,
      "old_curl_peak_abs_median": 5.124872916550039,
      "old_curl_peak_jump_gt_10_count": 25,
      "old_curl_peak_jump_gt_30_count": 21,
      "old_curl_peak_max_jump": 155.62133529821674,
      "old_curl_peak_winding_exact_colocation_fraction": 0.0,
      "seed": 1,
      "true_winding_count_max": 4566,
      "true_winding_count_median": 149.0,
      "true_winding_count_min": 72
    },
    {
      "broad_fraction_final": 1.0,
      "broad_fraction_gt_0_99_first_step": 25,
      "max_amp_checkpoints": {
        "0": 0.7470417142065005,
        "100": 77365705322.20493,
        "125": 404054118883166.5,
        "150": 2.2627562275067715e+18,
        "175": 1.282023916355568e+22,
        "199": 5.206738859764494e+25,
        "25": 3.5772395393274925,
        "50": 4809.265816824556,
        "75": 16586918.208914524
      },
      "max_amp_gt_1e3_first_step": 45,
      "old_curl_peak_abs_max": 8.922636403845097,
      "old_curl_peak_abs_median": 5.399576400994706,
      "old_curl_peak_jump_gt_10_count": 33,
      "old_curl_peak_jump_gt_30_count": 29,
      "old_curl_peak_max_jump": 140.8900280360537,
      "old_curl_peak_winding_exact_colocation_fraction": 0.0,
      "seed": 2,
      "true_winding_count_max": 4605,
      "true_winding_count_median": 140.5,
      "true_winding_count_min": 65
    },
    {
      "broad_fraction_final": 1.0,
      "broad_fraction_gt_0_99_first_step": 25,
      "max_amp_checkpoints": {
        "0": 0.7484532208104275,
        "100": 86479622942.79695,
        "125": 434557958864081.75,
        "150": 2.31745592984719e+18,
        "175": 1.274003299867184e+22,
        "199": 5.058588389444968e+25,
        "25": 3.556429697862706,
        "50": 5008.78194530257,
        "75": 18891649.15036906
      },
      "max_amp_gt_1e3_first_step": 45,
      "old_curl_peak_abs_max": 8.803385969848875,
      "old_curl_peak_abs_median": 5.816473813261631,
      "old_curl_peak_jump_gt_10_count": 46,
      "old_curl_peak_jump_gt_30_count": 42,
      "old_curl_peak_max_jump": 159.80613254815975,
      "old_curl_peak_winding_exact_colocation_fraction": 0.005,
      "seed": 3,
      "true_winding_count_max": 4677,
      "true_winding_count_median": 137.0,
      "true_winding_count_min": 60
    },
    {
      "broad_fraction_final": 1.0,
      "broad_fraction_gt_0_99_first_step": 24,
      "max_amp_checkpoints": {
        "0": 0.9337547001831207,
        "100": 91086654827.48177,
        "125": 487231282610436.75,
        "150": 2.7043491276657367e+18,
        "175": 1.5317585084354088e+22,
        "199": 6.209247049249283e+25,
        "25": 3.6747353175384063,
        "50": 5240.543896636618,
        "75": 19775488.151419163
      },
      "max_amp_gt_1e3_first_step": 45,
      "old_curl_peak_abs_max": 8.80306494418728,
      "old_curl_peak_abs_median": 6.192298502906343,
      "old_curl_peak_jump_gt_10_count": 56,
      "old_curl_peak_jump_gt_30_count": 44,
      "old_curl_peak_max_jump": 158.60012610335465,
      "old_curl_peak_winding_exact_colocation_fraction": 0.0,
      "seed": 4,
      "true_winding_count_max": 4587,
      "true_winding_count_median": 134.5,
      "true_winding_count_min": 62
    },
    {
      "broad_fraction_final": 1.0,
      "broad_fraction_gt_0_99_first_step": 25,
      "max_amp_checkpoints": {
        "0": 0.8819630068905941,
        "100": 97576210438.22916,
        "125": 462149072517450.5,
        "150": 2.325217072512101e+18,
        "175": 1.2167591918810572e+22,
        "199": 4.639562263114168e+25,
        "25": 3.933510466300347,
        "50": 5797.306105769631,
        "75": 20571699.3578604
      },
      "max_amp_gt_1e3_first_step": 44,
      "old_curl_peak_abs_max": 8.677472208299972,
      "old_curl_peak_abs_median": 5.673124438922678,
      "old_curl_peak_jump_gt_10_count": 30,
      "old_curl_peak_jump_gt_30_count": 26,
      "old_curl_peak_max_jump": 145.54037240532435,
      "old_curl_peak_winding_exact_colocation_fraction": 0.035,
      "seed": 5,
      "true_winding_count_max": 4560,
      "true_winding_count_median": 131.0,
      "true_winding_count_min": 66
    },
    {
      "broad_fraction_final": 1.0,
      "broad_fraction_gt_0_99_first_step": 25,
      "max_amp_checkpoints": {
        "0": 0.6871653086038178,
        "100": 86917211039.52896,
        "125": 437675748669011.2,
        "150": 2.27824607318561e+18,
        "175": 1.223207357103875e+22,
        "199": 4.8251818698665595e+25,
        "25": 3.4182396967027244,
        "50": 5016.916375322187,
        "75": 19153354.428204913
      },
      "max_amp_gt_1e3_first_step": 45,
      "old_curl_peak_abs_max": 9.024604857663043,
      "old_curl_peak_abs_median": 5.373194161299052,
      "old_curl_peak_jump_gt_10_count": 41,
      "old_curl_peak_jump_gt_30_count": 40,
      "old_curl_peak_max_jump": 171.1724276862369,
      "old_curl_peak_winding_exact_colocation_fraction": 0.0,
      "seed": 6,
      "true_winding_count_max": 4614,
      "true_winding_count_median": 121.0,
      "true_winding_count_min": 62
    },
    {
      "broad_fraction_final": 1.0,
      "broad_fraction_gt_0_99_first_step": 24,
      "max_amp_checkpoints": {
        "0": 0.8186518179712606,
        "100": 105646854019.2523,
        "125": 521797513211914.2,
        "150": 2.7774487210140667e+18,
        "175": 1.5102974927913825e+22,
        "199": 6.008666960662738e+25,
        "25": 3.4690063079844783,
        "50": 5400.68163427684,
        "75": 20876004.55347926
      },
      "max_amp_gt_1e3_first_step": 45,
      "old_curl_peak_abs_max": 8.829369525009203,
      "old_curl_peak_abs_median": 5.784650822307129,
      "old_curl_peak_jump_gt_10_count": 45,
      "old_curl_peak_jump_gt_30_count": 35,
      "old_curl_peak_max_jump": 136.74063039199433,
      "old_curl_peak_winding_exact_colocation_fraction": 0.005,
      "seed": 7,
      "true_winding_count_max": 4612,
      "true_winding_count_median": 131.0,
      "true_winding_count_min": 61
    }
  ],
  "smooth_phase_negative_control": {
    "old_curl_abs_max": 4.71238898038469,
    "old_curl_cells_abs_gt_0_1": 847,
    "phase_safe_winding_abs_max": 1.4135798584282297e-16,
    "phase_safe_winding_cells_abs_gt_0_5": 0
  },
  "summary": {
    "first_step_mask_gt_0_15_covers_gt_99pct": {
      "max": 25,
      "median": 25.0,
      "min": 24,
      "values": [
        25,
        25,
        25,
        25,
        24,
        25,
        25,
        24
      ]
    },
    "first_step_max_abs_psi_gt_1e3": {
      "max": 46,
      "median": 45.0,
      "min": 44,
      "values": [
        46,
        45,
        45,
        45,
        45,
        44,
        45,
        45
      ]
    },
    "median_max_abs_psi_by_step": {
      "0": 0.8264850792300878,
      "100": 88783138885.13936,
      "125": 448353515690766.1,
      "150": 2.3213365011796454e+18,
      "175": 1.278013608111376e+22,
      "199": 5.132663624604731e+25,
      "25": 3.5640554181346547,
      "50": 5320.612429203005,
      "75": 19072216.288457185
    },
    "old_curl_peak_exact_winding_colocation_fraction": {
      "max": 0.035,
      "median": 0.0025,
      "min": 0.0,
      "values": [
        0.02,
        0.0,
        0.0,
        0.005,
        0.0,
        0.035,
        0.0,
        0.005
      ]
    },
    "old_curl_peak_jump_gt_10_per_run": [
      25,
      25,
      33,
      46,
      56,
      30,
      41,
      45
    ],
    "old_curl_peak_jump_gt_30_per_run": [
      22,
      21,
      29,
      42,
      44,
      26,
      40,
      35
    ],
    "old_curl_peak_max_jump": {
      "max": 171.1724276862369,
      "median": 152.07034715286062,
      "min": 136.74063039199433
    },
    "seeds": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7
    ],
    "true_winding_count_median_across_time_per_run": [
      134.0,
      149.0,
      140.5,
      137.0,
      134.5,
      131.0,
      121.0,
      131.0
    ]
  }
}
```