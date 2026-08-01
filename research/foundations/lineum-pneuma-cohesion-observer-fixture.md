# Pneuma-Inspired Cohesion Observer Known-Answer Fixture

**Status:** validated known-answer fixture; synthetic observer gate passed; no Lineum application executed  
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
**Object-definition predecessor:** `research/foundations/lineum-core-envelope-wake-and-attraction-preregistration.md`, version 0.2.0, blob `621cc5f9147dde4a3819e9fc2d3febe05e387cf8`  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Scope:** Validate a known-answer causal observer for distributed cohesion before applying any analogous metric to Lineum. The observer separates an internally restoring collective from geometrically similar source-off gases, advected gases, externally prepared but no-longer-maintained populations, and an almost-unperturbed sham.  
**Central question:** Can a small observer ensemble detect that a collective has a source-off restoring organization rather than merely persistent shape, common translation, or historical external preparation?  
**Current confidence:** high that the frozen observer passed the declared synthetic fixture and timestep controls; low that the same observables will remain valid for continuous Lineum vortex fields; no evidence yet that actual Lineum vortices form a cohesive particle, that pneuma is a physical field, or that ancient texts encode Lineum.

## 1. Answer first

The first concrete translation of the pneuma analogy worked at the level it was allowed to test.

A synthetic collective with real internal restoring relations repaired a large deformation while moving freely as a whole. Geometrically identical gases, an advected gas, and a population that had only been externally organized in its past did not repair. An almost-unchallenged elastic sham was correctly rejected because there was no meaningful injury from which to claim recovery.

Across three integration steps and twelve untouched held-out seeds:

```text
elastic true positives:        36 / 36
null and sham true negatives: 144 / 144
false positives:                0
false negatives:                0
classification drift by dt:     0
```

This validates only the observer fixture. It does not show that the P2 remnant or any other Lineum state has this property.

## 2. Version history and preserved preregistration

Version 0.1.0 was committed before the confirmatory execution:

```text
preregistration commit: c9bba1291afe93d408f8560520ef4197ed71d069
held-out seeds: 200..211
integration steps: 0.01, 0.005, 0.0025
horizon: 6.0
cases and thresholds: frozen
```

Protocol development had used seeds `0..111`; those exploratory runs were excluded from the retained validation. Version 0.2.0 records the first execution of the untouched confirmatory seeds `200..211` without changing a threshold, case, force law, horizon, or acceptance condition.

## 3. Historical metaphor and operational translation

The relevant historical inspiration was the Stoic description of pneuma as an inward-and-outward tensility that gives qualities and makes a body one object. The scientific translation is deliberately narrower:

> Does the whole exert a reproducible internal restoring response after deformation while preserving free bulk motion?

This report does not add a `pneuma` field. `Pneuma-inspired` names the provenance of the question, not an implemented or physical ontology.

A pass requires all of the following:

```text
meaningful deformation was applied;
initial force points back toward the reference relational geometry;
tracked shape recovers;
permutation-invariant pair-distance structure recovers;
bulk translation remains conserved;
recovery occurs with no external organizing source after the challenge.
```

## 4. Known-answer fixture classes

### 4.1 Elastic collective

Sixteen points form an irregular ring. Each point is connected to offsets `1`, `2`, and `5` around the ring by Hooke-like distance springs. Relative-velocity damping removes internal oscillation without damping center-of-mass motion.

```text
internal restoring organization = present
external source during challenge = absent
bulk translation = free
```

### 4.2 Gas

The same deformed positions and bulk velocity continue with no internal forces.

```text
internal restoring organization = absent
```

### 4.3 Advected gas

The gas receives the same common bulk velocity as the elastic collective. Translation-aligned persistence is therefore insufficient.

```text
common motion = present
internal restoring organization = absent
```

### 4.4 External-history population

The state is interpreted as having been arranged previously by an external organizer, but the organizer is absent for the entire challenge. Its continuation is intentionally identical to the gas.

```text
prior external organization = allowed as history
source-off internal restoring organization = absent
```

### 4.5 Sham elastic

The elastic network receives only tiny position noise instead of the declared macroscopic deformation. It can be stiff and can reduce its already tiny error, but it is not eligible for a repair claim.

```text
internal restoring organization = present
material challenge = absent
scientific recovery claim = inadmissible
```

## 5. Frozen geometry and dynamics

Reference point `i` is

```text
theta_i = 2 pi i / 16
r_i = 1 + 0.12 cos(3 theta_i) + 0.05 sin(5 theta_i)
R_i = [r_i cos(theta_i), r_i sin(theta_i)]
```

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

For each edge `(i,j)`,

```text
F_i += k (|X_j-X_i| - l_ij^0) (X_j-X_i)/|X_j-X_i|
F_j -= same
k = 4.0
```

Relative damping is

```text
F_i^damp = -gamma (v_i - mean(v))
gamma = 2.0
```

