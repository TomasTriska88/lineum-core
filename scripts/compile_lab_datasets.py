#!/usr/bin/env python3
"""
scripts/compile_lab_datasets.py
================================
Canonical replay dataset compiler for the Lineum Lab visualizer.
Transforms raw audit simulation outputs (*_frames_phi.npy, *_trajectories.csv, 
and *_phi_center_log.csv) into 7 Svelte-compatible JSON files:
- phi_frames.json
- trajectories.json
- metadata.json
- resonance.json
- harmonics.json
- stretching_data.json
- discovery.json

Coordinate Mapping Note:
------------------------
In the physics solver, grid coordinates are represented as (row, col) matching (y, x).
The trajectories.csv output logs 'x' as the column index (horizontal) and 'y' as 
the row index (vertical).
The Svelte visualizer path schema expects [x, y, amplitude, step] which maps directly
to [col_index, row_index, scaled_amplitude, step] in 128x128 solver coordinates.
"""

import os
import sys
import json
import glob
import argparse
import subprocess
import numpy as np
import pandas as pd

# First 50 Riemann Zeta zeros for scanner and resonance correlations
ZETA_ZEROS_REF = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
    37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
    52.970321, 56.446248, 59.347044, 60.831779, 62.839000,
    65.112000, 67.079000, 69.115000, 72.067000, 75.704000,
    77.144000, 79.337000, 82.910000, 84.735000, 87.425000,
    88.809000, 92.491000, 94.651000, 95.883000, 98.831000,
    101.317000, 103.725000, 105.446000, 107.168000, 111.029000,
    111.874000, 114.320000, 116.226000, 118.790000, 121.370000,
    122.946000, 124.256000, 127.516000, 129.578000, 131.087000,
    133.497000, 134.756000, 138.116000, 139.736000, 141.123000
]

def get_git_commit(repo_root=None):
    """Retrieve current HEAD git commit hash."""
    cwd = repo_root if repo_root else os.getcwd()
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL, cwd=cwd
        ).decode("utf-8").strip()
    except Exception:
        return "unknown"

def normalize_list(l):
    """Normalize list values to [0.0, 1.0]."""
    if not l:
        return []
    if len(l) < 2:
        return [1.0]
    mi, mx = min(l), max(l)
    if mx == mi:
        return [1.0] * len(l)
    return [(x - mi) / (mx - mi) for x in l]

def find_file(directory, patterns):
    """Search for a file matching patterns within directory."""
    for p in patterns:
        matches = glob.glob(os.path.join(directory, p))
        if matches:
            return matches[0]
    return None

