# Classical Reference Before Lineum Emergence — Reciprocal Exchange First

**Status:** active preregistration; reciprocal-exchange execution not yet started  
**Version:** 0.3.0  
**Evidence cutoff:** 2026-08-06  
**Repository / branch / base:** `TomasTriska88/lineum-core` / `develop` / `2d69bd3236e20767c508134e7ba565f54f00dbd1`  
**Historical filename retained:** `research/lineum-classical-bright-soliton-reference-preregistration.md`  
**Root programme:** `research/lineum-public-tolog-galactic-shape-b4.md`, version `0.10.1`, evidence cutoff `2026-08-05`  
**Verified predecessor:** `research/lineum-public-tolog-galactic-shape-b4-localized-l1-verification-receipt.md`, version `1.0.0`, evidence cutoff `2026-08-06`  
**Scope:** one conventional non-spatial reciprocal-exchange reference is now primary; the bright-soliton reference is preserved as a paused localization calibration; every Lineum substitution remains blocked  
**Current confidence:** protocol-level only; no new physical or numerical result

## Plain conclusion

The next question is no longer whether a localized pulse can keep its shape. It is first whether two components can exchange one conserved quantity in both directions, and what additional structure is required for the quantity to return.

The smallest useful reference therefore has no grid, Laplacian, vortex, boundary, noise, cap, saturation, or Lineum field. It contains only two coupled modes with an exact ledger. This isolates the missing "pipe back" before spatial localization is reintroduced.

The soliton work is not deleted. It remains in this same report as a paused calibration for localization after reciprocal exchange is understood.

## Owner-provided direction and correction

The following statements are owner-provided methodological constraints, not evidence:

- **Classical-first direction:** reproduce established scientific behavior first and introduce Lineum emergence only at the smallest place where an understood mechanism is missing.
- **Single-report constraint:** continue in this report; do not create another research report for the exchange reference.
- **Scope correction:** do not assume that a soliton is the main answer to the B4 failure. Treat it only as a possible later localization calibration.

Agent formalization: the cheapest discriminating step is a conventional two-mode exchange model that separates four logically different behaviors:

1. reciprocal coherent return;
2. reciprocal but relaxing equilibration;
3. one-way accumulation;
4. no coupling.

No Lineum mechanism is selected by this formalization.

## Inherited evidence

The independently verified B4 localized-L1 screen recomputed all 28 frozen cases with zero numerical and categorical mismatches. It observed two cap-dependent partial `psi` recoveries and zero full-state recoveries. Removing the `phi` cap produced zero recoveries while `phi` continued to grow. The result is `robust_within_tested_domain` for that numerical observation, but no return mechanism is identified and wider Lineum is not falsified.

This report therefore inherits the following bounded problem:

> The tested implementation can move quantity from the `psi` side into `phi`, and `phi` can influence later `psi` updates, but the tested system did not demonstrate a cap-free, explicit, conserved, reciprocal return cycle for the full state.

## Current implementation audit

At Core commit `2d69bd3236e20767c508134e7ba565f54f00dbd1`, `lineum_core/math.py` labels the current path as "Mode Coupling (Energy Transfer)" and computes, in operational form,

```text
delta_e = mode_coupling_strength * |psi|^2 * kappa * dt
phi <- phi + delta_e
|psi|^2 <- max(|psi|^2 - delta_e, 0)
```

The same update then diffuses `phi` and clips it to `[0, phi_cap]`.

`phi` also affects `psi` through a gradient-driven flow term and a bounded nonlinear interaction term. Those terms are influences from `phi` to `psi`, but they are not an explicit reverse ledger paired with `phi <- phi - returned_quantity`. The implementation therefore contains:

- an explicit accounted transfer `psi -> phi`;
- indirect `phi -> psi` influence;
- no explicit reciprocal conserved exchange law;
- explicit caps and separate dissipation/diffusion paths.

The current `test_mode_coupling_conservation` checks only that `phi_gain > 0` and is finite. It does not assert exact total-ledger conservation after the complete step, a reverse transfer, a recurrence time, or full-state return.

This is an implementation fact, not a physical interpretation.

## Retrieved historical variants and provenance limits

A historical Core commit `8c4ff12af79b218fce8938497f56f75c4567195e` contained `scripts/poc_reservoir.py`. That POC continuously injected random perturbations at a source, sculpted a `phi` sink and a high-`kappa` corridor, and measured global tension. It tested source-to-sink routing in an open driven system. It did not preregister reciprocal return, close an energy ledger, remove stochastic injection, or test recovery after source removal. The file is absent from the current `develop` tree and is retained here only as historical hypothesis provenance.

