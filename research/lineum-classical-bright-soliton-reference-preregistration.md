# Classical Reference Before Lineum Emergence — Reciprocal Exchange First

**Status:** validated conventional reference; Lineum comparison not started  
**Version:** 0.6.0  
**Evidence cutoff:** 2026-08-06  
**Repository / branch / base:** `TomasTriska88/lineum-core` / `develop` / `d771373125ecae6acef5b0c1955bb2eb1bfe4c53`  
**Historical filename retained:** `research/lineum-classical-bright-soliton-reference-preregistration.md`  
**Root programme:** B4 report `0.10.1`; localized-L1 verification receipt `1.0.0`  
**Scope:** non-spatial conventional exchange first; soliton localization paused; every Lineum substitution blocked  
**Confidence:** `robust_within_tested_domain` for the frozen conventional reference; no Lineum mechanism tested

## Plain conclusion

The frozen conventional reference and its separately written analytic checker both passed. The checker used the exact committed primary SHA, reported zero mismatches, imported no primary solver, and did not rerun the primary. We can now reliably distinguish coherent return, incomplete detuned transfer with recurrence, reciprocal relaxation without return, one-way accumulation, and no coupling within this protocol. This does not validate Lineum, identify a Lineum return mechanism, or establish that nature uses this model.

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

The capsule contains the complete primary, closed-form checker, permanent tests, and machine-readable development receipt. The checker imports no primary module, recomputes closed-form event populations and gates, validates error/max-transfer witnesses, detects tampered events/gates/witnesses, and binds its verdict to the canonical source JSON SHA-256. It does not replay every RK4 substep; trajectory-wide maxima therefore still share primary-code audit and test dependence. The official checker was invoked exactly once after the primary result was committed; its retained receipt is below.

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

## Independent official checker result

The checker was invoked exactly once from committed report `0.5.0`, without rerunning the primary:

```text
python exchange_checker.py --input OFFICIAL_PRIMARY.json --output reciprocal-exchange-checker-official.json
```

```text
started UTC = 2026-08-06T14:10:14.716547+00:00
finished UTC = 2026-08-06T14:10:16.042605+00:00
checker return code = 0
elapsed seconds = 0.625619634
Python = 3.13.5 CPython
platform = Linux-6.18.35-x86_64-with-glibc2.41
checker source SHA-256 = 13f80277c725d0ee0b45b939d2c7731cd2fbed09102f99a0152574a4df7d61dd
primary input SHA-256 = bcfec07204869be1b8d798d1d0f4d20999a38cf132e72cbf4d31de6d0a0c5e98
checker JSON bytes / SHA-256 = 300 / 27ba9b699ec2cfaba38fd051fd80eed374ac5a072a6e8897e838c0003e86798f
stdout = passed=True mismatches=0
stderr bytes = 0
primary rerun = false
```

Exact bounded verdict:

```json
{"independence":{"closed_form_events":true,"imports_primary":false,"replays_all_RK4_steps":false},"mismatches":[],"passed":true,"schema":"lineum-reciprocal-exchange-check/1","source_sha256":"bcfec07204869be1b8d798d1d0f4d20999a38cf132e72cbf4d31de6d0a0c5e98"}
```

The first disposable `0.6.0` report generator stopped before writing a report because the exact checker JSON braces were interpreted by its outer f-string; no retained artifact or repository state changed. The generator was corrected without changing source, result, gate, or checker.

The same outer wrapper later emitted `TERM environment variable not set` and returned status `1` after the checker receipt and output were written. Checker stderr was empty; the JSON parsed and matched its receipt. This is a technical post-processing failure with no observed scientific effect. The checker is not rerun.

Independence is bounded: event values and gates are recomputed from closed forms, but the checker does not replay every RK4 substep. Trajectory-wide maxima still depend on primary-code audit and permanent tamper tests. Within that declared boundary, the conventional result reaches `robust_within_tested_domain`, not `mechanistically_supported` or `empirically_connected`.

## Evidence boundary and variant impact

1. **Implementation:** RK4 primary, closed-form checker, gates, schemas, extraction and tamper tests exist.
2. **Observed:** the single official primary passed all five lanes and the one-shot analytic checker returned zero mismatches against its exact SHA.
3. **Cautious interpretation:** the conventional classification is robust within the frozen event, gate, precision, and independence boundary.
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
| `OFFICIAL_CHECKER.json` | 300 | `27ba9b699ec2cfaba38fd051fd80eed374ac5a072a6e8897e838c0003e86798f` |
| `OFFICIAL_CHECKER_EXECUTION.json` | 1327 | `8906872f1371d74e1d22e39636aa3538ce6fe378ce953fc2a6f139939ecb2dea` |
| `OFFICIAL_CHECKER_WRAPPER_NOTE.json` | 648 | `7612365674642f60d27cc8ea085b3175eb7d3586c6429732868968062ac284ed` |
| `OFFICIAL_CHECKER.stdout` | 25 | `7aa7cc637d98c079a5b5bfaef1a383d3eccdd34ca83d3be7b1cf420dcdf165af` |
| `OFFICIAL_CHECKER.stderr` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Archive bytes `7760`; archive SHA-256 `0b21f4fda65c315aaa1387a0d1fa414b2d286166940b690f4d52c346c97e0705`; deterministic XZ/TAR encoded as Base64.

## Exact next gate

Commit this exact independently checked reference before any Lineum comparison. The next consequential step remains in this same report and must be preregistered before execution: audit the exact current homogeneous deterministic Core update and classify its explicit `psi -> phi` bookkeeping and indirect `phi -> psi` influence against R2 reciprocal relaxation and R3 one-way accumulation. Freeze term ablations, total-ledger observers, phase-information limits, cap/dissipation handling, and the meaning of every outcome before running it.

No new field, reciprocal repair, spatial extension, soliton run, parameter tuning, mechanism ranking, whitepaper edit, or claim about real physics is authorized by this checkpoint.

<!-- CAPSULE bytes=7760 sha256=0b21f4fda65c315aaa1387a0d1fa414b2d286166940b690f4d52c346c97e0705 -->
```base64
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
```
<!-- END CAPSULE -->