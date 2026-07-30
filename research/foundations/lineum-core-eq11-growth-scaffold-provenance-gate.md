# Eq-11.1 Growth and Scaffold Provenance Gate

**Status:** active provenance report; cited source commit and active root runner do not provide an executable Eq-11.1 receipt; no numerical repair experiment authorized

**Version:** 0.8.0  
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

### 5.5 Current-state revalidation before the next provenance pass

The active state was re-read before continuing:

- target repository and branch: `TomasTriska88/lineum-core`, `develop`;
- root router blob: `5568c13966b501de68297a7856edfb7ef746c890`;
- Core rules blob: `cb1bb75d1266eb403bf522086b9286113e88bc13`;
- repository-boundary blob: `05b805c16c68b52c8618c564f9155e9cef913254`;
- the Core Codex path is a relocation and scope notice, while the canonical operational Codex remains in `lineum-dynamics/docs/LINEUM_CODEX_v1.md`;
- ClickUp task `869ebyvpb` remains `in progress` with high priority under `Research & Engineering → Engine R&D → Core Simulations`.

This revalidation changes no scientific result. It confirms that provenance reconstruction remains the authorized next action and that no Eq-11.1 numerical repair run is currently permitted.

### 5.6 Current equation-history whitepaper consistency audit

The current source is `whitepapers/1-core/02-core-equation.md`, blob `64f8341551d5737a6eb4919030bbb85a4b50380c`.

The document is not one coherent Eq-11.1 validation receipt. It layers several scientifically distinct claim families and sometimes presents later limitations beside earlier strong language without resolving their evidentiary status.

#### Claim family A — Eq-11 dimensional scaling

The Version 11 section states that multi-scale sweeps confirmed numerical stability and bounded gradients, then the immediately following destructive audit states that the same minimal equation encounters unavoidable exponential divergence after longer horizons and is barred from canonical promotion.

Classification: `documented_candidate_then_destructive_failure`; the positive and negative claims must not be merged into a generic statement that Eq-11 is stable.

#### Claim family B — Eq-11.1 scalar amplitude bounding

The Version 11.1 section claims that `-lambda Phi² Psi` and the phase-gradient leakage term bound amplitude over long horizons, including strong language about 50,000- to 100,000-step persistence, broad parameter robustness, and no fine-tuning.

This is a scalar-amplitude and global-energy claim. It does not by itself prove preservation of a topological core, repair, heredity, or independence from external scaffolding.

Classification: `strong_prose_claim_without_recovered_executable_receipt`.

#### Claim family C — isolated topological-core survival

The document separately claims indefinite vortex-core preservation with approximately `Max Psi ≈ 1.87` and `Core Psi ≈ 0.00019`. Elsewhere in the recorded reconstruction history, a nominal topological node decays into a scalar puddle and no tested open-vacuum frontier preserves both topology and a quiet far field.

Classification: `direct_internal_conflict_requiring_commit_and_runner separation`.

#### Claim family D — pair and multi-body binding

The document records short-term stationary locks, oscillatory pair states, wakes, phase-locked forcing, static confinement, and rotational backgrounds. It also records that symmetric locks eventually scatter, third-body interference shatters locks, generic ambient backgrounds fail to capture, and the unmodified minimal open-vacuum system fails to spontaneously bind `N >= 3` structures.

Classification: `mixed_intrinsic_and_extrinsic_mechanisms`; pair binding, environmental forcing, confinement, and spontaneous self-assembly must remain separate variants.

#### Claim family E — engineered stabilization principles

Later minimal-isolation tests explicitly classify kinetic-to-phase redistribution and super-linear overlap troughs as failed mechanisms for spontaneous stabilization. Their earlier engineered successes depended on rigid symmetric seeds or forced high-amplitude overlaps.

Classification: `unsupported_under_generic_isolation`; earlier demonstrations cannot be used as evidence of native spontaneous stabilization.

#### Claim family F — closed-energy and scaffold variants

