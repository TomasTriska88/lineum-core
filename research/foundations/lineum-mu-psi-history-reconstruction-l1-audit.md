# Mu-Psi History Reconstruction L1 Audit and Preregistration Correction

**Status:** active implementation audit result; transcribed-reference L1 passed; direct import of the active Core remains pending; one predecessor equation is corrected and superseded within the scope stated below  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-07-31  
**Scope:** Core-only audit of the deterministic NumPy `mu` write path. This report tests whether the explicit `mu` trajectory can be reconstructed from the exact `Psi`-energy history consumed by the update, corrects the predecessor preregistration's closed-form recurrence, and distinguishes a transcribed source adapter from a direct import of the active package. It does not test `Phi`-only reduction, continuum convergence, branch ontology, consciousness, quantum measurement, or correspondence with nature.  
**Central questions:** Does an independent implementation reconstruct the current `mu` trajectory exactly from the write-time `Psi` energy history? Does reconstruction fail when given the wrong activity snapshot or wrong temporal ordering? What exact recurrence is implemented after sequential in-place growth and decay?  
**Current confidence:** high that the corrected recurrence matches the deterministic NumPy source path at blob `bb877021810691223a0eb960a45493a2e351112a`; high that two independent reconstruction implementations reproduce the transcribed adapter over the frozen matrix; high that the predecessor first-order coefficient was incomplete; medium for active-package equivalence because this environment could not import a fresh checkout; no claim about `mu = Phi`, a fundamental analog ontology, quantum mechanics, or nature.

## 1. Answer first

The narrow result passed, but the audit first found and corrected an error in its own preregistration.

The current code applies the `mu` operations sequentially:

```text
1. add activity-driven growth;
2. apply decay to the already-grown value;
3. clip the result.
```

The predecessor report had written the decay as though it acted on the old value. That omitted a cross term proportional to `rho * eta * activity * dt^2`. The mistake does not change the main determinism conclusion, but the published recurrence and closed-form coefficient were not exact.

After correcting that order:

- 32 deterministic runs were executed;
- the matrix covered four initialization families, two timesteps, two stencils, and both `Phi` diffusion timestep modes;
- the matrix contained 2,621,440 cell-step updates;
- a vectorized reconstruction and an independent Python-scalar reconstruction both matched every stored `mu` value with maximum absolute error `0.0`;
- the corrected constant-activity closed form matched to `4.440892098500626e-16`;
- using the post-mode-coupling output energy instead of the actual write-time energy produced nonzero errors from `2.9026037664164894e-05` to `4.817052198928251e-04`;
- reversing the activity history produced nonzero errors from `1.9799097623741123e-02` to `1.4079178162864864e-01`.

Therefore the test is sensitive to both the exact observation point and temporal order. Within the transcribed deterministic source path:

```text
current mu is an exactly reconstructible state coordinate
of complete write-time Psi-energy history, kappa, initial mu,
and frozen parameters.
```

This is an implementation result. It does not prove that `mu` is physically identical to `Phi`, nor that nature contains an analogous field.

## 2. Programme coordinates and lineage

Target:

```text
repository: TomasTriska88/lineum-core
branch: develop
```

Root scientific programme:

```text
path: research/foundations/lineum-continuous-source-cosmology-validation.md
version: 0.4.14
evidence cutoff: 2026-07-29
blob SHA: 3fba3925553cd5596e46c02fa35d1db91523537d
```

Mandatory continuity companion:

```text
path: research/foundations/lineum-root-programme-continuity-and-impact-ledger.md
version: 0.3.0
evidence cutoff: 2026-07-31
blob SHA: 5304874451caf32313ad0e8e3c59e53958698d79
```

Conceptual parent:

```text
path: research/foundations/lineum-mu-branch-relative-identity-and-entanglement-hypothesis.md
version: 0.2.0
blob SHA: b55bc1639fc8ed6efa7b8286e9113afa88ee298c
```

Immediate predecessor:

```text
path: research/foundations/lineum-mu-phi-reduction-and-continuum-preregistration.md
version: 0.1.0
blob SHA: 16fac63f7659427ee18865fce82fbad0868311bd
```

Active source coordinate transcribed for this audit:

```text
path: lineum_core/math.py
blob SHA: bb877021810691223a0eb960a45493a2e351112a
path exercised: deterministic NumPy update with use_mu=True,
use_mode_coupling=True, and quantum noise disabled
```

Lineage:

