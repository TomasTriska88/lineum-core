# Lineum-Native Galactic Radial-Locking: Lane A Baseline Receipt

**Status:** active  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-08-04  
**Scope:** first deterministic baseline receipt for the preregistered Lineum-native radial-locking test  
**Current confidence:** high for reproduction of the extracted NumPy path; low for mechanism identification until mandatory controls are complete  
**Operational task:** ClickUp task `869edcdkk`

## 1. Lineage and boundary

Root programme: `research/lineum-native-field-stress-tests.md`, version 0.1.0.  
Parent protocol: `research/lineum-native-galactic-radial-locking-test.md`, version 0.2.0.

This child receipt records only Lane A. It contains no external private theory, manuscript, equation, or unpublished dataset.

## 2. Plain-language result

The baseline did **not** produce the preregistered outer radial-locking shape.

The generated `phi` field remained finite and temporally steady, and a non-zero radial gradient reached the outer band. The velocity-like proxy nevertheless fell sharply instead of forming an approximately level plateau.

This is a preliminary bounded negative result for one frozen initialization and parameter regime, not a universal conclusion about Lineum.

## 3. Frozen implementation and environment

Repository: `TomasTriska88/lineum-core`  
Branch: `develop`  
Parent protocol endpoint before this run: `5466c8fcd68dae91b451fce4ed21e0b979b47210`  
Frozen engine file: `lineum_core/math.py`  
Frozen engine blob SHA: `bb877021810691223a0eb960a45493a2e351112a`

The environment could not clone the repository because outbound DNS was unavailable. The run therefore used a lane-specific extraction of every current NumPy `_step_numpy` operation reached by Lane A. Unreached noise, `mu`, fallback-reaction, PyTorch, and wave branches were omitted.

This is not yet a direct package-import reproduction. The extracted arithmetic was executed twice in fresh processes using two separately assembled scripts.

Execution facts:

```text
backend = NumPy CPU
dtype = float64 / complex128
grid = 128 x 128
periodic roll boundaries = enabled
random input = none
steps = 2000
retained samples = every 10 steps from 1600 through 2000
sample count = 41
```

## 4. Metric clarification

The parent protocol did not spell out the normalization used by `plateau_slope`. Before interpreting the result it was frozen as:

```text
x = (r - 24) / 16
y = v_phi / mean(v_phi)
plateau_slope = OLS slope of y against x for 24 <= r <= 40
```

The same definition is mandatory for Lane B and all direct comparisons in this protocol version.

## 5. Result

| Metric | Required | Observed | Result |
|---|---:|---:|---|
| `plateau_cv` | `<= 0.10` | `1.17279504274407` | fail |
| `abs(plateau_slope)` | `<= 0.15` | `3.36298790808512` | fail |
| `gradient_log_slope` | `[-1.25, -0.75]` | `-20.4566513290255` | fail |
| `temporal_cv` | `<= 0.10` | `0.0459401725708738` | pass |
| `radial_signal_ratio` | `>= 10` | `4687014.26630595` | pass |
| numerical stability | finite, no reset/cap | finite | pass |

Additional observations:

```text
outer_g_mean = 4.7471018940855483e-10
far_g_mean = 1.0128200223779039e-16
outer_v_mean = 7.1059796215675652e-05
max_abs_psi = 0.12015263413294726
max_phi = 0.00026979882026544868
max_mu = 0
```

Only three of six gates passed, so `candidate_signal_all_criteria = false`.

## 6. What the implementation computed

1. The NGC 3198 stellar surface-brightness profile initialized only the magnitude of complex `psi`.
2. Existing mode coupling transferred local `|psi|^2` into `phi`.
3. Existing `phi` diffusion and gradient feedback evolved the fields for 2000 updates.
4. The observer radially averaged `phi`, differentiated it, and computed `v_phi = sqrt(r * |d phi/dr|)`.

Observed in the run:

- finite fields with no reset or cap approach;
- a non-zero outer gradient;
- stable late-time band mean;
- a steeply declining rather than flat outer proxy.

## 7. Narrow interpretation

Supported:

> Current default deterministic Lineum NumPy dynamics, under this exact input encoding and parameter regime, did not produce the preregistered dimensionless radial-locking proxy after 2000 updates.

Not established:

- failure of all Lineum configurations or historical equation families;
- failure of the `mu` memory channel;
- uniqueness or physical validity of the observer;
- any physical statement about gravity, dark matter, lensing, or km/s.

## 8. Failure-to-mechanism ledger

Failed: the plateau shape.

