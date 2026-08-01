# Autonomous Cohesion Causal-Path Discriminator

**Status:** active preregistration; owner failure-gate response formalized; no confirmatory numerical result yet  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-01  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`  
**Recovered root version:** 0.4.14  
**Root evidence cutoff:** 2026-07-29  
**Root blob SHA:** `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, version 0.3.0, blob `5304874451caf32313ad0e8e3c59e53958698d79`  
**Conceptual lineage:** `lineum-gnostic-enochic-dead-sea-scrolls-metaphor-audit.md` v0.2.0 -> `lineum-pneuma-cohesion-observer-fixture.md` v0.2.0 -> `lineum-pneuma-cohesion-observer-adversarial-audit.md` v0.1.0  
**Immediate predecessor blob SHA:** `c3371db997abdd172485bcdadb65ef43467d71a6`  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Scope:** A synthetic known-answer causal intervention that tests whether restoration depends on an intact local reciprocal interaction path and whether any external organizer performs work during the challenge. It does not import Lineum modules and cannot establish a Lineum particle or a physical pneuma.  
**Central question:** Can a counterfactual graph cut plus an explicit organizer ledger distinguish internally mediated restoration from continuous global reference control and from order that survives only as preparation history?  
**Current confidence:** high in the analytic null predictions; medium that the frozen positive local and global controllers will meet the quantitative horizon thresholds without retuning; zero evidence yet for application to P2 or nature.

## 1. Answer first

The next test will no longer ask only whether a deformed shape returns. It will ask whether the repair requires an intact chain of interactions inside the object and whether any external organizer supplies force or information during the repair.

The key intervention is a causal cut. Two halves are displaced rigidly relative to one another. All distances inside each half remain unchanged, so only links crossing between the halves know that the whole has been damaged.

Expected distinction:

```text
local reciprocal collective with intact cross-links:
    should pull the halves back together;

same collective after all cross-links are cut:
    should preserve each half but lose whole-object restoration;

global reference controller:
    should restore the whole even when the declared interaction graph is cut,
    because it does not need that graph;

controller removed before the challenge:
    should not restore merely because it organized the object in the past.
```

A recovery score alone remains insufficient. The autonomy gate additionally requires zero external organizing action during the challenge, reciprocal internal forces, and a large loss of whole-object recovery when the internal causal path is severed.

## 2. Owner failure-gate response

The project owner rejected the premise that repair instructions should be supplied from outside:

> No external instructions should be given.

This is recorded as an architectural constraint, not experimental evidence. The agent formalizes it as:

```text
autonomous_cohesion_candidate = restoration after a local relational injury
                                with no external reference controller active,
                                through declared internal interactions,
                                and with a counterfactual dependence on an intact causal path.
```

The external controller is retained only as an adversarial null. It is not proposed as a Lineum mechanism.

## 3. Inherited evidence and mechanism retrieval

Decision-relevant inherited facts are:

- the first cohesion fixture reproduced shape and pair-distance restoration but classified a continuous external reference controller as cohesive in `36/36` runs;
- the minimum-flux Lineum observer is already known to be non-identifying because matched smooth disorder can pass;
- current Core source accounting contains a coherent software pump without a demonstrated physical stock or closed energy ledger;
- the completed `mu x kappa` repair matrix found no repair synergy: structured static `kappa` weakly redirected activity, while the tested `mu` contribution was negligible and slightly negative;
- the active Core implementation has no term that detects missing structure or compares the state against a target;
- passive reversible membrane candidates tested in current fields did not close their receiving-store and return-path gates;
- exact state transplant reproduces software continuation but does not establish autonomous identity or heredity.

The present repair is therefore an observer-and-intervention repair. It does not add a new Lineum field, controller, scaffold, or target-copying term.

Repository code search was not authoritative in this checkpoint: one multi-repository search returned an upstream error and narrower code searches returned no indexed matches despite known reports. Explicitly known reports and immutable blobs were used instead. Cross-repository families not directly retrieved remain `not_yet_compared`, not absent.

## 4. Cross-disciplinary causal-isomorphism audit

Distributed formation-control research distinguishes controllers using local relative measurements from leader or global-reference control. The relevant shared mathematical structure is a graph whose edges carry the information needed to constrain global shape.

Portable references:

