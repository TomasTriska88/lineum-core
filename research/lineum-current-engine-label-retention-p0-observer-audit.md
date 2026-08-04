# Lineum Label-Retention P0 Observer Audit

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** pre-dynamics known-answer audit of the two frozen structural-label observers used by the current-engine label-retention programme  
**Central question:** do the preregistered observers distinguish the equal-energy horizontal and vertical source families on held-out nuisance cases without class imbalance or transpose inconsistency?  
**Current confidence:** high that the observer mathematics passed in the available NumPy 2.3.5 environment; official P0 gate remains unresolved because the environment violates the repository NumPy `<2.0.0` requirement

## 1. Report lineage

Root programme:

- `research/lineum-native-field-stress-tests.md`;
- inherited root version: `0.2.1`;
- evidence cutoff: `2026-08-04`.

Cross-question synthesis:

- `research/lineum-cross-question-emergence-synthesis.md`;
- inherited version: `0.1.0`;
- commit: `9f1b9f38b1e65e1cebd4f65cbdc769195c779448`.

Immediate parent protocol:

- `research/lineum-current-engine-label-retention-test.md`;
- inherited version: `0.1.0`;
- commit: `11e08efd53cfcc22072a7301107b30b91bb73df5`;
- parent report blob SHA: `827d312e3826f26dbab4303da482b38bf337e41c`.

Repository checkpoint before this report:

- repository: `TomasTriska88/lineum-core`;
- branch: `develop`;
- head: `11e08efd53cfcc22072a7301107b30b91bb73df5`.

## 2. Purpose and hard boundary

P0 audits only the readout mathematics on pristine known-answer arrays.

It does not execute:

- the current Lineum engine;
- the standalone dynamic snapshot;
- `phi` or `mu` accumulation;
- source-off relaxation;
- causal echo;
- cap, timestep, or resolution lanes;
- any galaxy, cosmology, compact-object, or physical-information mapping.

A P0 pass means only that the selected observers can identify the deliberately simple orientation label before dynamics are introduced.

## 3. Frozen known-answer construction

The audit uses the exact parent-protocol family:

- square grid `N = 64`;
- separations `10`, `12`, and `14` cells;
- Gaussian widths `2.5` and `3.5` cells;
- integer shifts `(-3, -2)`, `(-2, 3)`, `(0, 0)`, `(2, -3)`, and `(3, 2)`;
- horizontal label `A` and vertical label `B`;
- independent normalization to unit total `sum(abs(psi)^2)`;
- `30` nuisance variants and `60` labelled arrays;
- training variants where index modulo `3` is `0` or `1`;
- held-out variants where index modulo `3` is `2`;
- both labels for one nuisance tuple remain in the same split.

## 4. Frozen observers

### 4.1 Centroid-corrected quadrupole

For nonnegative weights `F`:

`Q(F) = sum(F ((x - x_c)^2 - (y - y_c)^2)) / [sum(F ((x - x_c)^2 + (y - y_c)^2)) + 1e-30]`.

Predictions:

- `Q > 1e-6` -> label `A`;
- `Q < -1e-6` -> label `B`;
- otherwise unclassified and therefore incorrect.

### 4.2 Independent pooled-field nearest-centroid observer

Each field is:

1. recentered to its nearest integer weighted centroid;
2. normalized by its `L2` norm;
3. pooled into an `8 x 8` feature grid;
4. compared by Euclidean distance with two class centroids built from training variants only.

This observer does not call or reuse the quadrupole score.

### 4.3 Permutation null

Each observer uses `2000` deterministic label permutations.

The one-sided p-value is:

`p = (1 + number(null_accuracy >= observed_accuracy)) / 2001`.

## 5. Parent P0 gates

The parent protocol requires:

- held-out balanced accuracy `>= 0.95` for both observers;
- permutation p-value `<= 0.01` for both observers;
- maximum quadrupole transpose antisymmetry error `<= 1e-12`;
- class-accuracy imbalance `<= 0.05`;
- maximum relative equal-energy error `<= 1e-14`.

The parent environment requirement is:

- Python `>= 3.10`;
- NumPy `>= 1.24, < 2.0.0`.

## 6. Exact execution

