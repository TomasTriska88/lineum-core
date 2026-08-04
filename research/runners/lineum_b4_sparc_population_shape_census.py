#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, csv, hashlib, itertools, json, lzma, math, os, platform, sys, zipfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import differential_evolution, least_squares, minimize

ARCHIVE_SHA='0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588'
RS=5.0
V0B=(0.0,400.0); KB=(1e-6,100.0)
V0S=(25.0,75.0,150.0,250.0); KS=(0.01,0.1,1.0,10.0)
STARTS=list(itertools.product(V0S,KS))
SHAPES=('tanh','exponential','rational','arctan','algebraic')
LANES=('unsigned_fiducial','signed_fiducial')
CURVE_TOL=1e-5
SEED=20260804

def sha_bytes(b:bytes)->str: return hashlib.sha256(b).hexdigest()

def parse_member(payload:bytes)->np.ndarray:
    rows=[]
    for line in payload.decode('utf-8').splitlines():
        if not line.strip() or line.lstrip().startswith('#'): continue
        rows.append([float(x) for x in line.split()])
    a=np.asarray(rows,float)
    if a.ndim!=2 or a.shape[1]!=8 or not np.isfinite(a).all():
        raise ValueError(f'invalid member shape/content: {a.shape}')
    if not np.all(np.diff(a[:,0])>0) or not np.all(a[:,2]>0):
        raise ValueError('radii must increase and uncertainties must be positive')
    return a

def shape_value(name:str,x):
    if name=='tanh': return np.tanh(x)
    if name=='exponential': return 1.0-np.exp(-x)
    if name=='rational': return x/(1.0+x)
    if name=='arctan': return (2.0/np.pi)*np.arctan((np.pi/2.0)*x)
    if name=='algebraic': return x/np.sqrt(1.0+x*x)
    raise KeyError(name)

def shape_scalar(name:str,x:float)->float:
    if name=='tanh': return math.tanh(x)
    if name=='exponential': return 1.0-math.exp(-x)
    if name=='rational': return x/(1.0+x)
    if name=='arctan': return (2.0/math.pi)*math.atan((math.pi/2.0)*x)
    if name=='algebraic': return x/math.sqrt(1.0+x*x)
    raise KeyError(name)

def bary2(a:np.ndarray,lane:str)->np.ndarray:
    gas=np.sign(a[:,3])*a[:,3]**2 if lane=='signed_fiducial' else a[:,3]**2
    return gas+0.5*a[:,4]**2+0.7*a[:,5]**2

def curve(a:np.ndarray,lane:str,shape:str,p)->np.ndarray:
    total=bary2(a,lane)+float(p[0])**2*shape_value(shape,float(p[1])*a[:,0]/RS)
    return np.sqrt(np.maximum(total,0.0))

def objective(a,lane,shape,p)->float:
    y=curve(a,lane,shape,p)
    return float(np.sum(((y-a[:,1])/a[:,2])**2))

def de_powell(a,lane,shape,seed):
    f=lambda p: objective(a,lane,shape,p)
    de=differential_evolution(f,[V0B,KB],seed=seed,popsize=15,maxiter=600,tol=1e-10,atol=1e-10,polish=False,workers=1,updating='immediate')
    po=minimize(f,de.x,method='Powell',bounds=[V0B,KB],options={'xtol':1e-12,'ftol':1e-12,'maxiter':100000})
    if float(po.fun)<=float(de.fun): return {'chi2':float(po.fun),'parameters':[float(x) for x in po.x],'de_chi2':float(de.fun),'de_success':bool(de.success),'powell_success':bool(po.success)}
    return {'chi2':float(de.fun),'parameters':[float(x) for x in de.x],'de_chi2':float(de.fun),'de_success':bool(de.success),'powell_success':bool(po.success)}

