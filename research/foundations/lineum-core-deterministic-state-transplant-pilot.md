# Deterministic State Transplant Pilot in Lineum Core

**Status:** active implementation checkpoint; isolated pilot passed; supported-environment and full causal-matrix validation pending

**Version:** 0.1.0

**Evidence cutoff:** 2026-07-30

**Scope:** A Core-only intervention testing whether a numerical Lineum trajectory can be paused, transferred into a clean recipient, and continued exactly when the live fields, complete `CoreConfig`, step index, and NumPy random-generator state are transferred together. This report does not use Lina EI, symbolic memory, Lineum Dynamics, OEA, external language models, or private data.

**Central question:** Is the currently implemented Core state plus its numerical context sufficient to continue one donor trajectory exactly after serialization and restoration, and does removing the random-generator state break that exact continuation when stochastic forcing is active?

**Current confidence:** High that the new checkpoint format round-trips the tested arrays and rejects a modified payload; medium that the full transferred package reproduces the active Core NumPy continuation because the isolated verifier recreated the current NumPy execution path; low for any claim about heredity, autonomous copying, biological analogy, identity, or sufficiency outside this one deterministic continuation test.

## 1. Answer first

The smallest completed pilot passed.

A donor was advanced for five steps, serialized, and then advanced for seven more steps in two ways:

1. the original donor continued without interruption;
2. a clean recipient loaded the donor fields, configuration, step index, and exact NumPy generator state and then continued.

The two final states were bit-for-bit identical for `psi`, `phi`, `kappa`, and `mu`.

A matched control loaded the same fields and configuration but replaced the donor random-generator state with seed `999`. Its `psi` field diverged from the uninterrupted donor, with a maximum absolute difference of approximately `0.0648056` after seven continuation steps.

The plain interpretation is similar to pausing a shuffled deck halfway through a game. Copying the board position is not enough to replay the same future draws. To continue the exact same stochastic history, the order of the remaining deck must also be copied. In the current NumPy path, the live fields are the board position and the NumPy generator state is the remaining deck order.

This establishes a software continuation fact within the tested setup. It does not establish heredity. The recipient did not reconstruct the donor from a smaller developmental recipe, maintain itself without the transferred state, or create a second copy.

## 2. Repository boundary

All implementation and evidence in this checkpoint belong only to `TomasTriska88/lineum-core`.

No file, branch, commit, state, or configuration in `TomasTriska88/osobni-pamet` was read or modified for this implementation lane. No Dynamics or OEA component is required.

The added Core files are:

- `lineum_core/state_checkpoint.py`: portable checkpoint encoding, integrity validation, NumPy generator-state capture and restoration, independent state cloning, and controlled continuation through `step_core`;
- `tests/test_state_checkpoint.py`: four regression tests for round-trip fidelity, exact continuation, random-history ablation, and tamper rejection.

## 3. Tested carrier decomposition

This pilot tests only a restricted Core-level package:

\[
P = (L, C, X, R),
\]

where:

- \(L\) is the current `step_core` NumPy update law;
- \(C\) is the complete `CoreConfig` dataclass value;
- \(X\) is the serialized numerical state containing the present `psi`, `phi`, `kappa`, and `mu` arrays;
- \(R\) is the complete legacy NumPy random-generator state returned by `numpy.random.get_state()`.

The checkpoint also records the integer step index, but the present solver does not consume that integer during an update. It is provenance, not a demonstrated causal input.

This pilot does not yet define or test a separate Core developmental baseline \(B\). It also does not include symbolic memory \(M\). Therefore it is a state-continuation test, not the full `L/B/X/M` transplantation matrix registered in the broader hereditary-carrier audit.

## 4. Checkpoint format

The format identifier is:

```text
lineum-core-state-checkpoint
```

The current format version is `1`.

Each checkpoint contains:

- the format identifier and version;
- a non-negative step index;
- every field of the supplied `CoreConfig` dataclass;
- present arrays among `psi`, `phi`, `kappa`, `mu`, and `delta`;
- for each array: exact NumPy dtype string, shape, and C-order bytes encoded as Base64;
- optionally, the NumPy generator name, key array, position, Gaussian-cache flag, and cached Gaussian value;
- a SHA-256 digest over the canonical JSON representation of every preceding item.

Canonical JSON uses sorted keys, compact separators, ASCII output, UTF-8 encoding, and rejects non-finite JSON numbers.

The integrity digest detects accidental or deliberate modifications to checkpoint metadata or content. It is not a signature and does not authenticate who created the checkpoint.

## 5. Frozen pilot inputs

### 5.1 Execution path

- backend: NumPy;
- canonical deterministic initialization: enabled;
- active Core source inspected: `lineum_core/math.py` blob SHA `bb877021810691223a0eb960a45493a2e351112a`;
- checkpoint module implementation commit: `6c3fbc90e1896c030c3b30d53c0e4ac7c66ab251`;
- regression-test commit: `0fe159e1878a6e709343580be7203f5f80b47fee`.