### 6.1 Script path

Temporary local path:

`.scratch/lineum-p0-audit.py`

The actual container path was `/mnt/data/lineum-p0-audit.py` because no repository checkout was available. This temporary path is not evidence. The complete script is embedded in Section 11.

### 6.2 Script fingerprint

SHA-256:

`a06272712465b11b5ed1c9f80e9db86be570bd57c049fb6754d32580cfcf386d`

Line count:

`272`.

### 6.3 Command

`python3 /mnt/data/lineum-p0-audit.py > /mnt/data/lineum-p0-output.json`

### 6.4 Output fingerprint

SHA-256:

`712ccf4a6b242f3d3cc511132257485dda267971d04af64d95a641343e036d26`

## 7. Environment receipt

- Python: `3.13.5`;
- NumPy: `2.3.5`;
- platform: `Linux-6.12.13-x86_64-with-glibc2.41`;
- machine: `x86_64`;
- processor string: empty in the available runtime.

Environment verdict:

`invalid_for_official_parent_gate`.

Reason:

NumPy `2.3.5` is outside the repository requirement `>=1.24,<2.0.0`.

## 8. Attempted compliant environment restoration

### 8.1 Command

`python3 -m venv /mnt/data/lineum-p0-venv && /mnt/data/lineum-p0-venv/bin/python -m pip install --disable-pip-version-check --no-input 'numpy==1.26.4'`

### 8.2 Result

The configured package source returned:

`ERROR: Could not find a version that satisfies the requirement numpy==1.26.4 (from versions: none)`

and:

`ERROR: No matching distribution found for numpy==1.26.4`.

No retry, alternate external package index, or unverified binary installation was attempted.

## 9. Machine-readable result

```json
{
  "environment": {
    "machine": "x86_64",
    "numpy": "2.3.5",
    "platform": "Linux-6.12.13-x86_64-with-glibc2.41",
    "processor": "",
    "python": "3.13.5 (main, May  5 2026, 21:05:52) [GCC 14.2.0]"
  },
  "max_quadrupole_transpose_antisymmetry_error": 1.1102230246251565e-16,
  "max_relative_energy_difference": 4.440892098500626e-16,
  "minimum_absolute_heldout_quadrupole": 0.6436406050680992,
  "n_test": 20,
  "n_train": 40,
  "n_trajectories": 60,
  "n_variants": 30,
  "pooled_balanced_accuracy": 1.0,
  "pooled_class_A_accuracy": 1.0,
  "pooled_class_B_accuracy": 1.0,
  "pooled_permutation_p": 0.0004997501249375312,
  "quadrupole_balanced_accuracy": 1.0,
  "quadrupole_class_A_accuracy": 1.0,
  "quadrupole_class_B_accuracy": 1.0,
  "quadrupole_permutation_p": 0.0004997501249375312,
  "source_sha256": "a06272712465b11b5ed1c9f80e9db86be570bd57c049fb6754d32580cfcf386d"
}
```

## 10. Interpretation

### 10.1 What the available run observed

Within NumPy `2.3.5`:

- all `20` held-out labelled arrays were classified correctly by the quadrupole observer;
- all `20` held-out labelled arrays were classified correctly by the independent pooled-field observer;
- both class-specific accuracies were `1.0` for both observers;
- both permutation p-values reached the minimum attainable value under `2000` permutations, approximately `0.00049975`;
- the largest equal-energy mismatch was about `4.44e-16`, far below the `1e-14` gate;
- the largest transpose antisymmetry error was about `1.11e-16`, far below the `1e-12` gate;
- the weakest held-out absolute quadrupole score was about `0.644`, far from the `1e-6` unclassified threshold.

### 10.2 Narrow provisional conclusion

The two observers are internally consistent and strongly separate the deliberately simple known-answer orientation family in the available runtime.

Status:

`observer_math_provisionally_passed_in_noncompliant_environment`.

### 10.3 Why the official gate remains unresolved

The preregistered environment gate was not satisfied. The result cannot be promoted to an official P0 pass without reproduction using an allowed NumPy `<2.0.0` environment.

No Lineum dynamics may be interpreted from this checkpoint because none were executed.

## 11. Exact executable script

