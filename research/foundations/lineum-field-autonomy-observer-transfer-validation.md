# Field Autonomy Observer Transfer Validation

**Status:** validated known-answer field-readout transfer; no Lineum-Core field application executed  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-01  
**Repository:** `TomasTriska88/lineum-core`  
**Target branch:** `develop`  
**Root scientific report:** `research/foundations/lineum-continuous-source-cosmology-validation.md`  
**Recovered root version:** 0.4.14  
**Root evidence cutoff:** 2026-07-29  
**Root blob SHA:** `3fba3925553cd5596e46c02fa35d1db91523537d`  
**Mandatory continuity companion:** `research/foundations/lineum-root-programme-continuity-and-impact-ledger.md`, version 0.3.0, blob `5304874451caf32313ad0e8e3c59e53958698d79`  
**Immediate preregistration:** `research/foundations/lineum-field-autonomy-observer-transfer-gate.md`, commit `2e8d8a26129ce664010a925e720b5acaa3bf0f63`, blob `7855fa5d85797ae1aa11ee367c2bd15685018210`  
**Validated point-fixture predecessor:** `research/foundations/lineum-autonomous-cohesion-causal-path-discriminator.md` v0.4.0, blob `eea76f13fade63e3e62c32c78cc4ef437c6f665a`  
**Operational task:** ClickUp `869echn1w — Audit Gnostic, Enochic, and Dead Sea Scrolls metaphors for Lineum`  
**Current Core implementation inspected but not executed:** `lineum_core/math.py`, blob `bb877021810691223a0eb960a45493a2e351112a`  
**Scope:** Test whether a causal autonomy distinction already validated in a labeled point fixture can be recovered from continuous scalar-field readouts alone.  
**Central question:** Can symmetry-invariant field signatures distinguish internal path-mediated restoration from severed paths, removed forces, continuous global control, and matched disorder without reading point labels or a target template?  
**Current confidence:** high for the frozen synthetic transfer result and its numerical checks; zero evidence for a Lineum particle, P2 identity, physical pneuma, life, consciousness, or correspondence to nature.

## 1. Answer first

The field-readout transfer passed every frozen gate.

The observer was shown only smooth scalar density fields rendered from hidden synthetic states. It did not receive point coordinates, labels, edges, forces, case names, or the original target geometry. From those fields it correctly recovered the known causal distinction:

```text
local intact internal path:
    strong restoration;

same local system after cross-path removal:
    no restoration;

all local forces removed:
    no restoration;

global reference controller:
    strong restoration, unchanged by the graph cut, with nonzero external action;

global controller removed:
    no restoration;

radial-envelope-matched disordered cloud:
    no restoration.
```

The weakest local-intact field recovery over every seed and timestep was `0.9511216003`. The strongest local-cut recovery remained below `-0.0013886514`; values near or below zero mean that the injury did not shrink. The minimum paired local cut sensitivity was `0.9531339582` against the frozen `0.70` threshold.

The global controller restored at least `0.9949004981`, but the full and graph-cut trajectories and field scores were exactly identical. Its external action was approximately `7.66–7.69`, while local, removed, and disorder lanes recorded zero external action.

This validates only the transfer from labeled point trajectories to unlabeled continuous field observations. It does not validate a field-native Lineum object or authorize P2 classification.

## 2. Frozen protocol receipt

The protocol was committed before execution:

```text
preregistration commit = 2e8d8a26129ce664010a925e720b5acaa3bf0f63
confirmatory seeds = 700..711
integration steps = 0.01, 0.005, 0.0025
hidden cases = 7
hidden trajectories = 252
challenged and matched-twin paths = 504
primary rendered fields = 1008
primary grid = 64 x 64
refinement grid = 128 x 128
Gaussian width = 0.12
render domain = [-2.4, 2.4)^2
```

No seed, timestep, force constant, graph, challenge, field width, grid, signature, threshold, or gate changed after preregistration.

## 3. What the implementation computes

The hidden known-answer generator contains sixteen unit-mass points connected by reciprocal distance-restoring springs, or an adversarial global coordinate-wise controller. A graph cut removes every declared internal path between two equal halves. A matched challenge rigidly separates those halves while preserving center of mass and every within-half distance.

Each hidden state is converted to a normalized scalar density:

```text
rho(x) = sum_i exp(-|x-x_i|^2 / (2 sigma^2))
```

The observer uses two independent field-only summaries:

1. magnitudes of radial-windowed angular Fourier moments, which remove absolute orientation and reflection sign;
2. quantiles of the field autocorrelation, which remove translation and provide a second incomplete shape summary.

For each summary, recovery is measured relative to a matched unchallenged twin:

