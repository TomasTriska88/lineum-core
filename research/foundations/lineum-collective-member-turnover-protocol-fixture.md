# Collective Member-Turnover Protocol Known-Answer Fixture

**Status:** validated known-answer fixture; no Lineum application executed  
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
**Cohesion predecessor:** `research/foundations/lineum-pneuma-cohesion-adversarial-near-miss-fixture.md`, version 0.2.0, blob `d58b227c0cdd88f7e3ae8903e7b4482aee17a7e2`  
**Object-definition predecessor:** `research/foundations/lineum-core-envelope-wake-and-attraction-preregistration.md`, version 0.2.0, blob `621cc5f9147dde4a3819e9fc2d3febe05e387cf8`  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Scope:** Validate a label-free observer of organization recovery after explicit member removal and insertion.  
**Central question:** Can a collective reconstruct its relational organization after 25% member turnover without permanent member identity or an active external organizer?  
**Current confidence:** high that the frozen observer passed the declared synthetic fixtures and timestep checks; low that the inserted global protocol represents any actual Lineum mechanism; no evidence yet for a Lineum collective particle, P2 identity, strictly local flocking, life, soul, or ancient encoded physics.

## 1. Answer first

The known-answer member-turnover fixture passed.

Four of sixteen members were removed and replaced by points at random positions. A dynamic protocol that continually rebuilt roles from the current population restored one collective ring in every held-out run, even after arbitrary array relabeling. Fixed member slots, a broken template, and a gas did not integrate the replacements. An external controller repaired the geometry but was rejected because it remained active, and a no-turnover sham was rejected because no material replacement occurred.

```text
confirmatory trajectories:        252
turnover-robust positives:          72 / 72
registered controls rejected:     180 / 180
false positives:                     0
false negatives:                     0
classification changes across dt:    0
```

This is the first synthetic result in this programme that directly demonstrates the distinction suggested by the flock analogy:

```text
the microscopic members can change while a declared higher-level organization recovers.
```

The protocol was inserted by design, uses the global centroid and global angular ordering, and already knows the target radius and equal-spacing rule. The result therefore validates the **observer and causal distinction**, not emergence of such a protocol from Lineum or from purely local rules.

## 2. Version history and preregistration receipt

Version 0.1.0 was committed before confirmatory execution:

```text
preregistration commit: c4d8b107454ee363bf563d425fe3659dc6a4817d
exploratory seeds excluded: 0..29
held-out seeds: 600..611
timesteps: 0.01, 0.005, 0.0025
population: 16
replaced members: 4
turnover fraction: 0.25
horizon: 8.0
thresholds, cases, and expected results: frozen
```

No threshold, force, case, seed, observer, or classification rule changed after the preregistration commit.

## 3. Case definitions

| Case | Construction | Frozen answer |
|---|---|---|
| `protocol` | Roles rebuilt each step from current centroid and angular ordering | turnover robust |
| `protocol_relabelled` | Same physical state after arbitrary array permutation | turnover robust |
| `fixed_slots` | Original labelled spring slots, no role reassignment | not robust |
| `broken_template` | New members disconnected from surviving old template | not robust |
| `turnover_gas` | Same replacement state, no relative force | not robust |
| `external_active` | External controller continuously assigns and repairs roles | not autonomous |
| `protocol_sham` | Dynamic protocol but no replaced members | not eligible |

## 4. Geometry, challenge, and inserted protocol

The reference population is a regular unit ring:

```text
R_i = [cos(2 pi i / 16), sin(2 pi i / 16)].
```

For a material challenge, four indices are sampled without replacement and replaced by random points with radii in `[0.15, 1.75]`, random angles, and small Gaussian noise. Every point begins with common velocity `[0.25, -0.10]`.

The dynamic protocol is permutation-invariant but not strictly local:

1. find the instantaneous centroid;
2. sort all current members by polar angle;
3. pull each member toward unit radius;
4. move each member tangentially toward its larger adjacent angular gap;
5. apply only relative damping;
6. subtract mean force so bulk motion remains free.

