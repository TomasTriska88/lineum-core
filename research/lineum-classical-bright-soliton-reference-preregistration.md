# Classical Reference Before Lineum Emergence — Reciprocal Exchange First

**Status:** validated homogeneous Core snapshot; spatial comparison and repair not started  
**Version:** 0.9.0  
**Evidence cutoff:** 2026-08-06  
**Repository / branch / base:** `TomasTriska88/lineum-core` / `develop` / `1b7510fed36d6dc82beba65e0ba9e3cdcdf983b1`  
**Report path:** `research/lineum-classical-bright-soliton-reference-preregistration.md`  
**Confidence:** conventional reference and exact homogeneous scalar snapshot `robust_within_tested_domain`; no wider mechanism or real-physics connection established

## Plain conclusion

The official homogeneous primary and the separately written checker agree with **zero mismatches**. In this exact reduction, `psi` falls and later exceeds its initial energy, but `phi` never decreases and the declared `E+phi` ledger grows by millions. This is not a demonstrated return of stored quantity from `phi` to `psi`.

The ablations isolate why:

- explicit mode transfer is one-way but approximately ledger-conserving: `psi -> phi`;
- separate `phi -> psi` feedback increases `psi` without debiting `phi`;
- dissipation removes quantity without crediting the reservoir;
- the external `phi` cap changes retained `phi`, but did not cause the `psi` recovery in this lane.

Therefore, visual or scalar recovery of `psi` is not sufficient evidence for a reciprocal cycle or full-state recovery. This is a verified negative accounting result for the homogeneous deterministic snapshot, not a falsification of spatial Lineum.

The owner direction remains `owner_provided_pre_hypothesis`: established science first; Lineum emergence only at the smallest missing function; keep this single report; do not assume a soliton is the answer.

## Immutable provenance

```text
executable checkpoint commit = 2fd4554cffcfb65ac30258c76bf41a6022ea5589
executable report blob = befbcee6e15ca94324017051684e4c57ca5678dc
retained-primary commit = 1b7510fed36d6dc82beba65e0ba9e3cdcdf983b1
retained-primary report blob = 0d303e88324a0821a21fbdbd7ecf6442d5c83101
primary JSON bytes / SHA-256 = 23054 / fb05d61caeb2cfa14f9a8581b73304aefd4b67ee19c6ef8a6f7a12533c55c0ba
source-audited Core commit = f1bd74ec2cb62d3b8d56bda05f524c6f63ab9775
lineum_core/math.py blob = bb877021810691223a0eb960a45493a2e351112a
physics-contract test blob = 7acbb8a1c5ff85a5b24970d216aa2a08111b0941
primary source SHA-256 = 242b6d05cef2e1026e23cabbcc0bfc0d5499f155f1c72f5229475da9f5b806e9
checker source SHA-256 = 34a0fd5583609b59d430805b3d0d048cdcdff4e311cadb45cf98f408c4233a5b
```

The complete executable package and official primary remain losslessly available in this report's immutable earlier commits. Version `0.9.0` adds only the exact checker evidence below, avoiding recursive duplication of already compressed data. No equation, lane, threshold, output, or interpretation changed.

## Current implementation represented by the snapshot

```text
phi_local = clip(phi,0,10)
s = 0.1*tanh(0.4*phi_local)
q = s*psi/(1+abs(s*psi)/10)
psi <- psi+q                  [feedback; no phi debit]
psi <- 0.995*psi              [dissipation; no reservoir credit]
E_pre = abs(psi)^2
delta_e = 0.001*E_pre
phi <- phi+delta_e            [explicit one-way mode transfer]
abs(psi) <- sqrt(max(E_pre-delta_e,0))
phi <- clip(phi,0,phi_cap)     [external cap]
```

Uniform fields, `kappa=1`, `mu=0`, `delta=0`, disabled noise, and `dt=1` remove gradients, diffusion, spatial transport, linons, and fluctuations. The surviving multipliers are real and positive, so this reduction has no second relative-phase carrier and cannot instantiate conventional coherent R0 return. The existing Core mode-coupling test checks positive finite `phi_gain`; it does not assert reverse debit, closed full-step accounting, recurrence, or full-state return.

## Verified official observations

| Lane | Verified classification | Recovery | True return | Final `E` | Final `phi` | Final ledger |
|---|---|---:|---:|---:|---:|---:|
| `C0_full_default_cap` | `apparent_energy_recovery_without_reciprocal_ledger` | step `701` | no | `2900150.257034308` | `1000000.0` | `3900150.257034308` |
| `C0b_full_cap_free` | `apparent_energy_recovery_without_reciprocal_ledger` | step `701` | no | `2900150.257034308` | `2359502.643825432` | `5259652.90085974` |
| `C1_no_phi_feedback` | `dissipative_one_way_accumulation` | no | no | `2.650267646912908e-10` | `0.0902893517688856` | `0.09028935203391236` |
| `C2_mode_transfer_only` | `one_way_conserved_transfer` | no | no | `0.13519992446823598` | `0.8648000730057612` | `0.9999999974739973` |
| `C3_phi_feedback_only_seeded` | `unpaired_feedback_source` | no | no | `1482693.5590557144` | `1.0` | `1482694.5590557144` |
| `C4_dissipation_only` | `dissipative_sink` | no | no | `4.427529784808337e-05` | `0` | `4.427529784808337e-05` |
| `C5_no_terms_null` | `stationary_null` | no | no | `1.0` | `0` | `1.0` |