### 5.2 Grid and initial state

Grid size:

```text
12 x 12
```

Coordinates:

\[
x,y \in \operatorname{linspace}(-1,1,12).
\]

Envelope:

\[
e(x,y)=\exp[-4(x^2+y^2)].
\]

Phase:

\[
p(x,y)=\exp[i(1.7x-0.8y)].
\]

Initial arrays:

\[
\psi_0=0.15\,e\,p,
\]

\[
\phi_0=0.02\,e,
\]

\[
\kappa_0=0.55+0.35\,e,
\]

\[
\mu_0=0.01(1-e).
\]

Dtypes were `complex128` for `psi` and `float64` for the other arrays.

### 5.3 Configuration and timing

The pilot used the active default `CoreConfig` except:

```text
use_mu = true
noise_strength = 0.004
```

Random seed before donor warm-up:

```text
314159
```

Warm-up steps before checkpoint:

```text
5
```

Continuation steps after checkpoint:

```text
7
```

Reset-history control seed:

```text
999
```

No external input, network service, language model, wall-clock value, or private repository state was supplied.

## 6. Intervention lanes

### 6.1 Full state-and-random-history transfer

1. Initialize NumPy determinism with seed `314159`.
2. Advance the initial state by five steps.
3. Serialize `CoreConfig`, `psi`, `phi`, `kappa`, `mu`, step index `5`, and the full NumPy generator state.
4. Continue the donor for seven steps without interruption.
5. Load the checkpoint into independent recipient arrays and restore the generator state.
6. Continue the recipient for seven steps.
7. Compare every retained state array using exact `numpy.array_equal`.

### 6.2 Reset-random-history control

Repeat the full transfer, but do not restore the checkpoint generator state. Set NumPy seed to `999` immediately before the recipient continuation.

This preserves the transferred field snapshot and configuration while changing future stochastic draws.

### 6.3 Integrity control

Create a valid checkpoint, change its step index after hashing, and require the loader to reject it with an integrity-hash error.

## 7. Machine-readable pilot result

```json
{
  "backend": "numpy",
  "checkpoint_bytes": 12191,
  "checkpoint_file_sha256": "975f9137634ef1781e7afc8a269a43bf752fa19ac629b2255906f85bc7dc8361",
  "continuation_steps": 7,
  "full_transfer": {
    "final_psi_sha256": "db62daa90d4badefd40e887f25ed0257d395302c25b5f6be9f48b7529c79c6d1",
    "kappa_bitwise_equal": true,
    "max_abs_psi_difference": 0.0,
    "mu_bitwise_equal": true,
    "phi_bitwise_equal": true,
    "psi_bitwise_equal": true
  },
  "grid_size": 12,
  "numpy": "2.3.5",
  "python": "3.13.5",
  "recipient_step_index": 5,
  "reset_rng_control": {
    "final_psi_sha256": "7990b4cb3e54d6f41b19336b0f615b917c560776e0a316a9c3e0affebcd89629",
    "max_abs_psi_difference": 0.06480561760422429,
    "psi_bitwise_equal": false
  },
  "schema": "lineum-core-transplant-pilot-result-v1",
  "seed": 314159,
  "warmup_steps": 5
}
```

## 8. Regression-test receipt

Executed command:

```text
python -m pytest -q
```

Result:

```text
....                                                                     [100%]
4 passed in 0.14s
```

The four tests cover:

1. exact round-trip restoration of arrays, configuration, step index, and stable serialized hash;
2. bitwise continuation after restoring fields, configuration, and random-generator state;
3. divergence after resetting random history while leaving fields and configuration unchanged;
4. rejection of a checkpoint modified after its integrity digest was created.

## 9. Exact reproduction algorithm

The implementation is deterministic under a deterministic `step_core` NumPy path and fixed environment:

```python
ExecutionPolicy.init_core_determinism(seed=314159, device_mode="numpy")
config = CoreConfig(use_mu=True, noise_strength=0.004)

donor_at_checkpoint = run_steps(initial_state, config, 5)
checkpoint = serialize_checkpoint(
    create_checkpoint(donor_at_checkpoint, config, step_index=5)
)

uninterrupted = run_steps(donor_at_checkpoint, config, 7)
recipient_state, recipient_config, _ = load_checkpoint(checkpoint)
restored = run_steps(recipient_state, recipient_config, 7)

for key in ("psi", "phi", "kappa", "mu"):
    assert numpy.array_equal(uninterrupted[key], restored[key])
```

Reset-history control:

```python
recipient_state, recipient_config, _ = load_checkpoint(
    checkpoint,
    restore_rng=False,
)
numpy.random.seed(999)
reset_history = run_steps(recipient_state, recipient_config, 7)
assert not numpy.array_equal(uninterrupted["psi"], reset_history["psi"])
```