Remained positive:

- stable non-zero outer response;
- temporal steadiness;
- no numerical-cap dependence.

The failure location remains unresolved among equation regime, parameter regime, disk encoding, observer, and finite-grid geometry.

Registered repair classes, not yet selected or tuned:

1. feedback strength or sign;
2. structural memory through `mu`;
3. another historically relevant Lineum equation family;
4. a different identifying observer;
5. scaling or boundary effects.

The cheapest frozen discriminator remains Lane B with drift removed.

## 9. Reproduction receipts

Full extracted runner SHA-256: `e9b2250ea81103f19a33c1ae9e34a4efc69754494553eb7ecc5c3ddee99ec85e`  
Full output SHA-256: `07e09a69a0af9138f2a0d5f2484288b99fead821aaaf90cb18d0b0b2618d6a06`  
Compact runner SHA-256: `d9dab20771fa91b85e38b24659f0106852bef43f17536fa18a4f148c99c017cc`  
Compact output SHA-256: `7070ecba23fbef5675da88413d8a5c5301cc419df6b7337ca1226f60cf8a3061`

Both fresh-process runs agreed on every scientific metric to floating-point precision. This checks reproduction of the same arithmetic, not an independent numerical method.

## 10. Executable reproduction code

```python
import json, time
import numpy as np

R=np.array([0.32,0.64,0.96,1.28,1.61,1.93,2.24,2.57,2.89,3.21,3.54,3.85,4.17,4.50,4.82,5.15,5.46,5.78,6.10,6.43,6.74,7.06,8.04,9.04,10.04,11.04,12.05,14.05,16.07,18.13,20.05,22.12,24.03,26.10,28.16,30.08,32.14,34.06,36.12,38.19,40.10,42.17,44.08],float)
SB=np.array([1084.92,590.57,410.97,329.34,268.62,247.67,227.56,205.02,200.20,208.58,208.47,196.07,179.96,164.19,150.99,138.08,126.00,113.63,101.19,86.52,70.23,57.67,40.74,31.83,26.64,21.02,15.42,6.42,2.95,2.39,1.44,0.72,0.28,0.16,0.08,0.04,0.02,0.01,0.01,0.00,0.00,0.00,0.00],float)

N=128; DT=1.; PD=.05; FD=.05; DRIFT=-.004; COUPLING=.001
yy,xx=np.indices((N,N),dtype=float); c=(N-1)/2; rr=np.hypot(xx-c,yy-c)
rk=rr*(R[-1]/44.0)
psi=(.25*np.interp(rk,R,SB,left=SB[0],right=0.)/SB.max()).astype(complex)
phi=np.zeros((N,N)); k=np.ones((N,N)); mu=np.zeros((N,N))

def lap(f):
    return PD*(np.roll(f,1,0)+np.roll(f,-1,0)+np.roll(f,1,1)+np.roll(f,-1,1)-4*f)

def phi_lap(f):
    return .05*(np.roll(f,1,0)+np.roll(f,-1,0)+np.roll(f,1,1)+np.roll(f,-1,1)-4*f)

def step(psi,phi):
    dm=1.+mu
    pint=np.clip(phi,0.,10.)
    interaction=.1*np.tanh((.04*pint*k*dm)/.1)*psi
    interaction/=1.+np.abs(interaction)/10.
    gx,gy=np.gradient(phi)
    flow=DRIFT*(gx+1j*gy)*k*dm
    flow/=1.+np.abs(flow)/10.
    psi=psi+flow*DT
    psi=psi+interaction*DT
    psi=psi-.005*psi*DT
    psi=psi+lap(psi)*k*DT
    e=np.abs(psi)**2
    de=COUPLING*e*k*DT
    phi=phi+de
    psi=(psi/(np.sqrt(e)+1e-12))*np.sqrt(np.maximum(e-de,0.))
    phi=phi+k*FD*phi_lap(phi) # legacy per-update semantics
    phi=np.clip(phi,0.,1e6)
    return psi,phi

bins=np.floor(rr).astype(int)
def radial(a):
    s=np.bincount(bins.ravel(),weights=a.ravel(),minlength=57)
    n=np.bincount(bins.ravel(),minlength=57)
    return np.divide(s[:57],n[:57],out=np.zeros(57),where=n[:57]>0)
def observe(phi):
    p=radial(phi); r=np.arange(57.,dtype=float)
    g=np.abs(np.gradient(p)); v=np.sqrt(np.maximum(r*g,0.))
    b=(r>=24)&(r<=40); f=(r>48)&(r<=56)
    x=(r[b]-24.)/16.; y=v[b]/(v[b].mean()+1e-300)
    pos=(r>0)&(g>0); ls=np.full(57,np.nan)
    ls[pos]=np.gradient(np.log(g[pos]),np.log(r[pos]))
    return p,g,v,{
      "plateau_cv":float(v[b].std()/(v[b].mean()+1e-300)),
      "plateau_slope":float(np.polyfit(x,y,1)[0]),
      "gradient_log_slope":float(np.nanmedian(ls[b])),
      "outer_g_mean":float(g[b].mean()),
      "far_g_mean":float(g[f].mean()),
      "radial_signal_ratio":float(g[b].mean()/max(g[f].mean(),np.finfo(float).tiny)),
      "outer_v_mean":float(v[b].mean())}

samples=[]; maxpsi=maxphi=0.; t=time.perf_counter()
for i in range(1,2001):
    psi,phi=step(psi,phi)
    maxpsi=max(maxpsi,float(np.abs(psi).max()))
    maxphi=max(maxphi,float(phi.max()))
    if i>=1600 and i%10==0: samples.append((i,observe(phi)[3]["outer_v_mean"]))
p,g,v,m=observe(phi)
tv=np.array([x[1] for x in samples])
m["temporal_cv"]=float(tv.std()/(tv.mean()+1e-300))
criteria={
 "plateau_cv":m["plateau_cv"]<=.10,
 "plateau_slope":abs(m["plateau_slope"])<=.15,
 "gradient_log_slope":-1.25<=m["gradient_log_slope"]<=-.75,
 "temporal_cv":m["temporal_cv"]<=.10,
 "radial_signal_ratio":m["radial_signal_ratio"]>=10.,
 "numerical_stability":bool(np.isfinite(psi).all() and np.isfinite(phi).all() and np.abs(psi).max()<.99e6)}
out={"lane":"A","frozen_math_blob_sha":"bb877021810691223a0eb960a45493a2e351112a","grid":128,"steps":2000,"retention":"every 10 steps from 1600 through 2000 inclusive","runtime_seconds":time.perf_counter()-t,"max_abs_psi":maxpsi,"max_phi":maxphi,"max_mu":0.,"metrics":m,"criteria":criteria,"candidate_signal_all_criteria":all(criteria.values()),"profiles":{"r":list(range(57)),"phi_bar":p.tolist(),"g_phi":g.tolist(),"v_phi":v.tolist()},"temporal_samples":[{"step":i,"outer_v_mean":x} for i,x in samples]}
print(json.dumps(out,indent=2,sort_keys=True))
```

