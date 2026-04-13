import os

files = [
    'whitepapers/2-cosmology/hypotheses/39-cosmo-hyp-four-forces-hadrons.md',
    'whitepapers/2-cosmology/hypotheses/40-cosmo-hyp-relativity-and-warp.md',
    'whitepapers/2-cosmology/hypotheses/41-cosmo-hyp-entanglement-teleportation.md',
    'whitepapers/3-ontology/hypotheses/21-ontology-hyp-macro-consciousness.md'
]

out_lines = []

for fpath in files:
    if not os.path.exists(fpath):
        out_lines.append(f'FILE NOT FOUND {fpath}')
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    first_80 = ''.join(lines[:80])
    
    orig_loc = [i+1 for i, L in enumerate(lines) if '## Original Extract' in L]
    interp_loc = [i+1 for i, L in enumerate(lines) if '## Interpretation' in L]
    
    txt = ''.join(lines)
    phi_count = txt.count('φ')
    mu_count = txt.count('μ')
    hypo_count = txt.lower().count('it is hypothesized')
    
    out_lines.append('=' * 60)
    out_lines.append(fpath)
    out_lines.append('=' * 60)
    out_lines.append('1) FIRST 80 LINES:')
    out_lines.append(first_80)
    out_lines.append('2) LOCATIONS:')
    out_lines.append(f'   - ## Original Extract (Verbatim): {orig_loc}')
    out_lines.append(f'   - ## Interpretation (Non-verbatim): {interp_loc}')
    out_lines.append('3) SEARCH RESULTS:')
    out_lines.append(f'   - count of "φ": {phi_count}')
    out_lines.append(f'   - count of "μ": {mu_count}')
    out_lines.append(f'   - count of "it is hypothesized": {hypo_count}')
    out_lines.append('\n')

with open('.agent/scratch/proof_output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))
