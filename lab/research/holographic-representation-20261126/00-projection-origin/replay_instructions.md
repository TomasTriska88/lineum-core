# Replay

In an isolated working directory, copy `used_frames.npz` and `replay_audit.py`, then extract the historical audit ZIP there. Copy its `projection_results.json` to `expected.json`. Run `python replay_audit.py` with NumPy, SciPy and Pillow. Compare the numeric fields of the new `projection_results.json` to `expected.json` (tolerance 1e-10 absolute/relative). Source-archive metadata is carried forward from the original audit, not claimed to be a hash of the extracted frame NPZ. See `input_provenance.json` for actual array digests. The replay does not rerun the original physical solver.
