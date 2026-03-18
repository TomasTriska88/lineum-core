import json
from pathlib import Path

def test_lineum_config_emails():
    """
    Ensure that the formal Lineum configuration solely uses core@lineum.io
    and does not contain any legacy noreply or personal gmail addresses.
    """
    config_path = Path("portal/src/lib/data/project/lineum-config.json")
    assert config_path.exists(), "lineum-config.json does not exist."
    
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    contact_block = config.get("contact", {})
    
    # Enforce strict values
    assert contact_block.get("primary") == "core@lineum.io", "Primary contact must be core@lineum.io"
    assert contact_block.get("noreply") == "core@lineum.io", "Noreply contact must be core@lineum.io"
    
    # Generic sweep just in case new keys were added
    for key, value in contact_block.items():
        val_str = str(value).lower()
        assert "gmail.com" not in val_str, f"Found legacy gmail address in contact.{key}"
        assert "noreply@" not in val_str, f"Found legacy noreply address in contact.{key}"