```text
lineum-continuous-source-cosmology-validation.md v0.4.14
    |
    +-- lineum-root-programme-continuity-and-impact-ledger.md v0.3.0
    |
    +-- lineum-eq11-epsilon-relic-foam-provenance-comparison.md v0.1.0
            |
            +-- lineum-mu-branch-relative-identity-and-entanglement-hypothesis.md v0.2.0
                    |
                    +-- lineum-mu-phi-reduction-and-continuum-preregistration.md v0.1.0
                            |
                            +-- this L1 audit and correction v0.1.0
```

ClickUp was not called. The returned MCP rate-limit window was respected. Operational synchronization remains pending as one future batched update.

## 3. Evidence layers

### 3.1 What the implementation computes

For each cell and step, define:

```text
m_n = mu before the write
A_n = max(E_n - q_n, 0)
E_n = the pre-mode-coupling |Psi|^2 snapshot used by the mu write
q_n = mu_peak_cutoff_ratio * max(E_n) when the ratio is in (0, 1)
g_n = eta * A_n * kappa * dt
d = 1 - rho * dt
```

The source executes:

```text
m_tmp = m_n + g_n * (1 + m_n)
m_(n+1) = clip(d * m_tmp, 0, mu_cap)
```

Equivalently:

```text
m_(n+1) = clip(d * ((1 + g_n) * m_n + g_n), 0, mu_cap)
```

With `y_n = 1 + m_n`, before clipping:

```text
y_(n+1) = B_n * y_n + c
B_n = (1 - rho * dt) * (1 + eta * A_n * kappa * dt)
c = rho * dt
```

### 3.2 What was numerically observed

```text
runs: 32
cell-steps: 2,621,440
maximum vectorized reconstruction error: 0.0
maximum independent scalar reconstruction error: 0.0
constant-activity closed-form error: 4.440892098500626e-16
zero-activity decay error: 1.1102230246251565e-16
```

Negative controls:

```text
wrong activity snapshot maximum-error range:
2.9026037664164894e-05 to 4.817052198928251e-04

reversed history maximum-error range:
1.9799097623741123e-02 to 1.4079178162864864e-01
```

### 3.3 Interpretation

`mu` is a deterministic, causally active summary of the declared history. It can make a history-dependent update locally Markovian: the next step needs the current stored `mu` rather than the full past.

Deterministic reducibility to complete `Psi` history does not imply practical redundancy. Replacing `mu` may require retaining a long, nonlinear, globally thresholded history.

### 3.4 Hypotheses still open

- `mu` is reconstructible from `Phi` history alone;
- `mu` is a coarse-grained or slower representation of `Phi`;
- a simpler finite-memory coordinate replaces `mu` in closed loop;
- a relational or branch-aware state contains information absent from the current local recurrence;
- Lineum's intended carrier is fundamentally analog or continuous.

### 3.5 Observable-universe boundary

No empirical statement about the observable universe was tested. Agreement inside this implementation is not evidence that nature uses `Psi`, `Phi`, `mu`, a lattice, a continuum, branches, or the same memory law.

## 4. Verified predecessor correction

The predecessor preregistration stated:

```text
mu_(n+1) = mu_n
           + eta * A_n * kappa * (1 + mu_n) * dt
           - rho * mu_n * dt
```

and therefore used:

```text
B_n = 1 + [eta * A_n * kappa - rho] * dt
```

That is not exact for the current sequential in-place implementation. The source first mutates `mu` with growth and then computes decay from the mutated value:

```python
mu += growth
mu -= rho * mu * dt
```

The exact unclipped recurrence is:

```text
g_n = eta * A_n * kappa * dt
d = 1 - rho * dt
mu_tmp = (1 + g_n) * mu_n + g_n
mu_(n+1) = d * mu_tmp
```

or:

```text
y_(n+1) = d * (1 + g_n) * y_n + (1 - d)
```

The predecessor coefficient omitted:

```text
-rho * eta * A_n * kappa * dt^2
```

Scope-safe verdict:

```text
predecessor closed-form coefficient:
falsified_within_current_sequential_numpy_mu_update

deterministic reducibility conclusion:
still_supported

Phi-only reduction:
untested

independent physical mu:
not established
```

The predecessor remains preserved as historical preregistration. This successor controls any use of its recurrence.

## 5. Frozen matrix

Each run used:

```text
grid: 32 x 32
steps: 80
kappa: uniform 1
initial Phi: zero
initial mu: zero
mode coupling: enabled
quantum noise: disabled
mu write: enabled
mu_eta: 0.005
mu_rho: 0.0001
mu_cap: 10
mu_peak_cutoff_ratio: 0.1
```

