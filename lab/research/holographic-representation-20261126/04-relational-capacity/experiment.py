"""Read-only native CPU component diagnostic against independent 3D reference."""
import hashlib,json,itertools,platform
from pathlib import Path
import numpy as np
from core_numpy_excerpt import CoreConfig,_step_numpy
P=Path(__file__).parent
assert hashlib.sha256((P/'protocol.md').read_bytes()).hexdigest()=='a4742e57c3601185462c54e180c874efd1ee0cc97651265c549d18ddc3301e02'
assert hashlib.sha256((P/'core_numpy_excerpt.py').read_bytes()).hexdigest()=='cea229a9dd5885471e389a238f022d8ea05f187828f3c7434b314456d8026c44'
N,D,C=8,9,4
R=np.array([.045,.065,.085,.025]); M=np.array([[0,.012,0,.009],[.012,0,.015,0],[0,.015,0,.011],[.009,0,.011,0]]); M-=np.diag(M.sum(axis=1))
def lap(a,axis):
 p=np.pad(a,[(1,1) if i==axis else (0,0) for i in range(a.ndim)],mode='edge');return np.take(p,np.arange(a.shape[axis]),axis=axis)+np.take(p,np.arange(2,a.shape[axis]+2),axis=axis)-2*a
def step(a):return a+R.reshape(1,C,1,1,1)*sum(lap(a,i) for i in (2,3,4))+np.einsum('ij,bjzyx->bizyx',M,a)
def observe(a):
 front=[]
 for t in range(65):
  if t<32:front.append(a[:,0,0].copy())
  if t<64:a=step(a)
 return np.stack(front,axis=1),a[:,0,0]-a[:,0,-1]
def native(x,seed,history=False):
 np.random.seed(int(seed));s={'psi':np.full((N,N),.01+0j),'phi':np.zeros((N,N)),'kappa':np.full((N,N),.8),'mu':np.zeros((N,N))}; cfg=CoreConfig(use_mu=True);h=[]
 for d in x:
  s['delta']=d;s=_step_numpy(s,cfg)
  v=np.stack([s['psi'].real,s['psi'].imag,s['phi'],s['kappa'],s['mu']]);assert np.isfinite(v).all();h.append(v)
 return np.stack(h) if history else h[-1]
rng=np.random.default_rng(1142706); blocks=[];train=[];families=[]
for fam in ('iid','smooth'):
 a=rng.normal(size=(48,C,D,N,N))
 if fam=='smooth':
  for _ in range(7):a=step(a)
  a/=a.std(axis=(2,3,4),keepdims=True)
 blocks.append(np.stack((a,a[:,:,::-1]),axis=1).reshape(-1,C,D,N,N));train.extend(np.repeat(np.arange(48)<24,2));families.extend([fam]*96)
