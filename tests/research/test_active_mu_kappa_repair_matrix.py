from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

SCRIPT_PATH = (
    Path(__file__).resolve().parents[2]
    / "scripts"
    / "research"
    / "active_mu_kappa_repair_matrix.py"
)
SPEC = importlib.util.spec_from_file_location(
    "active_mu_kappa_repair_matrix", SCRIPT_PATH
)
assert SPEC is not None and SPEC.loader is not None
matrix = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = matrix
SPEC.loader.exec_module(matrix)


def test_geometry_preserves_mean_and_valid_range():
    for contrast in (0.25, 0.40):
        geometry = matrix.build_geometry(32, contrast)
        assert np.mean(geometry["structured"]) == 0.55
        assert np.all(geometry["structured"] > 0.0)
        assert np.all(geometry["structured"] <= 1.0)
        assert np.count_nonzero(geometry["damage"]) == 45


def test_recovery_metric_toy_signs_are_frozen():
    assert matrix.toy_metric_check() == {
        "half_recovery": 0.5,
        "negative_recovery": -0.125,
    }


def test_matrix_is_exactly_repeatable_and_has_no_supportive_cell():
    first = matrix.run_matrix()
    second = matrix.run_matrix()
    assert json.dumps(first, sort_keys=True) == json.dumps(
        second, sort_keys=True
    )
    assert first["supportive_cells"] == []
    assert not first["combined_supported_in_any_cell"]
    assert len(first["cells"]) == 8


def test_mu_is_negligible_and_kappa_effect_is_bounded_positive():
    result = matrix.run_matrix()
    mu_effects = []
    kappa_effects = []
    for cell in result["cells"]:
        lanes = {lane["lane"]: lane for lane in cell["lanes"]}
        mu_effects.extend(
            [
                lanes["Y1S0"]["recovery_fraction"]
                - lanes["YS00"]["recovery_fraction"],
                lanes["Y1S1"]["recovery_fraction"]
                - lanes["Y0S1"]["recovery_fraction"],
            ]
        )
        kappa_effects.extend(
            [
                lanes["Y0S1"]["recovery_fraction"]
                - lanes["YS00"]["recovery_fraction"],
                lanes["Y1S1"]["recovery_fraction"]
                - lanes["Y1S0"]["recovery_fraction"],
            ]
        )
    assert max(abs(value) for value in mu_effects) == (
        4.216379362752265e-05
    )
    assert all(value < 0.0 for value in mu_effects)
    assert min(kappa_effects) > 0.011
    assert max(kappa_effects) == 0.024091442639686052


def test_all_cells_remain_finite_without_fail_safe_reset():
    result = matrix.run_matrix()
    for cell in result["cells"]:
        for lane in cell["lanes"]:
            assert lane["repair_validation"]["finite"]
            assert not lane["repair_validation"][
                "possible_fail_safe_reset"
            ]
            assert lane["repair_validation"]["max_abs_psi"] < 0.142
            assert lane["removal_validation"]["finite"]
            assert not lane["removal_validation"][
                "possible_fail_safe_reset"
            ]
