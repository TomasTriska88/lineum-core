import json,hashlib,platform
from pathlib import Path
import numpy as np
P=Path(__file__).parent
p=P/'experiment.py'
# Reuse definitions, not the already executed main experiment loops.
exec(compile(p.read_text().split('for seed in SEEDS:',1)[0],str(p),'exec'))
base_step=_step_numpy
def no_birth(s,cfg):
 orig=np.random.rand;calls=[]
 def gated(*shape):
  a=orig(*shape);calls.append(shape);return np.ones_like(a)
 try:
  np.random.rand=gated;z=base_step(s,cfg)
 finally:np.random.rand=orig
 assert calls==[(N,N)]
 return z
_step_numpy=no_birth
result={'environment':[platform.python_version(),np.__version__],'protocol_sha256':hashlib.sha256((P/'ablation_protocol.md').read_bytes()).hexdigest(),'E0':E0,'columns':['norm','initial_overlap','winding_fraction','phase_current','m3','continuity','mu_mass','m3_phase'],'source_columns':['gross_increment','forcing_squared_norm','overlap_real','sink'],'windows':windows,'checkpoints':checkpoints,'cases':[]}
for W in (.02,.10):
 for seed in SEEDS:
  perm=np.random.default_rng(seed+100).permutation(N*N);kick=.5*np.random.default_rng(seed+200).normal(size=(N,N))*ring;k=np.full((N,N),.4);cfg=CoreConfig(use_mu=False,noise_strength=0.)
  for mode in modes:
   lanes=[{'psi':initial.copy(),'phi':np.zeros_like(r),'kappa':k.copy(),'mu':np.zeros_like(r)} for _ in range(2)];rows=[[],[]];works=[[],[]];dist=[];kick_distance=None;np.random.seed(seed)
   for t in range(T):
    if t==64:
     old=norm(lanes[1]['psi']);lanes[1]['psi']*=np.exp(1j*kick);assert abs(norm(lanes[1]['psi'])-old)<1e-10*max(1.,old);kick_distance=1-overlap(lanes[0]['psi'],lanes[1]['psi'])
    rng=np.random.get_state()
    for i in range(2):
     np.random.set_state(rng);prev=lanes[i]['psi'].copy();lanes[i],work=step(lanes[i],cfg,mode,t,perm);end=np.random.get_state()
     if i==0:after=end
     else:assert np.array_equal(after[1],end[1]) and after[2:]==end[2:]
     rows[i].append(measure(lanes[i]['psi'],prev,lanes[i]['mu']));works[i].append(work)
    dist.append(1-overlap(lanes[0]['psi'],lanes[1]['psi']))
   case={'seed':seed,'material':'no_birth_no_noise','budget':W,'mode':mode,'kick_distance':kick_distance,'distance_checkpoints':[dist[t] for t in checkpoints],'lanes':[]}
   for i in range(2):
    a=np.asarray(works[i]);assert abs(a[:,0].sum()-(0 if mode=='quiet' else W*DRIVE))<1e-8
    assert np.all(a[DRIVE:,0]==0) and np.all(a[DRIVE:,3]==0)
    obs=[aggregate(rows[i],*w) for w in windows];late=np.array(obs[1]['sums'])/obs[1]['count'];post=np.array(obs[2]['sums'])/obs[2]['count']
    late_gate=bool(late[2]>=.9 and late[1]>=.5 and late[4]>=.1 and late[5]>=.95 and dist[127]<=kick_distance/2);gate=bool(late_gate and post[2]>=.5)
    case['lanes'].append({'window':obs,'checkpoints':[rows[i][t] for t in checkpoints],'source_sums':a.sum(0).tolist(),'source_max_forcing':float(a[:,1].max()),'gate':gate,'late_gate':late_gate})
   result['cases'].append(case)
(P/'ablation.json').write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
for W in (.02,.10):
 for mode in modes:
  cases=[c for c in result['cases'] if c['budget']==W and c['mode']==mode];ls=[c['lanes'][0] for c in cases];late=np.median([np.asarray(l['window'][1]['sums'])/32 for l in ls],axis=0);post=np.median([np.asarray(l['window'][2]['sums'])/32 for l in ls],axis=0);rec=np.median([c['distance_checkpoints'][6]/max(c['kick_distance'],1e-30) for c in cases]);print(W,mode,'norm overlap winding current m3 continuity mu',np.round(late,5).tolist(),'post',np.round(post[[0,1,2,4]],5).tolist(),'recovery',round(float(rec),4),'gate',sum(l['gate'] for c in cases for l in c['lanes']))
