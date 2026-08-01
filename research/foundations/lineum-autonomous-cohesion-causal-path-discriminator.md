# Autonomous Cohesion Causal-Path Discriminator

**Status:** active preregistration; prior causal-path negative result preserved; angular-momentum and symmetry audit frozen before execution  
**Version:** 0.3.0  
**Evidence cutoff:** 2026-08-01  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`  
**Recovered root version:** 0.4.14  
**Root evidence cutoff:** 2026-07-29  
**Root blob SHA:** `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, version 0.3.0, blob `5304874451caf32313ad0e8e3c59e53958698d79`  
**Conceptual lineage:** `lineum-gnostic-enochic-dead-sea-scrolls-metaphor-audit.md` v0.2.0 -> `lineum-pneuma-cohesion-observer-fixture.md` v0.2.0 -> `lineum-pneuma-cohesion-observer-adversarial-audit.md` v0.1.0 -> this report  
**Immediate predecessor blob SHA:** `c3371db997abdd172485bcdadb65ef43467d71a6`  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Scope:** A synthetic known-answer causal intervention testing whether restoration depends on an intact local reciprocal interaction path and whether an external organizer acts during the challenge. No Lineum module is imported.  
**Central question:** Can a graph cut plus an organizer ledger distinguish internally mediated restoration from global reference control and from preparation history alone?  
**Current confidence:** high in the numerical and analytic results for this synthetic system; high that the graph cut has causal power; high that the frozen absolute-orientation recovery gate is invalid for autonomy; zero evidence for P2, particles, pneuma as a field, souls, life, or nature.

## 1. Answer first

The causal cut worked, but the frozen autonomy verdict did not.

The local reciprocal network repaired the damaged geometry only when its cross-links remained intact. Removing those links reduced whole-object repair to zero. A global reference controller repaired the object whether the graph was intact or cut, but its external action ledger was large. Removing either organizer before the challenge produced no repair.

However, the local intact network restored the shape while the whole object settled approximately `6.31 degrees` rotated relative to its matched twin. The preregistered `R_cross` observer compared an absolute oriented vector and therefore counted only about `61.8%` recovery. The permutation-invariant pair geometry counted about `97.3%` recovery, and a post-hoc proper-rotation diagnostic counted more than `99.90%` cross-group recovery.

The frozen protocol therefore fails exactly as preregistered:

```text
local causal path dependence = supported in the synthetic domain
external-controller distinction = supported by action ledger and cut invariance
preparation history alone = insufficient
absolute-orientation autonomy gate = failed
rotation-invariant autonomy verdict = not preregistered and therefore not accepted
P2 application = prohibited
```

## 2. Version history and frozen execution receipt

Version `0.1.0` was committed before confirmatory execution:

```text
preregistration commit = 671d1d8747783fc3533811adbb04fd8dab5dd896
confirmatory seeds = 500..511
integration steps = 0.01, 0.005, 0.0025
formation horizon = 4.0
challenge horizon = 6.0
force constants and thresholds = frozen
```

Version `0.2.0` records the first execution without changing any seed, timestep, force, graph, partition, challenge, horizon, threshold, or declared gate. The rotation-aligned diagnostic was calculated only after the frozen gate failed and is explicitly non-confirmatory.

Version `0.3.0` freezes the angular-momentum, timestep, rotation-equivariance, and reflection-equivariance audit in Section 17 before execution. It does not alter or reinterpret the failed version-0.1.0 protocol.

## 3. Owner failure-gate response and formalization

The project owner rejected the premise that repair instructions should be supplied from outside:

> No external instructions should be given.

This is an architectural constraint, not evidence. It was formalized before execution as:

```text
autonomous_cohesion_candidate = restoration after a relational injury
                                with no external reference controller active,
                                through declared internal interactions,
                                and with counterfactual dependence on an intact causal path.
```

The global controller remains an adversarial null, not a proposed Lineum mechanism.

## 4. Inherited evidence

The lane inherits these programme facts:

- the first cohesion fixture classified a continuous external reference controller as cohesive in `36/36` adversarial runs;
- the minimum-flux Lineum observer is non-identifying because matched smooth disorder can pass;
- current Core source accounting includes a coherent software pump without a demonstrated physical stock or closed energy ledger;
- the tested `mu x kappa` repair matrix showed no synergy, with a negligible and slightly negative `mu` effect;
- active Core has no term that detects missing structure or compares the current state with a target;
- tested passive boundary candidates did not close receiving-store and return-path gates;
- exact state transplant supports software continuation, not autonomous identity or heredity.

This report repairs an observer protocol only. It adds no field, scaffold, target-copying controller, equation, public API, or whitepaper claim.

## 5. Cross-disciplinary structure

Distributed formation-control literature distinguishes local relative constraints from global or leader reference control. The shared mathematical object is an information graph whose edges specify which relationships can carry corrective information.

Portable references:

