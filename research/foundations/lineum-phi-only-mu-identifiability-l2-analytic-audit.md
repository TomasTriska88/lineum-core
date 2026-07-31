# Phi-Only Mu Identifiability L2 Analytic Audit

**Status:** active analytic and frozen-reference result; conditional Phi-only reconstruction supported; global identity not established  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-07-31  
**Scope:** Core-only audit of whether the current local `mu` write state is identifiable from complete consecutive `Phi` observations under the deterministic mode-coupling path. This report derives an exact inverse in the unclipped, known-parameter, invertible-diffusion regime and records counterexamples under clipping and blocked `kappa`. It does not claim that `mu` is physically identical to `Phi`, that explicit `mu` can be removed safely in closed loop, or that nature is analog.  
**Central questions:** Can the write-time `Psi` energy required by the current `mu` recurrence be recovered from consecutive `Phi` frames? Under which implementation conditions is the mapping injective? Which operations destroy the information?  
**Current confidence:** high for the algebraic inverse and frozen numerical checks in the declared uniform-`kappa`, unclipped periodic lane; high that clipping and zero-write regions create non-identifiability; medium for equivalence with a directly imported active package because the current environment could not obtain a fresh local checkout; no empirical claim about the observable universe.

## 1. Answer first

The project-owner intuition receives a conditional, not universal, success.

In the current deterministic mode-coupling path, one `Phi` step contains the same write-time `Psi` energy that drives `mu`. If the `Phi` diffusion step is known and invertible, and no clipping or hidden write blockage occurs, two consecutive `Phi` frames are sufficient to reconstruct that energy and therefore reconstruct `mu` exactly.

Plain picture:

- `Psi` activity pours dye into `Phi`;
- `Phi` diffusion smears the dye afterward;
- when the smearing rule is known and reversible, the pre-smear dye deposit can be recovered;
- the recovered deposit determines the next `mu` state.

However, saturation and blocked write regions act like an overexposed camera or a closed valve. Different incoming signals can then leave the same recorded `Phi` frame. In those regimes, `Phi` alone no longer identifies `mu`.

The scope-safe verdict is:

```text
Phi-only reconstruction of current mu:
supported in the known, unclipped, invertible deterministic lane

global statement mu = Phi:
not established

Phi-only identifiability across clipping or blocked kappa:
falsified by explicit counterexample
```

## 2. Programme coordinates and lineage

Repository and branch:

```text
TomasTriska88/lineum-core
develop
```

Root programme:

```text
path: research/foundations/lineum-continuous-source-cosmology-validation.md
version: 0.4.14
evidence cutoff: 2026-07-29
blob SHA: 3fba3925553cd5596e46c02fa35d1db91523537d
```

Continuity ledger:

```text
path: research/foundations/lineum-root-programme-continuity-and-impact-ledger.md
version: 0.3.0
evidence cutoff: 2026-07-31
blob SHA: 5304874451caf32313ad0e8e3c59e53958698d79
```

Conceptual parent:

```text
research/foundations/lineum-mu-branch-relative-identity-and-entanglement-hypothesis.md
version: 0.2.0
blob SHA: b55bc1639fc8ed6efa7b8286e9113afa88ee298c
```

Preregistration parent:

```text
research/foundations/lineum-mu-phi-reduction-and-continuum-preregistration.md
version: 0.1.0
blob SHA: 16fac63f7659427ee18865fce82fbad0868311bd
```

Immediate predecessor:

```text
research/foundations/lineum-mu-psi-history-reconstruction-l1-audit.md
version: 0.1.0
blob SHA: 7ba9f83cd839a6cd383bf591b9c0b8a59fe4a6f6
```

Active source coordinate used for the frozen transcription:

```text
lineum_core/math.py
blob SHA: bb877021810691223a0eb960a45493a2e351112a
```

ClickUp was not called because the previously returned MCP rate-limit window was still being respected. Git remains the scientific source of truth; operational synchronization remains pending as one batched update.

## 3. Implementation equations

Under current mode coupling, before `Phi` diffusion:

```text
Phi_pre = Phi_n + alpha * E_n
alpha = mode_coupling_strength * kappa * dt
E_n = |Psi|^2 at the write-time snapshot
```

For uniform `kappa = 1`, periodic boundaries, and no clipping, the subsequent diffusion is linear:

```text
Phi_(n+1) = M Phi_pre
M = I + beta s L
beta = phi_diffusion * 0.05 = 0.0025
s = dt when phi_diffusion_scales_with_dt is True, otherwise 1
L = declared LAP4 or LAP8 lattice Laplacian
```

When `M` is invertible:

```text
Phi_pre = M^(-1) Phi_(n+1)
E_n = [M^(-1) Phi_(n+1) - Phi_n] / alpha
```

