# Pneuma-Inspired Cohesion Observer Known-Answer Fixture

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
**Object-definition predecessor:** `research/foundations/lineum-core-envelope-wake-and-attraction-preregistration.md`, version 0.2.0, blob `621cc5f9147dde4a3819e9fc2d3febe05e387cf8`  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Scope:** Validate a known-answer causal observer for distributed cohesion before applying any analogous metric to Lineum. The observer must separate an internally restoring collective from geometrically similar source-off gases, advected gases, externally prepared but no-longer-maintained populations, and an almost-unperturbed sham.  
**Central question:** Can a small observer ensemble detect that a collective has a source-off restoring organization rather than merely persistent shape, common translation, or historical external preparation?  
**Current confidence:** high that the fixture classes have known causal differences; medium that the frozen metric ensemble will separate them on held-out perturbations; no claim yet about actual Lineum vortices, particles, pneuma, souls, or physical matter.

## 1. Answer first

The historical Stoic pneuma analogy is translated here into one narrow systems question:

> Does the whole exert a reproducible internal restoring response after deformation while preserving free bulk motion?

This report does **not** add a `pneuma` field or ancient ontology. It validates an observer on synthetic systems whose answer is known by construction.

A genuine pass requires all of the following:

```text
meaningful deformation was applied;
initial force points back toward the reference relational geometry;
tracked shape recovers;
permutation-invariant pair-distance structure recovers;
bulk translation remains conserved;
recovery occurs with no external organizing source after the challenge.
```

A visually coherent population must fail if it only translates, retains a deformed snapshot, or was arranged by a source that is absent during the challenge.

## 2. Preserved exploratory history and confirmatory boundary

Protocol development used non-confirmatory seeds `0..111` to choose a stable fixture, integration horizon, and thresholds. Those runs are exploratory and cannot serve as the retained validation result.

This version freezes an untouched confirmatory set:

```text
held-out seeds: 200..211
integration steps: dt = 0.01, 0.005, 0.0025
horizon: T = 6.0 model units
cases: elastic, gas, advected_gas, external_history, sham_elastic
```

No confirmatory output for seeds `200..211` existed when this version was committed.

## 3. Known-answer fixture classes

### 3.1 Elastic collective

Sixteen points form an irregular ring. Each point is connected to offsets `1`, `2`, and `5` around the ring by Hooke-like distance springs. The force depends only on pair separation and rest length. Relative-velocity damping removes internal oscillation without damping center-of-mass motion.

Known answer:

```text
internal restoring organization = present
external source during challenge = absent
bulk translation = free
```

### 3.2 Gas

The same deformed positions and bulk velocity are continued with no internal forces.

Known answer:

```text
internal restoring organization = absent
```

### 3.3 Advected gas

The gas receives the same common bulk velocity as the elastic collective. Translation-aligned image overlap must not be interpreted as cohesion.

Known answer:

```text
common motion = present
internal restoring organization = absent
```

### 3.4 External-history population

The state is interpreted as having been arranged previously by an external organizer, but that organizer is absent for the entire challenge. Numerically its post-removal continuation is identical to the gas. This intentionally tests whether historical preparation or an orderly initial frame is mistaken for autonomous cohesion.

Known answer:

```text
prior external organization = allowed as history
source-off internal restoring organization = absent
```

### 3.5 Sham elastic

The elastic network is perturbed only by tiny numerical-scale position noise rather than the declared macroscopic deformation. It can possess high stiffness and apparent recovery but must fail the meaningful-challenge gate.

Known answer:

```text
internal restoring organization = present
material challenge = absent
scientific recovery claim = not admissible
```

## 4. Frozen geometry and dynamics

Reference point `i` has angle and radius

```text
theta_i = 2 pi i / 16
r_i = 1 + 0.12 cos(3 theta_i) + 0.05 sin(5 theta_i)
R_i = [r_i cos(theta_i), r_i sin(theta_i)]
```

The irregular modulation avoids a perfectly symmetric ring while remaining deterministic.

The challenged state is