The changelog later introduces a closed-energy thermodynamic cycle as a candidate after unilateral open-vacuum and local-depletion variants failed. Static `kappa` confinement and phase-locked external forcing are also described as viable extrinsic architectures.

Classification: `separate_environment_or_boundary_variants`, not evidence that the unmodified Eq-11.1 law is self-sufficient.

#### Whitepaper-level verdict

The whitepaper is a valuable hypothesis and chronology source, but currently has the provenance status:

```text
internally_layered_claim_record_with_unresolved_conflicts
```

It must not be treated as a single validated experiment. Commit archaeology must split at least the following variants before any code is reconstructed:

1. isolated scalar amplitude bound;
2. isolated topological vortex survival;
3. open-vacuum pair dynamics;
4. phase-gradient leakage / bridge suppression;
5. background-flow or rotational-frame assistance;
6. static `kappa` confinement;
7. phase-locked external forcing;
8. closed-energy thermodynamic circulation;
9. engineered overlap and flow-warp mechanisms already negative under generic isolation.

No numerical repair experiment is authorized by this audit.

### 5.7 Search-index limitations observed

Repository file search located the current equation-history path only through a broad `equation history` query. Exact searches for `Eq-11.1`, `Near-Threshold Coupling Corridor`, and the explicit operator phrase returned no useful file or commit results despite the known commit `4b08ab1` existing.

A nominal “most recent commits” search also returned results ending on 2026-03-13 even though later immutable commits on `develop` are known and directly fetchable. Broad commit-message searches for terms visibly present in later history returned no matches.

Classification: `search_index_incomplete_for_provenance`. Exact commit fetches, changelog phrases, changed-file inspection, immutable SHAs, and branch comparisons must take precedence over search absence.

### 5.8 Exact payload audit of commit `4b08ab1`

Commit `4b08ab1ebac1beb287c5ecd7f74803e530e7e7ad` was created on 2026-04-06. Its patch changed the equation-history whitepaper from version `1.2.11` to `1.2.20`, changed the document date from 2026-03-31 to 2026-04-06, and expanded the declared equation range from V1–V7 to V1–V11.1.

The same documentation commit introduced, in one payload:

- removal of the advection hypothesis and promotion of a metabolic-amplification framing;
- the Eq-11 dimensionally invariant candidate;
- the destructive long-horizon Eq-11 divergence claim;
- the Eq-11.1 equation and “code-backed” gradient-dissipation wording;
- claimed 50,000- and 100,000-step amplitude-bounding audits;
- cluster ceiling and lambda-limit claims;
- scalar collision and fragmentation claims;
- indefinite isolated vortex-core preservation claims;
- failed advection results;
- bridge-suppression, oscillatory-pair, wake, rotational-frame, channel-flow, torque, self-repairing wake, and thermodynamic-minimization claims;
- the practical open-vacuum N=2 limit and Near-Threshold Coupling Corridor;
- rejection of N>=3 spontaneous composition without external geometry or fields.

Strong positive, negative, intrinsic, and externally assisted claims were therefore introduced together inside a bulk retrospective documentation patch. They were not represented in that commit as a sequence of separately versioned executable experiments with one receipt per claim.

The commit uses phrases such as “code-backed”, “validated”, “proved”, and “verified”, but no corresponding complete Eq-11.1 runner, initializer, parameter manifest, raw state, or command receipt has yet been recovered from its changed-file evidence.

Classification:

```text
bulk_retrospective_documentation_bundle_without_recovered_executable_chain
```

Consequences:

1. the commit can date the introduction of wording and candidate equations;
2. it cannot validate any of the numerical or physical interpretations by itself;
3. each claim family must be independently traced to an executable artifact or downgraded to unreproduced prose;
4. contradictions inside the payload are historical evidence, not a reason to select whichever sentence supports the preferred story.

### 5.9 Broad branch-compare limitation

Comparing `4b08ab1` with current `develop` confirms that `develop` is 227 commits ahead. The returned changed-file inventory is dominated by later governance, Core-library evolution, output updates, and the major Portal migration out of Core.