Factorial axes:

```text
initialization:
- Gaussian packet
- phase-winding Gaussian packet
- two separated packets
- band-limited smooth random field

dt: 1.0, 0.5
stencil: LAP4, LAP8
Phi diffusion timestep semantics: legacy, dt-scaled
```

Total:

```text
4 * 2 * 2 * 2 = 32 runs
32 * 80 * 32 * 32 = 2,621,440 cell-step updates
```

This is not a continuum-limit study. Grid size remained fixed and this source lane has no explicit physical `dx`.

## 6. Independent checks

### 6.1 Vectorized replay

Pass criterion:

```text
max absolute error <= 1e-12
```

Observed: `0.0`.

### 6.2 Scalar replay

A second reconstructor used nested Python scalar loops and did not call the vectorized implementation. Observed maximum error: `0.0`.

### 6.3 Analytic toys

Zero activity:

```text
mu_n = mu_0 * (1 - rho * dt)^n
```

Observed error: `1.1102230246251565e-16`.

Constant unclipped activity:

```text
B = (1 - rho * dt) * (1 + eta * A * kappa * dt)
c = rho * dt
y_n = B^n * y_0 + c * (B^n - 1) / (B - 1)
```

Observed error: `4.440892098500626e-16`.

A high-growth clipping control reached its exact declared cap of `0.5`.

## 7. Negative controls

The current update uses `|Psi|^2` before mode-coupling energy is removed. Reconstructing from the later output state's `|Psi|^2` failed in every run. Saving only ordinary output `Psi` is therefore insufficient for exact replay unless the write-time activity is also recorded or reconstructed.

Reversing the exact activity frames also failed in every run. Current `mu` depends on temporal order, not only an unordered activity total.

## 8. Local verdict

```text
L1_transcribed_reference_status = passed
active_package_import_match = pending
current_mu_informational_independence_from_complete_write_time_Psi_history = absent
current_mu_causal_activity = present
current_mu_practical_redundancy = not established
mu_equals_Phi = untested
```

Permitted statement:

> For the deterministic NumPy path transcribed from the stated source blob, the complete `mu` trajectory is uniquely and exactly reconstructible from the write-time `Psi`-energy history, `kappa`, initial `mu`, and frozen parameters.

Prohibited stronger statements:

- `mu` is physically unreal;
- `mu` is identical to `Phi`;
- `mu` can be deleted without changing closed-loop futures;
- the universe is analog;
- Lineum explains memory, identity, measurement, or consciousness.

## 9. Root-programme impact matrix

| Branch | Relationship | Evidence | Cheapest next discriminator |
|---|---|---|---|
| Current local `mu` as independent information | `contradicts` strong informational independence | Exact reconstruction in two implementations | Direct active-package import receipt |
| Current local `mu` as causal memory state | `supports` | It is read by the update and preserves temporal order | Closed-loop replacement |
| `mu` as practical history compression | `supports` | Full history reproduces it; instantaneous output state does not | Finite-memory and description-length comparison |
| `mu = Phi` or higher-scale `Phi` | `not_yet_compared` | L1 used `Psi` history | L2 `Phi`-only reconstruction |
| Relational or branch-aware `mu` | `constrains` | Current local state has no informational independence from complete write history | Define a relational observable absent from this recurrence |
| Analog/continuum ontology | `unaffected` | No `dx` refinement occurred | Explicit-`dx` reference lane |
| Tree or fractal branching | `unaffected` | No branch observer was used | Define observer before scaling test |
| Eq-11.1 / epsilon / Relic Foam | `unaffected` | Not executed | Preserve their independent provenance gates |
| Root P2 recovery | `unaffected` | Separate memory audit | Recover and replay retained P2 package |
| Research reliability | `supports` adversarial correction | Preregistered algebraic error exposed before promotion | Direct import comparison receipt |

## 10. Open branches and reopen triggers

### O1: direct active-Core receipt

Status: `queued`.

Required:

- clean checkout of `develop`;
- exact commit SHA;
- repository dependencies;
- import `lineum_core.math`;
- execute the same frozen states;
- compare per-step `Psi`, `Phi`, and `mu` with the embedded adapter.

Pass: all declared arrays agree within `1e-12`. A larger difference is `unresolved_divergence`, not evidence for independent `mu`.

### O2: `Phi`-only reduction

Status: `queued_after_O1`.

Test one-, two-, and four-timescale kernels, spatial coarse-graining, finite-lag models, and matched-capacity controls. Freeze fitting before held-out closed-loop replacement.

