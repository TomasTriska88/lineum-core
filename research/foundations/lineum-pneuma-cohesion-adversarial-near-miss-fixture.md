# Pneuma-Inspired Cohesion Observer Adversarial Near-Miss Fixture

**Status:** validated known-answer adversarial fixture; no Lineum application executed  
**Version:** 0.2.0  
**Evidence cutoff:** 2026-08-01  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`  
**Recovered root version:** 0.4.14  
**Root evidence cutoff:** 2026-07-29  
**Root blob SHA:** `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, version 0.3.0, blob `5304874451caf32313ad0e8e3c59e53958698d79`  
**Conceptual predecessor:** `research/foundations/lineum-gnostic-enochic-dead-sea-scrolls-metaphor-audit.md`, version 0.2.0, blob `aa7895df7e66ff348159c8ecbb6d06a92f22950c`  
**Immediate predecessor:** `research/foundations/lineum-pneuma-cohesion-observer-fixture.md`, version 0.2.0, blob `2cc957d7d40907a092f8762bb73ccff7bfdf7e70`  
**Object-definition predecessor:** `research/foundations/lineum-core-envelope-wake-and-attraction-preregistration.md`, version 0.2.0, blob `621cc5f9147dde4a3819e9fc2d3febe05e387cf8`  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Scope:** Validate a permutation-invariant and source-aware observer of synthetic mechanical cohesion against difficult near-miss controls.  
**Central question:** Can internal restoring organization be distinguished from interaction, rigidity, radial compaction, visual persistence, historical preparation, and active external maintenance without using permanent member labels?  
**Current confidence:** high that the frozen observer passed the declared synthetic cases and timestep controls; low that it will transfer unchanged to continuous Lineum fields; no evidence yet for a Lineum collective particle, P2 cohesion, physical pneuma, soul, or ancient encoded physics.

## 1. Answer first

The adversarial fixture passed every frozen gate.

The observer accepted internally restoring, source-off systems even after arbitrary member relabeling. It rejected systems that merely collided, froze around the damaged geometry, restored only their radius, translated rigidly, had been organized only in the past, or were actively repaired by an external template.

```text
confirmatory trajectories:              324
internally cohesive positives accepted: 108 / 108
near-miss controls rejected:            216 / 216
false positives:                         0
false negatives:                         0
classification changes across dt:        0
```

The most important control was the active external template. It restored the pair geometry by more than `99.5%` and the relational spectrum by more than `99.8%`, yet the observer rejected it because the organizing source remained active. This demonstrates that geometric recovery and source-off autonomy are separate requirements.

The result validates synthetic **mechanical cohesion**, not collective identity under member birth, death, exchange, copying, or heredity.

## 2. Version history and preregistration receipt

Version 0.1.0 was committed before confirmatory execution:

```text
preregistration commit: 51990040f224fa7ddb89d61845476928dc969b2b
exploratory seeds excluded from validation: 0..19
held-out confirmatory seeds: 400..411
integration steps: 0.01, 0.005, 0.0025
horizon: 6.0
thresholds, cases, and expected classifications: frozen
```

Confirmatory execution did not change any threshold, force law, case, seed, horizon, observer, or decision rule. Because of the execution-time limit, the three timestep blocks were evaluated separately with the same frozen functions and then combined in the exact preregistered row order before one joint verification and digest calculation.

## 3. Historical inspiration and scientific translation

The source-critical parent audit extracted from Stoic pneuma only the systems question of inward/outward organization and body-forming tensility. The operational translation was:

> Does a whole exhibit a source-off internal restoring response that recovers relational organization while preserving free bulk motion?

`Pneuma-inspired` records hypothesis provenance. No `pneuma` variable, ancient ontology, or physical correspondence is introduced.

## 4. Known-answer classes

