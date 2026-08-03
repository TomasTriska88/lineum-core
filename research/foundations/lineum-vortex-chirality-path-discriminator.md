# Vortex Chirality Path Discriminator

**Status:** active negative-result report; sub-grid localization passed, but the frozen achiral null was charge-aware chiral  
**Version:** 0.3.0  
**Evidence cutoff:** 2026-08-03  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Parent audit:** `research/foundations/lineum-vortex-chirality-parity-existing-hypothesis-audit.md`, version 0.1.0, commit `ad422c0b96858fba75b4a407939a0d3bce2e96c8`  
**Preregistration commit:** `6d30759ffa4c29001712b17905540717c544aff0`  
**Preregistration blob:** `4f05f8212d002cacb6130c93127967fc61b344f7`  
**Receipt-correction checkpoint:** `1e917cbb5e5750f0b159df38331b50a481e66799`  
**Frozen scientific-source SHA-256:** `7d766543634135231315eb676006cb445ba9ff051b8098f7c2620f00b2fbe8c7`  
**Instrumentation-corrected source SHA-256:** `cfebe7b60962276646e3232a6cbfe7c3397833608e93ccb51c2f0ea00e6ed9b2`  
**Immediate numerical predecessor:** `research/foundations/lineum-synthetic-vortex-field-causal-observer.md`, version 0.2.0, blob `aff6a5362f06b7258fe64b2234426db05d974d37`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`, recovered version 0.4.14, evidence cutoff 2026-07-29, blob `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, version 0.3.0, blob `5304874451caf32313ad0e8e3c59e53958698d79`  
**Scope:** Two independent known-answer tests: sub-grid localization of analytic complex-field vortices, and kinematic path connectivity between a labelled planar constellation and its mirror. No current Lineum equation or module was imported. No P2 state was used.  
**Central questions:** Can a field-only estimator remove plaquette-centre grid-phase error? Does a mirror endpoint define a distinct sector for free labelled points, or only when an additional oriented relation is explicitly protected?  
**Current confidence:** high that the frozen sub-grid localization lane passed in the analytic renderer; high that free collision-free mirror reachability, protected-cycle obstruction, teleport detection, and relabelling detection worked in the declared fixture; high that the selected rectangle was not a valid charge-aware achiral null; zero evidence for intrinsic Lineum chirality, a particle, spinor, gauge field, fermionic statistics, or physical correspondence.

## 1. Answer first

The corrected frozen execution produced one strong positive result and one genuine test-design failure.

The field-only sub-grid estimator passed every localization gate. It reduced the mean core-position error from `0.0412218` model units for plaquette centres to `0.00134168` for bilinear complex-zero interpolation, a reduction by approximately `96.75%`. The result converged monotonically across grids `64`, `96`, and `144`, agreed with an independent affine estimator, and remained invariant under a global field phase.

The path fixture also passed every dynamic and continuity control. Free labelled points reached their mirror without collision; a protected oriented cycle rejected that path when signed area reached zero; a same-sector path retained orientation; teleportation and same-charge relabelling produced large discontinuities.

However, the frozen supposed achiral null failed:

```text
rectangle mirror error = 0.4850712500726661
required error < 1e-10
```

The rectangle is geometrically achiral when charges are ignored. With the frozen alternating charge assignment, reflection swaps the positive and negative spatial sublattices. No allowed proper rotation plus charge-preserving permutation maps the reflected charged configuration back to the original. The null was therefore not charge-aware achiral.

The accepted outcomes are:

```text
localization_outcome = PASS_SUBGRID_LOCALIZATION
path_outcome = FAIL_STATIC_CHIRALITY_CONTROL
overall_pass = false
```

No fixture, charge, threshold, estimator, metric, path, seed, or grid was changed after seeing the result.

## 2. Preserved execution history

### 2.1 Attempt 1

The exact preregistered source completed its scientific calculations but failed at final JSON serialization because NumPy boolean scalars were not converted to native JSON types.

```text
source SHA-256 = 7d766543634135231315eb676006cb445ba9ff051b8098f7c2620f00b2fbe8c7
exception = TypeError: Object of type bool is not JSON serializable
complete receipt = no
scientific result accepted = no
```

### 2.2 Frozen instrumentation correction

Version 0.2.0 froze one correction at the output boundary only: recursive conversion of NumPy scalar values to ordinary Python JSON scalar values. All scientific calculations and decision rules remained unchanged.

