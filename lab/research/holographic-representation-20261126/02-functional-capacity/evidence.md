# Equal-budget functional capacity — independent reference diagnostic

2026-11-26. Lina EI Issue #69, E0-A OPEN. Source-only exploratory continuation of the projection ambiguity and spatial material relation diagnostics. No native physics run, learning, Core alteration or live owner action. Uses the previously specified independent 4-real-field linear 8x8x9 reflecting diffusion/exchange reference; coefficients and selected task intentionally engineered. The mean map is an exact closed subsystem of this linear reference: depth diffusion cancels in the sum and exchange is local. The spectral alternative is a conventional geometry-aware low-mode encoding, NOT spontaneous encoding by the Grid. Both reduced representations store 256 scalar values vs 2304 full state; full 3D input is available to the initial encoder, no actual equivalent-compute gain asserted. Two symmetric external test pulses, 48 unseen initial states plus their depth reflections, 96 trajectories. Near/far sign is an observer-defined physical discrimination endpoint, not memory or useful learned relay. Pooled depth-mean error at most 2.3e-15 absolute. Depth mean classification at chance (ties half-credit); the equal-budget spectral alternative achieves 83.33/87.5% at tick 4, 91.67/100% at tick 16, and 100% in both families at ticks 32 and 64. At tick 64 its relative face contrast L2 error is 1.6983% iid and 0.6054% smooth; depth mean map error 1.6487% and 0.5074%. Full spectral and direct stencil parity and reflection controls pass. This is the consequence of dissipative removal of high modes in the linear reference, not proof that native four fields encode missing spatial information. No noise or training, no geometry-free reconstruction. Repeat identical JSON verified, independent modal-vs-stencil check (not independent full implementation of whole experiment). Do not promote H11/H4/E0-A. Next native discriminator requires actual learned histories, identical withheld cues and resolution/equal resource controls; native operator and admission preflight remain outstanding. No new law.

## protocol.md

```text
# Functional capacity at equal scalar state budget — prospective protocol
2026-11-26; isolated reference diagnostic for Lina EI #69, E0-A open. No live Grid, original Core, or asset modification. Reuse the prior independent four-real-field 8x8x9 linear reflecting diffusion/exchange model (not Lineum or Lina native). New discriminator: useful response prediction rather than complete reconstruction. Compare exact depth-mean 2D evolution (256 scalars), equal-size conventional spectral reduced-order model (4x4 spatial low modes, 4 depth modes, four fields = 256 scalars), and first-state persistence baseline. Full reference 2304 scalars. Initial encoders see the full reference state; spectral encoder explicitly uses reference geometry. Neither implies an emergent representation. Model time 64 steps with identical held-out center-depth positive local pulse at ticks 0 and 16, into the first field, different positions. Record at ticks 4,16 (before second pulse),32,64. 24 iid and 24 smooth novel arrays, each paired with its depth reflection (96 cases), fixed RNG seed 481926; smooth uses 7 reference steps and per-field scale normalization. Observations: all-channel depth-mean map; first-minus-last depth face map (depth-direction information); classify sign of the spatial mean of first-field face contrast. Mirror pair gives equal mean and opposite contrast under symmetric sources. Evaluate pooled relative L2 error and accuracy; ties receive half credit, balanced classes by construction; numerical tie tolerance 1e-12. Record per-family/horizon results and maximum reference-vs-reduced mean difference, reflection symmetry, exact independent full spectral vs stencil parity. Primary falsifier for universal equal-budget capacity: a reduced mean map cannot classify a nonzero depth-direction sign for mirror pairs. Require mean error <1e-12 and no more than chance depth-sign accuracy for mean-only; spectral baseline not assumed to win both. No noise, no learned history, no claim about actual memory or compute savings. Storage counts exclude shared model coefficients and temporary arrays; wall clock is not a capacity-matched benchmark. No post-result retuning.
```

## experiment.py