| Case | Causal construction | Frozen expected verdict |
|---|---|---|
| `elastic` | Sparse internal springs restore reference relations | cohesive |
| `elastic_relabelled` | Same state and graph after consistent random member relabeling | cohesive |
| `shape_memory_complete` | Internal all-pair reference rest lengths | cohesive mechanically |
| `repulsive_gas` | Short-range interaction without reference memory | not cohesive |
| `deformed_glass` | Stiff network whose equilibrium is the damaged state | not cohesive |
| `radial_restorer` | Restores scale but not pair organization | not cohesive |
| `rigid_advected` | Persistent co-moving image without restoring force | not cohesive |
| `external_removed` | Historically prepared, organizer absent during challenge | not cohesive |
| `external_template_active` | Excellent repair driven by an active external template | not cohesive |

The complete shape-memory network is a true positive for mechanical cohesion, but it is explicitly not evidence of emergent identity or robustness to member turnover.

## 5. Frozen geometry, dynamics, and observer

For `N = 16`, the deterministic reference is

```text
theta_i = 2 pi i / 16
r_i = 1 + 0.12 cos(3 theta_i) + 0.05 sin(5 theta_i)
R_i = [r_i cos(theta_i), r_i sin(theta_i)].
```

The challenge is

```text
X_i(0) = A R_i + eta_i
A = [[1.25, 0.10],
     [0.02, 0.75]]
eta_i ~ Normal(0, 0.035^2 I)
v_bulk = [0.30, -0.15].
```

Integration uses semi-implicit Euler. Internal pair forces are equal and opposite, and all damping acts only on velocity relative to the center-of-mass velocity.

The observer uses no permanent member correspondence.

### 5.1 Pair-distance error

```text
E_pair(X) = RMS(sort(d(X)) - sort(d_ref)) / mean(d_ref).
```

### 5.2 Relational kernel-spectrum error

```text
K_ij = exp(-|X_i-X_j|^2 / (2 sigma^2)),
sigma = median reference pair distance,
E_spec(X) = RMS(sort(eig(K)) - sort(eig(K_ref))) / RMS(eig(K_ref)).
```

### 5.3 Frozen gates

At `t_early = 0.25` and `T = 6.0`:

```text
G_challenge   = E_pair(0) > 0.05
G_early_pair  = [E_pair(0)-E_pair(t_early)] / E_pair(0) > 0.05
G_early_spec  = [E_spec(0)-E_spec(t_early)] / E_spec(0) > 0.03
G_pair        = [E_pair(0)-E_pair(T)] / E_pair(0) > 0.80
G_spec        = [E_spec(0)-E_spec(T)] / E_spec(0) > 0.80
G_source_off  = no external organizer active during challenge
G_bulk        = |mean(v(T))-v_bulk| < 1e-8
G_bounded     = max_t R_rms(t) < 1.8 R_ref
                and 0.6 < R_rms(T)/R_ref < 1.4
```

```text
cohesive = all eight gates pass.
```

## 6. Complete executable verification code

