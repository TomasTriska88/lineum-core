# Lineum Label-Retention P1 Preflight

**Status:** active  
**Version:** 0.2.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** one-pair deterministic preflight for the current-engine Q3 label-retention protocol  
**Central question:** does one representative equal-energy orientation pair complete imprint and clean source removal with numerically valid `phi` and `mu` traces whose passive evolution matches the preregistered implementation expectations?  
**Current confidence:** high in the mechanical result inside the declared standalone NumPy runtime; low in any physical interpretation beyond that runtime and one source pair

## 1. Report lineage and programme boundary

This report belongs to the Lineum-native three-question programme:

1. emergent galactic long-range radial response;
2. natural bounded saturation and genuine attraction;
3. information retention during relaxation toward a common coarse state.

The root programme version at preregistration was `0.2.2`, with evidence cutoff `2026-08-04`. The immediate parent protocol froze a full held-out label-retention experiment using equal-energy horizontal and vertical source histories. The observer preflight previously showed that two independent readers could identify the pristine source family, but that result was provisional because it ran in NumPy `2.3.5` while the then-current repository declaration still excluded NumPy 2.x.

This child preflight tests only the mechanical assumptions required before the full population lane. It does not alter the Lineum equation, production code, dependency declaration, or any whitepaper.

## 2. Owner and source boundary

The project owner restricted active scientific work to the three questions above and their connection to measurements or established constraints from the real universe. Dependency work is supporting infrastructure only.

This report contains no TOLOG material and does not use any private uploaded document. It tests only a frozen standalone snapshot of the current Lineum numerical operations.

## 3. Frozen representative source pair

The test uses a periodic `64 x 64` grid and two real nonnegative, independently normalized source amplitudes with equal total energy:

- label `A`: two horizontal Gaussian lobes;
- label `B`: two vertical Gaussian lobes;
- lobe separation: `12` cells;
- Gaussian width: `3.5` cells;
- translation: `(0, 0)`;
- initial `phi = 0`;
- initial `mu = 0`;
- uniform `kappa = 1`.

Required equality and symmetry gates:

- relative total-energy mismatch `<= 1e-14`;
- sorted-amplitude mismatch `<= 1e-14`;
- quadrupole transpose antisymmetry error `<= 1e-12`.

## 4. Frozen dynamics

The deterministic update uses:

- `dt = 0.1`;
- `psi_diffusion = 0.05`;
- `phi_diffusion = 0.05`;
- `reaction_strength = 0.0007`;
- implemented `psi` dissipation coefficient `0.005`;
- `drift_strength = 0`;
- no stochastic source;
- no mode coupling;
- `mu_eta = 0.005` during imprint;
- `mu_rho = 0.0001`;
- `mu_cap = 10`;
- `mu_peak_cutoff_ratio = 0.1`;
- `psi_amp_cap = 1e6`;
- `phi_cap = 1e6`.

Imprint lasts `120` updates. The passive phase then sets `psi` to exact zero once, sets `mu_eta = 0`, retains zero drift, and records checkpoints after `0`, `100`, `500`, `1000`, and `2000` updates.

Under these source-off conditions, the implemented `mu` update reduces pointwise to:

`mu_(n+1) = (1 - mu_rho * dt) * mu_n`.

Therefore the expected passive decay factor is:

`f_n = (1 - 0.0001 * 0.1)^n`.

This rule preserves the normalized spatial shape of `mu` by construction when no cap is reached. A positive shape-retention result is therefore an implementation consequence, not a discovery of new physics.

## 5. Preregistered validity gates

The lane is valid only if all of the following hold:

- no NaN or infinity;
- no fail-safe reset;
- source-off `max(abs(psi)) <= 1e-15` at every checkpoint;
- imprint `max(abs(psi)) < 0.1 * psi_amp_cap`;
- `max(phi) < 0.1 * phi_cap`;
- `max(mu) < 0.25 * mu_cap`;
- all initial equality checks pass;
- horizontal and vertical quadrupole signs remain opposite;
- relative `mu` decay-factor error is `<= 1e-12`;
- normalized passive `mu` shape difference is `<= 1e-12`;
- transposed `phi` and `mu` pairs agree within `1e-12` relative L2.