This broad comparison is useful for confirming branch ancestry and large repository movement. It is not sufficient to prove whether a short-lived Eq-11.1 research script existed and was later deleted because:

- the change set is very large;
- the API inventory is mixed with an extensive Portal removal;
- returned file lists may be capped or omit detail needed for exhaustive provenance;
- a missing filename in this broad response is not proof of historical absence.

Classification: `ancestry_confirmed_but_file_provenance_incomplete`.

### 5.10 Exact named-script receipt audit

The current equation-history whitepaper explicitly names two Eq-11 manipulation scripts:

- `eval_eq11_flow_redistribution.py`;
- `eval_eq11_pair_overlap.py`.

The earlier provenance trail also names `eval_closed_system_stress.py` as a candidate stress/reconstruction receipt. A symmetric exact-path audit tested each filename at:

- repository root;
- `scripts/`;
- `.scratch/`.

Each path was tested against both:

- historical source commit `4b08ab1ebac1beb287c5ecd7f74803e530e7e7ad`;
- current branch `develop` at the evidence cutoff.

| Named artifact | Root at `4b08ab1` | `scripts/` at `4b08ab1` | `.scratch/` at `4b08ab1` | Root on `develop` | `scripts/` on `develop` | `.scratch/` on `develop` | Current classification |
|---|---:|---:|---:|---:|---:|---:|---|
| `eval_closed_system_stress.py` | 404 | 404 | 404 | 404 | 404 | 404 | `named_in_provenance_but_not_located_at_18_cell_audit_subset` |
| `eval_eq11_flow_redistribution.py` | 404 | 404 | 404 | 404 | 404 | 404 | `whitepaper_named_but_not_located_at_18_cell_audit_subset` |
| `eval_eq11_pair_overlap.py` | 404 | 404 | 404 | 404 | 404 | 404 | `whitepaper_named_but_not_located_at_18_cell_audit_subset` |

Receipt totals:

```text
named artifacts: 3
refs per artifact: 2
paths per ref: 3
exact fetches: 18
located files: 0
404 responses: 18
```

This result establishes only that none of the three named files is versioned at the tested exact paths in the cited bulk documentation commit or current `develop`.

It does **not** establish that:

- the experiments never ran locally;
- no renamed implementation existed;
- no deleted file existed in an intermediate commit;
- prose values are necessarily false;
- the equations cannot be reconstructed independently.

It does establish that the present whitepaper references are not sufficient executable receipts. Until a renamed or intermediate artifact is recovered, claims depending on these scripts remain `unreproduced_prose_claims` rather than validated results.

The `.scratch/` checks are especially important: repository policy treats `.scratch/` as disposable. A local script may have existed there and later vanished. Such a possibility preserves historical uncertainty but cannot satisfy permanent reproducibility.

Classification of the exact-path lane:

```text
complete_for_three_named_artifacts_and_two_tested_refs;
negative_for_file_location;
inconclusive_for_unversioned_or_renamed_history
```

The next safe discriminator is not parameter tuning. It is recovery of additional filenames, output names, immutable commit SHAs, or code fragments from committed documentation/search artifacts and intermediate commit patches.

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

### 6.1 Initial populated artifact matrix

| Artifact / claim family | Exact evidence recovered | Equation / algorithm | Parameters and initializer | Observer and output | Status | Reopen trigger |
|---|---|---|---|---|---|---|
| `eval_closed_system_stress.py` | filename in provenance; 6 exact path/ref checks all 404 | not recovered | not recovered | not recovered | `unreproduced_named_artifact` | recover renamed/deleted file, immutable patch, or complete embedded code |
| `eval_eq11_flow_redistribution.py` | filename in current whitepaper; 6 exact path/ref checks all 404 | prose describes negative flow divergence redistributed into imaginary phase rotation | coefficients, grid, timestep, seed and initializer not recovered | prose later reports generic-isolation failure and `+300%` defect density | `unreproduced_engineered_mechanism_with_negative_prose_result` | recover executable receipt and reproduce both engineered success and generic-isolation failure |
| `eval_eq11_pair_overlap.py` | filename in current whitepaper; 6 exact path/ref checks all 404 | prose describes super-linear `Phi` coupling weighted by `|Psi|^4` in overlap regions | coefficients, grid, timestep, seed and initializer not recovered | prose later reports `0%` deviation under generic random thermal isolation | `unreproduced_engineered_mechanism_with_negative_prose_result` | recover executable receipt and reproduce both forced-overlap success and generic-isolation null result |
| Eq-11.1 bulk claim bundle in `4b08ab1` | complete documentation patch recovered | explicit Eq-11.1 law plus multiple later assisted variants | incomplete and internally mixed | many scalar, topology, binding and limit values in prose | `bulk_retrospective_documentation_without_executable_chain` | split into claim-specific receipts with exact code and outputs |

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