- Olfati-Saber, Reza. `Flocking for Multi-Agent Dynamic Systems: Algorithms and Theory`. *IEEE Transactions on Automatic Control* 51(3), 2006, 401-420. DOI `10.1109/TAC.2005.864190`.
- Aranda, Miguel, et al. `Distributed Formation Stabilization Using Relative Position Measurements in Local Coordinates`. *IEEE Transactions on Automatic Control*, 2016.
- Suttner, Raik, and Zhiyong Sun. `Formation Shape Control Based on Distance Measurements Using Lie Bracket Approximations`. *SIAM Journal on Control and Optimization* 58, 2020. DOI `10.1137/18M117131X`.
- Belabbas, M.-A. `Decentralized Formation Control Part I: Geometric Aspects`, 2011, arXiv `1101.2416`.

These references justify a known-answer graph intervention. They do not establish that Lineum or physical particles use this architecture.

## 6. Frozen synthetic system

Sixteen unit-mass points use the irregular reference ring

```text
theta_i = 2 pi i / 16
r_i = 1 + 0.12 cos(3 theta_i) + 0.05 sin(5 theta_i)
R_i = [r_i cos(theta_i), r_i sin(theta_i)]
```

The full undirected graph contains cyclic offsets `1`, `2`, and `5`:

```text
full edges = 48
cross-partition edges = 16
edges after cut = 32
left group = nodes 0..7
right group = nodes 8..15
```

Initial formation states are

```text
X_i = A R_i + eta_i
A = [[1.20, 0.08],
     [0.03, 0.82]]
eta_i ~ Normal(0, 0.05^2 I)
v_bulk = [0.30, -0.15]
```

Local edge forces are equal and opposite:

```text
F_ij = 4 (|X_j-X_i| - l_ij) (X_j-X_i) / |X_j-X_i|
F_i += F_ij
F_j -= F_ij
F_damp,i = -2 (v_i - mean(v))
```

The global adversarial controller is

```text
F_ext = -4 ((X - mean(X)) - R) - 2 (v - mean(v))
```

After formation, velocities are normalized to `v_bulk`. The challenged state receives opposite half translations:

```text
delta = [0.35, 0.12]
left half  <- left half  - delta / 2
right half <- right half + delta / 2
```

This preserves every within-half distance and the total center of mass. Every challenged lane has a matched no-shift twin.

## 7. Frozen cases and gates

```text
L_INTact:      local reciprocal forces, full graph
L_CUT:         local reciprocal forces, all cross edges removed
L_REMOVED:     local formation, no force during challenge
G_CONTINUOUS:  global controller remains active
G_CUT:         global controller remains active; graph cut is irrelevant to its law
G_REMOVED:     global formation, controller removed before challenge
```

The preregistered primary metric was

```text
d(t) = centroid_right(t) - centroid_left(t)
e_cross(t) = |d_challenged(t) - d_twin(t)| / |delta|
R_cross = 1 - e_cross(T) / e_cross(0)
```

The second geometry metric used sorted all-pair distances between challenged and twin states. Additional ledgers recorded external action, external work, internal reciprocity, bulk velocity, spring energy, and damping dissipation.

The decisive frozen requirements included:

```text
L_INTact: R_cross > 0.90 and R_pair > 0.80
L_CUT: R_cross < 0.05
L_REMOVED: R_cross < 0.05
G_CONTINUOUS and G_CUT: R_cross > 0.90, R_pair > 0.80, A_ext > 0.01
G_REMOVED: R_cross < 0.05
local cut sensitivity: R_cross(L_INTact) - R_cross(L_CUT) > 0.85
global cut invariance: absolute difference < 0.02
```

No post-hoc metric may convert this frozen version into a pass.

## 8. Execution environment and independent checks

```text
Python = 3.13.5
NumPy = 2.3.5
platform = Linux 6.12.13 x86_64, glibc 2.41
reported trajectories = 432 including matched twins
standalone code SHA-256 = 0e41ef6ec3922989e72e96f2b3b04dfc71c258dc647167cd3c7821744960b399
standalone JSON output SHA-256 = d7f00875408229cec4bea43c1d39225ccabb8cd3dff9c42214de2eddbfff21fe
```

Independent checks:

- explicit edge-loop and incidence-matrix force implementations agreed at the initial challenge to maximum error `1.5543122344752192e-15`;
- final local decision metrics and coordinates for seed `500` agreed between both implementations to maximum error `4.884981308350689e-15` across all three timesteps;
- `G_CONTINUOUS` and `G_CUT` were bit-for-bit identical for every matched seed and timestep;
- removed-force and cut analytic nulls reproduced to roundoff;
- all bulk-velocity errors were below `1.56e-15`;
- the local mechanical ledger residual decreased from at most `3.1215907903825446e-4` at `dt=0.01` to `1.9323379502500515e-5` at `dt=0.0025` for `L_INTact`.

The reciprocity ratio gate failed narrowly in near-zero-force late states: maximum ratio `7.722571531188021e-12` exceeded the frozen `1e-12` threshold. At that instant the absolute net-force numerator was only `3.73471365847992e-15`, divided by a total-force denominator `4.8361010880858507e-4`. The ratio design is therefore ill-conditioned near quiescence, but the frozen gate remains failed.

## 9. Confirmatory results

### 9.1 Mean and range by timestep

