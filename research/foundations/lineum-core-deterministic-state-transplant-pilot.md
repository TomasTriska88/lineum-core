# Deterministic State Transplant Pilot in Lineum Core

**Status:** active research checkpoint; isolated NumPy pilot passed; public-library placement superseded; supported-environment validation pending

**Version:** 0.2.0

**Evidence cutoff:** 2026-07-30

**Scope:** A Core-only intervention testing whether a numerical Lineum trajectory can be paused, transferred into a clean recipient, and continued exactly when the live fields, complete `CoreConfig`, step index, and NumPy random-generator state are transferred together. This report does not use Lina EI, symbolic memory, Lineum Dynamics, OEA, external language models, or private data.

**Central question:** Is the currently implemented Core state plus its numerical context sufficient to continue one donor trajectory exactly after serialization and restoration, and does removing the random-generator state break exact continuation when stochastic forcing is active?

**Current confidence:** High for the isolated round-trip, integrity, and exact-continuation observations; medium for active-Core equivalence because the isolated verifier freezes only the inspected NumPy path; low for heredity, autonomous copying, biological analogy, identity, or sufficiency outside this test.

## 1. Version 0.2 architectural correction

Version 0.1.0 placed the checkpoint helper under the installable `lineum_core/` package. That placement is superseded. The helper originated in a single causal experiment and had not passed the public-library promotion gate. Its scientific result remains unchanged, but its architecture is now classified correctly as research tooling.

The retained implementation is `scripts/research/heredity_transplant_harness.py`. Its regression coverage is `tests/research/test_heredity_transplant_harness.py`. Neither path is part of the installable public package. The previous placement remains visible in Git history; this revision does not reinterpret it as having been valid public API.

## 2. Answer first

The smallest completed pilot passed.

A donor was advanced for five steps, serialized, and then advanced for seven more steps in two ways: uninterrupted, and after loading the transferred fields, configuration, step index, and exact NumPy generator state into independent arrays. The final `psi`, `phi`, `kappa`, and `mu` arrays were bit-for-bit identical.

A matched control transferred the same fields and configuration but reset the future random history to seed `999`. Its `psi` field diverged from the uninterrupted donor, with maximum absolute difference `0.06480561760422429` after seven continuation steps.

The plain mental picture is a paused card game. The fields are the board position. The random-generator state is the exact order of the undealt deck. Copying only the board cannot reproduce the same future cards.

This is a software continuation result. It is not a demonstration of heredity, regrowth, self-maintenance, or second-generation copying.

## 3. Tested package

The tested package is `P = (L, C, X, R)`, where:

- `L` is the inspected `step_core` NumPy update law;
- `C` is the complete `CoreConfig` value;
- `X` is the live `psi`, `phi`, `kappa`, and `mu` field state;
- `R` is the complete legacy NumPy random-generator state.

The step index is retained as provenance but is not consumed by the active update law.

## 4. Frozen inputs

- grid: `12 x 12`;
- initial envelope: `exp(-4 * (x^2 + y^2))` over `linspace(-1, 1, 12)`;
- initial `psi`: `0.15 * envelope * exp(i * (1.7*x - 0.8*y))`;
- initial `phi`: `0.02 * envelope`;
- initial `kappa`: `0.55 + 0.35 * envelope`;
- initial `mu`: `0.01 * (1 - envelope)`;
- `CoreConfig` defaults except `use_mu=True`, `noise_strength=0.004`;
- donor seed: `314159`;
- checkpoint after `5` steps;
- continuation horizon: `7` steps;
- reset-history seed: `999`;
- backend: NumPy;
- active Core source inspected: `lineum_core/math.py` blob SHA `bb877021810691223a0eb960a45493a2e351112a`.

## 5. Machine-readable result

