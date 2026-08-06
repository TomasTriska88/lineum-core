# Classical Reference Before Lineum Emergence — Reciprocal Exchange First

**Status:** active executable preregistration; official execution not started  
**Version:** 0.4.0  
**Evidence cutoff:** 2026-08-06  
**Repository / branch / base:** `TomasTriska88/lineum-core` / `develop` / `d8318358d4cc3919c38c65d5cf07a7f8089fb91e`  
**Historical filename retained:** `research/lineum-classical-bright-soliton-reference-preregistration.md`  
**Root programme:** B4 report `0.10.1`; localized-L1 verification receipt `1.0.0`  
**Scope:** non-spatial conventional exchange first; soliton localization paused; every Lineum substitution blocked  
**Confidence:** `implemented_and_development_checked`; no official retained result

## Plain conclusion

The smallest conventional reference is now executable. It can distinguish a phase-preserving quantity that moves out and returns, a two-way process that merely relaxes to equilibrium, a one-way accumulator, and no coupling. A non-official fine-step run separated all five lanes; a coarser step exposed the expected numerical sensitivity in only the strict R2 analytic-error gate. This validates the harness vocabulary in development, not Lineum or nature.

The owner direction remains `owner_provided_pre_hypothesis`: established science first; Lineum emergence only at the smallest missing function; keep one report; do not assume a soliton is the main answer. The soliton lane remains `dormant_pending_exchange_reference` and was not executed.

## Inherited evidence and implementation audit

The independently checked B4 localized-L1 screen reproduced 28/28 cases with zero checker mismatches, two cap-dependent partial `psi` recoveries, and zero cap-free full-state recoveries. This is `robust_within_tested_domain` only; wider Lineum and real physics remain unresolved.

At Core base `2d69bd32...`, the explicit ledger is operationally `delta_e=coupling*|psi|^2*kappa*dt`, `phi += delta_e`, `|psi|^2 -= delta_e`. Later `phi` terms influence `psi`, but no paired explicit `phi -= returned; psi += returned` ledger exists. The current conservation test checks positive finite `phi_gain`, not total closed conservation, reverse transfer, recurrence, or full-state return. This is an implementation fact, not a physical interpretation.

A historical source-sink reservoir POC used continuous random injection, a `phi` sink, and a `kappa` corridor; it did not test source-off reciprocal return. Cross-repository variant search returned upstream `502`, so the registry is incomplete, not empty. No private TOLOG material or third-party code is included.

## Frozen conventional reference

For complex amplitudes `a,b`, freeze

```text
i d/dt [a,b]^T = [[Delta/2,g],[g,-Delta/2]] [a,b]^T; (a(0),b(0))=(1,0)
```

with `P_A=|a|^2`, `P_B=|b|^2`, `P_A+P_B=1` for real `g,Delta`.

| Lane | Frozen model | Exact distinguishing behavior |
|---|---|---|
| R0 | `g=1, Delta=0`, horizon `2*pi` | `a=cos(t)`, `b=-i sin(t)`; transfer `pi/2`, population return `pi`, exact state recurrence `2*pi` |
| R1 | `g=1, Delta=2`, horizon `2*pi/sqrt(2)` | `P_B=0.5 sin^2(sqrt(2)t)`; maximum `0.5`; population return without complete transfer |
| R2 | `P_A'=-P_A+P_B`, `P_B'=P_A-P_B`, horizon `10` | conserved reciprocal relaxation to `(0.5,0.5)`; no return |
| R3 | `P_A'=-P_A`, `P_B'=P_A`, horizon `10` | conserved one-way accumulation; no return |
| R4 | `g=0, Delta=0`, horizon `10` | no transfer |

Official primary: original fixed-step classical RK4, Python standard library, binary64, `dt=0.001`, exact event landing only by shortening the final substep, no randomness, cap, clipping, filtering, reset, or renormalization. The CLI rejects another official `dt`.

Frozen gates remain: R0/R1 ledger `<=1e-10`, analytic population error `<=1e-9`, declared transfer/return/maxima and R0 state recurrence `<=1e-8`; R2/R3 ledger `<=1e-12`, analytic error `<=1e-10`, monotonicity and declared final bounds, no return; R4 ledger and departure `<=1e-12`, no transfer. Population recurrence is not automatically complex-state identity. Reciprocity alone is insufficient for oscillatory return: R2 is reciprocal but loses phase information and relaxes.

## Executable and independent checker

The capsule contains the complete primary, closed-form checker, permanent tests, and machine-readable development receipt. The checker imports no primary module, recomputes closed-form event populations and gates, validates error/max-transfer witnesses, detects tampered events/gates/witnesses, and binds its verdict to the canonical source JSON SHA-256. It does not replay every RK4 substep; trajectory-wide maxima therefore still share primary-code audit and test dependence.

Test-first chronology: the initial test failed because the modules did not exist. The first implementation generalized a previously exposed two-component-only RK4 helper. Coarse `dt=0.01` missed only R2 analytic error (`2.493758533006485e-10` versus `1e-10`); fine `dt=0.005` passed all lanes. Tamper tests first exposed missing checker bindings, then passed after repair. A larger readable draft and a first compact generator were rejected before publication because transport display truncated and a non-raw string risked LaTeX control characters. No branch mutation or official run resulted. A later unreferenced staging blob `3a1afabf...` differed from the local draft only by its final newline; validating that exact form exposed that the standalone bootstrap selected its own marker instead of the real capsule. The bootstrap was changed to use the last marker and a separate permanent report-only extraction test was added. The final compact refactor reproduces the same coarse/fine values.