| dt | case | mean `R_cross` | range `R_cross` | mean `R_pair` | minimum `R_pair` | external action range |
|---:|---|---:|---:|---:|---:|---:|
| 0.0100 | `L_INTact` | 0.617924 | 0.613491–0.620265 | 0.972595 | 0.969619 | 0 |
| 0.0100 | `L_CUT` | 3.52e-16 | -4.88e-15–4.55e-15 | -0.002061 | -0.004202 | 0 |
| 0.0100 | `L_REMOVED` | -3.87e-14 | -4.37e-14–-3.53e-14 | 7.64e-15 | 9.99e-16 | 0 |
| 0.0100 | `G_CONTINUOUS` | 0.997625 | 0.997625–0.997625 | 0.995691 | 0.995674 | 7.666–7.695 |
| 0.0100 | `G_CUT` | 0.997625 | 0.997625–0.997625 | 0.995691 | 0.995674 | 7.666–7.695 |
| 0.0100 | `G_REMOVED` | -3.71e-14 | -4.09e-14–-3.44e-14 | 1.97e-14 | 1.84e-14 | 0 |
| 0.0050 | `L_INTact` | 0.617907 | 0.613474–0.620252 | 0.972568 | 0.969593 | 0 |
| 0.0050 | `L_CUT` | 6.94e-16 | -5.33e-15–7.22e-15 | -0.002092 | -0.004236 | 0 |
| 0.0050 | `L_REMOVED` | -2.16e-14 | -2.55e-14–-1.87e-14 | -8.38e-15 | -1.09e-14 | 0 |
| 0.0050 | `G_CONTINUOUS` | 0.997521 | 0.997521–0.997521 | 0.995503 | 0.995485 | 7.663–7.692 |
| 0.0050 | `G_CUT` | 0.997521 | 0.997521–0.997521 | 0.995503 | 0.995485 | 7.663–7.692 |
| 0.0050 | `G_REMOVED` | -2.15e-14 | -2.46e-14–-1.78e-14 | -1.75e-14 | -1.98e-14 | 0 |
| 0.0025 | `L_INTact` | 0.617898 | 0.613465–0.620246 | 0.972555 | 0.969580 | 0 |
| 0.0025 | `L_CUT` | 3.24e-16 | -5.77e-15–1.03e-14 | -0.002108 | -0.004253 | 0 |
| 0.0025 | `L_REMOVED` | -1.90e-14 | -2.24e-14–-1.71e-14 | -2.04e-14 | -2.33e-14 | 0 |
| 0.0025 | `G_CONTINUOUS` | 0.997468 | 0.997468–0.997468 | 0.995407 | 0.995389 | 7.662–7.691 |
| 0.0025 | `G_CUT` | 0.997468 | 0.997468–0.997468 | 0.995407 | 0.995389 | 7.662–7.691 |
| 0.0025 | `G_REMOVED` | -1.78e-14 | -1.95e-14–-1.53e-14 | -2.58e-14 | -2.73e-14 | 0 |

### 9.2 Frozen gate results

```json
{
  "L_INTact_R_cross_all_gt_0_90": false,
  "L_INTact_R_pair_all_gt_0_80": true,
  "L_CUT_R_cross_all_lt_0_05": true,
  "L_REMOVED_R_cross_all_lt_0_05": true,
  "G_CONTINUOUS_R_cross_all_gt_0_90": true,
  "G_CUT_R_cross_all_gt_0_90": true,
  "G_REMOVED_R_cross_all_lt_0_05": true,
  "local_cut_sensitivity_all_gt_0_85": false,
  "global_cut_invariance_all_lt_0_02": true,
  "global_cut_bit_identical_all": true,
  "bulk_error_all_lt_1e_10": true,
  "reciprocity_ratio_all_lt_1e_12": false,
  "force_implementations_all_lt_1e_12": true
}
```

The local cut-sensitivity score ranged only `0.613465–0.620265`, below the frozen `0.85` requirement because the same orientation-sensitive `R_cross` metric was used in both terms.

## 10. Post-hoc rotation diagnostic

The disagreement between `R_cross` and `R_pair` prompted a diagnostic that was not part of the frozen gate.

After aligning the final challenged local state to its twin by translation and the best proper rotation:

```text
dt = 0.0100:
    mean rotation = 6.31137 degrees
    rotation range = 6.27899–6.38260 degrees
    minimum aligned R_cross = 0.999083

dt = 0.0050:
    mean rotation = 6.31175 degrees
    rotation range = 6.27933–6.38300 degrees
    minimum aligned R_cross = 0.999088

dt = 0.0025:
    mean rotation = 6.31195 degrees
    rotation range = 6.27951–6.38320 degrees
    minimum aligned R_cross = 0.999090
```

The mean normalized labeled-coordinate mismatch after alignment was approximately `0.00294`.

This diagnostic strongly suggests that the local positive control restored its relational geometry up to a legitimate rigid transformation. It does not retroactively pass the preregistered protocol. A new version would have to freeze an observer on the quotient space of translations and rotations before execution.

## 11. Interpretation

### What the toy implementation computes

- local lanes use stored edge rest lengths and reciprocal pair forces;
- global lanes use coordinate-wise access to a centered absolute reference;
- cut lanes remove all declared information and force paths between two equal halves;
- removed lanes contain preparation history but no challenge force.

