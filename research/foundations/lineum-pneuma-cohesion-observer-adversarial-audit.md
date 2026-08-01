# Adversarial Audit of the Pneuma-Inspired Cohesion Observer

**Status:** active negative-result audit; original fixture reproduced; autonomy discriminator failed  
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
**Direct predecessor:** `research/foundations/lineum-pneuma-cohesion-observer-fixture.md`, version 0.2.0, blob `2cc957d7d40907a092f8762bb73ccff7bfdf7e70`  
**Operational task:** ClickUp `869echn1w`  
**Scope:** Independent reproduction and adversarial challenge of the known-answer cohesion observer before any application to P2 or another Lineum state.  
**Central question:** Does the frozen observer distinguish internally self-maintained cohesion from externally imposed shape restoration, or does it only detect that some force restores a reference geometry?  
**Current confidence:** high that the published fixture results reproduce; high that the current observer cannot establish autonomy; high that application to Lineum must remain blocked until source and intervention controls are added.

## 1. Answer first

The original synthetic result reproduces exactly, but its scientific interpretation is too strong.

The fixture correctly distinguishes an active spring network from three copies of the same force-free continuation and from a minimally perturbed sham. It does not yet distinguish internal self-organization from an external controller that continuously restores the same shape while preserving free center-of-mass motion.

An adversarial external shape controller passed every frozen cohesion gate in all seeds and timesteps:

```text
external-controller false positives:
    dt = 0.0100: 12 / 12
    dt = 0.0050: 12 / 12
    dt = 0.0025: 12 / 12
    total:          36 / 36
```

Therefore:

```text
shape_restoration_detection = reproduced
internal_autonomous_cohesion = not_identified
observer_status = invalid_or_incomplete_for_lineum_application
P2_application = blocked
```

## 2. What was independently reproduced

The complete executable code embedded in the predecessor report was transcribed and executed in an independent Python environment.

The reported classification matrix reproduced:

```text
elastic:
    12 / 12 positives at each of three timesteps

gas:
    0 / 12 positives

advected_gas:
    0 / 12 positives

external_history:
    0 / 12 positives

sham_elastic:
    0 / 12 positives
```

Representative primary-step means at `dt = 0.01`:

```text
elastic initial shape error:       0.25845593664874883
elastic final shape error:         0.002232743248694602
elastic mean shape recovery:       0.9913701714366988
elastic mean pair recovery:        0.9856232926563692
elastic mean effective stiffness:  7.389055809538809
maximum bulk-velocity error:        2.237726045655905e-16
```

The timestep trend also reproduced. This confirms implementation consistency for the declared spring toy; it does not validate the observer's causal interpretation.

## 3. Structural weakness in the original controls

The published code defines:

```python
active = case in ("elastic", "sham_elastic")
```

The cases `gas`, `advected_gas`, and `external_history` all use:

```text
the same perturbed positions;
the same common bulk velocity;
zero internal force;
the same ballistic continuation.
```

They are different labels for the same dynamical control. In particular:

```text
external_history != external organizer removed during a simulated preparation phase
external_history == gas with a narrative label
```

The test therefore contains only three distinct dynamics:

1. active internal springs;
2. force-free ballistic continuation;
3. active springs with a perturbation below the eligibility threshold.

The reported `144 / 144` null and sham true negatives overstate control diversity because three null labels are dynamically identical.

## 4. Adversarial external-controller control

A new control was added without changing any observer threshold.

The controller acts on centered coordinates:

```text
X_c = X - mean(X)
V_c = V - mean(V)
F_ext = -k (X_c - R) - gamma V_c
k = 4.0
gamma = 2.0
```

where `R` is the same reference geometry used by the observer.

Properties:

```text
restoring force = external and reference-aware
center-of-mass force = exactly zero
bulk translation = conserved
shape recovery = expected
pair-distance recovery = expected
no internal pairwise interaction protocol = present
```

This is a deliberately adversarial analogue of a hidden external organizer. It should be rejected by an autonomy observer.

## 5. Adversarial results

Across seeds `200..211`:

```text
dt = 0.01:
    cohesive verdicts:       12 / 12
    minimum shape recovery:  0.9976243479516124
    minimum pair recovery:   0.9952871940745723
    minimum k_eff:           3.9990510530892056
    maximum bulk error:      1.5021383168150947e-15

dt = 0.005:
    cohesive verdicts:       12 / 12
    minimum shape recovery:  0.9975203688991212
    minimum pair recovery:   0.9950799156631079
    minimum k_eff:           3.9990510530892056
    maximum bulk error:      1.7843618982877262e-15

dt = 0.0025:
    cohesive verdicts:       12 / 12
    minimum shape recovery:  0.9974676882786040
    minimum pair recovery:   0.9949748458206163
    minimum k_eff:           3.9990510530892056
    maximum bulk error:      1.4812222630807097e-15
```

No threshold was tuned for this control. The false-positive result is stable under the same timestep refinement used by the predecessor.

## 6. Why the observer fails

The verdict is:

```text
cohesive = meaningful_perturbation
           and restoring_force
           and shape_recovery
           and pair_recovery
           and bulk_motion_conservation
```