- Olfati-Saber, Reza. `Flocking for Multi-Agent Dynamic Systems: Algorithms and Theory`. *IEEE Transactions on Automatic Control* 51(3), 2006, 401-420. DOI `10.1109/TAC.2005.864190`.
- Aranda, Miguel, et al. `Distributed Formation Stabilization Using Relative Position Measurements in Local Coordinates`. *IEEE Transactions on Automatic Control*, 2016. The method uses relative neighbour positions in independent local frames and no common reference.
- Suttner, Raik, and Zhiyong Sun. `Formation Shape Control Based on Distance Measurements Using Lie Bracket Approximations`. *SIAM Journal on Control and Optimization* 58, 2020. DOI `10.1137/18M117131X`.
- Belabbas, M.-A. `Decentralized Formation Control Part I: Geometric Aspects`, 2011, arXiv `1101.2416`, on information graphs, rigidity, and formation equivalence modulo rigid transformations.

These works do not validate Lineum. They justify the discriminator: if recovery is genuinely mediated by local relations, changing the information graph should change the recovery in a predictable way. A global controller should instead be insensitive to that cut while revealing external action.

Biological self-repair, tissue morphogenesis, animal flocking, and autonomous robotics remain only cross-scale analogy families. No biological or empirical-universe correspondence is tested here.

## 5. Frozen synthetic system

### 5.1 Reference geometry

There are `N = 16` unit-mass points:

```text
theta_i = 2 pi i / 16
r_i = 1 + 0.12 cos(3 theta_i) + 0.05 sin(5 theta_i)
R_i = [r_i cos(theta_i), r_i sin(theta_i)]
```

The internal graph contains undirected edges at cyclic offsets `1`, `2`, and `5`. Duplicate edges are removed. Every edge stores its local rest length `l_ij = |R_j - R_i|`.

The partition is fixed before execution:

```text
left group:  i = 0..7
right group: i = 8..15
cross edge: one endpoint in each group
```

### 5.2 Formation state

For seed `s`, initial positions are:

```text
X_i = A R_i + eta_i
A = [[1.20, 0.08],
     [0.03, 0.82]]
eta_i ~ Normal(0, 0.05^2 I)
```

Initial velocities are the common bulk velocity:

```text
v_bulk = [0.30, -0.15]
```

Formation horizon is `T_form = 4.0`.

### 5.3 Internal reciprocal dynamics

For every active edge `(i,j)`:

```text
d_ij = X_j - X_i
F_ij = k_s (|d_ij| - l_ij) d_ij / |d_ij|
F_i += F_ij
F_j -= F_ij
k_s = 4.0
```

Relative damping preserves center-of-mass velocity:

```text
F_i^damp = -gamma (v_i - mean(v))
gamma = 2.0
```

The graph-cut lane removes every cross edge immediately before the challenge. All within-group edges remain unchanged.

### 5.4 Global reference controller

The adversarial external controller acts on centered coordinates:

```text
X_c = X - mean(X)
V_c = V - mean(V)
F_ext = -k_g (X_c - R) - gamma V_c
k_g = 4.0
gamma = 2.0
```

It preserves net center-of-mass force but has coordinate-wise access to the global target `R`. It is external by construction.

### 5.5 Challenge

At the end of formation, the complete pre-challenge state is recorded. Immediately before the positional challenge, all point velocities are set to the common `v_bulk`; the intervention is applied identically to challenged and matched-twin lanes and is not counted as repair.

The two equal groups are shifted rigidly in opposite directions:

```text
delta = [0.35, 0.12]
left:  X_i <- X_i - delta / 2
right: X_i <- X_i + delta / 2
```

This preserves total center of mass and every within-group pair distance. Only the relationship between the two groups and cross-edge lengths is damaged.

Challenge horizon is `T_test = 6.0`.

Every case has a matched no-shift twin evolved with the same formation history, law, seed, timestep, and velocity normalization.

## 6. Frozen cases

```text
L_INTact:
    local reciprocal graph during formation and challenge;
    all cross edges retained;

L_CUT:
    local reciprocal graph during formation;
    all cross edges removed before challenge;

L_REMOVED:
    local reciprocal graph during formation;
    all internal forces removed before challenge;

G_CONTINUOUS:
    global controller during formation and challenge;

G_CUT:
    global controller during formation and challenge;
    the same graph cut is declared, but the controller does not use the graph;

G_REMOVED:
    global controller during formation;
    controller removed before challenge.
```

