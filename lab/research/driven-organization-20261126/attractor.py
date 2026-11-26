import json,hashlib,platform
from pathlib import Path
import numpy as np
P=Path(__file__).parent
p=P/'ablation.py'
# Use verified prior definitions, not earlier top-level runs.
exec(compile(p.read_text().split('for W in (.02,.10):',1)[0],str(p),'exec'))
original=initial.copy();base_energy=E0;W=.10;DRIVE=512;T=640
shapes={'plus_lobes':original,'minus_lobes':np.conj(original),'zero_winding':abs(original).astype(complex),'plus_round':.22*ring*np.exp(1j*theta)}
shapes={n:z*np.sqrt(base_energy/norm(z)) for n,z in shapes.items()};modes=('quiet','ring','aligned');checkpoints=(0,31,127,255,383,511,575,639);windows=((480,511),(608,639));cfg=CoreConfig(use_mu=False,noise_strength=0.)
perm=np.random.default_rng(26112800).permutation(N*N)
def minus_fraction(z):
 return float(np.mean([abs(np.angle(np.roll(z[p],-1)*np.conj(z[p])).sum()/(2*np.pi)+1)<1e-6 for p in paths]))
result={'environment':[platform.python_version(),np.__version__],'protocol_sha256':hashlib.sha256((P/'attractor_protocol.md').read_bytes()).hexdigest(),'E0':base_energy,'windows':windows,'checkpoints':checkpoints,'columns':['norm','initial_overlap','winding_plus_fraction','phase_current','m3','continuity','mu_mass','m3_phase','winding_minus_fraction','max_amp'],'cases':[],'pairs':[]}
for mode in modes:
 endpoints={511:{},639:{}}
 for name,initial in shapes.items():
  E0=norm(initial);s={'psi':initial.copy(),'phi':np.zeros_like(r),'kappa':np.full((N,N),.4),'mu':np.zeros_like(r)};rows=[];works=[];np.random.seed(26112700)
  for t in range(T):
   prev=s['psi'].copy();s,w=step(s,cfg,mode,t,perm);z=s['psi'];rows.append(measure(z,prev,s['mu'])+[minus_fraction(z),float(abs(z).max())]);works.append(w)
   if t in endpoints:endpoints[t][name]=z.copy()
  a=np.asarray(works);assert abs(a[:,0].sum()-(0 if mode=='quiet' else .1*512))<1e-8 and np.all(a[DRIVE:,0]==0)
  obs=[dict(aggregate(rows,*w),minus_sum=float(np.asarray(rows[w[0]:w[1]+1])[:,8].sum())) for w in windows]
  result['cases'].append(dict(mode=mode,shape=name,window=obs,checkpoints=[rows[t] for t in checkpoints],source_sums=a.sum(0).tolist()))
 for t,states in endpoints.items():
  keys=list(states);pairs=[dict(a=a,b=b,overlap=overlap(states[a],states[b])) for i,a in enumerate(keys) for b in keys[i+1:]]
  result['pairs'].append(dict(mode=mode,tick=t,pairs=pairs))
(P/'attractor.json').write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
for c in result['cases']:
 print(c['mode'],c['shape'],'drive',np.round(np.asarray(c['window'][0]['sums'])/32,6).tolist(),'minus',c['window'][0]['minus_sum']/32,'post',np.round(np.asarray(c['window'][1]['sums'])/32,6).tolist())
for c in result['pairs']:print(c['mode'],c['tick'],'min pair overlap',min(p['overlap'] for p in c['pairs']))
