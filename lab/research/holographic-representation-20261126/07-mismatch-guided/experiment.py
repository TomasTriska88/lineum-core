"""Frozen active observation experiment; independent 3D reference and native CPU excerpt."""
import hashlib,json,platform
from pathlib import Path
import numpy as np
from core_numpy_excerpt import CoreConfig,_step_numpy
P=Path(__file__).parent
assert hashlib.sha256((P/'core_numpy_excerpt.py').read_bytes()).hexdigest()=='cea229a9dd5885471e389a238f022d8ea05f187828f3c7434b314456d8026c44'
N,D,C=8,9,4
R=np.array([.045,.065,.085,.025]);M=np.array([[0,.012,0,.009],[.012,0,.015,0],[0,.015,0,.011],[.009,0,.011,0]]);M-=np.diag(M.sum(axis=1))
rng=np.random.default_rng(2611261627);Y,X=np.indices((N,N));conduct=[];families=[]
for fam in ('ellipsoid','box','annulus','double_lobe'):
 for i in range(20):
  x,y=rng.uniform(2,5,2);rx,ry=rng.uniform(1.3,2.4,2);angle=rng.uniform(0,2*np.pi);u=(X-x)*np.cos(angle)+(Y-y)*np.sin(angle);v=-(X-x)*np.sin(angle)+(Y-y)*np.cos(angle);q=(u/rx)**2+(v/ry)**2
  if fam=='ellipsoid':mask=q<=1
  elif fam=='box':mask=(abs(u)<=rx)&(abs(v)<=ry)
  elif fam=='annulus':mask=(q>=.25)&(q<=1.5)
  else:mask=(((u-.8)/rx)**2+(v/ry)**2<=.7)|(((u+.8)/rx)**2+(v/ry)**2<=.7)
  assert mask.any();k=np.ones((D,N,N));k[1:3]=np.where(mask,rng.uniform(.12,.45),1.);conduct.extend((k,k[::-1].copy()));families.extend((fam,fam))
