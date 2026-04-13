import os
import time
from pathlib import Path

def main():
    # Traverse up to the repository root relative to this script
    root = Path(__file__).resolve().parent.parent
    scratch_dir = root / ".scratch"
    
    if not scratch_dir.exists() or not scratch_dir.is_dir():
        return
        
    # Set threshold to 3 days
    threshold_days = 3
    threshold_time = time.time() - (threshold_days * 24 * 3600)
    
    deleted_count = 0
    for filepath in scratch_dir.glob("**/*"):
        if filepath.is_file() and filepath.name != "README.md":
            try:
                mtime = filepath.stat().st_mtime
                if mtime < threshold_time:
                    filepath.unlink()
                    deleted_count += 1
            except Exception:
                pass
                
    if deleted_count > 0:
        print(f">>> [Lineum Core] Swept {deleted_count} stale artifacts from .scratch/ (> {threshold_days} days old).", flush=True)

if __name__ == "__main__":
    main()
