# Collective Member-Turnover Protocol Known-Answer Fixture

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
**Cohesion predecessor:** `research/foundations/lineum-pneuma-cohesion-adversarial-near-miss-fixture.md`, version 0.2.0, blob `d58b227c0cdd88f7e3ae8903e7b4482aee17a7e2`  
**Object-definition predecessor:** `research/foundations/lineum-core-envelope-wake-and-attraction-preregistration.md`, version 0.2.0, blob `621cc5f9147dde4a3819e9fc2d3febe05e387cf8`  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Scope:** Validate a label-free observer of organization recovery after explicit member removal and insertion.  
**Central question:** Can a collective reconstruct its relational organization after 25% member turnover without relying on permanent member identity or an active external organizer?  
**Current confidence:** high that the synthetic cases have known causal differences; medium that the frozen observer will classify held-out cases across timestep refinement; no result yet on confirmatory seeds, self-generated local flocking, actual Lineum vortices, P2, physical particles, life, soul, or ancient encoded physics.

## 1. Answer first

Mechanical cohesion is weaker than collective identity.

A rubber frame can restore its shape while every component remains permanently assigned to one slot. A flock-like collective must do something harder: lose members, accept replacements, and rebuild the relevant relations without requiring the replacements to be the same microscopic individuals.

This fixture replaces `4/16 = 25%` of a ring collective with new points at random positions. It then compares:

```text
a label-free dynamic protocol that reorders and reintegrates all current members;
the same protocol after arbitrary array relabeling;
a fixed slot/template network;
a template whose edges to replaced members are removed;
a turnover gas;
an active external repair controller;
a no-turnover sham.
```

The observer uses only population geometry and source accounting. It does not know the final assignment of members to positions.

A pass validates only a synthetic **turnover-robust organization observer**. The dynamic protocol is inserted by design and uses the global centroid and angular ordering; it is not evidence that such a protocol emerges from the Lineum equation or from strictly local rules.

## 2. Exploratory history and held-out boundary

Exploratory development used seeds `0..29` and is excluded from the retained result.

Frozen confirmatory set:

```text
held-out seeds: 600..611
timesteps: 0.01, 0.005, 0.0025
horizon: 8.0 model units
early horizon: 0.5 model units
population: 16
replaced members: 4
turnover fraction: 0.25
```

No confirmatory output for seeds `600..611` existed when this version was committed.

## 3. Known-answer cases

### 3.1 Dynamic protocol

At every step, members are sorted by angle around the instantaneous centroid. Radial forces restore a declared radius, while tangential forces move each member toward the larger of its adjacent angular gaps. The graph is rebuilt from the current population rather than retained by member label.

```text
turnover recovery = present by construction
external source during challenge = absent
expected verdict = turnover robust
```

### 3.2 Dynamic protocol relabelled

The same state is randomly permuted in array order before evolution. No force or observer may depend on that order.

```text
same physical process under relabeling
expected verdict = turnover robust
```

### 3.3 Fixed slots

A sparse spring graph retains original member-slot labels and reference distances. Replacements inherit arbitrary removed array slots but no role reassignment mechanism.

```text
fixed internal template = present
label-free reintegration protocol = absent
expected verdict = not turnover robust
```

### 3.4 Broken template

All template edges incident to replaced indices are removed. Surviving members retain a partial network; new members are disconnected.

```text
partial old organization = present
new-member integration = absent
expected verdict = not turnover robust
```

### 3.5 Turnover gas

The same turnover state translates without internal force.

```text
member turnover = present
reorganization = absent
expected verdict = not turnover robust
```

### 3.6 Active external controller

An external controller sorts members and continuously pulls them toward a regular ring assignment. It should repair geometry but fail source-off autonomy.

```text
geometric recovery = present
external organizer = active
expected verdict = not turnover robust
```

### 3.7 Protocol sham

The dynamic protocol receives only tiny position noise and no member replacement.

```text
repair ability = present
material turnover challenge = absent
expected verdict = not eligible
```

## 4. Frozen geometry and turnover challenge

The reference population is a regular ring:

```text
R_i = [cos(2 pi i / 16), sin(2 pi i / 16)].
```

All members receive small position noise. For non-sham cases, four indices are sampled without replacement. Their points are replaced by independent positions with random angle and radius uniformly sampled from `[0.15, 1.75]`, plus Gaussian noise of standard deviation `0.03`.

Every member begins with common velocity

```text
v_bulk = [0.25, -0.10].
```

## 5. Frozen observer

The observer removes translation and uses no member correspondence.

