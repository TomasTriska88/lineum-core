import hashlib,json,platform
from pathlib import Path
import numpy as np
from core_numpy_excerpt import CoreConfig,_step_numpy
P=Path(__file__).parent
assert hashlib.sha256((P/'core_numpy_excerpt.py').read_bytes()).hexdigest()=='cea229a9dd5885471e389a238f022d8ea05f187828f3c7434b314456d8026c44'
N,T=24,96
Y,X=np.indices((N,N)); mid=N//2
D=np.minimum(abs(Y-mid),N-abs(Y-mid))+np.minimum(abs(X-mid),N-abs(X-mid)); far=D>=3
K=np.full((N,N),.8); modes=('learned','shuffled','uniform','zero','frozen')
fields=('psi','phi','kappa','mu'); dirs=((0,4),(4,0),(0,-4),(-4,0))
def state(mu,point=None):
 s={'psi':np.zeros((N,N),complex),'phi':np.zeros((N,N)),'kappa':K.copy(),'mu':mu.copy()}
 if point is not None:s['psi'][point]=.32
 return s
def copy(s):return {k:v.copy() for k,v in s.items()}
def gate(s):
 a=np.clip(abs(s['psi']),0,1e6); gx,gy=np.gradient(a); gx=np.clip(gx,-1e6,1e6); gy=np.clip(gy,-1e6,1e6)
 return (1/(1+np.exp(-5*(a+np.sqrt(np.clip(gx**2+gy**2,0,1e12))))))*s['kappa']
def components(mask):
 todo=set(map(tuple,np.argwhere(mask))); n=0
 while todo:
  n+=1; q=[todo.pop()]
  while q:
   y,x=q.pop()
   for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
    p=((y+a)%N,(x+b)%N)
    if p in todo:todo.remove(p);q.append(p)
 return n
def norms(a):return float(np.sum(abs(a)**2))
def summaries(rows):
 a=np.asarray(rows,float); E=a[:,4]; F=a[:,5]; A=a[:,6]
 return dict(remote_extra=int(a[:,0].sum()),remote_suppressed=int(a[:,1].sum()),max_components=int(a[:,2].max()),max_remote_peaks=int(a[:,3].max()),remote_integral=float(F.sum()),ablation_remote_integral=float(A.sum()),relative_causal_effect=float((F.sum()-A.sum())/max(F.sum(),1e-30)),excess_final_to_peak=float(np.mean(np.sqrt(E[-16:]))/max(np.sqrt(E.max()),1e-30)),baseline_final_rms=float(np.mean(np.sqrt(a[-16:,7]/N**2))),mu_difference_final=float(a[-1,8]),near_history_integral=float(a[:,9].sum()),opposite_history_integral=float(a[:,10].sum()))
result={'environment':{'python':platform.python_version(),'numpy':np.__version__},'columns':['remote_extra_gates','remote_suppressed_gates','positive_gate_components','remote_excess_local_maxima','excess_psi_squared_norm','far_excess_psi_squared_norm','far_ablation_excess_psi_squared_norm','baseline_psi_squared_norm','mu_difference_l1','trained_location_excess_squared_norm','opposite_location_excess_squared_norm'],'cases':[],'training':[]}
for i in range(8):
 seed=26112600+i; dy,dx=dirs[i%4]; p=(mid+dy,mid+dx); op=(mid-dy,mid-dx)
 np.random.seed(seed+1000); s=state(np.zeros((N,N)),p)
 for t in range(32):s=_step_numpy(s,CoreConfig(use_mu=True))
 mu=s['mu'].copy(); perm=np.random.default_rng(seed+2000).permutation(mu.ravel()).reshape(N,N); uniform=np.full_like(mu,mu.mean()); assert np.array_equal(np.sort(mu.ravel()),np.sort(perm.ravel())); assert abs(mu.sum()-uniform.sum())<1e-10
 result['training'].append({'seed':seed,'location':p,'mu':mu.tolist(),'mass':float(mu.sum())})
 for mode,m in zip(modes,(mu,perm,uniform,np.zeros_like(mu),mu)):
  cfg=CoreConfig(use_mu=mode!='frozen'); b=state(m); u=state(m,(mid,mid)); a=copy(u); np.random.seed(seed); rows=[]; first=np.full((N,N),-1,int); plus=np.zeros((N,N),int); minus=np.zeros((N,N),int)
  for t in range(T):
   rng=np.random.get_state(); rs=np.random.RandomState(); rs.set_state(rng); r=rs.rand(N,N); gb=gate(b); gu=gate(u); ga=gate(a); mb=r<gb; mt=r<gu; pos=mt&~mb&far; neg=mb&~mt&far; first[(first<0)&pos]=t;plus+=pos;minus+=neg
   b=_step_numpy(b,cfg); after=np.random.get_state(); np.random.set_state(rng); u=_step_numpy(u,cfg)
   np.random.set_state(rng); original=np.random.rand; calls=[]
   def forced(*shape):
    z=original(*shape);calls.append(shape);return np.where(far,np.where(mb,ga/2,(1+ga)/2),z)
   try:np.random.rand=forced; a=_step_numpy(a,cfg)
   finally:np.random.rand=original
   assert calls==[(N,N)]; end=np.random.get_state(); assert np.array_equal(end[1],after[1]) and end[2:]==after[2:]
   assert all(np.isfinite(s[k]).all() for s in (b,u,a) for k in fields); assert all(np.array_equal(s['kappa'],K) for s in (b,u,a)); assert all(s['mu'].min()>=0 and s['mu'].max()<10 and abs(s['psi']).max()<1e6*.99 and s['phi'].max()<1e6 for s in (b,u,a))
   z=abs(u['psi']-b['psi']); zz=abs(a['psi']-b['psi']); peaks=(z>=.005)&far
   for axis in (0,1):
    for shift in (-1,1):peaks&=z>np.roll(z,shift,axis)
   rows.append([int(pos.sum()),int(neg.sum()),components(pos),int(peaks.sum()),norms(z),norms(z[far]),norms(zz[far]),norms(b['psi']),float(abs(u['mu']-b['mu']).sum()),norms(z[p[0]-1:p[0]+2,p[1]-1:p[1]+2]),norms(z[op[0]-1:op[0]+2,op[1]-1:op[1]+2])])
  result['cases'].append(dict(seed=seed,mode=mode,rows=rows,first_positive_remote_gate=first.tolist(),positive_gate_counts=plus.tolist(),negative_gate_counts=minus.tolist(),summary=summaries(rows)))
result['summary']={mode:{k:float(np.median([c['summary'][k] for c in result['cases'] if c['mode']==mode])) for k in result['cases'][0]['summary']} for mode in modes}
learn=[c['summary'] for c in result['cases'] if c['mode']=='learned'];result['gate_count']=sum(c['remote_extra']>0 and c['max_components']>=2 and c['relative_causal_effect']>0 for c in learn);result['gate_pass']=result['gate_count']>=6 and result['summary']['learned']['relative_causal_effect']>0
(P/'results.json').write_text(json.dumps(result,separators=(',',':'),sort_keys=True)+'\n');print(json.dumps({'summary':result['summary'],'gate_count':result['gate_count'],'gate_pass':result['gate_pass']},indent=2))