## 6. Execution receipt

### 6.1 Retained runner identity

- Git blob SHA: `e83a6214877f9f7fa0f9ff4d99bfdc3c022ba4b3`;
- SHA-256 of the exact runner text independently re-executed on `2026-08-04`: `b9e2476469c3a9e97abcbee09b1ef4b10ba3e9984f3f2ba5bcdac7b4f427f0e7`;
- reproduction command: `python research/runners/lineum_p1_preflight.py`;
- independent re-execution command used in the available ChatGPT runtime: `python /mnt/data/lineum_p1_preflight.py`.

### 6.2 Environment

- Python: `3.13.5`;
- NumPy: `2.3.5`;
- platform: `Linux-6.12.13-x86_64-with-glibc2.41`;
- architecture: `x86_64`;
- retained first successful wall-clock time: `1.5263817899999594 s`;
- independent re-execution wall-clock time: `1.5054090920002636 s`.

The Python host emitted an unrelated spreadsheet-runtime warmup traceback on stderr before the experiment. The experiment process nevertheless returned code `0`, produced valid JSON, and all declared numerical gates passed. This warning is retained as an environment limitation rather than hidden.

### 6.3 Failed compact-output attempt

An earlier compact runner completed the numerical calculations but failed while serializing a `numpy.bool_` value to JSON. The scientific arrays and metrics had already been calculated, but the process did not produce a valid machine-readable receipt. The correction converted gate values explicitly to ordinary Python `bool` objects. The corrected run reproduced the decision-relevant values; the largest previously observed numerical difference between equivalent runner paths was approximately `2.78e-17`.

The failed serialization attempt is not counted as a successful scientific execution.

## 7. Human-readable results

All preregistered gates passed in the corrected retained run.

Initial construction:

- relative energy mismatch: `4.440892098500625e-16`;
- sorted-amplitude maximum mismatch: `2.7755575615628914e-17`;
- quadrupole antisymmetry error: `1.1102230246251565e-16`.

Maximum values across imprint and passive evolution:

- maximum `abs(psi)`: `0.10933524493152957`;
- maximum `phi`: `0.0003394883141741534`;
- maximum `mu`: `0.0005574986435013754`;
- maximum source-off `abs(psi)`: exactly `0.0`.

At the final `2000`-update source-off checkpoint:

- `mu` retained `0.9801985752862405` of its imprint RMS amplitude;
- the analytic expected factor was `0.9801985752863286`;
- the relative decay-factor error remained below `9.0e-14`;
- normalized `mu` shape change was about `2.1e-15`;
- `phi` retained about `0.5360370913933448` of its imprint RMS amplitude;
- both channels preserved the correct opposite horizontal/vertical quadrupole signs;
- transpose mismatches remained at floating-point-noise scale.

## 8. Decision-complete machine-readable receipt

