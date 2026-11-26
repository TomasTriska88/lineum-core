"""Isolated boundary-driven native CPU component diagnostic; see frozen protocol."""
import hashlib,json,platform
from pathlib import Path
import numpy as np
from core_numpy_excerpt import CoreConfig,_step_numpy
P=Path(__file__).parent
assert hashlib.sha256((P/'protocol.md').read_bytes()).hexdigest()=='72871ba1008bbcc60881e698b53c7900ae81a95ef7d7c430c40883432782774f'
source=(P/'core_numpy_excerpt.py').read_text(); h=2166136261
for c in '\n'.join(l.rstrip() for l in source[source.index('@dataclass(frozen=True)'):].splitlines()).rstrip():h=((h^ord(c))*16777619)&0xffffffff
assert h==0x56103725
N,D,C=8,9,4
R=np.array([.045,.065,.085,.025]); M=np.array([[0,.012,0,.009],[.012,0,.015,0],[0,.015,0,.011],[.009,0,.011,0]]); M-=np.diag(M.sum(axis=1))
def lap(a,axis):
 p=np.pad(a,[(1,1) if i==axis else (0,0) for i in range(a.ndim)],mode='edge');return np.take(p,np.arange(a.shape[axis]),axis=axis)+np.take(p,np.arange(2,a.shape[axis]+2),axis=axis)-2*a
def step(a):return a+R.reshape(1,C,1,1,1)*sum(lap(a,i) for i in (2,3,4))+np.einsum('ij,bjzyx->bizyx',M,a)
rng=np.random.default_rng(932061); blocks=[]; train=[]; families=[]
for family in ('iid','smooth'):
 a=rng.normal(size=(36,C,D,N,N))
 if family=='smooth':
  for _ in range(7):a=step(a)
  a/=a.std(axis=(2,3,4),keepdims=True)
 blocks.append(np.stack((a,a[:,:,::-1]),axis=1).reshape(-1,C,D,N,N));train.extend(np.repeat(np.arange(36)<24,2));families.extend([family]*72)
a=np.concatenate(blocks); train=np.array(train); families=np.array(families); count=len(a)
front=[]; mean=[]
for t in range(65):
 if t<32:front.append(a[:,0,0].copy());mean.append(a[:,0].mean(axis=1))
 if t<64:a=step(a)
front=np.stack(front,axis=1);mean=np.stack(mean,axis=1);targets=np.stack((a[:,0,0]-a[:,0,-1],a[:,0,-1]),axis=1)
assert np.max(abs(mean[::2]-mean[1::2]))<1e-12
seeds=np.repeat(rng.integers(0,2**31,size=count//2),2);orders=np.repeat(np.array([rng.permutation(32) for _ in range(count//2)]),2,axis=0)
features={}; receipts={}
for arm in ('front','depth_mean','front_time_shuffle','front_mu_off','zero_delta'):
 out=[]
 cfg=CoreConfig(use_mu=arm!='front_mu_off')
 for i in range(count):
  np.random.seed(int(seeds[i]));s={'psi':np.full((N,N),.01+0j),'phi':np.zeros((N,N)),'kappa':np.full((N,N),.8),'mu':np.zeros((N,N))}
  for t in range(32):
   s['delta']=(mean[i,t] if arm=='depth_mean' else np.zeros((N,N)) if arm=='zero_delta' else front[i,orders[i,t]] if arm=='front_time_shuffle' else front[i,t]);s=_step_numpy(s,cfg)
   assert all(np.isfinite(x).all() for x in s.values())
  out.append(np.stack([s['psi'].real,s['psi'].imag,s['phi'],s['kappa'],s['mu']]))
 features[arm]=np.stack(out);receipts[arm]={'pair_max_abs':float(np.max(abs(features[arm][::2]-features[arm][1::2]))),'pair_rms':float(np.sqrt(np.mean((features[arm][::2]-features[arm][1::2])**2))),'test_mu_mean':float(features[arm][~train,4].mean())}
 print(arm,receipts[arm],flush=True)
features['raw_5']=front[:,[0,8,16,24,31]]
ema=np.zeros((count,5,N,N));rates=np.array([0,.5,.8,.95,.99])[None,:,None,None]
for t in range(32):ema=rates*ema+(1-rates)*front[:,t,None]
features['ema_5']=ema
for arm in ('joint_spatial_shuffle','mu_spatial_shuffle'):
 v=features['front'].copy().reshape(count,5,-1)
 for i in range(count):
  order=rng.permutation(N*N)
  if arm=='joint_spatial_shuffle':v[i]=v[i][:,order]
  else:v[i,4]=v[i,4,order]
 features[arm]=v.reshape(count,5,N,N)
 assert np.array_equal(np.sort(features[arm].reshape(count,5,-1),axis=-1),np.sort(features['front'].reshape(count,5,-1),axis=-1))
rows=[];predictions={}
for arm,f in features.items():
 X=f.transpose(0,2,3,1).reshape(count,-1,5);Y=targets.transpose(0,2,3,1).reshape(count,-1,2)
 x=X[train].reshape(-1,5);y=Y[train].reshape(-1,2);center=x.mean(0);scale=x.std(0);scale[scale<1e-12]=1
 z=(x-center)/scale;yc=y.mean(0);w=np.linalg.solve(z.T@z+.1*np.eye(5),z.T@(y-yc));pred=((X-center)/scale)@w+yc
 predictions[arm]=pred
 for fam in ('all','iid','smooth'):
  ix=(~train)&((families==fam) if fam!='all' else True)
  for j,name in enumerate(('contrast','far_face')):
   pp=pred[ix,:,j];tt=Y[ix,:,j];p=pp.mean(1);t=tt.mean(1);assert np.min(abs(t))>1e-12
   rows.append({'arm':arm,'family':fam,'target':name,'nrmse':float(np.linalg.norm(pp-tt)/np.linalg.norm(tt)),'sign_accuracy':float(np.mean(np.where(abs(p)<1e-12,.5,np.sign(p)==np.sign(t))))})
allrows={r['arm']:r for r in rows if r['family']=='all' and r['target']=='contrast'}
for k,v in allrows.items():print(k,v,flush=True)
f=allrows['front'];gates={'above_chance':f['sign_accuracy']>.5,'beats_mean_zero_shuffle':all(f['nrmse']<allrows[k]['nrmse'] for k in ('depth_mean','zero_delta','joint_spatial_shuffle')),'beats_raw_ema':all(f['nrmse']<allrows[k]['nrmse'] for k in ('raw_5','ema_5'))}
result=dict(scope='reference + exact normalized CPU excerpt; not full native Grid',seed=932061,train_volumes=int(train.sum()),test_volumes=int((~train).sum()),state_scalars=320,reference_scalars=2304,receipts=receipts,rows=rows,gates=gates,environment={'python':platform.python_version(),'numpy':np.__version__})
(P/'results.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed(P/'measurements.npz',train=train,families=families,targets=targets,front=front,mean=mean,**{'feature_'+k:v for k,v in features.items()},**{'prediction_'+k:v for k,v in predictions.items()})