```python
import hashlib
import json
import numpy as np

N = 16
SEEDS = list(range(400, 412))
DTS = [0.01, 0.005, 0.0025]
T_FINAL = 6.0
T_EARLY = 0.25
CASES = [
    "elastic",
    "elastic_relabelled",
    "shape_memory_complete",
    "repulsive_gas",
    "deformed_glass",
    "radial_restorer",
    "rigid_advected",
    "external_removed",
    "external_template_active",
]
POSITIVE_CASES = ["elastic", "elastic_relabelled", "shape_memory_complete"]
BULK = np.array([0.30, -0.15], dtype=float)


def reference_shape(n=N):
    theta = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    radius = 1.0 + 0.12 * np.cos(3.0 * theta) + 0.05 * np.sin(5.0 * theta)
    return np.column_stack((radius * np.cos(theta), radius * np.sin(theta)))


def sparse_edges(n=N):
    edges = set()
    for i in range(n):
        for offset in (1, 2, 5):
            edges.add(tuple(sorted((i, (i + offset) % n))))
    return sorted(edges)


def complete_edges(n=N):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


REF = reference_shape()
SPARSE = sparse_edges()
COMPLETE = complete_edges()
REST_SPARSE = np.asarray([np.linalg.norm(REF[j] - REF[i]) for i, j in SPARSE])
REST_COMPLETE = np.asarray([np.linalg.norm(REF[j] - REF[i]) for i, j in COMPLETE])


def initial_state(seed):
    rng = np.random.default_rng(seed)
    transform = np.array([[1.25, 0.10], [0.02, 0.75]], dtype=float)
    x = REF @ transform.T + rng.normal(scale=0.035, size=REF.shape)
    x -= x.mean(axis=0)
    v = np.repeat(BULK[None, :], N, axis=0)
    return x, v


def pair_distances(x):
    return np.asarray([
        np.linalg.norm(x[j] - x[i])
        for i in range(N)
        for j in range(i + 1, N)
    ])


REF_PAIR = np.sort(pair_distances(REF))
SIGMA = float(np.median(REF_PAIR))


def pair_error(x):
    observed = np.sort(pair_distances(x))
    return float(np.sqrt(np.mean((observed - REF_PAIR) ** 2)) / np.mean(REF_PAIR))


def kernel_spectrum(x):
    difference = x[:, None, :] - x[None, :, :]
    distance_squared = np.sum(difference * difference, axis=2)
    kernel = np.exp(-distance_squared / (2.0 * SIGMA * SIGMA))
    return np.sort(np.linalg.eigvalsh(kernel))


REF_SPECTRUM = kernel_spectrum(REF)


def spectrum_error(x):
    observed = kernel_spectrum(x)
    numerator = np.sqrt(np.mean((observed - REF_SPECTRUM) ** 2))
    denominator = np.sqrt(np.mean(REF_SPECTRUM ** 2))
    return float(numerator / denominator)


def rms_radius(x):
    centered = x - x.mean(axis=0)
    return float(np.sqrt(np.mean(np.sum(centered * centered, axis=1))))


REF_RADIUS = rms_radius(REF)


def spring_forces(x, v, edges, rest_lengths, stiffness, damping):
    forces = np.zeros_like(x)
    for index, (i, j) in enumerate(edges):
        delta = x[j] - x[i]
        distance = float(np.sqrt(np.dot(delta, delta)))
        if distance > 1e-12:
            force = stiffness * (distance - rest_lengths[index]) * delta / distance
            forces[i] += force
            forces[j] -= force
    forces += -damping * (v - v.mean(axis=0))
    return forces


def repulsive_forces(x, v):
    forces = np.zeros_like(x)
    cutoff = 0.55
    stiffness = 2.0
    for i, j in COMPLETE:
        delta = x[j] - x[i]
        distance = float(np.sqrt(np.dot(delta, delta)))
        if 1e-12 < distance < cutoff:
            force = -stiffness * (cutoff - distance) * delta / distance
            forces[i] += force
            forces[j] -= force
    forces += -0.5 * (v - v.mean(axis=0))
    return forces


def radial_forces(x, v):
    centered = x - x.mean(axis=0)
    radius = np.linalg.norm(centered, axis=1)
    forces = np.zeros_like(x)
    for i in range(N):
        if radius[i] > 1e-12:
            forces[i] += -4.0 * (radius[i] - REF_RADIUS) * centered[i] / radius[i]
    forces -= forces.mean(axis=0)
    forces += -2.0 * (v - v.mean(axis=0))
    return forces


def external_template_forces(x, v):
    centered = x - x.mean(axis=0)
    forces = -4.0 * (centered - REF)
    forces -= forces.mean(axis=0)
    forces += -2.0 * (v - v.mean(axis=0))
    return forces


def relabel_state(x, v, seed):
    rng = np.random.default_rng(seed + 9999)
    permutation = rng.permutation(N)
    x_new = x[permutation]
    v_new = v[permutation]
    old_to_new = {old: new for new, old in enumerate(permutation)}
    mapped = [tuple(sorted((old_to_new[i], old_to_new[j]))) for i, j in SPARSE]
    pairs = sorted(zip(mapped, REST_SPARSE), key=lambda item: item[0])
    edges_new = [item[0] for item in pairs]
    rest_new = np.asarray([item[1] for item in pairs])
    return x_new, v_new, edges_new, rest_new


def simulate(case, seed, dt):
    x, v = initial_state(seed)
    sparse = SPARSE
    sparse_rest = REST_SPARSE
    source_off = True

    if case == "elastic_relabelled":
        x, v, sparse, sparse_rest = relabel_state(x, v, seed)

    glass_rest = None
    if case == "deformed_glass":
        glass_rest = np.asarray([np.linalg.norm(x[j] - x[i]) for i, j in SPARSE])

    pair_0 = pair_error(x)
    spectrum_0 = spectrum_error(x)
    pair_early = None
    spectrum_early = None
    maximum_radius = rms_radius(x)

    steps = int(round(T_FINAL / dt))
    early_step = int(round(T_EARLY / dt))

    for step in range(steps):
        if case in ("elastic", "elastic_relabelled"):
            forces = spring_forces(x, v, sparse, sparse_rest, 4.0, 2.0)
        elif case == "shape_memory_complete":
            forces = spring_forces(x, v, COMPLETE, REST_COMPLETE, 0.5, 2.0)
        elif case == "repulsive_gas":
            forces = repulsive_forces(x, v)
        elif case == "deformed_glass":
            forces = spring_forces(x, v, SPARSE, glass_rest, 4.0, 2.0)
        elif case == "radial_restorer":
            forces = radial_forces(x, v)
        elif case in ("rigid_advected", "external_removed"):
            forces = np.zeros_like(x)
        elif case == "external_template_active":
            source_off = False
            forces = external_template_forces(x, v)
        else:
            raise ValueError(case)

        v += dt * forces
        x += dt * v
        maximum_radius = max(maximum_radius, rms_radius(x))

        if step + 1 == early_step:
            pair_early = pair_error(x)
            spectrum_early = spectrum_error(x)

    pair_final = pair_error(x)
    spectrum_final = spectrum_error(x)
    recovery_pair_early = (pair_0 - pair_early) / pair_0
    recovery_spectrum_early = (spectrum_0 - spectrum_early) / spectrum_0
    recovery_pair = (pair_0 - pair_final) / pair_0
    recovery_spectrum = (spectrum_0 - spectrum_final) / spectrum_0
    bulk_error = float(np.linalg.norm(v.mean(axis=0) - BULK))
    final_radius_ratio = rms_radius(x) / REF_RADIUS
    bounded = bool(maximum_radius < 1.8 * REF_RADIUS and 0.6 < final_radius_ratio < 1.4)

    cohesive = bool(
        pair_0 > 0.05
        and recovery_pair_early > 0.05
        and recovery_spectrum_early > 0.03
        and recovery_pair > 0.80
        and recovery_spectrum > 0.80
        and source_off
        and bulk_error < 1e-8
        and bounded
    )

    return {
        "case": case,
        "seed": seed,
        "dt": dt,
        "pair_0": float(pair_0),
        "spectrum_0": float(spectrum_0),
        "pair_early": float(pair_early),
        "spectrum_early": float(spectrum_early),
        "pair_final": float(pair_final),
        "spectrum_final": float(spectrum_final),
        "recovery_pair_early": float(recovery_pair_early),
        "recovery_spectrum_early": float(recovery_spectrum_early),
        "recovery_pair": float(recovery_pair),
        "recovery_spectrum": float(recovery_spectrum),
        "bulk_error": bulk_error,
        "maximum_radius": float(maximum_radius),
        "final_radius_ratio": float(final_radius_ratio),
        "source_off": bool(source_off),
        "bounded": bounded,
        "cohesive": cohesive,
    }


def summarize(rows):
    summary = {}
    for dt in DTS:
        summary[str(dt)] = {}
        for case in CASES:
            subset = [row for row in rows if row["dt"] == dt and row["case"] == case]
            summary[str(dt)][case] = {
                "n": len(subset),
                "cohesive_count": sum(row["cohesive"] for row in subset),
                "pair_0_mean": float(np.mean([row["pair_0"] for row in subset])),
                "recovery_pair_early_mean": float(np.mean([row["recovery_pair_early"] for row in subset])),
                "recovery_spectrum_early_mean": float(np.mean([row["recovery_spectrum_early"] for row in subset])),
                "recovery_pair_mean": float(np.mean([row["recovery_pair"] for row in subset])),
                "recovery_pair_min": float(np.min([row["recovery_pair"] for row in subset])),
                "recovery_spectrum_mean": float(np.mean([row["recovery_spectrum"] for row in subset])),
                "recovery_spectrum_min": float(np.min([row["recovery_spectrum"] for row in subset])),
                "bulk_error_max": float(np.max([row["bulk_error"] for row in subset])),
                "bounded_count": sum(row["bounded"] for row in subset),
                "source_off_count": sum(row["source_off"] for row in subset),
            }
    return summary


def relative_difference(a, b):
    return abs(a - b) / max(abs(b), 1e-15)


def verify(rows, summary):
    expected = {
        "elastic": 12,
        "elastic_relabelled": 12,
        "shape_memory_complete": 12,
        "repulsive_gas": 0,
        "deformed_glass": 0,
        "radial_restorer": 0,
        "rigid_advected": 0,
        "external_removed": 0,
        "external_template_active": 0,
    }

    for dt in DTS:
        block = summary[str(dt)]
        for case, expected_count in expected.items():
            assert block[case]["cohesive_count"] == expected_count
        assert max(block[case]["bulk_error_max"] for case in CASES) < 1e-8
        assert block["external_template_active"]["recovery_pair_min"] > 0.80
        assert block["external_template_active"]["recovery_spectrum_min"] > 0.80
        assert block["external_template_active"]["source_off_count"] == 0
        assert block["radial_restorer"]["recovery_pair_mean"] < 0.70
        assert block["radial_restorer"]["recovery_spectrum_mean"] < 0.70

        glass = [row for row in rows if row["dt"] == dt and row["case"] == "deformed_glass"]
        assert max(abs(row["recovery_pair_early"]) for row in glass) < 1e-8
        assert max(abs(row["recovery_pair"]) for row in glass) < 1e-8

        elastic = [row for row in rows if row["dt"] == dt and row["case"] == "elastic"]
        relabelled = [row for row in rows if row["dt"] == dt and row["case"] == "elastic_relabelled"]
        elastic.sort(key=lambda row: row["seed"])
        relabelled.sort(key=lambda row: row["seed"])
        for original, permuted in zip(elastic, relabelled):
            assert original["cohesive"] == permuted["cohesive"]
            for key in (
                "pair_0", "spectrum_0",
                "recovery_pair_early", "recovery_spectrum_early",
                "recovery_pair", "recovery_spectrum",
            ):
                assert abs(original[key] - permuted[key]) < 1e-10

    coarse = summary[str(0.01)]
    fine = summary[str(0.0025)]
    for case in POSITIVE_CASES:
        assert relative_difference(coarse[case]["recovery_pair_mean"], fine[case]["recovery_pair_mean"]) < 0.01
        assert relative_difference(coarse[case]["recovery_spectrum_mean"], fine[case]["recovery_spectrum_mean"]) < 0.01


rows = [simulate(case, seed, dt) for dt in DTS for case in CASES for seed in SEEDS]
summary = summarize(rows)
verify(rows, summary)
raw_json = json.dumps(rows, sort_keys=True, separators=(",", ":"))
summary_json = json.dumps(summary, sort_keys=True, separators=(",", ":"))
print(json.dumps({
    "raw_row_count": len(rows),
    "raw_rows_sha256": hashlib.sha256(raw_json.encode("utf-8")).hexdigest(),
    "summary_sha256": hashlib.sha256(summary_json.encode("utf-8")).hexdigest(),
    "summary": summary,
}, indent=2, sort_keys=True))
```

