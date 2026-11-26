"""Frozen active observation experiment; independent 3D reference and native CPU excerpt."""
import hashlib,json,platform
from pathlib import Path
import numpy as np
from core_numpy_excerpt import CoreConfig,_step_numpy
P=Path(__file__).parent
assert hashlib.sha256((P/'protocol.md').read_bytes()).hexdigest()=='df2a6e9bd5decc9e1f94a0785d3b87807753f68fe8aa551c16e6c19f8d4aea92'
assert hashlib.sha256((P/'core_numpy_excerpt.py').read_bytes()).hexdigest()=='cea229a9dd5885471e389a238f022d8ea05f187828f3c7434b314456d8026c44'
N,D,C=8,9,4
R=np.array([.045,.065,.085,.025]);M=np.array([[0,.012,0,.009],[.012,0,.015,0],[0,.015,0,.011],[.009,0,.011,0]]);M-=np.diag(M.sum(axis=1))
rng=np.random.default_rng(2611261516);Y,X=np.indices((N,N));conduct=[];families=[]
for fam in ('ellipsoid','box','annulus','double_lobe'):
 for i in range(24):
  x,y=rng.uniform(2,5,2);rx,ry=rng.uniform(1.3,2.4,2);angle=rng.uniform(0,2*np.pi);u=(X-x)*np.cos(angle)+(Y-y)*np.sin(angle);v=-(X-x)*np.sin(angle)+(Y-y)*np.cos(angle);q=(u/rx)**2+(v/ry)**2
  if fam=='ellipsoid':mask=q<=1
  elif fam=='box':mask=(abs(u)<=rx)&(abs(v)<=ry)
  elif fam=='annulus':mask=(q>=.25)&(q<=1.5)
  else:mask=(((u-.8)/rx)**2+(v/ry)**2<=.7)|(((u+.8)/rx)**2+(v/ry)**2<=.7)
  assert mask.any();k=np.ones((D,N,N));k[1:3]=np.where(mask,rng.uniform(.12,.45),1.);conduct.extend((k,k[::-1].copy()));families.extend((fam,fam))
