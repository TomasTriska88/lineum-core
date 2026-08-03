# Vortex Chirality Path Discriminator

**Status:** active preregistered execution; first exact run reached a receipt-serialization exception; one instrumentation-only correction frozen  
**Version:** 0.2.0  
**Evidence cutoff:** 2026-08-03  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Parent audit:** `research/foundations/lineum-vortex-chirality-parity-existing-hypothesis-audit.md`, version 0.1.0, commit `ad422c0b96858fba75b4a407939a0d3bce2e96c8`  
**Preregistration commit:** `6d30759ffa4c29001712b17905540717c544aff0`  
**Preregistration blob:** `4f05f8212d002cacb6130c93127967fc61b344f7`  
**Frozen scientific-source SHA-256:** `7d766543634135231315eb676006cb445ba9ff051b8098f7c2620f00b2fbe8c7`  
**Instrumentation-corrected source SHA-256:** `cfebe7b60962276646e3232a6cbfe7c3397833608e93ccb51c2f0ea00e6ed9b2`  
**Immediate numerical predecessor:** `research/foundations/lineum-synthetic-vortex-field-causal-observer.md`, version 0.2.0, blob `aff6a5362f06b7258fe64b2234426db05d974d37`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`, recovered version 0.4.14, evidence cutoff 2026-07-29, blob `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, version 0.3.0, blob `5304874451caf32313ad0e8e3c59e53958698d79`  
**Scope:** Two independent known-answer tests: sub-grid localization of analytic complex-field vortices, and kinematic path connectivity between a labelled planar constellation and its mirror. No current Lineum equation or module is imported. No P2 state is used.  
**Central questions:** Can a field-only estimator remove plaquette-centre grid-phase error? Does a mirror endpoint define a distinct sector for free labelled points, or only when an additional oriented relation is explicitly protected?  
**Current confidence:** high in the analytic distinction between free point connectivity and protected signed-cycle obstruction; scientific gates are not yet accepted because the first exact run emitted no complete receipt; zero evidence for a Lineum particle, intrinsic chirality, spinor, gauge field, fermionic statistics, or physical correspondence.

## 1. Answer first

The first exact run did not produce an accepted scientific result.

The complete preregistered computation reached its final JSON output call and then raised:

```text
TypeError: Object of type bool is not JSON serializable
```

The offending objects are NumPy boolean scalars created by frozen comparisons. This is a receipt-formatting defect, not a change in the field detector, estimators, fixtures, metrics, thresholds, paths, or classifications.

No scientific gate from that run is accepted. A one-time instrumentation-only correction is frozen before another execution:

```text
convert NumPy scalar values recursively to ordinary Python JSON scalars;
leave every scientific computation and decision rule byte-for-byte unchanged;
execute the corrected source once;
stop if any scientific gate fails.
```

## 2. Owner principle and bounded question

The project owner proposed that mirror identity should be decided by whether the system can reach the mirror through its own continuous evolution without disintegration, reconstruction, protected-topology change, or external instruction.

This fixture tests only the prerequisite kinematic and observational logic:

```text
Does an admissible continuous path exist under declared constraints?
Does the observer identify the event that makes a protected path inadmissible?
```

Every path remains prescribed known-answer data. No path may be called autonomous.

## 3. Why free planar points and protected cycles are separated

The test distinguishes two state spaces.

### 3.1 Free labelled points

The only protected condition is that labelled points remain distinct. The frozen path to the mirror is:

```text
x_i(t) = (1 - 2t) x_i(0)
y_i(t) = y_i(0)
```

All frozen y-coordinates are distinct, so the midpoint is collinear but collision-free. A static signed area crosses zero, but zero area is not prohibited for free points.

### 3.2 Protected oriented cycle

The same points additionally retain fixed cyclic worldline order and nonzero signed cycle area. Since reflection reverses the area sign, every continuous path between the endpoints must cross zero area. Under this declared ontology the free mirror path is inadmissible.

The obstruction comes from the protected oriented relation, not from the point set alone.

## 4. Primary-source constraints