```json
{
  "configuration": {
    "dt": 0.1,
    "grid_size": 64,
    "imprint_steps": 120,
    "mu_cap": 10.0,
    "mu_eta_imprint": 0.005,
    "mu_eta_source_off": 0,
    "mu_rho": 0.0001,
    "separation": 12.0,
    "shift": [0, 0],
    "source_off_checkpoints": [0, 100, 500, 1000, 2000],
    "width": 3.5
  },
  "environment": {
    "machine": "x86_64",
    "numpy": "2.3.5",
    "platform": "Linux-6.12.13-x86_64-with-glibc2.41",
    "python": "3.13.5"
  },
  "initial_checks": {
    "quadrupole_A": 0.7362204283754187,
    "quadrupole_B": -0.7362204283754186,
    "quadrupole_transpose_antisymmetry_error": 1.1102230246251565e-16,
    "relative_energy_mismatch": 4.440892098500625e-16,
    "sorted_amplitude_max_mismatch": 2.7755575615628914e-17
  },
  "imprint": {
    "max_abs_psi": 0.10933524493152957,
    "max_phi": 0.0003394883141741534,
    "max_mu": 0.0005574986435013754,
    "phi_transpose_relative_l2": 4.850039700284275e-16,
    "mu_transpose_relative_l2": 5.5908302922144305e-16
  },
  "final_checkpoint_2000": {
    "expected_mu_decay_factor": 0.9801985752863286,
    "observed_mu_decay_factor_A": 0.9801985752862405,
    "observed_mu_decay_factor_B": 0.9801985752862404,
    "relative_mu_decay_error_A": 8.981923466585033e-14,
    "relative_mu_decay_error_B": 8.993249977892203e-14,
    "normalized_mu_shape_difference_A": 2.1143003862833887e-15,
    "normalized_mu_shape_difference_B": 2.085340205597396e-15,
    "mu_quadrupole_A": 0.8123392378661911,
    "mu_quadrupole_B": -0.8123392378661913,
    "mu_relative_signal_A": 0.9801985752862405,
    "phi_quadrupole_A": 0.6951014182027542,
    "phi_quadrupole_B": -0.6951014182027543,
    "phi_relative_signal_A": 0.5360370913933448,
    "max_abs_psi": 0.0
  },
  "gates": {
    "finite_all_checkpoints": true,
    "initial_energy": true,
    "initial_quadrupole_antisymmetry": true,
    "initial_sorted_amplitude": true,
    "mu_below_cap_guard": true,
    "mu_decay_matches_analytic": true,
    "mu_shape_preserved": true,
    "mu_transpose_symmetry": true,
    "opposite_mu_signs_when_signal_present": true,
    "opposite_phi_signs_when_signal_present": true,
    "phi_below_cap_guard": true,
    "phi_transpose_symmetry": true,
    "psi_below_cap_guard": true,
    "source_off_psi_zero": true
  },
  "runner_sha256": "b9e2476469c3a9e97abcbee09b1ef4b10ba3e9984f3f2ba5bcdac7b4f427f0e7",
  "successful_output_sha256": "bd3ffa6985c20d2f0489dff69a751b3df27c313d294ed795efd44c9fd5f3c3fd",
  "verdict": "preflight_passed"
}
```

## 9. Complete executable verification code