```text
d0 = distance between challenged and twin fields immediately after injury
df = distance between challenged and twin fields after the challenge horizon
R = 1 - df/d0
R_field = min(R_moment, R_autocorr)
```

The minimum prevents one favorable signature from rescuing the other.

## 4. Human-readable results

| `dt` | case | minimum moment recovery | minimum autocorrelation recovery | field-recovery range | external action |
|---:|---|---:|---:|---:|---:|
| 0.0100 | `L_INTact` | 0.994132239 | 0.951126792 | 0.951126792–0.970812506 | 0 |
| 0.0100 | `L_CUT` | -0.025244585 | -0.008221777 | -0.025244585–-0.001679567 | 0 |
| 0.0100 | `L_REMOVED` | approximately 0 | approximately 0 | approximately 0 | 0 |
| 0.0100 | `G_CONTINUOUS` | 0.995217832 | 0.995662729 | 0.995217832–0.995343646 | 7.662–7.693 |
| 0.0100 | `G_CUT` | 0.995217832 | 0.995662729 | 0.995217832–0.995343646 | 7.662–7.693 |
| 0.0100 | `G_REMOVED` | approximately 0 | approximately 0 | approximately 0 | 0 |
| 0.0100 | `D_SHUFFLED` | approximately 0 | approximately 0 | approximately 0 | 0 |
| 0.0050 | `L_INTact` | 0.994154844 | 0.951121600 | 0.951121600–0.970825986 | 0 |
| 0.0050 | `L_CUT` | -0.025382188 | -0.008224760 | -0.025382188–-0.001520092 | 0 |
| 0.0050 | `L_REMOVED` | approximately 0 | approximately 0 | approximately 0 | 0 |
| 0.0050 | `G_CONTINUOUS` | 0.995007234 | 0.995472143 | 0.995007234–0.995141774 | 7.659–7.690 |
| 0.0050 | `G_CUT` | 0.995007234 | 0.995472143 | 0.995007234–0.995141774 | 7.659–7.690 |
| 0.0050 | `G_REMOVED` | approximately 0 | approximately 0 | approximately 0 | 0 |
| 0.0050 | `D_SHUFFLED` | approximately 0 | approximately 0 | approximately 0 | 0 |
| 0.0025 | `L_INTact` | 0.994167583 | 0.951122274 | 0.951122274–0.970834638 | 0 |
| 0.0025 | `L_CUT` | -0.025455403 | -0.008217869 | -0.025455403–-0.001388651 | 0 |
| 0.0025 | `L_REMOVED` | approximately 0 | approximately 0 | approximately 0 | 0 |
| 0.0025 | `G_CONTINUOUS` | 0.994900498 | 0.995379387 | 0.994900498–0.995039545 | 7.658–7.689 |
| 0.0025 | `G_CUT` | 0.994900498 | 0.995379387 | 0.994900498–0.995039545 | 7.658–7.689 |
| 0.0025 | `G_REMOVED` | approximately 0 | approximately 0 | approximately 0 | 0 |
| 0.0025 | `D_SHUFFLED` | approximately 0 | approximately 0 | approximately 0 | 0 |

## 5. Independent and adversarial checks

All preregistered checks passed:

```text
minimum local cut sensitivity = 0.9531339581614626
maximum global cut difference = 0 exactly
maximum whole-scene rotation/reflection moment-score change = 2.8354e-12
maximum whole-scene rotation/reflection autocorrelation-score change = 0.0082305810
maximum 64-to-128-grid R_field change = 0.0202185207
maximum explicit-versus-vectorized renderer difference = 0
maximum direct-versus-basis moment-signature difference = 8.5265e-14
maximum point-force implementation difference = 7.4940e-15
maximum primary-grid boundary density ratio = 3.5217e-9
minimum initial moment-signature injury distance = 4.8689311180
minimum initial autocorrelation injury distance = 0.0071671061
```

The positive-family mean timestep changes were:

```text
L_INTact = 0.0000039787
G_CONTINUOUS = 0.0003102351
G_CUT = 0.0003102351
```

The global full and cut hidden trajectories were bit-for-bit identical, as required by the known-answer law. Their field metrics were also exactly identical.

The standalone script was executed in a fresh Python subprocess. The process exited with code zero and its JSON output parsed successfully. The host emitted an unrelated `artifact_tool` spreadsheet-runtime warmup traceback on standard error before script execution; no spreadsheet library is imported by the verifier, and the numerical output and exit status were unaffected. This environment warning is recorded rather than hidden.

## 6. Scientific interpretation

### What was reproducibly observed