### 5.1 Pair-distance error

```text
E_pair = RMS(sort(all pair distances) - sort(reference pair distances))
         / mean(reference pair distances).
```

### 5.2 Radial error

```text
E_radial = RMS(r_i - 1).
```

### 5.3 Angular-gap error

Sort polar angles around the instantaneous centroid. For cyclic gaps `g_i`,

```text
E_gap = RMS(g_i - 2 pi / 16) / (2 pi / 16).
```

### 5.4 Participation

Let each member's nearest-neighbor distance be divided by the regular-ring chord length. Final integration requires

```text
minimum ratio > 0.70
maximum ratio < 1.30.
```

This rejects an apparently good aggregate made from a dense clump plus isolated replacements.

### 5.5 Frozen gates

```text
G_turnover = replaced fraction >= 0.25
G_source_off = no external organizer active during challenge
G_early_pair = pair recovery by t=0.5 > 0.05
G_early_gap = angular-gap recovery by t=0.5 > 0.20
G_pair = final pair recovery > 0.90
G_gap = final angular-gap recovery > 0.90
G_radial = final radial error < 0.02
G_gap_absolute = final angular-gap error < 0.05
G_participation = nearest-neighbor ratio bounds pass
G_bounded = maximum RMS radius < 1.8 and final radius ratio in [0.7, 1.3]
G_bulk = final bulk-velocity error < 1e-8
```

```text
turnover_robust = all eleven gates pass.
```

## 6. Frozen expected classification

For every held-out seed and timestep:

```text
protocol              -> turnover robust
protocol_relabelled   -> turnover robust
fixed_slots           -> not turnover robust
broken_template       -> not turnover robust
turnover_gas          -> not turnover robust
external_active       -> not turnover robust
protocol_sham         -> not turnover robust
```

Additional frozen checks:

```text
protocol and protocol_relabelled:
    all observer metrics match within 1e-10 for the same seed and timestep;

external_active:
    final pair and gap recovery exceed 0.90,
    but source-off count is zero;

protocol_sham:
    final pair and gap recovery exceed 0.90,
    but turnover fraction is zero;

turnover_gas:
    absolute final pair and gap recovery remain below 1e-8.
```

Classification must remain unchanged across all three timesteps. For both positive cases, coarse-versus-fine relative differences in mean final pair and gap recovery must remain below `0.01`.

## 7. Complete executable verification code

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

## 8. Analytic sanity checks

1. Protocol radial and angular forces are mean-subtracted, so they do not accelerate the center of mass.
2. Spring forces are equal and opposite; relative damping sums to zero.
3. The observer uses sorted pair distances, radial distributions, sorted angular gaps, and nearest-neighbor participation, none of which uses member identity.
4. The relabelled protocol is numerically the same physical state under array permutation.
5. The external controller should recover geometry but is explicitly marked source-active.
6. The sham should recover tiny noise but has zero turnover fraction.
7. The gas has no relative force and therefore cannot change its co-moving geometry.
8. A positive protocol is inserted by design; the fixture tests the observer, not emergence of the protocol.

## 9. Result placeholder

```text
confirmatory_seeds_600_to_611 = not_executed_at_commit
fixture_verdict = preregistered
```

## 10. Interpretation boundary

A pass will establish only that the observer recognizes organization recovery after synthetic member replacement and rejects the registered controls.

It will not establish:

```text
strictly local flocking rules;
self-generated protocol or template;
continuous-field vortex membership;
Lineum collective identity;
P2 particle status;
copying, heredity, reproduction, life, agency, consciousness, ego, or soul;
ancient encoded physics.
```

## 11. Root-programme impact matrix

| Root branch | Relation | Expected impact |
|---|---|---|
| Collective-particle hypothesis | `supports` | Tests the defining claim that organization can outlive microscopic membership. |
| Mechanical cohesion fixtures | `depends_on` | Turnover robustness is a stronger gate built on prior source-off cohesion controls. |
| P2 remnant | `depends_on` | No actual P2 state is used. |
| Static recipe versus live state | `constrains` | A fixed template is tested separately from a dynamic role-reconstruction protocol. |
| Copying and heredity | `unaffected` | Replacement of members is not creation of a descendant. |
| Physical correspondence | `unaffected` | Synthetic observer validation says nothing about nature. |

## 12. Current verdict

```text
member_turnover_fixture = preregistered
confirmatory_execution = pending
held_out_seeds = frozen_600_to_611
observer_thresholds = frozen
lineum_application = not_authorized
next_action = execute_exact_embedded_code_then_record_complete_output
```