```python
from dataclasses import dataclass, replace
import json, math, platform, sys, time
import numpy as np

@dataclass(frozen=True)
class C:
    dt: float=.1; psi_diffusion: float=.05; phi_diffusion: float=.05
    reaction_strength: float=.0007; drift_strength: float=0.
    mu_eta: float=.005; mu_rho: float=.0001; mu_cap: float=10.
    mu_peak_cutoff_ratio: float=.1; psi_amp_cap: float=1e6; phi_cap: float=1e6

def lap(a):
    return np.roll(a,1,0)+np.roll(a,-1,0)+np.roll(a,1,1)+np.roll(a,-1,1)-4*a

def step(s,c):
    p=np.asarray(s["psi"],complex).copy(); f=np.asarray(s["phi"],float).copy()
    m=np.asarray(s["mu"],float).copy(); k=np.asarray(s["kappa"],float)
    mul=1+m; fi=np.clip(f,0,10)
    q=.1*np.tanh((.04*fi*k*mul)/.1)*p; q/=1+np.abs(q)/10
    gy,gx=np.gradient(f); flow=c.drift_strength*(gy+1j*gx)*k*mul
    flow/=1+np.abs(flow)/10
    p+=flow*c.dt
    mag=np.abs(p); z=mag>c.psi_amp_cap
    if np.any(z): p[z]*=c.psi_amp_cap/(mag[z]+1e-30)
    p+=q*c.dt; p-=.005*p*c.dt; p+=c.psi_diffusion*lap(p)*k*c.dt
    e=np.abs(p)**2; a=c.reaction_strength*(128/p.shape[0])**2
    f+=k*a*(e-f)*c.dt; f+=k*c.phi_diffusion*.05*lap(f)*c.dt
    f=np.clip(f,0,c.phi_cap)
    floor=c.mu_peak_cutoff_ratio
    if 0<floor<1: floor*=float(np.max(e))
    m+=c.mu_eta*np.maximum(e-floor,0)*k*mul*c.dt; m-=c.mu_rho*m*c.dt
    m=np.clip(m,0,c.mu_cap)
    if not all(np.all(np.isfinite(x)) for x in (p,f,m)): raise FloatingPointError
    if np.max(np.abs(p))>=.99*c.psi_amp_cap: raise FloatingPointError
    return {"psi":p,"phi":f,"mu":m,"kappa":k.copy()}

def xy(n):
    a=np.arange(n,dtype=float)-(n-1)/2
    return np.meshgrid(a,a,indexing="xy")

def norm(a):
    return np.asarray(a,complex)/math.sqrt(float(np.sum(np.abs(a)**2)))

def pair(n=64,sep=12.,w=3.5):
    x,y=xy(n); g=lambda dx,dy: np.exp(-(dx*dx+dy*dy)/(2*w*w))
    return norm(g(x-sep/2,y)+g(x+sep/2,y)),norm(g(x,y-sep/2)+g(x,y+sep/2))

def quad(a):
    a=np.maximum(np.asarray(a,float),0); t=float(a.sum())
    if t<=0:return 0.
    x,y=xy(a.shape[0]); cx=float((a*x).sum()/t); cy=float((a*y).sum()/t)
    dx=x-cx;dy=y-cy
    return float((a*(dx*dx-dy*dy)).sum()/((a*(dx*dx+dy*dy)).sum()+1e-30))

def rms(a): return float(np.sqrt(np.mean(np.abs(a)**2)))
def rel(a,b): return float(np.linalg.norm(a-b)/(np.linalg.norm(a)+1e-30))
def shape(a,b):
    na=float(np.linalg.norm(a));nb=float(np.linalg.norm(b))
    return 0. if na==nb==0 else float(np.linalg.norm(a/na-b/nb))

def cm(a,b,ra,rb):
    qa,qb=quad(a),quad(b); xa,xb=rms(a),rms(b)
    pa="A" if qa>1e-6 else ("B" if qa<-1e-6 else "U")
    pb="A" if qb>1e-6 else ("B" if qb<-1e-6 else "U")
    return {"rms_A":xa,"rms_B":xb,"relative_signal_A":xa/(ra+1e-30),
      "relative_signal_B":xb/(rb+1e-30),"quadrupole_A":qa,"quadrupole_B":qb,
      "prediction_A":pa,"prediction_B":pb,"opposite_correct_signs":pa=="A" and pb=="B",
      "max_A":float(a.max()),"max_B":float(b.max()),
      "finite":bool(np.all(np.isfinite(a)) and np.all(np.isfinite(b))),
      "transpose_relative_l2":rel(a,b.T)}

def main():
    t=time.perf_counter(); c=C(); pa,pb=pair(); n=64
    z=np.zeros((n,n)); k=np.ones((n,n))
    ea=float(np.sum(abs(pa)**2));eb=float(np.sum(abs(pb)**2))
    initial={"relative_energy_mismatch":abs(ea-eb)/max(ea,eb),
      "sorted_amplitude_max_mismatch":float(np.max(np.abs(np.sort(abs(pa).ravel())-np.sort(abs(pb).ravel())))),
      "quadrupole_A":quad(abs(pa)**2),"quadrupole_B":quad(abs(pb)**2)}
    initial["quadrupole_transpose_antisymmetry_error"]=abs(initial["quadrupole_A"]+initial["quadrupole_B"])
    sa={"psi":pa,"phi":z,"mu":z,"kappa":k};sb={"psi":pb,"phi":z,"mu":z,"kappa":k}
    mxp=max(np.max(abs(pa)),np.max(abs(pb)));mxf=mxm=0.
    for _ in range(120):
        sa=step(sa,c);sb=step(sb,c)
        mxp=max(mxp,float(np.max(abs(sa["psi"]))),float(np.max(abs(sb["psi"]))))
        mxf=max(mxf,float(sa["phi"].max()),float(sb["phi"].max()))
        mxm=max(mxm,float(sa["mu"].max()),float(sb["mu"].max()))
    rr={"phi_A":rms(sa["phi"]),"phi_B":rms(sb["phi"]),"mu_A":rms(sa["mu"]),"mu_B":rms(sb["mu"])}
    imprint={"A":{"max_abs_psi":mxp,"max_phi":mxf,"max_mu":mxm},
      "B":{"max_abs_psi":mxp,"max_phi":mxf,"max_mu":mxm},"rms":rr,
      "phi_transpose_relative_l2":rel(sa["phi"],sb["phi"].T),
      "mu_transpose_relative_l2":rel(sa["mu"],sb["mu"].T)}
    ma0,mb0=sa["mu"].copy(),sb["mu"].copy()
    sa["psi"][:]=0;sb["psi"][:]=0;off=replace(c,mu_eta=0)
    cps=[0,100,500,1000,2000];out={};cur=0;mxoff=0.
    for cp in cps:
        for _ in range(cp-cur):
            sa=step(sa,off);sb=step(sb,off)
            mxoff=max(mxoff,float(np.max(abs(sa["psi"]))),float(np.max(abs(sb["psi"]))))
            mxf=max(mxf,float(sa["phi"].max()),float(sb["phi"].max()))
            mxm=max(mxm,float(sa["mu"].max()),float(sb["mu"].max()))
        cur=cp;ex=(1-c.mu_rho*c.dt)**cp
        oa=rms(sa["mu"])/(rr["mu_A"]+1e-30);ob=rms(sb["mu"])/(rr["mu_B"]+1e-30)
        out[str(cp)]={"phi":cm(sa["phi"],sb["phi"],rr["phi_A"],rr["phi_B"]),
          "mu":cm(sa["mu"],sb["mu"],rr["mu_A"],rr["mu_B"]),
          "max_abs_psi":max(float(np.max(abs(sa["psi"]))),float(np.max(abs(sb["psi"])))),
          "expected_mu_decay_factor":ex,"observed_mu_decay_factor_A":oa,
          "observed_mu_decay_factor_B":ob,"relative_mu_decay_error_A":abs(oa-ex)/(ex+1e-30),
          "relative_mu_decay_error_B":abs(ob-ex)/(ex+1e-30),
          "normalized_mu_shape_difference_A":shape(sa["mu"],ma0),
          "normalized_mu_shape_difference_B":shape(sb["mu"],mb0)}
    gates={"initial_energy":initial["relative_energy_mismatch"]<=1e-14,
      "initial_sorted_amplitude":initial["sorted_amplitude_max_mismatch"]<=1e-14,
      "initial_quadrupole_antisymmetry":initial["quadrupole_transpose_antisymmetry_error"]<=1e-12,
      "finite_all_checkpoints":all(out[str(x)]["phi"]["finite"] and out[str(x)]["mu"]["finite"] for x in cps),
      "source_off_psi_zero":mxoff<=1e-15,"psi_below_cap_guard":mxp<.1*c.psi_amp_cap,
      "phi_below_cap_guard":mxf<.1*c.phi_cap,"mu_below_cap_guard":mxm<.25*c.mu_cap,
      "opposite_phi_signs_when_signal_present":all(out[str(x)]["phi"]["opposite_correct_signs"] for x in cps),
      "opposite_mu_signs_when_signal_present":all(out[str(x)]["mu"]["opposite_correct_signs"] for x in cps),
      "mu_decay_matches_analytic":all(max(out[str(x)]["relative_mu_decay_error_A"],out[str(x)]["relative_mu_decay_error_B"])<=1e-12 for x in cps),
      "mu_shape_preserved":all(max(out[str(x)]["normalized_mu_shape_difference_A"],out[str(x)]["normalized_mu_shape_difference_B"])<=1e-12 for x in cps),
      "phi_transpose_symmetry":all(out[str(x)]["phi"]["transpose_relative_l2"]<=1e-12 for x in cps),
      "mu_transpose_symmetry":all(out[str(x)]["mu"]["transpose_relative_l2"]<=1e-12 for x in cps)}
    return {"environment":{"python":sys.version,"numpy":np.__version__,"platform":platform.platform(),
      "machine":platform.machine(),"processor":platform.processor()},
      "configuration":{"grid_size":64,"separation":12.,"width":3.5,"shift":[0,0],
      "imprint_steps":120,"source_off_checkpoints":cps,"dt":c.dt,"mu_eta_imprint":c.mu_eta,
      "mu_eta_source_off":off.mu_eta,"mu_rho":c.mu_rho,"mu_cap":c.mu_cap},
      "initial_checks":initial,"imprint":imprint,"source_off":out,
      "maxima":{"max_source_off_abs_psi":mxoff,"max_phi_all_phases":mxf,"max_mu_all_phases":mxm},
      "gates":{k:bool(v) for k,v in gates.items()},"verdict":"preflight_passed" if all(gates.values()) else "preflight_invalid",
      "wall_clock_seconds":time.perf_counter()-t}

if __name__=="__main__": print(json.dumps(main(),indent=2,sort_keys=True))
```