### What was reproducibly observed

- the cut destroyed local whole-object correction while preserving each half's internal relationships;
- the global controller was completely insensitive to the graph cut and used substantial external action;
- preparation history alone produced no correction;
- the local intact network restored pair geometry but acquired a reproducible rigid rotation;
- results were stable across three timesteps and two force implementations.

### Cautious interpretation

The causal-path intervention is useful. It distinguishes a correction that depends on internal links from a global oracle. The failure lies primarily in the frozen observer's insistence on absolute orientation, not in an absence of local shape restoration.

### Prohibited interpretation

This does not establish a Lineum particle, `pneuma`, autonomous life, memory, heredity, consciousness, quantum mechanics, gravity, cosmology, or correspondence to physical matter.

## 12. Failure-to-mechanism analysis

### Exact failures

```text
frozen local absolute-orientation recovery gate = failed
frozen local cut-sensitivity threshold = failed through the same metric
frozen normalized reciprocity ratio = failed near quiescence
complete autonomy verdict = not accepted
```

### Positive behavior that remains

```text
local pair-geometry restoration = supported
counterfactual dependence on cross-links = supported
external-controller graph-cut invariance = supported
external organizer action ledger = supported
source-removal null = supported
preparation-history-only repair = unsupported
bulk conservation = supported
numerical implementation agreement = supported
```

### Failure location

```text
local force law = positive control remained functional
causal graph intervention = functional
integration = not the primary failure
absolute coordinate-frame observer = primary failure
reciprocity ratio conditioning = secondary observer failure
interpretation = frozen protocol correctly remains negative
```

### Reopenable repair classes

```text
R1 quotient-space observer:
    compare states modulo translation and proper rotation before applying cross-group metrics;

R2 purely relational observer:
    use labeled edge lengths, graph stress, rigidity-matrix modes, and topology without
    absolute orientation;

R3 orientation-as-state variant:
    retain orientation as a real identity variable only if another mechanism physically
    anchors it and a separate intervention demonstrates that requirement;

R4 causal-response observer:
    score changes in recovery after graph cuts, edge freezes, and pathway scrambles without
    requiring return to one absolute pose;

R5 reciprocity conditioning repair:
    report absolute closure residual and a normalized ratio only above a frozen force floor;

R6 functional rather than geometric recovery:
    test restored transport, boundedness, source ledger, or task response while allowing
    multiple equivalent shapes.
```

No repair is selected here. This verified negative result reopens the owner failure gate before the next consequential observer is frozen.

## 13. Root-programme impact matrix

| Root branch | Relation | Result |
|---|---|---|
| Collective-particle preregistration | `supports` and `constrains` | Causal-path ablation is useful, but identity metrics must respect physical symmetries. |
| P2 vortex-gas remnant | `unaffected` | Application remains prohibited. |
| Minimum-flux observer limitation | `supports` | A second observer failed by encoding a non-identifying coordinate choice. |
| Source-accounting programme | `supports` | Continuous global correction was exposed by external action `A_ext ≈ 7.66–7.69`. |
| Active `mu x kappa` repair matrix | `unaffected` | No new repair role is assigned to current fields. |
| Passive boundary programme | `supports` | A cut can be a causal intervention without being a physical membrane claim. |
| Mu/history reconstruction | `supports` | Matched twins remove baseline history drift, but history alone did not repair. |
| Copying and heredity | `unaffected` | No turnover, replication, or descent was tested. |
| Ancient-text structural audit | `constrains` | Pneuma-inspired cohesion remains an observer question, not an ontology. |
| Physical particle, soul, life, or cosmology | `unaffected` | No correspondence advanced. |
| Cross-repository variants | `not_yet_compared` | Connector indexing remained incomplete. |

## 14. Three evidence layers

```text
current Lineum implementation:
    not executed;
    inherited source, observer, and repair constraints remain unchanged;

established mathematical and empirical domains:
    distributed-control and rigidity research shows that local relative constraints and
    global reference control are operationally distinct, and that formation states are often
    considered modulo rigid transformations;

Lineum hypothesis:
    a candidate collective object may require source-accounted restoration that depends on
    internal causal paths and is evaluated under the actual symmetries of the state space;
    this remains untested in Lineum.
```

## 15. Current verdict

```text
owner_external_instruction_constraint = preserved
frozen_matrix_execution = completed
analytic_nulls = passed
independent_numerical_check = passed
local_path_dependence = supported_in_toy
external_global_control = distinguished_in_toy
absolute_orientation_observer = falsified_within_domain
reciprocity_ratio_observer = ill_conditioned_and_failed
complete_autonomy_gate = failed
P2_application = prohibited
next_action = owner_failure_gate_before_selecting_symmetry_invariant_repair
```

## 16. Complete executable verification code

