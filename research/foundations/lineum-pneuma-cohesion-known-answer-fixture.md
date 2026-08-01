# Distributed Cohesion Known-Answer Fixture

**Status:** active negative-result checkpoint; observer unsupported under tested conditions; no Lineum or physical validation claimed  
**Version:** 0.2.0  
**Evidence cutoff:** 2026-08-01  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`  
**Recovered root version:** 0.4.14  
**Root evidence cutoff:** 2026-07-29  
**Root blob SHA:** `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, version 0.3.0, evidence cutoff 2026-07-31, blob `5304874451caf32313ad0e8e3c59e53958698d79`  
**Immediate conceptual predecessor:** `research/foundations/lineum-gnostic-enochic-dead-sea-scrolls-metaphor-audit.md`, version 0.2.0, blob `aa7895df7e66ff348159c8ecbb6d06a92f22950c`  
**Related collective-object preregistration:** `research/foundations/lineum-core-envelope-wake-and-attraction-preregistration.md`, version 0.2.0, blob `621cc5f9147dde4a3819e9fc2d3febe05e387cf8`  
**Related reduction-first report:** `research/foundations/lineum-mu-branch-relative-identity-and-entanglement-hypothesis.md`, version 0.2.0, blob `b55bc1639fc8ed6efa7b8286e9113afa88ee298c`  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Scope:** A synthetic known-answer test of whether a frozen observer can distinguish an autonomously self-restoring distributed collective from a matched gas, a rigidly transported deformation, an externally driven template, and a geometrically convincing but membership-scrambled template. This report does not execute the Lineum PDE and does not test P2.  
**Central question:** Can a label-blind combination of geometric recovery, relational continuity, member-removal robustness, and source-off autonomy identify distributed cohesion without mistaking persistence, transport, common-clock control, or repeated resampling for an object?  
**Current confidence:** high that all four negative controls were correctly rejected; high that the preregistered fixture failed because the inserted elastic collective passed zero of twenty-four seeds; high that the failure is not explained by the tested invariance or timestep checks; unresolved whether the decisive mismatch belongs primarily to the synthetic collective, endpoint observer, perturbation horizon, or definition of identity after member loss; zero evidence that a Lineum state has distributed cohesion or that historical `pneuma` names a physical field.

## 1. Answer first

The historical inspiration is translated into one narrow systems question:

```text
Does the collective restore its own organization after deformation and member loss,
or does it merely keep moving, keep a similar outline, or obey an external controller?
```

The word `pneuma` is not introduced into the Lineum ontology, equation, public package, or whitepaper. In this report, `distributed cohesion` is an operational property, not a substance:

```text
distributed cohesion candidate
    = autonomous deformation recovery
    + relational continuity
    + robustness to bounded member removal
    + survival after external synchronization is absent
    + rejection of matched non-identifying controls
```

The first frozen observer did not pass its known-answer gate. It successfully rejected gas, rigid transport, external control after source removal, and a recurring shape with scrambled membership. However, the inserted elastic collective recovered only about half of the imposed deformation within the frozen readout windows and therefore failed the preregistered candidate thresholds in every seed.

No threshold was changed. The observer is classified:

```text
unsupported_under_tested_conditions
```

This is a failure of the current fixture-observer pair, not evidence against collective particles, Lineum, or any physical theory.

## 2. Inherited constraints

The root programme establishes that:

- the current coherent source is a software pump rather than a demonstrated physical fuel;
- centered stochastic activity can generate dense defects, but no stable localized particle has been demonstrated;
- the existing minimum-flux observer is non-identifying and can be passed by smooth transported disorder;
- P2 is a reproducible source-off multi-defect population result, not an individual or collective particle result;
- exact software continuation is not autonomous repair or heredity;
- no synthetic toy success may promote a physical-particle, soul, spirit, quantum, gravity, or cosmology claim.

Therefore this fixture is an observer prerequisite only. It cannot validate Lineum by construction.

## 3. Frozen fixture classes