Repository-wide searches for additional reservoir and return variants in connected sibling repositories were attempted, but the GitHub search service returned upstream `502` errors. This is a technical retrieval limitation, not evidence that no other variants exist. The cross-repository hypothesis registry remains incomplete and must be reopened if search access recovers.

No private TOLOG material, private messages, unpublished implementation, or third-party source code is used.

## Active scientific question

Can the smallest closed conventional system exhibit:

1. exact transfer from component A to component B;
2. exact return from B to A;
3. conservation of the total ledger;
4. clear separation from reciprocal relaxation and one-way accumulation?

This does **not** ask whether Lineum already performs that exchange. It establishes the reference behavior and the minimum variables needed to define "return."

## Frozen primary model: coherent reciprocal exchange

Let `a(t)` and `b(t)` be dimensionless complex mode amplitudes. Freeze

\[
i\frac{d}{dt}
\begin{pmatrix}
a\\
b
\end{pmatrix}
=
\begin{pmatrix}
\Delta/2 & g\\
g & -\Delta/2
\end{pmatrix}
\begin{pmatrix}
a\\
b
\end{pmatrix},
\qquad
a(0)=1,\quad b(0)=0.
\]

The tracked populations are

\[
P_A=|a|^2,\qquad P_B=|b|^2,\qquad P_{\mathrm{tot}}=P_A+P_B.
\]

The coupling matrix is Hermitian for real `g` and `Delta`, so `P_tot` is conserved.

### Resonant analytic solution

For `g=1` and `Delta=0`,

\[
a(t)=\cos t,\qquad b(t)=-i\sin t,
\]

and therefore

\[
P_A(t)=\cos^2 t,\qquad P_B(t)=\sin^2 t.
\]

Expected events:

```text
t = pi/2 : complete A -> B transfer
t = pi   : complete population return B -> A
t = 2pi  : complete state recurrence
```

The returned state at `t=pi` differs from the initial amplitude by a global phase `-1`; populations are identical. Population return and exact complex-state identity must not be conflated.

### Detuned analytic solution

Define

\[
\Omega=\sqrt{g^2+(\Delta/2)^2}.
\]

For `g=1` and `Delta=2`,

\[
P_B(t)=\frac{1}{2}\sin^2(\sqrt{2}\,t).
\]

The maximum transfer is exactly `1/2`, reached at `t=pi/(2*sqrt(2))`. Populations return at `t=pi/sqrt(2)`. This lane shows that reciprocal conservation alone does not guarantee complete transfer; resonance matters.

## Frozen conventional controls

### R0 — resonant coherent exchange

```text
model = complex two-mode Hermitian coupling
g = 1; Delta = 0
initial = a=1, b=0
horizon = 2*pi
```

Expected: periodic complete transfer and return.

### R1 — detuned coherent exchange

```text
model = complex two-mode Hermitian coupling
g = 1; Delta = 2
initial = a=1, b=0
horizon = 2*pi/sqrt(2)
```

Expected: conserved oscillation, maximum `P_B=0.5`, population recurrence without complete transfer.

### R2 — reciprocal rate exchange

Freeze real non-negative populations

\[
\dot P_A=-kP_A+kP_B,\qquad
\dot P_B=kP_A-kP_B,
\]

with `k=1`, `P_A(0)=1`, `P_B(0)=0`. The analytic solution is

\[
P_A=\frac{1+e^{-2t}}{2},\qquad
P_B=\frac{1-e^{-2t}}{2}.
\]

Expected: exact ledger conservation and bidirectional terms, but monotonic relaxation to `1/2,1/2`; no oscillatory return. This separates reciprocity from phase-preserving recurrence.

### R3 — one-way accumulator

Freeze

\[
\dot P_A=-\gamma P_A,\qquad
\dot P_B=\gamma P_A,
\]

with `gamma=1`, `P_A(0)=1`, `P_B(0)=0`. The analytic solution is

\[
P_A=e^{-t},\qquad P_B=1-e^{-t}.
\]

Expected: exact ledger conservation, monotonic accumulation in B, and no return. This is the closest conventional null to the explicit one-way bookkeeping part of the current `psi -> phi` update, but it is not claimed to reproduce the full Core implementation.

### R4 — uncoupled null

Freeze `g=0`, `Delta=0`, `a(0)=1`, `b(0)=0`.

Expected: `P_A=1`, `P_B=0` for the full horizon.

## Frozen numerical protocol for the next checkpoint

No official execution is authorized by this version.

The next executable version must use only the Python standard library so that the reference does not inherit the unresolved NumPy `<2.0` environment mismatch from the paused soliton lane.