## 7. Reproducible result

### 7.1 Environment

```text
Python: 3.13.5
NumPy: 2.3.5
Platform: Linux 6.12.13 x86_64, glibc 2.41
```

### 7.2 Classification

| Case | Expected per dt | dt=0.01 | dt=0.005 | dt=0.0025 |
|---|---:|---:|---:|---:|
| elastic | 12 | 12 | 12 | 12 |
| elastic relabelled | 12 | 12 | 12 | 12 |
| complete shape memory | 12 | 12 | 12 | 12 |
| repulsive gas | 0 | 0 | 0 | 0 |
| deformed glass | 0 | 0 | 0 | 0 |
| radial restorer | 0 | 0 | 0 | 0 |
| rigid advected | 0 | 0 | 0 | 0 |
| external organizer removed | 0 | 0 | 0 | 0 |
| active external template | 0 | 0 | 0 | 0 |

### 7.3 Decision-relevant metric summary

```json
{
  "raw_row_count": 324,
  "raw_rows_canonical_json_sha256": "33d93e9ad4fd50b92f6188da2e1e8d69760d470617eac264266a62889b5e67e5",
  "summary_canonical_json_sha256": "dcb05ef14a29955e2bd184244152fe1fb1ab45b21bfba8fdeb3aebe78574ea17",
  "positive_mean_recovery_ranges": {
    "elastic_pair": [0.9837883304019887, 0.9838095218511743],
    "elastic_spectrum": [0.9994267580583572, 0.9994520306666775],
    "shape_memory_pair": [0.9954613975183539, 0.9957380208607821],
    "shape_memory_spectrum": [0.9987912095080812, 0.9988888878406378]
  },
  "hard_near_misses": {
    "repulsive_gas_pair_recovery_range": [-2.899843033208695, -2.898966060457967],
    "deformed_glass_pair_recovery_absolute_max": 1.211066612208236e-14,
    "radial_restorer_pair_recovery_range": [0.48716093121197823, 0.48716311874953294],
    "radial_restorer_spectrum_recovery_range": [0.35220337999829715, 0.3522637097185886],
    "external_template_pair_recovery_range": [0.9953969131464069, 0.99567251555644],
    "external_template_spectrum_recovery_range": [0.9989027786465493, 0.9989960243722279],
    "external_template_source_off_count_per_dt": 0
  },
  "maximum_bulk_velocity_error": 6.938893903907228e-15,
  "positive_pair_recovery_coarse_fine_relative_difference_max": 0.000277884549936124,
  "positive_spectrum_recovery_coarse_fine_relative_difference_max": 0.0000977965480940619
}
```