Every term describes observable restoration, but none establishes where the restoring information and work originate.

The `k_eff` score uses the total supplied force. It cannot distinguish:

```text
internal reciprocal interactions;
external coordinate-wise feedback;
a hidden reference template;
a continuously supplied organizing field;
a boundary controller;
a nonlocal oracle with access to the target shape.
```

The observer therefore measures `reference-directed restoration`, not autonomous cohesion.

## 7. Additional limitations identified

### 7.1 No source-removal experiment

The predecessor describes source-off autonomy, but no external source is actually run and then removed. The `external_history` case is force-free for the entire challenge.

### 7.2 No member-turnover or deletion lane

The conceptual audit and collective-particle preregistration require robustness to member removal, exchange, or turnover. The validated fixture keeps all sixteen labeled points throughout.

### 7.3 Reference geometry is supplied to both law and observer

The spring network stores exact rest lengths derived from the target reference, and the observer compares against the same target. This is appropriate for a known-answer restoration toy, but too favorable for testing emergent identity.

### 7.4 The pair-distance signature is not a complete identity invariant

Sorted pair distances are permutation invariant, but distinct point configurations can share the same distance multiset. The metric should remain one member of an observer ensemble, not a complete object identifier.

### 7.5 Force access may not transfer to Lineum

The current Lineum observer may have access to states and update laws but not a unique decomposition into internal, external, boundary, and intervention forces. A causal intervention and accounting protocol is required.

## 8. Independent audit classification

```text
what_the_toy_implementation_computes:
    a reference-restoring spring network or force-free ballistic points;

what_was_reproduced:
    the spring network repairs the declared deformation with timestep-stable metrics;

what_the_adversarial_run_observed:
    an external reference-aware controller passes all current cohesion gates;

cautious_interpretation:
    the observer detects restoration but not autonomy;

hypothesis:
    autonomy may require source-removal, locality, reciprocity, work accounting,
    member-turnover, and hidden-template controls;

physical_correspondence:
    none; neither pneuma nor a Lineum particle was tested.
```

## 9. Failure-to-mechanism analysis

### What failed

The exact claim that the observer distinguishes internally restoring organization from externally imposed order is falsified within the tested synthetic domain.

### What remains positive

- deformation and recovery metrics are numerically stable;
- the spring fixture provides a useful positive restoration control;
- the sham gate correctly prevents claims from negligible challenges;
- translation removal and bulk-motion accounting work in the declared toy;
- the adversarial failure identifies a precise missing causal distinction.

### Failure location

```text
equation = not the primary failure
integration = not the primary failure
threshold = not the primary failure
observer causal scope = primary failure
control diversity = primary failure
interpretation = too strong
```

### Distinct repair classes

```text
R1 source-removal repair:
    run an external organizer during formation, remove it at a frozen time,
    and require continued restoration under new perturbations;

R2 locality-and-reciprocity repair:
    require restoration to arise from bounded local reciprocal interactions rather than
    coordinate-wise access to a global reference;

R3 accounting repair:
    measure intervention work, source work, boundary flux, and internal exchange so hidden
    external work cannot be called self-maintenance;

R4 template-blind repair:
    infer the restored organization from pre-intervention history and held-out prediction,
    not from a privileged supplied target shape;

R5 turnover repair:
    remove, replace, and permute members while testing recovery of relational invariants;

R6 causal-scramble repair:
    preserve snapshots and coarse trajectories while scrambling the interaction graph or
    source pathway, then test whether the same recovery remains.
```

No repair is selected in this report because the repository's negative-result owner gate requires the project owner's intuitive response before a replacement protocol is frozen.

## 10. Root-programme impact matrix

| Root branch | Relation | Result |
|---|---|---|
| Collective-particle preregistration | `constrains` | Shape restoration alone cannot support collective autonomy. |
| P2 vortex-gas remnant | `unaffected` | Application remains blocked. |
| Minimum-flux observer limitation | `supports` | Another apparently successful observer is shown to be non-identifying. |
| Source-accounting programme | `supports` | Hidden organizer work must be included before self-maintenance claims. |
| Mu and history reconstruction | `supports` | Template-blind history-based prediction remains a needed comparison. |
| Ancient-text audit | `constrains` | Pneuma-inspired cohesion remains useful only after autonomy controls. |
| Physical particle or soul correspondence | `unaffected` | No physical claim advanced. |

## 11. Current verdict

```text
published_fixture_reproduction = passed
published_fixture_numerical_stability = passed
control_diversity = insufficient
external_controller_adversarial_control = failed_36_of_36
shape_restoration_observer = supported
internal_autonomy_observer = falsified_within_tested_domain
member_turnover_observer = not_tested
source_off_organizer_removal = not_tested
P2_application = prohibited
next_action = owner_failure_gate_then_freeze_smallest_autonomy_discriminator
```

## 12. Reproduction note

The independent audit used NumPy in the ChatGPT Python execution environment. It did not import Lineum modules, access a local repository checkout, modify production code, or execute P2. The predecessor's embedded code and constants were transcribed directly. The adversarial controller used the same seeds, timesteps, horizon, reference geometry, initial deformation, observer metrics, and thresholds.
