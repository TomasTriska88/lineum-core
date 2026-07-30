# Static Baseline and Live-State Transplant Matrix in Lineum Core

**Status:** active research report; verified negative result for the static-baseline mechanism; owner failure-gate interpretation pending

**Version:** 0.1.0

**Evidence cutoff:** 2026-07-30

**Scope:** A Core-only four-lane pilot separating a static initial-state recipe from an already developed live field state. The pilot uses no Lina EI repository, symbolic memory, private data, Dynamics, OEA, language model, or external service.

**Central question:** Can a compact static recipe reconstruct a donor trajectory in a standardized recipient, and does supplying that recipe alongside the donor live state change later evolution?

**Current confidence:** High for the isolated lane relationships and the fact that active `step_core` does not consume the recipe after initialization; medium for quantitative portability across supported NumPy versions; low for any general heredity, biology, identity, or autonomous-copy claim.

## 1. Answer first

The proposed static “developmental baseline” is not an active hereditary mechanism in the current Core.

Using the same recipe and exactly the same random history rebuilt the donor state bit for bit. Using the same recipe with a different developmental random history did not rebuild the same donor: at the transplant point, `psi` had normalized RMS error `0.39287756500084337`, although its amplitude pattern still correlated `0.8916849964282161` with the donor.

After all recipients received the same seven-step challenge:

- the blank recipient remained very different from the donor (`psi` NRMSE `0.9846489404148044`, amplitude correlation `0.23439916233601724`);
- the recipe-grown recipient was not the donor (`psi` NRMSE `0.3773911042374487`) but retained a strongly similar broad amplitude shape (correlation `0.9667061702078517`);
- the live-state recipient matched the donor exactly;
- “recipe plus live state” was byte-identical to live state alone.

The everyday picture is a cake mould. It shapes the batter at the beginning, but once the cake is removed, keeping the mould beside it does not repair, steer, or regrow the cake. In the current solver, the recipe creates initial arrays and then disappears from causality.

## 2. What failed and what survived

**Verified failure within the tested domain:** a static initializer with independent noise is insufficient for exact donor reconstruction. Adding the initializer record to an already developed live state has no runtime effect because `step_core` reads only the live arrays and `CoreConfig`.

**Positive result that remains:** the same initializer produces a recognizably related large-scale amplitude envelope under a different stochastic history. The high correlation is evidence of family resemblance in this specific observable, not identity or heredity.

**Not falsified:** a dynamic repair law, an attractor-producing developmental process, a compressed active controller, environmental scaffolding, or another mechanism capable of reconstruction after perturbation.

## 3. Frozen causal lanes

| Lane | Starting content | Meaning |
|---|---|---|
| `N0_blank` | zero `psi`, `phi`, `mu`; uniform `kappa=0.55` | blank-recipient null |
| `B1_baseline_independent_history` | state grown for five steps from the recipe under seed `271828` | static recipe under independent development |
| `X1_live_state_only` | donor live state after five steps under seed `314159` | transplanted developed state |
| `BX_baseline_plus_live_state` | the same donor live state, with the recipe retained only as provenance | test whether the recipe remains causally active |

All four lanes then received the same seven-step challenge initialized with seed `161803`. The reference was the donor live state continued for the same seven steps under the same challenge seed.

The replay control regenerated the donor from the static recipe using the original donor seed `314159` for five steps.

## 4. Metrics

For each array `A`, normalized root-mean-square error is the RMS difference divided by the RMS magnitude of the reference, with a floor of `1e-15` in the denominator.

`numpy.array_equal` tests exact byte-level equality after dtype-preserving execution. Pearson correlation of flattened `abs(psi)` measures broad amplitude-shape similarity. Correlation does not test phase identity, causality, topological equivalence, or function.

## 5. Frozen inputs