```python
"""Equal-budget functional projection control; not native Lineum or Lina physics."""
from pathlib import Path
import json, platform, time
import numpy as np
from scipy.fft import dctn, idctn
from scipy.linalg import eigh

N,D,C=8,9,4
R=np.array([.045,.065,.085,.025])
M=np.array([[0,.012,0,.009],[.012,0,.015,0],[0,.015,0,.011],[.009,0,.011,0]])
M=M-np.diag(M.sum(axis=1))
T=64
TIMES=(4,16,32,64)

def lap(a,axis):
    p=np.pad(a,[(1,1) if i==axis else (0,0) for i in range(a.ndim)],mode='edge')
    return np.take(p,np.arange(a.shape[axis]),axis=axis)+np.take(p,np.arange(2,a.shape[axis]+2),axis=axis)-2*a

def step(a):
    return a+R.reshape((1,C)+(1,)*(a.ndim-2))*sum(lap(a,i) for i in range(2,a.ndim))+np.einsum('ij,bj...->bi...',M,a)

def enc(a):
    return dctn(a,axes=(2,3,4),norm='ortho')[:,:,:4,:4,:4].copy()

def dec(z):
    padded=np.zeros((len(z),C,D,N,N))
    padded[:,:,:z.shape[2],:z.shape[3],:z.shape[4]]=z
    return idctn(padded,axes=(2,3,4),norm='ortho')

def matrices(d,n):
    lam=lambda k: -4*np.sin(np.pi*np.arange(k)/(2*k))**2
    eig=lam(D)[:d,None,None]+lam(N)[None,:n,None]+lam(N)[None,None,:n]
    return np.eye(C)[None,None,None,:,:]+M[None,None,None,:,:]+eig[:,:,:,None,None]*np.diag(R)[None,None,None,:,:]

def modal_step(z,A):
    return np.einsum('zyxij,bjzyx->bizyx',A,z)

def targets(a):
    return a.mean(axis=2),a[:,:,0]-a[:,:,-1]

def metrics(pred,true):
    d=pred-true
    return float(np.linalg.norm(d)/max(np.linalg.norm(true),1e-30))

def accuracy(a,b):
    s=a[:,0].mean(axis=(1,2)); t=b[:,0].mean(axis=(1,2))
    assert np.min(np.abs(t))>1e-12
    return float(np.mean(np.where(np.abs(s)<1e-12,.5,np.sign(s)==np.sign(t))))

rng=np.random.default_rng(481926)
rows=[]; checks=[]
for family in ('iid','smooth'):
    a=rng.normal(size=(24,C,D,N,N))
    if family=='smooth':
        for _ in range(7):a=step(a)
        a/=a.std(axis=(2,3,4),keepdims=True)
    a=np.concatenate([a,a[:,:,::-1]],axis=0)
    mean=a.mean(axis=2); z=enc(a); full=dctn(a,axes=(2,3,4),norm='ortho')
    pmean,pcontrast=targets(a)
    A=matrices(4,4); Afull=matrices(D,N)
    assert mean[0].size==z[0].size==256 and a[0].size==2304
    for tick in range(T+1):
        if tick in TIMES:
            mt,ct=targets(a); sm,sc=targets(dec(z))
            parity=float(np.max(abs(idctn(full,axes=(2,3,4),norm='ortho')-a)))
            mirror=float(np.max(abs(mt[:24]-mt[24:])))
            anti=float(np.max(abs(ct[:24]+ct[24:])))
            meanerr=float(np.max(abs(mean-mt)))
            checks.append(dict(family=family,tick=tick,full_spectral_parity=parity,mirror_mean=mirror,mirror_contrast=anti,mean_error=meanerr))
            assert max(parity,mirror,anti,meanerr)<1e-12
            for name,pm,pc in [('depth_mean',mean,np.zeros_like(ct)),('spectral_256',sm,sc),('persistence_256',pmean,np.zeros_like(ct))]:
                rows.append(dict(family=family,tick=tick,method=name,mean_nrmse=metrics(pm,mt),contrast_nrmse=metrics(pc,ct),depth_sign_accuracy=accuracy(pc,ct)))
        if tick==T:break
        if tick in (0,16):
            pulse=np.zeros_like(a)
            y,x=(2,5) if tick==0 else (5,2)
            pulse[:,0,D//2,y,x]=.5
            a+=pulse; mean+=pulse.mean(axis=2); z+=enc(pulse); full+=dctn(pulse,axes=(2,3,4),norm='ortho')
        a=step(a);mean=step(mean);z=modal_step(z,A);full=modal_step(full,Afull)
assert all(r['depth_sign_accuracy']==.5 and r['mean_nrmse']<1e-12 for r in rows if r['method']=='depth_mean')
out=dict(protocol='functional equal-state-budget reference only',seed=481926,cases=96,state_scalars={'full':2304,'depth_mean':256,'spectral_256':256,'persistence_256':256},rows=rows,checks=checks,environment={'python':platform.python_version(),'numpy':np.__version__})
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
```

