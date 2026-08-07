from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "research" / "runners" / "lineum_b4_q2_spatial_accounting_stage_a.py"
spec = importlib.util.spec_from_file_location("stage_a", PATH)
assert spec is not None and spec.loader is not None
stage_a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stage_a)


def test_closure_ratio_uses_frozen_scale():
    assert stage_a.closure_ratio(1e-11, 0.0, 0.0) == 1e-11
    assert stage_a.closure_ratio(1.0, 100.0, 10.0) == 0.01


def test_mechanism_classification_is_frozen():
    common = dict(pre_local_epsi=10.0, pre_global_epsi=100.0, other_positive=0.0)
    assert stage_a.classify_mechanism(1e-9, 10.0, -1.0, 1.0, **common)["label"] == "unresolved_residual"
    assert stage_a.classify_mechanism(0.0, 10.0, -1.0, 9.0, **common)["label"] == "transport_accounted"
    assert stage_a.classify_mechanism(0.0, 9.0, -1.0, 9.0, **common)["label"] == "unpaired_source_dominated"
    assert stage_a.classify_mechanism(0.0, 10.0, 1.0, 1.0, **common)["label"] == "unpaired_source_dominated"
    assert stage_a.classify_mechanism(0.0, 0.0, 0.0, 0.0, **common)["label"] == "sink_or_dispersion_dominated"


def test_near_return_is_exactly_factor_two_diagnostic():
    metrics = {
        "finite": True,
        "reset_free": True,
        "psi_cap_free": True,
        "phi_cap_free": True,
        "total_energy_relative_error": 0.10,
        "energy_radial_profile_l2_error": 0.20,
        "half_energy_radius_absolute_error": 2.0,
        "center_displacement_after": 1.0,
        "phi_radial_profile_l2_error": 0.20,
    }
    assert stage_a.near_return(metrics)
    metrics["phi_radial_profile_l2_error"] = 0.2000000001
    assert not stage_a.near_return(metrics)


def test_stage_b_requires_same_lane_both_stencils():
    rows = []
    for stencil in stage_a.STENCILS:
        rows.append({"lane": "S1", "stencil": stencil, "mechanism": {"label": "transport_accounted"}, "near_return": True})
        rows.append({"lane": "S2", "stencil": stencil, "mechanism": {"label": "unpaired_source_dominated"}, "near_return": True})
    assert stage_a.stage_b_candidates(rows) == ["S1"]
    rows[-4]["near_return"] = False
    assert stage_a.stage_b_candidates(rows) == []


def test_protocol_constants_are_the_preregistered_values():
    assert stage_a.CLOSURE_RTOL == 1e-10
    assert stage_a.POSITIVE_RTOL == 1e-12
    assert stage_a.NEAR_RETURN_FACTOR == 2.0
    assert stage_a.LANE_NAMES == ("L0", "S1", "S2", "S3")
    assert stage_a.STENCILS == ("LAP4", "LAP8")