## 11. Machine-readable result

```json
{
  "candidate_signal_all_criteria": false,
  "criteria": {
    "gradient_log_slope": false,
    "numerical_stability": true,
    "plateau_cv": false,
    "plateau_slope": false,
    "radial_signal_ratio": true,
    "temporal_cv": true
  },
  "frozen_math_blob_sha": "bb877021810691223a0eb960a45493a2e351112a",
  "grid": 128,
  "lane": "A",
  "max_abs_psi": 0.12015263413294726,
  "max_mu": 0.0,
  "max_phi": 0.0002697988202654487,
  "metrics": {
    "far_g_mean": 1.0128200223779039e-16,
    "gradient_log_slope": -20.456651329025476,
    "outer_g_mean": 4.747101894085548e-10,
    "outer_v_mean": 7.105979621567565e-05,
    "plateau_cv": 1.1727950427440659,
    "plateau_slope": -3.3629879080851244,
    "radial_signal_ratio": 4687014.266305951,
    "temporal_cv": 0.04594017257087384
  },
  "retention": "every 10 steps from 1600 through 2000 inclusive",
  "steps": 2000
}
```

The executable code regenerates the complete radial and temporal profiles. The committed summary contains every value used for the declared pass/fail decision.

## 12. Root-programme impact

| Root question | Lane A impact |
|---|---|
| Q1 — Galactic radial locking | constrains the default deterministic baseline; no candidate signal |
| Q2 — Bounded saturation and attraction | finite execution observed; no attractor test |
| Q3 — Scalar minimum and information retention | unaffected |
| Compute question | local runtime recorded only; no external benchmark |

## 13. Next frozen discriminator

Lane B repeats the same run with only:

```text
drift_strength = 0
```

This determines whether the observed outer trace materially depends on `phi`-gradient feedback or mainly reflects passive diffusion and mode-coupling history. No later lane begins before Lane B is recorded.
