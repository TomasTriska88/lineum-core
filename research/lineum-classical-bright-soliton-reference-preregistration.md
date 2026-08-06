# Classical Bright-Soliton Reference Before Lineum Emergence

**Status:** active preregistration; no execution yet  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-06  
**Repository / branch / base:** `TomasTriska88/lineum-core` / `develop` / `c1935fabed22fb52291039604cf2b025f3bb0b19`  
**Scope:** conventional one-dimensional focusing cubic nonlinear Schrödinger / Gross–Pitaevskii bright-soliton reference; every Lineum substitution is blocked

## Direction and lineage

The owner changed the research order: reproduce established physics first, then remove exactly one understood function and test whether Lineum can replace it emergently. This is a methodological constraint, not physical evidence.

The predecessor B4 screen independently reproduced 28 `psi`–`phi` cases with zero checker mismatches. It found two cap-dependent partial `psi` recoveries and zero full-state recoveries. The exact localized-L1 route is therefore `unsupported_under_tested_conditions` as cap-free full-state recovery. It did not falsify wider Lineum, identify an energy-return path, or establish real physics.

Current `soliton-like` manuscript language remains analogy only. The stronger Eq-11 dissipative-localization claim is `unresolved` here. Conservative solitons and dissipative structures are separate families. No whitepaper change is authorized.

## Public-source intake

Only public scholarly equations and facts are used; no external code, data, private TOLOG material, or unpublished implementation is incorporated: Zakharov–Shabat (JETP 34, 1972, 62–69), Gross (DOI `10.1007/BF02731494`), Pitaevskii (JETP 13, 1961, 451–454), Strecker et al. (DOI `10.1038/nature747`), Khaykovich et al. (DOI `10.1126/science.1071021`), and Strang (DOI `10.1137/0705041`). Permitted use is attribution and original implementation only.

## Frozen analytic reference

\[
i\partial_t\psi=-\frac12\partial_{xx}\psi-|\psi|^2\psi.
\]

Freeze the exact stationary soliton

\[
\psi_s(x,t)=\operatorname{sech}(x)e^{it/2}.
\]

Conserved quantities are

\[
M=\int|\psi|^2dx,\quad P=\operatorname{Im}\int\psi^*\psi_xdx,\quad H=\int\left(\frac12|\psi_x|^2-\frac12|\psi|^4\right)dx,
\]

with known values `M=2`, `P=0`, `H=-1/3`, peak density `1`, and density variance `pi^2/12`. All variables are dimensionless; no laboratory, Lineum, or cosmological scale is inferred.

The claim tested is orbital stability, not attraction or exact return. A dissipative attraction question requires a separate reference.

## Frozen numerical protocol

```text
domain [-40,40), periodic; L=80; N=4096; dx=0.01953125
T=20; primary dt=0.001; diagnostics every 0.1
float64/complex128; no randomness
NumPy >=1.24,<2.0.0; SciPy >=1.10
```

Exact environment versions must be frozen with code. No clipping, filtering, renormalization, mask, cap, reset, or correction is allowed. Primary propagation is Strang split-step Fourier with nonlinear half-steps `exp(i|psi|^2 dt/2)` around the linear multiplier `exp(-i k^2 dt/2)`.

## Frozen lanes

- **A exact:** `psi=sech(x)`.
- **B perturbation:** `epsilon=0.05`; `psi=(1/sqrt(1+epsilon))*sech(x/(1+epsilon))`, preserving mass `2`.
- **C linear null:** remove the cubic term.
- **D defocusing null:** reverse the cubic sign.

Report finite state, mass/momentum/Hamiltonian drift, peak, periodic density centre, variance, and mass in `|x|>=30`. Lane A uses exact-field comparison after global-phase alignment only. Lane B fixes `eta_hat=M/2`, uses the preregistered density centre, aligns only global phase, and reports orbital L2 error plus projection residual.

## Frozen gates

Lane A at `T=20`: mass drift `<=1e-11`; momentum drift `<=1e-11`; Hamiltonian drift `<=1e-6`; field L2 error `<=1e-4`; density L2 error `<=1e-5`; boundary-tail fraction `<=1e-10`. Runs at `dt=0.002,0.001,0.0005` must show time-convergence order `>=1.7`.

Lane B: mass drift `<=1e-10`; Hamiltonian drift `<=1e-5`; orbital L2 error and projection residual each `<=0.10`; centre displacement `<=0.10`; boundary-tail fraction `<=0.01`.

Each null must meet at least one: orbital error `>0.25`, peak below `0.75` of initial, or boundary-tail fraction `>0.05`. Otherwise the observer is non-identifying and must be repaired before Lineum comparison.

## Independent verification and next gate

Before execution, version `0.2.0` must contain complete original primary code, analytic checks, machine-readable schema, environment receipt, hashes, and an independent fourth-order finite-difference method-of-lines verifier that imports no primary propagation, derivatives, metrics, or verdicts.

A pass validates only the frozen numerical reference. A failure requires methodological repair and does not falsify the analytic soliton. Implementation disagreement is `unresolved` and must be traced to the first divergent observable.

Focusing NLS is `active`; linear/defocusing controls are `queued`; moving/colliding, trapped-GPE, and dissipative-CGLE families are `dormant`; B4 is boundedly unsupported; Eq-11 is unresolved; linon identity and real-universe links are `not_yet_compared`; every Lineum substitution is `blocked`.

This version does not establish that the solver works, the pulse attracts, a linon is an NLS/GPE soliton, Eq-11 is right or wrong, or Lineum maps to gravity, dark matter, quantum measurement, cosmology, or ontology.

**Next:** commit complete executable version `0.2.0` before any official numerical run.