```text
X_i(0) = A R_i + eta_i
A = [[1.25, 0.10],
     [0.02, 0.75]]
eta_i ~ Normal(0, 0.035^2 I)
```

The common initial velocity is

```text
v_bulk = [0.30, -0.15]
```

For each registered edge `(i,j)`, the elastic force is

```text
F_i += k (|X_j-X_i| - l_ij^0) (X_j-X_i)/|X_j-X_i|
F_j -= same
```

with `k = 4.0`. Relative damping is

```text
F_i^damp = -gamma (v_i - mean(v))
gamma = 2.0
```

The equal-and-opposite spring forces and zero-sum relative damping preserve center-of-mass velocity analytically up to floating-point error.

Integration uses semi-implicit Euler:

```text
v <- v + dt F
x <- x + dt v
```

## 5. Frozen observer ensemble

### 5.1 Meaningful perturbation gate

Let `E_shape(0)` be the label-tracked Procrustes error after removing translation and optimal proper rotation.

```text
G_perturb = E_shape(0) > 0.05
```

This prevents an almost-unchallenged state from being called repaired.

### 5.2 Initial restoring projection

After translation and rotation alignment, let `u` be displacement from reference and `F` the aligned internal force. Define

```text
k_eff = - sum_i F_i dot u_i / sum_i |u_i|^2
```

Frozen gate:

```text
G_force = k_eff > 0.25
```

The value is an observer score in toy units, not a physical elastic modulus.

### 5.3 Tracked-shape recovery

```text
R_shape = [E_shape(0) - E_shape(T)] / E_shape(0)
G_shape = R_shape > 0.80
```

### 5.4 Permutation-invariant pair-structure recovery

All pair distances are sorted, producing a label-free distance signature. Its normalized RMS error relative to the reference is `E_pair`.

```text
R_pair = [E_pair(0) - E_pair(T)] / E_pair(0)
G_pair = R_pair > 0.80
```

### 5.5 Bulk-motion conservation

```text
G_bulk = |mean(v(T)) - v_bulk| < 1e-8
```

### 5.6 Frozen verdict

```text
cohesive = G_perturb and G_force and G_shape and G_pair and G_bulk
```

The label-tracked and permutation-invariant observers are intentionally both required. Agreement is necessary because each can hide a different failure.

## 6. Frozen expected classification

Across every held-out seed and timestep:

```text
elastic          -> cohesive

gas              -> not cohesive
advected_gas     -> not cohesive
external_history -> not cohesive
sham_elastic     -> not cohesive because G_perturb fails
```

Any false positive, false negative, loss of bulk conservation, NaN, integration instability, or classification change across the registered timestep sweep fails this fixture version.

For continuous metrics, the mean elastic recovery values at `dt=0.01` and `dt=0.0025` must differ by less than 1% relative for `E_shape(T)`, `E_pair(T)`, `R_shape`, and `R_pair`.

## 7. Complete executable verification code

