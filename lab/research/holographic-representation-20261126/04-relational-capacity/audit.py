"""Independent saved-output metrics and collision audit."""
import json, math, hashlib
from pathlib import Path
import numpy as np
p=Path(__file__).parent; r=json.loads((p/'results.json').read_text()); z=np.load(p/'measurements.npz'); errors=[]
for row in r['rows']:
 ix=~z['train'];
 if row['family']!='all':ix=ix&(z['families']==row['family'])
 target=z['target'][ix]; pred=z['prediction_'+row['arm']+'_'+row['kind']][ix]
 if pred.ndim==1:target=target.mean((1,2))
 ratio=math.sqrt(float(np.sum((pred-target)**2))/float(np.sum(target**2))); pm=pred.reshape(len(pred),-1).mean(1);tm=target.reshape(len(target),-1).mean(1); accuracy=sum(.5 if abs(a)<1e-12 else int(a*b>0) for a,b in zip(pm,tm))/len(pm)
 errors.extend([abs(ratio-row['nrmse']),abs(accuracy-row['accuracy'])])
assert max(errors)<1e-12
assert np.array_equal(z['collision_hist_a'],z['collision_hist_b']);assert np.array_equal(z['constant_a'],z['constant_b']);assert np.min(np.sqrt(np.mean((z['collision_target_a']-z['collision_target_b'])**2,axis=(1,2))))>1
for arm in ['joint','independent']:
 assert np.array_equal(np.sort(z['feature_'+arm].reshape(-1,5,64),axis=2),np.sort(z['feature_native'].reshape(-1,5,64),axis=2))
a={'metric_rows':len(r['rows']),'max_metric_error':max(errors),'collision_pairs_exact':32,'repeat_json_equal':(p/'first.json').read_bytes()==(p/'results.json').read_bytes(),'repeat_log_equal':(p/'run.log').read_bytes()==(p/'repeat.log').read_bytes(),'marginal_preservation':True};(p/'audit.json').write_text(json.dumps(a,indent=2)+'\n');print(a)