`L_REMOVED` and `G_REMOVED` share force-free challenge dynamics but have genuinely different simulated preparation histories. They are retained only to test whether preparation history alone creates repair; they are not counted as independent challenge mechanisms.

## 7. Frozen execution grid

```text
confirmatory seeds = 500..511
integration steps = [0.01, 0.005, 0.0025]
formation horizon = 4.0
challenge horizon = 6.0
integrator = semi-implicit Euler
cases = 6
matched twin per case = yes
expected trajectories = 12 * 3 * 6 * 2 = 432
```

No threshold, force constant, seed, horizon, partition, graph, or challenge vector may be changed after confirmatory execution. A failure may motivate a new version, but must remain recorded as the result of this frozen version.

## 8. Frozen observer and ledgers

### 8.1 Differential cross-group injury

For challenged run `C` and twin `T`:

```text
d(t) = centroid_right(t) - centroid_left(t)
e_cross(t) = |d_C(t) - d_T(t)| / |delta|
R_cross = 1 - e_cross(T_test) / e_cross(0)
```

The challenge should give `e_cross(0) = 1` within numerical tolerance.

### 8.2 Differential permutation-invariant geometry

At each time, all pair distances are sorted. The challenged-to-twin normalized RMS discrepancy is:

```text
e_pair(t) = RMS(sort(D_C(t)) - sort(D_T(t))) / mean(sort(D_T(t)))
R_pair = 1 - e_pair(T_test) / e_pair(0)
```

This remains an ensemble metric, not a complete identity invariant.

### 8.3 External organizer action

For declared external force `F_ext`:

```text
A_ext = integral sum_i |F_ext_i| dt
W_ext = integral sum_i F_ext_i dot v_i dt
```

`A_ext` is the primary non-cancelling action ledger. External autonomy gate:

```text
G_no_external = A_ext < 1e-10 during the challenge
```

### 8.4 Reciprocity

For internal edge forces:

```text
r_recip = max_t |sum_i F_internal_i| / (sum_i |F_internal_i| + 1e-15)
G_recip = r_recip < 1e-12
```

This checks action-reaction closure in the point toy. It is not a universal definition of locality.

### 8.5 Bulk conservation

```text
G_bulk = |mean(v(T_test)) - v_bulk| < 1e-10
```

### 8.6 Local mechanical ledger

For local-force lanes, record relative kinetic energy, spring potential, damping dissipation, and the semi-implicit integration residual:

```text
E_mech = K_relative + U_spring
ledger_residual = E_mech(T) - E_mech(0) + integral dissipation dt
```

The absolute residual must decrease under timestep refinement. It is diagnostic and is not allowed to rescue a failed causal classification.

## 9. Frozen family-level gates

The protocol passes only if all conditions hold for all twelve seeds at every timestep:

```text
L_INTact:
    R_cross > 0.90
    R_pair > 0.80
    G_no_external
    G_recip
    G_bulk

L_CUT:
    R_cross < 0.05
    G_no_external
    G_recip
    G_bulk

L_REMOVED:
    R_cross < 0.05
    G_no_external
    G_bulk

G_CONTINUOUS:
    R_cross > 0.90
    R_pair > 0.80
    A_ext > 0.01
    G_bulk

G_CUT:
    R_cross > 0.90
    R_pair > 0.80
    A_ext > 0.01
    G_bulk

G_REMOVED:
    R_cross < 0.05
    G_no_external
    G_bulk

local cut sensitivity:
    R_cross(L_INTact) - R_cross(L_CUT) > 0.85 for every matched seed and dt

global cut invariance:
    |R_cross(G_CONTINUOUS) - R_cross(G_CUT)| < 0.02
```

Classification must be unchanged across all three timesteps. Mean final metrics at `dt = 0.01` and `dt = 0.0025` must differ by less than `2%` for the two restoring positive controls.

### Autonomy verdict

```text
autonomous_cohesion_fixture = restoration
                              and zero external organizer action
                              and reciprocal internal closure
                              and strong counterfactual dependence on intact local paths
```

