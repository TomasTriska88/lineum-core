import pytest
from pathlib import Path
import re

def test_external_llm_api_key_isolation(project_root):
    """
    Ensure that the public physics repository never consumes external LLM keys.
    """
    root = Path(project_root)
    
    # Directories where API key usage is expressly forbidden
    forbidden_dirs = ["scripts", "tools", ".scratch", "tests"]
    
    forbidden_patterns = [
        re.compile(r'GEMINI_API_KEY'),
        re.compile(r'\.env\.local')
    ]
    
    errors = []
    
    for d in forbidden_dirs:
        dir_path = root / d
        if not dir_path.exists():
            continue
            
        # Check all py, js, ts, sh files
        for ext in ["*.py", "*.js", "*.ts", "*.sh"]:
            for filepath in dir_path.rglob(ext):
                # Skip this test file itself so it doesn't fail on reading its own source code
                if filepath.name == "test_api_key_isolation.py":
                    continue
                    
                content = filepath.read_text(encoding="utf-8", errors="ignore")
                
                for pattern in forbidden_patterns:
                    if pattern.search(content):
                        errors.append(f"Security Violation: File {filepath.relative_to(root)} accesses forbidden pattern '{pattern.pattern}'. External LLM keys do not belong in Lineum Core.")
                        break

    assert not errors, "API Key Isolation Failed:\n" + "\n".join(errors)