```python
import json
import math
import platform
import sys
import numpy as np

N = 16
SEEDS = list(range(500, 512))
DTS = [0.01, 0.005, 0.0025]
T_FORM = 4.0
T_TEST = 6.0
BULK = np.array([0.30, -0.15], dtype=float)
DELTA = np.array([0.35, 0.12], dtype=float)
K = 4.0
GAMMA = 2.0
CASES = ["L_INTact", "L_CUT", "L_REMOVED", "G_CONTINUOUS", "G_CUT", "G_REMOVED"]

theta = np.linspace(0.0, 2.0 * np.pi, N, endpoint=False)
radius = 1.0 + 0.12 * np.cos(3.0 * theta) + 0.05 * np.sin(5.0 * theta)
REFERENCE = np.column_stack((radius * np.cos(theta), radius * np.sin(theta)))
REFERENCE -= REFERENCE.mean(axis=0)

edge_set = set()
for i in range(N):
    for offset in (1, 2, 5):
        edge_set.add(tuple(sorted((i, (i + offset) % N))))
FULL_EDGES = sorted(edge_set)
CROSS_EDGES = [edge for edge in FULL_EDGES if (edge[0] < 8) != (edge[1] < 8)]
CUT_EDGES = [edge for edge in FULL_EDGES if edge not in CROSS_EDGES]
PAIR_I, PAIR_J = np.triu_indices(N, 1)


def make_graph(edges):
    incidence = np.zeros((len(edges), N), dtype=float)
    for row, (i, j) in enumerate(edges):
        incidence[row, i] = -1.0
        incidence[row, j] = 1.0
    return incidence, np.linalg.norm(incidence @ REFERENCE, axis=1)


FULL_B, FULL_REST = make_graph(FULL_EDGES)
CUT_B, CUT_REST = make_graph(CUT_EDGES)


def local_force_vectorized(x, v, incidence, rest):
    edge_vectors = incidence @ x
    distances = np.linalg.norm(edge_vectors, axis=1)
    units = np.divide(edge_vectors, distances[:, None], out=np.zeros_like(edge_vectors), where=distances[:, None] > 1e-15)
    edge_forces = K * (distances - rest)[:, None] * units
    force = -(incidence.T @ edge_forces)
    force += -GAMMA * (v - v.mean(axis=0))
    return force


def local_force_loop(x, v, edges, rest):
    force = np.zeros_like(x)
    for (i, j), rest_length in zip(edges, rest):
        delta = x[j] - x[i]
        distance = float(np.sqrt(delta @ delta))
        if distance > 1e-15:
            pair_force = K * (distance - rest_length) * delta / distance
            force[i] += pair_force
            force[j] -= pair_force
    force += -GAMMA * (v - v.mean(axis=0))
    return force


def global_force(x, v):
    return -K * ((x - x.mean(axis=0)) - REFERENCE) - GAMMA * (v - v.mean(axis=0))


def pair_signature(x):
    return np.sort(np.linalg.norm(x[PAIR_J] - x[PAIR_I], axis=1))


def cross_vector(x):
    return x[8:].mean(axis=0) - x[:8].mean(axis=0)


def relative_kinetic(v):
    centered = v - v.mean(axis=0)
    return 0.5 * np.sum(centered * centered)


def spring_energy(x, incidence, rest):
    distances = np.linalg.norm(incidence @ x, axis=1)
    return 0.5 * K * np.sum((distances - rest) ** 2)


def damping_rate(v):
    centered = v - v.mean(axis=0)
    return GAMMA * np.sum(centered * centered)


def initial_state(seed):
    rng = np.random.default_rng(seed)
    transform = np.array([[1.20, 0.08], [0.03, 0.82]], dtype=float)
    x = REFERENCE @ transform.T + rng.normal(0.0, 0.05, size=REFERENCE.shape)
    x -= x.mean(axis=0)
    return x, np.tile(BULK, (N, 1))


def form_state(seed, dt, mode):
    x, v = initial_state(seed)
    for _ in range(int(round(T_FORM / dt))):
        force = local_force_vectorized(x, v, FULL_B, FULL_REST) if mode == "local" else global_force(x, v)
        v += dt * force
        x += dt * v
    return x


def case_spec(case):
    if case == "L_INTact":
        return "local", "local", FULL_B, FULL_REST, FULL_EDGES
    if case == "L_CUT":
        return "local", "local", CUT_B, CUT_REST, CUT_EDGES
    if case == "L_REMOVED":
        return "local", "zero", None, None, None
    if case in ("G_CONTINUOUS", "G_CUT"):
        return "global", "global", None, None, None
    if case == "G_REMOVED":
        return "global", "zero", None, None, None
    raise ValueError(case)


FORMATION = {}
for dt in DTS:
    for seed in SEEDS:
        FORMATION[(dt, seed, "local")] = form_state(seed, dt, "local")
        FORMATION[(dt, seed, "global")] = form_state(seed, dt, "global")


def run_case(case, seed, dt):
    formation_mode, challenge_mode, incidence, rest, edges = case_spec(case)
    pre = FORMATION[(dt, seed, formation_mode)].copy()
    twin_x = pre.copy()
    challenged_x = pre.copy()
    twin_v = np.tile(BULK, (N, 1))
    challenged_v = np.tile(BULK, (N, 1))
    challenged_x[:8] -= DELTA / 2.0
    challenged_x[8:] += DELTA / 2.0

    cross_0 = np.linalg.norm(cross_vector(challenged_x) - cross_vector(twin_x)) / np.linalg.norm(DELTA)
    twin_pair_0 = pair_signature(twin_x)
    pair_0 = np.sqrt(np.mean((pair_signature(challenged_x) - twin_pair_0) ** 2)) / np.mean(twin_pair_0)

    force_impl_error = 0.0
    if challenge_mode == "local":
        force_impl_error = float(np.max(np.abs(local_force_vectorized(challenged_x, challenged_v, incidence, rest) - local_force_loop(challenged_x, challenged_v, edges, rest))))
        energy_0 = relative_kinetic(challenged_v) + spring_energy(challenged_x, incidence, rest)
    else:
        energy_0 = None

    external_action = 0.0
    external_work = 0.0
    reciprocity_max = 0.0
    dissipation = 0.0

    for _ in range(int(round(T_TEST / dt))):
        if challenge_mode == "local":
            challenged_force = local_force_vectorized(challenged_x, challenged_v, incidence, rest)
            twin_force = local_force_vectorized(twin_x, twin_v, incidence, rest)
            denominator = np.sum(np.linalg.norm(challenged_force, axis=1)) + 1e-15
            reciprocity_max = max(reciprocity_max, float(np.linalg.norm(challenged_force.sum(axis=0)) / denominator))
            dissipation += dt * damping_rate(challenged_v)
            external_force = np.zeros_like(challenged_force)
        elif challenge_mode == "global":
            challenged_force = global_force(challenged_x, challenged_v)
            twin_force = global_force(twin_x, twin_v)
            external_force = challenged_force
        else:
            challenged_force = np.zeros_like(challenged_x)
            twin_force = np.zeros_like(twin_x)
            external_force = challenged_force

        external_action += dt * np.sum(np.linalg.norm(external_force, axis=1))
        external_work += dt * np.sum(external_force * challenged_v)
        challenged_v += dt * challenged_force
        challenged_x += dt * challenged_v
        twin_v += dt * twin_force
        twin_x += dt * twin_v

    cross_f = np.linalg.norm(cross_vector(challenged_x) - cross_vector(twin_x)) / np.linalg.norm(DELTA)
    twin_pair_f = pair_signature(twin_x)
    pair_f = np.sqrt(np.mean((pair_signature(challenged_x) - twin_pair_f) ** 2)) / np.mean(twin_pair_f)

    ledger = None
    if challenge_mode == "local":
        energy_f = relative_kinetic(challenged_v) + spring_energy(challenged_x, incidence, rest)
        ledger = float(energy_f - energy_0 + dissipation)

    return {
        "case": case,
        "seed": seed,
        "dt": dt,
        "R_cross": float(1.0 - cross_f / cross_0),
        "R_pair": float(1.0 - pair_f / pair_0),
        "A_ext": float(external_action),
        "W_ext": float(external_work),
        "recip_max": float(reciprocity_max),
        "bulk_error": float(max(np.linalg.norm(challenged_v.mean(axis=0) - BULK), np.linalg.norm(twin_v.mean(axis=0) - BULK))),
        "ledger_residual": ledger,
        "force_impl_error": force_impl_error,
        "challenged_x": challenged_x,
        "twin_x": twin_x,
    }


ROWS = [run_case(case, seed, dt) for dt in DTS for case in CASES for seed in SEEDS]


def summarize(case, dt):
    selected = [row for row in ROWS if row["case"] == case and row["dt"] == dt]
    output = {}
    for key in ("R_cross", "R_pair", "A_ext", "recip_max", "bulk_error", "force_impl_error"):
        values = [row[key] for row in selected]
        output[f"{key}_min"] = float(np.min(values))
        output[f"{key}_max"] = float(np.max(values))
        output[f"{key}_mean"] = float(np.mean(values))
    ledgers = [row["ledger_residual"] for row in selected if row["ledger_residual"] is not None]
    if ledgers:
        output["ledger_abs_max"] = float(np.max(np.abs(ledgers)))
    return output


SUMMARY = {str(dt): {case: summarize(case, dt) for case in CASES} for dt in DTS}


def procrustes_diagnostic(row):
    challenged = row["challenged_x"] - row["challenged_x"].mean(axis=0)
    twin = row["twin_x"] - row["twin_x"].mean(axis=0)
    u, _, vt = np.linalg.svd(challenged.T @ twin)
    rotation = u @ vt
    if np.linalg.det(rotation) < 0.0:
        u[:, -1] *= -1.0
        rotation = u @ vt
    aligned = challenged @ rotation
    angle_deg = math.degrees(math.atan2(rotation[1, 0], rotation[0, 0]))
    aligned_cross_error = np.linalg.norm(cross_vector(aligned) - cross_vector(twin)) / np.linalg.norm(DELTA)
    return angle_deg, 1.0 - aligned_cross_error


ROTATION_DIAGNOSTIC = {}
for dt in DTS:
    values = [procrustes_diagnostic(row) for row in ROWS if row["case"] == "L_INTact" and row["dt"] == dt]
    ROTATION_DIAGNOSTIC[str(dt)] = {
        "angle_deg_min": float(np.min([value[0] for value in values])),
        "angle_deg_max": float(np.max([value[0] for value in values])),
        "angle_deg_mean": float(np.mean([value[0] for value in values])),
        "aligned_R_cross_min": float(np.min([value[1] for value in values])),
        "aligned_R_cross_mean": float(np.mean([value[1] for value in values])),
    }


def select(case, seed, dt):
    return next(row for row in ROWS if row["case"] == case and row["seed"] == seed and row["dt"] == dt)


local_cut_sensitivity = []
global_cut_difference = []
global_cut_exact = []
for dt in DTS:
    for seed in SEEDS:
        local_intact = select("L_INTact", seed, dt)
        local_cut = select("L_CUT", seed, dt)
        global_full = select("G_CONTINUOUS", seed, dt)
        global_cut = select("G_CUT", seed, dt)
        local_cut_sensitivity.append(local_intact["R_cross"] - local_cut["R_cross"])
        global_cut_difference.append(abs(global_full["R_cross"] - global_cut["R_cross"]))
        global_cut_exact.append(np.array_equal(global_full["challenged_x"], global_cut["challenged_x"]) and np.array_equal(global_full["twin_x"], global_cut["twin_x"]))


GATES = {
    "L_INTact_R_cross_all_gt_0_90": all(row["R_cross"] > 0.90 for row in ROWS if row["case"] == "L_INTact"),
    "L_INTact_R_pair_all_gt_0_80": all(row["R_pair"] > 0.80 for row in ROWS if row["case"] == "L_INTact"),
    "L_CUT_R_cross_all_lt_0_05": all(row["R_cross"] < 0.05 for row in ROWS if row["case"] == "L_CUT"),
    "L_REMOVED_R_cross_all_lt_0_05": all(row["R_cross"] < 0.05 for row in ROWS if row["case"] == "L_REMOVED"),
    "G_CONTINUOUS_R_cross_all_gt_0_90": all(row["R_cross"] > 0.90 for row in ROWS if row["case"] == "G_CONTINUOUS"),
    "G_CUT_R_cross_all_gt_0_90": all(row["R_cross"] > 0.90 for row in ROWS if row["case"] == "G_CUT"),
    "G_REMOVED_R_cross_all_lt_0_05": all(row["R_cross"] < 0.05 for row in ROWS if row["case"] == "G_REMOVED"),
    "local_cut_sensitivity_all_gt_0_85": all(value > 0.85 for value in local_cut_sensitivity),
    "global_cut_invariance_all_lt_0_02": all(value < 0.02 for value in global_cut_difference),
    "global_cut_bit_identical_all": all(global_cut_exact),
    "bulk_error_all_lt_1e_10": all(row["bulk_error"] < 1e-10 for row in ROWS),
    "reciprocity_ratio_all_lt_1e_12": all(row["recip_max"] < 1e-12 for row in ROWS if row["case"] in ("L_INTact", "L_CUT")),
    "force_implementations_all_lt_1e_12": all(row["force_impl_error"] < 1e-12 for row in ROWS if row["case"] in ("L_INTact", "L_CUT")),
}


RECEIPT = {
    "environment": {"python": sys.version, "numpy": np.__version__, "platform": platform.platform()},
    "trajectory_count": len(ROWS) * 2,
    "edge_count_full": len(FULL_EDGES),
    "edge_count_cross": len(CROSS_EDGES),
    "edge_count_cut": len(CUT_EDGES),
    "summary": SUMMARY,
    "rotation_diagnostic": ROTATION_DIAGNOSTIC,
    "gates": GATES,
    "local_cut_sensitivity_min": float(np.min(local_cut_sensitivity)),
    "local_cut_sensitivity_max": float(np.max(local_cut_sensitivity)),
    "global_cut_difference_max": float(np.max(global_cut_difference)),
}

print(json.dumps(RECEIPT, indent=2, sort_keys=True))
```

