# Mu-Phi History Identifiability L2a Audit

**Status:** active implementation audit result; restricted transcribed-reference `Phi`-history identification passed; unrestricted `Phi`-only identity falsified by a clipping counterexample; direct active-package equivalence, local finite-memory fitting, and closed-loop replacement remain pending  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-07-31  
**Scope:** Core-only analytic and numerical audit of whether the complete spatial `Phi` history identifies the current explicit `mu` trajectory in the deterministic NumPy mode-coupling path. The report distinguishes exact global inversion in a non-saturated uniform-`kappa` regime from local temporal coarse-graining and from unrestricted identification across clipping. It uses a frozen source transcription because a clean active-package checkout could not be imported in this environment. It does not change Core code, select a canonical ontology, test a continuum limit, or make a claim about nature.  
**Central questions:** Does the full spatial `Phi` history retain the write-time `Psi` energy needed to reconstruct `mu`? Is the mapping local or does it require inversion of spatial transport? Which current numerical operations destroy identifiability? Does success imply that `mu` is literally the same field as `Phi`?  
**Current confidence:** high for the analytic invertibility of the declared uniform-`kappa`, known-operator, non-clipped transport map; high for the frozen-reference numerical result over the registered matrix; high that `Phi` clipping destroys unrestricted identification; medium for active-package equivalence pending direct import; low for practical replacement by a compact local kernel; no evidential support for a physical identity between `mu` and `Phi`, a fundamental analog universe, quantum branching, consciousness, or correspondence with nature.

## 1. Answer first

The result is mixed in exactly the useful way.

In the ordinary non-saturated frozen-reference runs, the complete spatial history of `Phi` contained enough information to reconstruct the write-time `Psi` energy and therefore the complete `mu` trajectory. The reconstruction was not a simple local rescaling of `Phi`. It required mathematically undoing the known `Phi` diffusion over the whole lattice at every step.

A useful picture is ink spreading through wet paper:

```text
the deposited ink amount       = write-time Psi energy;
the blurred ink image          = stored Phi after diffusion;
the accumulated groove record  = mu.
```

If the paper response and blur operator are known and the image has not saturated, the original deposited ink can be recovered from the complete image. The recovered deposits then reproduce the groove record.

However, if the paper saturates to the same maximum darkness, two different deposits can leave the same `Phi` image while producing different `mu`. The current implementation therefore supports only a restricted statement:

```text
complete non-saturated Phi history can encode enough information
to reconstruct current mu under a known invertible update;
mu is not literally the Phi array;
Phi history does not identify mu in every allowed current-Core regime.
```

This is implementation-level information accounting. It is not evidence that nature contains either field or that both names denote one physical substance.

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

Preregistration parent:

```text
path: research/foundations/lineum-mu-phi-reduction-and-continuum-preregistration.md
version: 0.1.0
blob SHA: 16fac63f7659427ee18865fce82fbad0868311bd
```

Immediate numerical predecessor:

```text
path: research/foundations/lineum-mu-psi-history-reconstruction-l1-audit.md
version: 0.1.0
blob SHA: 7ba9f83cd839a6cd383bf591b9c0b8a59fe4a6f6
```

Active source coordinate transcribed:

```text
path: lineum_core/math.py
blob SHA: bb877021810691223a0eb960a45493a2e351112a
path represented: deterministic NumPy update;
use_mode_coupling = True;
use_mu = True;
disable_quantum_noise = True.
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
                            +-- lineum-mu-psi-history-reconstruction-l1-audit.md v0.1.0
                                    |
                                    +-- this L2a audit v0.1.0
```

The L1 report queued `Phi` reduction after a direct active-package comparison. That direct import remains required before any result is promoted as active-package validation. The present checkpoint does not waive that gate. It records a narrower analytic consequence and frozen-reference experiment that can be performed without Codex or a clean repository checkout.

ClickUp was not called because the returned MCP rate-limit window remained active. Git remains the scientific source of truth. Operational synchronization is pending as one future batched update.

## 3. Evidence layers

### 3.1 What the implementation computes

Under mode coupling, the current source first adds a local write to `Phi`:

```text
Phi_mid = Phi_n + s * E_n * kappa * dt
```

where:

```text
s   = mode_coupling_strength;
E_n = write-time |Psi|^2 used later by the mu update.
```

It then applies the declared lattice diffusion update and clips the result:

```text
Phi_(n+1) = clip(T[Phi_mid], 0, Phi_cap)
```

Current `mu` is subsequently written from the same `E_n`, after a global relative threshold, through the corrected sequential growth-and-decay recurrence recorded by L1.

### 3.2 What is analytically established

For uniform `kappa = 1`, periodic rolls, known parameters, no clipping, and the current small diffusion coefficient, the linear transport operator `T` is invertible for both tested stencils.

Consequently, the exact full spatial pair:

```text
Phi_n, Phi_(n+1)
```

determines:

```text
Phi_mid = inverse(T)[Phi_(n+1)]
E_n = (Phi_mid - Phi_n) / (s * dt)
```

and the recovered energy sequence determines `mu` through the L1 recurrence.

### 3.3 What was numerically observed

Thirty-two frozen-reference trajectories were executed over the same matrix as L1. Full spatial `Phi` inversion recovered:

```text
Phi_mid maximum error: 2.7755575615628914e-17
write-time energy maximum error: 3.47499806707674e-14
mu maximum error: 2.3869795029440866e-15
```

The errors are below the preregistered `1e-12` equivalence margin.

### 3.4 Interpretation

In the tested regime, `Phi` and `mu` are two different state representations of overlapping history information. `Phi` is a transported cumulative record; `mu` is a thresholded, nonlinear, non-diffusive memory coordinate reconstructed from the deposits encoded in that record.

This supports restricted informational reducibility. It does not support literal array identity or physical ontological identity.

### 3.5 Hypotheses

The following remain hypotheses:

- a compact local temporal kernel can replace the global inverse;
- coarse-grained `Phi` predicts `mu` out of distribution;
- reconstructed `mu` can replace explicit `mu` in closed loop;
- the restricted mapping survives structured `kappa`, clipping, stochasticity, precision changes, and continuum refinement;
- an analog physical carrier exists in nature.

No observable-universe claim was tested.

## 4. Exact restricted inversion

