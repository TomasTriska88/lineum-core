from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = (
    ROOT
    / "research"
    / "runners"
    / "lineum_b4_q2_m1_rs1_resolution_sensitivity.py"
)
SPEC = importlib.util.spec_from_file_location("lineum_b4_q2_m1_rs1", RUNNER_PATH)
assert SPEC is not None and SPEC.loader is not None
rs1 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rs1
SPEC.loader.exec_module(rs1)


def _result(
    size: int,
    *,
    c0: float = 0.0,
    c1: float,
    c2: float,
    c3: float,
    valid: bool = True,
    c0_phi: float = 0.0,
    c0_mu: float = 0.0,
) -> dict[str, Any]:
    return {
        "size": size,
        "values": {"C0": c0, "C1": c1, "C2": c2, "C3": c3},
        "c0_channel_divergences": {
            "psi": c0,
            "phi": c0_phi,
            "mu": c0_mu,
        },
        "valid": valid,
    }


def test_protocol_has_exactly_one_new_resolution_and_frozen_geometry() -> None:
    assert rs1.EXECUTION_SIZES == (96, 128)
    assert rs1.PROSPECTIVE_SIZE == 128
    assert rs1.REPRESENTATIVE_VARIANT_IDS == (12, 17)
    assert rs1.representative_schedule(96) == (
        (18.0, 3.75, 0, 0),
        (18.0, 5.25, 0, 0),
    )
    assert rs1.representative_schedule(128) == (
        (24.0, 5.0, 0, 0),
        (24.0, 7.0, 0, 0),
    )
    assert rs1.common_width(96) == 7.5
    assert rs1.common_width(128) == 10.0


@pytest.mark.parametrize("size", [64, 112, 144, 160])
def test_protocol_rejects_every_nonregistered_resolution(size: int) -> None:
    with pytest.raises(ValueError, match="sizes 96 and 128 only"):
        rs1.representative_schedule(size)
    with pytest.raises(ValueError, match="sizes 96 and 128 only"):
        rs1.common_width(size)


def test_frozen_sources_bind_the_parent_runner_and_active_core() -> None:
    assert rs1.FROZEN_SOURCE_BLOBS == {
        "research/runners/lineum_b4_q2_mu_causal_reuse.py": (
            "8f818480b6b7160a49365b730bf884a4b94d9deb"
        ),
        "lineum_core/math.py": "bb877021810691223a0eb960a45493a2e351112a",
        "requirements.txt": "942f2b94b3d3f8c767451ae2d847a7b17c86d81e",
        "requirements-dev.txt": "7a0907e3e6c2d15400d19b536227a509910ae7e9",
    }
    assert rs1.REQUIRED_PYTHON == "3.11.15"
    assert rs1.REQUIRED_NUMPY == "1.26.4"


def test_subthreshold_stable_pair_is_only_an_unsupported_primary_indication() -> None:
    reference = _result(96, c1=2.3074e-5, c2=2.3066e-5, c3=2.5523e-9)
    prospective = _result(128, c1=2.1e-5, c2=2.0e-5, c3=2.0e-9)

    receipt = rs1.classify_resolution_pair(reference, prospective)

    assert receipt["resolution_stability_pass"] is True
    assert receipt["ratios"] == {"C1": None, "C2": None, "C3": None}
    assert receipt["outcome"] == "rs1_primary_mu_only_unsupported_indication"


def test_signature_mismatch_is_resolution_sensitive_and_unresolved() -> None:
    reference = _result(96, c1=2e-5, c2=6e-5, c3=2e-9)
    prospective = _result(128, c1=2e-5, c2=2e-5, c3=2e-9)

    receipt = rs1.classify_resolution_pair(reference, prospective)

    assert receipt["signatures_match"] is False
    assert receipt["resolution_stability_pass"] is False
    assert receipt["outcome"] == "rs1_resolution_sensitive_unresolved"


