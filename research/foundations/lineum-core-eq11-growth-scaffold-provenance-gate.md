# Eq-11.1 Growth and Scaffold Provenance Gate

**Status:** active provenance report; no numerical Eq-11.1 repair experiment authorized

**Version:** 0.1.0  
**Evidence cutoff:** 2026-07-30

**Parent programme:** `research/foundations/lineum-core-active-growth-scaffold-repair-matrix.md`

## 1. Answer first

Eq-11.1 is currently the highest-priority distinct “active growth” candidate for the owner’s yeast-plus-mould hypothesis because an explicit growth/leakage equation survives in the repository. It is **not yet reproducible enough to run a repair experiment**.

The immediate task is provenance reconstruction, not parameter tuning and not code promotion.

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

Initial inspection shows a documentation-heavy commit containing repository prose and auxiliary search/result files such as `found.txt`, `found2.txt`, `search_out.txt`, `search_results.txt`, and `phase_mismatch_results.txt`, plus unrelated or adjacent files including an Eq-9 escape-fold test. No Eq-11.1 survivor/reproduction solver has yet been identified in the returned changed-file evidence.

Direct fetches at that commit returned `404 Not Found` for:

- `eval_closed_system_stress.py`;
- `scripts/eval_closed_system_stress.py`.

This is classified as `not_located_at_tested_paths`, not proof that no relevant code exists anywhere in the commit or its ancestry.

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

## 9. Continuous ledger

- `2026-07-30 lane creation`: opened a separate live report before further Eq-11.1 archaeology or numerical implementation.
- `initial retrieval`: recorded the explicit equation, all already known negative history, commit `4b08ab1`, and two failed exact-path fetches.
