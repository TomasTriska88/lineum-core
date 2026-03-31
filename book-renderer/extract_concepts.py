import re
import json

md_path = r'c:\Users\Tomáš\Documents\GitHub\lineum-core\docs\education\level1-book\level1-math-you-can-see.md'

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()
    
# Clean Windows crlf
text = text.replace('\r\n', '\n')

# Find chapters
chapters = []
for m in re.finditer(r'## Chapter (\d+): (.*?)\n', text):
    chapters.append({
        'num': int(m.group(1)),
        'title': m.group(2).strip(),
        'pos': m.start()
    })

concepts = []
blocks = re.split(r'\n### ', text)

for block in blocks[1:]:
    lines = block.split('\n')
    title = lines[0].strip()
    
    # Ignore sections that are not concepts
    if "Level" in title or "PART" in title:
        continue
        
    c_id = re.sub(r'[^a-z0-9]', '', title.lower())
    
    # Determine chapter
    block_pos = text.find('### ' + title)
    chapter_num = 1
    chapter_title = ""
    for ch in chapters:
        if ch['pos'] < block_pos:
            chapter_num = ch['num']
            chapter_title = ch['title']
            
    # Regex extraction
    hook_m = re.search(r'\*\*(Imagine.*?)\*\*', block)
    hook = hook_m.group(1).strip() if hook_m else ""
    
    img_path_m = re.search(r'\!\[.*?\]\((.*?)\)', block)
    img_path = img_path_m.group(1).strip() if img_path_m else ""
    
    img_prompt_m = re.search(r'\[IMAGE_PROMPT:\s*(.*?)\]', block)
    img_prompt = img_prompt_m.group(1).strip() if img_prompt_m else ""
    
    aha_m = re.search(r'> \*\*💡 AHA MOMENT:\*\*\s*(.*?)\n', block)
    aha = aha_m.group(1).strip() if aha_m else ""
    
    # Explain comes between hook and image
    explain_m = re.search(r'\*\*(?:Imagine.*?)\*\*\n(.*?)!\[', block, re.DOTALL)
    explain = explain_m.group(1).replace('\n', ' ').strip() if explain_m else ""
    
    what_m = re.search(r'\*\*What it is:\*\*\n(.*?)(?=\n\*\*|$)', block, re.DOTALL)
    what = what_m.group(1).replace('\n', ' ').strip() if what_m else ""
    
    how_m = re.search(r'\*\*How to solve:\*\*\n(.*?)(?=\n\*\*|$)', block, re.DOTALL)
    how = how_m.group(1).replace('\n', ' ').strip() if how_m else ""
    
    why_m = re.search(r'\*\*Why it works in space:\*\*\n(.*?)(?=\n\*\*|$)', block, re.DOTALL)
    why = why_m.group(1).replace('\n', ' ').strip() if why_m else ""
    
    summ_m = re.search(r'\*\*Summary:\*\*\n(.*?)(?=\n\n(?:###|---)|\Z)', block, re.DOTALL)
    summ = summ_m.group(1).replace('\n', ' ').strip() if summ_m else ""
    
    # Clean up artifacts like '---'
    if summ.endswith('---'): summ = summ[:-3].strip()

    concept = {
        'id': c_id,
        'chapterNumber': chapter_num,
        'chapterTitle': chapter_title,
        'title': title,
        'hook': hook,
        'explain': explain,
        'image': {
            'path': img_path,
            'prompt': img_prompt
        },
        'aha': aha,
        'whatItIs': what,
        'howToSolve': how,
        'whyItWorks': why,
        'summary': summ,
    }
    
    concepts.append(concept)
    if len(concepts) >= 15:
        break

ts_out = """export interface Concept {
  id: string;
  chapterNumber: number;
  chapterTitle: string;
  title: string;
  hook: string;
  explain: string;
  image: {
    path: string;
    prompt: string;
  };
  aha: string;
  whatItIs: string;
  howToSolve: string;
  whyItWorks: string;
  summary: string;
}

export const level1Concepts: Concept[] = """

ts_out += json.dumps(concepts, indent=2, ensure_ascii=False)
ts_out += ";\n"

with open(r'c:\\Users\\Tomáš\\Documents\\GitHub\\lineum-core\\book-renderer\\src\\lib\\data\\concepts.ts', 'w', encoding='utf-8') as f:
    f.write(ts_out)

print(f"Regex fully extracted {len(concepts)} concepts.")