## Development observations — not official evidence

| Lane | Fine pass | Max ledger drift | Max analytic error | Max B | Reversals | Return |
|---|---:|---:|---:|---:|---:|---:|
| R0 | yes | `2.724487302430134e-13` | `2.8774094218420032e-11` | `0.9999999999999309` | 3 | yes |
| R1 | yes | `1.5414336473895673e-12` | `5.847944350989565e-11` | `0.49999999999980743` | 3 | yes |
| R2 | yes | `2.220446049250313e-15` | `1.5456858015738817e-11` | `0.49999999896942265` | 0 | no |
| R3 | yes | `1.5543122344752192e-15` | `1.924349568582784e-12` | `0.9999546000702358` | 0 | no |
| R4 | yes | `0` | `0` | `0` | 0 | no |

Environment: Python `3.13.5`, CPython, `Linux-6.18.35-x86_64-with-glibc2.41`. Final source suite: nine tests total; seven passed and two report-context tests skipped without a report path; all nine passed from the extracted report. `official_profile_invoked=false`.

## Evidence boundary and variant impact

1. **Implementation:** RK4 primary, closed-form checker, gates, schemas, extraction and tamper tests exist.
2. **Observed:** coarse sensitivity and fine development separation reproduced; checker mismatches zero.
3. **Cautious interpretation:** the harness can distinguish the four behavioral classes in development.
4. **Hypothesis:** later Lineum ablations may be classified against R0–R4.
5. **Real physics:** no Lineum-to-laboratory, Rabi, quantum, gravity, dark-matter, cosmology, consciousness, or ontology connection is established.

Current explicit `psi -> phi` bookkeeping remains closest only to null R3, not formally compared. Indirect `phi -> psi` conservation role is unresolved. No new return term or field is authorized. B4 Question 2 depends on this vocabulary; Questions 1 and broader real-physics claims are unaffected. Soliton localization remains paused.

## Standalone reproduction

Save this report as `report.md`, then run the standard-library bootstrap below. Every byte and member fails closed on count and SHA-256.

```python
import base64,hashlib,io,json,lzma,re,tarfile
from pathlib import Path
s=Path('report.md').read_text();head='<!-- CAPSULE bytes=';i=s.rindex(head)+len(head);j=s.index(' sha256=',i);k=s.index(' -->',j);size=int(s[i:j]);sha=s[j+8:k]
nl=chr(10);a=s.index('```base64',k)+len('```base64');b=s.index(nl+'```'+nl+'<!-- END CAPSULE -->',a)
c=base64.b64decode(''.join(s[a:b].split()).encode());assert len(c)==size and hashlib.sha256(c).hexdigest()==sha
files={}
with tarfile.open(fileobj=io.BytesIO(lzma.decompress(c)),mode='r:') as t:
 for x in t.getmembers():
  assert x.isfile() and Path(x.name).name==x.name;files[x.name]=t.extractfile(x).read()
man=json.loads(files.pop('MANIFEST.json'));assert set(files)=={x['name'] for x in man['members']}
out=Path('extracted');out.mkdir(exist_ok=True)
for x in man['members']:
 d=files[x['name']];assert len(d)==x['bytes'] and hashlib.sha256(d).hexdigest()==x['sha256'];(out/x['name']).write_bytes(d)
```

Then run:

```bash
cd extracted
PYTHONDONTWRITEBYTECODE=1 python -m py_compile exchange_primary.py exchange_checker.py test_exchange.py
LINEUM_RECIPROCAL_REPORT=../report.md PYTHONDONTWRITEBYTECODE=1 python -m unittest -v test_exchange.py
```

| Member | Bytes | SHA-256 |
|---|---:|---|
| `exchange_primary.py` | 5258 | `8b22994b45b9fdcd4e2c251de3db983a42d0df901a0309ad41d599ae5286199f` |
| `exchange_checker.py` | 4287 | `13f80277c725d0ee0b45b939d2c7731cd2fbed09102f99a0152574a4df7d61dd` |
| `test_exchange.py` | 3375 | `b445e0e2a97ad4199a54988b39fa8db4354c004d83bc782f33bfea5c0a0c4745` |
| `DEVELOPMENT_RECEIPT.json` | 4036 | `064cda2cab4226b0ff6e7f30aa85d5945688ce0d40a0126289ad40550b2f7bc7` |

Archive bytes `5352`; archive SHA-256 `9c52e839c1d8f17a2b8732d49767e40922a1dfb16f7d6aadfd74439dbd38b678`; deterministic XZ/TAR encoded as Base64.

## Exact next gate

Commit this exact executable report. Re-fetch it by immutable commit, verify report blob and capsule member hashes, extract it, and rerun the tests. Then invoke the official primary exactly once:

```bash
python exchange_primary.py --profile official --output reciprocal-exchange-primary-official.json
```

Embed and commit that exact JSON, command/environment receipt, byte count, and SHA-256 in this same report before invoking the checker. The checker then runs exactly once against the committed primary result and is committed before interpretation. Until then: no official checker, tuning, threshold change, spatial extension, soliton run, Lineum substitution, mechanism ranking, or whitepaper edit.

<!-- CAPSULE bytes=5352 sha256=9c52e839c1d8f17a2b8732d49767e40922a1dfb16f7d6aadfd74439dbd38b678 -->
```base64
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
DQfIAAHBKYDwAQAToLaUscRn+wIAAAAABFla
```
<!-- END CAPSULE -->