The canonical digests use `json.dumps(..., sort_keys=True, separators=(",", ":"))` exactly as shown in the executable code.

### 7.4 Permutation check

For every seed and timestep, the original and consistently relabelled elastic systems matched in all declared permutation-invariant metrics to better than `1e-10`, and both were classified identically.

### 7.5 Source gate check

The active external template passed every geometric recovery threshold and remained bounded with conserved bulk motion. Its only decisive failure was that the organizer remained active. Therefore the source-off gate was independently exercised rather than redundant.

### 7.6 Compactness confounder check

The radial restorer showed early movement in the apparently correct direction and restored broad scale, but final pair recovery remained near `0.487` and spectral recovery near `0.352`. Compactness alone did not pass as relational cohesion.

### 7.7 Stiffness confounder check

The deformed glass was internally stiff but had its rest lengths defined by the damaged state. Its recovery stayed at floating-point zero and it was rejected. Stiffness alone was not treated as repair.

## 8. Analytic and independent checks

1. All internal pair forces are equal and opposite.
2. Relative damping, radial forces, and external-template forces are zero-sum.
3. Center-of-mass velocity is therefore conserved analytically; the observed maximum error was below `7e-15`.
4. Consistent member permutation leaves every unordered distance and kernel eigenvalue unchanged; the numerical comparison confirmed this.
5. The deformed glass begins at exact spring equilibrium for its own damaged rest lengths.
6. The active external template proves that recovery without a source ledger is non-identifying.
7. Three timesteps produced identical classification and recovery changes far inside the frozen tolerance.
8. Pair distributions and kernel spectra are separate permutation-invariant observer families; agreement reduces but does not eliminate observer degeneracy.