The executable code above contains the primary matrix and post-hoc rotation diagnostic. The independent explicit-loop continuation check was executed separately because embedding a second complete duplicate runner would obscure the primary reproduction path; its numerical comparison receipt is stated in Section 8.

## 17. Frozen angular-momentum and symmetry audit preregistration

### 17.1 Motivation and owner checkpoint

The project owner asked whether the approximately `6.31 degree` reorientation is genuinely an error. The prior report could only say that the absolute-orientation observer was non-invariant; it did not yet determine whether the reorientation came from legitimate internal shape dynamics, injected angular momentum, numerical torque, or axis-dependent implementation bias.

This section freezes the smallest audit before execution. It does not change the failed version-0.1.0 gates and cannot retroactively pass them.

### 17.2 Competing explanations

```text
H1 legitimate zero-angular-momentum reorientation:
    the network changes shape during repair and returns to an equivalent geometry with a
    geometric orientation shift, while total relative angular momentum remains zero;

H2 intervention injection:
    the positional challenge or velocity reset injects non-zero relative angular momentum;

H3 numerical torque:
    the integrator or force assembly creates angular momentum that does not converge away;

H4 coordinate-axis bias:
    the reported angle depends on the laboratory axes or implementation orientation;

H5 physical orientation state:
    absolute orientation is meaningful only if an explicit external anisotropy or anchor is
    present; no such anchor exists in the current local toy.
```