For uniform `kappa = 1`, define:

```text
a = Phi_diffusion * 0.05 * q
q = dt when phi_diffusion_scales_with_dt is True
q = 1 otherwise
```

Before clipping:

```text
Phi_(n+1) = (I + a L) Phi_mid
```

For a periodic `N x N` lattice, the Fourier multiplier for `LAP4` is:

```text
H4(kx, ky) =
1 + a * [2 cos(kx) + 2 cos(ky) - 4]
```

For `LAP8` with diagonal weight `0.25`:

```text
H8(kx, ky) =
1 + a * [
    2 cos(kx)
    + 2 cos(ky)
    + cos(kx) cos(ky)
    - 5
]
```

Across the frozen matrix, the smallest multiplier was:

```text
min H = 0.98
```

It therefore never approached zero. The inverse is:

```text
Phi_mid =
inverse_FFT(FFT(Phi_(n+1)) / H)
```

and:

```text
E_n =
(Phi_mid - Phi_n) /
(mode_coupling_strength * dt)
```

The dynamic threshold and corrected L1 recurrence then reproduce `mu`.

This inverse is global. A value at one cell depends on the complete spatial `Phi` frame after undoing diffusion. Exact success therefore does not establish that `mu` is a simple local running average of `Phi`.

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
mode_coupling_strength: 0.001
mu_eta: 0.005
mu_rho: 0.0001
mu_cap: 10
mu_peak_cutoff_ratio: 0.1
Phi cap: 1e6
```

Factorial axes:

```text
initialization:
- Gaussian packet
- phase-winding Gaussian packet
- two separated packets
- band-limited smooth random field

dt:
- 1.0
- 0.5

stencil:
- LAP4
- LAP8

Phi diffusion timestep semantics:
- legacy per-update
- dt-scaled
```

Total:

```text
runs: 32
cell-step updates: 2,621,440
```

This remains an implementation audit, not a continuum-limit experiment.

## 6. Positive result

The complete spatial `Phi` history was used without access to the stored write-time energy.

For each step:

1. invert the known `Phi` transport operator;
2. subtract the preceding `Phi` frame;
3. divide by the known mode-coupling coefficient and `dt`;
4. constrain tiny numerical negatives to zero;
5. apply the global relative energy threshold;
6. replay the corrected `mu` recurrence.

Pass criterion:

```text
maximum mu error <= 1e-12
```

Observed:

```text
maximum mu error =
2.3869795029440866e-15
```

Restricted classification:

```text
complete_spatial_Phi_history_identifies_current_mu
under_known_unclipped_uniform_kappa_frozen_reference
```

## 7. Sensitivity and negative controls

### 7.1 Omitting spatial deconvolution

A naive reconstruction treated the direct frame difference as the local deposited energy:

```text
E_naive =
(Phi_(n+1) - Phi_n) / (s * dt)
```

This ignores diffusion.

Observed maximum `mu` error range:

```text
0.0016244500172790804
to
0.017295496978526087
```

Therefore exact identification does not come from a trivial temporal difference.

### 7.2 Using the wrong stencil

The inverse was intentionally computed with `LAP8` for a `LAP4` run or vice versa.

Observed maximum `mu` error range:

```text
0.0006345973938056762
to
0.006165845555689109
```

The result depends on the correct spatial operator and is not a generic curve-fitting tautology.

### 7.3 Clipping counterexample

A forced write-stage counterexample used a uniform field, so diffusion was exactly zero:

```text
initial Phi: 0
Phi cap: 0.01
initial mu: 0
kappa: 1
dt: 1
```

Two write-time energies were applied:

```text
E1 = 20
E2 = 30
```

Both produced the same complete one-step `Phi` history:

```text
Phi history 1: [0, 0.01]
Phi history 2: [0, 0.01]
```

but different `mu`:

```text
mu1 = 0.089991
mu2 = 0.1349865
difference = 0.04499550000000001
```

The clipping map discarded the difference between the two deposits.

This is a current-equation forced-state counterexample, not a claim that the frozen natural matrix reached clipping. It proves that unrestricted current-Core `Phi` history does not uniquely determine `mu` across every allowed parameter regime.

## 8. Local verdict

```text
L2a_transcribed_reference_status =
restricted_pass

active_package_import_match =
pending

Phi_array_literal_identity_with_mu =
contradicted_by_different_current_update_roles

complete_spatial_Phi_history_identifies_mu_in_known_unclipped_uniform_kappa_regime =
supported

local_Phi_temporal_kernel_identifies_mu =
untested

Phi_history_identifies_mu_across_clipping =
falsified_by_forced_state_counterexample

current_mu_informational_independence_from_complete_Phi_history_in_restricted_regime =
absent

current_mu_practical_redundancy =
not_established

closed_loop_replacement =
untested