```python
from __future__ import annotations

import hashlib
import json
import math
import platform
import sys

import numpy as np

SEED = 20260804
LABEL_A = 0
LABEL_B = 1


def coordinates(size: int):
    axis = np.arange(size, dtype=np.float64) - (size - 1) / 2.0
    return np.meshgrid(axis, axis, indexing="xy")


def normalize_energy(amplitude: np.ndarray) -> np.ndarray:
    energy = float(np.sum(np.abs(amplitude) ** 2))
    if energy <= 0.0:
        raise ValueError("Amplitude must carry positive energy")
    return np.asarray(amplitude, dtype=np.complex128) / math.sqrt(energy)


def make_orientation_pair(
    size: int,
    separation: float,
    width: float,
    shift_x: int,
    shift_y: int,
):
    x, y = coordinates(size)

    def gaussian(dx, dy):
        return np.exp(-(dx * dx + dy * dy) / (2.0 * width * width))

    horizontal = gaussian(x - separation / 2.0, y) + gaussian(
        x + separation / 2.0, y
    )
    vertical = gaussian(x, y - separation / 2.0) + gaussian(
        x, y + separation / 2.0
    )
    horizontal = np.roll(horizontal, (shift_y, shift_x), axis=(0, 1))
    vertical = np.roll(vertical, (shift_y, shift_x), axis=(0, 1))
    return normalize_energy(horizontal), normalize_energy(vertical)


def quadrupole_score(weight: np.ndarray) -> float:
    field = np.maximum(np.asarray(weight, dtype=np.float64), 0.0)
    total = float(np.sum(field))
    if total <= 0.0:
        return 0.0
    x, y = coordinates(field.shape[0])
    cx = float(np.sum(field * x) / total)
    cy = float(np.sum(field * y) / total)
    dx = x - cx
    dy = y - cy
    denominator = float(np.sum(field * (dx * dx + dy * dy))) + 1e-30
    return float(np.sum(field * (dx * dx - dy * dy)) / denominator)


def recenter_integer(weight: np.ndarray) -> np.ndarray:
    field = np.maximum(np.asarray(weight, dtype=np.float64), 0.0)
    total = float(np.sum(field))
    if total <= 0.0:
        return field.copy()
    x, y = coordinates(field.shape[0])
    cx = float(np.sum(field * x) / total)
    cy = float(np.sum(field * y) / total)
    return np.roll(
        field,
        (-int(round(cy)), -int(round(cx))),
        axis=(0, 1),
    )


def pooled_feature(weight: np.ndarray, pooled_size: int = 8) -> np.ndarray:
    field = recenter_integer(weight)
    norm = float(np.linalg.norm(field))
    if norm <= 0.0:
        return np.zeros(pooled_size * pooled_size, dtype=np.float64)
    field = field / norm
    size = field.shape[0]
    if size % pooled_size != 0:
        raise ValueError("Grid size must be divisible by pooled_size")
    block = size // pooled_size
    pooled = field.reshape(
        pooled_size, block, pooled_size, block
    ).mean(axis=(1, 3))
    return pooled.ravel()


def balanced_accuracy(labels: np.ndarray, predictions: np.ndarray) -> float:
    scores = []
    for label in (LABEL_A, LABEL_B):
        mask = labels == label
        if not np.any(mask):
            raise ValueError("Both classes are required")
        scores.append(float(np.mean(predictions[mask] == labels[mask])))
    return 0.5 * sum(scores)


def nearest_centroid_predictions(
    train_features: np.ndarray,
    train_labels: np.ndarray,
    test_features: np.ndarray,
) -> np.ndarray:
    centroids = np.stack(
        [
            np.mean(train_features[train_labels == label], axis=0)
            for label in (LABEL_A, LABEL_B)
        ]
    )
    distances = np.linalg.norm(
        test_features[:, None, :] - centroids[None, :, :],
        axis=2,
    )
    return np.argmin(distances, axis=1)


def permutation_p_value(
    labels: np.ndarray,
    predictions: np.ndarray,
    rng: np.random.Generator,
    permutations: int = 2000,
) -> float:
    observed = balanced_accuracy(labels, predictions)
    exceed = 0
    for _ in range(permutations):
        shuffled = rng.permutation(labels)
        if balanced_accuracy(shuffled, predictions) >= observed:
            exceed += 1
    return (1.0 + exceed) / (permutations + 1.0)


def nuisance_schedule():
    return [
        (separation, width, shift_x, shift_y)
        for separation in (10.0, 12.0, 14.0)
        for width in (2.5, 3.5)
        for shift_x, shift_y in (
            (-3, -2),
            (-2, 3),
            (0, 0),
            (2, -3),
            (3, 2),
        )
    ]


def run_p0() -> dict:
    schedule = nuisance_schedule()
    labels = []
    variant_ids = []
    fields = []
    energy_differences = []
    antisymmetry_errors = []

    for variant_id, params in enumerate(schedule):
        psi_a, psi_b = make_orientation_pair(64, *params)
        energy_a = float(np.sum(np.abs(psi_a) ** 2))
        energy_b = float(np.sum(np.abs(psi_b) ** 2))
        energy_differences.append(
            abs(energy_a - energy_b) / max(energy_a, energy_b)
        )
        for label, psi in ((LABEL_A, psi_a), (LABEL_B, psi_b)):
            labels.append(label)
            variant_ids.append(variant_id)
            fields.append(np.abs(psi) ** 2)

    for separation in (10.0, 12.0, 14.0):
        for width in (2.5, 3.5):
            psi_a, psi_b = make_orientation_pair(
                64, separation, width, 0, 0
            )
            antisymmetry_errors.append(
                abs(
                    quadrupole_score(np.abs(psi_a) ** 2)
                    + quadrupole_score(np.abs(psi_b) ** 2)
                )
            )

    labels = np.asarray(labels, dtype=np.int64)
    variant_ids = np.asarray(variant_ids, dtype=np.int64)
    fields = np.stack(fields)

    variant_index = np.arange(len(schedule))
    train_variants = variant_index % 3 != 2
    test_variants = ~train_variants
    train_mask = train_variants[variant_ids]
    test_mask = test_variants[variant_ids]

    q_scores = np.asarray([quadrupole_score(field) for field in fields])
    q_predictions = np.full(len(fields), -1, dtype=np.int64)
    q_predictions[q_scores > 1e-6] = LABEL_A
    q_predictions[q_scores < -1e-6] = LABEL_B

    features = np.stack([pooled_feature(field) for field in fields])
    pooled_predictions = nearest_centroid_predictions(
        features[train_mask],
        labels[train_mask],
        features[test_mask],
    )

    q_test_predictions = q_predictions[test_mask]
    test_labels = labels[test_mask]

    result = {
        "n_variants": len(schedule),
        "n_trajectories": len(labels),
        "n_train": int(train_mask.sum()),
        "n_test": int(test_mask.sum()),
        "max_relative_energy_difference": float(max(energy_differences)),
        "max_quadrupole_transpose_antisymmetry_error": float(
            max(antisymmetry_errors)
        ),
        "quadrupole_balanced_accuracy": balanced_accuracy(
            test_labels, q_test_predictions
        ),
        "quadrupole_class_A_accuracy": float(
            np.mean(q_test_predictions[test_labels == LABEL_A] == LABEL_A)
        ),
        "quadrupole_class_B_accuracy": float(
            np.mean(q_test_predictions[test_labels == LABEL_B] == LABEL_B)
        ),
        "quadrupole_permutation_p": permutation_p_value(
            test_labels,
            q_test_predictions,
            np.random.default_rng(SEED + 1),
        ),
        "pooled_balanced_accuracy": balanced_accuracy(
            test_labels, pooled_predictions
        ),
        "pooled_class_A_accuracy": float(
            np.mean(pooled_predictions[test_labels == LABEL_A] == LABEL_A)
        ),
        "pooled_class_B_accuracy": float(
            np.mean(pooled_predictions[test_labels == LABEL_B] == LABEL_B)
        ),
        "pooled_permutation_p": permutation_p_value(
            test_labels,
            pooled_predictions,
            np.random.default_rng(SEED + 2),
        ),
        "minimum_absolute_heldout_quadrupole": float(
            np.min(np.abs(q_scores[test_mask]))
        ),
        "environment": {
            "python": sys.version,
            "numpy": np.__version__,
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": platform.processor(),
        },
    }
    return result


def main() -> None:
    source_path = __file__
    with open(source_path, "rb") as handle:
        source_sha256 = hashlib.sha256(handle.read()).hexdigest()
    result = run_p0()
    result["source_sha256"] = source_sha256
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
```