## 9. What was actually established

```text
implementation:
    nine synthetic point-system classes and a source-aware permutation-invariant observer
    were executed with the frozen code;

reproducible observation:
    108/108 internally cohesive cases passed and 216/216 near-miss controls failed
    across three timesteps and held-out seeds;

cautious interpretation:
    in this synthetic domain, relational recovery plus source-off accounting separates
    mechanical cohesion from interaction, compactness, rigidity, persistence, and external repair;

hypothesis:
    analogous observables may help test whether a Lineum vortex collective is more than a gas;

real-physics boundary:
    no actual Lineum state or physical particle was tested.
```

## 10. Limitations and next discriminator

The result remains deliberately below the collective-particle gate.

Unresolved limitations:

- point members are not continuous fields or vortices;
- reference relations are inserted into positive dynamics;
- no member is born, removed, exchanged, split, or merged;
- no self-generated protocol reconstructs missing relations;
- sorted pair distances and kernel spectra can have non-unique configurations;
- no wake, environment memory, boundary, phase winding, source stock, or field ledger exists;
- complete shape memory passes mechanical cohesion even though it may be a fixed internal template rather than an emergent collective identity;
- no unknown-reference observer was tested.

The next discriminator is therefore not another easier cohesion example. It is a **member-turnover protocol fixture** with at least:

