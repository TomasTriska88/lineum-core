# Lineum Core Execution Device Policy

## Contract

Lineum Core never selects CUDA merely because a GPU is visible. The runtime backend is selected explicitly with `LINEUM_DEVICE`:

- `numpy` uses the NumPy CPU solver and is the default.
- `torch-cpu` uses the PyTorch solver on CPU.
- `cuda` requests the PyTorch solver on a compatible CUDA device.

The legacy `LINEUM_USE_PYTORCH=1` environment variable maps to `torch-cpu` when `LINEUM_DEVICE` is absent. It does not opt into CUDA.

## Canonical Runs

Canonical runs always execute on CPU. If `cuda` is requested for a canonical run, the request is retained in runtime metadata but the selected device is PyTorch CPU. This preserves deterministic evidence across hardware.

## CUDA Compatibility

Before selecting CUDA, the execution policy verifies all of the following:

1. PyTorch is installed.
2. PyTorch reports CUDA as available.
3. The detected device architecture appears in the architectures compiled into the installed PyTorch build.

The policy derives architectures from the local runtime and contains no GPU-model or architecture allowlist. An incompatible explicit CUDA request fails before the solver launches a CUDA kernel.

## Verification

Run the permanent execution-policy regression tests:

```bash
python -m pytest tests/test_execution_policy.py -q
```

Verify the NumPy CPU physics path:

```bash
LINEUM_DEVICE=numpy python -m pytest tests/test_lineum_core_math.py tests/test_physics_contract.py -q
```

Verify the PyTorch CPU path:

```bash
LINEUM_DEVICE=torch-cpu python -m pytest tests/test_execution_policy.py tests/test_ra_scenarios.py -q
```
