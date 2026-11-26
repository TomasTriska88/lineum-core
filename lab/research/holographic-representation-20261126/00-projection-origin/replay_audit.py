import numpy as np, scipy.sparse as sp, importlib.util, hashlib, json
from pathlib import Path
from PIL import Image,ImageDraw
R=Path(__file__).parent
N=96; P=np.array([77,48]); d=np.arange(-18,19)[:,None,None]; y,x=np.mgrid[:N,:N].astype(float);y-=77;x-=48
src=R/'used_frames.npz'
expected=json.loads((R/'expected.json').read_text())
frames=np.load(src,allow_pickle=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert frames['source'].shape==(32,96,96)
a=frames['source']; tau=-np.log1p(-np.minimum(a.astype(float)/255,1-1e-6)); T=tau.reshape(len(a),-1).T
# Positive controls: original functions, identical source frames, no solver rerun.
def load(v):
 p=R/f'v{v}/campfire-isometric-v{v}/project.py';s=importlib.util.spec_from_file_location(f'v{v}',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mods={v:load(v) for v in (7,8)}
def metric(a):
 a=a.astype(float);return dict(contrast=float(np.abs(np.diff(a,axis=2)).sum()/max(a.sum(),1e-20)),mass=float(a.sum()/len(a)),area=float((a>.5).sum((1,2)).mean()),edge_max=float(max(a[:,0,:].max(),a[:,-1,:].max(),a[:,:,0].max(),a[:,:,-1].max())))
res={'source_sha256':expected['source_sha256'],'project_sha256':{v:sha(R/f'v{v}/campfire-isometric-v{v}/project.py') for v in (7,8)},'frames':[60,91],'original':{},'splat':{},'data_keys':expected['data_keys']}; pics={}
for yaw,el in [(0,0),(30,0),(45,35.26438968),(60,0),(80,0)]:
 key=f'{yaw}/{el}'; res['original'][key]={}
 for v,m in mods.items():
  z=m.project(a,'flame',yaw,el);res['original'][key][v]=metric(z/255)
  if yaw==45:
   ref=frames[f'iso_v{v}']
   res['original'][key][v]['matches_archive']=bool(np.array_equal(z,ref))
  if yaw==0: assert np.array_equal(z,a)
# independent forward orthographic projection with fixed common scale, no obliquity factor.
w7=5+3*np.exp(-(y/14)**2); c7=1.6*np.sin(x/7)*np.exp(-((y+9)/36)**2)
w8=1.05+1.35*np.exp(-(y/10)**2);c8=.32*x+1.65*np.sin(x/5.5+y/16)*(.4+.6*np.clip(-y/55,0,1))
weights={}
for key,w,c in [('v7',w7,c7),('v8',w8,c8),('width_only',w8,c7),('center_only',w7,c8),('flat_thin',w8,np.zeros_like(c8))]:
 q=np.exp(-.5*((d-c)/w)**2);weights[key]=(q/q.sum(0)).ravel()
cols=np.tile(np.arange(N*N),37)
for yaw,el in [(0,0),(30,0),(45,35.26438968),(60,0),(80,0),(90,0),(-45,35.26438968),(135,0),(90,35.26438968)]:
 th,e=np.deg2rad([yaw,el]);c,s=np.cos(th),np.sin(th);ce,se=np.cos(e),np.sin(e);scale=1 if yaw==el==0 else .88
 X=np.broadcast_to(48+scale*(c*x+s*d),(37,N,N)).ravel();Y=np.broadcast_to(77+scale*(ce*y+se*(s*x-c*d)),(37,N,N)).ravel();ix=np.floor(X).astype(int);iy=np.floor(Y).astype(int);fx=X-ix;fy=Y-iy
 key=f'{yaw}/{el}';res['splat'][key]={}
 for name,w in weights.items():
  rr=[];cc=[];vv=[]
  for dx,dy,f in [(0,0,(1-fx)*(1-fy)),(1,0,fx*(1-fy)),(0,1,(1-fx)*fy),(1,1,fx*fy)]:
   xx=ix+dx;yy=iy+dy;valid=(xx>=0)&(xx<N)&(yy>=0)&(yy<N);rr.append((yy[valid]*N+xx[valid]));cc.append(cols[valid]);vv.append((f*w)[valid])
  M=sp.coo_matrix((np.concatenate(vv),(np.concatenate(rr),np.concatenate(cc))),shape=(N*N,N*N)).tocsr();opt=(M@T).T.reshape(-1,N,N)/scale**2
  z=-np.expm1(-opt);m=metric(z);m['optical_mass_fraction']=float(opt.sum()*scale**2/tau.sum());res['splat'][key][name]=m
  if name in ('v7','v8','flat_thin'):pics[key,name]=np.rint(z[15]*255).astype('uint8')
  if yaw==el==0:assert np.max(np.abs(z-a/255))<2e-6
out=R/'projection_results.json';out.write_text(json.dumps(res,indent=2)+'\n')
canvas=Image.new('RGB',(3*210,9*112),(22,27,35));dr=ImageDraw.Draw(canvas)
for i,key in enumerate(res['splat']):
 for j,n in enumerate(('v7','v8','flat_thin')):
  im=Image.fromarray(pics[key,n]).convert('RGB');canvas.paste(im,(j*210+95,i*112+8));dr.text((j*210+6,i*112+12),f'{key}\n{n}',fill='white')
canvas.save(R/'projection_comparison.png')
print(json.dumps(res,indent=2))