## results.json

```json
{
  "protocol": "functional equal-state-budget reference only",
  "seed": 481926,
  "cases": 96,
  "state_scalars": {
    "full": 2304,
    "depth_mean": 256,
    "spectral_256": 256,
    "persistence_256": 256
  },
  "rows": [
    {
      "family": "iid",
      "tick": 4,
      "method": "depth_mean",
      "mean_nrmse": 2.444339249978762e-16,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "iid",
      "tick": 4,
      "method": "spectral_256",
      "mean_nrmse": 0.6858557526866532,
      "contrast_nrmse": 0.7228492098574828,
      "depth_sign_accuracy": 0.8333333333333334
    },
    {
      "family": "iid",
      "tick": 4,
      "method": "persistence_256",
      "mean_nrmse": 1.2085729224217876,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "iid",
      "tick": 16,
      "method": "depth_mean",
      "mean_nrmse": 3.0548309741877264e-16,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "iid",
      "tick": 16,
      "method": "spectral_256",
      "mean_nrmse": 0.3361567122600172,
      "contrast_nrmse": 0.37088453683789524,
      "depth_sign_accuracy": 0.9166666666666666
    },
    {
      "family": "iid",
      "tick": 16,
      "method": "persistence_256",
      "mean_nrmse": 4.0123697638017095,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "iid",
      "tick": 32,
      "method": "depth_mean",
      "mean_nrmse": 3.189417885703993e-16,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "iid",
      "tick": 32,
      "method": "spectral_256",
      "mean_nrmse": 0.12765649231702822,
      "contrast_nrmse": 0.13338175356748055,
      "depth_sign_accuracy": 1.0
    },
    {
      "family": "iid",
      "tick": 32,
      "method": "persistence_256",
      "mean_nrmse": 6.992367818420763,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "iid",
      "tick": 64,
      "method": "depth_mean",
      "mean_nrmse": 3.0699465959930933e-16,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "iid",
      "tick": 64,
      "method": "spectral_256",
      "mean_nrmse": 0.016487497295605457,
      "contrast_nrmse": 0.016982795054837272,
      "depth_sign_accuracy": 1.0
    },
    {
      "family": "iid",
      "tick": 64,
      "method": "persistence_256",
      "mean_nrmse": 11.071504499973168,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "smooth",
      "tick": 4,
      "method": "depth_mean",
      "mean_nrmse": 1.8965356793178764e-16,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "smooth",
      "tick": 4,
      "method": "spectral_256",
      "mean_nrmse": 0.3270193579762924,
      "contrast_nrmse": 0.3569062565377461,
      "depth_sign_accuracy": 0.875
    },
    {
      "family": "smooth",
      "tick": 4,
      "method": "persistence_256",
      "mean_nrmse": 0.41371069241722186,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "smooth",
      "tick": 16,
      "method": "depth_mean",
      "mean_nrmse": 2.2178605840494923e-16,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "smooth",
      "tick": 16,
      "method": "spectral_256",
      "mean_nrmse": 0.13370517066110826,
      "contrast_nrmse": 0.15056072657035235,
      "depth_sign_accuracy": 1.0
    },
    {
      "family": "smooth",
      "tick": 16,
      "method": "persistence_256",
      "mean_nrmse": 1.4295552495188093,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "smooth",
      "tick": 32,
      "method": "depth_mean",
      "mean_nrmse": 2.300922546280209e-16,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "smooth",
      "tick": 32,
      "method": "spectral_256",
      "mean_nrmse": 0.04413410879410715,
      "contrast_nrmse": 0.05081196053916916,
      "depth_sign_accuracy": 1.0
    },
    {
      "family": "smooth",
      "tick": 32,
      "method": "persistence_256",
      "mean_nrmse": 2.4309700059064347,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "smooth",
      "tick": 64,
      "method": "depth_mean",
      "mean_nrmse": 2.279982166758519e-16,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    },
    {
      "family": "smooth",
      "tick": 64,
      "method": "spectral_256",
      "mean_nrmse": 0.005074362642481196,
      "contrast_nrmse": 0.006054232575147608,
      "depth_sign_accuracy": 1.0
    },
    {
      "family": "smooth",
      "tick": 64,
      "method": "persistence_256",
      "mean_nrmse": 3.681071287078424,
      "contrast_nrmse": 1.0,
      "depth_sign_accuracy": 0.5
    }
  ],
  "checks": [
    {
      "family": "iid",
      "tick": 4,
      "full_spectral_parity": 1.7763568394002505e-15,
      "mirror_mean": 2.220446049250313e-16,
      "mirror_contrast": 0.0,
      "mean_error": 3.3306690738754696e-16
    },
    {
      "family": "iid",
      "tick": 16,
      "full_spectral_parity": 8.881784197001252e-16,
      "mirror_mean": 1.1102230246251565e-16,
      "mirror_contrast": 0.0,
      "mean_error": 1.942890293094024e-16
    },
    {
      "family": "iid",
      "tick": 32,
      "full_spectral_parity": 6.661338147750939e-16,
      "mirror_mean": 5.551115123125783e-17,
      "mirror_contrast": 0.0,
      "mean_error": 1.1102230246251565e-16
    },
    {
      "family": "iid",
      "tick": 64,
      "full_spectral_parity": 5.551115123125783e-16,
      "mirror_mean": 2.7755575615628914e-17,
      "mirror_contrast": 0.0,
      "mean_error": 6.938893903907228e-17
    },
    {
      "family": "smooth",
      "tick": 4,
      "full_spectral_parity": 2.220446049250313e-15,
      "mirror_mean": 4.440892098500626e-16,
      "mirror_contrast": 0.0,
      "mean_error": 6.661338147750939e-16
    },
    {
      "family": "smooth",
      "tick": 16,
      "full_spectral_parity": 1.9984014443252818e-15,
      "mirror_mean": 3.3306690738754696e-16,
      "mirror_contrast": 0.0,
      "mean_error": 4.440892098500626e-16
    },
    {
      "family": "smooth",
      "tick": 32,
      "full_spectral_parity": 1.7763568394002505e-15,
      "mirror_mean": 2.220446049250313e-16,
      "mirror_contrast": 0.0,
      "mean_error": 3.3306690738754696e-16
    },
    {
      "family": "smooth",
      "tick": 64,
      "full_spectral_parity": 1.887379141862766e-15,
      "mirror_mean": 1.1102230246251565e-16,
      "mirror_contrast": 0.0,
      "mean_error": 2.220446049250313e-16
    }
  ],
  "environment": {
    "python": "3.13.5",
    "numpy": "2.3.5"
  }
}
```

## manifest.json

```json
{
  "protocol.md": "06a157c8acd0b2118fb26f037cb53886cc258be990c7938171d76715e0176e63",
  "experiment.py": "1c7ba711f5e2ac29f5b8009ee825d067e679b644db901d65f3db4ba20ef81bf7",
  "results.json": "d7f40f389520ba3bbbc3c0840afb683cf1546239e93df3fefe08f08d37ada055",
  "stdout.json": "d7f40f389520ba3bbbc3c0840afb683cf1546239e93df3fefe08f08d37ada055",
  "repeat.json": "d7f40f389520ba3bbbc3c0840afb683cf1546239e93df3fefe08f08d37ada055"
}
```