This rule intentionally embodies the Community-Rule/covenant abstraction from the parent audit: current members are assigned roles by a reconstructive protocol rather than by permanent biological or numerical identity. The historical motif is only provenance for the systems question.

## 5. Frozen label-free observer

The observer receives no old-to-new member mapping.

### 5.1 Pair structure

```text
E_pair = RMS(sort(all pair distances) - sort(reference pair distances))
         / mean(reference pair distances).
```

### 5.2 Radial organization

```text
E_radial = RMS(r_i - 1).
```

### 5.3 Cyclic angular organization

After sorting current polar angles, let `g_i` be cyclic gaps:

```text
E_gap = RMS(g_i - 2 pi / 16) / (2 pi / 16).
```

### 5.4 Participation

Every final member must have a nearest-neighbor distance between `0.70` and `1.30` times the regular-ring chord. This rejects a good-looking core plus isolated replacements.

### 5.5 Frozen verdict

```text
turnover fraction >= 0.25
external organizer absent
pair recovery by t=0.5 > 0.05
gap recovery by t=0.5 > 0.20
final pair recovery > 0.90
final gap recovery > 0.90
final radial error < 0.02
final gap error < 0.05
participation bounds pass
maximum RMS radius < 1.8
final radius ratio in [0.7, 1.3]
bulk-velocity error < 1e-8
```

All gates are required.

## 6. Complete executable verification code

