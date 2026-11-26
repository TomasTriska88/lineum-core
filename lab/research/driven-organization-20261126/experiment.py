import json, hashlib, platform
from pathlib import Path
import numpy as np
from core_numpy_excerpt import CoreConfig,_step_numpy
P=Path(__file__).parent
assert hashlib.sha256((P/'core_numpy_excerpt.py').read_bytes()).hexdigest()=='cea229a9dd5885471e389a238f022d8ea05f187828f3c7434b314456d8026c44'
N=32; T=192; DRIVE=128; W=.02; SEEDS=(26112700,26112701,26112702)
y,x=np.indices((N,N));y=y-15.5;x=x-15.5;r=np.hypot(x,y);theta=np.arctan2(y,x)
ring=np.exp(-.5*((r-5)/1.8)**2); initial=.22*ring*(1+.45*np.cos(3*theta))*np.exp(1j*theta)
E0=float(np.sum(abs(initial)**2)); centered=np.exp(-r*r/8); shifted=np.exp(-((x-7)**2+y*y)/8)
materials={'base':(np.full((N,N),.4),False),'mu':(np.full((N,N),.4),True),'kappa_ring':(.4+.2*(ring.mean()-ring)/(1-ring.mean()),False)}
assert all(abs(k.mean()-.4)<1e-14 and k.min()>0 and k.max()<1 for k,_ in materials.values())
modes=('quiet','periodic','continuous','shifted','ring','aligned','shuffled_phase','flat_aligned','adaptive')
windows=((32,63),(96,127),(160,191)); checkpoints=(0,31,63,64,80,95,127,159,191)
paths=[]
for a in (4,6,8):
 lo=16-a;hi=15+a
 pts=[(lo,j) for j in range(lo,hi)]+[(j,hi) for j in range(lo,hi)]+[(hi,j) for j in range(hi,lo,-1)]+[(j,lo) for j in range(hi,lo,-1)]
 paths.append(tuple(np.asarray(pts).T))
def norm(z):return float(np.sum(abs(z)**2))
def overlap(a,b):return float(abs(np.vdot(a,b))/max(np.sqrt(norm(a)*norm(b)),1e-30))
def source(z,mode,t,perm):
 if t>=DRIVE or mode=='quiet' or (mode=='periodic' and t%8):return z,0.,0.,0.
 work=W*(8 if mode=='periodic' else 1);env=shifted if mode=='shifted' else ring if mode in ('ring','aligned','shuffled_phase') else np.ones_like(r) if mode=='flat_aligned' else centered
 phase=np.exp(1j*np.angle(z)) if mode in ('aligned','shuffled_phase','flat_aligned') else np.ones_like(z)
 if mode=='shuffled_phase':phase=phase.ravel()[perm].reshape(N,N)
 d=env*phase;d=d/np.sqrt(norm(d));cross=float(np.vdot(z,d).real)
 a=np.sqrt(cross*cross+work)-cross if cross<=0 else work/(np.sqrt(cross*cross+work)+cross)
 v=z+a*d;actual=norm(v)-norm(z);assert abs(actual-work)<1e-10*max(1.,norm(z))
 return v,actual,a*a,cross

def measure(z,prev,m):
 wind=[];cur=[]
 for p in paths:
  a=z[p];b=np.roll(a,-1);q=b*np.conj(a);wind.append(float(np.angle(q).sum()/(2*np.pi)));cur.append(float(q.imag.sum()/max(abs(q).sum(),1e-30)))
 density=abs(z)**2; c=np.sum(density*ring*np.exp(-3j*theta))/max(np.sum(density*ring),1e-30)
 return [norm(z),overlap(initial,z),float(np.mean(np.abs(np.asarray(wind)-1)<1e-6)),float(np.mean(cur)),float(abs(c)),float(overlap(prev,z)),float(m.sum()),float(np.angle(c))]

def step(s,cfg,mode,t,perm):
 z,w,crossnorm,cross=source(s['psi'],mode,t,perm);s['psi']=z
 s=_step_numpy(s,cfg);sink=0.
 if mode=='adaptive' and t<DRIVE:
  e=norm(s['psi']);factor=np.sqrt(max(.9,min(1.,E0/max(e,1e-30))));s['psi']*=factor;sink=e-norm(s['psi'])
 assert all(np.isfinite(v).all() for v in s.values()) and abs(s['psi']).max()<.99e6 and s['mu'].min()>=0 and s['mu'].max()<=10
 return s,[w,crossnorm,cross,sink]

def aggregate(rows,a,b):
 z=np.asarray(rows[a:b+1]);v=z[:,4]>=.1;angle=z[:,7];dif=np.angle(np.exp(1j*np.diff(angle)));mask=v[1:]&v[:-1]
 return {'count':len(z),'sums':z[:,:7].sum(0).tolist(),'valid_m3':int(v.sum()),'orientation_steps':int(mask.sum()),'orientation_signed':float(-dif[mask].sum()/3),'orientation_absolute':float(abs(dif[mask]).sum()/3)}
result={'environment':[platform.python_version(),np.__version__],'protocol_sha256':hashlib.sha256((P/'protocol.md').read_bytes()).hexdigest(),'E0':E0,'columns':['norm','initial_overlap','winding_fraction','phase_current','m3','continuity','mu_mass','m3_phase'],'source_columns':['gross_increment','forcing_squared_norm','overlap_real','sink'],'windows':windows,'checkpoints':checkpoints,'cases':[]}
for seed in SEEDS:
 perm=np.random.default_rng(seed+100).permutation(N*N);kick=.5*np.random.default_rng(seed+200).normal(size=(N,N))*ring
 for material,(k,learn) in materials.items():
  cfg=CoreConfig(use_mu=learn)
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
   case={'seed':seed,'material':material,'mode':mode,'kick_distance':kick_distance,'distance_checkpoints':[dist[t] for t in checkpoints],'lanes':[]}
   for i in range(2):
    a=np.asarray(works[i]);assert abs(a[:,0].sum()-(0 if mode=='quiet' else W*DRIVE))<1e-8
    assert np.all(a[DRIVE:,0]==0) and np.all(a[DRIVE:,3]==0)
    obs=[aggregate(rows[i],*w) for w in windows];late=np.array(obs[1]['sums'])/obs[1]['count'];post=np.array(obs[2]['sums'])/obs[2]['count']
    gate=bool(late[2]>=.9 and late[1]>=.5 and late[4]>=.1 and late[5]>=.95 and dist[127]<=kick_distance/2 and post[2]>=.5)
    case['lanes'].append({'window':obs,'checkpoints':[rows[i][t] for t in checkpoints],'source_sums':a.sum(0).tolist(),'source_max_forcing':float(a[:,1].max()),'gate':gate})
   result['cases'].append(case)
(P/'result.json').write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
for mat in materials:
 for mode in modes:
  cases=[c for c in result['cases'] if c['material']==mat and c['mode']==mode];ls=[c['lanes'][0] for c in cases];late=np.median([np.asarray(l['window'][1]['sums'])/32 for l in ls],axis=0);post=np.median([np.asarray(l['window'][2]['sums'])/32 for l in ls],axis=0);rec=np.median([c['distance_checkpoints'][6]/max(c['kick_distance'],1e-30) for c in cases]);print(mat,mode,'norm overlap winding current m3 continuity mu',np.round(late,5).tolist(),'post',np.round(post[[1,2,4]],5).tolist(),'recovery',round(float(rec),4),'gate',sum(l['gate'] for c in cases for l in c['lanes']))
