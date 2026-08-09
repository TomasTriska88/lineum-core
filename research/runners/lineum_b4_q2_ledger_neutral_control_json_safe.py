from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path
from typing import Any

BASE_RUNNER_GIT_BLOB = "cffa0cc87a070d6915606ab064ec3eee2d89a061"
STAGE = "Q2-PV1-B"
SCHEMA = "lineum-b4-q2-ledger-neutral-control/1"


def _load_base() -> Any:
    path = Path(__file__).with_name("lineum_b4_q2_ledger_neutral_control.py")
    spec = importlib.util.spec_from_file_location("lineum_b4_q2_pv1b_frozen_base", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load frozen Q2 PV1-B base runner from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sanitize_json_value(value: Any) -> Any:
    if isinstance(value, float):
        return value if math.isfinite(value) else None
    if isinstance(value, dict):
        return {key: sanitize_json_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [sanitize_json_value(item) for item in value]
    if isinstance(value, tuple):
        return [sanitize_json_value(item) for item in value]
    return value


def canonical_payload_sha256(payload: dict[str, Any]) -> str:
    sanitized = sanitize_json_value(payload)
    encoded = json.dumps(
        sanitized,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def run_json_safe() -> dict[str, Any]:
    base = _load_base()
    if base.STAGE != STAGE or base.SCHEMA != SCHEMA:
        raise RuntimeError("Frozen Q2 PV1-B base stage/schema mismatch")
    base._canonical_payload_sha256 = canonical_payload_sha256
    payload = base.run()
    sanitized = sanitize_json_value(payload)
    if sanitized["stage"] != STAGE or sanitized["schema"] != SCHEMA:
        raise RuntimeError("Sanitized Q2 PV1-B stage/schema mismatch")
    expected_hash = sanitized.pop("canonical_payload_sha256_without_self")
    observed_hash = canonical_payload_sha256(sanitized)
    if observed_hash != expected_hash:
        raise RuntimeError(
            "JSON-safe serialization changed the frozen payload hash unexpectedly"
        )
    sanitized["canonical_payload_sha256_without_self"] = expected_hash
    return sanitized


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Serialize the frozen B4 Q2 PV1-B control with non-finite diagnostics "
            "represented as JSON null without changing scientific classifications."
        )
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = run_json_safe()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload["summary"], sort_keys=True, allow_nan=False))
    return (
        0
        if payload["summary"]["outcome"] != "technical_or_methodological_failure"
        else 2
    )


if __name__ == "__main__":
    raise SystemExit(main())