Only `H1` can support treating the reorientation as an admissible symmetry-equivalent repair in this toy. `H5` remains a separate untested variant rather than an assumption.

### 17.3 Frozen dynamics and data

The audit reuses the exact `L_INTact` local-force system, graph, rest lengths, formation law, velocity reset, partition, challenge magnitude, seeds `500..511`, formation horizon `4.0`, challenge horizon `6.0`, and semi-implicit Euler convention from Sections 6–9.

The timestep grid is extended by one refinement level:

```text
dt = [0.01, 0.005, 0.0025, 0.00125]
```

No Lineum package is imported.

### 17.4 Angular-momentum observables

All quantities use center-of-mass coordinates:

```text
r_i = x_i - mean(x)
u_i = v_i - mean(v)
L = sum_i (r_ix u_iy - r_iy u_ix)
```

The direct torque is

```text
tau = sum_i (r_ix F_iy - r_iy F_ix)
```

The force law predicts:

```text
central spring torque = 0
damping torque = -gamma L
```

For the semi-implicit update, the discrete residual is

```text
epsilon_L = L_(n+1) - L_n - dt * tau_n
```

The audit records initial, maximum, and final absolute `L`; maximum spring torque; maximum total torque; and maximum absolute `epsilon_L`.

### 17.5 Symmetry controls