fundamental_analog_ontology =
untested
```

Permitted statement:

> In the deterministic frozen NumPy reference with uniform `kappa`, known mode-coupling and diffusion operators, and no `Phi` clipping, the complete spatial `Phi` history identifies the write-time `Psi` energy and reconstructs the current `mu` trajectory within floating-point precision.

Required qualification:

> This identification is global, operator-dependent, and regime-limited. It fails as a universal statement when `Phi` clipping destroys information.

Prohibited stronger statements:

- `mu` is literally the same array or equation as `Phi`;
- a local running average of `Phi` has already replaced `mu`;
- explicit `mu` can be deleted without changing futures;
- `mu` is physically unreal;
- Lineum is proven analog;
- nature uses the same information pathway;
- branch identity, quantum measurement, consciousness, or a soul has been explained.

## 9. Consequence for the owner hypothesis

The statement "`mu` may be `Phi` at a higher level" now has a supported narrow translation:

```text
in a non-saturated regime,
mu can be reconstructed as a nonlinear memory functional
of deposits recoverable from the complete transported Phi history.
```

It also has an unsupported or falsified stronger translation:

```text
mu is simply equal to the local Phi value
or Phi history always determines mu regardless of information loss.
```

The current evidence therefore favors:

```text
shared_history_representation
```

over:

```text
literal_field_identity
```

within the tested implementation scope.

## 10. Root-programme impact matrix

| Branch | Relationship | Evidence | Cheapest next discriminator |
|---|---|---|---|
| Current local `mu` as independent information | `contradicts` independence in restricted regime | Exact reconstruction from complete spatial `Phi` history | Structured-`kappa` and clipping matrix |
| `mu` as higher-scale or history form of `Phi` | `supports` restricted functional form | Known inverse recovers common write history | Held-out compact-kernel comparison |
| Literal `mu = Phi` | `contradicts` | Different arrays, transport, threshold, decay, and feedback; global inverse required | None needed for current literal implementation |
| Universal `Phi`-only identification | `contradicts` | Clipping collision yields same `Phi` history and different `mu` | Map natural saturation frequency |
| `mu` as practical compact memory | `supports` | Exact `Phi` recovery requires complete frames and operator inversion | Description-length and finite-memory audit |
| Relational or branch-aware `mu` | `constrains` | Current local state is reducible in a restricted ordinary-history regime | Specify a relational observable absent from this pathway |
| Analog/continuum ontology | `unaffected` | No explicit-`dx` refinement | Continuum-reference lane |
| Root source and fuel accounting | `unaffected` | Information reconstruction does not close energy ledger | Explicit stock/debit/return audit |
| Localization and identity | `unaffected` | No object observer or source-off persistence test | Preserve root gates |
| Eq-11.1, epsilon, Relic Foam | `unaffected` | None executed | Preserve separate provenance lanes |
| Research reliability | `supports` adversarial separation | Positive invertible regime and destructive counterexample both retained | Active-package receipt |

## 11. Open branches and reopen triggers

### O1: direct active-package equivalence

Status: `queued`.

A clean checkout must import the actual `lineum_core.math` and compare the frozen adapter step by step. Until then, this report is a transcribed-reference result.

### O2: structured `kappa`

Status: `untested`.

Uniform `kappa` made the transport diagonal in Fourier space. A structured `kappa` requires solving a variable-coefficient linear system and may introduce poorly observed or inaccessible regions.

### O3: natural clipping and finite precision

Status: `untested`.

Map whether ordinary registered trajectories approach `Phi` clipping under declared regimes. Repeat under float32 diagnostics and perturb stored `Phi` frames to measure inversion conditioning.

### O4: compact local and coarse-grained models

Status: `next`.

Fit and freeze:

- instantaneous `Phi`;
- finite local lags;
- one-, two-, and four-timescale exponential memories;
- spatial coarse-graining plus temporal memory;
- matched-capacity nonlinear state-space controls;
- shuffled and time-reversed nulls.

Evaluate held-out initializations, parameter shifts, and seeds. Exact global inversion is the upper-bound information control, not the practical candidate.

### O5: closed-loop replacement

Status: `queued_after_O4`.

Replace explicit feedback with frozen reconstructed `mu_hat`. Passive reconstruction alone does not establish dynamic redundancy.

### O6: continuum and stochastic robustness

Status: `untested`.

Repeat only after an explicit-`dx` reference and stochastic receipts are frozen.

Reopen this verdict if the active Core changes the mode-coupling observation point, `Phi` transport, boundary, clipping, threshold, `kappa`, precision, or `mu` write order; or if direct active-package comparison diverges.

## 12. Next cross-program discriminator

The next useful ChatGPT-executable step is L2b:

```text
Can a compact, local, causal history of Phi approximate mu
on held-out trajectories and remain stable when fed back?
```

The global inverse established that the information is present in the restricted regime. L2b determines whether the owner intuition yields a simple higher-scale state or only a mathematically expensive reconstruction of hidden deposits.

No code or whitepaper change is authorized from L2a.

## 13. Summary machine-readable receipt

```json
{
  "clipping_counterexample": {
    "E1": 20.0,
    "E2": 30.0,
    "mu1": 0.089991,
    "mu2": 0.1349865,
    "mu_difference": 0.04499550000000001,
    "phi_history_1": [
      0.0,
      0.01
    ],
    "phi_history_2": [
      0.0,
      0.01
    ]
  },
  "environment": {
    "numpy": "2.3.5",
    "platform": "Linux-6.12.13-x86_64-with-glibc2.41",
    "python": "3.13.5"
  },
  "matrix": {
    "max_e_write_error": 3.47499806707674e-14,
    "max_mu": 0.40871512935012855,
    "max_mu_from_phi_error": 2.3869795029440866e-15,
    "max_phi": 0.07467055493832993,
    "max_phi_mid_inverse_error": 2.7755575615628914e-17,
    "min_transfer_multiplier": 0.98,
    "naive_mu_error_range": [
      0.0016244500172790804,
      0.017295496978526087
    ],
    "runs": 32,
    "wrong_stencil_mu_error_range": [
      0.0006345973938056762,
      0.006165845555689109
    ]
  },
  "source_blob_sha": "bb877021810691223a0eb960a45493a2e351112a"
}
```

## 14. Complete machine-readable run output

```json
{
  "clipping_counterexample": {
    "energy_1": 20.0,
    "energy_2": 30.0,
    "mu_1": 0.089991,
    "mu_2": 0.1349865,
    "mu_difference": 0.04499550000000001,
    "phi_history_1": [
      0.0,
      0.01
    ],
    "phi_history_2": [
      0.0,
      0.01
    ]
  },
  "environment": {
    "numpy": "2.3.5",
    "platform": "Linux-6.12.13-x86_64-with-glibc2.41",
    "python": "3.13.5"
  },
  "matrix": {
    "cell_steps": 2621440,
    "max_energy_error": 3.47499806707674e-14,
    "max_mu": 0.40871512935012855,
    "max_mu_from_phi_error": 2.3869795029440866e-15,
    "max_phi": 0.07467055493832993,
    "max_phi_mid_inverse_error": 2.7755575615628914e-17,
    "minimum_transport_multiplier": 0.98,
    "naive_mu_error_range": [
      0.0016244500172790804,
      0.017295496978526087
    ],
    "runs": 32,
    "wrong_stencil_mu_error_range": [
      0.0006345973938056762,
      0.006165845555689109
    ]
  },
  "per_run": [
    {
      "dt": 1.0,
      "initialization": "gaussian",
      "max_energy_error": 1.8207657603852567e-14,
      "max_mu": 0.40871512935012855,
      "max_mu_from_phi_error": 1.7763568394002505e-15,
      "max_naive_mu_error": 0.017295496978526087,
      "max_phi": 0.07467055493832993,
      "max_phi_mid_inverse_error": 2.7755575615628914e-17,
      "max_wrong_stencil_mu_error": 0.006165845555689109,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP4"
    },
    {
      "dt": 1.0,
      "initialization": "winding",
      "max_energy_error": 1.509903313490213e-14,
      "max_mu": 0.36581122691600687,
      "max_mu_from_phi_error": 1.4432899320127035e-15,
      "max_naive_mu_error": 0.00873389902633026,
      "max_phi": 0.06902459242741336,
      "max_phi_mid_inverse_error": 2.7755575615628914e-17,
      "max_wrong_stencil_mu_error": 0.0023445768258054667,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP4"
    },
    {
      "dt": 1.0,
      "initialization": "two_packets",
      "max_energy_error": 1.3988810110276972e-14,
      "max_mu": 0.16374061146927463,
      "max_mu_from_phi_error": 8.326672684688674e-16,
      "max_naive_mu_error": 0.005445333753574727,
      "max_phi": 0.037482171001725386,
      "max_phi_mid_inverse_error": 1.3877787807814457e-17,
      "max_wrong_stencil_mu_error": 0.002213707865146186,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP4"
    },
    {
      "dt": 1.0,
      "initialization": "smooth_random",
      "max_energy_error": 1.2476131239225197e-14,
      "max_mu": 0.035773778348163205,
      "max_mu_from_phi_error": 2.498001805406602e-16,
      "max_naive_mu_error": 0.0016244500172790804,
      "max_phi": 0.009733826260815705,
      "max_phi_mid_inverse_error": 3.469446951953614e-18,
      "max_wrong_stencil_mu_error": 0.0006345973938056762,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP4"
    },
    {
      "dt": 1.0,
      "initialization": "gaussian",
      "max_energy_error": 1.8207657603852567e-14,
      "max_mu": 0.40871512935012855,
      "max_mu_from_phi_error": 1.7763568394002505e-15,
      "max_naive_mu_error": 0.017295496978526087,
      "max_phi": 0.07467055493832993,
      "max_phi_mid_inverse_error": 2.7755575615628914e-17,
      "max_wrong_stencil_mu_error": 0.006165845555689109,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP4"
    },
    {
      "dt": 1.0,
      "initialization": "winding",
      "max_energy_error": 1.509903313490213e-14,
      "max_mu": 0.36581122691600687,
      "max_mu_from_phi_error": 1.4432899320127035e-15,
      "max_naive_mu_error": 0.00873389902633026,
      "max_phi": 0.06902459242741336,
      "max_phi_mid_inverse_error": 2.7755575615628914e-17,
      "max_wrong_stencil_mu_error": 0.0023445768258054667,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP4"
    },
    {
      "dt": 1.0,
      "initialization": "two_packets",
      "max_energy_error": 1.3988810110276972e-14,
      "max_mu": 0.16374061146927463,
      "max_mu_from_phi_error": 8.326672684688674e-16,
      "max_naive_mu_error": 0.005445333753574727,
      "max_phi": 0.037482171001725386,
      "max_phi_mid_inverse_error": 1.3877787807814457e-17,
      "max_wrong_stencil_mu_error": 0.002213707865146186,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP4"
    },
    {
      "dt": 1.0,
      "initialization": "smooth_random",
      "max_energy_error": 1.2476131239225197e-14,
      "max_mu": 0.035773778348163205,
      "max_mu_from_phi_error": 2.498001805406602e-16,
      "max_naive_mu_error": 0.0016244500172790804,
      "max_phi": 0.009733826260815705,
      "max_phi_mid_inverse_error": 3.469446951953614e-18,
      "max_wrong_stencil_mu_error": 0.0006345973938056762,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP4"
    },
    {
      "dt": 1.0,
      "initialization": "gaussian",
      "max_energy_error": 1.8207657603852567e-14,
      "max_mu": 0.40666157572825207,
      "max_mu_from_phi_error": 2.3869795029440866e-15,
      "max_naive_mu_error": 0.014871030644824368,
      "max_phi": 0.07426917478339422,
      "max_phi_mid_inverse_error": 2.7755575615628914e-17,
      "max_wrong_stencil_mu_error": 0.006113140521040588,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP8"
    },
    {
      "dt": 1.0,
      "initialization": "winding",
      "max_energy_error": 1.7319479184152442e-14,
      "max_mu": 0.35508942388656783,
      "max_mu_from_phi_error": 2.1094237467877974e-15,
      "max_naive_mu_error": 0.009475113256815159,
      "max_phi": 0.06694496735346522,
      "max_phi_mid_inverse_error": 2.7755575615628914e-17,
      "max_wrong_stencil_mu_error": 0.002315464726645622,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP8"
    },
    {
      "dt": 1.0,
      "initialization": "two_packets",
      "max_energy_error": 1.2878587085651816e-14,
      "max_mu": 0.1583505111269542,
      "max_mu_from_phi_error": 8.326672684688674e-16,
      "max_naive_mu_error": 0.004626815133369433,
      "max_phi": 0.03648280690033631,
      "max_phi_mid_inverse_error": 1.3877787807814457e-17,
      "max_wrong_stencil_mu_error": 0.0021660584548740533,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP8"
    },
    {
      "dt": 1.0,
      "initialization": "smooth_random",
      "max_energy_error": 1.052630205312876e-14,
      "max_mu": 0.036580301923856604,
      "max_mu_from_phi_error": 2.3592239273284576e-16,
      "max_naive_mu_error": 0.0016596577874072948,
      "max_phi": 0.009770435011969562,
      "max_phi_mid_inverse_error": 3.469446951953614e-18,
      "max_wrong_stencil_mu_error": 0.0006432122711719743,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP8"
    },
    {
      "dt": 1.0,
      "initialization": "gaussian",
      "max_energy_error": 1.8207657603852567e-14,
      "max_mu": 0.40666157572825207,
      "max_mu_from_phi_error": 2.3869795029440866e-15,
      "max_naive_mu_error": 0.014871030644824368,
      "max_phi": 0.07426917478339422,
      "max_phi_mid_inverse_error": 2.7755575615628914e-17,
      "max_wrong_stencil_mu_error": 0.006113140521040588,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP8"
    },
    {
      "dt": 1.0,
      "initialization": "winding",
      "max_energy_error": 1.7319479184152442e-14,
      "max_mu": 0.35508942388656783,
      "max_mu_from_phi_error": 2.1094237467877974e-15,
      "max_naive_mu_error": 0.009475113256815159,
      "max_phi": 0.06694496735346522,
      "max_phi_mid_inverse_error": 2.7755575615628914e-17,
      "max_wrong_stencil_mu_error": 0.002315464726645622,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP8"
    },
    {
      "dt": 1.0,
      "initialization": "two_packets",
      "max_energy_error": 1.2878587085651816e-14,
      "max_mu": 0.1583505111269542,
      "max_mu_from_phi_error": 8.326672684688674e-16,
      "max_naive_mu_error": 0.004626815133369433,
      "max_phi": 0.03648280690033631,
      "max_phi_mid_inverse_error": 1.3877787807814457e-17,
      "max_wrong_stencil_mu_error": 0.0021660584548740533,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP8"
    },
    {
      "dt": 1.0,
      "initialization": "smooth_random",
      "max_energy_error": 1.052630205312876e-14,
      "max_mu": 0.036580301923856604,
      "max_mu_from_phi_error": 2.3592239273284576e-16,
      "max_naive_mu_error": 0.0016596577874072948,
      "max_phi": 0.009770435011969562,
      "max_phi_mid_inverse_error": 3.469446951953614e-18,
      "max_wrong_stencil_mu_error": 0.0006432122711719743,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP8"
    },
    {
      "dt": 0.5,
      "initialization": "gaussian",
      "max_energy_error": 3.47499806707674e-14,
      "max_mu": 0.22108857294619622,
      "max_mu_from_phi_error": 1.6375789613221059e-15,
      "max_naive_mu_error": 0.008811407073973653,
      "max_phi": 0.0426325837812352,
      "max_phi_mid_inverse_error": 2.0816681711721685e-17,
      "max_wrong_stencil_mu_error": 0.003827170178872769,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP4"
    },
    {
      "dt": 0.5,
      "initialization": "winding",
      "max_energy_error": 2.6756374893466273e-14,
      "max_mu": 0.18032491554310243,
      "max_mu_from_phi_error": 1.1934897514720433e-15,
      "max_naive_mu_error": 0.005615252203937937,
      "max_phi": 0.037538843693297464,
      "max_phi_mid_inverse_error": 1.3877787807814457e-17,
      "max_wrong_stencil_mu_error": 0.0013556517666749872,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP4"
    },
    {
      "dt": 0.5,
      "initialization": "two_packets",
      "max_energy_error": 2.3037127760972e-14,
      "max_mu": 0.10119361653128855,
      "max_mu_from_phi_error": 8.187894806610529e-16,
      "max_naive_mu_error": 0.0036702799874878122,
      "max_phi": 0.023112307861306448,
      "max_phi_mid_inverse_error": 1.0408340855860843e-17,
      "max_wrong_stencil_mu_error": 0.0014346427329392785,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP4"
    },
    {
      "dt": 0.5,
      "initialization": "smooth_random",
      "max_energy_error": 2.3342439092743916e-14,
      "max_mu": 0.025922379617816332,
      "max_mu_from_phi_error": 3.191891195797325e-16,
      "max_naive_mu_error": 0.0016352437116283342,
      "max_phi": 0.0068491092079795385,
      "max_phi_mid_inverse_error": 3.469446951953614e-18,
      "max_wrong_stencil_mu_error": 0.0006529616660101185,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP4"
    },
    {
      "dt": 0.5,
      "initialization": "gaussian",
      "max_energy_error": 3.47499806707674e-14,
      "max_mu": 0.22108857294619622,
      "max_mu_from_phi_error": 1.8318679906315083e-15,
      "max_naive_mu_error": 0.004560267622606057,
      "max_phi": 0.04319294492105268,
      "max_phi_mid_inverse_error": 2.0816681711721685e-17,
      "max_wrong_stencil_mu_error": 0.0019335332714529996,
      "minimum_transport_multiplier": 0.99,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP4"
    },
    {
      "dt": 0.5,
      "initialization": "winding",
      "max_energy_error": 2.6756374893466273e-14,
      "max_mu": 0.18032491554310243,
      "max_mu_from_phi_error": 1.2490009027033011e-15,
      "max_naive_mu_error": 0.0028579788650792977,
      "max_phi": 0.038068569891793475,
      "max_phi_mid_inverse_error": 1.3877787807814457e-17,
      "max_wrong_stencil_mu_error": 0.0006865272806665936,
      "minimum_transport_multiplier": 0.99,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP4"
    },
    {
      "dt": 0.5,
      "initialization": "two_packets",
      "max_energy_error": 2.3037127760972e-14,
      "max_mu": 0.10119361653128855,
      "max_mu_from_phi_error": 9.298117831235686e-16,
      "max_naive_mu_error": 0.0019322512792219886,
      "max_phi": 0.023423807017461364,
      "max_phi_mid_inverse_error": 1.0408340855860843e-17,
      "max_wrong_stencil_mu_error": 0.0007277064586336398,
      "minimum_transport_multiplier": 0.99,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP4"
    },
    {
      "dt": 0.5,
      "initialization": "smooth_random",
      "max_energy_error": 2.3342439092743916e-14,
      "max_mu": 0.025922379617816332,
      "max_mu_from_phi_error": 3.7470027081099033e-16,
      "max_naive_mu_error": 0.0008379220710673907,
      "max_phi": 0.006990500742477862,
      "max_phi_mid_inverse_error": 3.469446951953614e-18,
      "max_wrong_stencil_mu_error": 0.00032978778872021895,
      "minimum_transport_multiplier": 0.99,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP4"
    },
    {
      "dt": 0.5,
      "initialization": "gaussian",
      "max_energy_error": 3.175237850427948e-14,
      "max_mu": 0.21816676818277894,
      "max_mu_from_phi_error": 1.7486012637846216e-15,
      "max_naive_mu_error": 0.007840455582516865,
      "max_phi": 0.04201594719256962,
      "max_phi_mid_inverse_error": 2.0816681711721685e-17,
      "max_wrong_stencil_mu_error": 0.0037901810504347714,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP8"
    },
    {
      "dt": 0.5,
      "initialization": "winding",
      "max_energy_error": 2.403632848313464e-14,
      "max_mu": 0.17309189547775303,
      "max_mu_from_phi_error": 1.3461454173580023e-15,
      "max_naive_mu_error": 0.005906850906843453,
      "max_phi": 0.03595428817424389,
      "max_phi_mid_inverse_error": 1.3877787807814457e-17,
      "max_wrong_stencil_mu_error": 0.001347548279605259,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP8"
    },
    {
      "dt": 0.5,
      "initialization": "two_packets",
      "max_energy_error": 2.042810365310288e-14,
      "max_mu": 0.0975578050973563,
      "max_mu_from_phi_error": 7.632783294297951e-16,
      "max_naive_mu_error": 0.003298980747642982,
      "max_phi": 0.0224113912324224,
      "max_phi_mid_inverse_error": 1.0408340855860843e-17,
      "max_wrong_stencil_mu_error": 0.0014153510778722044,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP8"
    },
    {
      "dt": 0.5,
      "initialization": "smooth_random",
      "max_energy_error": 2.0872192862952943e-14,
      "max_mu": 0.025995791900860984,
      "max_mu_from_phi_error": 3.3306690738754696e-16,
      "max_naive_mu_error": 0.0016416749259012126,
      "max_phi": 0.0068370624510707025,
      "max_phi_mid_inverse_error": 3.469446951953614e-18,
      "max_wrong_stencil_mu_error": 0.0006570932787762564,
      "minimum_transport_multiplier": 0.98,
      "phi_diffusion_scales_with_dt": false,
      "stencil": "LAP8"
    },
    {
      "dt": 0.5,
      "initialization": "gaussian",
      "max_energy_error": 3.175237850427948e-14,
      "max_mu": 0.21816676818277894,
      "max_mu_from_phi_error": 1.7208456881689926e-15,
      "max_naive_mu_error": 0.004066444068802384,
      "max_phi": 0.04267450557072934,
      "max_phi_mid_inverse_error": 2.0816681711721685e-17,
      "max_wrong_stencil_mu_error": 0.0019172144908863593,
      "minimum_transport_multiplier": 0.99,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP8"
    },
    {
      "dt": 0.5,
      "initialization": "winding",
      "max_energy_error": 2.403632848313464e-14,
      "max_mu": 0.17309189547775303,
      "max_mu_from_phi_error": 1.3322676295501878e-15,
      "max_naive_mu_error": 0.0029877053903196734,
      "max_phi": 0.0365057412275687,
      "max_phi_mid_inverse_error": 1.3877787807814457e-17,
      "max_wrong_stencil_mu_error": 0.0006822251856148371,
      "minimum_transport_multiplier": 0.99,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP8"
    },
    {
      "dt": 0.5,
      "initialization": "two_packets",
      "max_energy_error": 2.042810365310288e-14,
      "max_mu": 0.0975578050973563,
      "max_mu_from_phi_error": 7.632783294297951e-16,
      "max_naive_mu_error": 0.0017315976679136836,
      "max_phi": 0.022746349986732514,
      "max_phi_mid_inverse_error": 1.0408340855860843e-17,
      "max_wrong_stencil_mu_error": 0.0007178072272703568,
      "minimum_transport_multiplier": 0.99,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP8"
    },
    {
      "dt": 0.5,
      "initialization": "smooth_random",
      "max_energy_error": 2.0872192862952943e-14,
      "max_mu": 0.025995791900860984,
      "max_mu_from_phi_error": 3.191891195797325e-16,
      "max_naive_mu_error": 0.000841285167955559,
      "max_phi": 0.006979935822364506,
      "max_phi_mid_inverse_error": 3.469446951953614e-18,
      "max_wrong_stencil_mu_error": 0.0003318249349787652,
      "minimum_transport_multiplier": 0.99,
      "phi_diffusion_scales_with_dt": true,
      "stencil": "LAP8"
    }
  ]
}
```

## 15. Standalone verification code

The following program reproduces the frozen matrix, exact inverse, negative controls, clipping counterexample, and machine-readable output without importing Lineum. It is intentionally a frozen adapter. Direct active-package comparison remains O1.

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
    mu_cap: float = 10.0
    cutoff: float = 0.1
    phi_cap: float = 1e6

def diffuse(field, kappa, rate, stencil):
    ku, kd = np.roll(kappa, 1, 0), np.roll(kappa, -1, 0)
    kl, kr = np.roll(kappa, 1, 1), np.roll(kappa, -1, 1)
    fu, fd = np.roll(field, 1, 0), np.roll(field, -1, 0)
    fl, fr = np.roll(field, 1, 1), np.roll(field, -1, 1)
    if stencil == "LAP8":
        kul, kur = np.roll(ku, 1, 1), np.roll(ku, -1, 1)
        kdl, kdr = np.roll(kd, 1, 1), np.roll(kd, -1, 1)
        ful, fur = np.roll(fu, 1, 1), np.roll(fu, -1, 1)
        fdl, fdr = np.roll(fd, 1, 1), np.roll(fd, -1, 1)
        total = (
            fu * ku + fd * kd + fl * kl + fr * kr
            + 0.25 * (ful * kul + fur * kur + fdl * kdl + fdr * kdr)
        )
        active = ku + kd + kl + kr + 0.25 * (kul + kur + kdl + kdr)
    else:
        total = fu * ku + fd * kd + fl * kl + fr * kr
        active = ku + kd + kl + kr
    return rate * (total - active * field)

def step(state, cfg):
    psi = np.asarray(state["psi"], np.complex128).copy()
    phi = np.asarray(state["phi"], np.float64).copy()
    kappa = np.asarray(state["kappa"], np.float64).copy()
    mu = np.asarray(state["mu"], np.float64).copy()
    phi_before = phi.copy()

    multiplier = 1.0 + mu
    factor = 0.1 * np.tanh(
        (0.04 * np.clip(phi, 0.0, 10.0) * kappa * multiplier) / 0.1
    )
    interaction = factor * psi
    interaction /= 1.0 + np.abs(interaction) / 10.0

    gx, gy = np.gradient(phi)
    flow = cfg.drift_strength * (gx + 1j * gy) * kappa * multiplier
    flow /= 1.0 + np.abs(flow) / 10.0

    psi += flow * cfg.dt
    psi += interaction * cfg.dt
    psi -= 0.005 * psi * cfg.dt
    psi += (
        diffuse(psi, kappa, cfg.psi_diffusion, cfg.stencil)
        * kappa
        * cfg.dt
    )
    e_write = np.abs(psi) ** 2

    delta_e = cfg.mode_strength * e_write * kappa * cfg.dt
    phi_mid = phi + delta_e
    psi_mag = np.sqrt(np.maximum(e_write - delta_e, 0.0))
    psi = (psi / (np.sqrt(e_write) + 1e-12)) * psi_mag

    phi_scale = cfg.dt if cfg.phi_dt else 1.0
    phi = (
        phi_mid
        + kappa
        * cfg.phi_diffusion
        * diffuse(phi_mid, kappa, 0.05, cfg.stencil)
        * phi_scale
    )
    phi = np.clip(phi, 0.0, cfg.phi_cap)

    floor = (
        cfg.cutoff * np.max(e_write)
        if 0.0 < cfg.cutoff < 1.0
        else cfg.cutoff
    )
    active = np.maximum(e_write - floor, 0.0)
    mu += cfg.eta * active * kappa * (1.0 + mu) * cfg.dt
    mu -= cfg.rho * mu * cfg.dt
    mu = np.clip(mu, 0.0, cfg.mu_cap)

    return {
        "psi": psi,
        "phi": phi,
        "kappa": kappa,
        "mu": mu,
    }, {
        "phi_before": phi_before,
        "phi_mid": phi_mid,
        "e_write": e_write,
    }

def replay_mu(energy_history, kappa, mu0, cfg):
    mu = mu0.copy()
    output = []
    for energy in energy_history:
        floor = (
            cfg.cutoff * np.max(energy)
            if 0.0 < cfg.cutoff < 1.0
            else cfg.cutoff
        )
        active = np.maximum(energy - floor, 0.0)
        mu += cfg.eta * active * kappa * (1.0 + mu) * cfg.dt
        mu -= cfg.rho * mu * cfg.dt
        mu = np.clip(mu, 0.0, cfg.mu_cap)
        output.append(mu.copy())
    return np.asarray(output)

def inverse_phi_transport(phi_after, cfg):
    n = phi_after.shape[0]
    ky = 2.0 * np.pi * np.fft.fftfreq(n)[:, None]
    kx = 2.0 * np.pi * np.fft.fftfreq(n)[None, :]
    if cfg.stencil == "LAP8":
        laplace_symbol = (
            2.0 * np.cos(kx)
            + 2.0 * np.cos(ky)
            + np.cos(kx) * np.cos(ky)
            - 5.0
        )
    else:
        laplace_symbol = (
            2.0 * np.cos(kx)
            + 2.0 * np.cos(ky)
            - 4.0
        )
    alpha = (
        cfg.phi_diffusion
        * 0.05
        * (cfg.dt if cfg.phi_dt else 1.0)
    )
    multiplier = 1.0 + alpha * laplace_symbol
    phi_mid = np.fft.ifft2(
        np.fft.fft2(phi_after) / multiplier
    ).real
    return phi_mid, float(np.min(multiplier))

def initial_state(kind, n=32, seed=1234):
    y, x = np.mgrid[0:n, 0:n]
    center = (n - 1) / 2.0
    if kind == "gaussian":
        amp = 1.4 * np.exp(
            -((x-center)**2 + (y-center)**2) / (2.0 * (n/8.0)**2)
        )
        phase = 0.0
    elif kind == "winding":
        amp = 1.3 * np.exp(
            -((x-center)**2 + (y-center)**2) / (2.0 * (n/7.0)**2)
        )
        phase = np.arctan2(y-center, x-center)
    elif kind == "two_packets":
        amp = (
            0.9 * np.exp(
                -((x-.32*n)**2 + (y-.5*n)**2) / (2.0*(n/10.0)**2)
            )
            + 0.8 * np.exp(
                -((x-.68*n)**2 + (y-.5*n)**2) / (2.0*(n/10.0)**2)
            )
        )
        phase = 0.6 * np.sin(2.0 * np.pi * x / n)
    else:
        rng = np.random.default_rng(seed)
        z = (
            rng.normal(size=(n, n))
            + 1j * rng.normal(size=(n, n))
        )
        ky = np.fft.fftfreq(n)[:, None]
        kx = np.fft.fftfreq(n)[None, :]
        smooth = np.fft.ifft2(
            np.fft.fft2(z)
            * np.exp(-(kx*kx + ky*ky) / (2.0 * .08**2))
        )
        smooth /= np.max(np.abs(smooth))
        amp, phase = 0.8 * np.abs(smooth), np.angle(smooth)
    return {
        "psi": amp * np.exp(1j * phase),
        "phi": np.zeros((n, n)),
        "kappa": np.ones((n, n)),
        "mu": np.zeros((n, n)),
    }

def run(kind, cfg, steps=80):
    state = initial_state(kind)
    kappa = state["kappa"].copy()
    mu0 = state["mu"].copy()
    phi_history = [state["phi"].copy()]
    true_energy = []
    true_mu = []
    inverse_errors = []
    energy_errors = []
    multipliers = []

    for _ in range(steps):
        state, receipt = step(state, cfg)
        phi_history.append(state["phi"].copy())
        true_energy.append(receipt["e_write"])
        true_mu.append(state["mu"].copy())
        phi_mid, minimum = inverse_phi_transport(state["phi"], cfg)
        energy = (
            phi_mid - receipt["phi_before"]
        ) / (cfg.mode_strength * cfg.dt)
        inverse_errors.append(
            np.max(np.abs(phi_mid - receipt["phi_mid"]))
        )
        energy_errors.append(
            np.max(np.abs(energy - receipt["e_write"]))
        )
        multipliers.append(minimum)

    true_mu = np.asarray(true_mu)
    phi_history = np.asarray(phi_history)

    recovered_energy = []
    for index in range(steps):
        phi_mid, _ = inverse_phi_transport(
            phi_history[index + 1], cfg
        )
        recovered_energy.append(
            np.maximum(
                (
                    phi_mid - phi_history[index]
                ) / (cfg.mode_strength * cfg.dt),
                0.0,
            )
        )
    recovered_mu = replay_mu(
        np.asarray(recovered_energy), kappa, mu0, cfg
    )

    naive_energy = np.maximum(
        (
            phi_history[1:] - phi_history[:-1]
        ) / (cfg.mode_strength * cfg.dt),
        0.0,
    )
    naive_mu = replay_mu(naive_energy, kappa, mu0, cfg)

    wrong_cfg = Cfg(
        **{
            **cfg.__dict__,
            "stencil": (
                "LAP8" if cfg.stencil == "LAP4" else "LAP4"
            ),
        }
    )
    wrong_energy = []
    for index in range(steps):
        phi_mid, _ = inverse_phi_transport(
            phi_history[index + 1], wrong_cfg
        )
        wrong_energy.append(
            np.maximum(
                (
                    phi_mid - phi_history[index]
                ) / (cfg.mode_strength * cfg.dt),
                0.0,
            )
        )
    wrong_mu = replay_mu(
        np.asarray(wrong_energy), kappa, mu0, cfg
    )

    return {
        "initialization": kind,
        "dt": cfg.dt,
        "stencil": cfg.stencil,
        "phi_diffusion_scales_with_dt": cfg.phi_dt,
        "max_phi_mid_inverse_error": float(max(inverse_errors)),
        "max_energy_error": float(max(energy_errors)),
        "max_mu_from_phi_error": float(
            np.max(np.abs(recovered_mu - true_mu))
        ),
        "max_naive_mu_error": float(
            np.max(np.abs(naive_mu - true_mu))
        ),
        "max_wrong_stencil_mu_error": float(
            np.max(np.abs(wrong_mu - true_mu))
        ),
        "minimum_transport_multiplier": float(min(multipliers)),
        "max_mu": float(np.max(true_mu)),
        "max_phi": float(np.max(phi_history)),
    }

rows = []
for dt in (1.0, 0.5):
    for stencil in ("LAP4", "LAP8"):
        for phi_dt in (False, True):
            cfg = Cfg(dt=dt, stencil=stencil, phi_dt=phi_dt)
            for kind in (
                "gaussian",
                "winding",
                "two_packets",
                "smooth_random",
            ):
                rows.append(run(kind, cfg))

def clipping_witness(energy, phi_cap=0.01):
    cfg = Cfg(phi_cap=phi_cap)
    phi_out = min(
        max(cfg.mode_strength * energy * cfg.dt, 0.0),
        phi_cap,
    )
    active = max(energy - cfg.cutoff * energy, 0.0)
    mu = cfg.eta * active * cfg.dt
    mu -= cfg.rho * mu * cfg.dt
    return phi_out, mu

phi1, mu1 = clipping_witness(20.0)
phi2, mu2 = clipping_witness(30.0)

output = {
    "environment": {
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "platform": platform.platform(),
    },
    "matrix": {
        "runs": len(rows),
        "cell_steps": len(rows) * 80 * 32 * 32,
        "max_phi_mid_inverse_error": max(
            row["max_phi_mid_inverse_error"] for row in rows
        ),
        "max_energy_error": max(
            row["max_energy_error"] for row in rows
        ),
        "max_mu_from_phi_error": max(
            row["max_mu_from_phi_error"] for row in rows
        ),
        "naive_mu_error_range": [
            min(row["max_naive_mu_error"] for row in rows),
            max(row["max_naive_mu_error"] for row in rows),
        ],
        "wrong_stencil_mu_error_range": [
            min(
                row["max_wrong_stencil_mu_error"]
                for row in rows
            ),
            max(
                row["max_wrong_stencil_mu_error"]
                for row in rows
            ),
        ],
        "minimum_transport_multiplier": min(
            row["minimum_transport_multiplier"] for row in rows
        ),
        "max_mu": max(row["max_mu"] for row in rows),
        "max_phi": max(row["max_phi"] for row in rows),
    },
    "clipping_counterexample": {
        "energy_1": 20.0,
        "energy_2": 30.0,
        "phi_history_1": [0.0, phi1],
        "phi_history_2": [0.0, phi2],
        "mu_1": mu1,
        "mu_2": mu2,
        "mu_difference": abs(mu2 - mu1),
    },
    "per_run": rows,
}
print(json.dumps(output, indent=2, sort_keys=True))
```