### O3: finite-history compression

Status: `untested`.

Measure how much `Psi/Phi` history is required before explicit `mu` offers no held-out predictive advantage.

### O4: stochastic robustness

Status: `untested`.

Re-enable stochastic terms with frozen seeds and record the exact pre-coupling activity snapshot. Randomness changes the generated history but not the conditional deterministic recurrence.

### O5: continuum stability

Status: `untested`.

Repeat the reduction in an explicit-`dx` reference model. A representation that works only at one lattice convention is not a scale-independent ontology result.

Reopen L1 if `math.py` changes its write order, activity snapshot, threshold, transport, decay, clipping, `kappa` input, stochastic input, precision, device, or backend; or if the active package diverges from the adapter.

## 11. Next cross-program discriminator

The next required step is not `Phi` fitting yet. It is the smallest missing provenance check:

```text
import the actual active Core from a clean develop checkout
and compare it step-by-step with this frozen adapter.
```

This environment could not obtain a checkout because outbound Git DNS resolution failed. The GitHub connector supplied the source but cannot execute the repository. The result is therefore a transcribed-reference pass, not active-package validation.

After direct equivalence passes, proceed to L2 `Phi`-only reduction. If it fails, resolve the smallest source mismatch before ontology interpretation.

## 12. Environment and machine-readable receipt

```json
{
  "environment": {
    "python": "3.13.5",
    "numpy": "2.3.5",
    "platform": "Linux-6.12.13-x86_64-with-glibc2.41"
  },
  "source_blob_sha": "bb877021810691223a0eb960a45493a2e351112a",
  "matrix": {
    "runs": 32,
    "cell_steps": 2621440,
    "max_vectorized_error": 0.0,
    "max_scalar_error": 0.0,
    "min_wrong_snapshot_error": 2.9026037664164894e-05,
    "max_wrong_snapshot_error": 0.0004817052198928251,
    "min_reversed_history_error": 0.019799097623741123,
    "max_reversed_history_error": 0.14079178162864864,
    "maximum_mu_observed": 0.40871512935012855
  },
  "analytic_checks": {
    "zero_activity_decay_max_error": 1.1102230246251565e-16,
    "constant_activity_closed_form_max_error": 4.440892098500626e-16,
    "clipping_reaches_declared_cap": true
  }
}
```

## 13. Standalone verification code

The following script reproduces the recurrence checks and matrix summary without importing Lineum. It is intentionally a frozen adapter. The direct active-package comparison remains O1.