The complete executable checkpoint implementation and regression tests are retained in the same Git checkpoint. This report freezes all experiment-specific inputs and outputs, but it does not reproduce the entire mutable Core update law inline. Therefore this checkpoint is not yet a complete portable reference-model result under the mutable-Core snapshot rule. A future validated revision must embed or generate a frozen standalone NumPy reference model and compare it against the active library in a supported dependency environment.

## 10. What the code does

The code now provides a general and reversible way to pause and restore Core NumPy trajectories.

It does not introduce a new equation, field, force, ontology, or physical claim. It does not alter `step_core`. It packages existing numerical state and context so that later causal-disassembly experiments can transfer or omit components intentionally instead of relying on ad hoc files.

## 11. What the simulation observed

Within the isolated pilot:

- the complete tested package reproduced the seven-step continuation exactly;
- replacing only future random history broke exact continuation;
- changing checkpoint metadata after hashing was detected;
- serialization and loading did not change the tested array bytes.

## 12. Interpretation

The result supports the narrow statement:

> Under active stochastic forcing in the tested Core NumPy path, exact continuation of a particular trajectory requires preserving both the numerical field snapshot and the random-generator state, in addition to the same update law and configuration.

This is a statement about exact replay and continuation. It does not show that the random-generator state is a biological analogue, a long-term memory field, or a minimal hereditary carrier. A different question—whether a recognizable organization returns statistically without replaying the exact noise—may not require the same random state.

The result also separates two future targets:

1. **exact continuation:** reproduce the same future bytes;
2. **organizational reconstruction:** recover the same class of structure or function despite different microscopic noise.

Exact continuation is stricter but scientifically narrower. Heredity-like reconstruction may tolerate microscopic differences while preserving higher-level organization.

## 13. Limitations and validity audit

### 13.1 Dependency mismatch

The repository declares:

```text
numpy>=1.24,<2.0.0
```

The isolated execution environment supplied NumPy `2.3.5`. Network access and an authenticated local Git checkout were unavailable, so the declared dependency version could not be installed or the complete repository test suite executed locally.

The pilot therefore remains an implementation checkpoint rather than a supported-environment validation. The next revision must rerun the tests with a supported NumPy version and record CI or local full-repository results.

### 13.2 Active-Core adapter scope

The isolated verifier recreated the inspected active NumPy execution path needed by the test. It did not execute the PyTorch CPU or CUDA paths and did not reconstruct unrelated repository modules.

No conclusion is retained for cross-backend checkpoint portability. A NumPy generator state cannot reproduce PyTorch random draws.

### 13.3 One donor and one horizon

Only one deterministic initial state, one configuration, one donor seed, one reset seed, one grid size, and one continuation horizon were inspected.

The pilot estimates feasibility, not population-level reliability or causal sufficiency across regimes.

### 13.4 Exact replay is not self-maintenance

The recipient received the donor's fully developed state. It did not regrow that state from a smaller baseline, survive partial erasure, or seed another recipient.

### 13.5 Integrity is not authenticity

SHA-256 detects modification relative to the stored digest. Anyone able to replace the checkpoint can also calculate a new digest. Signed provenance is outside this pilot.

## 14. Causal impact on the broader carrier audit

| Candidate | Updated status | Evidence from this pilot | Remaining discriminator |
|---|---|---|---|
| live field state `X` | still queued for standalone sufficiency | transferred without byte loss | run with donor `X` under default versus donor context |
| random state/history `R` | supported as necessary for exact replay under active noise | reset control diverged | test organizational similarity with independent noise |
| law and configuration `L,C` | required by construction, not independently ablated | both held fixed in passing lane | alternate compatible law and parameter substitutions |
| baseline `B` | untested | no separate Core baseline defined | preregister a baseline/state split without importing Lina EI |
| self-maintaining copy | untested | no second-generation transfer | source-off persistence, partial erasure, and second recipient |

No candidate is promoted to a hereditary carrier by this pilot.

## 15. Approved next Core-only checkpoint

The next small step is to convert the pilot into a supported, frozen Core experiment without touching Lina EI:

1. run the four checkpoint tests under the declared NumPy dependency range and the complete repository test environment;
2. embed a frozen standalone NumPy reference model and append an active-Core comparison receipt;
3. define a Core-only developmental baseline separately from the live state, without renaming either as DNA;
4. preregister and run four initial lanes: blank recipient, baseline only, live state only, and baseline plus live state;
5. compare both exact bytes and higher-level organization so that failure to replay microscopic noise is not confused with failure to reconstruct a pattern.

The current scientifically accurate conclusion is:

> Lineum Core can now serialize a tested stochastic NumPy trajectory and restore exact continuation when the field state, configuration, and random-generator state are transferred together. Resetting the random history breaks exact replay. This is a prerequisite for causal transplantation experiments, not evidence that a hereditary carrier has been identified.
