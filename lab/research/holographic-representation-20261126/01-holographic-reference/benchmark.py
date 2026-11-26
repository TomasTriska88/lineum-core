"""Independent 4-real-field reference; NOT Lineum Core or a proposed Core modification."""
import json, time, platform
from pathlib import Path
import numpy as np
from scipy.fft import dctn, idctn
from scipy.linalg import eigh
N,D,C=8,9,4
R=np.array([.045,.065,.085,.025])
# Symmetric source-neutral local exchange, deliberately chosen as a simple control.
M=np.array([[0,.012,0,.009],[.012,0,.015,0],[0,.015,0,.011],[.009,0,.011,0]])
M=M-np.diag(M.sum(axis=1))
T=80
TIMES=np.r_[np.arange(0,60,4),63]
assert len(TIMES)==16

def lap(a,axis):
    p=np.pad(a,[(1,1) if i==axis else (0,0) for i in range(a.ndim)],mode='edge')
    return np.take(p,np.arange(0,a.shape[axis]),axis=axis)+np.take(p,np.arange(2,a.shape[axis]+2),axis=axis)-2*a

def step(a):
    return a+R.reshape(1,C,1,1,1)*sum(lap(a,i) for i in (2,3,4))+np.einsum('ij,bjzyx->bizyx',M,a)

def simulate(a,steps=T):
    out=[a.copy()]
    for _ in range(steps): out.append(step(out[-1]))
    return np.stack(out,axis=1)

# Forward matrix in a spatial cosine basis; independent of direct physical-space stencil.
L=np.zeros((D,D))
for z in range(D-1):
    L[z,z]-=1;L[z+1,z+1]-=1;L[z,z+1]+=1;L[z+1,z]+=1
E=-4*np.sin(np.pi*np.arange(N)/(2*N))**2
Bmean=np.kron(np.eye(C),np.ones((1,D))/D)
Bfront=np.kron(np.eye(C),np.eye(D)[[0]])
methods={'mean_four':(Bmean,TIMES),'front_four':(Bfront,TIMES),'front_psi_equal_samples':(Bfront[[0]],np.arange(64))}
noise_levels=[0.,.001,.01]
solvers={}; ranks={}; singular={}; future={}; forward={}
for iy in range(N):
 for ix in range(N):
    A=np.eye(C*D)+np.kron(np.diag(R),L+(E[iy]+E[ix])*np.eye(D))+np.kron(M,np.eye(D))
    eig,U=eigh(A)
    future[iy,ix]=(U*eig**T)@U.T
    for method,(B,times) in methods.items():
        O=np.vstack([B@((U*eig**int(t))@U.T) for t in times]); forward[method,iy,ix]=O
        u,s,vh=np.linalg.svd(O,full_matrices=False)
        ranks[method,iy,ix]=int(np.sum(s>s[0]*1e-10));singular[method,iy,ix]=s.tolist()
        for noise in noise_levels:
            g=np.where(s>s[0]*1e-10,1/np.maximum(s,1e-300),0) if noise==0 else s/(s*s+noise*noise)
            solvers[method,noise,iy,ix]=(vh.T*g)@u.T

def project(traj,method):
    if method=='mean_four':return traj[:,TIMES].mean(axis=3)
    if method=='front_four':return np.take(traj,TIMES,axis=1)[:,:,:,0]
    return traj[:,:64,:1,0]

def recon(obs,method,noise):
    b=obs.shape[0]; spec=dctn(obs,axes=(-2,-1),norm='ortho').reshape(b,-1,N,N)
    res=np.empty((b,C*D,N,N)); pred=res.copy()
    for y in range(N):
      for x in range(N):
        res[:,:,y,x]=spec[:,:,y,x]@solvers[method,noise,y,x].T
        pred[:,:,y,x]=res[:,:,y,x]@future[y,x].T
    return idctn(res.reshape(b,C,D,N,N),axes=(-2,-1),norm='ortho'),idctn(pred.reshape(b,C,D,N,N),axes=(-2,-1),norm='ortho')

def advance(a):
    for _ in range(T):a=step(a)
    return a