```python
import hashlib
import json
import numpy as np

N = 16
RADIUS = 1.0
SEEDS = list(range(600, 612))
DTS = [0.01, 0.005, 0.0025]
T_FINAL = 8.0
T_EARLY = 0.5
CASES = [
    "protocol",
    "protocol_relabelled",
    "fixed_slots",
    "broken_template",
    "turnover_gas",
    "external_active",
    "protocol_sham",
]
POSITIVE_CASES = ["protocol", "protocol_relabelled"]
BULK = np.array([0.25, -0.10], dtype=float)

THETA = np.linspace(0.0, 2.0 * np.pi, N, endpoint=False)
REF = np.column_stack((np.cos(THETA), np.sin(THETA)))
EDGES = sorted({
    tuple(sorted((i, (i + offset) % N)))
    for i in range(N)
    for offset in (1, 2)
})
REST = np.asarray([np.linalg.norm(REF[j] - REF[i]) for i, j in EDGES])
COMPLETE = [(i, j) for i in range(N) for j in range(i + 1, N)]
REF_PAIR = np.sort(np.asarray([np.linalg.norm(REF[j] - REF[i]) for i, j in COMPLETE]))
EXPECTED_CHORD = 2.0 * RADIUS * np.sin(np.pi / N)


def turnover_state(seed, sham=False):
    rng = np.random.default_rng(seed)
    x = REF + rng.normal(scale=0.01, size=REF.shape)
    replaced = np.asarray([], dtype=int)
    if not sham:
        replaced = np.sort(rng.choice(N, 4, replace=False))
        angle = rng.uniform(-np.pi, np.pi, size=4)
        radius = rng.uniform(0.15, 1.75, size=4)
        x[replaced] = np.column_stack((radius * np.cos(angle), radius * np.sin(angle)))
        x[replaced] += rng.normal(scale=0.03, size=(4, 2))
    x -= x.mean(axis=0)
    v = np.repeat(BULK[None, :], N, axis=0)
    return x, v, replaced


def pair_error(x):
    distances = np.sort(np.asarray([
        np.linalg.norm(x[j] - x[i])
        for i, j in COMPLETE
    ]))
    return float(np.sqrt(np.mean((distances - REF_PAIR) ** 2)) / np.mean(REF_PAIR))


def ring_metrics(x):
    centered = x - x.mean(axis=0)
    radius = np.linalg.norm(centered, axis=1)
    radial_error = float(np.sqrt(np.mean((radius - RADIUS) ** 2)) / RADIUS)
    angle = np.mod(np.arctan2(centered[:, 1], centered[:, 0]), 2.0 * np.pi)
    angle = np.sort(angle)
    gaps = np.diff(np.concatenate((angle, [angle[0] + 2.0 * np.pi])))
    gap_error = float(
        np.sqrt(np.mean((gaps - 2.0 * np.pi / N) ** 2))
        / (2.0 * np.pi / N)
    )
    distance_matrix = np.linalg.norm(
        centered[:, None, :] - centered[None, :, :],
        axis=2,
    )
    np.fill_diagonal(distance_matrix, np.inf)
    nearest = distance_matrix.min(axis=1) / EXPECTED_CHORD
    return radial_error, gap_error, float(nearest.min()), float(nearest.max())


def rms_radius(x):
    centered = x - x.mean(axis=0)
    return float(np.sqrt(np.mean(np.sum(centered * centered, axis=1))))


def protocol_forces(x, v):
    centered = x - x.mean(axis=0)
    radius = np.linalg.norm(centered, axis=1)
    angle = np.mod(np.arctan2(centered[:, 1], centered[:, 0]), 2.0 * np.pi)
    order = np.argsort(angle)
    sorted_angle = angle[order]
    gaps = np.diff(np.concatenate((sorted_angle, [sorted_angle[0] + 2.0 * np.pi])))

    forces = np.zeros_like(x)
    for position, index in enumerate(order):
        previous_gap = gaps[position - 1]
        next_gap = gaps[position]
        unit = centered[index] / max(radius[index], 1e-12)
        tangent = np.array([-unit[1], unit[0]])
        forces[index] += -5.0 * (radius[index] - RADIUS) * unit
        forces[index] += 2.5 * (next_gap - previous_gap) * tangent

    forces -= forces.mean(axis=0)
    forces += -2.0 * (v - v.mean(axis=0))
    return forces


def spring_forces(x, v, edges, rest_lengths):
    forces = np.zeros_like(x)
    for index, (i, j) in enumerate(edges):
        delta = x[j] - x[i]
        distance = float(np.sqrt(np.dot(delta, delta)))
        if distance > 1e-12:
            force = 4.0 * (distance - rest_lengths[index]) * delta / distance
            forces[i] += force
            forces[j] -= force
    forces += -2.0 * (v - v.mean(axis=0))
    return forces


def external_forces(x, v):
    centered = x - x.mean(axis=0)
    angle = np.mod(np.arctan2(centered[:, 1], centered[:, 0]), 2.0 * np.pi)
    order = np.argsort(angle)
    offsets = np.angle(np.exp(1j * (angle[order] - THETA)))
    phase = np.angle(np.mean(np.exp(1j * offsets)))
    anchors = np.column_stack((np.cos(THETA + phase), np.sin(THETA + phase)))
    forces = np.zeros_like(x)
    for position, index in enumerate(order):
        forces[index] += -5.0 * (centered[index] - anchors[position])
    forces -= forces.mean(axis=0)
    forces += -2.0 * (v - v.mean(axis=0))
    return forces


def simulate(case, seed, dt):
    sham = case == "protocol_sham"
    x, v, replaced = turnover_state(seed, sham=sham)
    source_off = True

    if case == "protocol_relabelled":
        permutation = np.random.default_rng(seed + 10000).permutation(N)
        x = x[permutation]
        v = v[permutation]

    edges = None
    rest_lengths = None
    if case == "fixed_slots":
        edges = EDGES
        rest_lengths = REST
    elif case == "broken_template":
        replaced_set = set(replaced.tolist())
        retained = [
            (edge, rest)
            for edge, rest in zip(EDGES, REST)
            if edge[0] not in replaced_set and edge[1] not in replaced_set
        ]
        edges = [item[0] for item in retained]
        rest_lengths = np.asarray([item[1] for item in retained])

    pair_0 = pair_error(x)
    radial_0, gap_0, _, _ = ring_metrics(x)
    pair_early = None
    gap_early = None
    maximum_radius = rms_radius(x)

    steps = int(round(T_FINAL / dt))
    early_step = int(round(T_EARLY / dt))

    for step in range(steps):
        if case in ("protocol", "protocol_relabelled", "protocol_sham"):
            forces = protocol_forces(x, v)
        elif case in ("fixed_slots", "broken_template"):
            forces = spring_forces(x, v, edges, rest_lengths)
        elif case == "turnover_gas":
            forces = np.zeros_like(x)
        elif case == "external_active":
            source_off = False
            forces = external_forces(x, v)
        else:
            raise ValueError(case)

        v += dt * forces
        x += dt * v
        maximum_radius = max(maximum_radius, rms_radius(x))

        if step + 1 == early_step:
            pair_early = pair_error(x)
            _, gap_early, _, _ = ring_metrics(x)

    pair_final = pair_error(x)
    radial_final, gap_final, nearest_min, nearest_max = ring_metrics(x)
    recovery_pair_early = (pair_0 - pair_early) / pair_0
    recovery_gap_early = (gap_0 - gap_early) / gap_0
    recovery_pair = (pair_0 - pair_final) / pair_0
    recovery_gap = (gap_0 - gap_final) / gap_0
    turnover_fraction = 0.0 if sham else 0.25
    bulk_error = float(np.linalg.norm(v.mean(axis=0) - BULK))
    final_radius_ratio = rms_radius(x) / RADIUS
    bounded = bool(maximum_radius < 1.8 and 0.7 < final_radius_ratio < 1.3)
    integrated = bool(nearest_min > 0.70 and nearest_max < 1.30)

    verdict = bool(
        turnover_fraction >= 0.25
        and source_off
        and recovery_pair_early > 0.05
        and recovery_gap_early > 0.20
        and recovery_pair > 0.90
        and recovery_gap > 0.90
        and radial_final < 0.02
        and gap_final < 0.05
        and integrated
        and bounded
        and bulk_error < 1e-8
    )

    return {
        "case": case,
        "seed": seed,
        "dt": dt,
        "pair_0": float(pair_0),
        "radial_0": float(radial_0),
        "gap_0": float(gap_0),
        "recovery_pair_early": float(recovery_pair_early),
        "recovery_gap_early": float(recovery_gap_early),
        "recovery_pair": float(recovery_pair),
        "recovery_gap": float(recovery_gap),
        "radial_final": float(radial_final),
        "gap_final": float(gap_final),
        "nearest_ratio_min": float(nearest_min),
        "nearest_ratio_max": float(nearest_max),
        "turnover_fraction": turnover_fraction,
        "source_off": bool(source_off),
        "bounded": bounded,
        "integrated": integrated,
        "bulk_error": bulk_error,
        "turnover_robust": verdict,
    }


def summarize(rows):
    summary = {}
    for dt in DTS:
        summary[str(dt)] = {}
        for case in CASES:
            subset = [row for row in rows if row["dt"] == dt and row["case"] == case]
            summary[str(dt)][case] = {
                "n": len(subset),
                "pass_count": sum(row["turnover_robust"] for row in subset),
                "recovery_pair_early_mean": float(np.mean([row["recovery_pair_early"] for row in subset])),
                "recovery_gap_early_mean": float(np.mean([row["recovery_gap_early"] for row in subset])),
                "recovery_pair_mean": float(np.mean([row["recovery_pair"] for row in subset])),
                "recovery_pair_min": float(np.min([row["recovery_pair"] for row in subset])),
                "recovery_gap_mean": float(np.mean([row["recovery_gap"] for row in subset])),
                "recovery_gap_min": float(np.min([row["recovery_gap"] for row in subset])),
                "radial_final_max": float(np.max([row["radial_final"] for row in subset])),
                "gap_final_max": float(np.max([row["gap_final"] for row in subset])),
                "bulk_error_max": float(np.max([row["bulk_error"] for row in subset])),
                "source_off_count": sum(row["source_off"] for row in subset),
                "turnover_fraction_mean": float(np.mean([row["turnover_fraction"] for row in subset])),
            }
    return summary


def relative_difference(a, b):
    return abs(a - b) / max(abs(b), 1e-15)


def verify(rows, summary):
    expected = {
        "protocol": 12,
        "protocol_relabelled": 12,
        "fixed_slots": 0,
        "broken_template": 0,
        "turnover_gas": 0,
        "external_active": 0,
        "protocol_sham": 0,
    }

    for dt in DTS:
        block = summary[str(dt)]
        for case, expected_count in expected.items():
            assert block[case]["pass_count"] == expected_count
        assert max(block[case]["bulk_error_max"] for case in CASES) < 1e-8
        assert block["external_active"]["recovery_pair_min"] > 0.90
        assert block["external_active"]["recovery_gap_min"] > 0.90
        assert block["external_active"]["source_off_count"] == 0
        assert block["protocol_sham"]["recovery_pair_min"] > 0.90
        assert block["protocol_sham"]["recovery_gap_min"] > 0.90
        assert block["protocol_sham"]["turnover_fraction_mean"] == 0.0

        gas = [row for row in rows if row["dt"] == dt and row["case"] == "turnover_gas"]
        assert max(abs(row["recovery_pair"]) for row in gas) < 1e-8
        assert max(abs(row["recovery_gap"]) for row in gas) < 1e-8

        original = sorted(
            [row for row in rows if row["dt"] == dt and row["case"] == "protocol"],
            key=lambda row: row["seed"],
        )
        relabelled = sorted(
            [row for row in rows if row["dt"] == dt and row["case"] == "protocol_relabelled"],
            key=lambda row: row["seed"],
        )
        for first, second in zip(original, relabelled):
            assert first["turnover_robust"] == second["turnover_robust"]
            for key in (
                "pair_0", "radial_0", "gap_0",
                "recovery_pair_early", "recovery_gap_early",
                "recovery_pair", "recovery_gap",
                "radial_final", "gap_final",
            ):
                assert abs(first[key] - second[key]) < 1e-10

    coarse = summary[str(0.01)]
    fine = summary[str(0.0025)]
    for case in POSITIVE_CASES:
        assert relative_difference(coarse[case]["recovery_pair_mean"], fine[case]["recovery_pair_mean"]) < 0.01
        assert relative_difference(coarse[case]["recovery_gap_mean"], fine[case]["recovery_gap_mean"]) < 0.01


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
| protocol | 12 | 12 | 12 | 12 |
| protocol relabelled | 12 | 12 | 12 | 12 |
| fixed slots | 0 | 0 | 0 | 0 |
| broken template | 0 | 0 | 0 | 0 |
| turnover gas | 0 | 0 | 0 | 0 |
| active external controller | 0 | 0 | 0 | 0 |
| protocol sham | 0 | 0 | 0 | 0 |

### 7.3 Machine-readable checkpoint

```json
{
  "raw_row_count": 252,
  "raw_rows_canonical_json_sha256": "12488c9c625e025ed24745f3a6ad80d90a67254acc5258370bac5d8622158f17",
  "summary_canonical_json_sha256": "52f67f6896d8d4d768577ca147199e04e35347401c8ceea2a649b37bda7f1ce3",
  "positive_recovery_ranges": {
    "pair_mean": [0.9992182682653242, 0.9992617413839343],
    "gap_mean": [0.9997167526681335, 0.9997327210596786],
    "maximum_final_radial_error": 0.00013260419310918555,
    "maximum_final_gap_error": 0.00023392881125974019
  },
  "controls": {
    "fixed_slots_pair_recovery_range": [-0.5033838636079552, -0.5030658992030251],
    "broken_template_pair_recovery_range": [-0.00503870349341016, -0.0050386588212312],
    "turnover_gas_absolute_recovery": "floating_point_zero",
    "external_active_pair_recovery_range": [0.9991787175738032, 0.999224325201835],
    "external_active_gap_recovery_range": [0.9996428991942131, 0.9996627361586921],
    "external_active_source_off_count_per_dt": 0,
    "protocol_sham_pair_recovery_range": [0.9996818459370257, 0.9996999165550694],
    "protocol_sham_turnover_fraction": 0.0
  },
  "maximum_bulk_velocity_error": 8.886119947416683e-16,
  "positive_pair_coarse_fine_relative_difference_max": 0.00004350712951390797,
  "positive_gap_coarse_fine_relative_difference_max": 0.000015972915830731634
}
```

The canonical digests use `json.dumps(..., sort_keys=True, separators=(",", ":"))`.

## 8. Decision-relevant observations

### 8.1 Membership labels were unnecessary

The protocol and randomly relabelled protocol matched in all declared metrics within `1e-10` for every seed and timestep. Array identity was not used by the dynamics or observer.

### 8.2 New members were genuinely integrated in the toy model

All positive runs ended with every member's nearest-neighbor distance within the frozen participation range. The result was not produced by a good core plus isolated replacements.

### 8.3 Fixed slots did not substitute for a reconstructive protocol

The fixed-slot network moved away from the reference pair distribution after arbitrary member replacement, with mean pair recovery near `-0.503`. It retained internal forces but lacked a mechanism for assigning replacements to current collective roles.

### 8.4 Old partial structure did not integrate replacements

Removing all template edges incident to replaced members left the old subnetwork partially active but produced no collective repair. This distinguishes persistence of surviving structure from restoration of the complete population.

### 8.5 External and sham gates were independently necessary

The external controller and no-turnover sham both achieved more than `99.9%` final pair and gap recovery. They failed solely because the former was externally maintained and the latter had no member turnover. Geometry alone would have produced two false claims.

## 9. Evidence layers

```text
implementation:
    an explicitly engineered global role-reconstruction protocol and six controls were executed;