- two field summaries independently detected restoration in the intact local system;
- both rejected the cut, force-removed, controller-removed, and disordered controls;
- the local result depended strongly on an intact hidden causal path;
- the global controller was insensitive to the path cut and used measurable external action;
- the field classifier was stable under timestep refinement, grid refinement, rotation, and reflection;
- two point-force implementations, two field renderers, and two moment implementations agreed within the frozen limits.

### Cautious interpretation

A causal autonomy observer can be transferred from labeled point data to smooth unlabeled scalar-field readouts in this known-answer synthetic domain. Field restoration alone remains insufficient: the distinction requires intervention metadata and a separate external-action ledger.

### What this does not show

```text
current Lineum fields contain a cohesive object = not shown
P2 is a particle or identity = not shown
current mu or kappa repairs structure = not shown
physical matter uses the synthetic graph mechanism = not shown
pneuma is a physical field = not shown
life, consciousness, soul, gravity, or cosmology = not shown
```

The field signatures are still incomplete identifiers. Autocorrelation can admit homometric counterexamples, and moment magnitudes can discard decision-relevant phase information. Their success here depends on the declared fixture and controls, not universal completeness.

## 7. Root-programme impact

| Root branch | Relation | Result |
|---|---|---|
| Collective-particle observer | `supports` and `constrains` | Causal and symmetry logic survives the field-readout transfer, but field restoration alone remains non-identifying. |
| P2 vortex-gas remnant | `unaffected` | No field-native causal intervention or object identity has been demonstrated. |
| Minimum-flux observer limitation | `supports` | Multiple invariant signatures plus matched disorder reject the tested smooth-readout nulls. |
| Source accounting | `supports` | Strong restoration was separated from autonomy through external action and graph-cut response. |
| `mu x kappa` repair matrix | `unaffected` | No repair role is assigned to current fields. |
| Boundary and seam programme | `constrains` | A hidden synthetic graph cut is not evidence of a physical membrane. |
| Identity and transplant programme | `supports` and `constrains` | Labels and absolute pose are unnecessary in the fixture; causal continuity and source accounting remain required. |
| Copying and heredity | `unaffected` | No turnover, copying, content transfer, or descent was tested. |
| Ancient-text structural audit | `constrains` | The pneuma analogy produced a useful observer architecture, not a new ontology. |
| Physical universe | `not_yet_compared` | No empirical correspondence follows from this transfer test. |

## 8. Current verdict and next gate

```text
field_readout_transfer = validated_in_known_answer_fixture
all_frozen_gates = passed
field_restoration_alone = insufficient
causal_path_dependence = recovered_from_unlabeled_fields
external_global_control = distinguished_with_ledger_and_cut_invariance
current_Core_execution = not_performed
P2_application = still_prohibited
production_code_change = none
whitepaper_change = none
next_action = preregister a field-native synthetic local-interaction fixture
```

The next experiment must remove the hidden point graph entirely. It should use a continuous field law with explicitly local transport or coupling, a field-native causal cut, a matched global-controller adversary, source removal, and the same symmetry and disorder controls. Only after that field-native fixture passes may a separate P2 applicability audit be considered.

## 9. Reproduction receipt

```text
standalone verifier SHA-256 = 0ac60397a6d1b24be84af838cf146425ae00f6b7de17c027cf796050a5547a20
compact machine receipt SHA-256 = 01d8ca96a76684af955e140271c4c1052958fdd635573448fd523ae12a56bf6b
full standalone JSON SHA-256 = 35e24fced6258e331ca48686845d901c717c19325e7278504b42a17f130688cf
```

Requirements:

```text
Python 3.13-compatible interpreter
NumPy
no Lineum package import
no network access
```

Run:

```bash
python field_autonomy_observer_transfer_gate.py
```

## 10. Compact machine-readable output