Three geometrically equivalent lanes are frozen for every seed and timestep:

```text
BASE:
    the original formed state, bulk velocity, and challenge;

ROTATED:
    rotate the entire formed state, bulk velocity, and challenge by +37 degrees before the
    challenge; use the same distance-based graph and rest lengths;

MIRRORED:
    reflect the entire formed state, bulk velocity, and challenge across the x axis.
```

The rotated lane tests rotational equivariance. The mirrored lane tests handedness: a genuine geometric reorientation must reverse sign under reflection while invariant recovery scores remain unchanged.

A descriptive `REVERSED_DELTA` lane applies `-delta` to the untransformed formed state. Its angle is recorded but no odd-symmetry gate is imposed because the irregular shape and fixed partition do not guarantee that reversing only the challenge is an exact symmetry.

### 17.6 Frozen recovery metrics

For each lane, the final challenged state is aligned to its matched twin by translation and optimal proper rotation.

```text
theta_final = signed proper-rotation angle
R_aligned_cross = 1 - aligned cross-group discrepancy / initial discrepancy
R_pair = permutation-invariant pair-distance recovery
coordinate_mismatch = normalized labeled-coordinate RMS after proper alignment
```

### 17.7 Frozen gates

The audit supports legitimate symmetry-equivalent reorientation only if every gate holds:

```text
G_initial_L:
    absolute L immediately after the challenge < 1e-12;

G_angular_closure:
    maximum absolute L during the challenge < 1e-10;
    maximum absolute spring torque < 1e-11;
    maximum absolute discrete angular residual < 1e-11;

G_geometry:
    R_pair > 0.95 for every BASE run;
    R_aligned_cross > 0.995 for every BASE run;

G_timestep:
    for each seed, absolute difference in theta_final between dt=0.0025 and dt=0.00125
    < 0.01 degree;
    mean angle difference at those timesteps < 0.005 degree;

G_rotation_equivariance:
    absolute BASE-minus-ROTATED angle difference < 1e-8 degree;
    absolute recovery-metric differences < 1e-10;

G_reflection_equivariance:
    absolute (theta_BASE + theta_MIRRORED) < 1e-8 degree;
    absolute recovery-metric differences < 1e-10.
```

The angular-momentum thresholds are intentionally many orders of magnitude below the observed six-degree orientation change. Failure of an equivariance or closure gate blocks the geometric-phase interpretation.

### 17.8 Independent checks

Two force assemblies remain mandatory:

```text
A. incidence-matrix vectorization;
B. explicit equal-and-opposite edge loop.
```

For seed `500` at every timestep, final coordinates, velocities, angular-momentum extrema, and orientation metrics must agree below `1e-10`.

The signed angle is also computed through two independent paths:

```text
A. SVD proper Procrustes rotation;
B. atan2 of the summed two-dimensional cross and dot products after centering.
```

The two angle calculations must agree below `1e-10` degree.

### 17.9 Outcome meanings

```text
all gates pass:
    the reorientation is numerically consistent with a symmetry-equivalent internal
    deformation cycle at effectively zero angular momentum in this synthetic model;

non-zero initial L:
    the intervention or velocity reset injected rotation;

L or angular residual fails to converge:
    numerical torque remains a plausible cause;

rotated control differs:
    axis or implementation bias invalidates the interpretation;

mirrored angle does not reverse:
    handedness or angle extraction is inconsistent;

geometry fails:
    the object did not actually restore even modulo rigid motion.
```

Even a complete pass validates only this known-answer local point network. It does not establish a Lineum object, a particle, physical pneuma, life, identity, or correspondence to nature.

### 17.10 Pre-execution status

```text
owner_question_recorded = yes
angular_audit_preregistered = yes
execution = not_started
prior_failed_gate = preserved
P2_application = prohibited
```