```python
import json
import math
import numpy as np

N = 16
SEEDS = list(range(200, 212))
DTS = [0.01, 0.005, 0.0025]
T_FINAL = 6.0
CASES = [
    "elastic",
    "gas",
    "advected_gas",
    "external_history",
    "sham_elastic",
]
BULK = np.array([0.30, -0.15], dtype=float)


def reference_shape(n=N):
    theta = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    radius = 1.0 + 0.12 * np.cos(3.0 * theta) + 0.05 * np.sin(5.0 * theta)
    return np.column_stack((radius * np.cos(theta), radius * np.sin(theta)))


def edge_list(n=N):
    edges = set()
    for i in range(n):
        for offset in (1, 2, 5):
            j = (i + offset) % n
            edges.add(tuple(sorted((i, j))))
    return sorted(edges)


def initial_state(seed, ref, perturbed):
    rng = np.random.default_rng(seed)
    if perturbed:
        transform = np.array([[1.25, 0.10], [0.02, 0.75]], dtype=float)
        x = ref @ transform.T + rng.normal(scale=0.035, size=ref.shape)
    else:
        x = ref.copy() + rng.normal(scale=0.001, size=ref.shape)
    x -= x.mean(axis=0)
    v = np.repeat(BULK[None, :], len(ref), axis=0)
    return x, v


def proper_alignment(x, ref):
    x_centered = x - x.mean(axis=0)
    r_centered = ref - ref.mean(axis=0)
    u, _, vt = np.linalg.svd(x_centered.T @ r_centered)
    rotation = u @ vt
    if np.linalg.det(rotation) < 0.0:
        u[:, -1] *= -1.0
        rotation = u @ vt
    return x_centered @ rotation, r_centered, rotation


def shape_error(x, ref):
    x_aligned, r_centered, _ = proper_alignment(x, ref)
    numerator = np.sqrt(np.mean((x_aligned - r_centered) ** 2))
    denominator = np.sqrt(np.mean(r_centered ** 2))
    return float(numerator / denominator)


def sorted_pair_distances(x):
    distances = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            distances.append(np.linalg.norm(x[j] - x[i]))
    return np.sort(np.asarray(distances, dtype=float))


def pair_error(x, ref):
    observed = sorted_pair_distances(x)
    expected = sorted_pair_distances(ref)
    return float(np.sqrt(np.mean((observed - expected) ** 2)) / np.mean(expected))


def spring_forces(x, v, ref, edges, active):
    forces = np.zeros_like(x)
    if active:
        for i, j in edges:
            rest_length = np.linalg.norm(ref[j] - ref[i])
            delta = x[j] - x[i]
            distance = np.linalg.norm(delta)
            if distance > 1e-12:
                force = 4.0 * (distance - rest_length) * delta / distance
                forces[i] += force
                forces[j] -= force
        velocity_center = v.mean(axis=0)
        forces += -2.0 * (v - velocity_center)
    return forces


def effective_stiffness(x, v, ref, edges, active):
    if not active:
        return 0.0
    forces = spring_forces(x, v, ref, edges, active=True)
    x_aligned, r_centered, rotation = proper_alignment(x, ref)
    displacement = x_aligned - r_centered
    aligned_forces = (forces - forces.mean(axis=0)) @ rotation
    denominator = np.sum(displacement * displacement)
    if denominator <= 1e-15:
        return float("nan")
    return float(-np.sum(aligned_forces * displacement) / denominator)


def simulate(case, seed, dt):
    ref = reference_shape()
    edges = edge_list()
    perturbed = case != "sham_elastic"
    active = case in ("elastic", "sham_elastic")
    x, v = initial_state(seed, ref, perturbed=perturbed)

    shape_0 = shape_error(x, ref)
    pair_0 = pair_error(x, ref)
    k_eff = effective_stiffness(x, v, ref, edges, active=active)

    steps = int(round(T_FINAL / dt))
    for _ in range(steps):
        forces = spring_forces(x, v, ref, edges, active=active)
        v += dt * forces
        x += dt * v

    shape_t = shape_error(x, ref)
    pair_t = pair_error(x, ref)
    recovery_shape = (shape_0 - shape_t) / shape_0
    recovery_pair = (pair_0 - pair_t) / pair_0
    bulk_error = np.linalg.norm(v.mean(axis=0) - BULK)

    cohesive = bool(
        shape_0 > 0.05
        and k_eff > 0.25
        and recovery_shape > 0.80
        and recovery_pair > 0.80
        and bulk_error < 1e-8
    )

    return {
        "case": case,
        "seed": seed,
        "dt": dt,
        "shape_0": float(shape_0),
        "shape_t": float(shape_t),
        "pair_0": float(pair_0),
        "pair_t": float(pair_t),
        "recovery_shape": float(recovery_shape),
        "recovery_pair": float(recovery_pair),
        "k_eff": float(k_eff),
        "bulk_error": float(bulk_error),
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
                "shape_0_mean": float(np.mean([row["shape_0"] for row in subset])),
                "shape_t_mean": float(np.mean([row["shape_t"] for row in subset])),
                "pair_0_mean": float(np.mean([row["pair_0"] for row in subset])),
                "pair_t_mean": float(np.mean([row["pair_t"] for row in subset])),
                "recovery_shape_mean": float(np.mean([row["recovery_shape"] for row in subset])),
                "recovery_shape_min": float(np.min([row["recovery_shape"] for row in subset])),
                "recovery_pair_mean": float(np.mean([row["recovery_pair"] for row in subset])),
                "recovery_pair_min": float(np.min([row["recovery_pair"] for row in subset])),
                "k_eff_mean": float(np.mean([row["k_eff"] for row in subset])),
                "k_eff_min": float(np.min([row["k_eff"] for row in subset])),
                "bulk_error_max": float(np.max([row["bulk_error"] for row in subset])),
            }
    return summary


def verify(summary):
    expected = {
        "elastic": 12,
        "gas": 0,
        "advected_gas": 0,
        "external_history": 0,
        "sham_elastic": 0,
    }
    for dt in DTS:
        block = summary[str(dt)]
        for case, expected_count in expected.items():
            assert block[case]["cohesive_count"] == expected_count
        assert max(block[case]["bulk_error_max"] for case in CASES) < 1e-8

    coarse = summary[str(0.01)]["elastic"]
    fine = summary[str(0.0025)]["elastic"]
    for key in ("shape_t_mean", "pair_t_mean", "recovery_shape_mean", "recovery_pair_mean"):
        relative_difference = abs(coarse[key] - fine[key]) / abs(fine[key])
        assert relative_difference < 0.01, (key, relative_difference)


rows = [simulate(case, seed, dt) for dt in DTS for case in CASES for seed in SEEDS]
summary = summarize(rows)
verify(summary)
print(json.dumps(summary, indent=2, sort_keys=True))
```