Semi-implicit Euler is used:

```text
v <- v + dt F
x <- x + dt v
```

## 6. Frozen observer ensemble

### 6.1 Meaningful perturbation

`E_shape` is the label-tracked Procrustes error after translation removal and optimal proper rotation.

```text
G_perturb = E_shape(0) > 0.05
```

### 6.2 Initial restoring projection

With aligned displacement `u` and internal force `F`,

```text
k_eff = - sum_i F_i dot u_i / sum_i |u_i|^2
G_force = k_eff > 0.25
```

This is a toy observer score, not a physical elastic modulus.

### 6.3 Tracked-shape recovery

```text
R_shape = [E_shape(0) - E_shape(T)] / E_shape(0)
G_shape = R_shape > 0.80
```

### 6.4 Permutation-invariant pair recovery

All pair distances are sorted to form a label-free signature with normalized RMS error `E_pair`.

```text
R_pair = [E_pair(0) - E_pair(T)] / E_pair(0)
G_pair = R_pair > 0.80
```

### 6.5 Bulk-motion conservation

```text
G_bulk = |mean(v(T)) - v_bulk| < 1e-8
```

### 6.6 Verdict

```text
cohesive = G_perturb and G_force and G_shape and G_pair and G_bulk
```

Both a tracking-based observer and a permutation-invariant observer are required because they have different failure modes.

## 7. Complete executable verification code

```python
import json
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

## 8. Reproducible result

### 8.1 Human-readable summary

The confirmatory run executed `180` trajectories:

```text
5 cases x 12 seeds x 3 timesteps = 180
```

Classification:

| Case | Expected passes per timestep | Observed at 0.01 | Observed at 0.005 | Observed at 0.0025 |
|---|---:|---:|---:|---:|
| elastic | 12 | 12 | 12 | 12 |
| gas | 0 | 0 | 0 | 0 |
| advected_gas | 0 | 0 | 0 | 0 |
| external_history | 0 | 0 | 0 | 0 |
| sham_elastic | 0 | 0 | 0 | 0 |

For the elastic case across registered timesteps:

```text
mean tracked-shape recovery: 0.991345 to 0.991370
minimum tracked-shape recovery: 0.979917
mean pair-structure recovery: 0.985584 to 0.985623
minimum pair-structure recovery: 0.969160
mean initial k_eff: 7.389056
minimum initial k_eff: 6.879927
maximum bulk-velocity error: 6.68443e-16
```

The sham showed why the perturbation gate matters:

```text
mean initial shape error: 0.00140136
mean k_eff: 13.50335
mean tracked recovery: approximately 0.9675
classification: rejected because E_shape(0) <= 0.05
```

The gas, advected gas, and external-history cases retained their deformation to floating-point tolerance and had `k_eff = 0`.

### 8.2 Timestep check

Relative differences between `dt=0.01` and `dt=0.0025` for elastic means were:

```json
{
  "pair_t_mean": 0.0027591239023565667,
  "recovery_pair_mean": 0.000039956053618954534,
  "recovery_shape_mean": 0.000025728081631261157,
  "shape_t_mean": 0.002944767394160772
}
```

All are below the frozen `0.01` limit. Classification was identical at all three steps.

### 8.3 Machine-readable compact output

```json
{
  "raw_row_count": 180,
  "raw_rows_canonical_json_sha256": "38583d9898a2f8d936a35791b43f275031088f333f73ad2c786a40045bc1c40f",
  "summary_canonical_json_sha256": "830c3851d2c246712b8737882bcb457ff74cc1315d61a420e48089eaae3b2856",
  "classification_by_dt": {
    "0.01": {"elastic": 12, "gas": 0, "advected_gas": 0, "external_history": 0, "sham_elastic": 0},
    "0.005": {"elastic": 12, "gas": 0, "advected_gas": 0, "external_history": 0, "sham_elastic": 0},
    "0.0025": {"elastic": 12, "gas": 0, "advected_gas": 0, "external_history": 0, "sham_elastic": 0}
  },
  "elastic": {
    "shape_0_mean": 0.25845593664874883,
    "k_eff_mean": 7.389055809538809,
    "k_eff_min": 6.87992733244465,
    "dt_0.01": {
      "shape_t_mean": 0.002232743248694602,
      "pair_t_mean": 0.0014646926134372334,
      "recovery_shape_mean": 0.9913701714366988,
      "recovery_shape_min": 0.9799340262803252,
      "recovery_pair_mean": 0.9856232926563692,
      "recovery_pair_min": 0.9691599329765039,
      "bulk_error_max": 2.237726045655905e-16
    },
    "dt_0.005": {
      "shape_t_mean": 0.0022370991767478522,
      "pair_t_mean": 0.0014673679870721692,
      "recovery_shape_mean": 0.9913533242646012,
      "recovery_shape_min": 0.9799224627192366,
      "recovery_pair_mean": 0.9855972949993911,
      "recovery_pair_min": 0.9691613510589283,
      "bulk_error_max": 6.684427777288335e-16
    },
    "dt_0.0025": {
      "shape_t_mean": 0.0022393375769757993,
      "pair_t_mean": 0.001468745063047155,
      "recovery_shape_mean": 0.9913446660402062,
      "recovery_shape_min": 0.9799167240915566,
      "recovery_pair_mean": 0.9855839126127108,
      "recovery_pair_min": 0.9691625441854588,
      "bulk_error_max": 5.79553433516819e-16
    }
  },
  "nulls": {
    "gas_advected_and_external_history": {
      "k_eff": 0.0,
      "recovery_magnitude": "floating_point_zero",
      "cohesive_count_total": 0
    },
    "sham_elastic": {
      "shape_0_mean": 0.0014013591613730697,
      "k_eff_mean": 13.503351386611358,
      "cohesive_count_total": 0,
      "failed_gate": "meaningful_perturbation"
    }
  }
}
```

The canonical raw-row digest is computed from `json.dumps(rows, sort_keys=True, separators=(",", ":"))`. The summary digest uses the same canonical JSON convention.

## 9. Independent sanity checks

1. Each spring contribution is equal and opposite, so total spring force is zero.
2. Relative damping sums to zero because `sum_i(v_i - mean(v)) = 0`.
3. Center-of-mass acceleration is therefore zero analytically.
4. The observed maximum bulk error was below `7e-16`, consistent with that invariant.
5. Gas cases have zero internal force by construction and yielded zero `k_eff`.
6. Two different geometry observers, tracked Procrustes shape and sorted pair distances, agreed.
7. Three timestep values retained classification and converged well inside the frozen tolerance.
8. The sham would have been a false repair claim without the independently required challenge-size gate.

## 10. What was actually established

```text
implementation:
    a synthetic spring-network fixture and observer ensemble were executed;