```python
import json
import platform
import sys
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class Cfg:
    dt: float = 1.0
    psi_diffusion: float = 0.05
    phi_diffusion: float = 0.05
    drift_strength: float = -0.004
    stencil: str = "LAP4"
    phi_dt: bool = False
    mode_strength: float = 0.001
    eta: float = 0.005
    rho: float = 0.0001
    cap: float = 10.0
    cutoff: float = 0.1

def diffuse(f, k, rate, stencil):
    ku, kd = np.roll(k, 1, 0), np.roll(k, -1, 0)
    kl, kr = np.roll(k, 1, 1), np.roll(k, -1, 1)
    fu, fd = np.roll(f, 1, 0), np.roll(f, -1, 0)
    fl, fr = np.roll(f, 1, 1), np.roll(f, -1, 1)
    if stencil == "LAP8":
        kul, kur = np.roll(ku, 1, 1), np.roll(ku, -1, 1)
        kdl, kdr = np.roll(kd, 1, 1), np.roll(kd, -1, 1)
        ful, fur = np.roll(fu, 1, 1), np.roll(fu, -1, 1)
        fdl, fdr = np.roll(fd, 1, 1), np.roll(fd, -1, 1)
        total = fu*ku + fd*kd + fl*kl + fr*kr + 0.25*(ful*kul + fur*kur + fdl*kdl + fdr*kdr)
        active = ku + kd + kl + kr + 0.25*(kul + kur + kdl + kdr)
    else:
        total = fu*ku + fd*kd + fl*kl + fr*kr
        active = ku + kd + kl + kr
    return rate*(total - active*f)

def step(s, c):
    psi = np.asarray(s["psi"], np.complex128).copy()
    phi = np.asarray(s["phi"], np.float64).copy()
    k = np.asarray(s["kappa"], np.float64).copy()
    mu = np.asarray(s["mu"], np.float64).copy()
    mult = 1.0 + mu
    factor = 0.1*np.tanh((0.04*np.clip(phi, 0, 10)*k*mult)/0.1)
    interaction = factor*psi
    interaction /= 1.0 + np.abs(interaction)/10.0
    gx, gy = np.gradient(phi)
    flow = c.drift_strength*(gx + 1j*gy)*k*mult
    flow /= 1.0 + np.abs(flow)/10.0
    psi += flow*c.dt
    psi += interaction*c.dt
    psi -= 0.005*psi*c.dt
    psi += diffuse(psi, k, c.psi_diffusion, c.stencil)*k*c.dt
    e_write = np.abs(psi)**2
    de = c.mode_strength*e_write*k*c.dt
    phi += de
    mag = np.sqrt(np.maximum(e_write - de, 0.0))
    psi = (psi/(np.sqrt(e_write) + 1e-12))*mag
    phi += k*c.phi_diffusion*diffuse(phi, k, 0.05, c.stencil)*(c.dt if c.phi_dt else 1.0)
    phi = np.clip(phi, 0.0, 1e6)
    floor = c.cutoff*np.max(e_write) if 0.0 < c.cutoff < 1.0 else c.cutoff
    active = np.maximum(e_write - floor, 0.0)
    mu += c.eta*active*k*(1.0 + mu)*c.dt
    mu -= c.rho*mu*c.dt
    mu = np.clip(mu, 0.0, c.cap)
    return {"psi": psi, "phi": phi, "kappa": k, "mu": mu}, e_write, np.abs(psi)**2

def replay(hist, k, mu0, c):
    mu = mu0.copy()
    out = []
    for e in hist:
        floor = c.cutoff*np.max(e) if 0.0 < c.cutoff < 1.0 else c.cutoff
        active = np.maximum(e - floor, 0.0)
        mu += c.eta*active*k*(1.0 + mu)*c.dt
        mu -= c.rho*mu*c.dt
        mu = np.clip(mu, 0.0, c.cap)
        out.append(mu.copy())
    return np.asarray(out)

def replay_scalar(hist, k, mu0, c):
    mu = mu0.copy()
    out = []
    for e in hist:
        floor = c.cutoff*float(np.max(e)) if 0.0 < c.cutoff < 1.0 else c.cutoff
        for i in range(mu.shape[0]):
            for j in range(mu.shape[1]):
                m = float(mu[i, j])
                a = max(float(e[i, j]) - floor, 0.0)
                m += c.eta*a*float(k[i, j])*(1.0 + m)*c.dt
                m -= c.rho*m*c.dt
                mu[i, j] = min(max(m, 0.0), c.cap)
        out.append(mu.copy())
    return np.asarray(out)

def init(kind, n=32, seed=1234):
    y, x = np.mgrid[0:n, 0:n]
    q = (n-1)/2
    if kind == "gaussian":
        amp = 1.4*np.exp(-((x-q)**2+(y-q)**2)/(2*(n/8)**2)); phase = 0.0
    elif kind == "winding":
        amp = 1.3*np.exp(-((x-q)**2+(y-q)**2)/(2*(n/7)**2)); phase = np.arctan2(y-q, x-q)
    elif kind == "two_packets":
        amp = 0.9*np.exp(-((x-.32*n)**2+(y-.5*n)**2)/(2*(n/10)**2)) + 0.8*np.exp(-((x-.68*n)**2+(y-.5*n)**2)/(2*(n/10)**2)); phase = .6*np.sin(2*np.pi*x/n)
    else:
        rng = np.random.default_rng(seed)
        z = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
        ky, kx = np.fft.fftfreq(n)[:,None], np.fft.fftfreq(n)[None,:]
        f = np.fft.ifft2(np.fft.fft2(z)*np.exp(-(kx*kx+ky*ky)/(2*.08**2)))
        f /= np.max(np.abs(f)); amp, phase = .8*np.abs(f), np.angle(f)
    return {"psi": amp*np.exp(1j*phase), "phi": np.zeros((n,n)), "kappa": np.ones((n,n)), "mu": np.zeros((n,n))}

def run(kind, c, steps=80):
    s = init(kind); mu0 = s["mu"].copy(); k = s["kappa"].copy()
    ew, eo, mh = [], [], []
    for _ in range(steps):
        s, a, b = step(s, c); ew.append(a); eo.append(b); mh.append(s["mu"].copy())
    ew, eo, mh = np.asarray(ew), np.asarray(eo), np.asarray(mh)
    return {
        "positive": float(np.max(np.abs(replay(ew,k,mu0,c)-mh))),
        "scalar": float(np.max(np.abs(replay_scalar(ew,k,mu0,c)-mh))),
        "wrong_snapshot": float(np.max(np.abs(replay(eo,k,mu0,c)-mh))),
        "reversed": float(np.max(np.abs(replay(ew[::-1],k,mu0,c)-mh))),
        "max_mu": float(np.max(mh)),
    }

rows = []
for dt in (1.0, .5):
    for stencil in ("LAP4", "LAP8"):
        for phi_dt in (False, True):
            c = Cfg(dt=dt, stencil=stencil, phi_dt=phi_dt)
            for kind in ("gaussian", "winding", "two_packets", "smooth_random"):
                rows.append(run(kind, c))

# Independent analytic checks.
c0 = Cfg(dt=.5, rho=.02)
h0 = np.zeros((20,1,1))
g0 = replay(h0, np.ones((1,1)), np.array([[.7]]), c0)[:,0,0]
e0 = np.array([.7*(1-c0.rho*c0.dt)**(n+1) for n in range(20)])
c1 = Cfg(dt=.25, rho=.003, eta=.02, cap=1e9, cutoff=0.0)
h1 = np.full((30,1,1), .4)
g1 = replay(h1, np.ones((1,1)), np.array([[.2]]), c1)[:,0,0]
d = 1-c1.rho*c1.dt; growth = c1.eta*.4*c1.dt; B = d*(1+growth); constant = 1-d
e1 = np.array([B**n*1.2 + constant*(B**n-1)/(B-1) - 1 for n in range(1,31)])

print(json.dumps({
  "environment": {"python": sys.version.split()[0], "numpy": np.__version__, "platform": platform.platform()},
  "runs": len(rows),
  "cell_steps": len(rows)*80*32*32,
  "max_positive": max(r["positive"] for r in rows),
  "max_scalar": max(r["scalar"] for r in rows),
  "wrong_snapshot_range": [min(r["wrong_snapshot"] for r in rows), max(r["wrong_snapshot"] for r in rows)],
  "reversed_range": [min(r["reversed"] for r in rows), max(r["reversed"] for r in rows)],
  "max_mu": max(r["max_mu"] for r in rows),
  "zero_activity_error": float(np.max(np.abs(g0-e0))),
  "constant_activity_error": float(np.max(np.abs(g1-e1)))
}, indent=2))
```