```text
corrected source SHA-256 = cfebe7b60962276646e3232a6cbfe7c3397833608e93ccb51c2f0ea00e6ed9b2
```

### 2.3 Attempt 2

```text
exit = normal
execution time = 3.943460464477539 seconds
raw stdout bytes = 78277
raw stdout SHA-256 = de7d5be3dc50853355009ac788ebb39603d7b8fc6acde02ff32a13dd1ce90cd9
canonical compact receipt SHA-256 = 033e0dae221cfc2b55b5519039c2f6fdcc25ea623896fc75df89f639c6448db8
```

The second execution was the single corrected run authorized by version 0.2.0.

## 3. Frozen implementation

The exact complete executable source is preserved in the preregistration version 0.1.0. Its scientific source hash is recorded above. The correction in version 0.2.0 changes only JSON scalar representation.

The field renderer computes:

```text
phase(x) = global_phase + sum_i q_i atan2(y-y_i, x-x_i)
amplitude(x) = product_i tanh(|x-x_i| / 0.18)
psi(x) = amplitude(x) exp(i phase(x))
```

The detector obtains integer plaquette winding. Three position representations are compared:

```text
plaquette-centre baseline;
bilinear complex-zero Newton intersection from the four plaquette corners;
independent affine Re/Im zero intersection from a local 4 x 4 node fit.
```

The path observer uses labelled positions, charge-preserving static matching, proper-rotation quotienting, signed cycle area, minimum pair separation, maximum labelled inter-frame jump, and two independent signed-area implementations.

## 4. Frozen parameters

```text
domain = [-4,4] x [-4,4]
grids = 64, 96, 144
seeds = 1000..1023
core radius = 0.18
global-phase control = 1.2345 radians
path frames = 101
six-core charges = [+1,-1,+1,-1,+1,-1]
```

The irregular six-core reference before centring is:

```text
[ [ 1.65,  0.15],
  [ 0.72,  1.55],
  [-0.86,  0.96],
  [-1.72, -0.25],
  [-0.28, -1.50],
  [ 1.12, -0.86] ]
```

The alleged achiral null was:

```text
positions = [[-1.0,-0.6],[1.0,-0.6],[1.0,0.6],[-1.0,0.6]]
charges = [+1,-1,+1,-1]
```

## 5. Localization result

All `216` seed-grid-fixture records passed their declared detection and localization gates.

### 5.1 Aggregate improvement

```text
mean plaquette-centre error = 0.04122176310426325
mean bilinear-zero error = 0.0013416769123272344
bilinear / centre ratio = 0.032547826...
relative reduction = approximately 96.75%
```

Mean bilinear error by grid:

```text
grid 64  = 0.0026969625348004698
grid 96  = 0.0009800540994748703
grid 144 = 0.00034801410270636257
```

The absolute error decreased monotonically under refinement.

### 5.2 Fixture maxima

```text
single vortex, 72 records:
    plaquette-centre max = 0.06290923798867208
    bilinear max = 0.002599010265784559
    bilinear max / cell = 0.020467205843053404
    affine max / cell = 0.05610527582502896
    bilinear-affine disagreement max / cell = 0.05227681490914685

opposite-charge pair, 72 records:
    plaquette-centre max = 0.0839281833302944
    bilinear max = 0.004900796022868765
    bilinear max / cell = 0.038593768680091525
    affine max / cell = 0.17916277719501666
    bilinear-affine disagreement max / cell = 0.1561953188113752

six-core constellation, 72 records:
    plaquette-centre max = 0.08692821564507772
    bilinear max = 0.004095944111853094
    bilinear max / cell = 0.03225555988084312
    affine max / cell = 0.13979378180588595
    bilinear-affine disagreement max / cell = 0.11961931919976755
```

All values remained far below the frozen thresholds.

### 5.3 Relational geometry and phase

Maximum symmetry-quotiented geometry error:

```text
grid 64  = 0.002304564278343785
grid 96  = 0.0006123564850342387
grid 144 = 0.0002033162700165579
```

The frozen limits were `0.040`, `0.025`, and `0.025` respectively.

Maximum global-phase output difference:

```text
6.619278685455839e-16
```

The frozen limit was `1e-10`.

### 5.4 Localization verdict

```text
detections_exact = passed
bilinear_single_lt_0_25h = passed
bilinear_multi_lt_0_45h = passed
affine_multi_lt_0_75h = passed
independent_agreement_lt_0_80h = passed
mean_bilinear_lt_0_45_center = passed
geometry_grid64_lt_0_040 = passed
geometry_grid96_lt_0_025 = passed
geometry_grid144_lt_0_025 = passed
global_phase_invariant_lt_1e_10 = passed
resolution_monotone = passed
localization_outcome = PASS_SUBGRID_LOCALIZATION
```

