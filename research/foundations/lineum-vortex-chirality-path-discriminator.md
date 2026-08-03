# Vortex Chirality Path Discriminator

**Status:** active preregistration; execution not started  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-03  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Parent audit:** `research/foundations/lineum-vortex-chirality-parity-existing-hypothesis-audit.md`, version 0.1.0, commit `ad422c0b96858fba75b4a407939a0d3bce2e96c8`  
**Immediate numerical predecessor:** `research/foundations/lineum-synthetic-vortex-field-causal-observer.md`, version 0.2.0, blob `aff6a5362f06b7258fe64b2234426db05d974d37`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`, recovered version 0.4.14, evidence cutoff 2026-07-29, blob `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, version 0.3.0, blob `5304874451caf32313ad0e8e3c59e53958698d79`  
**Scope:** Two independent known-answer tests: sub-grid localization of analytic complex-field vortices, and kinematic path connectivity between a labelled planar constellation and its mirror. No current Lineum equation or module is imported. No P2 state is used.  
**Central questions:** Can a field-only estimator remove plaquette-centre grid-phase error? Does a mirror endpoint define a distinct sector for free labelled points, or only when an additional oriented relation is explicitly protected?  
**Current confidence:** high in the analytic distinction between free point connectivity and protected signed-cycle obstruction; unknown whether the frozen sub-grid estimators pass their numerical gates; zero evidence for a Lineum particle, intrinsic chirality, spinor, gauge field, fermionic statistics, or physical correspondence.

## 1. Answer first

The next test deliberately separates two issues that the failed observer mixed together.

First, a vortex centre should not be replaced by the centre of the square containing it. The field itself has a complex zero at the core, so two independent local interpolators will estimate that zero below the mesh scale.

Second, a mirror image is not automatically a separate topological sector. A collection of distinct labelled points in a plane can generally move continuously to its mirror without point collision. The frozen free-point path used here simply compresses all x-coordinates through zero while keeping six distinct y-coordinates. At the midpoint the points are collinear but remain distinct.

An oriented embedded cycle is different only because an additional relation is protected. Its signed area starts positive and ends negative. By continuity, every path between those endpoints must pass through zero signed area. A nondegenerate-orientation rule therefore rejects the mirror path, but the rejection comes from the declared cycle structure, not from the point set alone.

Expected conceptual result:

```text
free labelled points:
    mirror is kinematically reachable without collision;

same points plus protected nondegenerate oriented cycle:
    mirror path must violate the protected orientation condition;

matching final picture with teleport or relabelling:
    not the same continuing instance;

static chirality score:
    useful descriptor, not a proof of disconnected identity sectors.
```

## 2. Owner principle and its bounded translation

The project owner proposed that mirror identity should be decided by whether the system can reach the mirror through its own continuous evolution without disintegration, reconstruction, protected-topology change, or external instruction.

This fixture tests only the prerequisite kinematic and observational logic:

```text
Does an admissible continuous path exist under declared constraints?
Does the observer correctly identify the event that makes a protected path inadmissible?
```

It does not yet test whether a current Lineum local law spontaneously generates such a path. Every path in this report is prescribed known-answer data and is therefore not autonomous.

## 3. Primary-source constraint audit

The preregistration is constrained by the following external work.

1. Robert Ghrist, **Configuration spaces and braid groups on graphs in robotics**, 1999, arXiv:math/9905023. Distinct labelled points are naturally represented by configuration spaces; braid groups describe nontrivial motion histories while collision avoidance is explicit.
2. Spencer A. Smith, **Point Vortices: Finding Periodic Orbits and their Topological Classification**, 2015, arXiv:1510.06756. Point-vortex trajectories can be classified by braid topology, separating trajectory topology from endpoint geometry.
3. C. L. Phillips, T. Peterka, D. Karpeyev, and A. Glatz, **Detecting vortices in superconductors: Extracting one-dimensional topological singularities from a discretized complex scalar field**, 2015, arXiv:1501.03207. Vortex cores in a discretized complex order parameter can be located more precisely than the underlying mesh.
4. Bogdan Damski and Krzysztof Sacha, **Changes of the topological charge of vortices**, 2002, arXiv:quant-ph/0202137. Vortex creation or annihilation can occur when assumptions behind circulation conservation fail; charge preservation must therefore be monitored rather than assumed from a label.
5. Dave Auckly and Martin Speight, **Fermionic quantization and configuration spaces for the Skyrme and Faddeev-Hopf models**, 2004, arXiv:hep-th/0411010. Finkelstein-Rubinstein-style quantization depends on the topology of specific model configuration spaces; it cannot be inferred merely from the presence of a vortex.
6. Matthew J. Bright, Andrew I. Cooper, and Vitaliy A. Kurlin, **Continuous chiral distances for two-dimensional lattices**, 2023, DOI `10.1002/chir.23598`. Chirality can be represented by a continuous distance in a shape space, reinforcing that a static chirality magnitude is not automatically a disconnected-component invariant.