```text
fixed-template cohesion that fails when members are exchanged;
protocol-maintained cohesion that rebuilds relations after member removal and insertion;
turnover gas with matched count, density, and energy;
external repair protocol active during challenge;
permutation-, rotation-, and population-size controls;
identity metrics frozen without using member labels or the known final assignment.
```

Only after that fixture passes should an analogous protocol observer be considered for a recovered Lineum state.

## 11. Root-programme impact matrix

| Root branch | Relation | Result impact |
|---|---|---|
| Collective-particle hypothesis | `supports` | Label-free synthetic mechanical cohesion survived hard near-miss controls. |
| P2 vortex-gas remnant | `depends_on` | P2 remains unrecovered and unclassified by this observer. |
| Minimum-flux observer limitation | `supports` | Relational recovery and source accounting add information beyond overlap and transport. |
| Source accounting | `supports` | Active external repair was rejected despite near-perfect geometry. |
| Protocol identity under turnover | `reopens` | Mechanical cohesion is now isolated as a weaker prerequisite requiring a new fixture. |
| Static recipe versus live state | `supports` | A built-in template can restore form without demonstrating emergent or membership-robust identity. |
| Copying and heredity | `unaffected` | No descendant, inheritance, or content transfer was tested. |
| Physical particle correspondence | `unaffected` | Synthetic observer success supplies no evidence about nature. |

## 12. Current verdict

```text
adversarial_known_answer_fixture = validated_within_declared_synthetic_domain
confirmatory_trajectories = 324
internally_cohesive_true_positive_rate = 1.0
registered_near_miss_true_negative_rate = 1.0
permutation_invariance = passed
source_off_autonomy_gate = independently_exercised_and_passed
timestep_classification_stability = passed
mechanical_cohesion_observer = validated_for_registered_toy_classes
membership_turnover_identity = not_tested
lineum_collective_cohesion = not_tested
p2_particle_status = unchanged
public_api_or_whitepaper_change = not_authorized
clickup_checkpoint_sync = failed_once_connector_tool_not_found_no_retry
next_action = preregister_member_turnover_protocol_fixture
```