def fit_shape(a,lane,shape):
    obs=a[:,1]; err=a[:,2]
    def fun(p): return (curve(a,lane,shape,p)-obs)/err
    starts=[]; ys=[]; sols=[]
    for x0 in STARTS:
        z=least_squares(fun,x0,bounds=([V0B[0],KB[0]],[V0B[1],KB[1]]),method='trf',jac='2-point',loss='linear',xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=100000)
        y=curve(a,lane,shape,z.x); c=float(np.sum(((y-obs)/err)**2))
        starts.append({'initial':[float(x0[0]),float(x0[1])],'parameters':[float(z.x[0]),float(z.x[1])],'chi2':c,'success':bool(z.success),'status':int(z.status),'nfev':int(z.nfev),'optimality':float(z.optimality)})
        ys.append(y); sols.append(z)
    best_i=min(range(len(starts)),key=lambda i: starts[i]['chi2'])
    best=starts[best_i]; best_y=ys[best_i]
    maxd=max(float(np.max(np.abs(y-best_y))) for y in ys)
    stable=(sum(s['success'] for s in starts)==len(STARTS) and maxd<=CURVE_TOL)
    fallback=None
    if not stable:
        fallback=de_powell(a,lane,shape,SEED)
        if fallback['chi2'] < best['chi2']:
            best={'initial':None,'parameters':fallback['parameters'],'chi2':fallback['chi2'],'success':True,'status':99,'nfev':None,'optimality':None}
            best_i=-1; best_y=curve(a,lane,shape,best['parameters'])
    p=best['parameters']; active=(p[0]<=1e-8 or p[0]>=400-1e-8 or p[1]<=1e-6+1e-10 or p[1]>=100-1e-8)
    scalar_chi2=0.0; scalar_max=0.0
    b=bary2(a,lane)
    for i in range(len(a)):
        tot=float(b[i])+p[0]**2*shape_scalar(shape,p[1]*float(a[i,0])/RS)
        y=math.sqrt(max(tot,0.0)); scalar_max=max(scalar_max,abs(y-float(best_y[i]))); scalar_chi2+=((y-float(obs[i]))/float(err[i]))**2
    return {'shape':shape,'best_start_index':best_i,'V0':p[0],'k_eff':p[1],'chi2':float(best['chi2']),'aic':float(best['chi2']+4.0),'converged_starts':sum(s['success'] for s in starts),'max_curve_difference':maxd,'stable_multistart':stable,'boundary_contact':bool(active),'fallback':fallback,'scalar_chi2':scalar_chi2,'scalar_chi2_difference':abs(scalar_chi2-float(best['chi2'])),'scalar_curve_max_difference':scalar_max,'starts':starts}

def process_galaxy(task):
    name,payload=task; a=parse_member(payload); out={'galaxy':name.replace('_rotmod.dat',''),'member':name,'member_sha256':sha_bytes(payload),'n_rows':int(len(a)),'rmax_kpc':float(a[:,0].max()),'vmax_kms':float(a[:,1].max()),'has_bulge':bool(np.any(np.abs(a[:,5])>0)),'negative_gas_rows':int(np.sum(a[:,3]<0)),'lanes':{}}
    for lane in LANES:
        bb=bary2(a,lane)
        fits=[fit_shape(a,lane,s) for s in SHAPES]
        fits.sort(key=lambda x:x['aic'])
        bary_chi2=float(np.sum(((np.sqrt(np.maximum(bb,0.0))-a[:,1])/a[:,2])**2))
        best=fits[0]; second=fits[1]; tanh=next(x for x in fits if x['shape']=='tanh')
        da_t=float(tanh['aic']-best['aic']); da2=float(second['aic']-best['aic']); improve=float(bary_chi2-best['aic'])
        informative=(len(a)>=10 and improve>=10 and not best['boundary_contact'])
        label=('compatible' if da_t<2 else ('tension' if da_t<10 else 'strongly_rejected'))
        out['lanes'][lane]={'baryons_chi2':bary_chi2,'baryons_aic':bary_chi2,'best_shape':best['shape'],'best_aic':best['aic'],'second_shape':second['shape'],'second_delta_aic':da2,'delta_aic_tanh':da_t,'tanh_best':da_t<=1e-8,'tanh_label':label,'shape_identified':da2>=2,'added_component_needed':improve>=10,'informative':informative,'negative_bary2_rows':int(np.sum(bb<0)),'fits':fits}
    return out

def select_audit(names):
    return [n for _,n in sorted((hashlib.sha256(n.encode()).hexdigest(),n) for n in names)[:20]]