```json
{
  "backend": "numpy",
  "checkpoint_bytes": 12191,
  "checkpoint_file_sha256": "975f9137634ef1781e7afc8a269a43bf752fa19ac629b2255906f85bc7dc8361",
  "continuation_steps": 7,
  "full_transfer": {
    "final_psi_sha256": "db62daa90d4badefd40e887f25ed0257d395302c25b5f6be9f48b7529c79c6d1",
    "kappa_bitwise_equal": true,
    "max_abs_psi_difference": 0.0,
    "mu_bitwise_equal": true,
    "phi_bitwise_equal": true,
    "psi_bitwise_equal": true
  },
  "recipient_step_index": 5,
  "reset_rng_control": {
    "final_psi_sha256": "7990b4cb3e54d6f41b19336b0f615b917c560776e0a316a9c3e0affebcd89629",
    "max_abs_psi_difference": 0.06480561760422429,
    "psi_bitwise_equal": false
  },
  "reset_seed": 999,
  "schema": "lineum-core-transplant-pilot-result-v1",
  "seed": 314159,
  "warmup_steps": 5
}
```

## 6. Controls and interpretation

The full-transfer lane establishes exact replay within the frozen setup. The reset-history lane establishes that the future stochastic sequence is causally necessary for exact byte-level continuation when noise is active.

This does not establish that the random state is a biological carrier. A higher-level organization might remain recognizable under independent microscopic noise even when exact bytes diverge. Exact replay and organizational reconstruction are therefore separate targets.

## 7. Verification receipt

The corrected research-scoped harness and consolidated regression suite were executed against an isolated reconstruction of the inspected active NumPy path:

```text
python -m pytest -q tests/research/test_heredity_transplant_harness.py
............                                                             [100%]
12 passed in 0.27s
```

The standalone verifier embedded below produced the same checkpoint receipt as the research-scoped harness.

- research harness SHA-256: `1182817c5fcf4d5fe4f7f8cb85dbeae2f2c441ac53a85e46681e188df03b35ae`;
- consolidated test SHA-256: `f267088904f66ff3af4fe7131020d2b755e7084d9c817b692bc8839af36c9870`;
- combined output SHA-256: `1e292dbf6dd1adff5a8ac7701db6ac5bbec2e7f67db34686c4d6c996181f6bc4`.

## 8. Standalone frozen verifier

Save the following block as `verify_state_transplant.py` and run `python verify_state_transplant.py`.

Recorded isolated environment: Python `3.13.5`, NumPy `2.3.5`.

