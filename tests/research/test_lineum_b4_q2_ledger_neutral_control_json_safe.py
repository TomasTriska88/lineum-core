from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WRAPPER_PATH = (
    ROOT / "research" / "runners" / "lineum_b4_q2_ledger_neutral_control_json_safe.py"
)
SPEC = importlib.util.spec_from_file_location("lineum_b4_q2_pv1b_json_safe", WRAPPER_PATH)
assert SPEC is not None and SPEC.loader is not None
safe = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = safe
SPEC.loader.exec_module(safe)


def test_nonfinite_diagnostics_become_json_null_only_at_serialization_boundary():
    source = {
        "finite": 1.25,
        "pos_inf": math.inf,
        "neg_inf": -math.inf,
        "nan": math.nan,
        "nested": [2.0, math.inf],
    }
    result = safe.sanitize_json_value(source)
    assert result == {
        "finite": 1.25,
        "pos_inf": None,
        "neg_inf": None,
        "nan": None,
        "nested": [2.0, None],
    }
    json.dumps(result, allow_nan=False)


def test_frozen_stage_schema_and_base_binding_are_unchanged():
    assert safe.STAGE == "Q2-PV1-B"
    assert safe.SCHEMA == "lineum-b4-q2-ledger-neutral-control/1"
    assert safe.BASE_RUNNER_GIT_BLOB == "cffa0cc87a070d6915606ab064ec3eee2d89a061"


def test_hash_is_defined_over_json_safe_representation():
    left = {"x": math.inf, "y": [1.0, math.nan]}
    right = {"x": None, "y": [1.0, None]}
    assert safe.canonical_payload_sha256(left) == safe.canonical_payload_sha256(right)