a=np.concatenate(blocks);train=np.array(train);families=np.array(families);n=len(a);front,target=observe(a);seeds=np.repeat(rng.integers(0,2**31,n//2),2)
features={'native':np.stack([native(x,s) for x,s in zip(front,seeds)]),'raw':front[:,[0,8,16,24,31]]}
ema=np.zeros_like(features['raw']);r=np.array([0,.5,.8,.95,.99])[None,:,None,None]
for t in range(32):ema=r*ema+(1-r)*front[:,t,None]
features['ema']=ema
rngp=np.random.default_rng(1142707)
for arm in ('joint','independent'):
 v=features['native'].reshape(n,5,-1).copy()
 for i in range(n):
  if arm=='joint':v[i]=v[i][:,rngp.permutation(N*N)]
  else:
   for j in range(5):v[i,j]=v[i,j,rngp.permutation(N*N)]
 features[arm]=v.reshape(n,5,N,N)
 assert np.array_equal(np.sort(v,axis=-1),np.sort(features['native'].reshape(n,5,-1),axis=-1))
def ridge(x,y,mask):
 x0=x[mask];y0=y[mask];mean=x0.mean(0);std=x0.std(0);std=np.where(std<1e-12,1,std);z=(x0-mean)/std;yc=y0.mean(0);w=np.linalg.solve(z.T@z+.1*np.eye(z.shape[1]),z.T@(y0-yc));return ((x-mean)/std)@w+yc
rows=[];preds={}
def score(arm,kind,p,t):
 for fam in ('all','iid','smooth'):
  mask=(~train)&((families==fam) if fam!='all' else True);pp=p[mask];tt=t[mask];pm=pp.reshape(len(pp),-1).mean(1);tm=tt.reshape(len(tt),-1).mean(1)
  rows.append(dict(arm=arm,kind=kind,family=fam,nrmse=float(np.linalg.norm(pp-tt)/np.linalg.norm(tt)),accuracy=float(np.mean(np.where(abs(pm)<1e-12,.5,np.sign(pm)==np.sign(tm))))))
for arm,f in features.items():
 g=f.reshape(n,5,-1);mean=g.mean(2);sd=g.std(2);marg=np.concatenate([mean,sd],axis=1);idx=[0,1,2,4] if arm in ('native','joint','independent') else list(range(5));z=(g-mean[:,:,None])/np.where(sd<1e-12,1,sd)[:,:,None];z=z.reshape(n,5,N,N)
 rel=np.stack([np.mean(z[:,i]*z[:,j],axis=(1,2)) for i,j in itertools.combinations(idx,2)]+[.5*(np.mean(z[:,i,:,:-1]*z[:,i,:,1:],axis=(1,2))+np.mean(z[:,i,:-1,:]*z[:,i,1:,:],axis=(1,2))) for i in idx],axis=1)
 for kind,x in [('marginal',marg),('relation',rel),('combined',np.concatenate([marg,rel],1))]:
  p=ridge(x,target.mean((1,2)),train);preds[arm+'_'+kind]=p;score(arm,kind,p,target.mean((1,2)))
 x=f.transpose(0,2,3,1).reshape(n*N*N,5);tr=np.repeat(train,N*N);y=target.ravel();p=ridge(x,y,tr).reshape(n,N,N);preds[arm+'_map_linear']=p;score(arm,'map_linear',p,target)
 mu=x[tr].mean(0);std=x[tr].std(0);xx=(x-mu)/np.where(std<1e-12,1,std);xq=np.column_stack([xx]+[xx[:,i]*xx[:,j] for i,j in itertools.combinations(idx,2)]);p=ridge(xq,y,tr).reshape(n,N,N);preds[arm+'_map_relational']=p;score(arm,'map_relational',p,target)
# A true 3D contrast mode whose boundary contribution is laterally uniform.
rngc=np.random.default_rng(1142708);base=rngc.normal(size=(32,C,D,N,N));mode=np.zeros((1,C,D,1,1));mode[0,0,:,0,0]=np.cos(np.pi*(np.arange(D)+.5)/D);fa,ta=observe(base+mode);fb,tb=observe(base-mode);cs=rngc.integers(0,2**31,32);hist_a=np.stack([native(x,s,True) for x,s in zip(fa,cs)]);hist_b=np.stack([native(x,s,True) for x,s in zip(fb,cs)]);grad_diff=max(float(np.max(abs(np.diff(fa,axis=ax)-np.diff(fb,axis=ax)))) for ax in (2,3));delta=ta-tb
exact_a=native(np.zeros((32,N,N)),1234,True);exact_b=native(np.full((32,N,N),.25),1234,True)
collision=dict(pairs=32,steps=32,max_gradient_difference=grad_diff,max_state_difference=float(np.max(abs(hist_a-hist_b))),exact_equal_pairs=int(np.sum(np.all(hist_a==hist_b,axis=(1,2,3,4)))),target_rms_difference=float(np.sqrt(np.mean(delta**2))),minimum_pair_target_rms=float(np.min(np.sqrt(np.mean(delta**2,axis=(1,2))))),exact_constant_input_equal=bool(np.array_equal(exact_a,exact_b)))
res=dict(rows=rows,collision=collision,train=int(train.sum()),test=int((~train).sum()),environment=dict(python=platform.python_version(),numpy=np.__version__))
(P/'results.json').write_text(json.dumps(res,indent=2)+'\n');np.savez_compressed(P/'measurements.npz',train=train,families=families,target=target,**{'feature_'+k:v for k,v in features.items()},**{'prediction_'+k:v for k,v in preds.items()},collision_target_a=ta,collision_target_b=tb,collision_front_a=fa,collision_front_b=fb,collision_hist_a=hist_a,collision_hist_b=hist_b,constant_a=exact_a,constant_b=exact_b)
for row in rows:
 if row['family']=='all':print(row)
print(collision)
