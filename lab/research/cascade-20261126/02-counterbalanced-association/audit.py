import json, math, statistics as st
from pathlib import Path
P=Path(__file__).parent
r=json.loads((P/'results.json').read_text()); n=0; maxerr=0
assert (P/'first.json').read_bytes()==(P/'results.json').read_bytes()
assert (P/'run.log').read_bytes()==(P/'repeat.log').read_bytes()
def check(x,y):
 global n,maxerr
 err=abs(x-y);maxerr=max(maxerr,err);n+=1;assert math.isclose(x,y,rel_tol=1e-10,abs_tol=1e-12),(x,y)
for h in r['training']:check(math.fsum(v for row in h['mu'] for v in row),h['mass'])
by={}
for t in r['trials']:
 assert len(t['rows'])==64
 b,c=(math.fsum(row[j] for row in t['rows']) for j in (0,1)); z=[math.sqrt(row[2]) for row in t['rows']]; q=[math.sqrt(row[3]/576) for row in t['rows']]
 x=(b-c)/max(b+c,1e-30);f=st.mean(z[-16:])/max(max(z),1e-30);quiet=st.mean(q[-16:]);check(x,t['contrast']);check(f,t['final_to_peak']);check(quiet,t['quiet_final_rms']);by.setdefault((t['seed'],t['mode']),[]).append(((-1)**(t['history']+t['cue'])*x,f,quiet))
for s in r['scores']:
 a=by[(s['seed'],s['mode'])];assert len(a)==4
 for j,k in enumerate(('association','final_to_peak','quiet_final_rms')):check(st.mean(v[j] for v in a),s[k])
for m,v in r['summary'].items():
 a=[s for s in r['scores'] if s['mode']==m];check(st.median(s['association'] for s in a),v['median_association']);check(st.median(s['final_to_peak'] for s in a),v['median_final_to_peak']);assert sum(s['association']>0 for s in a)==v['positive_seeds']
a={m:{s['seed']:s['association'] for s in r['scores'] if s['mode']==m} for m in r['summary']}
for m in ('shuffled','uniform'):check(st.median(a['learned'][k]-a[m][k] for k in a['learned']),r['learned_minus_'+m])
assert r['gate_pass']==(r['summary']['learned']['positive_seeds']>=7 and r['summary']['learned']['median_association']>=.05 and r['learned_minus_shuffled']>=.05 and r['learned_minus_uniform']>=.05)
assert max(abs(v) for v in a['zero'].values())<1e-15
out={'aggregation_checks':n,'max_absolute_residual':maxerr,'exact_repeat':True,'association_gate':r['gate_pass'],'training_histories':len(r['training']),'test_pairs':len(r['trials']),'observed_tick_rows':sum(len(t['rows']) for t in r['trials']),'zero_control_roundoff_max':max(abs(v) for v in a['zero'].values())}
(P/'audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