## 16. Limitations

1. The active package was not directly imported.
2. The deterministic NumPy source path was transcribed from the stated blob.
3. Only uniform `kappa = 1` was used in the natural trajectory matrix.
4. Exact inversion used the complete spatial `Phi` frame and exact operator parameters.
5. The natural matrix did not reach `Phi` clipping; clipping was tested with a forced write-stage counterexample.
6. No finite local memory model was fitted.
7. No held-out model selection, closed-loop replacement, or intervention was executed.
8. No stochastic path, float32 robustness, structured `kappa`, explicit-`dx` continuum limit, or physical calibration was tested.
9. Inversion accuracy does not imply numerical robustness under measurement noise.
10. No empirical evidence about the observable universe was used or produced.
11. The result does not promote any hypothesis into Core code or whitepapers.

## 17. Continuous decision ledger

| Date | Decision | Evidence | Status |
|---|---|---|---|
| 2026-07-31 | Preserve `mu` as possible higher-scale `Phi` | Owner hypothesis and conceptual parent | retained |
| 2026-07-31 | Use complete spatial `Phi` history as the information upper bound | Frozen L2a design | retained |
| 2026-07-31 | Accept exact restricted `Phi`-history reconstruction | 32 runs; maximum `mu` error `2.3869795029440866e-15` | `supported` |
| 2026-07-31 | Reject trivial local frame difference as exact | Naive-control errors up to `0.017295496978526087` | `unsupported_under_tested_conditions` |
| 2026-07-31 | Require correct spatial operator | Wrong-stencil errors up to `0.006165845555689109` | binding |
| 2026-07-31 | Reject universal `Phi`-history identification | Same clipped `Phi` history, different `mu` | `falsified_within_allowed_clipping_domain` |
| 2026-07-31 | Keep practical local reduction unresolved | No compact model or closed-loop test | `untested` |
| 2026-07-31 | Keep active-package match unresolved | Clean import unavailable | `queued` |
| 2026-07-31 | Do not update code or whitepapers | Evidence remains implementation-scoped | binding |
