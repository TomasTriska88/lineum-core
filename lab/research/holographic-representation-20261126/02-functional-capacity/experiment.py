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