1. Robert Ghrist, **Configuration spaces and braid groups on graphs in robotics**, 1999, arXiv:math/9905023.
2. Spencer A. Smith, **Point Vortices: Finding Periodic Orbits and their Topological Classification**, 2015, arXiv:1510.06756.
3. C. L. Phillips, T. Peterka, D. Karpeyev, and A. Glatz, **Detecting vortices in superconductors: Extracting one-dimensional topological singularities from a discretized complex scalar field**, 2015, arXiv:1501.03207.
4. Bogdan Damski and Krzysztof Sacha, **Changes of the topological charge of vortices**, 2002, arXiv:quant-ph/0202137.
5. Dave Auckly and Martin Speight, **Fermionic quantization and configuration spaces for the Skyrme and Faddeev-Hopf models**, 2004, arXiv:hep-th/0411010.
6. Matthew J. Bright, Andrew I. Cooper, and Vitaliy A. Kurlin, **Continuous chiral distances for two-dimensional lattices**, 2023, DOI `10.1002/chir.23598`.

These sources constrain the fixture only. They do not validate Lineum or establish physical vortices, molecules, Skyrmions, quantum particles, spinors, or fermionic statistics.

## 5. Frozen field and localization protocol

```text
domain = [-4,4] x [-4,4]
grids = 64, 96, 144
seeds = 1000..1023
core radius = 0.18
global-phase control = 1.2345 radians
six-core charges = [+1,-1,+1,-1,+1,-1]
```

The rendered field is:

```text
phase(x) = global_phase + sum_i q_i atan2(y-y_i, x-x_i)
amplitude(x) = product_i tanh(|x-x_i| / 0.18)
psi(x) = amplitude(x) exp(i phase(x))
```

Plaquette winding detects integer charge. Three centre representations are compared:

```text
plaquette centre baseline;
bilinear complex-zero Newton solve using the four plaquette corners;
independent affine real/imaginary zero intersection using a local 4 x 4 node fit.
```

Fixtures per seed and grid:

```text
one random +/- unit vortex;
a +/- pair separated by 1.35 with random pose;
a fixed irregular six-vortex constellation with random rotation and sub-cell shift;
a 37-degree rotation plus shift [0.43,-0.31];
a global phase shift.
```

The centred irregular reference before transformations is:

```text
[ [ 1.65,  0.15],
  [ 0.72,  1.55],
  [-0.86,  0.96],
  [-1.72, -0.25],
  [-0.28, -1.50],
  [ 1.12, -0.86] ]
```

Frozen localization gates:

```text
exact defect count and charges in every fixture;
bilinear single-core max error < 0.25 cell;
bilinear pair/six max error < 0.45 cell;
affine pair/six max error < 0.75 cell;
bilinear-affine max disagreement < 0.80 cell;
mean bilinear error < 0.45 * mean plaquette-centre error;
maximum symmetry-quotiented geometry error < 0.040 on grid 64;
maximum geometry error < 0.025 on grids 96 and 144;
global-phase output change < 1e-10;
mean absolute bilinear error decreases monotonically with grid refinement.
```

## 6. Frozen path protocol

The centred irregular reference has labels `0..5`, charges `[+1,-1,+1,-1,+1,-1]`, and cycle edges `(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)`.

Every path contains 101 frames.

Controls:

```text
free mirror path:
    x scales continuously from +1 to -1;
    y remains fixed;

same-sector path:
    proper rotation 0.8t;
    positive scales 1+0.10t and 1-0.05t;
    shift [0.25t,-0.18t];

achiral static rectangle:
    [[-1,-0.6],[1,-0.6],[1,0.6],[-1,0.6]];
    charges [+1,-1,+1,-1];

teleport attack:
    frame 51 jumps to mirror plus [1.1,-0.9];

same-charge relabelling attack:
    labels 0 and 2 exchange after frame 50 while geometry remains smooth.
```

Frozen path gates:

```text
irregular mirror static error > 0.08;
achiral rectangle mirror error < 1e-10;
free path endpoint equals mirror below 1e-12;
free path minimum pair separation > 0.25;
free path signed area changes sign and reaches normalized zero below 1e-12;
ordinary free-path step < 0.10;
protected-cycle observer rejects the free path at zero area;
same-sector normalized signed area remains > 0.80;
same-sector minimum separation > 0.25 and step < 0.10;
teleport labelled jump > 0.80;
relabel labelled jump > 0.80;
two signed-area implementations agree below 1e-12;
mirror area equals negative reference area below 1e-12.
```

## 7. Frozen scientific outcome classes

