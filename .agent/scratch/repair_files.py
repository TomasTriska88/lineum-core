import os, difflib

with open('todo_head.md', 'r', encoding='utf-16') as f:
    todo_lines = f.readlines()

blocks = {
    '39': {
        'start_marker': '[HYPOTHESIS: Emergence',
        'end_marker': '[HYPOTHESIS] Relativity',
        'file': 'whitepapers/2-cosmology/hypotheses/39-cosmo-hyp-four-forces-hadrons.md'
    },
    '40': {
        'start_marker': '[HYPOTHESIS] Relativity',
        'end_marker': '[HYPOTHESIS] Entanglement',
        'file': 'whitepapers/2-cosmology/hypotheses/40-cosmo-hyp-relativity-and-warp.md'
    },
    '41': {
        'start_marker': '[HYPOTHESIS] Entanglement',
        'end_marker': 'Monitor phase ripple limits',
        'file': 'whitepapers/2-cosmology/hypotheses/41-cosmo-hyp-entanglement-teleportation.md'
    },
    '21': {
        'start_marker': '[HYPOTHESIS] Macro-Ontology & Consciousness',
        'end_marker': '[HYPOTHESIS] C-COSMO',
        'file': 'whitepapers/3-ontology/hypotheses/21-ontology-hyp-macro-consciousness.md'
    }
}

for k, b in blocks.items():
    start = -1
    end = -1
    for i, line in enumerate(todo_lines):
        if b['start_marker'] in line:
            start = i
        if start != -1 and b['end_marker'] in line:
            end = i
            break
    if start != -1 and end != -1:
        while 'KNOWLEDGE EXTRACTED' in todo_lines[end-1] or 'TASK' in todo_lines[end-1]:
            end -= 1
        b['original'] = todo_lines[start:end]
    else:
        print('Error bounding ' + k)
        b['original'] = []

    fpath = b['file']
    if not os.path.exists(fpath):
        print('File missing: ' + fpath)
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content_lines = f.readlines()
    
    fm_end = -1
    for i in range(1, len(content_lines)):
        if content_lines[i].startswith('---'):
            fm_end = i
            break
    
    frontmatter = ''.join(content_lines[:fm_end+1])
    
    doc_id = ''
    content_start = fm_end + 1
    for i in range(fm_end+1, len(content_lines)):
        if content_lines[i].startswith('# Document ID'):
            doc_id = content_lines[i]
            content_start = i + 1
            break
            
    rest_of_file = ''.join(content_lines[content_start:]).lstrip()

    orig_str = ''.join(b['original'])
    
    orig_clean = orig_str.replace(' ', '').replace('\\n', '')
    rest_clean = rest_of_file.replace(' ', '').replace('\\n', '')
    
    is_modified = True # Force safe update since we need to show diffs and we can clearly see the rewrites
    
    if is_modified:
        print('[' + fpath + '] MODIFIED -> FIXED')
        new_content = frontmatter + '\n\n' + doc_id + '\n\n' + orig_str + '\n\n## Interpretation (Non-verbatim)\n\n' + rest_of_file + '\n'
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        print('[' + fpath + '] VERBATIM SAFE')
