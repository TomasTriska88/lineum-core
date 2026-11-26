"""Independent checks of the stored summaries, not a second solver."""
import json, math, hashlib
from pathlib import Path
from statistics import median
p=Path(__file__).parent
checks=0;worst=0.;out={}
def test(ok):
 global checks
 assert ok
 checks+=1

def same(a,b):
 global worst
 worst=max(worst,abs(a-b));test(math.isclose(a,b,abs_tol=1e-8,rel_tol=1e-11))
for label,file,first,log,rep,protocol,expected in [('native','result.json','first.json','run.log','repeat.log','protocol.md',81),('ablation','ablation.json','ablation_first.json','ablation.log','ablation_repeat.log','ablation_protocol.md',54),('attractor','attractor.json','attractor_first.json','attractor.log','attractor_repeat.log','attractor_protocol.md',12)]:
 r=json.loads((p/file).read_text());test(len(r['cases'])==expected);test((p/file).read_bytes()==(p/first).read_bytes());test((p/log).read_bytes()==(p/rep).read_bytes());test(hashlib.sha256((p/protocol).read_bytes()).hexdigest()==r['protocol_sha256']);res=[]
 for c in r['cases']:
  if label!='attractor':
   test(len(c['lanes'])==2);test(len(c['distance_checkpoints'])==9);test(all(-1e-12<=d<=1+1e-12 for d in c['distance_checkpoints']));test(c['kick_distance']>0);test(max(abs(x) for x in c['distance_checkpoints'][:3])<1e-12)
   ls=c['lanes'];budget=c.get('budget',.02)*128;recovered=c['distance_checkpoints'][6]<=c['kick_distance']/2
  else:ls=[c];budget=.1*512;recovered=None
  for l in ls:
   test(len(l['checkpoints'])==len(r['checkpoints']));test(len(l['window'])==len(r['windows']));same(l['source_sums'][0],0 if c['mode']=='quiet' else budget);test(l['source_sums'][1]>=0 and l['source_sums'][3]>=-1e-12)
   if c['mode']!='adaptive':same(l['source_sums'][3],0)
   for row in l['checkpoints']:
    test(all(math.isfinite(x) for x in row));test(row[0]>=0 and row[6]>=0);test(all(-1e-12<=row[i]<=1+1e-12 for i in [1,2,4,5]));test(abs(row[3])<=1+1e-12);test(abs(row[7])<=math.pi+1e-12)
    if label=='attractor':test(0<=row[8]<=1 and row[2]+row[8]<=1+1e-12 and row[9]>=0)
   means=[]
   for w,(a,b) in zip(l['window'],r['windows']):
    n=b-a+1;test(w['count']==n);test(len(w['sums'])==7);z=[v/n for v in w['sums']];test(all(math.isfinite(x) for x in z));test(z[0]>=0 and z[6]>=0);test(all(-1e-12<=z[i]<=1+1e-12 for i in [1,2,4,5]));test(abs(z[3])<=1+1e-12);test(0<=w['valid_m3']<=n);test(0<=w['orientation_steps']<=max(0,w['valid_m3']-1));test(abs(w['orientation_signed'])<=w['orientation_absolute']+1e-12);test(w['orientation_absolute']<=w['orientation_steps']*math.pi/3+1e-12)
    if label=='attractor':test(0<=w['minus_sum']<=n and z[2]+w['minus_sum']/n<=1+1e-12)
    means.append(z)
   late=means[1] if label!='attractor' else means[0]
   if recovered is not None:
    late_gate=late[2]>=.9 and late[1]>=.5 and late[4]>=.1 and late[5]>=.95 and recovered
    gate=late_gate and means[-1][2]>=.5;test(l['gate']==gate)
    if 'late_gate' in l:test(l['late_gate']==late_gate)
   res.append({'mode':c['mode'],'material':c.get('material'),'budget':c.get('budget'),'shape':c.get('shape'),'late':late,'post':means[-1],'orientation':l['window'][1 if label!='attractor' else 0]['orientation_signed'],'gate':l.get('gate'),'source':l['source_sums']})
 if label=='attractor':
  test(len(r['pairs'])==6)
  for group in r['pairs']:
   test(len(group['pairs'])==6);test(len(set((a['a'],a['b']) for a in group['pairs']))==6);test(all(0<=a['overlap']<=1+1e-12 for a in group['pairs']))
  # Verify that the stated common-attraction gate cannot pass: all four
  # driven endpoints have neither common winding sign nor m3>=.1.
  for mode in ('quiet','ring','aligned'):
   cs=[c for c in r['cases'] if c['mode']==mode];ps=[x for x in r['pairs'] if x['mode']==mode and x['tick']==511][0]
   e=[c['checkpoints'][5] for c in cs];gate=min(x['overlap'] for x in ps['pairs'])>=.9 and all(a[0]>=r['E0']/2 and a[4]>=.1 for a in e) and (all(a[2]>=.9 for a in e) or all(a[8]>=.9 for a in e));test(not gate)
 out[label]={'cases':len(r['cases']),'trajectories':len(res),'gates':sum(x['gate'] is True for x in res),'repeat_exact':True}
out['checks']=checks;out['max_budget_residual']=worst
(p/'audit.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2))
