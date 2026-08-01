# Distributed Cohesion Known-Answer Fixture

**Status:** active preregistration; no Lineum or physical validation claimed  
**Version:** 0.1.0  
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
**Current confidence:** high that the fixture classes are causally distinct by construction; medium that the frozen observer will separate all five without post-hoc threshold changes; zero evidence yet that a Lineum state has this property or that the historical concept of `pneuma` names a physical field.

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

## 10. Execution plan and permanent capture

The fixture will be executed in ChatGPT Python without importing repository code. The retained report update must contain:

- complete executable Python;
- machine-readable per-class pass counts and metric summaries;
- invariance and timestep results;
- every failure and anomaly;
- the exact interpretation allowed by Section 8;
- the next gate or owner failure-gate question.

No Lineum equation, production module, public API, or whitepaper will be modified in this lane.