def test_above_floor_ratio_outside_frozen_interval_is_unresolved() -> None:
    reference = _result(96, c1=2e-4, c2=2e-5, c3=2e-9)
    prospective = _result(128, c1=5e-4, c2=2e-5, c3=2e-9)

    receipt = rs1.classify_resolution_pair(reference, prospective)

    assert receipt["signatures_match"] is True
    assert receipt["ratios"]["C1"] == 2.5
    assert receipt["ratios_pass"] is False
    assert receipt["outcome"] == "rs1_resolution_sensitive_unresolved"


def test_mu_candidate_reopens_only_when_both_sizes_pass_every_candidate_gate() -> None:
    reference = _result(96, c1=4e-4, c2=1e-4, c3=2e-4)
    prospective = _result(128, c1=5e-4, c2=1.2e-4, c3=2.5e-4)

    receipt = rs1.classify_resolution_pair(reference, prospective)

    assert receipt["resolution_stability_pass"] is True
    assert receipt["mu_zeroing_reduction"]["96"] == pytest.approx(0.75)
    assert receipt["mu_zeroing_reduction"]["128"] == pytest.approx(0.76)
    assert receipt["outcome"] == "rs1_primary_mu_candidate_reopened"


def test_valid_but_nonidentifying_pattern_remains_mixed() -> None:
    reference = _result(96, c1=2e-4, c2=1.5e-4, c3=1e-4)
    prospective = _result(128, c1=2.2e-4, c2=1.6e-4, c3=1.1e-4)

    receipt = rs1.classify_resolution_pair(reference, prospective)

    assert receipt["resolution_stability_pass"] is True
    assert receipt["mu_zeroing_reduction"]["96"] < 0.50
    assert receipt["mu_zeroing_reduction"]["128"] < 0.50
    assert receipt["outcome"] == "rs1_mixed_pattern_unresolved"


def test_invalid_lane_or_nonnull_c0_fails_closed() -> None:
    valid_reference = _result(96, c1=2e-5, c2=2e-5, c3=2e-9)
    invalid_prospective = _result(
        128,
        c1=2e-5,
        c2=2e-5,
        c3=2e-9,
        c0_phi=2e-12,
    )

    receipt = rs1.classify_resolution_pair(valid_reference, invalid_prospective)

    assert receipt["resolution_stability_pass"] is False
    assert receipt["outcome"] == "rs1_inconclusive_or_confounded"


def test_primary_orchestrator_requests_96_then_128_once_without_a_sweep(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[int] = []

    class FakeExecutionPolicy:
        @staticmethod
        def get_metadata() -> dict[str, str]:
            return {"execution_backend": "fake-non-scientific-test"}

    class FakeParent:
        @staticmethod
        def core_bindings() -> tuple[type[object], type[FakeExecutionPolicy], object]:
            return object, FakeExecutionPolicy, object()

    def fake_run_size(
        parent: Any,
        *,
        CoreConfig: type[Any],
        step_fn: Any,
        size: int,
    ) -> dict[str, Any]:
        del parent, CoreConfig, step_fn
        calls.append(size)
        return _result(size, c1=2e-5, c2=2e-5, c3=2e-9)

    monkeypatch.setattr(rs1, "verify_frozen_sources", lambda root: {"passed": True})
    monkeypatch.setattr(rs1, "strict_runtime_gate", lambda: {"passed": True})
    monkeypatch.setattr(rs1, "_load_parent_runner", lambda: FakeParent())
    monkeypatch.setattr(rs1, "run_size", fake_run_size)
    monkeypatch.setattr(rs1, "_git_head", lambda root: "frozen-test-head")
    monkeypatch.setattr(rs1, "source_sha256", lambda path: "frozen-test-sha256")

    result = rs1.run_primary()

    assert calls == [96, 128]
    assert list(result["size_results"]) == ["96", "128"]
    assert result["protocol"]["broad_or_adaptive_sweep"] is False
    assert result["classification"]["outcome"] == (
        "rs1_primary_mu_only_unsupported_indication"
    )
    assert result["evidence_boundary"]["independent_checker_run"] is False
