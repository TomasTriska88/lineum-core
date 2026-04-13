import os

files = [
    'whitepapers/2-cosmology/hypotheses/39-cosmo-hyp-four-forces-hadrons.md',
    'whitepapers/2-cosmology/hypotheses/40-cosmo-hyp-relativity-and-warp.md',
    'whitepapers/2-cosmology/hypotheses/41-cosmo-hyp-entanglement-teleportation.md',
    'whitepapers/3-ontology/hypotheses/21-ontology-hyp-macro-consciousness.md'
]

out = []

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    out.append('════════════════════════════════════════════')
    out.append(f'FILE: {os.path.basename(f)}')
    out.append('════════════════════════════════════════════')
    
    out.append('1) FIRST 80 LINES OF FILE:')
    # join and ensure trailing newline
    eighto = ''.join(lines[:80])
    if not eighto.endswith('\n'): eighto += '\n'
    out.append(eighto)
    
    orig_loc = -1
    interp_loc = -1
    for i, l in enumerate(lines):
        if '## Original Extract' in l: orig_loc = i + 1
        if '## Interpretation' in l: interp_loc = i + 1
        
    out.append('2) LOCATION OF:')
    out.append(f'   - ## Original Extract (Verbatim): {"Line " + str(orig_loc) if orig_loc != -1 else "NOT FOUND"}')
    out.append(f'   - ## Interpretation (Non-verbatim): {"Line " + str(interp_loc) if interp_loc != -1 else "NOT FOUND"}')
    
    txt = ''.join(lines)
    phi_c = txt.count('φ') + txt.count('\\varphi')
    mu_c = txt.count('μ') + txt.count('\\mu')
    hypo_c = txt.lower().count('it is hypothesized')
    
    out.append('3) SEARCH RESULTS:')
    out.append(f'   - count of "φ" (including \\varphi): {phi_c}')
    out.append(f'   - count of "μ" (including \\mu): {mu_c}')
    out.append(f'   - count of "it is hypothesized": {hypo_c}')
    out.append('\n')

with open('.agent/scratch/proof_final.txt', 'w', encoding='utf-8') as out_f:
    out_f.write('\n'.join(out))