Expected summary:

```json
{
  "runs": 32,
  "cell_steps": 2621440,
  "max_positive": 0.0,
  "max_scalar": 0.0,
  "wrong_snapshot_range": [2.9026037664164894e-05, 0.0004817052198928251],
  "reversed_range": [0.019799097623741123, 0.14079178162864864],
  "max_mu": 0.40871512935012855,
  "zero_activity_error": 1.1102230246251565e-16,
  "constant_activity_error": 4.440892098500626e-16
}
```

## 14. Limitations

1. The active package was not imported directly.
2. Only the deterministic NumPy path was transcribed.
3. The matrix used a `32 x 32` lattice and 80 steps per run.
4. No nonuniform `kappa` family was included.
5. No natural nonzero initial `mu` family was included outside analytic toys.
6. No `Phi`-only model or closed-loop replacement was tested.
7. No stochastic replay, continuum limit, physical-unit calibration, or empirical-universe comparison was performed.
8. Exact zero is expected when two implementations receive the same `float64` inputs; the scalar, analytic, wrong-snapshot, reversed-history, and clipping controls provide sensitivity checks.
9. This is scientific software evidence, not a canonical whitepaper claim.

## 15. Continuous decision ledger

| Date | Decision | Evidence | Status |
|---|---|---|---|
| 2026-07-31 | Preserve the owner reduction intuition as a testable lane | Conceptual parent v0.2.0 | retained |
| 2026-07-31 | Preregister `Psi`-history reconstruction before `Phi` fitting | Immediate predecessor v0.1.0 | retained |
| 2026-07-31 | Reject predecessor first-order `B_n` as exact source recurrence | Sequential in-place growth then decay; analytic check | `falsified_within_domain` |
| 2026-07-31 | Accept exact transcribed-reference reconstruction | 32 runs, two reconstructors, 2,621,440 cell-steps | `supported` |
| 2026-07-31 | Keep active-package equivalence unresolved | Checkout/import unavailable | `queued` |
| 2026-07-31 | Do not infer `mu = Phi` | No `Phi`-only test | `untested` |
| 2026-07-31 | Do not update code or whitepapers | Evidence is local and implementation-scoped | binding |
