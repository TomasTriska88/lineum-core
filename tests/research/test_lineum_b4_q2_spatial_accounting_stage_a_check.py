from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path

import numpy as np

PATH = Path(__file__).resolve().parents[2] / "research" / "runners" / "lineum_b4_q2_spatial_accounting_stage_a_check.py"
spec = importlib.util.spec_from_file_location("b4_sa_checker", PATH)
assert spec is not None and spec.loader is not None
check = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = check
spec.loader.exec_module(check)


def test_independent_diffuse_constant_field_is_zero():
    field = np.ones((2, 5, 5), dtype=np.complex128)
    kappa = np.ones((2, 5, 5), dtype=float)
    for stencil in check.STENCILS:
        assert np.array_equal(check.independent_diffuse(field, kappa, 0.05, stencil), np.zeros_like(field))


def test_independent_labels_cover_all_frozen_categories():
    common = dict(pre_local=10.0, pre_global=100.0, other_positive=0.0)
    assert check.independent_label(1e-9, 10.0, -1.0, 1.0, **common)["label"] == "unresolved_residual"
    assert check.independent_label(0.0, 10.0, -1.0, 9.0, **common)["label"] == "transport_accounted"
    assert check.independent_label(0.0, 9.0, -1.0, 9.0, **common)["label"] == "unpaired_source_dominated"
    assert check.independent_label(0.0, 10.0, 1.0, 1.0, **common)["label"] == "unpaired_source_dominated"
    assert check.independent_label(0.0, 0.0, 0.0, 0.0, **common)["label"] == "sink_or_dispersion_dominated"


def test_independent_near_return_uses_frozen_factor_two_bounds():
    row = {
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
    assert check.independent_near_return(row)
    row["phi_radial_profile_l2_error"] = 0.2000000001
    assert not check.independent_near_return(row)


def test_numeric_match_tolerance_is_frozen_and_tight():
    assert check.numeric_match(1e10, 1e10 + 0.005)[0]
    assert not check.numeric_match(1e10, 1e10 + 0.02)[0]
    assert check.COMPARE_RTOL == 1e-12
    assert check.COMPARE_ATOL == 1e-8


def test_checker_source_does_not_import_primary_measurement_paths():
    tree = ast.parse(PATH.read_text(encoding="utf-8"))
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module)
    assert not any("lineum_b4_q2_spatial_accounting" in name for name in imported)
    text = PATH.read_text(encoding="utf-8")
    assert "lineum_b4_q2_spatial_accounting.py" not in text
    assert "lineum_b4_q2_spatial_accounting_stage_a.py" not in text


def test_compare_rows_rejects_categorical_or_numeric_change():
    base = {
        "stencil": "LAP4",
        "lane": "L0",
        "pre": {"global_epsi": 1.0, "local_epsi": 1.0, "half_energy_radius": 1.0},
        "accounting": {
            "maximum_residual_ratio": 0.0,
            "positive_local_feedback": 1.0,
            "positive_local_phi_gradient_flow": 1.0,
            "positive_local_psi_diffusion": 0.0,
            "unpaired_positive": 2.0,
            "transport_positive": 0.0,
            "transport_global_signed": 0.0,
            "feedback_global_signed": 1.0,
            "phi_gradient_flow_global_signed": 1.0,
            "linear_dissipation_global_signed": -1.0,
            "mode_transfer_epsi_global_signed": -0.1,
            "mode_transfer_phi_global_signed": 0.1,
        },
        "mechanism": {"label": "unpaired_source_dominated", "transport_global_noncreating": True},
        "recovery": {
            "finite": True, "reset_free": True, "psi_cap_free": True, "phi_cap_free": True,
            "total_energy_relative_error": 0.1, "energy_radial_profile_l2_error": 0.2,
            "half_energy_radius_absolute_error": 2.0, "center_displacement_after": 1.0,
            "phi_radial_profile_l2_error": 0.2, "localized_psi_recovery": False,
            "localized_full_state_recovery": False,
        },
        "near_return": True,
    }
    primary = []
    checker = []
    for stencil in check.STENCILS:
        for lane in check.LANES:
            p = {k: (v.copy() if isinstance(v, dict) else v) for k, v in base.items()}
            p["stencil"] = stencil
            p["lane"] = lane.name
            p["pre"] = base["pre"].copy(); p["accounting"] = base["accounting"].copy(); p["mechanism"] = base["mechanism"].copy(); p["recovery"] = base["recovery"].copy()
            c = {k: (v.copy() if isinstance(v, dict) else v) for k, v in p.items()}
            c["pre"] = p["pre"].copy(); c["accounting"] = p["accounting"].copy(); c["mechanism"] = p["mechanism"].copy(); c["recovery"] = p["recovery"].copy()
            primary.append(p); checker.append(c)
    result = check.compare_rows(primary, checker)
    assert result["numeric_mismatch_count"] == 0
    assert result["categorical_mismatch_count"] == 0
    checker[0]["mechanism"]["label"] = "transport_accounted"
    checker[1]["accounting"]["positive_local_feedback"] += 1.0
    result = check.compare_rows(primary, checker)
    assert result["numeric_mismatch_count"] == 1
    assert result["categorical_mismatch_count"] >= 1