## 12. Pre-dynamics protocol defects discovered during audit

No engine dynamics were executed because two parent-code discrepancies were found before the dynamic gate.

### 12.1 P0 stage is not dispatched by the parent executable

The parent report describes P0 but its embedded `main()` directly calls the full primary dynamic run. It does not provide a P0-only function or stage selector.

Impact:

- the P0 audit required the standalone script embedded here;
- the parent executable must be amended before extraction so that P0 can run without accidentally starting dynamics.

Required correction:

- add an explicit `run_p0()` path;
- add a stage selector whose default cannot silently bypass P0;
- preserve the present P0 script and result as the frozen audit record.

### 12.2 Cap-raised lane does not repeat the imprint under the raised cap

The parent prose states that the cap-raised control repeats the passive and causal lanes with `mu_cap = 100`.

The parent embedded code currently:

- imprints all states under the primary `mu_cap = 10`;
- raises the cap only during source-off or causal continuation.

This does not fully test whether cap choice influenced accumulation during imprint.

Required correction before dynamics:

- generate an independently imprinted `mu_cap = 100` trajectory;
- compare both imprint and post-imprint states;
- retain the current partial lane only as a post-imprint cap sensitivity subcontrol.

This discrepancy was discovered before any dynamic output and therefore does not invalidate a result; it blocks execution until corrected.