Additional discriminators:

- Full-lane minimum `E=0.23353976762645046` at step `350`.
- `phi_decrease_count=0`; first default-cap contact was step `1521`.
- Cap and cap-free lanes have identical final `psi` energy; only retained `phi` and ledger differ.
- Mode-transfer-only ledger drift was `2.5260027403106733e-09`; phase drift `0`.
- Feedback-only seeded lane held `phi=1` while final `E=1482693.5590557144`.

## Independent checker

The checker was invoked exactly once after the primary was committed, without rerunning or importing the primary solver:

```text
started UTC = 2026-08-06T15:22:30.859836+00:00
finished UTC = 2026-08-06T15:22:31.517766+00:00
elapsed seconds = 0.6579304010010674
return code = 0
checker source SHA-256 = 34a0fd5583609b59d430805b3d0d048cdcdff4e311cadb45cf98f408c4233a5b
primary input SHA-256 = fb05d61caeb2cfa14f9a8581b73304aefd4b67ee19c6ef8a6f7a12533c55c0ba
checker bytes / SHA-256 = 352 / 81cb30ba92ac3848095582afadde4fb9c24ac6138928e21c1eb3553f6d023adc
stdout = passed=True mismatches=0
stderr bytes = 0
primary rerun = false
```

```json
{"independence":{"active_core_runtime_adapter":false,"closed_form_dissipation_control":true,"imports_primary":false,"separate_scalar_replay":true},"mismatches":[],"passed":true,"schema":"lineum-core-homogeneous-check/1","source_sha256":"fc3e27e577359d4700d99793a0cab43afd37ee7162155e62754582af12928cb7"}
```

The checker separately replays the scalar map and dissipation closed form. It reports `passed=true`, `mismatches=[]`, `imports_primary=false`, `separate_scalar_replay=true`, and `active_core_runtime_adapter=false`.

## Evidence boundary

1. **Current implementation:** one-way accounted transfer, feedback amplification without paired `phi` debit, separate dissipation, and an external cap.
2. **Reproducible observation:** one primary and one independent checker agree with zero mismatches; recovery occurred with zero `phi` decreases and multimillion ledger growth.
3. **Cautious interpretation:** `psi` recovery alone is non-identifying and is not reciprocal full-state return in this snapshot.
4. **Hypothesis:** spatial gradients, diffusion, locality, or another term could change the classification; none is tested here.
5. **Known physics:** the conventional model supplies accounting vocabulary only. No laboratory, quantum, gravitational, dark-matter, cosmological, consciousness, or ontological connection is established.

The result is `robust_within_tested_domain` for the exact homogeneous deterministic scalar snapshot and declared ledger. It is not `mechanistically_supported`, `empirically_connected`, or a verdict on wider Lineum. Available NumPy `2.3.5` remains outside repository requirement `<2.0`.

## Lossless checker envelope

```python
from pathlib import Path
import base64,hashlib,json,lzma
s=Path('report.md').read_text();h='<!-- CHECKER-XZ bytes=';i=s.rindex(h)+len(h);j=s.index(' sha256=',i);e=s.index(' -->',j)
size=int(s[i:j]);sha=s[j+8:e];a=s.index('```base64',e)+len('```base64');b=s.index('```',a)
c=base64.b64decode(''.join(s[a:b].split()));assert len(c)==size and hashlib.sha256(c).hexdigest()==sha
env=json.loads(lzma.decompress(c));out=Path('checker-evidence');out.mkdir(exist_ok=True)
for n,m in env['members'].items():
 d=base64.b64decode(m['base64']);assert len(d)==m['bytes'] and hashlib.sha256(d).hexdigest()==m['sha256'];(out/n).write_bytes(d)
```

```text
compressed checker envelope bytes / SHA-256 = 1804 / dfcf7b9b9b05003d1beb10923579d5b9ab976eee2a9104f683faeeafbf472111
checker JSON bytes / SHA-256 = 352 / 81cb30ba92ac3848095582afadde4fb9c24ac6138928e21c1eb3553f6d023adc
checker execution bytes / SHA-256 = 1228 / 652cb6701f50f37341cb485463ca95cf7b0d8f762f4d4e89a4746f93e771cf5c
```

## Exact next scientific gate

Do **not** insert a reciprocal repair yet. The cheapest next discriminator remains in this same report: preregister a minimal spatial ablation that separately activates `phi` gradient forcing, `phi` diffusion, and local nonlinear interaction while preserving explicit source/sink accounting. It must determine whether spatial transport merely redistributes the same unpaired amplification or introduces a measurable reciprocal debit/return path.

Before execution, reopen the repository hypothesis registry for all spatial-return, reservoir, saturation, and phase-carrying variants; record provenance and a root-impact matrix; freeze the smallest periodic toy domain, term ablations, boundary conditions, ledger observers, and meanings of every outcome. No new field, repair, tuning, soliton run, production-code change, whitepaper edit, mechanism promotion, or real-physics claim is authorized.

<!-- CHECKER-XZ bytes=1804 sha256=dfcf7b9b9b05003d1beb10923579d5b9ab976eee2a9104f683faeeafbf472111 -->
```base64
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
```