All classes use `N = 32` labeled points in two dimensions, initialized near the same elliptical ring, with the same translational drift and matched small perturbations. Labels exist only to measure known-answer relational truth. Geometry metrics are permutation invariant; relational metrics use temporal associations that a later Lineum application must replace with a frozen uncertainty-aware vortex tracker.

### 3.1 C0 — autonomous elastic collective

The reference geometry is

```text
q_i = (cos(theta_i), 0.70 sin(theta_i)),
theta_i = 2 pi i / N.
```

Each point is connected to its four nearest reference neighbors. The dynamics use damped springs with reference edge lengths and no absolute-position pinning:

```text
m x_i'' = -k_s sum_j ((|x_i-x_j|-l_ij) unit_ij)
          -gamma (v_i-v_mean)
          + eta_i(t).
```

After member removal, the reference graph is rebuilt among the surviving points from their predeclared reference coordinates. This is an inserted known-answer repair protocol. It is not claimed to emerge in Lineum.

### 3.2 C1 — matched ballistic gas

The points share the same initial state and mean drift but have no restoring graph:

```text
x_i'' = eta_i(t).
```

It may preserve population density briefly but should not restore the declared relational geometry.

### 3.3 C2 — rigidly transported deformation

All points retain the deformed configuration and translate together. This control preserves membership, adjacency, and boundedness while lacking recovery.

### 3.4 C3 — externally driven template

While the controller is enabled, each point is pinned to a moving reference slot:

```text
m x_i'' = -k_p (x_i - (q_i + c(t))) - gamma_p (v_i-u).
```

The controller is removed before the second deformation. This class tests whether apparent cohesion is only common-clock or external-template enforcement.

### 3.5 C4 — membership-scrambled template

At each observation step, the same point labels are randomly reassigned among the moving reference slots with small matched noise. The outline and pair-distance distribution remain convincing, but member-to-role continuity is absent. This is a strong control against declaring a recurring shape to be one persistent collective.

## 4. Frozen protocol

```text
seeds:                 0 through 23
points:                32
integration step:      dt = 0.01
steps:                 1000
mean drift:            (0.15, 0.05)
small acceleration SD: 0.002 for dynamical classes
spring stiffness:      k_s = 18
relative damping:      gamma = 2.5
pin stiffness:         k_p = 18
pin damping:           gamma_p = 4
controller removal:    step 400
first deformation:     step 100
first readout:         step 300
second deformation:    step 500
second readout:        step 700
member removal:        step 750
third deformation:     step 750 after removal
third readout:         step 950
removed fraction:      0.20, rounded to the nearest point
```

The affine deformation about the instantaneous centroid is frozen as:

```text
A = [[1.45, 0.15],
     [0.00, 0.65]].
```

The same seed controls initial noise, acceleration noise, removed members, and membership scrambling across matched classes.

## 5. Frozen observables

### 5.1 Permutation-invariant shape error

For the active members, compute all pairwise distances, sort them, and compare them with the corresponding sorted reference distances:

```text
E_shape = ||sort(D_current) - sort(D_reference)||_2
          / max(||sort(D_reference)||_2, epsilon).
```

This is invariant to translation, rotation, reflection, and point permutation. It deliberately cannot detect membership scrambling by itself.

### 5.2 Recovery ratio

For each intervention:

```text
R = (E_just_after - E_readout) / max(E_just_after, epsilon).
```

`R = 1` is full geometric recovery; `R = 0` is no recovery; negative values indicate worsening.

### 5.3 Relational continuity

At each readout, construct a four-nearest-neighbor graph using persistent point labels and compare it with the reference graph on the same surviving labels:

```text
J_relation = |E_current intersect E_reference| / |E_current union E_reference|.
```

This known-answer metric distinguishes role continuity from a repeatedly reconstructed outline. A later Lineum observer may not use hidden true labels; it must use a frozen tracker and propagate assignment uncertainty.

### 5.4 Escape fraction

```text
F_escape = fraction of active points farther than 2.5 reference RMS radii
           from the active centroid.
```

This rejects apparent recovery accompanied by unbounded dispersal.

### 5.5 Independent secondary geometry check

A separate observer compares covariance eigenvalue ratios and radial quantiles after centering. It must agree on the sign of recovery with the pair-distance observer in at least 90% of all seed-class-intervention cells.