k=np.array(conduct);families=np.array(families);n=len(k);train=np.isin(families,['ellipsoid','box']);labels=np.tile([1.,-1.],n//2)
assert np.array_equal(np.sort(k[::2].reshape(-1,D*N*N),axis=1),np.sort(k[1::2].reshape(-1,D*N*N),axis=1))
assert np.array_equal(k[:,0],np.ones_like(k[:,0]))
def reference(k,xy,passive=False,history=False):
 a=np.zeros((len(k),C,D,N,N));x,y=xy
 if not passive:a[:,0,0]=np.exp(-((X-x)**2+(Y-y)**2)/2.)
 e0=a.sum(axis=(1,2,3,4));maxres=0.;snap=[];edges=[]
 for axis in (2,3,4):
  lo=[slice(None)]*5;hi=lo.copy();lo[axis]=slice(None,-1);hi[axis]=slice(1,None);lo,hi=tuple(lo),tuple(hi);klo=k[(lo[0],)+lo[2:]];khi=k[(hi[0],)+hi[2:]];w=2*klo*khi/(klo+khi);edges.append((lo,hi,w[:,None]))
 for t in range(65):
  if history and t<64:snap.append(a[:,0,0].copy())
  maxres=max(maxres,float(np.max(abs(a.sum(axis=(1,2,3,4))-e0))))
  assert a.min()>=-1e-14 and np.isfinite(a).all()
  if t==64:break
  d=np.zeros_like(a)
  for lo,hi,w in edges:
   flux=R.reshape(1,C,1,1,1)*w*(a[hi]-a[lo]);d[lo]+=flux;d[hi]-=flux
  a=a+d+np.einsum('ij,bjzyx->bizyx',M,a)
 return (np.stack(snap,1) if history else None),a[:,0,0].copy(),maxres
front,_,r1=reference(k,(2,2),history=True);passive,_,r2=reference(k,(2,2),passive=True,history=True);_,second,r3=reference(k,(5,5));_,hom,r4=reference(np.ones((1,D,N,N)),(5,5));target=second-hom
assert np.count_nonzero(passive)==0
seeds=np.repeat(rng.integers(0,2**31,n//2),2);noise=np.repeat(np.random.default_rng(2611261517).normal(0,1e-4,(n//2,64,N,N)),2,axis=0)
def native(data,use_mu=True):
 out=[];cfg=CoreConfig(use_mu=use_mu)
 for x,seed in zip(data,seeds):
  np.random.seed(int(seed));s={'psi':np.full((N,N),.01+0j),'phi':np.zeros((N,N)),'kappa':np.full((N,N),.8),'mu':np.zeros((N,N))}
  for delta in x:
   s['delta']=delta;s=_step_numpy(s,cfg)
   assert all(np.isfinite(v).all() for v in s.values())
  out.append(np.stack([s['psi'].real,s['psi'].imag,s['phi'],s['kappa'],s['mu']]))
 return np.stack(out)
features={}
for name,x,on in [('passive',passive,True),('active',front,True),('active_mu_off',front,False),('active_noise',front+noise,True),('active_demeaned',front-front.mean((2,3),keepdims=True),True)]:
 features[name]=native(x,on);print(name,'pair rms',np.sqrt(np.mean((features[name][::2]-features[name][1::2])**2)),flush=True)
features['raw']=front[:,[0,16,32,48,63]];features['ema']=np.zeros_like(features['raw']);r=np.array([0,.5,.8,.95,.99])[None,:,None,None]
for t in range(64):features['ema']=r*features['ema']+(1-r)*front[:,t,None]
rngp=np.random.default_rng(2611261518)
for name in ('joint_shuffle','independent_shuffle'):
 v=features['active'].reshape(n,5,-1).copy()
 for i in range(0,n,2):
  order=np.stack([rngp.permutation(N*N) for _ in range(1 if name=='joint_shuffle' else 5)])
  if len(order)==1:order=np.repeat(order,5,axis=0)
  for j in (i,i+1):v[j]=np.take_along_axis(v[j],order,axis=1)
 assert np.array_equal(np.sort(v,axis=-1),np.sort(features['active'].reshape(n,5,-1),axis=-1));features[name]=v.reshape(n,5,N,N)
assert np.array_equal(features['passive'][::2],features['passive'][1::2]);Yout=np.column_stack([labels,target.reshape(n,-1)])
rows=[];preds={}
for arm,f in features.items():
 x=f.reshape(n,-1);xc=x[train].mean(0);sd=x[train].std(0);sd=np.where(sd<1e-12,1,sd);z=(x-xc)/sd;yc=Yout[train].mean(0);zt=z[train];w=zt.T@np.linalg.solve(zt@zt.T+10*np.eye(train.sum()),Yout[train]-yc);p=z@w+yc;preds[arm]=p
 for fam in ('all','annulus','double_lobe'):
  ix=(~train)&((families==fam) if fam!='all' else True);pp=p[ix];tt=Yout[ix];pred=pp[:,0];pairdiff=pred[::2]-pred[1::2];yp=pp[:,1:];yt=tt[:,1:];den=np.linalg.norm(yt)
  row=dict(arm=arm,family=fam,n=int(ix.sum()),accuracy=float(np.mean(np.where(abs(pred)<1e-12,.5,np.sign(pred)==tt[:,0]))),paired_accuracy=float(np.mean(np.where(abs(pairdiff)<1e-12,.5,pairdiff>0))),nrmse=float(np.linalg.norm(yp-yt)/den),train_mean_nrmse=float(np.linalg.norm(yc[1:]-yt)/den));rows.append(row)
  if fam=='all':print(row,flush=True)
metrics={r['arm']:r for r in rows if r['family']=='all'};act=metrics['active'];gates={'active_observation':act['accuracy']>.5 and act['paired_accuracy']>.5 and act['accuracy']>metrics['passive']['accuracy'],'withheld_forecast':act['nrmse']<min(1.,act['train_mean_nrmse']),'competitive_compression':all(act['nrmse']<metrics[b]['nrmse'] and act['accuracy']>metrics[b]['accuracy'] for b in ('raw','ema'))}
res=dict(scope='Independent heterogeneous 3D reference; pinned native CPU component, experimenter supplied probe',rows=rows,gates=gates,reference=dict(max_mass_residual=max(r1,r2,r3,r4),passive_pairs_exact=96,active_pair_rms=float(np.sqrt(np.mean((front[::2]-front[1::2])**2))),minimum_active_pair_max_difference=float(np.min(np.max(abs(front[::2]-front[1::2]),axis=(1,2,3)))),target_pair_rms=float(np.sqrt(np.mean((target[::2]-target[1::2])**2))),target_rms=float(np.sqrt(np.mean(target**2))),native_demean_max_difference=float(np.max(abs(features['active']-features['active_demeaned'])))),environment=dict(python=platform.python_version(),numpy=np.__version__))
(P/'results.json').write_text(json.dumps(res,indent=2)+'\n');np.savez_compressed(P/'measurements.npz',conductivity=k,families=families,train=train,labels=labels,front=front,passive=passive,target=target,second=second,homogeneous=hom,seeds=seeds,**{'feature_'+k:v for k,v in features.items()},**{'prediction_'+k:v for k,v in preds.items()});print(res['reference'],gates)