- grid: `12 x 12`;
- initial recipe parameters: `extent=1`, `envelope_decay=4`, `psi_amplitude=0.15`, `phase_x=1.7`, `phase_y=-0.8`, `phi_amplitude=0.02`, `kappa_floor=0.55`, `kappa_amplitude=0.35`, `mu_amplitude=0.01`;
- `CoreConfig` defaults except `use_mu=True`, `noise_strength=0.004`;
- donor seed: `314159`;
- independent-development seed: `271828`;
- common challenge seed: `161803`;
- developmental horizon: `5` steps;
- common challenge horizon: `7` steps;
- backend: NumPy;
- active Core source inspected: `lineum_core/math.py` blob SHA `bb877021810691223a0eb960a45493a2e351112a`.

## 6. Machine-readable result

```json
{
  "schema": "lineum-core-baseline-state-matrix-v1",
  "same_history_replay": {
    "psi_bitwise_equal": true,
    "psi_nrmse": 0.0,
    "psi_amplitude_correlation": 1.0,
    "psi_sha256": "43d45269916b40b2720e1796eb07896d0cb0b15d78857786b1f587d73ad0ecc4"
  },
  "independent_history_at_transplant": {
    "psi_bitwise_equal": false,
    "psi_nrmse": 0.39287756500084337,
    "psi_amplitude_correlation": 0.8916849964282161,
    "psi_sha256": "a672789fd6ecb2e0dffa4856bae6ccd668ceeb124713a7ba6096f5d6ac2d0d83"
  },
  "lanes_after_common_challenge": {
    "N0_blank": {
      "psi_bitwise_equal": false,
      "psi_nrmse": 0.9846489404148044,
      "psi_amplitude_correlation": 0.23439916233601724,
      "psi_sha256": "3407eaea69a62fc2485496f01dc12ea3552c6ae0b9d28af7b16a1df7f6b2165e"
    },
    "B1_baseline_independent_history": {
      "psi_bitwise_equal": false,
      "psi_nrmse": 0.3773911042374487,
      "psi_amplitude_correlation": 0.9667061702078517,
      "psi_sha256": "d012b33b166744650534c7af43b727424feb58661d4dc238e736bfc2de003788"
    },
    "X1_live_state_only": {
      "psi_bitwise_equal": true,
      "psi_nrmse": 0.0,
      "psi_amplitude_correlation": 0.9999999999999998,
      "psi_sha256": "eccd1b646506c5be148831e434197370db5cb6139eb95961c54045546c2737db"
    },
    "BX_baseline_plus_live_state": {
      "psi_bitwise_equal": true,
      "psi_nrmse": 0.0,
      "psi_amplitude_correlation": 0.9999999999999998,
      "psi_sha256": "eccd1b646506c5be148831e434197370db5cb6139eb95961c54045546c2737db"
    }
  },
  "baseline_runtime_causal_input": false
}
```

## 7. Causal verdict

| Candidate | Status after pilot | Reason |
|---|---|---|
| static recipe as exact donor carrier | `unsupported_under_tested_conditions` | independent developmental history produced nonzero error |
| static recipe as broad morphology prior | `supported_within_tested_observable` | amplitude correlation remained high under independent history |
| live field state as exact short-horizon continuation carrier | `supported_within_tested_conditions` | `X1` matched reference bitwise under common challenge |
| recipe as runtime input after state creation | `falsified_within_current_implementation` | `BX` and `X1` were identical; `step_core` has no recipe input |
| strong hereditary/self-copy mechanism | `untested` | no regrowth after erasure, source removal, or second-generation copy |

## 8. Failure-to-mechanism map

The failure can be repaired only by changing the tested mechanism, not by relabelling this static initializer. Three qualitatively distinct candidate classes remain open:

1. **Active attractor or homeostatic law:** a persistent rule continuously pulls damaged states back toward an organization.
2. **Compressed generative controller:** a smaller transferable state unfolds a pattern through a multi-stage process rather than one initial array construction.
3. **Environmental or boundary scaffolding:** reconstruction depends on a standardized surrounding gradient, boundary, resource flow, or challenge sequence rather than the recipe alone.