## 6. Frozen candidate rule

A seed is classified as a distributed-cohesion candidate only when all conditions hold:

```text
R_after_controller_removal >= 0.75
R_after_member_removal     >= 0.60
J_relation_after_off       >= 0.65
J_relation_after_removal   >= 0.55
F_escape_final             <= 0.10
secondary_geometry_agrees  = true
```

The first deformation while the external controller is still available is descriptive only. It tests the expected false positive in C3 but is not part of the final candidate rule.

## 7. Fixture-level acceptance and failure conditions

The observer fixture passes only if:

```text
C0 autonomous collective: at least 20 of 24 seeds pass;
C1 ballistic gas:         at most 4 of 24 seeds pass;
C2 rigid deformation:     at most 4 of 24 seeds pass;
C3 driven template:       at most 4 of 24 seeds pass;
C4 scrambled template:    at most 4 of 24 seeds pass.
```

Additional hard checks:

1. Translation, rotation, reflection, and permutation change `E_shape` by less than `1e-10` on an exact fixture.
2. Repeating eight C0 and C3 seeds with `dt = 0.005` changes median recovery ratios and relational scores by less than `0.05`.
3. No threshold may be changed after viewing outcomes.
4. A failed class or failed hard check makes the observer `unsupported_under_tested_conditions`; no parameter tuning follows in the same lane.

## 8. Outcome interpretation

```text
fixture passes:
    the observer can distinguish the five inserted causal classes in this synthetic domain;
    application to Lineum becomes permissible but remains unvalidated;

C0 fails:
    the observer misses known autonomous cohesion or the synthetic implementation is defective;

C1 or C2 passes:
    motion, boundedness, or preserved adjacency is being mistaken for repair;

C3 passes:
    externally maintained order is being mistaken for source-off autonomy;

C4 passes:
    recurring geometry is being mistaken for persistent relational identity;

invariance or timestep check fails:
    the result is numerically or observer dependent and cannot advance.
```

## 9. Root-programme impact before execution

| Root branch | Relation | Preregistered effect |
|---|---|---|
| P2 multi-defect remnant | `depends_on` | No P2 interpretation changes unless this fixture passes and exact P2 is later recovered. |
| Collective-object preregistration | `supports` | Supplies a known-answer prerequisite for relational and repair observers. |
| Minimum-flux observer limitation | `supports` | Explicitly rejects transport and recurring-shape false positives. |
| Current source accounting | `unaffected` | The synthetic controller is declared and is not physical fuel. |
| Copying and heredity | `unaffected` | Member-removal recovery is not reproduction or lineage. |
| Mu reduction-first programme | `unaffected` | No new field or memory ontology is introduced. |
| Physical particle correspondence | `unaffected` | Synthetic classification has no direct empirical force. |

## 10. Execution environment and procedure

The fixture was executed once in ChatGPT Python without importing repository code.

```text
Python:   3.13.5
NumPy:    2.3.5
SciPy:    1.17.0
pandas:   2.2.3
Platform: Linux 6.12.13 x86_64, glibc 2.41
```

The exact script is retained in Section 15. It generated all 120 primary trajectories, the exact-transform invariance checks, sixteen timestep-comparison pairs, and the independent geometry-sign comparison in one execution path.

## 11. Machine-readable result