Narrow interpretation:

```text
A local complex-zero estimator can remove the dominant plaquette-centre grid-phase error
inside this analytic rendered-field fixture.
```

Prohibited interpretation:

```text
This does not prove localization accuracy in current Lineum dynamics, near noisy cores,
during creation or annihilation, or in the retained P2 population.
```

## 6. Path result

### 6.1 Positive known-answer controls

The irregular charge-aware constellation was statically distinguishable from its mirror:

```text
static chiral error = 0.14942352551176447
frozen requirement > 0.08
```

The free prescribed mirror path reached the endpoint continuously:

```text
minimum pair separation = 0.4
frozen requirement > 0.25
maximum labelled step = 0.0365000000000002
frozen requirement < 0.10
minimum absolute normalized signed area = 0.0
signed area changed sign = yes
endpoint matched the mirror below 1e-12 = yes
```

Therefore the free labelled point set was mirror-connected in the declared fixture. It became collinear at the midpoint without point collision.

The protected oriented-cycle observer rejected that same path because its signed area reached zero. A same-sector positive path retained orientation:

```text
minimum normalized signed area = 1.0
minimum pair separation = 1.1227329379687763
maximum labelled step = 0.018978663859660065
```

Continuity attacks were detected:

```text
teleport maximum labelled jump = 4.8345113506951245
same-charge relabelling maximum labelled jump = 2.7545500845888
frozen requirement for each > 0.80
```

The two signed-area implementations agreed exactly in the tested floating-point output:

```text
maximum disagreement = 0.0
reference signed area = 6.178850000000001
mirror signed area = -6.178850000000001
```

### 6.2 Failed achiral null

```text
achiral rectangle mirror error = 0.4850712500726661
frozen requirement < 1e-10
```

The geometry of the rectangle is mirror-symmetric, but the alternating charge decoration is not invariant under the allowed transformations. Reflection maps the positive defects to the spatial sites occupied by negative defects in the reference. The observer correctly preserved charge and therefore rejected the mirror.

This is a fixture failure rather than evidence that every rectangular point set is chiral.

### 6.3 Path gate table

```text
static_chiral_error_gt_0_08 = passed
achiral_error_lt_1e_10 = failed
free_endpoint_exact = passed
free_min_separation_gt_0_25 = passed
free_area_changes_sign = passed
free_area_hits_zero = passed
free_step_lt_0_10 = passed
protected_cycle_rejects_free_path = passed
same_sector_area_gt_0_80 = passed
same_sector_no_collision = passed
same_step_lt_0_10 = passed
teleport_jump_gt_0_80 = passed
relabel_jump_gt_0_80 = passed
area_implementations_agree = passed
mirror_area_negates = passed
path_outcome = FAIL_STATIC_CHIRALITY_CONTROL
```

## 7. Failure location

```text
field renderer = retained
plaquette winding detector = retained
bilinear sub-grid estimator = passed
independent affine estimator = passed
resolution and phase controls = passed
free mirror path = passed
protected oriented-cycle obstruction = passed
same-sector path = passed
teleport continuity attack = passed
same-charge relabelling attack = passed
irregular static chiral positive = passed
rectangle charge-aware achiral null = invalid and failed
complete path fixture = failed
```

The result falsifies the selected null fixture. It does not falsify static chirality measurement, free-point mirror connectivity, protected-cycle obstruction, or continuity attacks within their declared known-answer scope.

## 8. Failure-to-mechanism map

No replacement is selected in this version.

```text
R1 geometry-only achiral null:
    use an achiral point set without charge decoration to test only geometric symmetry;
    risk: it does not test the charge-aware observer used for vortices.

R2 charge-aware invariant null:
    choose a charge-decorated configuration whose mirror is demonstrably related by
    a proper rotation and a charge-preserving automorphism;
    risk: accidental additional symmetries can make the positive control weak.

R3 parity transforms charge:
    explicitly test a different transformation law in which reflection also maps
    charge or vortex species;
    risk: this would introduce a physical assumption not present in current Core.

R4 paired nulls:
    keep separate geometry-only and charge-aware achiral controls so that failure of
    one cannot be mistaken for failure of the other;
    risk: adds observer complexity but preserves the conceptual distinction.

R5 remove static achirality as a required path gate:
    retain static chirality only as a descriptor and let path accessibility decide;
    risk: loses a known-answer null for the static score and may hide overclassification.
```