Only `L_INTact` is expected to pass. `G_CONTINUOUS` is expected to restore but must fail autonomy because it uses external action and is graph-cut invariant.

## 10. Analytic sanity checks

Before interpreting numerical output:

1. `L_CUT`: the challenge is a rigid translation of each disconnected group. Within-group distances and forces match the twin. With equal normalized velocities and no cross edges, the difference in group-centroid separation must remain exactly `delta`; therefore `R_cross = 0` up to numerical roundoff.
2. `L_REMOVED` and `G_REMOVED`: zero challenge force implies ballistic challenged and twin states with identical velocities; therefore `R_cross = 0` exactly up to roundoff.
3. `G_CONTINUOUS` and `G_CUT`: the controller equation does not read the graph; both trajectories must match bit for bit for a given seed and timestep.
4. Internal edge forces are equal and opposite, so total internal force and center-of-mass acceleration vanish analytically.
5. The positional challenge preserves total center of mass because the groups have equal size and receive opposite shifts.

Violation of any analytic check invalidates the implementation before scientific interpretation.

## 11. Independent numerical check

The retained result requires two implementations of internal edge forces:

```text
implementation A: explicit edge loop with equal-and-opposite accumulation;
implementation B: incidence-matrix/vectorized edge force assembly.
```

One-step forces must agree to maximum absolute error below `1e-12`. Final decision metrics must agree below `1e-10` for at least one seed at each timestep. Timestep refinement is an additional, not substitute, check.

## 12. Outcome interpretation

```text
all gates pass:
    the toy observer distinguishes local reciprocal path-mediated restoration from
    continuous global reference control within the frozen synthetic domain;

local intact restores but cut also restores:
    the graph intervention lacks causal power or an undeclared pathway remains;

local intact fails to restore:
    the chosen local toy is not a valid positive control at the frozen horizon;
    do not retune this version after seeing confirmatory results;

global controller fails to restore:
    the adversarial positive control or numerical setup is invalid;

removed controllers restore:
    hidden state, unmatched twins, velocity normalization, or bookkeeping is wrong;

numerical implementations disagree:
    no scientific verdict is allowed.
```

A successful toy result authorizes only a later observer-transfer design. It does not authorize P2 classification, a new Core API, a Lineum equation change, whitepaper promotion, or physical claims.

## 13. Root-programme impact matrix before execution

| Root branch | Relation | Pre-execution impact |
|---|---|---|
| Collective-particle preregistration | `depends_on` | Supplies a causal autonomy gate stronger than shape persistence. |
| P2 vortex-gas remnant | `unaffected` | Application remains prohibited until the toy passes and a field-compatible intervention exists. |
| Minimum-flux observer limitation | `supports` | Explicitly addresses another non-identifying observer failure. |
| Source-accounting programme | `supports` | External organizer action receives its own ledger. |
| Active `mu x kappa` repair matrix | `constrains` | No target-detection or repair recipe is attributed to current `mu` or static `kappa`. |
| Passive boundary programme | `supports` | The graph cut is a causal intervention, not a claim of a physical membrane. |
| Mu/history reconstruction | `supports` | Observables are relative to matched pre-challenge history rather than a privileged observer target. |
| Copying and heredity | `unaffected` | No member turnover, replication, content transfer, or descent is tested. |
| Physical particle, life, soul, or cosmology mappings | `unaffected` | No correspondence claim is advanced. |
| Cross-repository mechanism families | `not_yet_compared` | Connector search was incomplete; absence is not inferred. |

## 14. Three-layer evidence separation

```text
current Lineum implementation:
    not executed in this lane;
    inherited facts only, including open source accounting and no demonstrated repair recipe;

established mathematical and empirical domains:
    distributed-control literature provides known systems in which local relative constraints
    and global or leader control are operationally distinct;
    this does not establish that physical particles use either architecture;

Lineum hypothesis and analogy:
    an emergent collective object may require internally mediated, source-accounted,
    counterfactually path-dependent restoration;
    this remains untested in Lineum.
```

## 15. Current verdict

```text
owner_failure_gate = resolved
selected_repair = locality_reciprocity_plus_source_ledger
preregistration = frozen
confirmatory_execution = not_started
P2_application = prohibited
next_action = execute_frozen_synthetic_matrix_in_chatgpt_then_embed_code_and_results
```