```json
{
  "invariance": {
    "base": 0.0,
    "max_abs": 1.623027463894968e-16,
    "permutation": 0.0,
    "reflection": 0.0,
    "rotation": 9.032353532909287e-17,
    "translation": 1.623027463894968e-16
  },
  "secondary_sign_agreement": {
    "agree": 358,
    "fraction": 0.9944444444444445,
    "total": 360
  },
  "summary": {
    "driven": {
      "F3_median": 0.07692307692307693,
      "J2_median": 0.8648648648648649,
      "J2_range": [0.8533333333333334, 0.8648648648648649],
      "J3_median": 0.45,
      "J3_range": [0.39759036144578314, 0.5061728395061729],
      "R1_median": 0.9853468228638401,
      "R2_median": -0.022032216945667978,
      "R2_range": [-0.022727723577807106, -0.02150493002309513],
      "R3_median": -0.008862380004259419,
      "R3_range": [-0.00943565125162642, -0.008559848139826794],
      "pass_count": 0
    },
    "elastic": {
      "F3_median": 0.0,
      "J2_median": 0.9209109730848861,
      "J2_range": [0.8888888888888888, 0.9696969696969697],
      "J3_median": 0.5337899543378996,
      "J3_range": [0.43209876543209874, 0.6086956521739131],
      "R1_median": 0.545135862349024,
      "R2_median": 0.5633817439120175,
      "R2_range": [0.5629517543650207, 0.5636192910369611],
      "R3_median": 0.523471308255951,
      "R3_range": [0.41505708954367576, 0.6153314704747902],
      "pass_count": 0
    },
    "gas": {
      "F3_median": 0.5,
      "J2_median": 0.4791666666666667,
      "J2_range": [0.41836734693877553, 0.5384615384615384],
      "J3_median": 0.4,
      "J3_range": [0.3409090909090909, 0.45348837209302323],
      "R1_median": -0.0013589470613820866,
      "R2_median": -0.0008693052618024277,
      "R2_range": [-0.00502875035339248, 0.005894426025904694],
      "R3_median": -0.0003431873957885495,
      "R3_range": [-0.0036118008189243117, 0.003765686662375178],
      "pass_count": 0
    },
    "rigid": {
      "F3_median": 0.5,
      "J2_median": 0.44103723963812325,
      "J2_range": [0.39603960396039606, 0.5],
      "J3_median": 0.4,
      "J3_range": [0.32558139534883723, 0.43373493975903615],
      "R1_median": -1.2737827731181265e-14,
      "R2_median": -5.90204582278657e-15,
      "R2_range": [-6.342403577730315e-15, -5.497538417063219e-15],
      "R3_median": -1.7346283882487594e-15,
      "R3_range": [-2.282881682638965e-15, -9.69386584068396e-16],
      "pass_count": 0
    },
    "scrambled": {
      "F3_median": 0.0,
      "J2_median": 0.06666666666666667,
      "J2_range": [0.024, 0.09401709401709402],
      "J3_median": 0.0899856166846458,
      "J3_range": [0.04854368932038835, 0.15789473684210525],
      "R1_median": 0.9766330704799822,
      "R2_median": 0.9759778352923564,
      "R2_range": [0.9729340629748442, 0.9785098384703864],
      "R3_median": 0.9740611921653045,
      "R3_range": [0.968302649294104, 0.9824785440284912],
      "pass_count": 0
    }
  },
  "timestep_convergence_median_absolute_differences": {
    "driven": {
      "dJ2": 0.0,
      "dJ3": 0.0,
      "dR1": 0.0011101347500470093,
      "dR2": 0.0015812175165893002,
      "dR3": 0.0004940959522504495
    },
    "elastic": {
      "dJ2": 0.0,
      "dJ3": 0.0,
      "dR1": 0.00012235408303323814,
      "dR2": 0.00013487420237573433,
      "dR3": 0.0009955061829211576
    }
  }
}
```

## 12. Human-readable result

### 12.1 Fixture verdict

```text
C0 autonomous elastic collective: 0/24 pass; required at least 20/24 -> FAIL
C1 ballistic gas:                 0/24 pass; allowed at most 4/24 -> PASS control
C2 rigid deformation:             0/24 pass; allowed at most 4/24 -> PASS control
C3 externally driven template:    0/24 pass; allowed at most 4/24 -> PASS control
C4 membership-scrambled template: 0/24 pass; allowed at most 4/24 -> PASS control

complete fixture verdict: unsupported_under_tested_conditions
```

### 12.2 What worked

The observer rejected every negative control.

