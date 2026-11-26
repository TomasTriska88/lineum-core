from pathlib import Path
import hashlib,json,math
import numpy as np
P=Path(__file__).parent
r=json.loads((P/'results.json').read_text());d=np.load(P/'measurements.npz');k=d['conductivity'];fam=d['families'];tr=d['train'];labels=d['labels'];t=d['target'];assert len(k)==160 and tr.sum()==80;assert np.array_equal(k[::2],k[1::2,::-1]);assert np.array_equal(t,d['second']-d['homogeneous']);
a=d['action_adaptive'];y=d['action_yoked'];fixed=d['action_fixed'];assert np.array_equal(a,d['scores'].argmax(1));assert np.all(fixed==0);assert np.max(abs(d['patterns'].sum((1,2))-1))<1e-14;assert abs(d['center'].sum()-1)<1e-14
for f in np.unique(fam):
 ix=fam==f;assert np.array_equal(np.bincount(a[ix],minlength=4),np.bincount(y[ix],minlength=4));assert np.array_equal(y[ix],np.roll(a[ix],2))
for arm in ('fixed','yoked'):
 assert np.array_equal(d['history_'+arm][:,:32],d['history_adaptive'][:,:32]);assert np.allclose((d['history_'+arm][:,32]-d['history_adaptive'][:,32]),d['patterns'][d['action_'+arm]]-d['patterns'][a],rtol=0,atol=1e-15)
assert r['reference']['changed_pair_actions']==np.count_nonzero(a[::2]!=a[1::2]);assert r['reference']['yoked_action_diff']==np.count_nonzero(a!=y)
err=0
for row in r['rows']:
 mask=(~tr)&((fam==row['family']) if row['family']!='all' else True);pred=d['prediction_'+row['arm']][mask];tt=t[mask].reshape(mask.sum(),64);score=pred[:,0];lab=labels[mask];acc=sum(.5 if abs(s)<1e-12 else float(s*l>0) for s,l in zip(score,lab))/len(score);dif=score[::2]-score[1::2];pa=sum(.5 if abs(s)<1e-12 else float(s>0) for s in dif)/len(dif);den=math.sqrt(float(np.sum(tt*tt)));rmse=math.sqrt(float(np.sum((tt-pred[:,1:])**2)))/den;mean=math.sqrt(float(np.sum((tt-t[tr].mean(0).ravel())**2)))/den
 for key,v in [('accuracy',acc),('paired_accuracy',pa),('nrmse',rmse),('train_mean_nrmse',mean)]:err=max(err,abs(v-row[key]))
 assert row['n']==mask.sum();assert d['feature_'+row['arm']].reshape(160,-1).shape[1]==320
assert err<1e-12;assert r['reference']['max_mass_residual']<1e-12
out=dict(metric_values_verified=4*len(r['rows']),max_metric_error=err,exact_reflection=True,matched_source_mass=True,yoked_action_counts_preserved=True,pre_action_history_identical=True,repeat_json_identical=(P/'first.json').read_bytes()==(P/'results.json').read_bytes(),repeat_measurement_hash_identical=hashlib.sha256((P/'measurements.npz').read_bytes()).hexdigest()==(P/'first_measurements.sha256').read_text().split()[0],repeat_log_identical=(P/'run.log').read_bytes()==(P/'repeat.log').read_bytes());assert all(out[x] for x in ('repeat_json_identical','repeat_measurement_hash_identical','repeat_log_identical'));(P/'audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