def compile_run(
    run_dir,
    output_dir,
    amplitude_scale_factor=1000000.0,
    frame_cap=100,
    spatial_downsample_step=2,
    decimals=3,
    scenario_label=None,
    dataset_classification=None,
    run_id=None,
    seed=None,
    config_dict=None
):
    """
    Compiles raw simulation files from run_dir to output_dir into Svelte JSON files.
    """
    if not os.path.exists(run_dir):
        raise FileNotFoundError(f"Source run directory does not exist: {run_dir}")
        
    os.makedirs(output_dir, exist_ok=True)
    
    # 0. Locate files
    phi_path = find_file(run_dir, ["*_frames_phi.npy", "*phi_frames.npy", "*phi.npy", "frames_phi.npy"])
    traj_path = find_file(run_dir, ["*_trajectories.csv", "trajectories.csv"])
    center_log_path = find_file(run_dir, ["*_phi_center_log.csv", "*center_log.csv", "phi_center_log.csv"])
    
    # Check required inputs
    missing = []
    if not phi_path:
        missing.append("frames_phi (.npy)")
    if not traj_path:
        missing.append("trajectories (.csv)")
    if not center_log_path:
        missing.append("phi_center_log (.csv)")
        
    if missing:
        raise FileNotFoundError(f"Missing required raw files in {run_dir}: {', '.join(missing)}")
        
    resolved_run_id = run_id if run_id else os.path.basename(os.path.abspath(run_dir))
    run_tag = resolved_run_id.split('_2026')[0] if '_2026' in resolved_run_id else resolved_run_id
    
    # 1. Load Phi-Field Frames
    phi_frames = np.load(phi_path)
    original_frame_count = len(phi_frames)
    
    # Determine step per frame
    # We try to look up max step from trajectories or logs, else default to 2000
    df_traj = pd.read_csv(traj_path)
    total_steps = int(df_traj['step'].max()) if not df_traj.empty else 2000
    orig_step_per_frame = total_steps // original_frame_count if original_frame_count > 0 else 1
    
    # Time downsampling (frame cap)
    time_step = 1
    if frame_cap and original_frame_count > frame_cap:
        time_step = int(np.ceil(original_frame_count / frame_cap))
        phi_frames_selected = phi_frames[::time_step]
    else:
        phi_frames_selected = phi_frames
        
    frame_count = len(phi_frames_selected)
    frame_steps = [int(idx * orig_step_per_frame) for idx in range(0, original_frame_count, time_step)]
    
    # Spatial downsampling and quantization
    phi_lowres = np.round(
        phi_frames_selected[:, ::spatial_downsample_step, ::spatial_downsample_step], 
        decimals=decimals
    ).tolist()
    
    phi_payload = {
        "metadata": {
            "source": resolved_run_id,
            "frame_count": frame_count,
            "grid_size": 128 // spatial_downsample_step,
            "original_grid_size": 128
        },
        "frames": phi_lowres
    }
    
    with open(os.path.join(output_dir, "phi_frames.json"), "w") as f:
        json.dump(phi_payload, f)
        
    # 2. Extract Trajectories
    # Group trajectories and filter for top 20 longest duration
    traj_info = df_traj.groupby('id')['step'].agg(['min', 'max'])
    traj_info['duration'] = traj_info['max'] - traj_info['min']
    top_ids = traj_info.sort_values('duration', ascending=False).head(20).index.tolist()
    
    trajectories_data = []
    for tid in top_ids:
        t_df = df_traj[df_traj['id'] == tid].sort_values('step')
        path = []
        min_s, max_s = t_df['step'].min(), t_df['step'].max()
        for target_step in frame_steps:
            if target_step < min_s or target_step > max_s:
                path.append(None)
            else:
                row = t_df[t_df['step'] <= target_step].tail(1)
                if not row.empty:
                    x_val = float(row['x'].values[0])
                    y_val = float(row['y'].values[0])
                    amp_val = float(row['amplitude'].values[0]) * amplitude_scale_factor
                    step_val = int(row['step'].values[0])
                    path.append([x_val, y_val, amp_val, step_val])
                else:
                    path.append(None)
        trajectories_data.append({"id": int(tid), "path": path})
        
    with open(os.path.join(output_dir, "trajectories.json"), "w") as f:
        json.dump(trajectories_data, f)
        
    # 3. Resonance & Center Evolution
    phi_log = pd.read_csv(center_log_path)
    phi_abs = phi_log['phi_center_abs'].values
    max_abs = phi_abs.max() if len(phi_abs) > 0 and phi_abs.max() > 0 else 1.0
    phi_norm_scaled = (phi_abs / max_abs * 40.0)
    
    phi_evolution = [float(phi_norm_scaled[min(int(step), len(phi_norm_scaled)-1)]) for step in frame_steps]
    
    with open(os.path.join(output_dir, "resonance.json"), "w") as f:
        json.dump({"zeta_zeros": ZETA_ZEROS_REF[:5], "phi_evolution": phi_evolution}, f)
        
    # 4. Fourier and Riemann Correlation (Discovery)
    fft_vals = np.abs(np.fft.rfft(phi_abs))
    max_fft = fft_vals.max() if len(fft_vals) > 0 and fft_vals.max() > 0 else 1.0
    fft_norm = (fft_vals / max_fft * 10.0).tolist()[:50]
    
    top_indices = np.argsort(phi_abs)[-50:]
    dejavu_points = sorted(top_indices.tolist())
    
    norm_dejavu = normalize_list(dejavu_points)
    norm_riemann = normalize_list(ZETA_ZEROS_REF[:len(norm_dejavu)])
    
    pearson_r = 0.0
    euclidean_dist = 0.0
    if len(norm_dejavu) > 1:
        corr = np.corrcoef(norm_dejavu, norm_riemann)[0, 1]
        pearson_r = float(corr) if not np.isnan(corr) else 0.0
        euclidean_dist = float(np.linalg.norm(np.array(norm_dejavu) - np.array(norm_riemann)))
        
    discovery_data = {
        "fourier_spectrum": [float(x) for x in fft_norm],
        "dejavu_points": [int(x) for x in dejavu_points],
        "norm_dejavu": [float(x) for x in norm_dejavu],
        "norm_riemann": [float(x) for x in norm_riemann],
        "pearson_r": float(pearson_r),
        "euclidean_dist": float(euclidean_dist),
        "zeta_zeros_ref": [float(x) for x in ZETA_ZEROS_REF[:len(norm_dejavu)]]
    }
    
    with open(os.path.join(output_dir, "discovery.json"), "w") as f:
        json.dump(discovery_data, f)
        
    # 5. Harmonics (Spiral fitting & zeta correlation)
    phi_const = (1 + 5**0.5) / 2
    golden_b = np.log(phi_const) / (np.pi / 2)
    frame_harmonics = []
    frame_correlation = []
    for i in range(frame_count):
        active = [p for traj in trajectories_data if (p := traj['path'][i])]
        h_score = 0.5
        if len(active) >= 3:
            rs = [np.sqrt((l[0]-64)**2 + (l[1]-64)**2) for l in active]
            thetas = [np.arctan2(l[1]-64, l[0]-64) for l in active]
            try:
                # fit spiral r = a * e^(b * theta) => ln(r) = ln(a) + b * theta
                b = np.polyfit(np.unwrap(thetas), np.log(np.array(rs) + 1e-6), 1)[0]
                h_score = 1.0 - min(1.0, abs(b - golden_b) / golden_b)
            except Exception:
                pass
        frame_harmonics.append(float(h_score))
        c_score = max(0.0, 1.0 - (min([abs(phi_evolution[i] - z) for z in ZETA_ZEROS_REF[:5]]) / 5.0))
        frame_correlation.append(float(c_score))
        
    with open(os.path.join(output_dir, "harmonics.json"), "w") as f:
        json.dump({"frame_harmonics": frame_harmonics, "frame_correlation": frame_correlation}, f)
        
    # 6. Tidal Stretching Data
    all_vars, all_dists = [], []
    for i in range(frame_count):
        active_pos = [[p[0], p[1]] for traj in trajectories_data if (p := traj['path'][i])]
        if len(active_pos) >= 2:
            pts = np.array(active_pos)
            all_vars.append(float(np.var(pts[:, 0]) + np.var(pts[:, 1])))
            all_dists.append(float(np.sqrt(np.sum((np.mean(pts, axis=0) - [64, 64])**2))))
        else:
            all_vars.append(0.0)
            all_dists.append(128.0)
            
    with open(os.path.join(output_dir, "stretching_data.json"), "w") as f:
        json.dump({
            "times": [int(step) for step in frame_steps],
            "variances": all_vars,
            "distances": all_dists
        }, f)
        
    # 7. Metadata (Provenance, scenario config, thresholds)
    median_birth_step = 0
    birth_steps = [t_df['step'].min() for tid in top_ids if not (t_df := df_traj[df_traj['id'] == tid]).empty]
    if birth_steps:
        median_birth_step = int(np.median(birth_steps))
        
    step_pf = orig_step_per_frame * time_step
    birth_frame = median_birth_step // step_pf if step_pf > 0 else 0
    
    # Resolve timestamps
    import datetime
    timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if "_" in resolved_run_id:
        parts = resolved_run_id.split("_")
        # Try to find a date-like part
        for idx in range(len(parts) - 1):
            if parts[idx].startswith("2026") or parts[idx].startswith("2025"):
                timestamp_str = parts[idx] + "_" + parts[idx+1]
                break
                
    git_hash = get_git_commit(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    meta_payload = {
        "run_id": resolved_run_id,
        "run_tag": run_tag,
        "timestamp": timestamp_str,
        "birth_frame": int(birth_frame),
        "frame_count": int(frame_count),
        "pearson_r": float(pearson_r),
        "euclidean_dist": float(euclidean_dist),
        "path_point_schema": ["x", "y", "amplitude", "step"],
        "dataset_classification": dataset_classification if dataset_classification else "experimental",
        "scenario_label": scenario_label if scenario_label else run_tag,
        "git_commit": git_hash,
        "seed": int(seed) if seed is not None else None,
        "config": config_dict if config_dict else {},
        "observer_thresholds": {
            "amplitude_threshold": 1000.0,
            "solver_normalized_threshold": 0.12,
            "amplitude_scale_factor": float(amplitude_scale_factor),
            "contact_distance_px": 12.0,
            "exit_distance_px": 14.0,
            "tear_distance_px": 18.0,
            "persistence_frames": 20
        }
    }
    
    with open(os.path.join(output_dir, "metadata.json"), "w") as f:
        json.dump(meta_payload, f, indent=4)
        
    print(f"Successfully compiled {resolved_run_id} into {output_dir}")
    return meta_payload

def main():
    parser = argparse.ArgumentParser(description="Compile raw Lineum simulation runs into visualizer JSONs.")
    parser.add_argument("--run-dir", required=True, help="Path to the directory containing raw simulation outputs.")
    parser.add_argument("--output-dir", required=True, help="Path to the target directory for compiled JSONs.")
    parser.add_argument("--amplitude-scale", type=float, default=1000000.0, help="Amplitude scale factor (default: 1_000_000).")
    parser.add_argument("--frame-cap", type=int, default=100, help="Maximum frame count cap (default: 100).")
    parser.add_argument("--spatial-downsample", type=int, default=2, help="Grid downsampling step (default: 2, e.g. 128x128 -> 64x64).")
    parser.add_argument("--decimals", type=int, default=3, help="Phi-field decimals rounding (default: 3).")
    parser.add_argument("--scenario-label", help="Scenario identifier label.")
    parser.add_argument("--dataset-classification", help="Dataset classification tag.")
    parser.add_argument("--run-id", help="Explicit override for Run ID.")
    parser.add_argument("--seed", type=int, help="Optional simulation random seed.")
    
    args = parser.parse_args()
    
    try:
        compile_run(
            run_dir=args.run_dir,
            output_dir=args.output_dir,
            amplitude_scale_factor=args.amplitude_scale,
            frame_cap=args.frame_cap,
            spatial_downsample_step=args.spatial_downsample,
            decimals=args.decimals,
            scenario_label=args.scenario_label,
            dataset_classification=args.dataset_classification,
            run_id=args.run_id,
            seed=args.seed
        )
        sys.exit(0)
    except Exception as e:
        print(f"Compilation failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