reproducible observation:
    the frozen label-free observer separated every held-out known-answer case;

cautious interpretation:
    higher-level organization can be operationally tracked across component replacement
    without tracking microscopic identity in this synthetic system;

hypothesis:
    a comparable observer may test whether a Lineum vortex collective preserves relations
    while individual detected defects turn over;

real-physics boundary:
    no physical particle, living system, soul, or actual Lineum state was tested.
```

## 10. Limitations and next discriminator

This result still inserts the answer into the toy dynamics:

- the target radius is declared;
- equal angular spacing is declared;
- the protocol has global centroid and global angular ordering;
- the population count remains constant after replacement;
- all members are identical points;
- no continuous field, phase winding, wake, resource stock, boundary, or history field exists;
- no mechanism must discover the protocol;
- no reproduction or descendant is created.

The next meaningful discriminator is therefore a **local-versus-global protocol comparison**:

```text
strictly local neighbor rules with no global centroid or ordering;
global protocol positive control;
local rules plus a hidden common clock;
local rules plus external boundary guidance;
matched gas and fixed-template controls;
member turnover, split, obstacle, and source-off challenges;
observer frozen before held-out cases.
```

This will determine whether turnover-robust organization can arise from local interactions rather than from a globally informed controller embedded inside the dynamics.

## 11. Root-programme impact matrix

| Root branch | Relation | Result impact |
|---|---|---|
| Collective-particle hypothesis | `supports` | The defining organization-with-member-turnover distinction is operationally measurable in a known-answer system. |
| Mechanical cohesion fixtures | `supports` | Adds a stronger gate beyond shape repair with fixed components. |
| P2 vortex-gas remnant | `depends_on` | P2 remains unrecovered and untested. |
| Static recipe versus live state | `constrains` | Fixed slots and surviving old structure failed to integrate replacements. |
| Protocol identity | `supports` | A dynamic current-population protocol succeeded where fixed membership structures failed. |
| Emergence from local rules | `not_yet_compared` | Current protocol uses global information and was inserted by design. |
| Copying and heredity | `unaffected` | No descendant or inherited content was produced. |
| Physical correspondence | `unaffected` | Synthetic observer success says nothing about nature. |

## 12. Current verdict

```text
member_turnover_known_answer_fixture = validated_within_declared_synthetic_domain
confirmatory_trajectories = 252
turnover_robust_true_positive_rate = 1.0
registered_control_true_negative_rate = 1.0
member_label_invariance = passed
replacement_participation_gate = passed
external_source_gate = independently_exercised_and_passed
material_turnover_gate = independently_exercised_and_passed
timestep_classification_stability = passed
organization_persists_across_member_replacement_in_toy = supported_by_inserted_global_protocol
strictly_local_emergent_protocol = not_tested
lineum_collective_identity = not_tested
p2_particle_status = unchanged
public_api_or_whitepaper_change = not_authorized
clickup_checkpoint_sync = failed_once_connector_tool_not_found_no_retry
next_action = preregister_local_versus_global_turnover_protocol_comparison
```