```text
primary integrator = original fixed-step classical RK4
nominal dt = 0.001
event handling = shorten only the final substep to land exactly on each frozen analytic event time
float = Python binary64
randomness = none
caps/clipping/renormalization = forbidden
official output = one deterministic JSON document
```

The independent checker must import no primary integration, metric, or verdict code. It must evaluate the closed-form solutions directly and compare the primary output at the preregistered event times.

## Frozen observables

For every lane report:

- finite values;
- maximum absolute ledger drift `|P_A+P_B-1|`;
- maximum absolute analytic population error;
- event-time populations;
- maximum transferred population;
- count of sign changes in `dP_B/dt` away from analytic turning points;
- whether a complete-transfer event occurred;
- whether a population-return event occurred;
- whether the full complex state returned exactly or only up to global phase.

No image similarity, fitted threshold, post-result event selection, or spatial observer is allowed.

## Frozen gates

### R0 resonant coherent exchange

```text
maximum ledger drift <= 1e-10
maximum analytic population error <= 1e-9
P_B(pi/2) >= 1 - 1e-9
P_A(pi) >= 1 - 1e-9
P_B(pi) <= 1e-9
state at 2*pi: max(|a-1|, |b|) <= 1e-8
```

### R1 detuned coherent exchange

```text
maximum ledger drift <= 1e-10
maximum analytic population error <= 1e-9
abs(max(P_B) - 0.5) <= 1e-8
P_B never exceeds 0.50000001
P_A(pi/sqrt(2)) >= 1 - 1e-9
P_B(pi/sqrt(2)) <= 1e-9
```

### R2 reciprocal rate exchange

```text
maximum ledger drift <= 1e-12
maximum analytic population error <= 1e-10
P_A is monotonic non-increasing
P_B is monotonic non-decreasing
abs(P_A(10) - 0.5) <= 2e-9
abs(P_B(10) - 0.5) <= 2e-9
no complete-transfer event
no population-return event after departure
```

### R3 one-way accumulator

```text
maximum ledger drift <= 1e-12
maximum analytic population error <= 1e-10
P_A is monotonic non-increasing
P_B is monotonic non-decreasing
P_A(10) <= 4.6e-5
P_B(10) >= 0.99995
no population-return event
```

### R4 uncoupled null

```text
maximum ledger drift <= 1e-12
max(|P_A-1|, |P_B|) <= 1e-12
no transfer event
```

If the primary misses a closed-form gate, repair the numerical method without changing the scientific equation or thresholds. If the checker disagrees, preserve both outputs and identify the first divergent observable. Neither case falsifies the analytic reference.

## Meaning of possible outcomes

- **R0 passes, R2/R3/R4 separate:** the harness can distinguish coherent return, relaxation, one-way accumulation, and no coupling.
- **R0 conserves but does not return:** implementation or observer defect; do not proceed to Lineum.
- **R2 appears to return:** return observer is invalid or circular.
- **R3 appears reciprocal:** ledger or derivative observer is invalid.
- **R0 and R1 are indistinguishable:** transfer-completeness observer lacks power.
- **All conventional lanes pass:** only the reference vocabulary is validated. No Lineum mechanism is supported.
- **A later Lineum lane matches R0 populations only:** phase, intervention, and ledger tests are still required before claiming the same mechanism.

## Soliton calibration branch — paused and preserved

The original version `0.1.0` preregistered the focusing cubic nonlinear Schrodinger / Gross-Pitaevskii equation

\[
i\partial_t\psi=-\frac12\partial_{xx}\psi-|\psi|^2\psi
\]

with stationary solution

\[
\psi_s(x,t)=\operatorname{sech}(x)e^{it/2}.
\]

It froze `M=2`, `P=0`, `H=-1/3`, peak density `1`, density variance `pi^2/12`, domain `[-40,40)`, `N=4096`, `T=20`, primary `dt=0.001`, Strang split-step propagation, exact and perturbed focusing lanes, and linear/defocusing nulls.

The branch tests orbital localization, not an energy-return pipe or an attractor. It is now `dormant_pending_exchange_reference`; its equations, thresholds, and prior Git history remain unchanged. Resuming it requires a prospective checkpoint in this same report.

## Unpublished executable attempt chronology

After version `0.1.0`, an executable soliton bundle was prepared in disposable local workspace and short development checks were attempted. The full official `T=20` run was not invoked because the available NumPy major version violated repository requirements.

Publication then failed closed: multiple staged Git blobs did not match the locally expected Git blob SHA. None was attached to a tree, commit, or branch ref. `develop` remained at `2d69bd3236e20767c508134e7ba565f54f00dbd1`.