```json
{
  "all_gates_passed": true,
  "challenged_and_twin_path_count": 504,
  "environment": {
    "numpy": "2.3.5",
    "platform": "Linux-6.12.13-x86_64-with-glibc2.41",
    "python": "3.13.5 (main, May  5 2026, 21:05:52) [GCC 14.2.0]"
  },
  "gates": {
    "D_SHUFFLED_R_field_all_lt_0_15": true,
    "G_CONTINUOUS_R_autocorr_all_gt_0_95": true,
    "G_CONTINUOUS_R_moment_all_gt_0_95": true,
    "G_CONTINUOUS_external_action_all_gt_0_01": true,
    "G_CUT_R_autocorr_all_gt_0_95": true,
    "G_CUT_R_moment_all_gt_0_95": true,
    "G_CUT_external_action_all_gt_0_01": true,
    "G_REMOVED_R_field_all_lt_0_15": true,
    "L_CUT_R_field_all_lt_0_15": true,
    "L_INTact_R_autocorr_all_gt_0_85": true,
    "L_INTact_R_moment_all_gt_0_85": true,
    "L_INTact_external_action_all_lt_1e_10": true,
    "L_REMOVED_R_field_all_lt_0_15": true,
    "all_boundary_ratios_lt_1e_8": true,
    "all_fields_mass_error_lt_1e_12": true,
    "all_initial_injuries_resolved": true,
    "global_field_metrics_exact_all": true,
    "global_hidden_bit_identical_all": true,
    "global_cut_invariance_all_lt_0_02": true,
    "local_cut_sensitivity_all_gt_0_70": true,
    "moment_implementations_lt_1e_12": true,
    "point_force_implementations_lt_1e_12": true,
    "positive_mean_timestep_change_lt_0_03": true,
    "renderer_agreement_lt_1e_13": true,
    "resolution_changes_lt_0_05": true,
    "rotation_reflection_changes_lt_0_03": true
  },
  "global_cut_difference_max": 0.0,
  "hidden_trajectory_count": 252,
  "initial_autocorr_distance_min": 0.007167106134140677,
  "initial_moment_distance_min": 4.8689311180087325,
  "local_cut_sensitivity_min": 0.9531339581614626,
  "moment_method_max_difference": 8.526512829121202e-14,
  "point_force_max_difference": 7.494005416219807e-15,
  "positive_timestep_changes": {
    "G_CONTINUOUS": 0.00031023512652905705,
    "G_CUT": 0.00031023512652905705,
    "L_INTact": 3.978724258946187e-06
  },
  "primary_boundary_ratio_max": 3.5216528937272618e-09,
  "primary_rendered_field_count": 1008,
  "refinement_boundary_ratio_max": 2.531831788686433e-19,
  "renderer_max_difference": 0.0,
  "resolution_max_difference": 0.0202185207390283,
  "symmetry_max_autocorr_difference": 0.008230581013880633,
  "symmetry_max_moment_difference": 2.8353985825901873e-12
}
```

## 11. Complete executable verifier