## 8. Analytic sanity checks

1. Each spring contribution is equal and opposite, so its total force is zero.
2. Relative damping sums to zero because `sum_i(v_i - mean(v)) = 0`.
3. Therefore center-of-mass acceleration is zero in every registered case.
4. The gas cases have exactly zero internal force in this fixture, so `k_eff = 0` by construction.
5. The elastic spring energy is minimized when registered edge lengths equal their rest lengths. Damping removes relative kinetic energy but not bulk translation.
6. The sham may have large `k_eff` and high fractional recovery, demonstrating why a meaningful-perturbation gate is logically necessary.

These checks are independent of the numerical classification output.

## 9. Result placeholder

No confirmatory result is reported in version 0.1.0.

```text
confirmatory_seeds_200_to_211 = not_executed_at_commit
fixture_verdict = preregistered
```

## 10. Interpretation boundary

A pass will establish only that the observer ensemble recognizes its synthetic target and rejects its declared nulls.

It will not establish:

```text
that actual Lineum vortex populations possess cohesion;
that a Lineum particle exists;
that pneuma is a physical field;
that Stoic physics describes nature correctly;
that ancient texts encode Lineum;
that recovery is life, consciousness, soul, or agency.
```

Application to actual Lineum remains blocked until the exact P2 package or another SHA-pinned executable candidate is available.

## 11. Root-programme impact matrix

| Root branch | Relation | Effect of this preregistration |
|---|---|---|
| Collective-particle hypothesis | `supports` | Supplies a known-answer causal observer gate before actual P2 use. |
| P2 vortex-gas remnant | `depends_on` | No application is permitted until exact P2 recovery. |
| Minimum-flux observer is non-identifying | `supports` | Adds force-response and relational recovery rather than image overlap alone. |
| Source accounting | `constrains` | Fixture recovery must be source-off and preserve free bulk motion. |
| Copying and heredity | `unaffected` | Cohesion is not reproduction or inheritance. |
| Physical particle correspondence | `unaffected` | Synthetic observer validation supplies no evidence about nature. |

## 12. Current verdict

```text
known_answer_fixture = preregistered
confirmatory_execution = pending
observer_thresholds = frozen
held_out_seeds = frozen_200_to_211
lineum_application = not_authorized
next_action = execute_exact_embedded_code_then_record_complete_output
```