```python
from __future__ import annotations
import base64, hashlib, json
from dataclasses import asdict, dataclass
from typing import Any, Dict, Mapping
import numpy as np

class ExecutionPolicy:
    @classmethod
    def init_core_determinism(cls, seed=42):
        np.random.seed(seed); np.random.RandomState(seed)

@dataclass(frozen=True)
class CoreConfig:
    dt:float=1.0; psi_diffusion:float=0.05; phi_diffusion:float=0.05
    reaction_strength:float=0.0007; noise_strength:float=0.005; drift_strength:float=-0.004
    stencil_type:str='LAP4'; disable_quantum_noise:bool=False; phi_diffusion_scales_with_dt:bool=False
    use_mode_coupling:bool=True; mode_coupling_strength:float=0.001; use_mu:bool=False
    mu_eta:float=0.005; mu_rho:float=0.0001; mu_cap:float=10.0; mu_peak_cutoff_ratio:float=0.1
    psi_amp_cap:float=1e6; grad_cap:float=1e6; phi_cap:float=1e6

def diffuse(field,kappa,rate,stencil):
    ku,kd,kl,kr=(np.roll(kappa,s,a) for s,a in ((1,0),(-1,0),(1,1),(-1,1)))
    fu,fd,fl,fr=(np.roll(field,s,a) for s,a in ((1,0),(-1,0),(1,1),(-1,1)))
    if stencil=='LAP8':
        kul,kur,kdl,kdr=np.roll(ku,1,1),np.roll(ku,-1,1),np.roll(kd,1,1),np.roll(kd,-1,1)
        ful,fur,fdl,fdr=np.roll(fu,1,1),np.roll(fu,-1,1),np.roll(fd,1,1),np.roll(fd,-1,1)
        total=fu*ku+fd*kd+fl*kl+fr*kr+.25*(ful*kul+fur*kur+fdl*kdl+fdr*kdr)
        active=ku+kd+kl+kr+.25*(kul+kur+kdl+kdr)
    else: total,active=fu*ku+fd*kd+fl*kl+fr*kr,ku+kd+kl+kr
    return rate*(total-active*field)

def step(state:Dict[str,Any],cfg:CoreConfig):
    psi=np.asarray(state['psi'],np.complex128); phi=np.asarray(state['phi'],np.float64)
    k=np.asarray(state['kappa'],np.float64); mu=np.asarray(state.get('mu',np.zeros_like(phi)),np.float64)
    delta=np.asarray(state.get('delta',np.zeros_like(phi)),np.float64); size=psi.shape[0]
    amp=np.clip(np.abs(psi),0,cfg.psi_amp_cap); gx,gy=np.gradient(amp+delta)
    gx=np.clip(gx,-cfg.grad_cap,cfg.grad_cap); gy=np.clip(gy,-cfg.grad_cap,cfg.grad_cap)
    grad=np.sqrt(np.clip(gx*gx+gy*gy,0,1e12))
    if cfg.disable_quantum_noise: linon=fluct=0.0
    else:
        prob=(1/(1+np.exp(-5*(amp+grad))))*k; hits=(np.random.rand(size,size)<prob).astype(float)
        phase=np.exp(1j*np.angle(psi)); linon=np.clip((.03+.02*np.clip(amp,0,None))*hits,0,10)*phase
        fluct=np.clip(np.random.normal(0,cfg.noise_strength,(size,size)),-1,1)*phase
    mult=1+mu; interaction=.1*np.tanh(.04*np.clip(phi,0,10)*k*mult/.1)*psi
    interaction/=1+np.abs(interaction)/10; px,py=np.gradient(phi)
    flow=cfg.drift_strength*(px+1j*py)*k*mult; flow/=1+np.abs(flow)/10
    psi+=flow*cfg.dt; mag=np.abs(psi); mask=mag>cfg.psi_amp_cap
    if np.any(mask): psi[mask]*=cfg.psi_amp_cap/(mag[mask]+1e-30)
    psi+=((linon+fluct)*k+interaction)*cfg.dt; psi-=.005*psi*cfg.dt
    psi+=diffuse(psi,k,cfg.psi_diffusion,cfg.stencil_type)*k*cfg.dt; energy=np.abs(psi)**2
    if cfg.use_mode_coupling:
        transfer=cfg.mode_coupling_strength*energy*k*cfg.dt; phi+=transfer
        psi=psi/(np.sqrt(energy)+1e-12)*np.sqrt(np.maximum(energy-transfer,0))
    else: phi+=k*cfg.reaction_strength*(128/size)**2*(energy-phi)*cfg.dt
    scale=cfg.dt if cfg.phi_diffusion_scales_with_dt else 1
    phi+=k*cfg.phi_diffusion*diffuse(phi,k,.05,cfg.stencil_type)*scale; phi=np.clip(phi,0,cfg.phi_cap)
    if cfg.use_mu:
        floor=cfg.mu_peak_cutoff_ratio
        if 0<floor<1: floor*=np.max(energy)
        mu+=cfg.mu_eta*np.maximum(energy-floor,0)*k*mult*cfg.dt; mu-=cfg.mu_rho*mu*cfg.dt
        mu=np.clip(mu,0,cfg.mu_cap)
    return {'psi':psi,'phi':phi,'kappa':k,'mu':mu}

def initial(size=12):
    axis=np.linspace(-1,1,size); y,x=np.meshgrid(axis,axis,indexing='ij'); e=np.exp(-4*(x*x+y*y))
    return {'psi':(.15*e*np.exp(1j*(1.7*x-.8*y))).astype(np.complex128),'phi':(.02*e).astype(float),'kappa':(.55+.35*e).astype(float),'mu':(.01*(1-e)).astype(float)}
def clone(s): return {k:v.copy() for k,v in s.items()}
def run(s,c,n):
    s=clone(s)
    for _ in range(n): s=step(s,c)
    return s

def enc(a):
    a=np.ascontiguousarray(a); return {'dtype':a.dtype.str,'shape':list(a.shape),'data_base64':base64.b64encode(a.tobytes()).decode()}
def dec(r):
    d=np.dtype(r['dtype']); shape=tuple(r['shape']); raw=base64.b64decode(r['data_base64'],validate=True)
    return np.frombuffer(raw,d).reshape(shape).copy()
def canonical(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False).encode()
def rng_record():
    g,keys,pos,has,cached=np.random.get_state(); return {'generator':g,'keys':enc(keys),'position':int(pos),'has_gauss':int(has),'cached_gaussian':float(cached)}
def checkpoint(state,cfg,step_index):
    p={'format':'lineum-core-state-checkpoint','version':1,'step_index':step_index,'config':asdict(cfg),'arrays':{k:enc(v) for k,v in state.items()},'numpy_rng_state':rng_record()}
    p['payload_sha256']=hashlib.sha256(canonical(p)).hexdigest(); return canonical(p)
def load(raw,restore=True):
    p=json.loads(raw); expected=p.pop('payload_sha256')
    if hashlib.sha256(canonical(p)).hexdigest()!=expected: raise ValueError('integrity hash mismatch')
    state={k:dec(v) for k,v in p['arrays'].items()}; cfg=CoreConfig(**p['config'])
    if restore:
        r=p['numpy_rng_state']; np.random.set_state((r['generator'],dec(r['keys']).astype(np.uint32),r['position'],r['has_gauss'],r['cached_gaussian']))
    return state,cfg,p['step_index']
def sha(a): return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()

def verify():
    cfg=CoreConfig(use_mu=True,noise_strength=.004); ExecutionPolicy.init_core_determinism(314159)
    donor=run(initial(),cfg,5); raw=checkpoint(donor,cfg,5); uninterrupted=run(donor,cfg,7)
    state,cfg2,index=load(raw,True); restored=run(state,cfg2,7)
    state,cfg3,_=load(raw,False); np.random.seed(999); reset=run(state,cfg3,7)
    return {'schema':'lineum-core-transplant-pilot-result-v1','backend':'numpy','seed':314159,'reset_seed':999,'warmup_steps':5,'continuation_steps':7,'recipient_step_index':index,'checkpoint_bytes':len(raw),'checkpoint_file_sha256':hashlib.sha256(raw).hexdigest(),'full_transfer':{**{f'{k}_bitwise_equal':bool(np.array_equal(uninterrupted[k],restored[k])) for k in ('psi','phi','kappa','mu')},'max_abs_psi_difference':float(np.max(np.abs(uninterrupted['psi']-restored['psi']))),'final_psi_sha256':sha(restored['psi'])},'reset_rng_control':{'psi_bitwise_equal':bool(np.array_equal(uninterrupted['psi'],reset['psi'])),'max_abs_psi_difference':float(np.max(np.abs(uninterrupted['psi']-reset['psi']))),'final_psi_sha256':sha(reset['psi'])}}
if __name__=='__main__': print(json.dumps(verify(),indent=2,sort_keys=True))
```

## 9. Limitations

The repository declares `numpy>=1.24,<2.0.0`, while the isolated environment supplied NumPy `2.3.5`. Network access and a usable authenticated local checkout were unavailable, so the full repository suite and supported dependency range could not be executed here. The result remains an isolated implementation checkpoint pending supported-environment CI or local validation.

Only one grid, donor, configuration, reset seed, and horizon were tested. PyTorch CPU and CUDA generator states are not represented by the NumPy checkpoint. SHA-256 detects mutation relative to a stored digest but does not authenticate the producer.

## 10. Current conclusion

> Under active stochastic forcing in the tested Core NumPy path, exact continuation of a particular trajectory requires preserving the numerical field snapshot and the random-generator state in addition to the same update law and configuration. The helper implementing this experiment is research tooling, not public `lineum_core` API.