These sources constrain the toy construction only. They do not validate Lineum or establish that its vortices are physical vortices, molecules, Skyrmions, or quantum particles.

## 4. Frozen outcome separation

The test has two independent top-level outcomes.

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

The overall result passes only when both independent outcomes pass.

No failure may be repaired by changing thresholds, fixtures, seeds, grids, paths, or estimators in this version.

## 5. Frozen field renderer

The analytic complex scalar field is:

```text
phase(x) = global_phase + sum_i q_i atan2(y-y_i, x-x_i)
amplitude(x) = product_i tanh(|x-x_i| / 0.18)
psi(x) = amplitude(x) exp(i phase(x))
```

The domain and grids are:

```text
domain = [-4, 4] x [-4, 4]
grids = 64, 96, 144
seeds = 1000..1023
charges for six-core fixture = [+1, -1, +1, -1, +1, -1]
```

The renderer is observational only and exerts no force.

## 6. Frozen vortex detector and estimators

### 6.1 Plaquette winding

Every nonzero plaquette is detected by wrapped phase circulation. The integer charge is the rounded circulation divided by `2 pi`.

### 6.2 Baseline plaquette centre

The failed predecessor representation is retained as a baseline:

```text
estimated core = geometric centre of the detected plaquette
```

### 6.3 Bilinear complex-zero estimator

The four complex corner values of a detected plaquette define

```text
psi(u,v) = a + b u + c v + d u v
```

for local coordinates `u,v` in `[0,1]`. Newton iteration solves

```text
Re(psi(u,v)) = 0
Im(psi(u,v)) = 0
```

from `(0.5, 0.5)`. A result is valid only when finite and inside the plaquette up to `1e-6` numerical tolerance.

### 6.4 Independent affine zero estimator

A separate least-squares estimator fits affine planes to real and imaginary field values on the local `4 x 4` node neighbourhood surrounding the plaquette:

```text
Re(psi) = a0 + ax x + ay y
Im(psi) = b0 + bx x + by y
```

Their intersection supplies an independent core estimate. A result is valid only when finite and within one cell width of the detected plaquette.

Neither estimator receives latent vortex coordinates.

## 7. Frozen localization fixtures

For every seed and grid:

```text
single-core fixture:
    one charge selected by seed parity;
    random position in [-1.2, 1.2]^2.

pair fixture:
    charges [+1, -1];
    separation 1.35;
    random rotation and translation with magnitude below 0.35.

six-core fixture:
    fixed irregular reference constellation;
    random whole-scene rotation;
    random translation restricted to half a grid cell in each axis.
```

The irregular reference is:

```text
[ [ 1.65,  0.15],
  [ 0.72,  1.55],
  [-0.86,  0.96],
  [-1.72, -0.25],
  [-0.28, -1.50],
  [ 1.12, -0.86] ]
```

and is centred before use.

A separate translation-plus-rotation control transforms the reference by `37 degrees` and `[0.43, -0.31]`.

A global phase of `1.2345` radians is added in the phase-invariance control.

## 8. Frozen localization metrics and gates

Let `h` be the grid spacing.

```text
all fixtures:
    exact defect count and charge multiset;

baseline:
    retained for comparison only;

bilinear single-core:
    maximum localization error < 0.25 h;

bilinear pair and six-core:
    maximum localization error < 0.45 h;

affine pair and six-core:
    maximum localization error < 0.75 h;

independent estimator agreement:
    maximum matched bilinear-affine distance < 0.80 h;

improvement:
    mean bilinear error < 0.45 * mean plaquette-centre error;

translation-plus-rotation geometry:
    maximum charge-aware proper-rotation error < 0.040 on grid 64;
    maximum error < 0.025 on grids 96 and 144;

global phase:
    detected charges and both sub-grid estimates unchanged below 1e-10;

resolution trend:
    mean bilinear localization error in absolute model units decreases monotonically
    from grid 64 to 96 to 144.
```

