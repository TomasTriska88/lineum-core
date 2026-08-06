# Classical Reference Before Lineum Emergence — Reciprocal Exchange First

**Status:** official homogeneous Core primary retained; independent checker pending  
**Version:** 0.8.0  
**Evidence cutoff:** 2026-08-06  
**Repository / branch / base:** `TomasTriska88/lineum-core` / `develop` / `2fd4554cffcfb65ac30258c76bf41a6022ea5589`  
**Report path:** `research/lineum-classical-bright-soliton-reference-preregistration.md`  
**Confidence:** conventional reference `robust_within_tested_domain`; homogeneous primary `reproduced`; independent homogeneous verification pending

## Plain conclusion

The official homogeneous primary reproduced all seven preregistered lanes exactly once. In the full current snapshot, `psi` first fell and then crossed its initial energy at step `701`, but `phi` never decreased and the declared combined ledger grew from `1` to millions. The observed `psi` recovery is therefore **not a demonstrated reciprocal return from `phi`**.

The ablations isolate the accounting. Mode transfer by itself behaves like the conventional one-way conserved reference R3: it moves quantity from `psi` into `phi`, approximately preserves `E+phi`, and never returns it. The separate `phi -> psi` feedback can amplify `psi` while leaving `phi` unchanged, so it is an unpaired source in this declared ledger. Dissipation is a separate sink. Removing the external `phi` cap changes retained `phi`, but not the `psi` trajectory in this frozen lane.

This applies only to the exact homogeneous deterministic scalar snapshot. It does not falsify spatial Lineum, establish a replacement mechanism, or connect Lineum to known real physics. The independent checker has not yet run.

The owner direction remains `owner_provided_pre_hypothesis`: established science first; introduce Lineum emergence only at the smallest missing function; keep this single report; do not assume a soliton is the answer.

## Frozen provenance and packaging

The complete executable preregistration, conventional R0–R4 reference, source audit, original primary/checker code, permanent tests, and all earlier receipts remain immutable in this same report at commit `2fd4554cffcfb65ac30258c76bf41a6022ea5589`, report blob `befbcee6e15ca94324017051684e4c57ca5678dc`.

Version `0.8.0` avoids recursively embedding that already compressed history. It retains the new official primary artifacts losslessly below and binds them to the immutable executable checkpoint by commit, blob, source hashes, byte counts, and SHA-256. This is a packaging normalization only; no equation, lane, threshold, source, output, or interpretation changed.

```text
source-audited Core commit = f1bd74ec2cb62d3b8d56bda05f524c6f63ab9775
lineum_core/math.py blob = bb877021810691223a0eb960a45493a2e351112a
physics-contract test blob = 7acbb8a1c5ff85a5b24970d216aa2a08111b0941
homogeneous primary source SHA-256 = 242b6d05cef2e1026e23cabbcc0bfc0d5499f155f1c72f5229475da9f5b806e9
homogeneous checker source SHA-256 = 34a0fd5583609b59d430805b3d0d048cdcdff4e311cadb45cf98f408c4233a5b
```

## Current implementation represented by the snapshot

Uniform `psi` and `phi`, `kappa=1`, `mu=0`, `delta=0`, disabled noise, and `dt=1` remove gradients, diffusion, spatial transport, linons, and fluctuations. The surviving NumPy-path algebra is:

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

The surviving multipliers are real and positive. This reduction has no second relative-phase carrier and therefore cannot instantiate the conventional coherent R0 mechanism. The existing Core mode-coupling test checks positive finite `phi_gain`; it does not assert reverse debit, closed full-step accounting, recurrence, or full-state return.

## Retained official primary

The primary was invoked exactly once from committed report `0.7.0`:

```text
python core_homogeneous_primary.py --profile official --output OFFICIAL_CORE_HOMOGENEOUS.json
```

```text
source commit = 2fd4554cffcfb65ac30258c76bf41a6022ea5589
source report blob = befbcee6e15ca94324017051684e4c57ca5678dc
started UTC = 2026-08-06T15:08:52.920245+00:00
finished UTC = 2026-08-06T15:08:53.486516+00:00
elapsed seconds = 0.5661870439998893
return code = 0
Python = 3.13.5 CPython
platform = Linux-6.18.35-x86_64-with-glibc2.41
primary bytes / SHA-256 = 23054 / fb05d61caeb2cfa14f9a8581b73304aefd4b67ee19c6ef8a6f7a12533c55c0ba
stdout bytes / SHA-256 = 69 / 7cc2bbf53b0f10c749b1622d7f6d27931bee5f4a01240cfbdcdbae5b103d7807
stderr bytes / SHA-256 = 0 / e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
checker invoked = false
```

