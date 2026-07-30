import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def test_whitepaper_contract_quarantine_scanning_logic():
    """
    Test that the whitepaper_contract.py script explicitly places quarantined items 
    in output_wp/archive/quarantine/_quarantine_registry.json.
    """
    q_reg_path = os.path.join(REPO_ROOT, "output_wp", "archive", "quarantine", "_quarantine_registry.json")
    
    # The registry should exist because we just ran it
    assert os.path.exists(q_reg_path), "Quarantine registry must exist in the archive directory."
    
    import json
    with open(q_reg_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    assert "quarantined_directories" in data
    
    # We expect `*_corrupted` runs to be present in this registry
    found_corrupted = False
    for p in data["quarantined_directories"]:
        if "corrupted" in p.lower() or "20260306_201952" in p.lower():
            found_corrupted = True
            break
            
    assert found_corrupted, "The tampered 20260306 run must be listed in the quarantine registry."