- The gas and rigid classes showed essentially zero geometric recovery and ended with median escape fraction `0.50`.
- The externally driven template recovered `98.53%` of the first deformation while the controller existed, then worsened slightly after the controller was removed. This confirms that the source-off condition distinguishes imposed order from autonomous recovery.
- The membership-scrambled template recovered about `97.6%` of geometric shape while its median relational Jaccard scores remained only `0.0667` and `0.0900`. This confirms that geometry alone would have produced a strong false positive.
- Translation, rotation, reflection, and permutation invariance passed by more than five orders of magnitude relative to the `1e-10` threshold.
- Timestep-halving checks passed. All median absolute differences were below `0.0016`, far below the frozen `0.05` threshold.
- The independent geometry observer agreed on recovery direction in `358/360 = 99.44%` of cells, above the required `90%`.

### 12.3 What failed

The inserted elastic collective remained bounded, preserved most relations, and moved toward its reference geometry, but did not recover enough by the frozen deadlines:

```text
median source-off recovery:       0.5634 versus required 0.75
median post-removal recovery:     0.5235 versus required 0.60
median relation after source-off: 0.9209 versus required 0.65
median relation after removal:    0.5338 versus required 0.55
median final escape fraction:     0.0000 versus maximum 0.10
```

The failure is therefore not absence of all restoring behavior. It is a mismatch between the preregistered definition of sufficient recovery and the response produced by the local spring-network fixture within the declared horizon. The observer-fixture pair had no seed satisfying every condition.

## 13. Failure-to-mechanism analysis

### 13.1 Exact bounded negative result

```text
the frozen observer-fixture pair is unsupported under the declared deformation,
readout horizon, local spring law, member-removal rule, and thresholds.
```

This result does not establish any of the following:

```text
collective identity is impossible;
relational particles are impossible;
Lineum lacks collective cohesion;
pneuma is or is not physical;
the P2 remnant is gas;
the original thresholds should be lowered.
```

### 13.2 Positive behavior that remains unexplained

The elastic class showed all of the following simultaneously:

- reproducible partial geometric restoration around `52-56%`;
- high relational preservation before member removal;
- no final escape;
- excellent timestep convergence;
- separation from all four false-positive controls.

The open question is whether this is an insufficient object, a legitimate adaptive object judged by an over-rigid observer, or an under-specified synthetic elasticity model.

### 13.3 Distinct repair classes registered but not selected

No repair is executed in this checkpoint.

```text
R-A mechanism-completeness repair:
    local distance springs may leave shear, bending, area, or global shape modes too weakly
    constrained; add one declared constitutive ingredient and ablate it independently.

R-B observer-timescale repair:
    endpoint recovery may misclassify a slow but stable relaxation; fit a frozen relaxation
    curve, asymptote, and time constant instead of requiring a selected deadline.

R-C identity-after-loss repair:
    exact original geometry and label-neighbor relations may be the wrong invariant after
    member deletion; test recovery of boundedness, graph spectrum, role distribution, and
    constitutive response while permitting a new equilibrium shape.

R-D intervention-domain repair:
    the declared deformation and twenty-percent removal may cross the fixture's linear or
    connected regime; preregister a deformation-by-removal factorial rather than tuning one
    successful amplitude post hoc.

R-E implementation-validity repair:
    independently derive and implement a known elastic network with an analytic small-
    deformation response before judging the observer.
```

### 13.4 Cheapest next discriminator, pending owner failure-gate input

The smallest candidate comparison is a frozen two-by-two toy matrix:

```text
mechanism:
    original local-distance network
    versus one independently justified bending/area-stabilized network;

observer:
    original endpoint rule
    versus a preregistered relaxation-asymptote rule;

controls:
    preserve the same gas, rigid, driven, and scrambled classes unchanged.
```

This matrix would distinguish an underpowered synthetic mechanism from an over-rigid endpoint observer. It is not authorized until the project-owner failure-gate response is recorded.

## 14. Root-programme impact after execution

| Root branch | Relation | Resulting effect |
|---|---|---|
| P2 multi-defect remnant | `unaffected` | Application to P2 remains blocked because the prerequisite fixture failed. |
| Collective-object preregistration | `constrains` | Exact-shape endpoint recovery is not yet a validated collective-identity observer. |
| Minimum-flux observer limitation | `supports` | Transport and recurring shape were correctly rejected as insufficient. |
| Common-source synchronization concern | `supports` | The driven template recovered only while externally controlled. |
| Member-turnover identity | `reopens` | The failure exposes a choice between original-shape identity and adaptive relational identity. |
| Current source accounting | `unaffected` | No Core source or reservoir claim changed. |
| Copying and heredity | `unaffected` | No reproduction or content transfer was tested. |
| Mu reduction-first programme | `unaffected` | No state-variable conclusion follows. |
| Physical particle correspondence | `unaffected` | No Lineum or real-particle evidence was produced. |

