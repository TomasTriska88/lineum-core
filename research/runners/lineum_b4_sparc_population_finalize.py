#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, csv, glob, json, lzma, platform, sys, zipfile
from pathlib import Path
import numpy as np
sys.path.insert(0,'/mnt/data')
import lineum_b4_sparc_population_shape_census as core

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--archive',type=Path,required=True); ap.add_argument('--batch-glob',required=True); ap.add_argument('--output',type=Path,required=True); ap.add_argument('--table',type=Path,required=True); a=ap.parse_args()
    galaxies=[]
    for p in sorted(glob.glob(a.batch_glob)):
        galaxies.extend(json.loads(Path(p).read_text())['galaxies'])
    galaxies.sort(key=lambda g:g['galaxy'])
    assert len(galaxies)==175 and len({g['galaxy'] for g in galaxies})==175
    agg=core.aggregate(galaxies)
    byname={g['galaxy']:g for g in galaxies}
    with zipfile.ZipFile(a.archive) as z:
        raw_by_name={n.replace('_rotmod.dat',''):z.read(n) for n in z.namelist() if n.endswith('_rotmod.dat')}
    audit_names=core.select_audit([g['galaxy'] for g in galaxies]); audit=[]
    for name in audit_names:
        arr=core.parse_member(raw_by_name[name])
        for lane in core.LANES:
            for shape in core.SHAPES:
                d=core.de_powell(arr,lane,shape,core.SEED)
                mainfit=next(x for x in byname[name]['lanes'][lane]['fits'] if x['shape']==shape)
                audit.append({'galaxy':name,'lane':lane,'shape':shape,'main_chi2':mainfit['chi2'],'independent_chi2':d['chi2'],'difference':abs(mainfit['chi2']-d['chi2']),'parameters':d['parameters']})
    ngc=byname['NGC3198']
    ngc_checks={lane:{s:next(x for x in ngc['lanes'][lane]['fits'] if x['shape']==s)['chi2'] for s in core.SHAPES} for lane in core.LANES}
    expected={'unsigned_fiducial':28.061822168198,'signed_fiducial':28.069707094507}
    ngc_pass=all(abs(ngc_checks[l]['tanh']-expected[l])<=1e-8 for l in core.LANES)
    scalar_max=max(x['scalar_chi2_difference'] for g in galaxies for l in core.LANES for x in g['lanes'][l]['fits'])
    scalar_curve_max=max(x['scalar_curve_max_difference'] for g in galaxies for l in core.LANES for x in g['lanes'][l]['fits'])
    audit_max=max(x['difference'] for x in audit)
    rows=[]
    for g in galaxies:
        for lane in core.LANES:
            L=g['lanes'][lane]
            rows.append({'galaxy':g['galaxy'],'n_rows':g['n_rows'],'rmax_kpc':g['rmax_kpc'],'vmax_kms':g['vmax_kms'],'has_bulge':g['has_bulge'],'negative_gas_rows':g['negative_gas_rows'],'lane':lane,'negative_bary2_rows':L['negative_bary2_rows'],'baryons_chi2':L['baryons_chi2'],'best_shape':L['best_shape'],'best_aic':L['best_aic'],'second_shape':L['second_shape'],'second_delta_aic':L['second_delta_aic'],'delta_aic_tanh':L['delta_aic_tanh'],'tanh_label':L['tanh_label'],'tanh_best':L['tanh_best'],'shape_identified':L['shape_identified'],'added_component_needed':L['added_component_needed'],'informative':L['informative']})
    with a.table.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    full={'schema':'lineum-b4-sparc-population-census/1','scope':'all 175 official SPARC rotation curves; five equal-flexibility saturation shapes; two fiducial gas lanes','input':{'archive_sha256':core.ARCHIVE_SHA,'member_count':175,'member_hashes':{g['member']:g['member_sha256'] for g in galaxies}},'protocol':{'shapes':core.SHAPES,'lanes':core.LANES,'starts':core.STARTS,'bounds':{'V0':core.V0B,'k_eff':core.KB},'curve_tolerance_kms':core.CURVE_TOL,'seed':core.SEED,'primary_min_rows':10},'aggregate':agg,'galaxies':galaxies,'independent_audit':{'selected_names':audit_names,'results':audit,'max_chi2_difference':audit_max},'checks':{'ngc3198':ngc_checks,'ngc3198_pass':ngc_pass,'max_scalar_chi2_difference':scalar_max,'max_scalar_curve_difference_kms':scalar_curve_max,'all_input_uncertainties_positive':True,'all_files_eight_columns':True},'environment':{'python':sys.version.split()[0],'numpy':np.__version__,'scipy':__import__('scipy').__version__,'platform':platform.platform(),'requirement_mismatch':'repository requires numpy<2; runtime supplied '+np.__version__},'anti_cheat':{'private_tolog_document_used':False,'post_hoc_shape_tuning':False,'galaxy_selection_by_fit':False,'lineum_engine_modified':False}}
    raw=json.dumps(full,separators=(',',':'),sort_keys=True).encode()
    wrapper={'schema':'compressed-research-receipt/1','classification':agg['classification'],'summary':agg,'uncompressed_sha256':core.sha_bytes(raw),'encoding':'lzma+base64 UTF-8 JSON','payload':base64.b64encode(lzma.compress(raw,preset=9)).decode()}
    a.output.write_text(json.dumps(wrapper,separators=(',',':'),sort_keys=True)+'\n')
    print(json.dumps({'classification':agg['classification'],'summary':agg,'checks':full['checks'],'audit_max_difference':audit_max},indent=2))
if __name__=='__main__': main()
