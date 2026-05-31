#!/usr/bin/env python3
"""
lab/extract_audit_data.py
=========================
[DEPRECATED] Thin compatibility wrapper for the Svelte visualizer data extraction pipeline.
This wrapper imports the modern canonical replay compiler from scripts/compile_lab_datasets.py.

Usage of this script directly is deprecated. Please migrate to scripts/compile_lab_datasets.py.
This script remains active to preserve compatibility with existing backend orchestrators, CLI tools,
and test hooks that expect data extraction to exist at this path.
"""

import os
import sys
import json
import shutil
import warnings

# Add repo root to sys.path so we can import scripts.compile_lab_datasets
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.append(REPO_ROOT)

try:
    from scripts.compile_lab_datasets import compile_run
except ImportError as e:
    print(f"Error importing compile_run from scripts.compile_lab_datasets: {e}", file=sys.stderr)
    sys.exit(1)

# Issue a deprecation warning but keep execution functional
warnings.warn(
    "lab/extract_audit_data.py is deprecated and will be removed in a future release. "
    "Use scripts/compile_lab_datasets.py for canonical replay dataset compilation.",
    DeprecationWarning,
    stacklevel=2
)

def run_legacy_sync():
    """Runs the legacy sync loop processing all runs in output_wp/runs and building the manifest."""
    output_wp = os.path.join(REPO_ROOT, "output_wp")
    runs_base = os.path.join(output_wp, "runs")
    lab_data_dir = os.path.join(REPO_ROOT, "lab", "public", "data")
    runs_data_dir = os.path.join(lab_data_dir, "runs")
    
    os.makedirs(runs_data_dir, exist_ok=True)
    
    if not os.path.exists(runs_base):
        print(f"Base runs directory does not exist: {runs_base}")
        return
        
    runs = [
        os.path.join(runs_base, d) 
        for d in os.listdir(runs_base) 
        if os.path.isdir(os.path.join(runs_base, d)) and not d.startswith('_') and not d.startswith('.')
    ]
    
    manifest = []
    print(f"Found {len(runs)} run directories in {runs_base} to process.")
    
    for run_dir in runs:
        run_id = os.path.basename(run_dir)
        target_dir = os.path.join(runs_data_dir, run_id)
        
        try:
            print(f"\n>>> [Legacy Wrapper] Processing Run: {run_id}")
            meta = compile_run(
                run_dir=run_dir,
                output_dir=target_dir,
                amplitude_scale_factor=1000000.0,
                frame_cap=100,
                spatial_downsample_step=2,
                decimals=3,
                dataset_classification="canonical_audit" if "whitepaper" in run_id else "experimental"
            )
            if meta:
                manifest.append(meta)
        except Exception as e:
            print(f"    [SKIP] Failed to process run {run_id}: {e}")
            
    manifest_path = os.path.join(lab_data_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=4)
        
    print(f"\n--- [Legacy Wrapper] Sync Complete: {len(manifest)} runs registered in manifest ---")

if __name__ == "__main__":
    run_legacy_sync()