reproducible observation:
    the frozen observer separated all registered known-answer cases on held-out seeds;

cautious interpretation:
    causal restoring response can be distinguished from shape persistence and common translation
    in this deliberately simple class;

hypothesis:
    an analogous response may help distinguish a Lineum collective object from a vortex gas;

real-physics boundary:
    no claim about physical particles, Stoic pneuma, souls, or nature was tested.
```

## 11. Limitations and adversarial next controls

This fixture is intentionally easy and cannot yet justify application to P2.

Known limitations:

- point particles are not continuous fields;
- edge labels are fixed in the dynamics;
- the tracked-shape observer uses correspondence labels;
- the null gases have no internal interaction at all;
- the externally prepared case is numerically identical to the gas after source removal;
- no member birth, death, exchange, split, merge, topology change, field wake, boundary, or source ledger is represented;
- `k_eff` can be high for a trivially small challenge, hence the separate perturbation gate;
- the reference geometry is known exactly, unlike an unknown Lineum object;
- no noisy interacting gas, metastable glass, rotating fluid vortex population, or rigid kinematic template was tested.

Before actual Lineum use, a second fixture must add adversarial near-misses:

```text
interacting but non-restoring gas;
metastable glass that relaxes without recovering the reference;
externally clocked collective with source removal;
rigid template and shape-memory template;
member turnover with and without protocol reconstruction;
rotation and permutation ambiguity;
continuous-field smooth patch and phase-winding nulls;
observer learned only from pre-intervention data.
```

## 12. Root-programme impact matrix

| Root branch | Relation | Result impact |
|---|---|---|
| Collective-particle hypothesis | `supports` | A known-answer causal cohesion gate now exists for further adversarial development. |
| P2 vortex-gas remnant | `depends_on` | No P2 classification changed; exact P2 remains unrecovered. |
| Minimum-flux observer is non-identifying | `supports` | Force response and relational recovery add information beyond overlap and transport. |
| Source accounting | `supports` | Recovery occurred source-off and did not damp or inject bulk motion. |
| Protocol identity under turnover | `not_yet_compared` | Fixed membership makes this a later fixture. |
| Body versus residual taxonomy | `not_yet_compared` | No wake or residual state exists here. |
| Copying and heredity | `unaffected` | Cohesion is not reproduction. |
| Physical particle correspondence | `unaffected` | Synthetic validation supplies no evidence about nature. |

## 13. Current verdict

```text
known_answer_fixture = validated_within_declared_synthetic_domain
confirmatory_trajectories = 180
elastic_true_positive_rate = 1.0
registered_null_true_negative_rate = 1.0
timestep_classification_stability = passed
bulk_motion_invariant = passed
pneuma_as_field = not_supported
lineum_collective_cohesion = not_tested
p2_particle_status = unchanged
public_api_or_whitepaper_change = not_authorized
next_action = build_adversarial_near_miss_cohesion_fixture_before_any_lineum_application
```
