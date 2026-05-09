import json
import re
import os
import sys
import urllib.request

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRATCH_DIR = os.path.join(REPO_ROOT, "lab", ".scratch", "voynich", "alephmembeth")
DATA_DIR = os.path.join(REPO_ROOT, "data", "voynich")
URL = "http://www.voynich.com/pages/PagesH.txt"
TXT_FILE = os.path.join(SCRATCH_DIR, "takahashi_clean.txt")

def fetch_data():
    os.makedirs(SCRATCH_DIR, exist_ok=True)
    if not os.path.exists(TXT_FILE):
        print(f"Downloading Voynich Takahashi IVTFF corpus from {URL}...")
        try:
            req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                text = response.read().decode('utf-8')
                with open(TXT_FILE, 'w', encoding='utf-8') as f:
                    f.write(text)
            print("Download successful.")
        except Exception as e:
            print(f"Failed to download corpus: {e}")
            return False
    return True

def generate_json_folios():
    if not os.path.exists(TXT_FILE):
        print("Corpus file missing.")
        return False
        
    os.makedirs(DATA_DIR, exist_ok=True)

    folios = {}
    current_folio = None
    
    with open(TXT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('<f'):
                match = re.search(r'<f([^>.]*)', line)
                if match:
                    current_folio = 'f' + match.group(1).replace('-', '') # E.g., f1v, f2r
                    if current_folio not in folios:
                        folios[current_folio] = []
                    
            if current_folio and line.strip() and not line.startswith('#'):
                # Strip tags like <f1v.P.1;H> or {plant}
                content = re.sub(r'<[^>]+>', '', line)
                content = re.sub(r'\{[^}]*\}', '', content)
                content = re.sub(r'=[^\s]*', '', content)
                content = content.replace('.', ' ').replace(',', ' ')
                content = re.sub(r'[*!\-=]', '', content)
                tokens = [t for t in content.split() if t]
                if tokens:
                    folios[current_folio].append(tokens)

    print(f"Parsed {len(folios)} unique folios from corpus.")

    count = 0
    for folio_id, lines in folios.items():
        tokens_out = []
        tid = 1
        curr_y = 5
        
        for row in lines:
            curr_x = 5
            for word in row:
                w_len = max(4, len(word) * 1.5)
                
                tok_type = 'Beta'
                color = 'purple'
                if word.endswith('dy') or word.endswith('iin') or word.endswith('y'):
                    tok_type = 'Omega'
                    color = 'amber'
                elif any(c in word for c in ['k', 't', 'p', 'f']):
                    tok_type = 'Alpha'
                    color = 'blue'
                    
                hyp = None
                if word in ['okam', 'okar'] and folio_id == 'f1v':
                    hyp = 'Verb: To Cut (BLOCKED)'
                    
                tokens_out.append({
                    'id': f'T{tid}',
                    'text': word,
                    'type': tok_type,
                    'x': round(curr_x, 1),
                    'y': round(curr_y, 1),
                    'w': round(w_len, 1),
                    'h': 3,
                    'layer': 3,
                    'color': color,
                    'hypothesis': hyp
                })
                tid += 1
                curr_x += w_len + 1.5
                
                if curr_x > 90:
                    curr_x = 5
                    curr_y += 4
                    
            curr_y += 4
            
        data = {
            'id': folio_id,
            'imageUrl': f'/voynich_{folio_id}.jpg' if folio_id == 'f1v' else f'/voynich_placeholder.jpg',
            'width': 1500,
            'height': 2000,
            'tokens': tokens_out,
            'hooks': [
                { 'id': 'H1', 'sourceToken': 'T4', 'targetX': 60, 'targetY': 45, 'type': 'L2_Serrated' }
            ] if folio_id == 'f1v' else []
        }

        out_file = os.path.join(DATA_DIR, f"{folio_id}.json")
        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        count += 1

    print(f"Successfully generated {count} JSON folio files into {DATA_DIR}.")
    return True

if __name__ == "__main__":
    print("--- Voynich Bring Your Own Data Pipeline ---")
    if fetch_data():
        if generate_json_folios():
            sys.exit(0)
    sys.exit(1)
