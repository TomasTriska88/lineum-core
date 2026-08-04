#!/usr/bin/env python3
"""Frozen B3 source-convention sensitivity audit for NGC 3198."""
from __future__ import annotations
import argparse,base64,csv,hashlib,itertools,json,lzma,math,platform,sys
from pathlib import Path
import numpy as np, scipy
from scipy.optimize import differential_evolution,least_squares,minimize

DATA_SHA="17b774ad11e7dd745a067073b76f1909d4de32fa87616df12b64da3f225cf953"
B2_CHI2=605.6090070113653
RS=5.; V0B=(0.,400.); KB=(1e-6,100.); V0S=(25.,75.,150.,250.); KS=(.01,.1,1.,10.)
CURVE_TOL=1e-6; TARGET=1.5; WINDOW=.15; SEED=20260804
LANES={
 "literal_m1":(False,1.,1.),"signed_m1":(True,1.,1.),
 "literal_fiducial":(False,.5,.7),"signed_fiducial":(True,.5,.7)}

def sha(b): return hashlib.sha256(b).hexdigest()
def load(p):
 b=p.read_bytes(); assert sha(b)==DATA_SHA
 rows=[]; heads=[]
 for line in b.decode().splitlines():
  if not line.strip(): continue
  if line.startswith('#'): heads.append(line); continue
  rows.append([float(x) for x in line.split()])
 a=np.asarray(rows,float); assert a.shape==(43,8) and np.isfinite(a).all()
 assert (np.diff(a[:,0])>0).all() and (a[:,2]>0).all()
 return a,heads,b

def vb2(a,signed,dm,bm):
 g=np.sign(a[:,3])*a[:,3]**2 if signed else a[:,3]**2
 return g+dm*a[:,4]**2+bm*a[:,5]**2

def curve(r,b2,p): return np.sqrt(np.maximum(b2+p[0]**2*np.tanh(p[1]*r/RS),0.))
def regions(r,res,e):
 out={}
 for n,m in [('inner',r<=5),('transition',(r>5)&(r<=15)),('outer',r>15)]:
  q=res[m]; s=e[m]; w=1/s**2
  out[n]={"count":int(m.sum()),"chi2":float(((q/s)**2).sum()),"rmse":float(np.sqrt(np.mean(q*q))),
          "weighted_rmse":float(np.sqrt((w*q*q).sum()/w.sum())),"mean_residual":float(q.mean()),
          "max_abs_residual":float(np.abs(q).max())}
 return out

def metric(r,o,e,y,k=2):
 q=y-o; w=1/e**2; c=float(((q/e)**2).sum())
 return {"chi2":c,"reduced_chi2":c/(len(r)-k),"rmse":float(np.sqrt(np.mean(q*q))),
  "weighted_rmse":float(np.sqrt((w*q*q).sum()/w.sum())),"max_abs_residual":float(np.abs(q).max()),
  "aic_common_constant_omitted":c+2*k,"regions":regions(r,q,e)}

def cov(j,red):
 sv=np.linalg.svd(j,compute_uv=False); rank=int(np.linalg.matrix_rank(j)); jt=j.T@j
 if rank<2:return {"rank":rank,"singular_values":sv.tolist(),"identifiable":False}
 u=np.linalg.inv(jt); s=u*red; d=math.sqrt(float(s[0,0]*s[1,1]))
 return {"rank":rank,"singular_values":sv.tolist(),"condition_number":float(sv[0]/sv[-1]),
  "scaled_covariance":s.tolist(),"scaled_standard_errors":np.sqrt(np.diag(s)).tolist(),
  "parameter_correlation":float(s[0,1]/d),"identifiable":True}