Latent coordinates are used only for known-answer evaluation.

## 9. Frozen chirality fixture

The centred irregular six-point reference from Section 7 is assigned fixed worldline labels `0..5`, charges `[+1,-1,+1,-1,+1,-1]`, and cycle edges

```text
(0,1), (1,2), (2,3), (3,4), (4,5), (5,0).
```

The mirror operation is:

```text
M(x,y) = (-x,y).
```

Static geometry is compared modulo translation, proper rotation, and charge-preserving permutation. Reflection is not admitted by the fit.

The signed cycle area is the standard shoelace area in the fixed worldline order.

## 10. Frozen path controls

Every path has 101 uniformly sampled frames.

### 10.1 Free-point mirror path

```text
x_i(t) = (1 - 2t) x_i(0)
y_i(t) = y_i(0)
```

Because all six frozen y-coordinates are distinct, the midpoint is collinear but contains no point collision.

This path is admissible under the free-point ontology:

```text
protected condition = distinct labelled points only
```

It is inadmissible under the protected-cycle ontology:

```text
protected condition = distinct labelled points
                    + fixed cyclic worldline order
                    + nonzero signed cycle area
```

### 10.2 Same-sector protected path

The reference undergoes a smooth proper rotation, positive anisotropic scaling, and translation:

```text
angle(t) = 0.8 t
scale_x(t) = 1 + 0.10 t
scale_y(t) = 1 - 0.05 t
shift(t) = [0.25 t, -0.18 t]
```

The determinant remains positive, so signed area must retain its sign.

### 10.3 Achiral static control

A rectangle with alternating charges is compared to its mirror while allowing charge-preserving permutation:

```text
[[-1.0,-0.6], [1.0,-0.6], [1.0,0.6], [-1.0,0.6]]
charges = [+1,-1,+1,-1]
```

The mirror must be symmetry-equivalent under the static observer.

### 10.4 Teleport attack

The first 50 frames remain at the reference. Frame 51 jumps to the mirror translated by `[1.1,-0.9]`, and the remaining frames stay there.

### 10.5 Same-charge relabelling attack

The geometric path is the valid same-sector path, but labels `0` and `2`, both positive charges, are exchanged after frame 50. Geometry is unchanged while labelled worldline continuity is broken.

## 11. Frozen path metrics and gates

```text
static chiral control:
    charge-aware proper-rotation mirror error > 0.08;

achiral static control:
    mirror error < 1e-10;

free mirror path:
    endpoint equals mirror below 1e-12;
    minimum pair separation > 0.25;
    signed area changes sign;
    minimum absolute normalized signed area < 1e-12;
    maximum ordinary labelled step < 0.10;

protected-cycle classification:
    free mirror path rejected because signed area reaches zero;

same-sector protected path:
    minimum normalized signed area > 0.80;
    no point collision;
    maximum ordinary labelled step < 0.10;

teleport attack:
    maximum labelled step > 0.80;

same-charge relabelling attack:
    maximum labelled step > 0.80;

independent area implementation:
    shoelace and edge-cross-sum signed areas agree below 1e-12 in every frame;

analytic mirror relation:
    area(mirror(reference)) = -area(reference) below 1e-12.
```

The path observer is allowed to classify only the declared kinematic constraints. It must not call a prescribed path autonomous.

## 12. Interpretation rules

### 12.1 If all gates pass

```text
sub-grid complex-zero localization is validated in the analytic renderer;
static chirality and dynamic path connectivity are successfully separated;
free planar labelled points are mirror-connected in this fixture;
a protected oriented cycle creates a declared path obstruction;
teleport and relabelling remain distinct from continuous instance history.
```

This would authorize a later, separately preregistered dynamic-law fixture. It would not authorize P2 application.

### 12.2 If localization fails

Stop. Do not loosen thresholds or add a field component. Classify whether failure belongs to field detection, interpolation, multiple-core distortion, grid resolution, or independent-estimator disagreement.

### 12.3 If path controls fail

Stop. Do not add spinor or gauge structure. Classify whether the fixture was statically achiral, the free path collided, the protected invariant was ill-defined, or the continuity attack was not identified.

## 13. Prohibited interpretations