No replacement class is selected in this report. The verified negative result triggers the owner common-sense gate before a new consequential mechanism is chosen.

## 9. Repository-boundary correction

The first implementation mistakenly placed experiment-specific baseline and checkpoint helpers inside `lineum_core/`. That placement is superseded under the public-library promotion gate.

The retained executable tool is `scripts/research/heredity_transplant_harness.py`, and its tests are `tests/research/test_heredity_transplant_harness.py`. The following obsolete placements are removed in the cleanup checkpoint:

- `lineum_core/developmental_baseline.py`;
- `lineum_core/state_checkpoint.py`;
- `scripts/run_core_baseline_state_matrix.py`;
- `tests/test_core_baseline_state_matrix.py`;
- `tests/test_state_checkpoint.py`.

The Git history preserves the mistake and correction. No public Core equation or `step_core` behavior is changed.

## 10. Verification receipt

```text
python -m pytest -q tests/research/test_heredity_transplant_harness.py
............                                                             [100%]
12 passed in 0.27s
```

The research-scoped harness and an isolated frozen verifier generated byte-identical machine-readable output.

- research harness SHA-256: `1182817c5fcf4d5fe4f7f8cb85dbeae2f2c441ac53a85e46681e188df03b35ae`;
- consolidated test SHA-256: `f267088904f66ff3af4fe7131020d2b755e7084d9c817b692bc8839af36c9870`;
- frozen verifier SHA-256: `987226b4cfdac67fec5de6ff31f3f1f8cb2c49a38efd4cc52e7d2c27453085fa`;
- combined output SHA-256: `1e292dbf6dd1adff5a8ac7701db6ac5bbec2e7f67db34686c4d6c996181f6bc4`.

## 11. Standalone frozen verifier

Save the following block as `verify_baseline_state_matrix.py` and run `python verify_baseline_state_matrix.py --experiment matrix`.

Recorded isolated environment: Python `3.13.5`, NumPy `2.3.5`.