The smallest useful next discriminator would compare at least one geometry-only achiral null and one mathematically proven charge-aware achiral null against the same irregular positive. Selection waits at the project-owner negative-result gate.

## 9. Evidence layers

### 9.1 What the implementation computes

A standalone analytic renderer generates complex scalar fields from prescribed vortex positions and charges. Plaquette winding detects charges. Two local interpolators estimate field zeros. A separate kinematic fixture evaluates static shape, signed area, pair separation, and labelled worldline jumps.

### 9.2 What was reproducibly observed

All localization gates and fourteen of fifteen path gates passed. The sole failed path gate was the allegedly achiral alternating-charge rectangle.

### 9.3 Cautious interpretation

Sub-grid complex-zero interpolation is a strong candidate replacement for plaquette-centre positions in future known-answer field observers. Static geometry, charge decoration, path connectivity, and continuing instance history must remain separate concepts.

### 9.4 Hypothesis only

A current Lineum vortex composite may or may not possess a protected oriented relation. No current Core trajectory was tested, and no signed cycle is known to be dynamically maintained by Lineum.

### 9.5 Established physics versus Lineum

Configuration-space and braid methods motivate separating endpoint shape from motion history. They do not establish that Lineum excitations instantiate the same physical topology or quantization.

## 10. Complete decision receipt

The full raw JSON output contained all `216` individual localization records and is cryptographically identified by the stdout and compact-receipt hashes in Section 2. The following machine-readable receipt contains every value used for the scientific decision and all frozen gates:

```json
{
  "attempt": 2,
  "compact_receipt_sha256": "033e0dae221cfc2b55b5519039c2f6fdcc25ea623896fc75df89f639c6448db8",
  "environment": {
    "numpy": "2.3.5",
    "platform": "Linux-6.12.13-x86_64-with-glibc2.41",
    "python": "3.13.5 (main, May  5 2026, 21:05:52) [GCC 14.2.0]"
  },
  "execution_seconds": 3.943460464477539,
  "localization": {
    "fixture_aggregates": {
      "pair": {
        "affine_max": 0.022750828850160845,
        "affine_max_over_h": 0.17916277719501666,
        "agreement_max_over_h": 0.1561953188113752,
        "bilinear_affine_max": 0.019834326198269865,
        "bilinear_max": 0.004900796022868765,
        "bilinear_max_over_h": 0.038593768680091525,
        "center_max": 0.0839281833302944,
        "count": 72
      },
      "single": {
        "affine_max": 0.007124479469844946,
        "affine_max_over_h": 0.05610527582502896,
        "agreement_max_over_h": 0.05227681490914685,
        "bilinear_affine_max": 0.006638325702748807,
        "bilinear_max": 0.002599010265784559,
        "bilinear_max_over_h": 0.020467205843053404,
        "center_max": 0.06290923798867208,
        "count": 72
      },
      "six": {
        "affine_max": 0.01775159134042996,
        "affine_max_over_h": 0.13979378180588595,
        "agreement_max_over_h": 0.11961931919976755,
        "bilinear_affine_max": 0.015189754819018101,
        "bilinear_max": 0.004095944111853094,
        "bilinear_max_over_h": 0.03225555988084312,
        "center_max": 0.08692821564507772,
        "count": 72
      }
    },
    "gates": {
      "affine_multi_lt_0_75h": true,
      "bilinear_multi_lt_0_45h": true,
      "bilinear_single_lt_0_25h": true,
      "detections_exact": true,
      "geometry_grid144_lt_0_025": true,
      "geometry_grid64_lt_0_040": true,
      "geometry_grid96_lt_0_025": true,
      "global_phase_invariant_lt_1e_10": true,
      "independent_agreement_lt_0_80h": true,
      "mean_bilinear_lt_0_45_center": true,
      "resolution_monotone": true
    },
    "geometry_error_max": {
      "144": 0.0002033162700165579,
      "64": 0.002304564278343785,
      "96": 0.0006123564850342387
    },
    "mean_bilinear_by_grid": {
      "144": 0.00034801410270636257,
      "64": 0.0026969625348004698,
      "96": 0.0009800540994748703
    },
    "mean_bilinear_error": 0.0013416769123272344,
    "mean_center_error": 0.04122176310426325,
    "pass": true,
    "phase_difference_max": 6.619278685455839e-16,
    "record_count": 216
  },
  "localization_outcome": "PASS_SUBGRID_LOCALIZATION",
  "overall_pass": false,
  "parameters": {
    "core_radius": 0.18,
    "domain_half": 4.0,
    "global_phase": 1.2345,
    "grids": [64, 96, 144],
    "path_frames": 101,
    "seeds": [1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023]
  },
  "path": {
    "achiral_error": 0.4850712500726661,
    "area_implementation_disagreement": 0.0,
    "free_max_step": 0.0365000000000002,
    "free_min_abs_normalized_area": 0.0,
    "free_min_separation": 0.4,
    "gates": {
      "achiral_error_lt_1e_10": false,
      "area_implementations_agree": true,
      "free_area_changes_sign": true,
      "free_area_hits_zero": true,
      "free_endpoint_exact": true,
      "free_min_separation_gt_0_25": true,
      "free_step_lt_0_10": true,
      "mirror_area_negates": true,
      "protected_cycle_rejects_free_path": true,
      "relabel_jump_gt_0_80": true,
      "same_sector_area_gt_0_80": true,
      "same_sector_no_collision": true,
      "same_step_lt_0_10": true,
      "static_chiral_error_gt_0_08": true,
      "teleport_jump_gt_0_80": true
    },
    "pass": false,
    "relabel_jump": 2.7545500845888,
    "same_max_step": 0.018978663859660065,
    "same_min_normalized_area": 1.0,
    "same_min_separation": 1.1227329379687763,
    "signed_area_mirror": -6.178850000000001,
    "signed_area_reference": 6.178850000000001,
    "static_chiral_error": 0.14942352551176447,
    "teleport_jump": 4.8345113506951245
  },
  "path_outcome": "FAIL_STATIC_CHIRALITY_CONTROL",
  "raw_stdout_bytes": 78277,
  "raw_stdout_sha256": "de7d5be3dc50853355009ac788ebb39603d7b8fc6acde02ff32a13dd1ce90cd9",
  "source_sha256": "cfebe7b60962276646e3232a6cbfe7c3397833608e93ccb51c2f0ea00e6ed9b2"
}
```

