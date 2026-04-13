import os, re
import subprocess

# 1. First commit current state so we can get clean diff
subprocess.run(['git', 'add', 'whitepapers/2-cosmology/hypotheses/*.md'])
subprocess.run(['git', 'add', 'whitepapers/3-ontology/hypotheses/*.md'])
subprocess.run(['git', 'commit', '-m', 'temp commit for clean output diff'])

# 2. Extract verbatim blocks from todo_head.md
with open('todo_head.md', 'r', encoding='utf-16') as f:
    todo_lines = f.readlines()

blocks = {
    '39': {
        'start': '- [ ] **[HYPOTHESIS: Emergence of the 4 Fundamental',
        'end': '         - **[HYPOTHESIS] The Speed of Light ($c$) & Photon Ontology:',
        'file': 'whitepapers/2-cosmology/hypotheses/39-cosmo-hyp-four-forces-hadrons.md'
    },
    '40': {
        'start': '         - **[HYPOTHESIS] The Speed of Light ($c$) & Photon Ontology:',
        'end': '         - **[HYPOTHESIS] Quantum Entanglement (The "Mandela',
        'file': 'whitepapers/2-cosmology/hypotheses/40-cosmo-hyp-relativity-and-warp.md'
    },
    '41': {
        'start': '         - **[HYPOTHESIS] Quantum Entanglement (The "Mandela',
        'end': '         - **[HYPOTHESIS] Macro-Ontology & Consciousness',
        'file': 'whitepapers/2-cosmology/hypotheses/41-cosmo-hyp-entanglement-teleportation.md'
    },
    '21': {
        'start': '         - **[HYPOTHESIS] Macro-Ontology & Consciousness',
        'end': '            - **[HYPOTHESIS] C-COSMO: The Multiverse',
        'file': 'whitepapers/3-ontology/hypotheses/21-ontology-hyp-macro-consciousness.md'
    }
}

for k, b in blocks.items():
    s_idx = -1
    e_idx = -1
    for i, line in enumerate(todo_lines):
        if b['start'] in line and s_idx == -1: s_idx = i
        if b['end'] in line and s_idx != -1 and e_idx == -1: e_idx = i
    
    if s_idx == -1 or e_idx == -1:
        print(f"Error bounds for {k}. {s_idx} to {e_idx}")
        continue
    
    orig_lines = todo_lines[s_idx:e_idx]
    orig_str = ''.join(orig_lines).rstrip() + '\n'
    
    fpath = b['file']
    if not os.path.exists(fpath): continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip frontmatter
    parts = content.split('---')
    if len(parts) >= 3:
        fm = '---' + parts[1] + '---'
        rest = '---'.join(parts[2:])
    else:
        fm = ''
        rest = content
        
    doc_id = ''
    rest_lines = rest.strip().split('\n')
    if rest_lines and '# Document ID:' in rest_lines[0]:
        doc_id = rest_lines[0]
        rest = '\n'.join(rest_lines[1:])
    
    # If we already added '## Interpretation', split by it to get the rewritten version.
    if '## Interpretation' in rest:
        rest = rest.split('## Interpretation')[-1]
    elif '## Original Extract' in rest:
        rest = rest.split('## Original Extract')[-1]
            
    rest = rest.strip()
    # Strip any leading (Non-verbatim) or headers from the rest that were leftover
    rest_clean_lines = []
    skip = True
    for l in rest.split('\n'):
        if skip and (l.strip() == '(Non-verbatim)' or l.strip() == '' or l.startswith('# ')):
            pass
        else:
            skip = False
            rest_clean_lines.append(l)
    
    rest = '\n'.join(rest_clean_lines).strip()
    
    new_doc = fm + '\n\n' + doc_id + '\n\n## Original Extract (Verbatim)\n\n' + orig_str + '\n## Interpretation (Non-verbatim)\n\n' + rest + '\n'
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
        
    print(f"[{fpath}] REWRITTEN")

# We will just print the diff and output it.
# Subprocess to get diffs
subprocess.run(['git', 'diff', 'HEAD'], stdout=open('.agent/scratch/final_diff.diff', 'w', encoding='utf-8'))
