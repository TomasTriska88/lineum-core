# Classical Reference Before Lineum Emergence — Reciprocal Exchange First

**Status:** official primary retained; independent checker pending  
**Version:** 0.5.0  
**Evidence cutoff:** 2026-08-06  
**Repository / branch / base:** `TomasTriska88/lineum-core` / `develop` / `42fef4b20b7faac6e8a0638b0ec36ba826134545`  
**Historical filename retained:** `research/lineum-classical-bright-soliton-reference-preregistration.md`  
**Root programme:** B4 report `0.10.1`; localized-L1 verification receipt `1.0.0`  
**Scope:** non-spatial conventional exchange first; soliton localization paused; every Lineum substitution blocked  
**Confidence:** `reproduced` for the frozen conventional primary; independent verification pending

## Plain conclusion

The frozen conventional reference was executed exactly once from committed report version `0.4.0` at `dt=0.001`. All five preregistered lanes passed: coherent return, incomplete detuned transfer with recurrence, reciprocal relaxation without return, one-way accumulation, and no coupling. This reaches `reproduced` for the conventional primary only. It does not validate Lineum, identify a return mechanism in Lineum, or establish that nature uses this model.

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

The capsule contains the complete primary, closed-form checker, permanent tests, and machine-readable development receipt. The checker imports no primary module, recomputes closed-form event populations and gates, validates error/max-transfer witnesses, detects tampered events/gates/witnesses, and binds its verdict to the canonical source JSON SHA-256. It does not replay every RK4 substep; trajectory-wide maxima therefore still share primary-code audit and test dependence. The official checker has not been invoked.

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

## Official primary result — checker pending

The official command was invoked exactly once from committed source commit `42fef4b20b7faac6e8a0638b0ec36ba826134545` and report blob `fe7117d869704de32c7e183dd97fa6d615941b0d`:

```text
python exchange_primary.py --profile official --output reciprocal-exchange-primary-official.json
```

```text
started UTC = 2026-08-06T14:01:13.534109+00:00
finished UTC = 2026-08-06T14:01:14.905108+00:00
solver return code = 0
elapsed seconds = 0.803070089
Python = 3.13.5 CPython
platform = Linux-6.18.35-x86_64-with-glibc2.41
primary JSON bytes = 7958
primary JSON SHA-256 = bcfec07204869be1b8d798d1d0f4d20999a38cf132e72cbf4d31de6d0a0c5e98
stdout bytes / SHA-256 = 79 / 891903996847a8586f47479829424479bfd80bd2792fad37412b679b051875f7
stderr bytes / SHA-256 = 0 / e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
checker invoked = false
```

| Lane | Pass | Max ledger drift | Max analytic error | Max B | Reversals | Return |
|---|---:|---:|---:|---:|---:|---:|
| R0 | yes | `7.993605777301127e-15` | `2.949862576429041e-13` | `1.0000000000000058` | 3 | yes |
| R1 | yes | `5.995204332975845e-15` | `1.3350431871117507e-13` | `0.4999999999999985` | 3 | yes |
| R2 | yes | `7.549516567451064e-15` | `2.5202062658991053e-14` | `0.49999999896942665` | 0 | no |
| R3 | yes | `3.9968028886505635e-15` | `1.3433698597964394e-14` | `0.9999546000702397` | 0 | no |
| R4 | yes | `0` | `0` | `0` | 0 | no |

The outer execution wrapper later returned status `1` with `TERM environment variable not set` and an ANSI clear sequence. This occurred after the solver receipt and output were written. Solver stderr was empty, the primary JSON parsed, and its byte count and SHA-256 matched the retained receipt. This is classified as a technical post-processing failure with no observed scientific effect. The official primary is not rerun.

The observation supports only that the frozen primary numerically reproduced its declared conventional behaviors and gates. Independent checking is still pending, so the status is `reproduced`, not `robust_within_tested_domain` or `mechanistically_supported`.

## Evidence boundary and variant impact