def aggregate(galaxies):
    result={'all_count':len(galaxies),'n_ge_10':sum(g['n_rows']>=10 for g in galaxies),'lanes':{},'joint':{}}
    for lane in LANES:
        info=[g for g in galaxies if g['lanes'][lane]['informative']]
        labels=[g['lanes'][lane]['tanh_label'] for g in info]
        deltas=[g['lanes'][lane]['delta_aic_tanh'] for g in info]
        winners={s:sum(g['lanes'][lane]['best_shape']==s for g in info) for s in SHAPES}
        compat=sum(x=='compatible' for x in labels); reject=sum(x=='strongly_rejected' for x in labels)
        result['lanes'][lane]={'informative_count':len(info),'tanh_compatible_count':compat,'tanh_compatible_fraction':compat/len(info) if info else None,'tanh_strongly_rejected_count':reject,'tanh_strongly_rejected_fraction':reject/len(info) if info else None,'median_delta_aic_tanh':float(np.median(deltas)) if deltas else None,'tanh_best_count':sum(g['lanes'][lane]['tanh_best'] for g in info),'shape_identified_count':sum(g['lanes'][lane]['shape_identified'] for g in info),'winner_counts':winners}
    both=[g for g in galaxies if all(g['lanes'][l]['informative'] for l in LANES)]
    same=sum(g['lanes'][LANES[0]]['tanh_label']==g['lanes'][LANES[1]]['tanh_label'] for g in both)
    result['joint']={'informative_both_count':len(both),'same_tanh_label_count':same,'same_tanh_label_fraction':same/len(both) if both else None,'same_winner_count':sum(g['lanes'][LANES[0]]['best_shape']==g['lanes'][LANES[1]]['best_shape'] for g in both)}
    A=result['lanes']['unsigned_fiducial']; B=result['lanes']['signed_fiducial']; J=result['joint']
    supported=all(x['tanh_compatible_fraction'] is not None and x['tanh_compatible_fraction']>=.8 and x['tanh_strongly_rejected_fraction']<=.1 and x['median_delta_aic_tanh']<2 for x in (A,B)) and J['same_tanh_label_fraction'] is not None and J['same_tanh_label_fraction']>=.9
    unsupported=any(x['tanh_compatible_fraction'] is not None and (x['tanh_compatible_fraction']<.5 or x['tanh_strongly_rejected_fraction']>.3) for x in (A,B))
    result['classification']='tanh_population_supported_within_tested_family' if supported else ('tanh_population_unsupported_within_tested_family' if unsupported else 'mixed_population_evidence')
    return result

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--archive',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); ap.add_argument('--table',type=Path,required=True); ap.add_argument('--workers',type=int,default=8); args=ap.parse_args()
    payload=args.archive.read_bytes()
    if sha_bytes(payload)!=ARCHIVE_SHA: raise ValueError('archive SHA mismatch')
    with zipfile.ZipFile(args.archive) as z:
        names=sorted(n for n in z.namelist() if n.endswith('_rotmod.dat'))
        if len(names)!=175: raise ValueError(f'expected 175 members, found {len(names)}')
        tasks=[(n,z.read(n)) for n in names]
    galaxies=[]
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futs={ex.submit(process_galaxy,t):t[0] for t in tasks}
        for i,f in enumerate(as_completed(futs),1):
            galaxies.append(f.result())
            if i%10==0: print(f'completed {i}/175',flush=True)
    galaxies.sort(key=lambda g:g['galaxy'])
    agg=aggregate(galaxies)
    audit_names=select_audit([g['galaxy'] for g in galaxies]); byname={g['galaxy']:g for g in galaxies}; audit=[]
    raw_by_name={n.replace('_rotmod.dat',''):p for n,p in tasks}
    audit_tasks=[]
    for name in audit_names:
        a=parse_member(raw_by_name[name])
        for lane in LANES:
            for shape in SHAPES: audit_tasks.append((name,a,lane,shape))
    def run_audit(t):
        name,a,lane,shape=t; d=de_powell(a,lane,shape,SEED); mainfit=next(x for x in byname[name]['lanes'][lane]['fits'] if x['shape']==shape); return {'galaxy':name,'lane':lane,'shape':shape,'main_chi2':mainfit['chi2'],'independent_chi2':d['chi2'],'difference':abs(mainfit['chi2']-d['chi2']),'parameters':d['parameters']}
    for i,t in enumerate(audit_tasks,1):
        audit.append(run_audit(t))
        if i%20==0: print(f'audit {i}/{len(audit_tasks)}',flush=True)
    ngc=next(g for g in galaxies if g['galaxy']=='NGC3198')
    ngc_checks={lane:{s:next(x for x in ngc['lanes'][lane]['fits'] if x['shape']==s)['chi2'] for s in SHAPES} for lane in LANES}
    expected={'unsigned_fiducial':28.061822168198,'signed_fiducial':28.069707094507}
    ngc_pass=all(abs(ngc_checks[l]['tanh']-expected[l])<=1e-8 for l in LANES)
    scalar_max=max(x['scalar_chi2_difference'] for g in galaxies for l in LANES for x in g['lanes'][l]['fits'])
    scalar_curve_max=max(x['scalar_curve_max_difference'] for g in galaxies for l in LANES for x in g['lanes'][l]['fits'])
    audit_max=max(x['difference'] for x in audit)
    rows=[]
    for g in galaxies:
        for lane in LANES:
            L=g['lanes'][lane]
            rows.append({'galaxy':g['galaxy'],'n_rows':g['n_rows'],'rmax_kpc':g['rmax_kpc'],'vmax_kms':g['vmax_kms'],'has_bulge':g['has_bulge'],'negative_gas_rows':g['negative_gas_rows'],'lane':lane,'negative_bary2_rows':L['negative_bary2_rows'],'baryons_chi2':L['baryons_chi2'],'best_shape':L['best_shape'],'best_aic':L['best_aic'],'second_shape':L['second_shape'],'second_delta_aic':L['second_delta_aic'],'delta_aic_tanh':L['delta_aic_tanh'],'tanh_label':L['tanh_label'],'tanh_best':L['tanh_best'],'shape_identified':L['shape_identified'],'added_component_needed':L['added_component_needed'],'informative':L['informative']})
    with args.table.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    full={'schema':'lineum-b4-sparc-population-census/1','scope':'all 175 official SPARC rotation curves; five equal-flexibility saturation shapes; two fiducial gas lanes','input':{'archive_sha256':ARCHIVE_SHA,'member_count':175,'member_hashes':{g['member']:g['member_sha256'] for g in galaxies}},'protocol':{'shapes':SHAPES,'lanes':LANES,'starts':STARTS,'bounds':{'V0':V0B,'k_eff':KB},'curve_tolerance_kms':CURVE_TOL,'seed':SEED,'primary_min_rows':10},'aggregate':agg,'galaxies':galaxies,'independent_audit':{'selected_names':audit_names,'results':audit,'max_chi2_difference':audit_max},'checks':{'ngc3198':ngc_checks,'ngc3198_pass':ngc_pass,'max_scalar_chi2_difference':scalar_max,'max_scalar_curve_difference_kms':scalar_curve_max,'all_input_uncertainties_positive':True,'all_files_eight_columns':True},'environment':{'python':sys.version.split()[0],'numpy':np.__version__,'scipy':scipy.__version__,'platform':platform.platform(),'workers':args.workers,'requirement_mismatch':'repository requires numpy<2; runtime supplied '+np.__version__},'anti_cheat':{'private_tolog_document_used':False,'post_hoc_shape_tuning':False,'galaxy_selection_by_fit':False,'lineum_engine_modified':False}}
    raw=json.dumps(full,separators=(',',':'),sort_keys=True).encode()
    wrapper={'schema':'compressed-research-receipt/1','classification':agg['classification'],'summary':agg,'uncompressed_sha256':sha_bytes(raw),'encoding':'lzma+base64 UTF-8 JSON','payload':base64.b64encode(lzma.compress(raw,preset=9)).decode()}
    args.output.write_text(json.dumps(wrapper,separators=(',',':'),sort_keys=True)+'\n')
    print(json.dumps({'classification':agg['classification'],'summary':agg,'checks':full['checks'],'audit_max_difference':audit_max},indent=2))

if __name__=='__main__': main()