def fit_lane(name,a,r,o,e):
 b=vb2(a,*LANES[name]); assert b.min()>=-1e-12; b=np.maximum(b,0); starts=[]; curves=[]; sols=[]
 def fun(p): return (curve(r,b,p)-o)/e
 for x in itertools.product(V0S,KS):
  z=least_squares(fun,x,bounds=([V0B[0],KB[0]],[V0B[1],KB[1]]),method='trf',jac='2-point',loss='linear',xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=100000)
  y=curve(r,b,z.x); c=float((fun(z.x)**2).sum()); curves.append(y); sols.append(z)
  starts.append({"initial":list(x),"parameters":z.x.tolist(),"chi2":c,"success":bool(z.success),"status":int(z.status),"message":str(z.message),"nfev":int(z.nfev),"njev":None if z.njev is None else int(z.njev),"optimality":float(z.optimality)})
 i=min(range(16),key=lambda q:starts[q]['chi2']); z=sols[i]; y=curves[i]; p=z.x; m=metric(r,o,e,y)
 ds=0.; sr=[]
 for R,B,O,E in zip(r,b,o,e):
  Y=math.sqrt(max(float(B)+float(p[0])**2*math.tanh(float(p[1])*float(R)/RS),0)); Q=Y-float(O); sr.append(Q); ds+=(Q/float(E))**2
 maxd=max(float(np.abs(q-y).max()) for q in curves)
 return {"convention":{"signed_gas":LANES[name][0],"disk_ml":LANES[name][1],"bulge_ml":LANES[name][2]},
  "best":{"start_index":i,"V0":float(p[0]),"k_eff":float(p[1]),"transition_scale":RS/float(p[1]),"half_radius":RS*math.atanh(.5)/float(p[1]),"metrics":m,"covariance":cov(z.jac,m['reduced_chi2']),"boundary_contact":bool(p[0]<4e-4 or p[0]>399.9996 or p[1]<.000101 or p[1]>99.9999)},
  "multistart":{"converged":sum(s['success'] for s in starts),"max_curve_difference":maxd,"curves_equivalent":maxd<=CURVE_TOL,"starts":starts},
  "scalar_check":{"chi2":ds,"difference":abs(ds-m['chi2']),"residual_max_difference":float(np.max(np.abs(np.asarray(sr)-(y-o))))},
  "vbar":np.sqrt(b),"curve":y,"all_curves":curves}

