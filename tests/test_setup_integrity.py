import sys
import subprocess
from pathlib import Path

def test_setup_py_integrity():
    """
    Ensures that setup.py is syntactically valid and package metadata is correctly formatted.
    This runs 'python setup.py check' natively to catch basic configuration issues.
    """
    root = Path(__file__).resolve().parent.parent
    setup_file = root / "setup.py"
    
    assert setup_file.exists(), "setup.py is missing from the repository root!"

    result = subprocess.run(
        [sys.executable, "setup.py", "check"],
        cwd=root,
        capture_output=True,
        text=True
    )
    
    # Strict validation of the check output
    assert result.returncode == 0, f"setup.py execution failed:\n{result.stderr}\n{result.stdout}"
