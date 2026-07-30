from pathlib import Path

import numpy as np
import pytest

import lineum_core.math as lineum_math
from lineum_core.math import CoreConfig, ExecutionPolicy


@pytest.fixture(autouse=True)
def reset_execution_policy(monkeypatch):
    original_use_pytorch = lineum_math.USE_PYTORCH
    original_state = {
        "device": ExecutionPolicy._device,
        "deterministic_mode": ExecutionPolicy._deterministic_mode,
        "is_canonical_run": ExecutionPolicy._is_canonical_run,
    }
    monkeypatch.delenv("LINEUM_DEVICE", raising=False)
    monkeypatch.delenv("LINEUM_USE_PYTORCH", raising=False)
    yield
    lineum_math.USE_PYTORCH = original_use_pytorch
    ExecutionPolicy._device = original_state["device"]
    ExecutionPolicy._deterministic_mode = original_state["deterministic_mode"]
    ExecutionPolicy._is_canonical_run = original_state["is_canonical_run"]
    if hasattr(ExecutionPolicy, "_backend"):
        ExecutionPolicy._backend = None
    if hasattr(ExecutionPolicy, "_requested_mode"):
        ExecutionPolicy._requested_mode = None


def _mock_cuda(monkeypatch, *, capability, compiled_architectures):
    if lineum_math.torch is None:
        pytest.skip("PyTorch is not installed")
    monkeypatch.setattr(lineum_math.torch.cuda, "is_available", lambda: True)
    monkeypatch.setattr(
        lineum_math.torch.cuda,
        "get_device_capability",
        lambda *_args, **_kwargs: capability,
    )
    monkeypatch.setattr(
        lineum_math.torch.cuda,
        "get_arch_list",
        lambda: list(compiled_architectures),
    )
    monkeypatch.setattr(lineum_math.torch.cuda, "manual_seed_all", lambda _seed: None)
    monkeypatch.setattr(lineum_math.torch, "manual_seed", lambda _seed: None)
    monkeypatch.setattr(
        lineum_math.torch,
        "use_deterministic_algorithms",
        lambda *_args, **_kwargs: None,
    )


def test_visible_cuda_is_not_selected_implicitly(monkeypatch):
    _mock_cuda(
        monkeypatch,
        capability=(12, 0),
        compiled_architectures=("sm_90",),
    )
    lineum_math.USE_PYTORCH = True

    ExecutionPolicy.init_core_determinism(enforce_canonical=False, seed=42)

    assert ExecutionPolicy.get_device().type == "cpu"


def test_explicit_torch_cpu_mode_uses_pytorch_without_cuda():
    if lineum_math.torch is None:
        pytest.skip("PyTorch is not installed")

    ExecutionPolicy.init_core_determinism(
        enforce_canonical=False,
        seed=42,
        device_mode="torch-cpu",
    )

    assert ExecutionPolicy.get_device().type == "cpu"
    assert ExecutionPolicy.get_metadata()["execution_backend"] == "pytorch"


def test_cpu_metadata_does_not_initialize_or_probe_cuda(monkeypatch):
    if lineum_math.torch is None:
        pytest.skip("PyTorch is not installed")
    capability_calls = []
    monkeypatch.setattr(lineum_math.torch.cuda, "is_available", lambda: True)
    monkeypatch.setattr(
        lineum_math.torch.cuda,
        "get_device_capability",
        lambda *_args, **_kwargs: capability_calls.append(True) or (9, 0),
    )

    ExecutionPolicy.init_core_determinism(
        enforce_canonical=False,
        seed=42,
        device_mode="torch-cpu",
    )
    metadata = ExecutionPolicy.get_metadata()

    assert capability_calls == []
    assert metadata["cuda_available"] is True
    assert metadata["cuda_compatible"] is None


def test_incompatible_cuda_request_fails_before_kernel_execution(monkeypatch):
    _mock_cuda(
        monkeypatch,
        capability=(12, 0),
        compiled_architectures=("sm_80", "sm_90"),
    )

    with pytest.raises(RuntimeError, match="sm_120"):
        ExecutionPolicy.init_core_determinism(
            enforce_canonical=False,
            seed=42,
            device_mode="cuda",
        )


def test_compatible_cuda_is_available_only_when_explicitly_requested(monkeypatch):
    _mock_cuda(
        monkeypatch,
        capability=(9, 0),
        compiled_architectures=("sm_80", "sm_90"),
    )

    ExecutionPolicy.init_core_determinism(
        enforce_canonical=False,
        seed=42,
        device_mode="cuda",
    )

    assert ExecutionPolicy.get_device().type == "cuda"


def test_canonical_run_forces_cpu_even_when_cuda_is_requested(monkeypatch):
    _mock_cuda(
        monkeypatch,
        capability=(9, 0),
        compiled_architectures=("sm_90",),
    )

    ExecutionPolicy.init_core_determinism(
        enforce_canonical=True,
        seed=42,
        device_mode="cuda",
    )

    assert ExecutionPolicy.get_device().type == "cpu"
    assert ExecutionPolicy.get_metadata()["requested_device_mode"] == "cuda"


def test_invalid_device_mode_fails_clearly():
    with pytest.raises(ValueError, match="LINEUM_DEVICE"):
        ExecutionPolicy.init_core_determinism(
            enforce_canonical=False,
            seed=42,
            device_mode="automatic-magic",
        )


def test_legacy_pytorch_switch_maps_to_torch_cpu(monkeypatch):
    if lineum_math.torch is None:
        pytest.skip("PyTorch is not installed")
    monkeypatch.setenv("LINEUM_USE_PYTORCH", "1")
    lineum_math.USE_PYTORCH = True

    ExecutionPolicy.init_core_determinism(enforce_canonical=False, seed=42)

    assert ExecutionPolicy.get_device().type == "cpu"


def test_step_core_executes_on_explicit_torch_cpu():
    if lineum_math.torch is None:
        pytest.skip("PyTorch is not installed")
    size = 4
    state = {
        "psi": np.full((size, size), 0.1 + 0.0j, dtype=np.complex128),
        "phi": np.zeros((size, size), dtype=np.float64),
        "kappa": np.ones((size, size), dtype=np.float64),
        "delta": np.zeros((size, size), dtype=np.float64),
    }
    config = CoreConfig(disable_quantum_noise=True)
    ExecutionPolicy.init_core_determinism(
        enforce_canonical=False,
        seed=42,
        device_mode="torch-cpu",
    )

    result = lineum_math.step_core(state, config)

    assert result["psi"].shape == (size, size)
    assert result["phi"].shape == (size, size)
    assert np.all(np.isfinite(result["psi"]))
    assert np.all(np.isfinite(result["phi"]))
    assert ExecutionPolicy.get_metadata()["execution_device"] == "cpu"


def test_readme_documents_explicit_device_modes():
    readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(
        encoding="utf-8"
    )

    assert "LINEUM_DEVICE=numpy" in readme
    assert "LINEUM_DEVICE=torch-cpu" in readme
    assert "LINEUM_DEVICE=cuda" in readme
