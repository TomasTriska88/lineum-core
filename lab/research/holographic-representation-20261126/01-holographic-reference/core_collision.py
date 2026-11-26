"""Exact whitespace-normalized CPU Core excerpt, mirrored 3D initial-data collision."""
import json, hashlib, time
from pathlib import Path
import numpy as np
from core_numpy_excerpt import CoreConfig, _step_numpy
source=Path(__file__).with_name('core_numpy_excerpt.py').read_text()
normalized='\n'.join(l.rstrip() for l in source[source.index('@dataclass(frozen=True)'):].splitlines()).rstrip()
h=2166136261
for c in normalized:h=((h^ord(c))*16777619)&0xffffffff
assert h==0x56103725
rng=np.random.default_rng(20261127)
rows=[]
for case in range(16):
    # All four fields (five real components) have independent dyadic values.
    v=rng.integers(1,65,size=(5,9,8,8)).astype(float)/256
    v[3]=.5+v[3] # kappa in [.5, .75]
    mirror=v[:,::-1].copy()
    a=v.mean(axis=1); b=mirror.mean(axis=1)
    assert np.array_equal(a,b) and not np.array_equal(v,mirror)
    def state(p):return {'psi':p[0].copy()+1j*p[1].copy(),'phi':p[2].copy(),'kappa':p[3].copy(),'mu':p[4].copy()}
    def run(p,seed,cfg):
        np.random.seed(seed);s=state(p);out=[]
        for _ in range(64):
            s=_step_numpy(s,cfg)
            assert all(np.isfinite(x).all() for x in s.values())
            out.append(np.stack([s['psi'].real,s['psi'].imag,s['phi'],s['kappa'],s['mu']]))
        return np.array(out)
    for use_mu in [False,True]:
        cfg=CoreConfig(use_mu=use_mu)
        x=run(a,case,cfg); y=run(b,case,cfg)
        alt=run(v[:,0],case,cfg)
        random_control=run(b,case+1000,cfg)
        rows.append(dict(case=case,use_mu=use_mu,initial_3d_rms=float(np.sqrt(np.mean((v-mirror)**2))),projection_collision_exact=bool(np.array_equal(a,b)),core_all_steps_collision_exact=bool(np.array_equal(x,y)),core_collision_max_abs=float(np.max(abs(x-y))),distinct_front_control_max_abs=float(np.max(abs(x-alt))),different_seed_control_max_abs=float(np.max(abs(x-random_control)))))
        assert rows[-1]['core_all_steps_collision_exact'] and rows[-1]['distinct_front_control_max_abs']>0 and rows[-1]['different_seed_control_max_abs']>0
result=dict(source_commit='8c4ff12af79b218fce8938497f56f75c4567195e',source_blob='d59db92efa9dc5efeffc58bafc8a0361767b144e',normalized_excerpt_fnv1a=f'{h:08x}',local_excerpt_sha256=hashlib.sha256(source.encode()).hexdigest(),rows=rows,scope='CPU _step_numpy excerpt, default LAP4 config with use_mu false/true; synthetic mirrored initial states only; no claim of 3D Core or whole-Core audit',all_pass=True)
Path(__file__).with_name('core_collision_results.json').write_text(json.dumps(result,indent=2)+'\n')
print('Core collisions:',sum(r['core_all_steps_collision_exact'] for r in rows),'/',len(rows),'pairs, each 64 steps')
print('3D RMS range',min(r['initial_3d_rms'] for r in rows),max(r['initial_3d_rms'] for r in rows))
print('positive front min',min(r['distinct_front_control_max_abs'] for r in rows),'different seed min',min(r['different_seed_control_max_abs'] for r in rows))
