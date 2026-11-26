import hashlib,json,platform
from pathlib import Path
import numpy as np
from core_numpy_excerpt import CoreConfig,_step_numpy
P=Path(__file__).parent
assert hashlib.sha256((P/'core_numpy_excerpt.py').read_bytes()).hexdigest()=='cea229a9dd5885471e389a238f022d8ea05f187828f3c7434b314456d8026c44'
N=24; A,D=(9,12),(15,12); B,C=(12,8),(12,16)
K=np.full((N,N),.8); modes=('learned','shuffled','uniform','frozen','zero')
regions=[(slice(y-1,y+2),slice(x-1,x+2)) for y,x in (B,C)]
def state(mu,point=None):
 s={'psi':np.zeros((N,N),complex),'phi':np.zeros((N,N)),'kappa':K.copy(),'mu':mu.copy()}
 if point is not None:s['psi'][point]=.32
 return s
def step(s,cfg):
 s=_step_numpy(s,cfg)
 assert all(np.isfinite(v).all() for v in s.values()) and np.array_equal(s['kappa'],K)
 assert abs(s['psi']).max()<.99e6 and s['phi'].max()<1e6 and s['mu'].max()<10 and s['mu'].min()>=0
 return s
def trial(mu,cue,cfg,seed):
 b=state(mu); u=state(mu,cue); np.random.seed(seed); rows=[]
 for t in range(64):
  rng=np.random.get_state(); b=step(b,cfg); after=np.random.get_state(); np.random.set_state(rng); u=step(u,cfg); end=np.random.get_state(); assert np.array_equal(after[1],end[1]) and after[2:]==end[2:]
  z=abs(u['psi']-b['psi'])**2
  rows.append([float(z[regions[0]].sum()),float(z[regions[1]].sum()),float(z.sum()),float((abs(b['psi'])**2).sum())])
 a=np.asarray(rows); s=a.sum(0)
 return {'rows':rows,'contrast':float((s[0]-s[1])/max(s[0]+s[1],1e-30)),'final_to_peak':float(np.mean(np.sqrt(a[-16:,2]))/max(np.sqrt(a[:,2].max()),1e-30)),'quiet_final_rms':float(np.mean(np.sqrt(a[-16:,3]/N**2)))}
result={'environment':{'python':platform.python_version(),'numpy':np.__version__},'columns':['target_B_excess_squared','target_C_excess_squared','whole_excess_squared','quiet_squared'],'training':[],'trials':[],'scores':[]}
for i in range(8):
 seed=26112640+i; mus=[]
 for h in range(2):
  mu=np.zeros((N,N)); cfg=CoreConfig(use_mu=True)
  for cycle in range(4):
   for c in (0,1) if cycle%2==0 else (1,0):
    s=state(mu,(A,D)[c]); target=(B,C)[c^h]; np.random.seed(seed+1000+cycle*2+c)
    for t in range(24):
     if t==8:s['psi'][target]+=.32
     s=step(s,cfg)
    mu=s['mu'].copy()
  mus.append(mu);result['training'].append({'seed':seed,'history':h,'mu':mu.tolist(),'mass':float(mu.sum())})
 perm=np.random.default_rng(seed+2000).permutation(N*N)
 for mode in modes:
  cc=[]; ratios=[]; quiet=[]
  for h,mu in enumerate(mus):
   m={'learned':mu,'shuffled':mu.ravel()[perm].reshape(N,N),'uniform':np.full_like(mu,mu.mean()),'frozen':mu,'zero':np.zeros_like(mu)}[mode]
   if mode in ('shuffled','uniform'):assert abs(m.sum()-mu.sum())<1e-10
   cfg=CoreConfig(use_mu=mode!='frozen')
   for c,cue in enumerate((A,D)):
    x=trial(m,cue,cfg,seed+3000+c); cc.append((-1)**(h+c)*x['contrast']);ratios.append(x['final_to_peak']);quiet.append(x['quiet_final_rms']);result['trials'].append(dict(seed=seed,history=h,cue=c,mode=mode,**x))
  result['scores'].append(dict(seed=seed,mode=mode,association=float(np.mean(cc)),final_to_peak=float(np.mean(ratios)),quiet_final_rms=float(np.mean(quiet))))
scores={m:np.asarray([x['association'] for x in result['scores'] if x['mode']==m]) for m in modes}
result['summary']={m:{'median_association':float(np.median(scores[m])),'positive_seeds':int((scores[m]>0).sum()),'median_final_to_peak':float(np.median([x['final_to_peak'] for x in result['scores'] if x['mode']==m]))} for m in modes}
result['learned_minus_shuffled']=float(np.median(scores['learned']-scores['shuffled']));result['learned_minus_uniform']=float(np.median(scores['learned']-scores['uniform']));result['gate_pass']=bool((scores['learned']>0).sum()>=7 and np.median(scores['learned'])>=.05 and result['learned_minus_shuffled']>=.05 and result['learned_minus_uniform']>=.05)
assert np.max(abs(scores['zero']))<1e-15
(P/'results.json').write_text(json.dumps(result,separators=(',',':'),sort_keys=True)+'\n');print(json.dumps({k:result[k] for k in ('summary','learned_minus_shuffled','learned_minus_uniform','gate_pass')},indent=2))
