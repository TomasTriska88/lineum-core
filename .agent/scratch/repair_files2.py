import os, re
with open('todo_head.md', 'r', encoding='utf-16') as f:
    todo_lines = f.readlines()

blocks = {
    '39': {
        'start': '- [ ] **[HYPOTHESIS: Emergence',
        'end': '         - **[HYPOTHESIS] Relativity in Lineum',
        # But wait, 39 ended at Relativity. In the array, let's grab the actual string:
        'file': 'whitepapers/2-cosmology/hypotheses/39-cosmo-hyp-four-forces-hadrons.md'
    },
    '40': {
        'start': '         - **[HYPOTHESIS] Relativity in Lineum',
        'end': '         - **[HYPOTHESIS] Quantum Entanglement',
        'file': 'whitepapers/2-cosmology/hypotheses/40-cosmo-hyp-relativity-and-warp.md'
    },
    '41': {
        'start': '         - **[HYPOTHESIS] Quantum Entanglement',
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
    orig_str = ''.join(orig_lines)
    
    fpath = b['file']
    if not os.path.exists(fpath): continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip frontmatter
    # Find second ---
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
    
    # Also strip original if we already pasted it
    # Just take everything after Interpretation as the current rewritten content.
    rest = rest.strip()
    
    new_doc = fm + '\n\n' + doc_id + '\n\n' + orig_str + '\n\n## Interpretation (Non-verbatim)\n\n' + rest + '\n'
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
        
    print(f"[{fpath}] MODIFIED -> FIXED")