The recovered `E_n` supplies the exact activity used by the current corrected `mu` recurrence:

```text
q_n = mu_peak_cutoff_ratio * max(E_n)
A_n = max(E_n - q_n, 0)
g_n = mu_eta * A_n * kappa * dt
d = 1 - mu_rho * dt
mu_(n+1) = clip(d * ((1 + g_n) * mu_n + g_n), 0, mu_cap)
```

Therefore consecutive `Phi` frames identify the next `mu` state whenever all inverse assumptions hold.

## 4. Fourier invertibility check

For periodic uniform lattices, `M` is diagonal in Fourier space.

For `LAP4`:

```text
lambda(kx, ky) = 2 cos(kx) + 2 cos(ky) - 4
M_hat = 1 + beta s lambda
```

The minimum tested multiplier was `0.98`, safely separated from zero.

The corresponding declared `LAP8` symbol also produced a minimum tested multiplier of `0.98` in the frozen matrix. Thus the inverse was numerically well conditioned for the tested coefficients.

This does not prove invertibility for arbitrary coefficients, boundaries, structured `kappa`, or future equations.

## 5. Frozen numerical matrix

The test used synthetic smooth positive energy histories so that identifiability of the `Phi -> E -> mu` chain could be isolated from unrelated `Psi` integration details.

Matrix:

```text
grid: 32 x 32
steps per run: 100
stencil: LAP4, LAP8
dt: 1.0, 0.5
phi_diffusion_scales_with_dt: False, True
kappa: uniform 1
initial Phi: zero
initial mu: zero
Phi clipping: inactive
mu parameters: current defaults
random seed: 42
runs: 8
cell-steps: 819,200
```

Observed maxima across the matrix:

```json
{
  "maximum_energy_reconstruction_error": 4.5075054799781356e-14,
  "maximum_mu_reconstruction_error": 2.498001805406602e-16,
  "minimum_diffusion_inverse_multiplier": 0.98,
  "all_mu_errors_below_1e-12": true
}
```

Per-lane maximum `mu` errors ranged from approximately `9.7e-17` to `2.5e-16`.

The energy error is amplified by division by the small mode-coupling coefficient `0.001 * dt`, but the reconstructed thresholded `mu` update remained at floating-point roundoff.

## 6. Counterexamples and information loss

### 6.1 Phi clipping

Take uniform initial `Phi = 0`, `dt = 1`, `mode_coupling_strength = 0.001`, and an artificially low diagnostic `phi_cap = 0.001`.

Two distinct uniform energy fields:

```text
E_1 = 2
E_2 = 20
```

both produce the same clipped output:

```text
Phi_(n+1) = 0.001 everywhere
```

Their maximum `Phi` difference is exactly `0.0`, while their `mu` writes differ because the underlying activities differ.

Therefore clipping makes the `Phi` observation non-injective.

### 6.2 Blocked kappa

Where `kappa = 0`, the current mode-coupling write to `Phi` is zero regardless of local `E_n`. The `mu` write is also multiplied by `kappa` in the current implementation, so the local next `mu` remains unaffected there. However, energy hidden behind `kappa = 0` cannot be inferred from `Phi`, and later changes to `kappa` or a different future model could expose state-history distinctions not recorded in `Phi`.

For structured nonzero `kappa`, the diffusion operator is no longer the simple translation-invariant Fourier multiplier used here. Identifiability then requires a separate operator-rank and conditioning audit.

### 6.3 Unknown parameters or hidden updates

The inverse also fails as an operational reconstruction when any of the following are unknown or unrecorded:

- mode-coupling strength;
- `dt` semantics;
- stencil;
- boundary treatment;
- `kappa` field;
- clipping events;
- external modifications to `Phi`;
- the exact observation point within the update.

## 7. Independent checks

The main inverse used a Fourier-space inversion of the declared linear diffusion operator.

Independent checks included:

1. direct forward replay from the reconstructed energy;
2. exact `mu` replay using the corrected recurrence from the L1 audit;
3. both LAP4 and LAP8 symbols;
4. both legacy and `dt`-scaled `Phi` diffusion semantics;
5. an explicit clipping collision where two distinct energies produced identical `Phi` output.

Pass threshold:

```text
maximum reconstructed mu error <= 1e-12
```

Observed maximum:

```text
2.498001805406602e-16
```

## 8. Local verdict

```text
L2_analytic_unclipped_uniform_kappa_status = supported
Phi_pair_to_write_time_energy = exactly_invertible_within_tested_lane
Phi_history_to_mu = exactly_reconstructible_within_tested_lane
mu_is_literally_Phi = not_established
mu_can_be_deleted_in_closed_loop = untested
Phi_clipping_global_identifiability = falsified_by_counterexample
structured_kappa_identifiability = untested
active_package_import_match = pending
```

