import hashlib,json,itertools,sys,platform
from pathlib import Path
import numpy as np
from core_numpy_excerpt import CoreConfig,_step_numpy
P=Path(__file__).parent
source=Path(sys.argv[1]); assert hashlib.sha256(source.read_bytes()).hexdigest()=='86ec82a758a4ff08a73399eb655ca5877d2fe0930a34d73f582b99d64d948928'
assert hashlib.sha256((P/'core_numpy_excerpt.py').read_bytes()).hexdigest()=='cea229a9dd5885471e389a238f022d8ea05f187828f3c7434b314456d8026c44'
r=json.loads(source.read_text()); N=24; cues=((9,12),(15,12)); times=(1,8,24,64); modes=('learned','shuffled','uniform','zero'); K=np.full((N,N),.8)
seeds=sorted(set(x['seed'] for x in r['training'])); maps={(x['seed'],x['history']):np.asarray(x['mu']) for x in r['training']}; old={(x['seed'],x['history'],x['mode'],x['cue']):np.asarray(x['rows']) for x in r['trials']}
def state(mu,c=None):
 s=dict(psi=np.zeros((N,N),complex),phi=np.zeros((N,N)),kappa=K.copy(),mu=mu.copy())
 if c is not None:s['psi'][c]=.32
 return s
def stats(z):
 return [float(z.mean()),float(np.sqrt(np.mean(z*z))),*[float(np.sqrt(np.mean((z-np.roll(z,1,axis=i))**2))) for i in (0,1)]]
def features(s):return sum((stats(z) for z in (s['psi'].real,s['psi'].imag,s['phi'],s['mu'])),[])
def minus(a,b):return {k:a[k]-b[k] for k in ('psi','phi','mu')}
rows=[]; max_error=0.; ticks=0
for seed in seeds:
 perm=np.random.default_rng(seed+2000).permutation(N*N)
 for h in (0,1):
  mu=maps[seed,h]
  for mode in modes:
   m={'learned':mu,'shuffled':mu.ravel()[perm].reshape(N,N),'uniform':np.full_like(mu,mu.mean()),'zero':np.zeros_like(mu)}[mode]
   for c,cue in enumerate(cues):
    b=state(m);u=state(m,cue); f={k:[] for k in ('quiet','cue','excess')};np.random.seed(seed+3000+c); cfg=CoreConfig(use_mu=True)
    for t in range(1,65):
     rng=np.random.get_state(); b=_step_numpy(b,cfg); after=np.random.get_state();np.random.set_state(rng);u=_step_numpy(u,cfg); end=np.random.get_state(); assert np.array_equal(after[1],end[1]) and after[2:]==end[2:]
     z=float(np.sum(abs(u['psi']-b['psi'])**2)); max_error=max(max_error,abs(z-old[seed,h,mode,c][t-1,2])); ticks+=1
     if t in times:
      for key,s in [('quiet',b),('cue',u),('excess',minus(u,b))]: f[key].extend(features(s))
    rows.append(dict(seed=seed,history=h,mode=mode,cue_index=c,initial=stats(m),**f))
assert max_error<1e-10
# One paired history difference per seed, concatenate two cue measurements (no train/test seed overlap).
def evaluate(d,signs):
 d=d*np.asarray(signs)[:,None]; out=[]
 for i in range(len(d)):
  tr=np.delete(d,i,axis=0);scale=np.sqrt(np.mean(tr*tr,axis=0));safe=scale>1e-14
  v=np.divide(tr,scale,out=np.zeros_like(tr),where=safe); q=np.divide(d[i],scale,out=np.zeros_like(d[i]),where=safe)
  out.append(float(np.dot(v.mean(0),q)/max(safe.sum(),1)))
 return out
def acc(v):return (sum(x>1e-12 for x in v)+.5*sum(abs(x)<=1e-12 for x in v))/len(v)
idx={(x['seed'],x['history'],x['mode'],x['cue_index']):x for x in rows}; results={}
for mode in modes:
 results[mode]={}
 for key in ('initial','quiet','cue','excess'):
  d=np.asarray([sum([list(np.asarray(idx[s,0,mode,c][key])-idx[s,1,mode,c][key]) for c in ((0,) if key=='initial' else (0,1))],[]) for s in seeds]);scores=evaluate(d,[1]*len(seeds));a=acc(scores);null=[acc(evaluate(d,sgn)) for sgn in itertools.product((-1,1),repeat=len(seeds))]
  results[mode][key]={'accuracy':a,'p_exact_unadjusted':sum(x>=a for x in null)/len(null),'scores':scores,'median_feature_difference_rms':float(np.median(np.sqrt(np.mean(d*d,axis=1))))}
assert all(results['zero'][k]['accuracy']==.5 for k in results['zero'])
out=dict(environment={'python':platform.python_version(),'numpy':np.__version__},seeds=seeds,times=times,columns=['mean','rms','roughness_y','roughness_x'],fields=['psi_real','psi_imag','phi','mu'],replay_ticks=ticks,replay_max_error=max_error,rows=rows,results=results)
(P/'results.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n');print(json.dumps({'replay_ticks':ticks,'replay_max_error':max_error,'results':results},indent=2))
