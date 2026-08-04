#!/usr/bin/env python3
import csv, json, statistics, sys
from collections import Counter
from pathlib import Path

p=Path(sys.argv[1])
rows=list(csv.DictReader(p.open()))
assert len(rows)==350
lanes=('unsigned_fiducial','signed_fiducial')
out={'lanes':{},'joint':{}}
by={(r['galaxy'],r['lane']):r for r in rows}
for lane in lanes:
    info=[r for r in rows if r['lane']==lane and r['informative']=='True']
    labels=[r['tanh_label'] for r in info]
    deltas=[float(r['delta_aic_tanh']) for r in info]
    out['lanes'][lane]={
      'informative_count':len(info),
      'compatible_count':labels.count('compatible'),
      'strong_rejected_count':labels.count('strongly_rejected'),
      'median_delta_aic_tanh':statistics.median(deltas),
      'tanh_best_count':sum(r['tanh_best']=='True' for r in info),
      'winner_counts':dict(Counter(r['best_shape'] for r in info)),
      'shape_identified_count':sum(r['shape_identified']=='True' for r in info),
    }
names=sorted({r['galaxy'] for r in rows})
both=[n for n in names if all(by[(n,l)]['informative']=='True' for l in lanes)]
out['joint']={
 'informative_both_count':len(both),
 'same_label_count':sum(by[(n,lanes[0])]['tanh_label']==by[(n,lanes[1])]['tanh_label'] for n in both),
 'same_winner_count':sum(by[(n,lanes[0])]['best_shape']==by[(n,lanes[1])]['best_shape'] for n in both),
}
assert out['lanes']['unsigned_fiducial']['informative_count']==102
assert out['lanes']['unsigned_fiducial']['compatible_count']==82
assert out['lanes']['unsigned_fiducial']['strong_rejected_count']==14
assert out['lanes']['unsigned_fiducial']['tanh_best_count']==68
assert out['lanes']['unsigned_fiducial']['shape_identified_count']==32
assert out['lanes']['unsigned_fiducial']['winner_counts']=={'tanh':68,'rational':16,'algebraic':10,'arctan':5,'exponential':3}
assert out['lanes']['signed_fiducial']==out['lanes']['unsigned_fiducial']
assert out['joint']=={'informative_both_count':102,'same_label_count':102,'same_winner_count':102}
print(json.dumps(out,indent=2,sort_keys=True))