Permitted statement:

> In the tested deterministic, unclipped, uniform-`kappa` lane, consecutive `Phi` frames contain enough information to reconstruct the write-time `Psi` energy and the complete current `mu` trajectory to floating-point precision.

Prohibited stronger statements:

- `mu` and `Phi` are the same physical field;
- `mu` is redundant in every reachable state;
- explicit `mu` can be removed without changing future dynamics;
- `Phi` always preserves the full system history;
- the observable universe uses this memory architecture.

## 9. Practical meaning for Lineum

This result moves the ontology question one step downward.

Current `mu` is not required as an independently informative variable in the ideal tested lane because its write driver can be recovered from `Phi` transitions. Yet explicit `mu` may still be the simplest stable state representation:

- reconstructing it from `Phi` requires two frames, exact parameters, and inversion of a spatial operator;
- clipping and hidden operations destroy exact recoverability;
- maintaining `mu` locally avoids repeatedly solving an inverse problem;
- closed-loop replacement may amplify tiny reconstruction errors or alter reachable states.

The next scientific question is therefore no longer merely whether passive `mu` values can be fitted from `Phi`. It is whether a frozen `Phi`-derived state can replace explicit `mu` in the feedback loop without changing future `Psi/Phi` trajectories.

## 10. Root-programme impact matrix

| Programme branch | Relationship | Evidence | Cheapest next discriminator |
|---|---|---|---|
| Current local `mu` as independently informative state | `contradicts` in ideal lane | Exact `Phi`-pair inversion and `mu` replay | Closed-loop replacement |
| `mu` as practical Markov memory | `supports` | Explicit state avoids spatial inverse and stores temporal order | Complexity and perturbation comparison |
| `mu` as higher-scale or slower `Phi` description | `supports` conditionally | `Phi` transitions encode the same write driver | L2 closed-loop replacement across unseen trajectories |
| Literal `mu = Phi` identity | `contradicts` as direct code identity | Distinct update, transport, clipping, and feedback rules | Compare minimal state transformations |
| Independent relational or branch-aware `mu` | `constrains` | Current local `mu` adds no information in ideal lane | Define an observable absent from local history |
| Analog/continuum ontology | `unaffected` | No explicit-`dx` refinement | Continuum reference lane |
| Source/resource accounting | `unaffected` | Inversion tracks information, not energy supply | Explicit stock/debit audit |
| Particle identity and localization | `unaffected` | No object observer was tested | Retained P2 continuation and identity observer |

## 11. Open branches and reopen triggers

Open branches:

- structured positive `kappa` operator rank and conditioning;
- boundaries other than the periodic roll implementation;
- clipping frequency in reachable current-Core trajectories;
- stochastic source with frozen seeds;
- finite-window and learned approximations that do not know exact equations;
- closed-loop replacement of explicit `mu`;
- perturbation growth under repeated inverse reconstruction;
- direct active-package equivalence receipt;
- explicit continuum `dx/dt` reference.

Reopen or weaken the current support if:

- active-Core import diverges from the frozen equations;
- reachable runs frequently trigger `Phi` clipping;
- the structured-`kappa` operator is rank deficient or severely ill conditioned;
- closed-loop substitution diverges despite passive exact reconstruction;
- another current update modifies `Phi` between the declared observation frames.

## 12. Next discriminator

The next lane is L4 closed-loop replacement:

1. run the explicit-`mu` reference trajectory;
2. reconstruct the write driver from consecutive `Phi` frames;
3. replace stored `mu` feedback with the reconstructed state;
4. freeze all parameters and seeds;
5. compare `Psi`, `Phi`, `mu_hat`, stability, and divergence time;
6. repeat on unseen initializations and perturbations;
7. separately test clipping and structured-`kappa` regimes.

Passive equality is not enough. Only closed-loop survival can show practical dynamical redundancy.

## 13. Complete reproduction code