1. **Implementation:** RK4 primary, closed-form checker, gates, schemas, extraction and tamper tests exist.
2. **Observed:** the single official primary passed all five frozen lanes; development coarse/fine sensitivity remains recorded; the official checker has not run.
3. **Cautious interpretation:** the primary harness reproduced the frozen behavioral classes; independent analytic verification is still required.
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
| `OFFICIAL_PRIMARY.json` | 7958 | `bcfec07204869be1b8d798d1d0f4d20999a38cf132e72cbf4d31de6d0a0c5e98` |
| `OFFICIAL_PRIMARY_EXECUTION.json` | 1130 | `eadda5347469a9096bfa1c3a881290e2bcda287428d4da08822018684392a240` |
| `OFFICIAL_PRIMARY_WRAPPER_NOTE.json` | 642 | `602ef678f62b007832102f51d8e101751a2e44c8fee506b4832079c1d4fbb1f2` |
| `OFFICIAL_PRIMARY.stdout` | 79 | `891903996847a8586f47479829424479bfd80bd2792fad37412b679b051875f7` |
| `OFFICIAL_PRIMARY.stderr` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Archive bytes `7252`; archive SHA-256 `93cdffc13cf6f95922a02160774fabcd0dfa6e6117f39de5f97e06a087abff9c`; deterministic XZ/TAR encoded as Base64.

## Exact next gate

Commit this exact report with the retained primary before invoking the checker. Re-fetch it by immutable commit, verify the report blob, capsule, official JSON and source hashes, extract it, and rerun the nine non-checker tests. Then invoke the independent checker exactly once:

```bash
python exchange_checker.py --input OFFICIAL_PRIMARY.json --output reciprocal-exchange-checker-official.json
```

Embed and commit that exact checker JSON, command/environment receipt, byte count, SHA-256, mismatches, and bounded interpretation in this same report before any Lineum comparison. Until then: no primary rerun, tuning, threshold change, spatial extension, soliton run, Lineum substitution, mechanism ranking, or whitepaper edit.

<!-- CAPSULE bytes=7252 sha256=93cdffc13cf6f95922a02160774fabcd0dfa6e6117f39de5f97e06a087abff9c -->
```base64
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
cVKX2JWkI+eHX/JVoK5TKCC8+phhE1skDegoIL3mPmnASgSpC1d4iXUrqlOq+6QrfxAcqzKFQh4hKynqaHYvP14//5aldY0chwxa
ZMdv95GfZvInO6MP737VD+EfiYnAicuTFqnboT4y09Bu4mr4/gs/jT/JMlD58VWsHb6tArziBC2vV74sdkCbNigyqq0S+2Yjenl5
ubqGB8MBhhpMpnYmK+5RvAFyCle//mjtgGumWd4jcE+JIVqCwwnhZSYJbZdtNkQifsu3UFU6muuwxDyFnNaGOMEHIal4sdQ6cU5t
fZf43Zw9XSx7h1SVZPXU/CVXwnC1CQSbwwdC79nSrmY4QKih5MTxx82mFidZwAj7ms1G28hgQIHyJh9HoUeJoNlLRHOMb0LFYy6J
drAyHPFRAkZwhgiejwKeI6dWdpGJYOLShJBm4ToXfVauWN++7BswAHAdaGEHcG/IuMaSszoeOrkP1XvRGATyi0XEjCVpR0Yi2TpO
hvSNKzuBYjQPr9Kwm4Ss9DJEWPw445dGUBUHiSNXLGIlvNvdjp+xc3THghXkv6CPmJGbe9qj3ZYWf5m6pDJ3eL+D/FufQMLi/7LA
zvuZP2Gm4olJ5v2eeJcozf7sRpN4+8Yd6QOYNnUYQnG5uCeuQM1d7nMno/cRf9uiPS34rvpNE5tNcXsn+j2DuAS8xl+Y0AP1AzAX
8GZa6732L/QAlkltv8v925SSCoCZGNMLzDqDu/TjhFhZGPYYiYkYO7kLTdNdjyzoLme7yjicGZp8eLhEycbjwnTshNedn2/g2hB+
KPAeWobL+7H9etu2hnYMXw7voui9KOYz69fvdZVKbxJWZVNTNU6odZWEOMOx5Axf4mfLSnHWkS6RhoxEmN8YO9bg2Wq0BI64XuqK
FoVnrjTtKLWeBMaFPZ6dRtTcg6WqOOvm0jwpVbeH2zYpBfimU32pEcD10XOTIdHBVqfUMWs9ssfCCOGpQJnhR7aDwwM7LN6qL+QX
46/+b71EGu8s/OLWjDfjoqn7Y9dl1zHUy6ivGu15QedVckUgLXa0CqIeXH7WiCCDCLrlGGS3nogebf2JTvZbCQy9AOwx427FZ7Hn
qfiKVCWqvifxM14J4FEkIOJhGHxjgU619+0bE84TSJFq3A7a5NqXlKJIryChsZWGntek/JlWnqLacBE1sYWwIMqyCPdaoDNYKxBI
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
```
<!-- END CAPSULE -->