Before any implementation, the next retrieval pass is frozen as follows:

1. extract additional output filenames, experiment labels (`EXP24`–`EXP39`, Phase 15–21), immutable SHAs, and code fragments from the current whitepaper, `4b08ab1` patch, and committed search artifacts;
2. test every newly recovered exact path at its associated commit and current `develop`, preserving every 404 and every located file;
3. inspect located outputs for embedded parameters, command lines, source hashes, seeds, grids, timesteps, observers, and parent script names;
4. trace later Phase 15–21 reconstruction separately from the original bulk documentation payload;
5. classify every artifact in the provenance matrix before selecting an executable candidate;
6. do not synthesize missing code or tune parameters until the matrix shows one fully specified baseline candidate.

## 11. Continuous ledger

- `2026-07-30 lane creation`: opened a separate live report before further Eq-11.1 archaeology or numerical implementation.
- `initial retrieval`: recorded the explicit equation, all already known negative history, commit `4b08ab1`, and two failed exact-path fetches.
- `source-commit classification`: inspected changed-file evidence, `found.txt`, `search_out.txt`, and `phase_mismatch_results.txt`; classified the cited commit as documentation/search evidence without a located Eq-11.1 executable or complete numerical chain.
- `root-runner check`: inspected the active simulation loop and classified `lineum.py` as a harness for public `step_core`, not an implementation of the documented Eq-11.1 growth/leakage law.
- `task-system correction`: confirmed ClickUp workspace `90121717552` as Lineum Dynamics, created active task `869ebyvpb` in `Research & Engineering → Engine R&D → Core Simulations`, and classified repository `todo.md` files as historical evidence rather than the active backlog.
- `state revalidation`: re-read the current Core rules, repository boundaries, Codex routing notice, canonical Dynamics Codex, active report, and ClickUp task before resuming provenance archaeology; no scientific result changed and no numerical run was authorized.
- `next-pass preregistration`: froze a retrieval-first plan using unique operators, exact commit archaeology, explicit separation of original and reconstructed claims, and a prohibition on code synthesis before a complete baseline candidate is recovered.
- `current-whitepaper consistency audit`: split the equation-history document into distinct scalar, topological, binding, scaffold, forcing, and closed-cycle claim families; recorded direct internal conflicts and negative isolation results; classified the document as a layered claim record rather than a single validation receipt.
- `search-index limitation`: exact phrase and commit searches failed to recover known Eq-11.1 provenance, and nominal recent-commit search stopped before known later history; immutable fetches and branch comparisons now take precedence.
- `source-payload audit`: established that `4b08ab1` introduced most Eq-11 and Eq-11.1 positive, negative, intrinsic, assisted, and N=2-limit claims together in a bulk documentation patch without a recovered executable chain.
- `broad-compare audit`: confirmed 227-commit ancestry from `4b08ab1` to `develop` while recording that the large Portal migration and response limits make the broad file inventory insufficient for exact script provenance.
- `named-script audit`: extracted three explicit or provenance-named scripts and completed 18 exact path/ref fetches; all returned 404, so none is currently a recoverable executable receipt at the tested paths.
- `artifact-matrix initialization`: populated the first permanent matrix rows, preserving both the missing receipts and the negative prose results associated with the two engineered stabilization mechanisms.
