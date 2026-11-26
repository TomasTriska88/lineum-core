import json,math,hashlib,statistics,zipfile,base64
from pathlib import Path
P=Path(__file__).parent
r=json.loads((P/'results.json').read_text()); assert len(r['cases'])==40 and len(r['training'])==8
assert (P/'first.json').read_bytes()==(P/'results.json').read_bytes() and (P/'run.log').read_bytes()==(P/'repeat.log').read_bytes()
assert len({(c['mode'],c['seed']) for c in r['cases']})==40
checks=0; residual=0.; recomputed={}; gate=0; positive=0
for c in r['cases']:
 rows=c['rows']; assert len(rows)==96 and all(len(row)==11 and all(math.isfinite(x) and x>=0 for x in row) for row in rows)
 p=sum(row[0] for row in rows); n=sum(row[1] for row in rows); assert p==sum(map(sum,c['positive_gate_counts'])) and n==sum(map(sum,c['negative_gate_counts']))
 assert all((first>=0)==(count>0) and -1<=first<96 for fr,cs in zip(c['first_positive_remote_gate'],c['positive_gate_counts']) for first,count in zip(fr,cs))
 F=math.fsum(row[5] for row in rows); A=math.fsum(row[6] for row in rows)
 v={'remote_extra':p,'remote_suppressed':n,'max_components':max(row[2] for row in rows),'max_remote_peaks':max(row[3] for row in rows),'remote_integral':F,'ablation_remote_integral':A,'relative_causal_effect':(F-A)/max(F,1e-30),'excess_final_to_peak':statistics.mean(math.sqrt(row[4]) for row in rows[-16:])/math.sqrt(max(row[4] for row in rows)),'baseline_final_rms':statistics.mean(math.sqrt(row[7]/576) for row in rows[-16:]),'mu_difference_final':rows[-1][8],'near_history_integral':math.fsum(row[9] for row in rows),'opposite_history_integral':math.fsum(row[10] for row in rows)}
 for k,val in v.items():
  error=abs(val-c['summary'][k]);residual=max(residual,error);assert math.isclose(val,c['summary'][k],rel_tol=1e-12,abs_tol=1e-12);checks+=1
 recomputed.setdefault(c['mode'],[]).append(v)
 if c['mode']=='learned':
  gate+=p>0 and v['max_components']>=2 and v['relative_causal_effect']>0
  positive+=v['relative_causal_effect']>0
for m,cs in recomputed.items():
 for k in cs[0]:
  v=statistics.median(c[k] for c in cs);assert math.isclose(v,r['summary'][m][k],rel_tol=1e-12,abs_tol=1e-12);checks+=1
assert gate==r['gate_count'] and r['gate_pass']==(gate>=6 and r['summary']['learned']['relative_causal_effect']>0)
print(json.dumps({'cases':len(r['cases']),'native_test_trajectories':120,'training_trajectories':8,'per_tick_measured_rows':3840,'recomputed_metrics':checks,'max_absolute_residual':residual,'gate_count':gate,'gate_pass':r['gate_pass'],'learned_positive_causal_cases':positive,'deterministic_repeat_byte_equal':True},indent=2))