```python
from __future__ import annotations
import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from typing import Any, Dict, Mapping
import numpy as np

class ExecutionPolicy:
    @classmethod
    def init_core_determinism(cls, enforce_canonical=True, seed=42, device_mode=None):
        if device_mode not in (None, 'numpy'):
            raise RuntimeError('Verifier supports only NumPy.')
        np.random.seed(seed)
        np.random.RandomState(seed)

@dataclass(frozen=True)
class CoreConfig:
    dt: float = 1.0
    psi_diffusion: float = 0.05
    phi_diffusion: float = 0.05
    reaction_strength: float = 0.0007
    noise_strength: float = 0.005
    drift_strength: float = -0.004
    stencil_type: str = 'LAP4'
    disable_quantum_noise: bool = False
    phi_diffusion_scales_with_dt: bool = False
    use_mode_coupling: bool = True
    mode_coupling_strength: float = 0.001
    use_mu: bool = False
    mu_eta: float = 0.005
    mu_rho: float = 0.0001
    mu_cap: float = 10.0
    mu_peak_cutoff_ratio: float = 0.1
    psi_amp_cap: float = 1000000.0
    grad_cap: float = 1000000.0
    phi_cap: float = 1000000.0

def diffuse(field, kappa, rate, stencil):
    ku,kd,kl,kr=(np.roll(kappa,s,a) for s,a in ((1,0),(-1,0),(1,1),(-1,1)))
    fu,fd,fl,fr=(np.roll(field,s,a) for s,a in ((1,0),(-1,0),(1,1),(-1,1)))
    if stencil == 'LAP8':
        kul,kur,kdl,kdr=np.roll(ku,1,1),np.roll(ku,-1,1),np.roll(kd,1,1),np.roll(kd,-1,1)
        ful,fur,fdl,fdr=np.roll(fu,1,1),np.roll(fu,-1,1),np.roll(fd,1,1),np.roll(fd,-1,1)
        total=fu*ku+fd*kd+fl*kl+fr*kr+0.25*(ful*kul+fur*kur+fdl*kdl+fdr*kdr)
        active=ku+kd+kl+kr+0.25*(kul+kur+kdl+kdr)
    else:
        total,active=fu*ku+fd*kd+fl*kl+fr*kr,ku+kd+kl+kr
    return rate*(total-active*field)

def step_core(state: Dict[str,Any], cfg: CoreConfig):
    psi=np.asarray(state['psi'],dtype=np.complex128); phi=np.asarray(state['phi'],dtype=np.float64)
    kappa=np.asarray(state['kappa'],dtype=np.float64); mu=np.asarray(state.get('mu',np.zeros_like(phi)),dtype=np.float64)
    delta=np.asarray(state.get('delta',np.zeros_like(phi)),dtype=np.float64); size=psi.shape[0]
    amp=np.clip(np.abs(psi),0,cfg.psi_amp_cap); gx,gy=np.gradient(amp+delta)
    gx=np.clip(gx,-cfg.grad_cap,cfg.grad_cap); gy=np.clip(gy,-cfg.grad_cap,cfg.grad_cap)
    grad=np.sqrt(np.clip(gx**2+gy**2,0,1e12))
    if cfg.disable_quantum_noise: linon=fluct=0.0
    else:
        probability=(1/(1+np.exp(-5*(amp+grad))))*kappa
        hits=(np.random.rand(size,size)<probability).astype(np.float64)
        effect=np.clip((0.03+0.02*np.clip(amp,0,None))*hits,0,10)
        phase=np.exp(1j*np.angle(psi)); linon=effect*phase
        fluct=np.clip(np.random.normal(0,cfg.noise_strength,(size,size)),-1,1)*phase
    multiplier=1+mu; interaction=0.1*np.tanh(0.04*np.clip(phi,0,10)*kappa*multiplier/0.1)*psi
    interaction/=1+np.abs(interaction)/10
    pgx,pgy=np.gradient(phi); flow=cfg.drift_strength*(pgx+1j*pgy)*kappa*multiplier
    flow/=1+np.abs(flow)/10; psi+=flow*cfg.dt
    mag=np.abs(psi); mask=mag>cfg.psi_amp_cap
    if np.any(mask): psi[mask]*=cfg.psi_amp_cap/(mag[mask]+1e-30)
    psi+=((linon+fluct)*kappa+interaction)*cfg.dt; psi-=0.005*psi*cfg.dt
    psi+=diffuse(psi,kappa,cfg.psi_diffusion,cfg.stencil_type)*kappa*cfg.dt
    energy=np.abs(psi)**2
    if cfg.use_mode_coupling:
        transfer=cfg.mode_coupling_strength*energy*kappa*cfg.dt; phi+=transfer
        psi=psi/(np.sqrt(energy)+1e-12)*np.sqrt(np.maximum(energy-transfer,0))
    else:
        phi+=kappa*cfg.reaction_strength*(128/size)**2*(energy-phi)*cfg.dt
    scale=cfg.dt if cfg.phi_diffusion_scales_with_dt else 1
    phi+=kappa*cfg.phi_diffusion*diffuse(phi,kappa,0.05,cfg.stencil_type)*scale; phi=np.clip(phi,0,cfg.phi_cap)
    if cfg.use_mu:
        floor=cfg.mu_peak_cutoff_ratio
        if 0<floor<1: floor*=np.max(energy)
        mu+=cfg.mu_eta*np.maximum(energy-floor,0)*kappa*multiplier*cfg.dt; mu-=cfg.mu_rho*mu*cfg.dt
        mu=np.clip(mu,0,cfg.mu_cap)
    return {'psi':psi,'phi':phi,'kappa':kappa,'mu':mu}

@dataclass(frozen=True)
class Baseline:
    grid_size:int=12; extent:float=1.0; envelope_decay:float=4.0; psi_amplitude:float=0.15
    phase_x:float=1.7; phase_y:float=-0.8; phi_amplitude:float=0.02
    kappa_floor:float=0.55; kappa_amplitude:float=0.35; mu_amplitude:float=0.01

def initial(b):
    axis=np.linspace(-b.extent,b.extent,b.grid_size); y,x=np.meshgrid(axis,axis,indexing='ij')
    e=np.exp(-b.envelope_decay*(x*x+y*y)); p=np.exp(1j*(b.phase_x*x+b.phase_y*y))
    return {'psi':(b.psi_amplitude*e*p).astype(np.complex128),'phi':(b.phi_amplitude*e).astype(np.float64),'kappa':(b.kappa_floor+b.kappa_amplitude*e).astype(np.float64),'mu':(b.mu_amplitude*(1-e)).astype(np.float64)}

def blank(b):
    shape=(b.grid_size,b.grid_size)
    return {'psi':np.zeros(shape,np.complex128),'phi':np.zeros(shape),'kappa':np.full(shape,b.kappa_floor),'mu':np.zeros(shape)}

def clone(s): return {k:(v.copy() if isinstance(v,np.ndarray) else v) for k,v in s.items()}
def run(s,c,n):
    s=clone(s)
    for _ in range(n): s=step_core(s,c)
    return s

def nrmse(a,b): return float(np.sqrt(np.mean(np.abs(a-b)**2))/max(float(np.sqrt(np.mean(np.abs(a)**2))),1e-15))
def corr(a,b): return float(np.corrcoef(np.abs(a).ravel(),np.abs(b).ravel())[0,1])
def sha(a): return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()
def receipt(ref,cand): return {'bitwise_equal':bool(np.array_equal(ref,cand)),'nrmse':nrmse(ref,cand),'amplitude_correlation':corr(ref,cand),'sha256':sha(cand)}

def matrix():
    b=Baseline(); c=CoreConfig(use_mu=True,noise_strength=0.004)
    ExecutionPolicy.init_core_determinism(seed=314159,device_mode='numpy'); donor=run(initial(b),c,5)
    ExecutionPolicy.init_core_determinism(seed=314159,device_mode='numpy'); replay=run(initial(b),c,5)
    ExecutionPolicy.init_core_determinism(seed=271828,device_mode='numpy'); independent=run(initial(b),c,5)
    lanes={'N0_blank':blank(b),'B1_baseline_independent_history':independent,'X1_live_state_only':clone(donor),'BX_baseline_plus_live_state':clone(donor)}
    ExecutionPolicy.init_core_determinism(seed=161803,device_mode='numpy'); reference=run(clone(donor),c,7)
    out={}
    for name,state in lanes.items():
        ExecutionPolicy.init_core_determinism(seed=161803,device_mode='numpy'); out[name]=receipt(reference['psi'],run(state,c,7)['psi'])
    return {'same_history_replay':receipt(donor['psi'],replay['psi']),'independent_history_at_transplant':receipt(donor['psi'],independent['psi']),'lanes_after_common_challenge':out,'baseline_runtime_causal_input':False}

if __name__=='__main__': print(json.dumps(matrix(),indent=2,sort_keys=True))
```

## 12. Limitations

The repository-supported NumPy range is `<2.0`, while the isolated verifier used NumPy `2.3.5`. Full repository CI, PyTorch paths, CUDA, multiple donors, larger grids, longer horizons, perturbation recovery, and second-generation transfer were not tested. The amplitude correlation can remain high even when phase and exact state differ materially. This result therefore rejects only the static-initializer mechanism under the frozen setup.

## 13. Current conclusion

> The current Core can replay a donor exactly when the same initial recipe and the same stochastic history are repeated, but the static recipe alone does not reconstruct the exact donor under independent development and has no causal role after initialization. It behaves as an initial-condition generator, not as an active hereditary or repair mechanism.
