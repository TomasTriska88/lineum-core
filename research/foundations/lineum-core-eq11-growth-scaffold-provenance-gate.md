# Eq-11.1 Growth and Scaffold Provenance Gate

**Status:** active provenance report; cited source commit and active root runner do not provide an executable Eq-11.1 receipt; no numerical repair experiment authorized

**Version:** 0.4.0  
**Evidence cutoff:** 2026-07-30

**Parent programme:** `research/foundations/lineum-core-active-growth-scaffold-repair-matrix.md`

## 1. Answer first

Eq-11.1 remains the highest-priority distinct “active growth” candidate for the owner’s yeast-plus-mould hypothesis because an explicit growth/leakage equation survives in the repository. It is **not yet reproducible enough to run a repair experiment**.

Neither the repository commit cited near the historical survivor claim nor the active root `lineum.py` presently supplies the claimed Eq-11.1 mechanism as a complete executable reproduction chain. The immediate task remains provenance reconstruction, not parameter tuning and not code promotion.

## 2. Gate question

Can one complete, internally consistent Eq-11.1 implementation and undamaged baseline be reconstructed from versioned repository evidence without relying on missing scripts, retrospective prose, or selectively chosen claims?

A repair experiment is allowed only after that answer is yes.

## 3. Surviving explicit equation

The current equation-history whitepaper records:

```text
∂t Psi = D_Psi ∇²Psi + [alpha tanh(c1 Phi) - gamma - lambda Phi² - c_w |∇Psi|²] Psi
∂t Phi = D_Phi ∇²Phi + c2 |Psi|² - gamma_Phi Phi
```

This is a candidate/historical research law, not the active public `lineum_core.math.step_core` implementation.

## 4. Known negative and contradictory history

The same whitepaper records all of the following and they must remain visible:

- the original script and exact parameters behind the historical isolated-survivor claim were omitted from version control;
- a reconstructed topological node decayed from approximately `1.99` to a scalar puddle near `0.54` over the reported horizon;
- a local reference neighbourhood used `alpha=0.5`, `gamma=0.05`, `c_w=0.5`, `c2=1.0`, and `D_r=0.05`, but yielded no autonomous isolated survival in its single-parameter sweep;
- lowering `lambda` to `0.01` produced apparent short-horizon persistence followed by delayed far-field boiling and loss of the original topology;
- the reported `lambda ∈ {0.03,0.05,0.07}` and `alpha ∈ {0.8,1.0}` frontier contained no cell that both preserved the core and kept the vacuum quiet;
- source-normalized multi-body geometries did not rescue the open limit;
- a weak smooth external Gaussian `kappa` well up to the reported `0.05` strength did not contain the exhaust.

These are repository claims requiring reproduction, not independently verified facts.

## 5. Commit archaeology checkpoint

The whitepaper points to short commit `4b08ab1`. GitHub resolves it to:

```text
4b08ab1ebac1beb287c5ecd7f74803e530e7e7ad
```

Commit message:

```text
docs: Formalize Eq-11.1 syntax and add Near-Threshold Coupling Corridor limits
```

### 5.1 Evidence actually recovered from the commit

The changed-file evidence is documentation- and search-heavy. It includes repository prose plus auxiliary files such as:

- `found.txt` and `found2.txt` — extracted prose lines about earlier Eq-4/Eq-8 claims and todo material, not executable Eq-11.1 code;
- `search_out.txt` and other search files — Windows filesystem search listings, including many local `.scratch` paths;
- `phase_mismatch_results.txt` — six summary values (`Survivors: 52`, `Decays: 44`, two mismatch summaries, effect size `0.142`) without equation, parameters, initializer, command, seed, or state artifact;
- an adjacent Eq-9 escape-fold test and unrelated documentation/portal changes.

`search_out.txt` contains no `eq11` match in the retrieved content. It is a path inventory rather than source code or a numerical receipt.

No Eq-11.1 survivor/reproduction solver has been identified in the commit’s recovered changed-file evidence.

### 5.2 Exact-path checks

Direct fetches at the cited commit returned `404 Not Found` for:

- `eval_closed_system_stress.py`;
- `scripts/eval_closed_system_stress.py`.

These results are classified as `not_located_at_tested_paths`, not proof that no relevant code exists anywhere in the commit or ancestry.

### 5.3 Current classification of `4b08ab1`

| Property | Classification |
|---|---|
| equation prose | `historical_documentation_evidence` |
| exact survivor executable | `not_located` |
| complete parameter set | `not_recovered` |
| initializer | `not_recovered` |
| integration convention | `not_recovered` |
| numerical output provenance | `insufficient`; summary text exists without runnable chain |
| use as validation receipt | `prohibited` |