## 15. Complete executable verification code

```python
import json
import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, squareform

N = 32
DT = 0.01
STEPS = 1000
DRIFT = np.array([0.15, 0.05])
DEFORMATION = np.array([[1.45, 0.15], [0.00, 0.65]])
REMOVE_COUNT = round(0.20 * N)
K_S = 18.0
GAMMA = 2.5
K_P = 18.0
GAMMA_P = 4.0
NOISE_SD = 0.002
CLASSES = ["elastic", "gas", "rigid", "driven", "scrambled"]

theta = 2.0 * np.pi * np.arange(N) / N
REFERENCE = np.column_stack((np.cos(theta), 0.70 * np.sin(theta)))


def knn_edges(points, k=4, labels=None):
    points = np.asarray(points)
    distances = squareform(pdist(points))
    np.fill_diagonal(distances, np.inf)
    edges = set()
    for i in range(len(points)):
        count = min(k, len(points) - 1)
        neighbors = np.argpartition(distances[i], count - 1)[:count]
        for j in neighbors:
            a = int(labels[i]) if labels is not None else i
            b = int(labels[j]) if labels is not None else j
            edges.add(tuple(sorted((a, b))))
    return edges


def reference_graph(active):
    active = np.asarray(active, dtype=int)
    return knn_edges(REFERENCE[active], 4, active)


def shape_error(points, active):
    current = np.sort(pdist(points))
    target = np.sort(pdist(REFERENCE[np.asarray(active)]))
    return float(np.linalg.norm(current - target) /
                 max(np.linalg.norm(target), 1e-12))


def secondary_error(points, active):
    centered = points - points.mean(axis=0)
    target = REFERENCE[np.asarray(active)]
    target = target - target.mean(axis=0)
    eig = np.sort(np.linalg.eigvalsh(np.cov(centered.T, bias=True)))[::-1]
    eig_target = np.sort(
        np.linalg.eigvalsh(np.cov(target.T, bias=True))
    )[::-1]
    eig_error = np.linalg.norm(eig - eig_target) / max(eig_target.sum(), 1e-12)
    radii = np.sort(np.linalg.norm(centered, axis=1))
    target_radii = np.sort(np.linalg.norm(target, axis=1))
    radial_error = np.linalg.norm(radii - target_radii) / max(
        np.linalg.norm(target_radii), 1e-12
    )
    return float(0.5 * (eig_error + radial_error))


def relation_jaccard(points, active):
    current = knn_edges(points, 4, np.asarray(active))
    target = reference_graph(active)
    return len(current & target) / max(len(current | target), 1)


def escape_fraction(points, active):
    centered = points - points.mean(axis=0)
    target = REFERENCE[np.asarray(active)]
    target = target - target.mean(axis=0)
    target_rms = np.sqrt(np.mean(np.sum(target ** 2, axis=1)))
    return float(np.mean(np.linalg.norm(centered, axis=1) > 2.5 * target_rms))


def apply_deformation(points):
    center = points.mean(axis=0)
    return (points - center) @ DEFORMATION.T + center


def spring_force(points, velocity, active):
    active = np.asarray(active)
    index = {label: i for i, label in enumerate(active)}
    force = np.zeros_like(points)
    for a, b in reference_graph(active):
        i, j = index[a], index[b]
        displacement = points[i] - points[j]
        distance = np.linalg.norm(displacement)
        if distance < 1e-12:
            continue
        rest_length = np.linalg.norm(REFERENCE[a] - REFERENCE[b])
        edge_force = -K_S * (distance - rest_length) * displacement / distance
        force[i] += edge_force
        force[j] -= edge_force
    force -= GAMMA * (velocity - velocity.mean(axis=0))
    return force


def pin_force(points, velocity, active, step, dt):
    target = REFERENCE[np.asarray(active)] + DRIFT * (step * dt)
    return -K_P * (points - target) - GAMMA_P * (velocity - DRIFT)


def recovery(before, after):
    return (before - after) / max(before, 1e-12)


def simulate(system_class, seed, dt=DT):
    total_steps = round((STEPS * DT) / dt)
    rng = np.random.default_rng(seed)
    active = list(range(N))
    points = REFERENCE.copy() + rng.normal(0.0, 0.01, (N, 2))
    velocity = np.tile(DRIFT, (N, 1)) + rng.normal(0.0, 0.005, (N, 2))

    event_1 = round(1.0 / dt)
    read_1 = round(3.0 / dt)
    controller_off = round(4.0 / dt)
    event_2 = round(5.0 / dt)
    read_2 = round(7.0 / dt)
    removal = round(7.5 / dt)
    read_3 = round(9.5 / dt)
    events = {}

    def scrambled_template(step):
        permutation = rng.permutation(len(active))
        base = REFERENCE[np.asarray(active)][permutation] + DRIFT * (step * dt)
        return base + rng.normal(0.0, 0.01, base.shape)

    for step in range(total_steps + 1):
        if step == event_1:
            points = apply_deformation(points)
            events["e1_after"] = (
                shape_error(points, active),
                secondary_error(points, active),
            )
        if step == read_1:
            events["e1_read"] = (
                shape_error(points, active),
                secondary_error(points, active),
                relation_jaccard(points, active),
                escape_fraction(points, active),
            )
        if step == event_2:
            points = apply_deformation(points)
            events["e2_after"] = (
                shape_error(points, active),
                secondary_error(points, active),
            )
        if step == read_2:
            events["e2_read"] = (
                shape_error(points, active),
                secondary_error(points, active),
                relation_jaccard(points, active),
                escape_fraction(points, active),
            )
        if step == removal:
            removal_rng = np.random.default_rng(10_000 + seed)
            removed = set(
                removal_rng.choice(active, REMOVE_COUNT, replace=False).tolist()
            )
            keep = [i for i, label in enumerate(active) if label not in removed]
            active = [label for label in active if label not in removed]
            points = points[keep]
            velocity = velocity[keep]
            points = apply_deformation(points)
            events["e3_after"] = (
                shape_error(points, active),
                secondary_error(points, active),
            )
        if step == read_3:
            events["e3_read"] = (
                shape_error(points, active),
                secondary_error(points, active),
                relation_jaccard(points, active),
                escape_fraction(points, active),
            )
            break

        if system_class == "elastic":
            force = spring_force(points, velocity, active)
            force += rng.normal(0.0, NOISE_SD, points.shape)
            velocity += dt * force
            points += dt * velocity
        elif system_class == "gas":
            velocity += dt * rng.normal(0.0, NOISE_SD, points.shape)
            points += dt * velocity
        elif system_class == "rigid":
            velocity[:] = DRIFT
            points += dt * DRIFT
        elif system_class == "driven":
            if step < controller_off:
                force = pin_force(points, velocity, active, step, dt)
                force += rng.normal(0.0, NOISE_SD, points.shape)
                velocity += dt * force
            else:
                velocity += dt * rng.normal(0.0, NOISE_SD, points.shape)
            points += dt * velocity
        elif system_class == "scrambled":
            points = scrambled_template(step + 1)
            velocity[:] = DRIFT
        else:
            raise ValueError(system_class)

    r1 = recovery(events["e1_after"][0], events["e1_read"][0])
    r2 = recovery(events["e2_after"][0], events["e2_read"][0])
    r3 = recovery(events["e3_after"][0], events["e3_read"][0])
    s1 = recovery(events["e1_after"][1], events["e1_read"][1])
    s2 = recovery(events["e2_after"][1], events["e2_read"][1])
    s3 = recovery(events["e3_after"][1], events["e3_read"][1])
    secondary_agrees = (
        ((r2 >= 0) == (s2 >= 0)) and ((r3 >= 0) == (s3 >= 0))
    )
    j2 = events["e2_read"][2]
    j3 = events["e3_read"][2]
    f3 = events["e3_read"][3]
    passed = (
        r2 >= 0.75
        and r3 >= 0.60
        and j2 >= 0.65
        and j3 >= 0.55
        and f3 <= 0.10
        and secondary_agrees
    )
    return {
        "class": system_class,
        "seed": seed,
        "dt": dt,
        "R1": r1,
        "R2": r2,
        "R3": r3,
        "S1": s1,
        "S2": s2,
        "S3": s3,
        "J2": j2,
        "J3": j3,
        "F3": f3,
        "secondary_agrees": secondary_agrees,
        "passed": passed,
    }


results = [
    simulate(system_class, seed)
    for system_class in CLASSES
    for seed in range(24)
]
frame = pd.DataFrame(results)

summary = {}
for system_class, group in frame.groupby("class"):
    summary[system_class] = {
        "pass_count": int(group["passed"].sum()),
        "R1_median": float(group["R1"].median()),
        "R2_median": float(group["R2"].median()),
        "R3_median": float(group["R3"].median()),
        "J2_median": float(group["J2"].median()),
        "J3_median": float(group["J3"].median()),
        "F3_median": float(group["F3"].median()),
        "R2_range": [float(group["R2"].min()), float(group["R2"].max())],
        "R3_range": [float(group["R3"].min()), float(group["R3"].max())],
        "J2_range": [float(group["J2"].min()), float(group["J2"].max())],
        "J3_range": [float(group["J3"].min()), float(group["J3"].max())],
    }

exact = REFERENCE.copy()
angle = 0.731
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)],
])
permutation = np.random.default_rng(123).permutation(N)
invariance = {
    "base": shape_error(exact, list(range(N))),
    "translation": shape_error(exact + np.array([3.2, -1.7]), list(range(N))),
    "rotation": shape_error(exact @ rotation.T, list(range(N))),
    "reflection": shape_error(exact * np.array([-1.0, 1.0]), list(range(N))),
    "permutation": shape_error(exact[permutation], list(range(N))),
}
invariance["max_abs"] = max(abs(value) for value in invariance.values())

convergence_rows = []
for system_class in ["elastic", "driven"]:
    for seed in range(8):
        coarse = simulate(system_class, seed, 0.01)
        fine = simulate(system_class, seed, 0.005)
        convergence_rows.append({
            "class": system_class,
            "seed": seed,
            "dR1": abs(coarse["R1"] - fine["R1"]),
            "dR2": abs(coarse["R2"] - fine["R2"]),
            "dR3": abs(coarse["R3"] - fine["R3"]),
            "dJ2": abs(coarse["J2"] - fine["J2"]),
            "dJ3": abs(coarse["J3"] - fine["J3"]),
        })
convergence = pd.DataFrame(convergence_rows)
convergence_summary = {}
for system_class, group in convergence.groupby("class"):
    convergence_summary[system_class] = {
        column: float(group[column].median())
        for column in ["dR1", "dR2", "dR3", "dJ2", "dJ3"]
    }

all_sign_checks = []
for row in results:
    for index in [1, 2, 3]:
        all_sign_checks.append(
            (row[f"R{index}"] >= 0) == (row[f"S{index}"] >= 0)
        )

output = {
    "summary": summary,
    "invariance": invariance,
    "timestep_convergence_median_absolute_differences": convergence_summary,
    "secondary_sign_agreement": {
        "agree": int(sum(all_sign_checks)),
        "total": len(all_sign_checks),
        "fraction": float(np.mean(all_sign_checks)),
    },
}
print(json.dumps(output, indent=2, sort_keys=True))
```

## 16. Current verdict and hard stop

```text
observer_false_positive_rejection = supported_in_synthetic_fixture
observer_known_positive_recovery = failed
observer_fixture = unsupported_under_tested_conditions
threshold_retuning = prohibited_in_this_lane
application_to_P2 = blocked
Lineum_equation_change = not_authorized
physical_correspondence = none
next_action = owner_failure_gate_before_selecting_repair_class
```