```python
import itertools
import json
import numpy as np


def lap(field, stencil="LAP4"):
    up = np.roll(field, 1, axis=0)
    dn = np.roll(field, -1, axis=0)
    lf = np.roll(field, 1, axis=1)
    rt = np.roll(field, -1, axis=1)
    if stencil == "LAP8":
        ul = np.roll(up, 1, axis=1)
        ur = np.roll(up, -1, axis=1)
        dl = np.roll(dn, 1, axis=1)
        dr = np.roll(dn, -1, axis=1)
        return up + dn + lf + rt + 0.25 * (ul + ur + dl + dr) - 5.0 * field
    return up + dn + lf + rt - 4.0 * field


def phi_step(phi, energy, dt, stencil, scale_with_dt, cap=1e6):
    pre = phi + 0.001 * energy * dt
    scale = dt if scale_with_dt else 1.0
    out = pre + 0.0025 * scale * lap(pre, stencil)
    return np.clip(out, 0.0, cap)


def invert_phi_step(phi_next, stencil, scale):
    n = phi_next.shape[0]
    ky = 2.0 * np.pi * np.fft.fftfreq(n)
    kx = 2.0 * np.pi * np.fft.fftfreq(n)
    k_x, k_y = np.meshgrid(kx, ky)
    if stencil == "LAP4":
        lam = 2.0 * np.cos(k_x) + 2.0 * np.cos(k_y) - 4.0
    else:
        lam = (
            2.0 * np.cos(k_x)
            + 2.0 * np.cos(k_y)
            + 0.5 * np.cos(k_x + k_y)
            + 0.5 * np.cos(k_x - k_y)
            - 5.0
        )
    multiplier = 1.0 + 0.0025 * scale * lam
    pre = np.fft.ifft2(np.fft.fft2(phi_next) / multiplier).real
    return pre, float(np.min(multiplier))


def mu_step(mu, energy, dt):
    floor = 0.1 * np.max(energy)
    active = np.maximum(energy - floor, 0.0)
    growth = 0.005 * active * (1.0 + mu) * dt
    out = mu + growth
    out -= 0.0001 * out * dt
    return np.clip(out, 0.0, 10.0)


def run():
    rng = np.random.default_rng(42)
    rows = []
    for stencil, dt, scale_with_dt in itertools.product(
        ("LAP4", "LAP8"), (1.0, 0.5), (False, True)
    ):
        n = 32
        phi = np.zeros((n, n))
        mu = np.zeros((n, n))
        max_energy_error = 0.0
        max_mu_error = 0.0
        min_multiplier = 1.0
        for _ in range(100):
            raw = rng.normal(size=(n, n))
            spectrum = np.fft.fft2(raw)
            freq = np.fft.fftfreq(n)
            smooth_filter = np.exp(-0.1 * (freq[:, None] ** 2 + freq[None, :] ** 2))
            energy = np.abs(np.fft.ifft2(spectrum * smooth_filter).real)
            energy = 2.0 * energy / np.max(energy)

            phi_next = phi_step(phi, energy, dt, stencil, scale_with_dt)
            pre, multiplier = invert_phi_step(
                phi_next, stencil, dt if scale_with_dt else 1.0
            )
            energy_hat = (pre - phi) / (0.001 * dt)

            mu_next = mu_step(mu, energy, dt)
            mu_hat_next = mu_step(mu, energy_hat, dt)

            max_energy_error = max(
                max_energy_error, float(np.max(np.abs(energy - energy_hat)))
            )
            max_mu_error = max(
                max_mu_error, float(np.max(np.abs(mu_next - mu_hat_next)))
            )
            min_multiplier = min(min_multiplier, multiplier)
            phi = phi_next
            mu = mu_next

        rows.append(
            {
                "stencil": stencil,
                "dt": dt,
                "phi_diffusion_scales_with_dt": scale_with_dt,
                "maximum_energy_error": max_energy_error,
                "maximum_mu_error": max_mu_error,
                "minimum_inverse_multiplier": min_multiplier,
            }
        )

    phi = np.zeros((8, 8))
    collision_a = phi_step(phi, np.full((8, 8), 2.0), 1.0, "LAP4", False, cap=0.001)
    collision_b = phi_step(phi, np.full((8, 8), 20.0), 1.0, "LAP4", False, cap=0.001)

    output = {
        "rows": rows,
        "maximum_energy_error": max(row["maximum_energy_error"] for row in rows),
        "maximum_mu_error": max(row["maximum_mu_error"] for row in rows),
        "minimum_inverse_multiplier": min(row["minimum_inverse_multiplier"] for row in rows),
        "clipping_collision_phi_difference": float(
            np.max(np.abs(collision_a - collision_b))
        ),
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    run()
```

## 14. Machine-readable summary

```json
{
  "status": "conditional_support",
  "runs": 8,
  "cell_steps": 819200,
  "maximum_energy_reconstruction_error": 4.5075054799781356e-14,
  "maximum_mu_reconstruction_error": 2.498001805406602e-16,
  "minimum_diffusion_inverse_multiplier": 0.98,
  "clipping_collision_phi_difference": 0.0,
  "phi_only_identifiable_in_unclipped_uniform_kappa_lane": true,
  "phi_only_globally_identifiable": false,
  "closed_loop_replacement_tested": false,
  "active_package_import_match": "pending"
}
```
