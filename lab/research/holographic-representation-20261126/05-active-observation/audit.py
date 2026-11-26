"""Independent metric and matched-pair audit using the saved arrays, not the solver."""
from pathlib import Path
import json, math
import numpy as np
P=Path(__file__).parent
r=json.loads((P/'results.json').read_text());d=np.load(P/'measurements.npz');k=d['conductivity'];fam=d['families'];tr=d['train'];labels=d['labels'];t=d['target'];x=d['front'];p=d['passive'];assert len(k)==192 and tr.sum()==96 and not np.any(p);assert np.array_equal(k[::2],k[1::2,::-1]);assert np.array_equal(k[:,0],np.ones_like(k[:,0]));assert np.array_equal(d['feature_passive'][::2],d['feature_passive'][1::2]);assert np.array_equal(d['feature_active'],d['feature_active_demeaned']);assert np.array_equal(t,d['second']-d['homogeneous']);
min_signal=min(max(abs(a-b).ravel()) for a,b in zip(x[::2],x[1::2]));assert min_signal>0 and abs(min_signal-r['reference']['minimum_active_pair_max_difference'])<1e-14
for arm in ('joint_shuffle','independent_shuffle'):
 assert np.array_equal(np.sort(d['feature_'+arm].reshape(192,5,64),axis=-1),np.sort(d['feature_active'].reshape(192,5,64),axis=-1))
err=0
for row in r['rows']:
 mask=(~tr)&((fam==row['family']) if row['family']!='all' else True);pred=d['prediction_'+row['arm']][mask];tt=t[mask].reshape(mask.sum(),64);score=pred[:,0];lab=labels[mask];acc=sum(.5 if abs(s)<1e-12 else float(s*l>0) for s,l in zip(score,lab))/len(score);dif=score[::2]-score[1::2];pa=sum(.5 if abs(s)<1e-12 else float(s>0) for s in dif)/len(dif);den=math.sqrt(float(np.sum(tt*tt)));rmse=math.sqrt(float(np.sum((tt-pred[:,1:])**2)))/den;mean=math.sqrt(float(np.sum((tt-t[tr].mean(0).ravel())**2)))/den
 for key,v in [('accuracy',acc),('paired_accuracy',pa),('nrmse',rmse),('train_mean_nrmse',mean)]:err=max(err,abs(v-row[key]))
 assert row['n']==mask.sum()
assert err<1e-12
out=dict(metric_values_verified=4*len(r['rows']),max_metric_error=err,passive_collision_pairs=96,active_distinct_pairs=96,exact_reflection=True,shuffle_histograms_preserved=True,repeat_json_identical=(P/'first.json').read_bytes()==(P/'results.json').read_bytes(),repeat_log_identical=(P/'run.log').read_bytes()==(P/'repeat.log').read_bytes())
assert out['repeat_json_identical'] and out['repeat_log_identical'];(P/'audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
