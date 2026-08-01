# Pneuma-Inspired Cohesion Observer Adversarial Near-Miss Fixture

**Status:** active preregistration; protocol frozen before confirmatory held-out execution  
**Version:** 0.1.0  
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
**Scope:** Adversarially test whether a permutation-invariant, source-aware cohesion observer can distinguish internally restoring organization from interacting but non-restoring populations, metastable rigidity, radial compaction, unchanged advection, removed external organization, and active external template control.  
**Central question:** Can mechanical cohesion be recognized without permanent member labels while rejecting systems that are merely interactive, rigid, compacting, historically prepared, or externally maintained?  
**Current confidence:** high that the fixture cases have distinct known causal classes; medium that the frozen observer will classify all held-out cases across timestep refinement; no result yet on confirmatory seeds, actual Lineum fields, P2, physical particles, pneuma, soul, or ancient encoded physics.

## 1. Answer first

The first known-answer fixture showed that a simple spring collective can be separated from a free gas. That was necessary but too easy.

This second fixture asks whether the observer survives harder near-misses:

```text
an interacting gas that moves because of collisions but has no remembered organization;
a glass-like network that is stiff around the damaged shape rather than restoring the original;
a radial restorer that repairs size but not relational geometry;
a rigidly advected pattern that looks perfectly persistent;
a previously organized population after its organizer is removed;
an active external template that genuinely repairs shape but is not autonomous;
a mechanically cohesive shape-memory network;
an equivalent elastic collective after arbitrary member relabeling.
```

The observer is intentionally split into causal gates:

```text
meaningful challenge;
early permutation-invariant movement toward the reference organization;
long-horizon recovery of pair structure;
long-horizon recovery of a relational spectrum;
source-off autonomy;
boundedness;
free bulk-motion conservation.
```

A pass establishes only synthetic mechanical cohesion. It does not establish collective identity under birth, death, exchange, copying, or heredity.

## 2. Preserved exploratory history and confirmatory boundary

Protocol development used exploratory seeds `0..19`. Those runs selected stable fixture parameters and thresholds but are excluded from the retained validation result.

The untouched confirmatory set is frozen as:

```text
held-out seeds: 400..411
integration steps: dt = 0.01, 0.005, 0.0025
horizon: T = 6.0 model units
early-response horizon: 0.25 model units
cases: elastic, elastic_relabelled, shape_memory_complete,
       repulsive_gas, deformed_glass, radial_restorer,
       rigid_advected, external_removed, external_template_active
```

No confirmatory output for seeds `400..411` existed when this version was committed.

## 3. Fixture classes and known causal answers

### 3.1 Elastic

The sparse internal spring network from the predecessor fixture restores registered reference distances. It is source-off and preserves center-of-mass motion.

```text
mechanical cohesion = present
expected verdict = cohesive
```

### 3.2 Elastic relabelled

The complete state, reference coordinates, and spring graph are consistently permuted by a seed-dependent random member relabeling. The physical system is identical; only labels change.

```text
mechanical cohesion = present
permanent observer labels = absent
expected verdict = cohesive
```

A failure here falsifies the claimed label independence of this observer version.

### 3.3 Complete shape-memory network

All point pairs carry internal spring rest lengths from the reference shape. The mechanism contains a strong distributed template but no external force during the challenge.

```text
mechanical cohesion = present
member-turnover identity = not tested
expected verdict = cohesive
```

This is a positive control for mechanical cohesion, not evidence of emergent or membership-robust identity.

### 3.4 Repulsive gas

Points interact through short-range soft repulsion and relative damping. They can exchange momentum and strongly change shape, but no force remembers the reference organization.

```text
interaction = present
reference-restoring organization = absent
expected verdict = not cohesive
```

### 3.5 Deformed glass

The sparse spring graph is frozen with rest lengths measured from the already deformed challenge state. It is internally stiff but regards the damaged geometry as equilibrium.

```text
stiffness = present
recovery toward original organization = absent
expected verdict = not cohesive
```

### 3.6 Radial restorer

Every member is pulled toward the reference root-mean-square radius around the instantaneous centroid. This repairs broad scale and compactness while leaving angular and pair relations unconstrained.

```text
size restoration = present
specific relational restoration = absent
expected verdict = not cohesive
```