def nrmse(a,b):return float(np.linalg.norm(a-b)/max(np.linalg.norm(b),1e-30))
rng=np.random.default_rng(20261126)
# Frozen seeds and two held-out ensembles; no fitted decoder training.
rows=[]
shuffle_rows=[]
shuffle_rng=np.random.default_rng(48251)
for ensemble in ['iid','smooth']:
    a=rng.normal(size=(24,C,D,N,N))
    if ensemble=='smooth':
        for _ in range(7):a=step(a)
        a/=np.std(a,axis=(2,3,4),keepdims=True)
    t0=time.perf_counter();traj=simulate(a);elapsed=time.perf_counter()-t0
    mirror=simulate(a[:,:,::-1]); symmetry=float(np.max(abs(traj.mean(axis=3)-mirror.mean(axis=3))))
    # Verify independently constructed linear observation matrices against reference.
    x=dctn(a,axes=(-2,-1),norm='ortho').reshape(len(a),C*D,N,N)
    oracle_error=0
    for method in methods:
        obs=project(traj,method);spec=dctn(obs,axes=(-2,-1),norm='ortho').reshape(len(a),-1,N,N)
        for y in range(N):
          for z in range(N):oracle_error=max(oracle_error,float(np.max(abs(spec[:,:,y,z]-x[:,:,y,z]@forward[method,y,z].T))))
        for noise in noise_levels:
            noisy=obs+rng.normal(0,noise,obs.shape)
            start=time.perf_counter();est,pred=recon(noisy,method,noise);decode=time.perf_counter()-start
            if method=='front_four' and noise==.001:
                for kind in ('joint_time_shuffle','independent_field_time_shuffle'):
                    shuffled=noisy.copy()
                    for b in range(len(a)):
                        if kind=='joint_time_shuffle':
                            shuffled[b]=noisy[b,shuffle_rng.permutation(16)]
                        else:
                            for c in range(C):
                                shuffled[b,:,c]=noisy[b,shuffle_rng.permutation(16),c]
                    assert np.array_equal(np.sort(noisy,axis=1),np.sort(shuffled,axis=1))
                    est_s,pred_s=recon(shuffled,method,noise)
                    shuffle_rows.append(dict(ensemble=ensemble,method=kind,noise=noise,volume_nrmse=nrmse(est_s,a),far_face_future_nrmse=nrmse(pred_s[:,:,-1],traj[:,-1,:,-1])))
            extr=np.zeros_like(a);extr[:,:obs.shape[2]]=noisy[:,0,:,None,:,:]
            basefuture=advance(extr)
            rows.append(dict(ensemble=ensemble,method=method,noise=noise,volume_nrmse=nrmse(est,a),psi_nrmse=nrmse(est[:,0],a[:,0]),far_face_future_nrmse=nrmse(pred[:,:, -1],traj[:,-1,:,-1]),extrusion_nrmse=nrmse(extr,a),extrusion_far_future_nrmse=nrmse(basefuture[:,:,-1],traj[:,-1,:,-1]),decode_seconds=decode,reference_seconds=elapsed,mean_mirror_max_abs=symmetry))
    assert oracle_error<1e-10 and symmetry<1e-12,(oracle_error,symmetry)
    print(ensemble,'matrix parity',oracle_error,'mirror',symmetry,flush=True)
# Count singular modes surviving an absolute noise-scale threshold (not bit capacity).
rank_summary={m:{'min':min(ranks[m,y,x] for y in range(N) for x in range(N)),'max':max(ranks[m,y,x] for y in range(N) for x in range(N)),'total':sum(ranks[m,y,x] for y in range(N) for x in range(N)),'sv_gt_001':sum(sum(s>.001 for s in singular[m,y,x]) for y in range(N) for x in range(N)),'sv_gt_01':sum(sum(s>.01 for s in singular[m,y,x]) for y in range(N) for x in range(N))} for m in methods}
result=dict(scope='independent linear 3D reference; not original Core',shape=[C,D,N,N],unknowns=C*D*N*N,instant_2d_scalars=C*N*N,temporal_scalars=64*N*N,seed=20261126,test_volumes_per_ensemble=24,times_four=TIMES.tolist(),ranks=rank_summary,results=rows,shuffle_controls=shuffle_rows,environment=dict(python=platform.python_version(),numpy=np.__version__))
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(rank_summary,indent=2))
for r in rows: print(r['ensemble'],r['method'],r['noise'],*[round(r[k],4) for k in ['volume_nrmse','psi_nrmse','far_face_future_nrmse','extrusion_nrmse','extrusion_far_future_nrmse']])
