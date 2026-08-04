#!/usr/bin/env python3
import argparse, json, sys, zipfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import lineum_b4_sparc_population_shape_census as core

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--archive',type=Path,required=True); ap.add_argument('--start',type=int,required=True); ap.add_argument('--end',type=int,required=True); ap.add_argument('--output',type=Path,required=True); ap.add_argument('--workers',type=int,default=5); a=ap.parse_args()
    payload=a.archive.read_bytes(); assert core.sha_bytes(payload)==core.ARCHIVE_SHA
    with zipfile.ZipFile(a.archive) as z:
        names=sorted(n for n in z.namelist() if n.endswith('_rotmod.dat'))
        tasks=[(n,z.read(n)) for n in names[a.start:a.end]]
    galaxies=[]
    with ProcessPoolExecutor(max_workers=a.workers) as ex:
        fs={ex.submit(core.process_galaxy,t):t[0] for t in tasks}
        for f in as_completed(fs): galaxies.append(f.result())
    galaxies.sort(key=lambda g:g['galaxy'])
    a.output.write_text(json.dumps({'start':a.start,'end':a.end,'galaxies':galaxies},separators=(',',':'),sort_keys=True)+'\n')
    print(json.dumps({'start':a.start,'end':a.end,'count':len(galaxies)}))
if __name__=='__main__': main()