This case guards against mistaking simple compaction for object identity.

### 3.7 Rigid advected pattern

The deformed configuration translates with a common velocity and no internal force. It keeps a stable image in a co-moving frame.

```text
visual persistence = present
restoring organization = absent
expected verdict = not cohesive
```

### 3.8 External organizer removed

The initial pattern is interpreted as externally prepared, but the organizer is absent throughout the challenge. Its post-removal dynamics are deliberately identical to rigid advection.

```text
historical external preparation = present
source-off restoring organization = absent
expected verdict = not cohesive
```

### 3.9 Active external template

A laboratory-frame template force restores every member toward the reference coordinates after translation removal. It should produce excellent geometric recovery, but the organizing source remains active throughout the challenge.

```text
geometric recovery = present
source-off autonomy = absent
expected verdict = not cohesive
```

This case tests whether the autonomy gate does real work rather than merely accompanying an already failed geometry score.

## 4. Frozen geometry and shared initial state

For `N = 16`,

```text
theta_i = 2 pi i / 16
r_i = 1 + 0.12 cos(3 theta_i) + 0.05 sin(5 theta_i)
R_i = [r_i cos(theta_i), r_i sin(theta_i)]
```

The challenge is

```text
X_i(0) = A R_i + eta_i
A = [[1.25, 0.10],
     [0.02, 0.75]]
eta_i ~ Normal(0, 0.035^2 I)
```

with common velocity

```text
v_bulk = [0.30, -0.15].
```

The sparse elastic graph connects ring offsets `1`, `2`, and `5`. The complete shape-memory network connects all pairs.

Integration uses semi-implicit Euler:

```text
v <- v + dt F
x <- x + dt v
```

## 5. Frozen permutation-invariant observer

### 5.1 Pair-distance error

All unordered pair distances are sorted. With sorted reference distances `d_ref`,

```text
E_pair(X) = RMS(sort(d(X)) - d_ref) / mean(d_ref).
```

This is invariant to translation, rotation, reflection, and member relabeling. It is not a complete identity invariant by itself.

### 5.2 Relational kernel-spectrum error

Construct

```text
K_ij = exp(-|X_i-X_j|^2 / (2 sigma^2)),
sigma = median reference pair distance.
```

Sort the eigenvalues of `K` and compare them with the reference spectrum:

```text
E_spec(X) = RMS(lambda(X) - lambda_ref) / RMS(lambda_ref).
```

The spectrum is permutation invariant and supplies a second relational family with different degeneracies from sorted pair distances.

### 5.3 Early causal recovery

At `t_early = 0.25`,

```text
R_pair_early = [E_pair(0) - E_pair(t_early)] / E_pair(0)
R_spec_early = [E_spec(0) - E_spec(t_early)] / E_spec(0).
```

Frozen gates:

```text
G_early_pair = R_pair_early > 0.05
G_early_spec = R_spec_early > 0.03
```

These gates reject stable but non-restoring templates and distinguish direction of response from long-horizon coincidence.

### 5.4 Final relational recovery

```text
R_pair = [E_pair(0) - E_pair(T)] / E_pair(0)
R_spec = [E_spec(0) - E_spec(T)] / E_spec(0)
```

Frozen gates:

```text
G_pair = R_pair > 0.80
G_spec = R_spec > 0.80
```

### 5.5 Meaningful challenge, autonomy, boundedness, and bulk motion

```text
G_challenge = E_pair(0) > 0.05
G_source_off = no external organizer is active during the challenge
G_bulk = |mean(v(T)) - v_bulk| < 1e-8
G_bounded = max_t R_rms(t) < 1.8 R_ref
            and 0.6 < R_rms(T)/R_ref < 1.4
```

### 5.6 Verdict

```text
cohesive = G_challenge
           and G_early_pair
           and G_early_spec
           and G_pair
           and G_spec
           and G_source_off
           and G_bulk
           and G_bounded
```

No label-tracked shape metric appears in the verdict.

## 6. Frozen expected classification and failure conditions

For every held-out seed and timestep:

```text
elastic                  -> cohesive
elastic_relabelled       -> cohesive
shape_memory_complete    -> cohesive
repulsive_gas            -> not cohesive
deformed_glass           -> not cohesive
radial_restorer          -> not cohesive
rigid_advected           -> not cohesive
external_removed         -> not cohesive
external_template_active -> not cohesive
```