## 10. Narrow verdict

`preflight_passed` in the declared standalone NumPy `2.3.5` runtime.

The implementation did this:

- imprinted source-dependent spatial structure into `phi` and `mu`;
- removed `psi` exactly for the passive phase;
- preserved `mu` shape while multiplying it by the declared decay factor;
- diffused and decayed `phi` while preserving the tested orientation sign.

The reproducible run observed this:

- one equal-energy orientation pair remained distinguishable in both `phi` and `mu` through the final checkpoint;
- no cap, source regeneration, transpose asymmetry, non-finite value, or analytic-decay mismatch invalidated the lane.

The allowed interpretation is limited to this statement:

> The frozen current-engine operations can mechanically deposit and passively retain the selected one-pair orientation trace under the declared deterministic finite-grid conditions.

## 11. What remains unproved

This preflight does not establish:

- held-out population-level information retention;
- robustness to translations, widths, separations, noise, resolution, timestep, or boundary changes;
- causal reuse of the retained trace;
- active-Core equivalence in a repository-supported dependency environment;
- permanent memory;
- quantum information preservation;
- a genuine attractor;
- galactic history dependence;
- a connection to black holes, gravity, dark matter, consciousness, or real-universe physics;
- a reason to modify a whitepaper or equation.

## 12. Cross-question impact and next gates

- **Q3 information retention:** `supports` preparation of the full held-out P1 population and later causal-echo lanes; it does not itself satisfy Q3.
- **Q2 saturation/attraction:** `unaffected` except that no cap confound appeared in this tiny lane; passive exponential decay is not attraction.
- **Q1 galactic response:** `unaffected` directly; a radial assembly-history test becomes meaningful only after a retained channel demonstrates causal reuse.
- **Real universe:** `not_yet_connected`.

The project owner subsequently selected an additional Q1 comparator step: independently reconstruct the publicly described TOLOG hyperbolic-tangent galactic fit as an isolated external benchmark, then reverse-engineer which general response properties an emergent Lineum foam/field/vortex mechanism would need to replace. That comparator must use only independently retrievable public sources and public astronomical data. It may not use, reconstruct, paraphrase, or search from any privately uploaded TOLOG document.

The full P1 population remains open and is not superseded by the comparator step.