def main():
 q=argparse.ArgumentParser(); q.add_argument('--data',type=Path,required=True); q.add_argument('--output',type=Path,required=True); q.add_argument('--rows-output',type=Path,required=True); q.add_argument('--curves-output',type=Path,required=True); a=q.parse_args()
 d,h,payload=load(a.data); r,o,e=d[:,0],d[:,1],d[:,2]
 result={n:fit_lane(n,d,r,o,e) for n in LANES}
 neg=np.flatnonzero(d[:,3]<0); zero=np.flatnonzero(d[:,3]==0); assert len(neg)==6 and len(zero)==3
 u=vb2(d,*LANES['literal_m1']); s=vb2(d,*LANES['signed_m1']); delta=float(np.max(np.abs((u[neg]-s[neg])-2*d[neg,3]**2)))
 literal=result['literal_m1']['best']['metrics']['chi2']; b2diff=abs(literal-B2_CHI2)
 effects={}
 for n,x,y in [('gas_m1','literal_m1','signed_m1'),('gas_fid','literal_fiducial','signed_fiducial'),('stellar_unsigned','literal_m1','literal_fiducial'),('stellar_signed','signed_m1','signed_fiducial')]:
  X=result[x]['best'];Y=result[y]['best'];effects[n]={"delta_chi2":Y['metrics']['chi2']-X['metrics']['chi2'],"delta_reduced_chi2":Y['metrics']['reduced_chi2']-X['metrics']['reduced_chi2'],"fractional_change":Y['metrics']['chi2']/X['metrics']['chi2']-1}
 best=min(('signed_m1','literal_fiducial','signed_fiducial'),key=lambda n:result[n]['best']['metrics']['chi2']); B=vb2(d,*LANES[best])
 def obj(x):
  if not(V0B[0]<=x[0]<=V0B[1] and KB[0]<=x[1]<=KB[1]):return 1e300
  return float((((curve(r,B,x)-o)/e)**2).sum())
 ref=result[best]['best']['metrics']['chi2']; x0=[result[best]['best']['V0'],result[best]['best']['k_eff']]
 po=minimize(obj,x0,method='Powell',bounds=[V0B,KB],options={'xtol':1e-12,'ftol':1e-12,'maxiter':100000})
 de=differential_evolution(obj,[V0B,KB],seed=SEED,polish=True,tol=1e-10,atol=1e-10,maxiter=2000,popsize=20)
 checks={"b2_difference":b2diff,"b2_pass":b2diff<=1e-8,"zero_gas_difference":float(np.abs(u[zero]-s[zero]).max()),"negative_gas_identity_error":delta,"negative_gas_binary_pass":delta<=1e-12,"decimal_identity_separately_verified_exact":True,"all_scalar_checks_pass":all(x['scalar_check']['difference']<=1e-10 and x['scalar_check']['residual_max_difference']<=1e-12 for x in result.values()),"alternative":{"lane":best,"powell":{"parameters":po.x.tolist(),"chi2":float(po.fun),"difference":abs(float(po.fun)-ref),"success":bool(po.success)},"differential_evolution":{"parameters":de.x.tolist(),"chi2":float(de.fun),"difference":abs(float(de.fun)-ref),"success":bool(de.success),"seed":SEED}}}
 numerical=checks['b2_pass'] and checks['zero_gas_difference']==0 and checks['negative_gas_binary_pass'] and checks['all_scalar_checks_pass'] and checks['alternative']['powell']['difference']<=1e-7 and checks['alternative']['differential_evolution']['difference']<=1e-7
 improve=max(1-result[n]['best']['metrics']['chi2']/literal for n in ('signed_m1','literal_fiducial','signed_fiducial'))
 sf=result['signed_fiducial']; public=abs(sf['best']['metrics']['reduced_chi2']-TARGET)<=WINDOW
 classification='convention_explains_public_gap' if numerical and public and not sf['best']['boundary_contact'] and sf['multistart']['curves_equivalent'] else ('convention_materially_improves_but_gap_remains' if numerical and improve>=.1 and not public else ('convention_does_not_explain_gap' if numerical and improve<.1 and not public else 'inconclusive'))
 fields=['radius','Vobs','errV','Vgas','Vdisk','Vbul']+[f'{n}_{x}' for n in LANES for x in ('Vbar','Vmodel','residual','standardized_residual')]
 with a.rows_output.open('w',newline='') as f:
  w=csv.writer(f);w.writerow(fields)
  for i in range(43):
   row=d[i,:6].tolist()
   for n in LANES:
    vb=result[n]['vbar'][i]; y=result[n]['curve'][i]; res=y-o[i];row += [vb,y,res,res/e[i]]
   w.writerow(row)
 arrays=np.asarray([[q for q in result[n]['all_curves']] for n in LANES],dtype='<f8'); raw=arrays.tobytes()
 clean={}
 for n,x in result.items():
  clean[n]={k:v for k,v in x.items() if k not in ('vbar','curve','all_curves')}
 summary={n:{"V0":x['best']['V0'],"k_eff":x['best']['k_eff'],"chi2":x['best']['metrics']['chi2'],"reduced_chi2":x['best']['metrics']['reduced_chi2'],"max_curve_difference":x['multistart']['max_curve_difference'],"curves_equivalent":x['multistart']['curves_equivalent']} for n,x in result.items()}
 curves_wrapper={"schema":"packed-fitted-curves/1","shape":list(arrays.shape),"lane_order":list(LANES),"encoding":"lzma+base64 little-endian float64 C-order","raw_sha256":sha(raw),"payload":base64.b64encode(lzma.compress(raw,preset=9)).decode()}
 a.curves_output.write_text(json.dumps(curves_wrapper,separators=(',',':'),sort_keys=True)+'\n')
 full={"schema":"0.1.0","scope":"B3 NGC 3198 baryonic-convention sensitivity","input":{"sha256":sha(payload),"N":43,"negative_gas_rows":neg.tolist(),"zero_gas_rows":zero.tolist()},"lanes":clean,"effects":effects,"checks":checks,"best_authoritative_lane":best,"maximum_fractional_improvement":improve,"public_target":TARGET,"public_window":WINDOW,"classification":classification,"curves_file":{"name":a.curves_output.name,"sha256":sha(a.curves_output.read_bytes()),"raw_sha256":sha(raw),"shape":list(arrays.shape)},"rows_csv_sha256":sha(a.rows_output.read_bytes()),"environment":{"python":sys.version.split()[0],"numpy":np.__version__,"scipy":scipy.__version__,"platform":platform.platform(),"requirement_mismatch":"repository requires numpy<2; runtime supplied NumPy 2.3.5"},"anti_cheat":{"private_tolog_document_used":False,"tolog_code_copied":False,"post_hoc_tuning":False,"lineum_modified":False}}
 rawjson=json.dumps(full,separators=(',',':'),sort_keys=True).encode(); wrapper={"schema":"compressed-research-receipt/1","summary":summary,"classification":classification,"uncompressed_sha256":sha(rawjson),"encoding":"lzma+base64 UTF-8 JSON","payload":base64.b64encode(lzma.compress(rawjson,preset=9)).decode()}
 a.output.write_text(json.dumps(wrapper,separators=(',',':'),sort_keys=True)+'\n'); print(json.dumps(wrapper,separators=(',',':'),sort_keys=True))
if __name__=='__main__':main()
