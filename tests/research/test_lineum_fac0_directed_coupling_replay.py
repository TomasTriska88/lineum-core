import importlib.util
from pathlib import Path


def _load_runner():
    path = (
        Path(__file__).resolve().parents[2]
        / "research"
        / "runners"
        / "lineum_fac0_directed_coupling_replay.py"
    )
    spec = importlib.util.spec_from_file_location(
        "lineum_fac0_directed_coupling_replay", path
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_fac0_r1_supported_replay_gate():
    payload = _load_runner().run()
    assert payload["source"]["math_blob_match"]
    assert payload["environment"]["repository_numpy_contract_pass"]
    assert payload["graph_check"]["passed"]
    assert payload["linearity_check"]["passed"]
    assert payload["stochastic_delta_matched_rng"]["passed"]
    assert payload["passed"]