## 11. Root-programme impact matrix

| Root branch | Relation | Result |
|---|---|---|
| retained P2 recovery | `unaffected` | Exact recovery remains mandatory. |
| P2 observer | `depends_on` | Sub-grid localization is promising, but the path fixture is not fully validated and no P2 application is authorized. |
| minimum-flux observer limitation | `supports` | Known-answer null controls remain necessary before object assignment. |
| source accounting | `constrains` | A later dynamic path must ledger external work and regeneration. |
| causal-path point fixture | `supports` | Motion history and causal accessibility remain distinct from endpoint resemblance. |
| synthetic vortex-field observer | `supports` and `constrains` | Its grid-position failure was repaired in the analytic renderer; its charge-aware relational question remains open. |
| transplant, copying, heredity | `supports` | Teleport and relabelling attacks remained distinguishable from continuing instance history. |
| historical spinor and vector-gauge branches | `unaffected` | No new field or spinor state was introduced. |
| `mu`, `kappa`, membrane, Eq-11.1, epsilon, Relic Foam | `not_yet_compared` | No mechanism from those lanes was used. |
| particle, life, soul, entanglement, cosmology | `unaffected` | No physical correspondence advanced. |

## 12. Current verdict

```text
preregistration_preserved = true
receipt_correction_only = true
corrected_execution_completed = true
localization_outcome = PASS_SUBGRID_LOCALIZATION
path_outcome = FAIL_STATIC_CHIRALITY_CONTROL
overall_pass = false
subgrid_localization = validated_in_analytic_renderer
free_point_mirror_path = supported_in_kinematic_fixture
protected_cycle_obstruction = supported_in_kinematic_fixture
teleport_rejection = supported_in_kinematic_fixture
same_charge_relabelling_rejection = supported_in_kinematic_fixture
charge_aware_achiral_null = falsified
complete_path_observer = not_validated
P2_application = prohibited
Core_change = none
whitepaper_change = none
next_action = owner_failure_gate_before_selecting_replacement_null
```

## 13. Prohibited interpretations

```text
no claim that current Lineum vortices are intrinsically chiral;
no claim that a Lineum mirror is the same or a different object;
no claim that current Lineum dynamics generates the prescribed mirror path;
no spin-1/2, fermion, parity-violation, WZW, or vector-gauge claim;
no application to P2;
no Core or whitepaper promotion.
```