k=np.array(conduct);families=np.array(families);n=len(k);train=np.isin(families,['ellipsoid','box']);labels=np.tile([1.,-1.],n//2)
assert np.array_equal(np.sort(k[::2].reshape(-1,D*N*N),axis=1),np.sort(k[1::2].reshape(-1,D*N*N),axis=1))
assert np.array_equal(k[:,0],np.ones_like(k[:,0]))
positions=np.array([[2,2],[5,2],[2,5],[5,5]])
def pulse(x,y):
 v=np.exp(-((X-x)**2+(Y-y)**2)/2.);return v/v.sum()
patterns=np.stack([pulse(x,y) for x,y in positions])
def reference(k,xy,passive=False,history=False,actions=None):
 a=np.zeros((len(k),C,D,N,N));x,y=xy
 if not passive:a[:,0,0]=pulse(x,y)
 e0=a.sum(axis=(1,2,3,4));maxres=0.;snap=[];edges=[]
 for axis in (2,3,4):
  lo=[slice(None)]*5;hi=lo.copy();lo[axis]=slice(None,-1);hi[axis]=slice(1,None);lo,hi=tuple(lo),tuple(hi);klo=k[(lo[0],)+lo[2:]];khi=k[(hi[0],)+hi[2:]];w=2*klo*khi/(klo+khi);edges.append((lo,hi,w[:,None]))
 for t in range(65):
  if t==32 and actions is not None:a[:,0,0]+=patterns[actions]
  if history and t<64:snap.append(a[:,0,0].copy())
  maxres=max(maxres,float(np.max(abs(a.sum(axis=(1,2,3,4))-e0-(actions is not None and t>=32)))))
  assert a.min()>=-1e-14 and np.isfinite(a).all()
  if t==64:break
  d=np.zeros_like(a)
  for lo,hi,w in edges:
   flux=R.reshape(1,C,1,1,1)*w*(a[hi]-a[lo]);d[lo]+=flux;d[hi]-=flux
  a=a+d+np.einsum('ij,bjzyx->bizyx',M,a)
 return (np.stack(snap,1) if history else None),a[:,0,0].copy(),maxres
front,_,r1=reference(k,(3.5,3.5),history=True);_,second,r3=reference(k,(3,1));_,hom,r4=reference(np.ones((1,D,N,N)),(3,1));target=second-hom
seeds=np.repeat(rng.integers(0,2**31,n//2),2)
def native(data,use_mu=True):
 out=[];cfg=CoreConfig(use_mu=use_mu)
 for x,seed in zip(data,seeds):
  np.random.seed(int(seed));s={'psi':np.full((N,N),.01+0j),'phi':np.zeros((N,N)),'kappa':np.full((N,N),.8),'mu':np.zeros((N,N))}
  for delta in x:
   s['delta']=delta;s=_step_numpy(s,cfg)
   assert all(np.isfinite(v).all() for v in s.values())
  out.append(np.stack([s['psi'].real,s['psi'].imag,s['phi'],s['kappa'],s['mu']]))
 return np.stack(out)
pre=native(front[:,:32]);scores=np.stack([pre[:,4,y-1:y+2,x-1:x+2].mean((1,2)) for x,y in positions],axis=1)
mu_action=scores.argmax(1);fixed=np.zeros(n,dtype=int)
phi=pre[:,2];mu=pre[:,4];mismatch=np.abs(phi/np.maximum(phi.mean((1,2),keepdims=True),1e-30)-mu/np.maximum(mu.mean((1,2),keepdims=True),1e-30))
mismatch_scores=np.stack([mismatch[:,y-1:y+2,x-1:x+2].mean((1,2)) for x,y in positions],axis=1);adaptive=mismatch_scores.argmax(1);yoked=adaptive.copy()
for fam in np.unique(families):
 ids=np.flatnonzero(families==fam);yoked[ids]=np.roll(adaptive[ids],2);assert np.array_equal(np.bincount(yoked[ids],minlength=4),np.bincount(adaptive[ids],minlength=4))
features={};hist={};actions={'mismatch':adaptive,'fixed':fixed,'mu':mu_action,'yoked':yoked};residuals=[r1,r3,r4]
for arm,ac in actions.items():
 data,_,r=reference(k,(3.5,3.5),history=True,actions=ac);assert np.array_equal(data[:,:32],front[:,:32]);hist[arm]=data;residuals.append(r);features[arm]=native(data);features['raw_'+arm]=data[:,[0,16,32,48,63]];print('completed',arm,flush=True)
Yout=np.column_stack([labels,target.reshape(n,-1)])
rows=[];preds={}
for arm,f in features.items():
 x=f.reshape(n,-1);xc=x[train].mean(0);sd=x[train].std(0);sd=np.where(sd<1e-12,1,sd);z=(x-xc)/sd;yc=Yout[train].mean(0);zt=z[train];w=zt.T@np.linalg.solve(zt@zt.T+10*np.eye(train.sum()),Yout[train]-yc);p=z@w+yc;preds[arm]=p
 for fam in ('all','annulus','double_lobe'):
  ix=(~train)&((families==fam) if fam!='all' else True);pp=p[ix];tt=Yout[ix];pred=pp[:,0];pairdiff=pred[::2]-pred[1::2];yp=pp[:,1:];yt=tt[:,1:];den=np.linalg.norm(yt)
  row=dict(arm=arm,family=fam,n=int(ix.sum()),accuracy=float(np.mean(np.where(abs(pred)<1e-12,.5,np.sign(pred)==tt[:,0]))),paired_accuracy=float(np.mean(np.where(abs(pairdiff)<1e-12,.5,pairdiff>0))),nrmse=float(np.linalg.norm(yp-yt)/den),train_mean_nrmse=float(np.linalg.norm(yc[1:]-yt)/den));rows.append(row)
  if fam=='all':print(row,flush=True)
metrics={r['arm']:r for r in rows if r['family']=='all'};act=metrics['mismatch'];gates={'mismatch':bool(act['accuracy']>max(.5,*(metrics[a]['accuracy'] for a in ('fixed','mu','yoked'))) and act['nrmse']<min(1.,act['train_mean_nrmse'],*(metrics[a]['nrmse'] for a in ('fixed','mu','yoked'))))}
res=dict(scope='Independent reference, unchanged native CPU component, external state-driven action selector',rows=rows,gates=gates,reference=dict(max_mass_residual=max(residuals),pulse_mass=[float(pulse(3.5,3.5).sum())]+[float(v.sum()) for v in patterns],action_counts={a:np.bincount(v,minlength=4).tolist() for a,v in actions.items()},changed_pair_actions=int(np.count_nonzero(adaptive[::2]!=adaptive[1::2])),mu_changed_pair_actions=int(np.count_nonzero(mu_action[::2]!=mu_action[1::2])),yoked_action_diff=int(np.count_nonzero(adaptive!=yoked)),test_action_counts={a:np.bincount(v[~train],minlength=4).tolist() for a,v in actions.items()}),environment=dict(python=platform.python_version(),numpy=np.__version__))
(P/'results.json').write_text(json.dumps(res,indent=2)+'\n');np.savez_compressed(P/'measurements.npz',conductivity=k,families=families,train=train,labels=labels,positions=positions,patterns=patterns,center=pulse(3.5,3.5),target=target,second=second,homogeneous=hom,seeds=seeds,pre=pre,scores=scores,mismatch_scores=mismatch_scores,**{'action_'+k:v for k,v in actions.items()},**{'history_'+k:v for k,v in hist.items()},**{'feature_'+k:v for k,v in features.items()},**{'prediction_'+k:v for k,v in preds.items()});print(res['reference'],gates)