The commit may establish when wording was introduced. It does not currently establish that the claimed Eq-11.1 survivor was reproducibly executed.

### 5.4 Active root-runner check

Current `lineum.py` on `develop`, blob `a57171a633b85d02e4c2047d367cab5b534181aa`, imports:

```python
from lineum_core.math import step_core, CoreConfig
```

Its active simulation loop constructs a standard `CoreConfig` from noise, drift, dissipation, diffusion, reaction, and mode-coupling settings, then calls:

```python
state = step_core({"psi": psi, "phi": phi, "kappa": kappa, "delta": delta}, cfg)
```

It does not execute the explicit Eq-11.1 `alpha tanh(c1 Phi) - gamma - lambda Phi² - c_w |∇Psi|²` law in that loop.

A stale code-search hit for `c_w` in `lineum.py` therefore does not establish that the current root runner is Eq-11.1. Classification: `active_harness_for_public_step_core`, not an Eq-11.1 reproduction implementation.

## 6. Required provenance matrix

For every discovered Eq-11 or Eq-11.1 artifact, record:

| Field | Required value |
|---|---|
| path / commit | exact immutable location |
| equation variant | Eq-11, Eq-11.1, later modification, or sandbox reduction |
| status | canonical, candidate, historical, experimental, deprecated, contradicted, or unreproducible |
| integration | spatial stencil/spectral operator, `dx`, `dt`, boundary conditions, update order |
| parameters | every coefficient and initial field value |
| initializer | exact amplitude, phase winding, centering, grid and domain |
| observer | survival, topology, far-field quietness and failure thresholds |
| evidence | script, test, output artifact, prose only, or missing |
| known failure | decay, boiling, fragmentation, numerical reset, boundary artefact, or unknown |

## 7. Hard preregistered gate

No Eq-11.1 numerical repair run may begin until:

1. all recoverable implementations and parameter sets are symmetrically inventoried;
2. at least one candidate has a fully specified executable law and initializer;
3. its undamaged control is reproduced independently;
4. a topological observer distinguishes a surviving vortex from a filled scalar puddle;
5. a far-field observer rejects vacuum boiling;
6. grid, timestep, boundary, and precision checks are declared before results;
7. the candidate passes its baseline without post-hoc parameter rescue.

If no candidate passes, the provenance lane ends with `no_reproducible_eq11_baseline_found`; Eq-11.1 is not tested for repair and the programme moves to the next mechanism family.

## 8. Prohibited interpretations

This provenance work cannot establish particles, biology, heredity, consciousness, cosmology, or correspondence with nature. A successful baseline would establish only that one documented numerical mechanism can maintain one operationally defined structure under frozen simulation conditions.

## 9. Operational tracking boundary

The durable scientific source of truth is this version-controlled report. It records equations, evidence, negative results, uncertainty, and the scientific decision trail.

Operational status, priority, assignment, and completion are tracked in the Lineum Dynamics ClickUp workspace, task:

```text
869ebyvpb — Research: Active Growth and Scaffold Repair (Eq-11.1 Provenance Gate)
```

Repository `todo.md` files are historical evidence only. They may help reconstruct old ideas or experiment history, but they do not define current priority, status, or planned work.

## 10. Next provenance actions

Before any implementation:

1. identify commits that introduced and later modified Eq-11 and Eq-11.1 wording;
2. inspect their complete changed-file lists for versioned scripts, tests, outputs, or parameter manifests;
3. recover any referenced `.scratch` filenames from committed search artifacts while treating absent scratch contents as unavailable evidence;
4. trace the later Phase 15–21 reconstruction chain separately from the original survivor claim;
5. populate the provenance matrix before selecting an executable candidate.

## 11. Continuous ledger

- `2026-07-30 lane creation`: opened a separate live report before further Eq-11.1 archaeology or numerical implementation.
- `initial retrieval`: recorded the explicit equation, all already known negative history, commit `4b08ab1`, and two failed exact-path fetches.
- `source-commit classification`: inspected changed-file evidence, `found.txt`, `search_out.txt`, and `phase_mismatch_results.txt`; classified the cited commit as documentation/search evidence without a located Eq-11.1 executable or complete numerical chain.
- `root-runner check`: inspected the active simulation loop and classified `lineum.py` as a harness for public `step_core`, not an implementation of the documented Eq-11.1 growth/leakage law.
- `task-system correction`: confirmed ClickUp workspace `90121717552` as Lineum Dynamics, created active task `869ebyvpb` in `Research & Engineering → Engine R&D → Core Simulations`, and classified repository `todo.md` files as historical evidence rather than the active backlog.