Because the exact executable payload and receipts never entered version control, they are classified as `unretained_technical_attempt`, not retained scientific evidence. If the soliton lane resumes, its executable bundle must be rebuilt, rechecked, committed, and rerun from the frozen initial state. This version does not reuse the rejected blobs.

## Variant ledger

| Variant | Provenance | Status | Cheapest discriminator |
|---|---|---|---|
| Current Core explicit `psi -> phi` bookkeeping | current implementation | `implemented`; reverse ledger absent | compare against R3 before adding space |
| Current Core indirect `phi -> psi` influence | current implementation | `implemented`; conservation role unresolved | freeze terms separately after conventional reference |
| Historical source-sink reservoir POC | commit `8c4ff12...` | `historical_untested_for_return` | source-off closed-ledger rerun if reopened |
| R0 coherent reciprocal exchange | conventional reference | `active_preregistered` | exact event-time comparison |
| R1 detuned coherent exchange | conventional control | `queued_preregistered` | maximum-transfer gate |
| R2 reciprocal rate exchange | conventional control | `queued_preregistered` | monotonicity and no-return gates |
| R3 one-way accumulator | conventional null | `queued_preregistered` | monotonicity and no-return gates |
| R4 uncoupled | null | `queued_preregistered` | no-transfer gate |
| Bright soliton localization | prior version `0.1.0` | `dormant_pending_exchange_reference` | later full retained run |
| New Lineum return term | not selected | `blocked` | only after conventional gates pass |
| Emergent return from existing fields | owner direction / hypothesis family | `not_yet_tested` | later ablation against explicit conventional term |
| New fundamental field or reservoir | generic alternative | `dormant` | allowed only after minimal-ingredient failure |

## Root-programme impact

| Root item | Relationship | Bounded impact |
|---|---|---|
| B4 Question 1: galactic curve target | `unaffected` | No galaxy observable is tested. |
| B4 Question 2: bounded return | `depends_on` | The exchange reference defines return before another spatial test. |
| B4 Question 3: information-preserving scalar state | `constrains` | Mere accumulation is distinguished from reciprocal return, but information retention is not yet tested. |
| `tanh` replacement | `not_yet_compared` | No replacement law is proposed. |
| LAP4/LAP8 transport | `unaffected` | Space is intentionally removed. |
| Soliton and localization claims | `constrains` | Localization is deferred until exchange semantics are validated. |
| Real physics and ontology | `not_yet_compared` | No empirical mapping follows. |

## Public-source and rights intake

The two-mode equations are independently specified and implemented from standard mathematics. No third-party code, data, figure, or private material will be copied.

Historical attribution only:

- I. I. Rabi, "Space Quantization in a Gyrating Magnetic Field," *Physical Review* 51, 652-654 (1937), DOI `10.1103/PhysRev.51.652`.

The report uses the two-mode oscillation structure as a conventional mathematical reference. It does not claim that Core fields are quantum states, spins, atoms, or laboratory Rabi oscillations.

## Three-layer evidence boundary

1. **Current implementation:** explicit one-way accounted `psi -> phi` transfer, indirect `phi -> psi` influence, diffusion, dissipation, noise options, and caps.
2. **Conventional reference:** exact reciprocal two-mode mathematics and rate-equation controls.
3. **Lineum hypothesis:** an existing-field emergent mechanism might later reproduce the required return behavior without inserting a hand-written return term.

No result currently connects layer 1 to layer 2 mechanistically or either layer to observable-universe evidence.

## Prohibited conclusions

This version does not establish that:

- the reciprocal-exchange runner works;
- the current Core implementation violates or satisfies a complete physical conservation law;
- `phi` is literally an energy reservoir;
- coherent two-mode exchange is the correct Lineum mechanism;
- a linon is a soliton, quantum state, particle, or oscillator;
- the B4 failure is repaired;
- Lineum maps to Bose condensates, Rabi oscillations, gravity, dark matter, quantum measurement, cosmology, consciousness, or ontology.

## Exact next gate

Commit this preregistration before any exchange calculation.

Then, in this same report and no other report:

1. embed complete original standard-library RK4 primary code;
2. embed a separately written closed-form checker;
3. embed permanent tests for equations, event times, gates, independence, and deterministic JSON;
4. record source hashes and environment receipt;
5. commit the executable checkpoint;
6. run the official primary exactly once;
7. commit its exact output before running the checker.

Until the executable checkpoint is committed: no official exchange run, no soliton run, no spatial term, no parameter sweep, no Lineum return term, no mechanism ranking, and no whitepaper edit.
