# Lineum Public-TOLOG Galactic Shape Benchmark — B4 Analytic Checkpoint

**Status:** validated  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** pre-fit analytic and implementation gates only; no astronomical fit result has been inspected  
**Current confidence:** high within the declared floating-point environment

## Plain result

All five preregistered saturating functions passed the fairness gates before any NGC 3198 fit was run. They all begin at zero, have the same unit initial slope, rise monotonically, remain bounded between zero and one on the frozen grid, and approach the same unit plateau.

This means the astronomical comparison can now ask about curve shape rather than accidentally comparing different central normalizations or plateau amplitudes.

## Frozen function family

The tested functions are:

- `tanh(x)`;
- `1-exp(-x)`;
- `x/(1+x)`;
- `(2/pi)*atan((pi/2)*x)`;
- `x/sqrt(1+x^2)`.

Every function has `S(0)=0`, `S'(0)=1`, and `S(infinity)=1`.

## Analytic receipt

| Shape | finite-difference derivative at zero | `S(100)` | half-saturation argument | half value | gate |
|---|---:|---:|---:|---:|---|
| `tanh` | `0.9999999999996667` | `1.0` | `0.5493061443340548` | `0.49999999999999994` | pass |
| `exponential` | `0.9999999999732445` | `1.0` | `0.6931471805599453` | `0.5` | pass |
| `rational` | `1.000000000001` | `0.9900990099009901` | `1.0` | `0.5` | pass |
| `arctan` | `0.9999999999991775` | `0.9959472074048805` | `0.6366197723675814` | `0.5` | pass |
| `algebraic` | `0.9999999999995001` | `0.9999500037496876` | `0.5773502691896258` | `0.5` | pass |

For each shape, the following gates passed:

- finite value at zero;
- zero value within `1e-15`;
- unit derivative within `1e-8`;
- monotonicity on `10001` points over `x in [0,100]`;
- boundedness within `1e-14`;
- `S(100)>=0.99`;
- finite positive analytic half-saturation argument;
- half-saturation value within `1e-14`;
- independent scalar and vector evaluation agreement within `1e-14`.

## Exact procedure

The derivative was checked with a central finite difference using step `1e-6`. Monotonicity and boundedness were checked on a uniform `10001`-point grid from zero to one hundred. Scalar and vector implementations were compared at `x=[0,0.1,1,10,100]`.

The exact analytic-only command was equivalent to:

```text
python research/runners/lineum_public_tolog_galactic_shape_b4.py \
  --analytic-only \
  --output research/results/lineum_public_tolog_galactic_shape_b4_analytic.json
```

The repository runner is a small loader plus a losslessly compressed sibling source. The loader decompressed the frozen source and produced a receipt byte-for-byte identical to direct source execution.

## Provenance and hashes

- input data were not opened by the analytic-only lane;
- loader SHA-256: `0c6cfc5d8e5dec3abf2dcb4ee8d021afb826f4529ecad7a6c2c9d67e8d610045`;
- compressed source SHA-256: `4542bc3379b7cf0308f2dde21e0c025a90136c9b5c66a8914cefa3d56b80595c`;
- decompressed source SHA-256: `7d6e153d4de97f0babfe1d8b8ae8539ad6f8f0949ba066a778dbe685c38d3b3e`;
- analytic receipt SHA-256: `50a8d204e5810d6bd7f17de72a55434f1e1fca1a851c20cac90c875242402a13`.

Environment:

- Python `3.13.5`;
- NumPy `2.3.5`;
- SciPy `1.17.0`;
- Linux x86-64.

Repository requirements declare NumPy below `2.0.0`; the supplied runtime uses NumPy `2.3.5`. This checkpoint concerns elementary function evaluations and independent scalar/vector agreement, so the mismatch is recorded but does not change the gate result.

## Scientific separation

**Implementation:** five explicitly normalized mathematical functions were evaluated.

**Observed:** all frozen analytic gates passed.

**Interpretation:** the functions are fair enough for the declared two-parameter astronomical shape comparison.

**Hypothesis:** no function is yet preferred by galaxy data.

**Known-physics boundary:** this checkpoint contains no galaxy fit and says nothing about gravity, dark matter, modified gravity, TOLOG derivation, or Lineum emergence.

## Next permitted step

The preregistered NGC 3198 fits may now run without changing the functions, starts, bounds, source lanes, metrics, or decision thresholds.