```text
no claim that Lineum vortices possess intrinsic chirality;
no claim that a mirror is or is not the same Lineum object;
no claim of spin-1/2, fermionic statistics, parity violation, WZW physics, or gauge fields;
no claim that a kinematic path is generated by the current Lineum law;
no claim that a signed-area constraint exists in Lineum;
no application to retained P2;
no Core or whitepaper change.
```

## 14. Root-programme impact before execution

| Root branch | Relation | Pre-execution status |
|---|---|---|
| retained P2 recovery | `unaffected` | Still mandatory and blocked by exact-package recovery. |
| P2 observer | `depends_on` | No application until known-answer field and path observers pass. |
| source accounting | `constrains` | Later dynamic paths must declare work and external intervention. |
| causal-path toy | `supports` | Path history remains more informative than endpoint resemblance. |
| transplant and copying | `supports` | Teleport and relabelling attacks preserve endpoint appearance while breaking instance continuity. |
| historical spinor / vector gauge | `constrains` | No new field is introduced before scalar-history alternatives are exhausted. |
| particle, life, soul, quantum, cosmology | `unaffected` | No correspondence is tested. |

## 15. Frozen executable source

```python
import itertools
import json
import math
import platform
import sys

import numpy as np

GRIDS = [64, 96, 144]
SEEDS = list(range(1000, 1024))
DOMAIN_HALF = 4.0
CORE_RADIUS = 0.18
GLOBAL_PHASE = 1.2345
CHARGES6 = np.array([1, -1, 1, -1, 1, -1], dtype=int)
REFERENCE = np.array([
    [1.65, 0.15],
    [0.72, 1.55],
    [-0.86, 0.96],
    [-1.72, -0.25],
    [-0.28, -1.50],
    [1.12, -0.86],
], dtype=float)
REFERENCE -= REFERENCE.mean(axis=0)


def wrap_phase(value):
    return (value + np.pi) % (2.0 * np.pi) - np.pi


def grid_axis(grid):
    return np.linspace(-DOMAIN_HALF, DOMAIN_HALF, grid)


def render_field(points, charges, grid, global_phase=0.0):
    axis = grid_axis(grid)
    xx, yy = np.meshgrid(axis, axis, indexing="xy")
    phase = np.full_like(xx, float(global_phase), dtype=float)
    amplitude = np.ones_like(xx, dtype=float)
    for point, charge in zip(points, charges):
        dx = xx - point[0]
        dy = yy - point[1]
        distance = np.hypot(dx, dy)
        phase += charge * np.arctan2(dy, dx)
        amplitude *= np.tanh(distance / CORE_RADIUS)
    return amplitude * np.exp(1j * phase)


def detect_plaquettes(psi):
    phase = np.angle(psi)
    p00 = phase[:-1, :-1]
    p01 = phase[:-1, 1:]
    p11 = phase[1:, 1:]
    p10 = phase[1:, :-1]
    winding = (
        wrap_phase(p01 - p00)
        + wrap_phase(p11 - p01)
        + wrap_phase(p10 - p11)
        + wrap_phase(p00 - p10)
    )
    charge = np.rint(winding / (2.0 * np.pi)).astype(int)
    rows, cols = np.where(charge != 0)
    return [(int(r), int(c), int(charge[r, c])) for r, c in zip(rows, cols)]


def plaquette_center(row, col, grid):
    axis = grid_axis(grid)
    return np.array([
        0.5 * (axis[col] + axis[col + 1]),
        0.5 * (axis[row] + axis[row + 1]),
    ])


def bilinear_zero(psi, row, col):
    p00 = psi[row, col]
    p01 = psi[row, col + 1]
    p10 = psi[row + 1, col]
    p11 = psi[row + 1, col + 1]
    a = p00
    b = p01 - p00
    c = p10 - p00
    d = p11 - p10 - p01 + p00
    uv = np.array([0.5, 0.5], dtype=float)
    for _ in range(20):
        u, v = uv
        value = a + b * u + c * v + d * u * v
        du = b + d * v
        dv = c + d * u
        jacobian = np.array([[du.real, dv.real], [du.imag, dv.imag]], dtype=float)
        residual = np.array([value.real, value.imag], dtype=float)
        try:
            step = np.linalg.solve(jacobian, residual)
        except np.linalg.LinAlgError:
            return None
        uv -= step
        if np.linalg.norm(step) < 1e-13:
            break
    if not np.all(np.isfinite(uv)) or np.any(uv < -1e-6) or np.any(uv > 1.0 + 1e-6):
        return None
    axis = grid_axis(psi.shape[0])
    u, v = np.clip(uv, 0.0, 1.0)
    return np.array([
        axis[col] + u * (axis[col + 1] - axis[col]),
        axis[row] + v * (axis[row + 1] - axis[row]),
    ])


def affine_zero(psi, row, col):
    grid = psi.shape[0]
    axis = grid_axis(grid)
    r0 = max(0, row - 1)
    r1 = min(grid, row + 3)
    c0 = max(0, col - 1)
    c1 = min(grid, col + 3)
    samples = []
    real_values = []
    imag_values = []
    for r in range(r0, r1):
        for c in range(c0, c1):
            samples.append([1.0, axis[c], axis[r]])
            real_values.append(psi[r, c].real)
            imag_values.append(psi[r, c].imag)
    design = np.asarray(samples, dtype=float)
    real_fit = np.linalg.lstsq(design, np.asarray(real_values), rcond=None)[0]
    imag_fit = np.linalg.lstsq(design, np.asarray(imag_values), rcond=None)[0]
    matrix = np.array([[real_fit[1], real_fit[2]], [imag_fit[1], imag_fit[2]]])
    rhs = -np.array([real_fit[0], imag_fit[0]])
    try:
        point = np.linalg.solve(matrix, rhs)
    except np.linalg.LinAlgError:
        return None
    if not np.all(np.isfinite(point)):
        return None
    center = plaquette_center(row, col, grid)
    h = axis[1] - axis[0]
    if np.max(np.abs(point - center)) > 1.5 * h:
        return None
    return point


def observe(points, charges, grid, global_phase=0.0):
    psi = render_field(points, charges, grid, global_phase)
    detections = detect_plaquettes(psi)
    rows = []
    for row, col, charge in detections:
        rows.append({
            "charge": charge,
            "center": plaquette_center(row, col, grid),
            "bilinear": bilinear_zero(psi, row, col),
            "affine": affine_zero(psi, row, col),
        })
    return rows


def match_error(observed, latent, latent_charges, key):
    if len(observed) != len(latent):
        return math.inf, []
    errors = []
    pairs = []
    for charge in sorted(set(latent_charges.tolist())):
        obs_indices = [i for i, item in enumerate(observed) if item["charge"] == charge]
        lat_indices = np.where(latent_charges == charge)[0].tolist()
        if len(obs_indices) != len(lat_indices):
            return math.inf, []
        best = None
        for permutation in itertools.permutations(obs_indices):
            current = []
            valid = True
            for oi, li in zip(permutation, lat_indices):
                estimate = observed[oi][key]
                if estimate is None:
                    valid = False
                    break
                current.append(float(np.linalg.norm(estimate - latent[li])))
            if valid and (best is None or max(current) < max(best[0])):
                best = (current, list(zip(permutation, lat_indices)))
        if best is None:
            return math.inf, []
        errors.extend(best[0])
        pairs.extend(best[1])
    return max(errors) if errors else 0.0, pairs


def estimator_distance(observed, key_a, key_b):
    distances = []
    for item in observed:
        if item[key_a] is None or item[key_b] is None:
            return math.inf
        distances.append(float(np.linalg.norm(item[key_a] - item[key_b])))
    return max(distances) if distances else 0.0


def proper_rotation(source, target):
    source = source - source.mean(axis=0)
    target = target - target.mean(axis=0)
    u, _, vt = np.linalg.svd(source.T @ target)
    rotation = u @ vt
    if np.linalg.det(rotation) < 0:
        u[:, -1] *= -1
        rotation = u @ vt
    return rotation


def invariant_error(source, source_charges, target, target_charges):
    if len(source) != len(target) or sorted(source_charges.tolist()) != sorted(target_charges.tolist()):
        return math.inf
    scale = np.sqrt(np.mean(np.sum((target - target.mean(axis=0)) ** 2, axis=1)))
    best = math.inf
    for permutation in itertools.permutations(range(len(source))):
        ordered_charges = source_charges[list(permutation)]
        if not np.array_equal(ordered_charges, target_charges):
            continue
        ordered = source[list(permutation)]
        rotation = proper_rotation(ordered, target)
        aligned = (ordered - ordered.mean(axis=0)) @ rotation
        residual = np.sqrt(np.mean(np.sum((aligned - (target - target.mean(axis=0))) ** 2, axis=1)))
        best = min(best, float(residual / max(scale, 1e-15)))
    return best


def extracted_points(observed, key):
    if any(item[key] is None for item in observed):
        return None, None
    points = np.array([item[key] for item in observed], dtype=float)
    charges = np.array([item["charge"] for item in observed], dtype=int)
    return points, charges


def rotate_translate(points, angle, shift):
    matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
    return points @ matrix.T + np.asarray(shift)


def signed_area(points):
    x = points[:, 0]
    y = points[:, 1]
    return 0.5 * float(np.sum(x * np.roll(y, -1) - y * np.roll(x, -1)))


def signed_area_cross(points):
    total = 0.0
    for i in range(len(points)):
        j = (i + 1) % len(points)
        total += np.cross(points[i], points[j])
    return 0.5 * float(total)


def min_pair_distance(points):
    distance = np.linalg.norm(points[:, None, :] - points[None, :, :], axis=2)
    distance += np.eye(len(points)) * 1e9
    return float(np.min(distance))


def max_labelled_step(frames, label_orders=None):
    maximum = 0.0
    for index in range(len(frames) - 1):
        left = frames[index]
        right = frames[index + 1]
        if label_orders is None:
            maximum = max(maximum, float(np.max(np.linalg.norm(right - left, axis=1))))
        else:
            left_order = label_orders[index]
            right_order = label_orders[index + 1]
            left_by_label = {label: left[pos] for pos, label in enumerate(left_order)}
            right_by_label = {label: right[pos] for pos, label in enumerate(right_order)}
            jumps = [np.linalg.norm(right_by_label[label] - left_by_label[label]) for label in left_by_label]
            maximum = max(maximum, float(max(jumps)))
    return maximum


def localization_receipt():
    records = []
    phase_differences = []
    geometry_errors = {64: [], 96: [], 144: []}
    for grid in GRIDS:
        axis = grid_axis(grid)
        h = float(axis[1] - axis[0])
        for seed in SEEDS:
            rng = np.random.default_rng(seed)
            single_charge = np.array([1 if seed % 2 == 0 else -1], dtype=int)
            single = rng.uniform(-1.2, 1.2, size=(1, 2))
            angle = rng.uniform(0.0, 2.0 * np.pi)
            shift = rng.uniform(-0.35, 0.35, size=2)
            direction = np.array([math.cos(angle), math.sin(angle)])
            pair = np.array([-0.675 * direction, 0.675 * direction]) + shift
            pair_charges = np.array([1, -1], dtype=int)
            scene_angle = rng.uniform(0.0, 2.0 * np.pi)
            subcell_shift = rng.uniform(-0.5 * h, 0.5 * h, size=2)
            six = rotate_translate(REFERENCE, scene_angle, subcell_shift)
            for name, points, charges in (
                ("single", single, single_charge),
                ("pair", pair, pair_charges),
                ("six", six, CHARGES6),
            ):
                observed = observe(points, charges, grid)
                observed_phase = observe(points, charges, grid, GLOBAL_PHASE)
                row = {"grid": grid, "h": h, "seed": seed, "fixture": name, "exact": len(observed) == len(points) and sorted(item["charge"] for item in observed) == sorted(charges.tolist())}
                for key in ("center", "bilinear", "affine"):
                    error, _ = match_error(observed, points, charges, key)
                    row[key + "_max_error"] = error
                row["bilinear_affine_max"] = estimator_distance(observed, "bilinear", "affine")
                records.append(row)
                base_b, base_c = extracted_points(observed, "bilinear")
                phase_b, phase_c = extracted_points(observed_phase, "bilinear")
                if base_b is None or phase_b is None:
                    phase_differences.append(math.inf)
                else:
                    phase_differences.append(invariant_error(base_b, base_c, phase_b, phase_c))
            moved = rotate_translate(six, math.radians(37.0), [0.43, -0.31])
            base_obs = observe(six, CHARGES6, grid)
            moved_obs = observe(moved, CHARGES6, grid)
            base_points, base_charges = extracted_points(base_obs, "bilinear")
            moved_points, moved_charges = extracted_points(moved_obs, "bilinear")
            if base_points is None or moved_points is None:
                geometry_errors[grid].append(math.inf)
            else:
                geometry_errors[grid].append(invariant_error(moved_points, moved_charges, base_points, base_charges))
    centre_errors = [row["center_max_error"] for row in records]
    bilinear_errors = [row["bilinear_max_error"] for row in records]
    mean_bilinear_by_grid = {grid: float(np.mean([row["bilinear_max_error"] for row in records if row["grid"] == grid])) for grid in GRIDS}
    gates = {
        "detections_exact": all(row["exact"] for row in records),
        "bilinear_single_lt_0_25h": all(row["bilinear_max_error"] < 0.25 * row["h"] for row in records if row["fixture"] == "single"),
        "bilinear_multi_lt_0_45h": all(row["bilinear_max_error"] < 0.45 * row["h"] for row in records if row["fixture"] in ("pair", "six")),
        "affine_multi_lt_0_75h": all(row["affine_max_error"] < 0.75 * row["h"] for row in records if row["fixture"] in ("pair", "six")),
        "independent_agreement_lt_0_80h": all(row["bilinear_affine_max"] < 0.80 * row["h"] for row in records),
        "mean_bilinear_lt_0_45_center": float(np.mean(bilinear_errors)) < 0.45 * float(np.mean(centre_errors)),
        "geometry_grid64_lt_0_040": max(geometry_errors[64]) < 0.040,
        "geometry_grid96_lt_0_025": max(geometry_errors[96]) < 0.025,
        "geometry_grid144_lt_0_025": max(geometry_errors[144]) < 0.025,
        "global_phase_invariant_lt_1e_10": max(phase_differences) < 1e-10,
        "resolution_monotone": mean_bilinear_by_grid[64] > mean_bilinear_by_grid[96] > mean_bilinear_by_grid[144],
    }
    return {
        "records": records,
        "geometry_error_max": {str(grid): max(values) for grid, values in geometry_errors.items()},
        "phase_difference_max": max(phase_differences),
        "mean_center_error": float(np.mean(centre_errors)),
        "mean_bilinear_error": float(np.mean(bilinear_errors)),
        "mean_bilinear_by_grid": {str(k): v for k, v in mean_bilinear_by_grid.items()},
        "gates": gates,
        "pass": all(gates.values()),
    }


def path_receipt():
    reference = REFERENCE.copy()
    mirror = reference.copy()
    mirror[:, 0] *= -1.0
    area0 = signed_area(reference)
    free_frames = []
    same_frames = []
    for t in np.linspace(0.0, 1.0, 101):
        free = reference.copy()
        free[:, 0] *= 1.0 - 2.0 * t
        free_frames.append(free)
        angle = 0.8 * t
        sx = 1.0 + 0.10 * t
        sy = 1.0 - 0.05 * t
        matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]) @ np.diag([sx, sy])
        same_frames.append(reference @ matrix.T + np.array([0.25 * t, -0.18 * t]))
    free_areas = np.array([signed_area(frame) for frame in free_frames])
    same_areas = np.array([signed_area(frame) for frame in same_frames])
    area_disagreement = max(abs(signed_area(frame) - signed_area_cross(frame)) for frame in free_frames + same_frames)
    free_min_sep = min(min_pair_distance(frame) for frame in free_frames)
    same_min_sep = min(min_pair_distance(frame) for frame in same_frames)
    free_step = max_labelled_step(free_frames)
    same_step = max_labelled_step(same_frames)
    rectangle = np.array([[-1.0, -0.6], [1.0, -0.6], [1.0, 0.6], [-1.0, 0.6]])
    rectangle_charges = np.array([1, -1, 1, -1], dtype=int)
    rectangle_mirror = rectangle.copy(); rectangle_mirror[:, 0] *= -1
    chiral_error = invariant_error(mirror, CHARGES6, reference, CHARGES6)
    achiral_error = invariant_error(rectangle_mirror, rectangle_charges, rectangle, rectangle_charges)
    teleport_frames = [reference.copy() for _ in range(51)] + [mirror + np.array([1.1, -0.9]) for _ in range(50)]
    teleport_jump = max_labelled_step(teleport_frames)
    relabel_orders = []
    normal_order = list(range(6))
    swapped_order = [2, 1, 0, 3, 4, 5]
    for index in range(101):
        relabel_orders.append(normal_order if index <= 50 else swapped_order)
    relabel_jump = max_labelled_step(same_frames, relabel_orders)
    normalized_free_area = np.abs(free_areas / area0)
    normalized_same_area = same_areas / area0
    gates = {
        "static_chiral_error_gt_0_08": chiral_error > 0.08,
        "achiral_error_lt_1e_10": achiral_error < 1e-10,
        "free_endpoint_exact": float(np.max(np.abs(free_frames[-1] - mirror))) < 1e-12,
        "free_min_separation_gt_0_25": free_min_sep > 0.25,
        "free_area_changes_sign": free_areas[0] * free_areas[-1] < 0,
        "free_area_hits_zero": float(np.min(normalized_free_area)) < 1e-12,
        "free_step_lt_0_10": free_step < 0.10,
        "protected_cycle_rejects_free_path": float(np.min(normalized_free_area)) < 1e-12,
        "same_sector_area_gt_0_80": float(np.min(normalized_same_area)) > 0.80,
        "same_sector_no_collision": same_min_sep > 0.25,
        "same_step_lt_0_10": same_step < 0.10,
        "teleport_jump_gt_0_80": teleport_jump > 0.80,
        "relabel_jump_gt_0_80": relabel_jump > 0.80,
        "area_implementations_agree": area_disagreement < 1e-12,
        "mirror_area_negates": abs(signed_area(mirror) + area0) < 1e-12,
    }
    return {
        "signed_area_reference": area0,
        "signed_area_mirror": signed_area(mirror),
        "static_chiral_error": chiral_error,
        "achiral_error": achiral_error,
        "free_min_separation": free_min_sep,
        "same_min_separation": same_min_sep,
        "free_min_abs_normalized_area": float(np.min(normalized_free_area)),
        "same_min_normalized_area": float(np.min(normalized_same_area)),
        "free_max_step": free_step,
        "same_max_step": same_step,
        "teleport_jump": teleport_jump,
        "relabel_jump": relabel_jump,
        "area_implementation_disagreement": area_disagreement,
        "gates": gates,
        "pass": all(gates.values()),
    }


LOCALIZATION = localization_receipt()
PATH = path_receipt()
if LOCALIZATION["pass"]:
    localization_outcome = "PASS_SUBGRID_LOCALIZATION"
elif not LOCALIZATION["gates"]["detections_exact"]:
    localization_outcome = "FAIL_FIELD_DETECTION"
elif not LOCALIZATION["gates"]["independent_agreement_lt_0_80h"]:
    localization_outcome = "FAIL_LOCALIZATION_INDEPENDENT_CHECK"
else:
    localization_outcome = "FAIL_SUBGRID_LOCALIZATION"

if PATH["pass"]:
    path_outcome = "PASS_PATH_COMPONENT_OBSERVER"
elif not PATH["gates"]["static_chiral_error_gt_0_08"] or not PATH["gates"]["achiral_error_lt_1e_10"]:
    path_outcome = "FAIL_STATIC_CHIRALITY_CONTROL"
elif not all(PATH["gates"][key] for key in ("free_endpoint_exact", "free_min_separation_gt_0_25", "free_area_changes_sign", "free_area_hits_zero", "free_step_lt_0_10")):
    path_outcome = "FAIL_FREE_PATH_CONTROL"
elif not all(PATH["gates"][key] for key in ("protected_cycle_rejects_free_path", "same_sector_area_gt_0_80", "same_sector_no_collision", "same_step_lt_0_10")):
    path_outcome = "FAIL_PROTECTED_CYCLE_CONTROL"
else:
    path_outcome = "FAIL_CONTINUITY_ATTACK_CONTROL"

RECEIPT = {
    "environment": {
        "python": sys.version,
        "numpy": np.__version__,
        "platform": platform.platform(),
    },
    "parameters": {
        "grids": GRIDS,
        "seeds": SEEDS,
        "domain_half": DOMAIN_HALF,
        "core_radius": CORE_RADIUS,
        "global_phase": GLOBAL_PHASE,
        "path_frames": 101,
    },
    "localization_outcome": localization_outcome,
    "path_outcome": path_outcome,
    "overall_pass": LOCALIZATION["pass"] and PATH["pass"],
    "localization": LOCALIZATION,
    "path": PATH,
}
print(json.dumps(RECEIPT, indent=2, sort_keys=True))
```

## 16. Reproduction

Copy Section 15 into a UTF-8 Python file and run it with Python 3 and NumPy. The script prints one complete JSON receipt. No Lineum checkout, SciPy installation, private repository, or network connection is required.

## 17. Stop condition

After the first untouched execution, update this report with the complete JSON receipt, classification, independent checks, positive results, negative results, and root-programme impact. Do not run a revised source in the same checkpoint if any frozen gate fails.