```python
import json
import math
import platform
import sys
import numpy as np

N = 16
SEEDS = list(range(700, 712))
DTS = [0.01, 0.005, 0.0025]
T_FORM = 4.0
T_TEST = 6.0
BULK = np.array([0.30, -0.15], dtype=float)
DELTA = np.array([0.35, 0.12], dtype=float)
K = 4.0
GAMMA = 2.0
SIGMA = 0.12
CASES = ["L_INTact", "L_CUT", "L_REMOVED", "G_CONTINUOUS", "G_CUT", "G_REMOVED", "D_SHUFFLED"]

theta = np.linspace(0.0, 2.0 * np.pi, N, endpoint=False)
radius = 1.0 + 0.12 * np.cos(3.0 * theta) + 0.05 * np.sin(5.0 * theta)
REFERENCE = np.column_stack((radius * np.cos(theta), radius * np.sin(theta)))
REFERENCE -= REFERENCE.mean(axis=0)

edge_set = set()
for i in range(N):
    for offset in (1, 2, 5):
        edge_set.add(tuple(sorted((i, (i + offset) % N))))
FULL_EDGES = sorted(edge_set)
CROSS_EDGES = [e for e in FULL_EDGES if (e[0] < 8) != (e[1] < 8)]
CUT_EDGES = [e for e in FULL_EDGES if e not in CROSS_EDGES]


def make_graph(edges):
    B = np.zeros((len(edges), N), dtype=float)
    for row, (i, j) in enumerate(edges):
        B[row, i] = -1.0
        B[row, j] = 1.0
    return B, np.linalg.norm(B @ REFERENCE, axis=1)


FULL_B, FULL_REST = make_graph(FULL_EDGES)
CUT_B, CUT_REST = make_graph(CUT_EDGES)


def local_force_vectorized(x, v, B, rest):
    d = B @ x
    dist = np.linalg.norm(d, axis=1)
    units = np.divide(d, dist[:, None], out=np.zeros_like(d), where=dist[:, None] > 1e-15)
    edge_forces = K * (dist - rest)[:, None] * units
    return -(B.T @ edge_forces) - GAMMA * (v - v.mean(axis=0))


def local_force_loop(x, v, edges, rest):
    force = np.zeros_like(x)
    for (i, j), rest_length in zip(edges, rest):
        d = x[j] - x[i]
        dist = float(np.linalg.norm(d))
        if dist > 1e-15:
            pair_force = K * (dist - rest_length) * d / dist
            force[i] += pair_force
            force[j] -= pair_force
    return force - GAMMA * (v - v.mean(axis=0))


def global_force(x, v):
    return -K * ((x - x.mean(axis=0)) - REFERENCE) - GAMMA * (v - v.mean(axis=0))


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


FORMATION = {}
for dt in DTS:
    for seed in SEEDS:
        FORMATION[(dt, seed, "local")] = form_state(seed, dt, "local")
        FORMATION[(dt, seed, "global")] = form_state(seed, dt, "global")


def shuffled_cloud(pre, seed):
    centered = pre - pre.mean(axis=0)
    radii = np.linalg.norm(centered, axis=1)
    rng = np.random.default_rng(170000 + seed)
    angles = rng.uniform(0.0, 2.0 * np.pi, size=N)
    x = np.column_stack((radii * np.cos(angles), radii * np.sin(angles)))
    return x - x.mean(axis=0)


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
    if case == "D_SHUFFLED":
        return "local", "zero", None, None, None
    raise ValueError(case)


def run_hidden(case, seed, dt, use_loop=False):
    formation_mode, challenge_mode, B, rest, edges = case_spec(case)
    pre = FORMATION[(dt, seed, formation_mode)].copy()
    if case == "D_SHUFFLED":
        pre = shuffled_cloud(pre, seed)
    twin0 = pre.copy()
    chall0 = pre.copy()
    chall0[:8] -= DELTA / 2.0
    chall0[8:] += DELTA / 2.0
    twin_x = twin0.copy()
    chall_x = chall0.copy()
    twin_v = np.tile(BULK, (N, 1))
    chall_v = np.tile(BULK, (N, 1))
    external_action = 0.0
    for _ in range(int(round(T_TEST / dt))):
        if challenge_mode == "local":
            if use_loop:
                chall_force = local_force_loop(chall_x, chall_v, edges, rest)
                twin_force = local_force_loop(twin_x, twin_v, edges, rest)
            else:
                chall_force = local_force_vectorized(chall_x, chall_v, B, rest)
                twin_force = local_force_vectorized(twin_x, twin_v, B, rest)
            external_force = np.zeros_like(chall_force)
        elif challenge_mode == "global":
            chall_force = global_force(chall_x, chall_v)
            twin_force = global_force(twin_x, twin_v)
            external_force = chall_force
        else:
            chall_force = np.zeros_like(chall_x)
            twin_force = np.zeros_like(twin_x)
            external_force = chall_force
        external_action += dt * np.sum(np.linalg.norm(external_force, axis=1))
        chall_v += dt * chall_force
        chall_x += dt * chall_v
        twin_v += dt * twin_force
        twin_x += dt * twin_v
    return {
        "case": case,
        "seed": seed,
        "dt": dt,
        "A_ext": float(external_action),
        "chall0": chall0,
        "twin0": twin0,
        "challf": chall_x,
        "twinf": twin_x,
        "challv": chall_v,
        "twinv": twin_v,
    }


ROWS = [run_hidden(case, seed, dt) for dt in DTS for seed in SEEDS for case in CASES]


def grid_cache(n):
    half = 2.4
    dx = 2.0 * half / n
    coords = np.linspace(-half, half, n, endpoint=False) + dx / 2.0
    X, Y = np.meshgrid(coords, coords, indexing="xy")
    R = np.sqrt(X * X + Y * Y)
    TH = np.arctan2(Y, X)
    centers = np.linspace(0.10, 1.65, 8)
    width = 0.18
    windows = np.exp(-0.5 * ((R[None, :, :] - centers[:, None, None]) / width) ** 2)
    modes = np.arange(9)
    basis = windows[:, None, :, :] * np.exp(-1j * modes[None, :, None, None] * TH[None, None, :, :])
    return {"X": X, "Y": Y, "R": R, "TH": TH, "basis": basis}


GRIDS = {64: grid_cache(64), 128: grid_cache(128)}


def render_vectorized(pos, n):
    X = GRIDS[n]["X"]
    Y = GRIDS[n]["Y"]
    p = pos - pos.mean(axis=0)
    dx = X[None, :, :] - p[:, 0, None, None]
    dy = Y[None, :, :] - p[:, 1, None, None]
    rho = np.exp(-(dx * dx + dy * dy) / (2.0 * SIGMA ** 2)).sum(axis=0)
    rho /= rho.sum()
    boundary = np.zeros_like(rho, dtype=bool)
    boundary[:4, :] = True
    boundary[-4:, :] = True
    boundary[:, :4] = True
    boundary[:, -4:] = True
    return rho, float(rho[boundary].max() / rho.max())


def render_loop(pos, n):
    X = GRIDS[n]["X"]
    Y = GRIDS[n]["Y"]
    p = pos - pos.mean(axis=0)
    rho = np.zeros((n, n), dtype=float)
    for xy in p:
        rho += np.exp(-((X - xy[0]) ** 2 + (Y - xy[1]) ** 2) / (2.0 * SIGMA ** 2))
    return rho / rho.sum()


def moment_signature(rho, n):
    moments = np.einsum("ij,bmij->bm", rho, GRIDS[n]["basis"], optimize=True)
    signature = np.abs(moments) / (abs(moments[0, 0]) + 1e-15)
    return signature.ravel().astype(float)


def moment_signature_direct(rho, n):
    R = GRIDS[n]["R"]
    TH = GRIDS[n]["TH"]
    values = []
    for center in np.linspace(0.10, 1.65, 8):
        window = np.exp(-0.5 * ((R - center) / 0.18) ** 2)
        for mode in range(9):
            values.append(abs(np.sum(rho * window * np.exp(-1j * mode * TH))))
    values = np.asarray(values)
    return values / (values[0] + 1e-15)


def autocorrelation_signature(rho):
    corr = np.fft.ifft2(np.abs(np.fft.fft2(rho)) ** 2).real
    corr /= corr.max()
    return np.quantile(corr.ravel(), np.linspace(0.0, 1.0, 128))


def field_features(pos, n):
    rho, boundary_ratio = render_vectorized(pos, n)
    return rho, moment_signature(rho, n), autocorrelation_signature(rho), boundary_ratio


def restoration(row, n):
    features = {}
    max_boundary = 0.0
    max_mass_error = 0.0
    for key in ("chall0", "twin0", "challf", "twinf"):
        rho, moment, autocorr, boundary = field_features(row[key], n)
        features[key] = (moment, autocorr)
        max_boundary = max(max_boundary, boundary)
        max_mass_error = max(max_mass_error, abs(float(rho.sum()) - 1.0))
    mc0, ac0 = features["chall0"]
    mt0, at0 = features["twin0"]
    mcf, acf = features["challf"]
    mtf, atf = features["twinf"]
    d0_moment = float(np.sqrt(np.mean((mc0 - mt0) ** 2)))
    df_moment = float(np.sqrt(np.mean((mcf - mtf) ** 2)))
    d0_autocorr = float(np.sqrt(np.mean((ac0 - at0) ** 2)))
    df_autocorr = float(np.sqrt(np.mean((acf - atf) ** 2)))
    R_moment = 1.0 - df_moment / d0_moment
    R_autocorr = 1.0 - df_autocorr / d0_autocorr
    return {
        "R_moment": float(R_moment),
        "R_autocorr": float(R_autocorr),
        "R_field": float(min(R_moment, R_autocorr)),
        "d0_moment": d0_moment,
        "d0_autocorr": d0_autocorr,
        "boundary_ratio": max_boundary,
        "mass_error": max_mass_error,
    }


PRIMARY = []
for row in ROWS:
    result = restoration(row, 64)
    PRIMARY.append({**{k: row[k] for k in ("case", "seed", "dt", "A_ext")}, **result})


def select_primary(case, seed, dt):
    return next(r for r in PRIMARY if r["case"] == case and r["seed"] == seed and r["dt"] == dt)


summary = {}
for dt in DTS:
    summary[str(dt)] = {}
    for case in CASES:
        selected = [r for r in PRIMARY if r["case"] == case and r["dt"] == dt]
        summary[str(dt)][case] = {
            "R_moment_min": float(np.min([r["R_moment"] for r in selected])),
            "R_moment_mean": float(np.mean([r["R_moment"] for r in selected])),
            "R_autocorr_min": float(np.min([r["R_autocorr"] for r in selected])),
            "R_autocorr_mean": float(np.mean([r["R_autocorr"] for r in selected])),
            "R_field_min": float(np.min([r["R_field"] for r in selected])),
            "R_field_max": float(np.max([r["R_field"] for r in selected])),
            "R_field_mean": float(np.mean([r["R_field"] for r in selected])),
            "A_ext_min": float(np.min([r["A_ext"] for r in selected])),
            "A_ext_max": float(np.max([r["A_ext"] for r in selected])),
        }


angle = math.radians(37.0)
ROTATION = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
REFLECTION = np.array([[-1.0, 0.0], [0.0, 1.0]])


def transformed_row(row, matrix):
    output = {k: row[k] for k in ("case", "seed", "dt", "A_ext")}
    for key in ("chall0", "twin0", "challf", "twinf"):
        output[key] = row[key] @ matrix.T
    return output


symmetry_differences = []
for row in ROWS:
    if row["case"] == "L_INTact" and row["dt"] == 0.005:
        base = select_primary("L_INTact", row["seed"], 0.005)
        for name, matrix in (("rotation", ROTATION), ("reflection", REFLECTION)):
            transformed = restoration(transformed_row(row, matrix), 64)
            symmetry_differences.append({
                "seed": row["seed"],
                "transform": name,
                "R_moment_difference": abs(transformed["R_moment"] - base["R_moment"]),
                "R_autocorr_difference": abs(transformed["R_autocorr"] - base["R_autocorr"]),
                "R_field_difference": abs(transformed["R_field"] - base["R_field"]),
            })


resolution = []
for row in ROWS:
    if row["seed"] == 700 and row["case"] != "D_SHUFFLED":
        low = select_primary(row["case"], 700, row["dt"])
        high = restoration(row, 128)
        resolution.append({
            "case": row["case"],
            "dt": row["dt"],
            "R_field_64": low["R_field"],
            "R_field_128": high["R_field"],
            "difference": abs(low["R_field"] - high["R_field"]),
            "boundary_128": high["boundary_ratio"],
            "mass_error_128": high["mass_error"],
        })


renderer_differences = []
for case in ("L_INTact", "L_CUT", "L_REMOVED", "G_CONTINUOUS", "G_CUT", "G_REMOVED"):
    row = next(r for r in ROWS if r["case"] == case and r["seed"] == 700 and r["dt"] == 0.005)
    for key in ("chall0", "twin0", "challf", "twinf"):
        vectorized, _ = render_vectorized(row[key], 64)
        explicit = render_loop(row[key], 64)
        renderer_differences.append(float(np.max(np.abs(vectorized - explicit))))


sample = next(r for r in ROWS if r["case"] == "L_INTact" and r["seed"] == 700 and r["dt"] == 0.005)
moment_differences = []
for grid in (64, 128):
    rho, _ = render_vectorized(sample["chall0"], grid)
    moment_differences.append(float(np.max(np.abs(moment_signature(rho, grid) - moment_signature_direct(rho, grid)))))


force_differences = []
for dt in DTS:
    for case in ("L_INTact", "L_CUT"):
        vectorized = next(r for r in ROWS if r["case"] == case and r["seed"] == 700 and r["dt"] == dt)
        explicit = run_hidden(case, 700, dt, use_loop=True)
        force_differences.append(float(max(
            np.max(np.abs(vectorized["challf"] - explicit["challf"])),
            np.max(np.abs(vectorized["twinf"] - explicit["twinf"])),
            np.max(np.abs(vectorized["challv"] - explicit["challv"])),
            np.max(np.abs(vectorized["twinv"] - explicit["twinv"])),
        )))


local_cut_differences = []
global_cut_differences = []
global_hidden_exact = []
global_field_exact = []
for dt in DTS:
    for seed in SEEDS:
        local_full = select_primary("L_INTact", seed, dt)
        local_cut = select_primary("L_CUT", seed, dt)
        global_full = select_primary("G_CONTINUOUS", seed, dt)
        global_cut = select_primary("G_CUT", seed, dt)
        local_cut_differences.append(local_full["R_field"] - local_cut["R_field"])
        global_cut_differences.append(abs(global_full["R_field"] - global_cut["R_field"]))
        hidden_full = next(r for r in ROWS if r["case"] == "G_CONTINUOUS" and r["seed"] == seed and r["dt"] == dt)
        hidden_cut = next(r for r in ROWS if r["case"] == "G_CUT" and r["seed"] == seed and r["dt"] == dt)
        global_hidden_exact.append(all(np.array_equal(hidden_full[k], hidden_cut[k]) for k in ("chall0", "twin0", "challf", "twinf", "challv", "twinv")))
        global_field_exact.append(all(global_full[k] == global_cut[k] for k in ("R_moment", "R_autocorr", "R_field", "d0_moment", "d0_autocorr")))


positive_timestep_changes = {}
for case in ("L_INTact", "G_CONTINUOUS", "G_CUT"):
    coarse = np.mean([r["R_field"] for r in PRIMARY if r["case"] == case and r["dt"] == 0.01])
    fine = np.mean([r["R_field"] for r in PRIMARY if r["case"] == case and r["dt"] == 0.0025])
    positive_timestep_changes[case] = float(abs(coarse - fine))


gates = {
    "L_INTact_R_moment_all_gt_0_85": all(r["R_moment"] > 0.85 for r in PRIMARY if r["case"] == "L_INTact"),
    "L_INTact_R_autocorr_all_gt_0_85": all(r["R_autocorr"] > 0.85 for r in PRIMARY if r["case"] == "L_INTact"),
    "L_INTact_external_action_all_lt_1e_10": all(r["A_ext"] < 1e-10 for r in PRIMARY if r["case"] == "L_INTact"),
    "L_CUT_R_field_all_lt_0_15": all(r["R_field"] < 0.15 for r in PRIMARY if r["case"] == "L_CUT"),
    "L_REMOVED_R_field_all_lt_0_15": all(r["R_field"] < 0.15 for r in PRIMARY if r["case"] == "L_REMOVED"),
    "G_CONTINUOUS_R_moment_all_gt_0_95": all(r["R_moment"] > 0.95 for r in PRIMARY if r["case"] == "G_CONTINUOUS"),
    "G_CONTINUOUS_R_autocorr_all_gt_0_95": all(r["R_autocorr"] > 0.95 for r in PRIMARY if r["case"] == "G_CONTINUOUS"),
    "G_CONTINUOUS_external_action_all_gt_0_01": all(r["A_ext"] > 0.01 for r in PRIMARY if r["case"] == "G_CONTINUOUS"),
    "G_CUT_R_moment_all_gt_0_95": all(r["R_moment"] > 0.95 for r in PRIMARY if r["case"] == "G_CUT"),
    "G_CUT_R_autocorr_all_gt_0_95": all(r["R_autocorr"] > 0.95 for r in PRIMARY if r["case"] == "G_CUT"),
    "G_CUT_external_action_all_gt_0_01": all(r["A_ext"] > 0.01 for r in PRIMARY if r["case"] == "G_CUT"),
    "G_REMOVED_R_field_all_lt_0_15": all(r["R_field"] < 0.15 for r in PRIMARY if r["case"] == "G_REMOVED"),
    "D_SHUFFLED_R_field_all_lt_0_15": all(r["R_field"] < 0.15 for r in PRIMARY if r["case"] == "D_SHUFFLED"),
    "local_cut_sensitivity_all_gt_0_70": all(value > 0.70 for value in local_cut_differences),
    "global_cut_invariance_all_lt_0_02": all(value < 0.02 for value in global_cut_differences),
    "all_fields_mass_error_lt_1e_12": all(r["mass_error"] < 1e-12 for r in PRIMARY) and all(r["mass_error_128"] < 1e-12 for r in resolution),
    "all_boundary_ratios_lt_1e_8": all(r["boundary_ratio"] < 1e-8 for r in PRIMARY) and all(r["boundary_128"] < 1e-8 for r in resolution),
    "all_initial_injuries_resolved": all(r["d0_moment"] >= 1e-8 and r["d0_autocorr"] >= 1e-8 for r in PRIMARY),
    "renderer_agreement_lt_1e_13": max(renderer_differences) < 1e-13,
    "moment_implementations_lt_1e_12": max(moment_differences) < 1e-12,
    "rotation_reflection_changes_lt_0_03": max(max(r["R_moment_difference"], r["R_autocorr_difference"]) for r in symmetry_differences) < 0.03,
    "resolution_changes_lt_0_05": max(r["difference"] for r in resolution) < 0.05,
    "positive_mean_timestep_change_lt_0_03": max(positive_timestep_changes.values()) < 0.03,
    "point_force_implementations_lt_1e_12": max(force_differences) < 1e-12,
    "global_hidden_bit_identical_all": all(global_hidden_exact),
    "global_field_metrics_exact_all": all(global_field_exact),
}


receipt = {
    "environment": {
        "python": sys.version,
        "numpy": np.__version__,
        "platform": platform.platform(),
    },
    "hidden_trajectory_count": len(ROWS),
    "challenged_and_twin_path_count": 2 * len(ROWS),
    "primary_rendered_field_count": 4 * len(ROWS),
    "summary": summary,
    "gates": gates,
    "all_gates_passed": all(gates.values()),
    "local_cut_sensitivity_min": float(np.min(local_cut_differences)),
    "global_cut_difference_max": float(np.max(global_cut_differences)),
    "positive_timestep_changes": positive_timestep_changes,
    "symmetry_max_moment_difference": float(max(r["R_moment_difference"] for r in symmetry_differences)),
    "symmetry_max_autocorr_difference": float(max(r["R_autocorr_difference"] for r in symmetry_differences)),
    "resolution_max_difference": float(max(r["difference"] for r in resolution)),
    "renderer_max_difference": float(max(renderer_differences)),
    "moment_method_max_difference": float(max(moment_differences)),
    "point_force_max_difference": float(max(force_differences)),
    "primary_boundary_ratio_max": float(max(r["boundary_ratio"] for r in PRIMARY)),
    "refinement_boundary_ratio_max": float(max(r["boundary_128"] for r in resolution)),
    "initial_moment_distance_min": float(min(r["d0_moment"] for r in PRIMARY)),
    "initial_autocorr_distance_min": float(min(r["d0_autorr"] for r in PRIMARY)) if False else float(min(r["d0_autocorr"] for r in PRIMARY)),
}

print(json.dumps(receipt, indent=2, sort_keys=True))
```