| Lane | Classification | Pass | Apparent recovery | True reciprocal return | Final `E` | Final `phi` | Final ledger |
|---|---|---:|---:|---:|---:|---:|---:|
| `C0_full_default_cap` | `apparent_energy_recovery_without_reciprocal_ledger` | yes | step `701` | no | `2900150.257034308` | `1000000.0` | `3900150.257034308` |
| `C0b_full_cap_free` | `apparent_energy_recovery_without_reciprocal_ledger` | yes | step `701` | no | `2900150.257034308` | `2359502.643825432` | `5259652.90085974` |
| `C1_no_phi_feedback` | `dissipative_one_way_accumulation` | yes | no | no | `2.650267646912908e-10` | `0.0902893517688856` | `0.09028935203391236` |
| `C2_mode_transfer_only` | `one_way_conserved_transfer` | yes | no | no | `0.13519992446823598` | `0.8648000730057612` | `0.9999999974739973` |
| `C3_phi_feedback_only_seeded` | `unpaired_feedback_source` | yes | no | no | `1482693.5590557144` | `1.0` | `1482694.5590557144` |
| `C4_dissipation_only` | `dissipative_sink` | yes | no | no | `4.427529784808337e-05` | `0` | `4.427529784808337e-05` |
| `C5_no_terms_null` | `stationary_null` | yes | no | no | `1.0` | `0` | `1.0` |

Additional observations:

- `C0` minimum energy was `0.23353976762645046` at step `350`; `phi_decrease_count=0`; first cap contact was step `1521`.
- Default-cap `C0` and cap-free `C0b` produced identical final `psi` energy; only retained `phi` and the ledger changed.
- `C2` maximum ledger drift was `2.5260027403106733e-09` and phase drift was `0.0`.
- `C3` held `phi=1` while `E` rose to `1482693.5590557144`.
- Every lane passed its preregistered discriminator; `all_pass=true`.

## Evidence boundary

1. **Current implementation:** one-way accounted mode transfer, feedback amplification without paired `phi` debit, separate dissipation, and an external cap.
2. **Reproduced observation:** the one-shot primary passed all seven lanes; `psi` recovery occurred with zero `phi` decreases and multimillion ledger growth.
3. **Cautious interpretation:** `psi` recovery alone is non-identifying and is not evidence of reciprocal full-state return in this snapshot.
4. **Hypothesis:** spatial gradients, diffusion, locality, or another term could change the classification; none is tested here.
5. **Real physics:** no laboratory, quantum, gravitational, dark-matter, cosmological, consciousness, or ontological connection is established.

Available NumPy `2.3.5` is outside repository requirement `<2.0`; this is a standard-library source-audited snapshot, not a supported active-runtime equivalence claim.

## Lossless primary envelope

Save the Base64 body as part of this report. The following standard-library bootstrap reconstructs the exact primary artifacts and verifies every hash:

```python
from pathlib import Path
import base64,hashlib,json,lzma
s=Path('report.md').read_text();h='<!-- PRIMARY-XZ bytes=';i=s.rindex(h)+len(h);j=s.index(' sha256=',i);e=s.index(' -->',j)
size=int(s[i:j]);sha=s[j+8:e];a=s.index('```base64',e)+len('```base64');b=s.index('```',a)
c=base64.b64decode(''.join(s[a:b].split()));assert len(c)==size and hashlib.sha256(c).hexdigest()==sha
env=json.loads(lzma.decompress(c));out=Path('official-primary');out.mkdir(exist_ok=True)
for n,m in env['members'].items():
 d=base64.b64decode(m['base64']);assert len(d)==m['bytes'] and hashlib.sha256(d).hexdigest()==m['sha256'];(out/n).write_bytes(d)
```

```text
compressed envelope bytes / SHA-256 = 6696 / fbd86d942976f4b77c16b0d32f4989a80c6d8651ae3b6173c9aea0088c9c08ac
OFFICIAL_CORE_HOMOGENEOUS.json bytes / SHA-256 = 23054 / fb05d61caeb2cfa14f9a8581b73304aefd4b67ee19c6ef8a6f7a12533c55c0ba
OFFICIAL_CORE_HOMOGENEOUS_EXECUTION.json bytes / SHA-256 = 1188 / 629efe4242f090ced71bf9152e9bba52d59cd7af9fc7b98a88799f1eb4ce1146
```

## Exact next gate

Commit this exact retained primary. Re-fetch it by immutable commit and verify the report blob, primary envelope, official JSON hash, and the unchanged checker source from executable commit `2fd4554...`. Then invoke the independent checker exactly once without rerunning the primary:

```bash
python core_homogeneous_checker.py --input OFFICIAL_CORE_HOMOGENEOUS.json --output OFFICIAL_CORE_HOMOGENEOUS_CHECKER.json
```

Commit the exact checker output and execution receipt in this same report before any new experiment or interpretation. Until then: no primary rerun, tuning, spatial extension, soliton run, reciprocal repair, new field, production-code change, whitepaper edit, mechanism ranking, or real-physics claim.

<!-- PRIMARY-XZ bytes=6696 sha256=fbd86d942976f4b77c16b0d32f4989a80c6d8651ae3b6173c9aea0088c9c08ac -->
```base64
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
```