```text
localization_outcome:
    PASS_SUBGRID_LOCALIZATION
    FAIL_FIELD_DETECTION
    FAIL_SUBGRID_LOCALIZATION
    FAIL_LOCALIZATION_INDEPENDENT_CHECK

path_outcome:
    PASS_PATH_COMPONENT_OBSERVER
    FAIL_STATIC_CHIRALITY_CONTROL
    FAIL_FREE_PATH_CONTROL
    FAIL_PROTECTED_CYCLE_CONTROL
    FAIL_CONTINUITY_ATTACK_CONTROL
```

No scientific outcome was accepted from the first exact run because no complete JSON receipt was emitted.

## 8. First exact execution receipt

```json
{
  "attempt": 1,
  "source_sha256": "7d766543634135231315eb676006cb445ba9ff051b8098f7c2620f00b2fbe8c7",
  "exit": "exception",
  "exception_type": "TypeError",
  "exception_message": "Object of type bool is not JSON serializable",
  "complete_json_receipt_emitted": false,
  "scientific_gate_result_accepted": false,
  "parameter_change": false,
  "metric_change": false,
  "threshold_change": false,
  "fixture_change": false
}
```

The execution environment was Python 3.13 with NumPy 2.x on Linux. A NumPy deprecation warning for two-dimensional `np.cross` was also emitted; it did not stop execution and does not motivate a code change in this checkpoint.

## 9. Minimal reproduction of the receipt defect

```python
import json
import numpy as np

receipt = {"gate": np.bool_(True)}
json.dumps(receipt)
```

Expected result:

```text
TypeError: Object of type bool is not JSON serializable
```

## 10. Frozen instrumentation-only correction

The complete scientific source remains the source committed in version 0.1.0. The only authorized textual replacement is the final JSON serialization boundary.

Original final statement:

```python
print(json.dumps(RECEIPT, indent=2, sort_keys=True))
```

Frozen replacement:

```python
def to_jsonable(value):
    if isinstance(value, dict):
        return {str(key): to_jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [to_jsonable(item) for item in value]
    if isinstance(value, tuple):
        return [to_jsonable(item) for item in value]
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value

print(json.dumps(to_jsonable(RECEIPT), indent=2, sort_keys=True))
```

Correction classification:

```text
scientific state generation = unchanged
field renderer = unchanged
detector = unchanged
estimators = unchanged
fixtures and paths = unchanged
seeds and grids = unchanged
metrics and gates = unchanged
outcome classification = unchanged
only JSON scalar representation = changed
```

The corrected complete source SHA-256 is:

```text
cfebe7b60962276646e3232a6cbfe7c3397833608e93ccb51c2f0ea00e6ed9b2
```

Exactly one corrected execution is authorized.

## 11. Interpretation rules after corrected execution

If a scientific gate fails, stop without changing the fixture. Record which lane failed and preserve the other lane independently.

If both lanes pass, only the known-answer observer is validated. A later separately preregistered test must still ask whether a local Lineum-like law generates an admissible path without an external target.

## 12. Prohibited interpretations

```text
no accepted scientific result from attempt 1;
no claim of intrinsic Lineum chirality;
no claim that a Lineum mirror is same or different;
no spin-1/2, fermion, parity-violation, WZW, or gauge-field claim;
no claim that prescribed paths are autonomous;
no P2 application;
no Core or whitepaper change.
```

## 13. Root-programme impact

| Root branch | Relation | Current effect |
|---|---|---|
| retained P2 recovery | `unaffected` | Exact recovery remains mandatory. |
| P2 observer | `depends_on` | No application before accepted known-answer receipts. |
| source accounting | `constrains` | A later dynamic path must ledger external work. |
| causal-path toy | `supports` | History and causal accessibility remain distinct from endpoint resemblance. |
| transplant and copying | `supports` | Teleport and relabelling are retained adversarial controls. |
| historical spinor / vector gauge | `unaffected` | No new field was introduced. |
| physical particle, life, soul, quantum, cosmology | `unaffected` | No correspondence was tested. |

## 14. Current verdict

```text
preregistration_preserved = true
first_exact_execution_completed_normally = false
first_exact_execution_exception = receipt_serialization
scientific_result_accepted = false
instrumentation_only_correction_frozen = true
corrected_execution_authorized = one
P2_application = prohibited
Core_change = none
whitepaper_change = none
next_action = run_corrected_source_once_then_stop_on_any_scientific_failure
```