## 13. Root-programme impact matrix

| Root item | P0 impact |
|---|---|
| Q1 galactic radial response | `unaffected`; no dynamics or radial observable executed |
| Q2 attraction and saturation | `constrains` protocol only; cap-control defect was found before execution |
| Q3 information retention | `supports` observer readiness provisionally; official environment gate unresolved |
| Current `phi` or `mu` memory | `not_yet_compared`; no fields were evolved |
| Historical Eq-11 | `not_yet_compared` |
| Public TOLOG information language | `constrains`: the programme now has explicit held-out readouts rather than an invariant-node percentage |
| Physical information in nature | `unaffected` |

## 14. Next gate

Before any Lineum dynamic run:

1. reproduce P0 in a NumPy `>=1.24,<2.0.0` environment;
2. amend the parent executable to expose an explicit P0-only stage;
3. correct the cap-raised imprint lane;
4. verify the amended parent report and source fingerprint;
5. perform the active-Core versus standalone one-step and ten-step adapter comparison;
6. execute the primary `N = 64` dynamics only if every preceding gate passes.

No parameter, threshold, observer, split, or label may be changed in response to the provisional P0 outcome.

## 15. Prohibited conclusions

This checkpoint does not establish that:

- the official P0 gate passed;
- `phi` or `mu` retains information;
- the Lineum engine was executed;
- a passive record exists;
- a causal echo exists;
- a cap-independent mechanism exists;
- Lineum has an attractor;
- Lineum explains galaxy dynamics;
- a numerical orientation label corresponds to physical information in the universe.

## 16. ClickUp status

No ClickUp call was made. The previously reported rolling limit remains the last known connector state.

`ClickUp mode = unsynchronized`.

## 17. Execution log

1. Ran the frozen P0 observer mathematics on `30` nuisance pairs and `20` held-out labelled arrays.
2. Both observers achieved perfect held-out balanced accuracy with balanced class performance and minimum permutation p-values.
3. Equal-energy and transpose-antisymmetry checks passed by wide margins.
4. Detected that NumPy `2.3.5` violates the repository dependency declaration.
5. Attempted one isolated installation of NumPy `1.26.4`; the configured package source exposed no matching version.
6. Preserved the P0 result as provisional rather than silently accepting an invalid environment.
7. Found two parent-protocol implementation discrepancies before any dynamics: absent P0-only dispatch and incomplete cap-raised imprint control.
8. No Lineum engine dynamics, production-code change, whitepaper change, observational fit, or physical claim was executed.