Additional diagnostic expectations:

```text
external_template_active:
    final pair and spectrum recovery each exceed 0.80,
    but G_source_off fails;

radial_restorer:
    final pair recovery remains below 0.70
    and final spectrum recovery remains below 0.70;

deformed_glass:
    absolute early and final pair recovery remain below 1e-8;

elastic_relabelled:
    classification and all permutation-invariant metrics match elastic
    to within 1e-10 for the same seed and timestep.
```

Any false positive, false negative, NaN, loss of bulk conservation, unbounded positive case, classification change across the timestep sweep, or violation of these diagnostic expectations fails this fixture version.

For each positive class, the relative difference between the mean `R_pair` at `dt=0.01` and `dt=0.0025` must be below `0.01`; the same applies to mean `R_spec`.

## 7. Complete executable verification code

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
    mapped = [
        tuple(sorted((old_to_new[i], old_to_new[j])))
        for i, j in SPARSE
    ]
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
                "pair_0",
                "spectrum_0",
                "recovery_pair_early",
                "recovery_spectrum_early",
                "recovery_pair",
                "recovery_spectrum",
            ):
                assert abs(original[key] - permuted[key]) < 1e-10

    coarse = summary[str(0.01)]
    fine = summary[str(0.0025)]
    for case in POSITIVE_CASES:
        assert relative_difference(
            coarse[case]["recovery_pair_mean"],
            fine[case]["recovery_pair_mean"],
        ) < 0.01
        assert relative_difference(
            coarse[case]["recovery_spectrum_mean"],
            fine[case]["recovery_spectrum_mean"],
        ) < 0.01


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

## 8. Analytic sanity checks

1. Every internal pair force is equal and opposite.
2. Relative damping sums to zero.
3. Radial forces are explicitly mean-subtracted.
4. The external template force is also mean-subtracted, so no fixture changes bulk velocity merely by using a laboratory template.
5. Therefore all cases preserve center-of-mass velocity analytically up to floating-point error.
6. The deformed glass has exactly zero spring extension at the challenge instant, so it should not move toward the original reference absent numerical disturbance.
7. Relabeling consistently permutes points, graph endpoints, and rest lengths; every pair-distance and kernel-spectrum observable must therefore remain identical.
8. The active external template is expected to pass geometric gates but fail autonomy, proving that source accounting is logically independent of visual recovery.
9. The radial restorer can repair scale while leaving pair organization wrong, proving that compactness is not sufficient.

## 9. Result placeholder

No confirmatory result is reported in version 0.1.0.

```text
confirmatory_seeds_400_to_411 = not_executed_at_commit
fixture_verdict = preregistered
```

## 10. Interpretation boundary

A pass will establish only that this synthetic observer recognizes internal mechanical recovery without labels and rejects the registered near-misses.

It will not establish:

```text
membership-turnover identity;
self-generated protocol;
repair in a continuous field;
Lineum vortex cohesion;
a P2 particle;
copying, heredity, life, observerhood, consciousness, or soul;
physical validity of Stoic pneuma;
ancient encoded physics.
```

A failure must be retained. Thresholds may not be rescued post hoc. Any replacement observer requires a new version or successor preregistration.

## 11. Root-programme impact matrix

| Root branch | Relation | Expected impact |
|---|---|---|
| Collective-particle hypothesis | `supports` | Tests a label-free cohesion gate against harder false positives. |
| P2 vortex-gas remnant | `depends_on` | No application occurs before exact P2 recovery. |
| Minimum-flux observer limitation | `supports` | Adds causal relational recovery and autonomy gates. |
| Source accounting | `supports` | Active external repair must fail despite excellent geometry. |
| Protocol identity under turnover | `constrains` | Shape-memory cohesion is explicitly weaker than membership-robust identity. |
| Copying and heredity | `unaffected` | Mechanical cohesion does not imply reproduction. |
| Physical correspondence | `unaffected` | Synthetic classification says nothing about nature. |

## 12. Current verdict

```text
adversarial_fixture = preregistered
confirmatory_execution = pending
observer_thresholds = frozen
held_out_seeds = frozen_400_to_411
lineum_application = not_authorized
next_action = execute_exact_embedded_code_then_record_complete_output
```
