import os
import re

todo_path = r'C:\Users\Tomáš\Documents\GitHub\lineum-core\todo.md'
output_dir = r'C:\Users\Tomáš\Documents\GitHub\lineum-core\whitepapers'

with open(todo_path, 'r', encoding='utf-8') as f:
    todo_lines = f.readlines()

# Define the sections by starting headers
sections = [
    ("## 🧱 Priority 0 - Basic principles and critical points\n", None),
    ("### 🔲 A. Basic invariances and \"first principles\" #structure", r"3-theory\06-theory-fundamental-invariants.md"),
    ("### 🔲 B. Numerical robustness and artifacts #numerics", r"2-experiments\09-exp-numerical-robustness.md"),
    ("### 🔲 C. Dimensions, units, and SI anchoring #units", r"3-theory\07-theory-emergent-scale.md"),
    ("### 🔲 D. Statistical power, errors and uncertainties #stats", r"2-experiments\10-exp-statistical-baseline.md"),
    ("### 🔲 E. Null models and baseline comparison #nulltests", r"2-experiments\11-exp-null-models.md"),
    ("### 🔲 F. Reproducibility and independent verification #repro", r"5-applications\05-app-reproduction-pipeline.md"),
    ("### 🔲 G. Implementation details and stability against \"engineering\" choices #impl", r"5-applications\06-app-implementation-details.md"),
    ("### 🔲 H. The role of κ and parametric space #structure", r"2-experiments\12-exp-kappa-parametric-sweeps.md"),
    ("### 🔲 I. Limit transitions and scaling #test", r"3-theory\09-theory-limit-transitions.md"),
    ("### 🔲 J. Criteria for \"physical\" interpretation #meta", r"1-core\04-core-interpretation-criteria.md"),
    ("### 🔲 K. Bridge to empirics and \"anti-numerology\" #empirics", r"2-experiments\13-exp-empirical-bridge.md"),
    ("### 🔲 L. Falsifiability and \"promotion pipeline\" #meta", r"1-core\05-core-falsifiability.md"),
    ("### 🔲 M. Terminology and Naming Conventions #meta", r"1-core\06-core-terminology.md"),
    ("### 🔲 N. Presentation and communication of results #meta", r"5-applications\07-app-communication.md"),
    ("## 🧪 Priority: Highest – exploring _effective_ mapping to real physics", None),
    ("### 🔲 1. Dark matter and dark energy #hypothesis", r"4-ontology-cosmology\11-cosmo-dark-sector.md"),
    ("### 🔲 2. Validation of known particles and quantum properties #hypothesis", r"2-experiments\14-exp-particle-validation.md"),
    ("### 🔲 3. Electromagnetism and fields #hypothesis", r"4-ontology-cosmology\12-cosmo-electromagnetism.md"),
    ("### 🔲 4. Weak and strong interaction #hypothesis", r"4-ontology-cosmology\13-cosmo-weak-strong.md"),
    ("## 🌌 C. Eq-8 Emergent Cosmology Simulator", r"4-ontology-cosmology\14-cosmo-eq8-simulator.md")
]

# Extract blocks
current_section_idx = -1
extracted_blocks = {}
remaining_todo = []

i = 0
while i < len(todo_lines):
    line = todo_lines[i]
    matched = False
    for idx, (header, target) in enumerate(sections):
        if line.startswith(header):
            current_section_idx = idx
            matched = True
            break
    
    if matched:
        if sections[current_section_idx][1] is not None:
            extracted_blocks[current_section_idx] = [line]
        else:
            remaining_todo.append(line)
            current_section_idx = -1
    else:
        if current_section_idx != -1 and sections[current_section_idx][1] is not None:
            extracted_blocks[current_section_idx].append(line)
        else:
            remaining_todo.append(line)
    i += 1

import difflib

# 1. Update todo.md
todo_diff = list(difflib.unified_diff(
    todo_lines, 
    remaining_todo, 
    fromfile=r"c:\Users\Tomáš\Documents\GitHub\lineum-core\todo.md", 
    tofile=r"c:\Users\Tomáš\Documents\GitHub\lineum-core\todo.md"
))

# 2. Extract specific files
diffs = []
diffs.append("".join(todo_diff))

for idx, lines in extracted_blocks.items():
    target_rel = sections[idx][1]
    target_abs = os.path.join(output_dir, target_rel)
    os.makedirs(os.path.dirname(target_abs), exist_ok=True)
    
    header_content = f"# {target_rel.split(os.sep)[-1].replace('.md', '')}\n\n> **[DRAFT]** Migrated from canonical todo.md for consolidation.\n\n"
    
    new_content = [header_content] + lines
    
    diff = list(difflib.unified_diff(
        [], 
        new_content, 
        fromfile=target_abs.replace(os.sep, '/'), 
        tofile=target_abs.replace(os.sep, '/'),
        n=0
    ))
    diff_fixed = [f"--- /dev/null\n+++ {target_abs.replace(os.sep, '/')}\n@@ -0,0 +1,{len(new_content)} @@\n"] + [("+" + l) if not l.startswith("+") else "+"+l for l in new_content]
    diffs.append("".join(diff_fixed))

with open(os.path.join(output_dir, "triage_plan.patch"), "w", encoding='utf-8') as f:
    f.write("\n".join(diffs))

# Save the modifications
with open(todo_path, "w", encoding='utf-8') as f:
    f.writelines(remaining_todo)

for idx, lines in extracted_blocks.items():
    target_rel = sections[idx][1]
    target_abs = os.path.join(output_dir, target_rel)
    header_content = f"# {target_rel.split(os.sep)[-1].replace('.md', '')}\n\n> **[DRAFT]** Migrated from canonical todo.md for consolidation.\n\n"
    with open(target_abs, "w", encoding='utf-8') as f:
        f.writelines([header_content] + lines)

print(f"Generated {len(extracted_blocks)} drafted files into whitepapers/. Created triage_plan.patch")
