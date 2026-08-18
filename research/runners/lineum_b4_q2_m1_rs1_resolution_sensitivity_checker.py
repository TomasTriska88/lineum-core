from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import statistics
import subprocess
from typing import Any, Mapping, Sequence


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PRIMARY_RELATIVE_PATH = (
    "research/lineum-public-tolog-b4/"
    "q2-m1-rs1-resolution-sensitivity.json"
)

CHECKER_ID = "Q2-M1-RS1-IC1"
PROTOCOL_ID = "Q2-M1-RS1"
LANES = ("C0", "C1", "C2", "C3")
CHANNELS = ("psi", "phi", "mu")
SIZES = (96, 128)
VARIANT_IDS = (12, 17)

CAUSAL_NULL_MAX = 1e-12
CAUSAL_FULL_ABS_FLOOR = 1e-4
CAUSAL_SINGLE_ABS_FLOOR = 5e-5
CAUSAL_ZEROING_REDUCTION_MIN = 0.50
SCALE_RATIO_MIN = 0.5
SCALE_RATIO_MAX = 2.0

EXPECTED_PRIMARY_CHECKOUT_BYTES = 13155
EXPECTED_PRIMARY_CHECKOUT_SHA256 = (
    "f1f43968bbd84de63568365371d9e1587a4feb9107020c4e143c466a77b78f2a"
)
EXPECTED_PRIMARY_GIT_BLOB = "d7f8b714dafbc1b5b98920a09f1b639ff16882c4"
EXPECTED_PRIMARY_CANONICAL_SHA256 = (
    "0598c14e59eccaa151b0437385ca677f5c86604b16280e6c51f8392e65cbef3f"
)
EXPECTED_PRIMARY_HEAD = "f14d431e3d54da0cbdb06a4ec64f0a48d806e3c0"
EXPECTED_PRIMARY_RUNNER_SHA256 = (
    "5c471bffb13b534a1de5fa774ba3b652a1ba357b239ecf60a3c12def5649be7a"
)
EXPECTED_PRIMARY_OUTCOME = "rs1_primary_mu_only_unsupported_indication"

EXPECTED_SOURCE_BLOBS = {
    "research/runners/lineum_b4_q2_mu_causal_reuse.py": (
        "8f818480b6b7160a49365b730bf884a4b94d9deb"
    ),
    "lineum_core/math.py": "bb877021810691223a0eb960a45493a2e351112a",
    "requirements.txt": "942f2b94b3d3f8c767451ae2d847a7b17c86d81e",
    "requirements-dev.txt": "7a0907e3e6c2d15400d19b536227a509910ae7e9",
}

EXPECTED_PROTOCOL = {
    "base_representative_params": [
        [12.0, 2.5, 0, 0],
        [12.0, 3.5, 0, 0],
    ],
    "base_size": 64,
    "broad_or_adaptive_sweep": False,
    "causal_full_abs_floor": CAUSAL_FULL_ABS_FLOOR,
    "causal_null_max": CAUSAL_NULL_MAX,
    "causal_single_abs_floor": CAUSAL_SINGLE_ABS_FLOOR,
    "causal_zeroing_reduction_min": CAUSAL_ZEROING_REDUCTION_MIN,
    "continuum_convergence_claim": False,
    "dt": 0.1,
    "echo_steps": 200,
    "execution_sizes": [96, 128],
    "imprint_steps": 120,
    "lanes": list(LANES),
    "representative_variant_ids": list(VARIANT_IDS),
    "scale_ratio_interval": [SCALE_RATIO_MIN, SCALE_RATIO_MAX],
    "seed": 20260804,
    "single_new_unobserved_size": 128,
    "source_off_steps": 2000,
}

EXPECTED_SIZE_GEOMETRY = {
    "96": {
        "size": 96,
        "scale_relative_to_n64": 1.5,
        "common_width": 7.5,
        "schedule": [[18.0, 3.75, 0, 0], [18.0, 5.25, 0, 0]],
    },
    "128": {
        "size": 128,
        "scale_relative_to_n64": 2.0,
        "common_width": 10.0,
        "schedule": [[24.0, 5.0, 0, 0], [24.0, 7.0, 0, 0]],
    },
}

EXPECTED_VALUES = {
    "96": {
        "C0": 0.0,
        "C1": 2.307400657646299e-05,
        "C2": 2.3065589896044145e-05,
        "C3": 2.5522854035019165e-09,
    },
    "128": {
        "C0": 0.0,
        "C1": 8.849683912246693e-06,
        "C2": 8.84787514935925e-06,
        "C3": 4.798573422491428e-10,
    },
}


class CheckFailure(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def _reject_nonfinite_json(value: str) -> Any:
    raise CheckFailure(f"non-finite JSON constant is forbidden: {value}")


def load_json_strict(path: Path) -> tuple[bytes, dict[str, Any]]:
    raw = path.read_bytes()
    try:
        decoded = json.loads(
            raw.decode("utf-8"),
            parse_constant=_reject_nonfinite_json,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CheckFailure(f"retained primary is not strict UTF-8 JSON: {exc}") from exc
    _require(isinstance(decoded, dict), "retained primary root must be an object")
    return raw, decoded


def canonical_payload_sha256_without_self(payload: Mapping[str, Any]) -> str:
    without_self = dict(payload)
    without_self.pop("canonical_payload_sha256_without_self", None)
    try:
        encoded = json.dumps(
            without_self,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise CheckFailure(f"payload cannot be canonically encoded: {exc}") from exc
    return hashlib.sha256(encoded).hexdigest()


def _git_identity(root: Path, arguments: Sequence[str], *, label: str) -> str:
    try:
        completed = subprocess.run(
            ["git", *arguments],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            encoding="ascii",
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        stderr = getattr(exc, "stderr", "") or ""
        detail = stderr.strip() or exc.__class__.__name__
        raise CheckFailure(f"Git identity failed for {label}: {detail}") from exc
    identity = completed.stdout.strip().lower()
    _require(
        len(identity) == 40
        and all(character in "0123456789abcdef" for character in identity),
        f"Git identity for {label} is not a SHA-1: {identity!r}",
    )
    return identity


def verify_primary_file_identity(
    path: Path,
    raw: bytes,
    *,
    root: Path = REPOSITORY_ROOT,
) -> dict[str, Any]:
    try:
        relative_path = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise CheckFailure("retained primary must be inside the repository") from exc
    _require(
        relative_path == PRIMARY_RELATIVE_PATH,
        f"unexpected retained-primary path: {relative_path}",
    )

    checkout_sha256 = hashlib.sha256(raw).hexdigest()
    _require(
        len(raw) == EXPECTED_PRIMARY_CHECKOUT_BYTES,
        f"checkout byte count changed: {len(raw)}",
    )
    _require(
        checkout_sha256 == EXPECTED_PRIMARY_CHECKOUT_SHA256,
        f"checkout SHA-256 changed: {checkout_sha256}",
    )

    filtered_blob = _git_identity(
        root,
        ["hash-object", f"--path={relative_path}", "--", relative_path],
        label="filtered retained primary",
    )
    head_blob = _git_identity(
        root,
        ["rev-parse", f"HEAD:{relative_path}"],
        label="HEAD retained primary",
    )
    _require(
        filtered_blob == EXPECTED_PRIMARY_GIT_BLOB,
        f"filtered retained-primary blob changed: {filtered_blob}",
    )
    _require(
        head_blob == EXPECTED_PRIMARY_GIT_BLOB,
        f"HEAD retained-primary blob changed: {head_blob}",
    )
    return {
        "path": relative_path,
        "checkout_bytes": len(raw),
        "checkout_sha256": checkout_sha256,
        "filtered_git_blob": filtered_blob,
        "head_git_blob": head_blob,
    }


def _mapping(value: Any, label: str) -> Mapping[str, Any]:
    _require(isinstance(value, Mapping), f"{label} must be an object")
    return value


def _finite_float(value: Any, label: str) -> float:
    _require(
        isinstance(value, (int, float)) and not isinstance(value, bool),
        f"{label} must be numeric",
    )
    converted = float(value)
    _require(math.isfinite(converted), f"{label} must be finite")
    _require(converted >= 0.0, f"{label} must be non-negative")
    return converted


def validate_protocol_and_sources(payload: Mapping[str, Any]) -> None:
    _require(payload.get("protocol_id") == PROTOCOL_ID, "protocol ID changed")
    _require(
        payload.get("stage")
        == "prospective_normalized_lattice_resolution_sensitivity",
        "stage changed",
    )
    _require(payload.get("empirically_connected") is False, "empirical boundary changed")
    _require(payload.get("protocol") == EXPECTED_PROTOCOL, "frozen protocol changed")

    runtime = _mapping(payload.get("runtime_gate"), "runtime_gate")
    _require(
        runtime
        == {
            "numpy_version": "1.26.4",
            "passed": True,
            "python_version": "3.11.15",
            "required_numpy": "1.26.4",
            "required_python": "3.11.15",
        },
        "runtime gate changed or did not pass",
    )

    source_gate = _mapping(payload.get("source_identity_gate"), "source_identity_gate")
    _require(source_gate.get("passed") is True, "primary source gate did not pass")
    _require(
        source_gate.get("method") == "git_filtered_worktree_and_head_blob",
        "primary source identity method changed",
    )
    for surface in ("expected", "actual", "head"):
        _require(
            source_gate.get(surface) == EXPECTED_SOURCE_BLOBS,
            f"primary source identity surface changed: {surface}",
        )

    environment = _mapping(payload.get("environment"), "environment")
    _require(
        environment.get("git_head") == EXPECTED_PRIMARY_HEAD,
        "primary execution commit changed",
    )
    _require(
        environment.get("runner_sha256") == EXPECTED_PRIMARY_RUNNER_SHA256,
        "primary runner checkout SHA-256 changed",
    )
    _require(environment.get("numpy") == "1.26.4", "primary NumPy changed")
    _require(
        isinstance(environment.get("python"), str)
        and environment["python"].startswith("3.11.15 "),
        "primary Python changed",
    )

    boundary = _mapping(payload.get("evidence_boundary"), "evidence_boundary")
    expected_boundary = {
        "normalized_lattice_sensitivity_only": True,
        "continuum_convergence_established": False,
        "retained_q2_m1_primary_reclassified": False,
        "independent_checker_run": False,
        "q2_rescue_tested": False,
        "physical_memory_field_established": False,
        "gravity_established": False,
        "quantum_memory_established": False,
        "consciousness_established": False,
        "cosmology_established": False,
    }
    _require(boundary == expected_boundary, "primary evidence boundary changed")


def recompute_size_result(label: str, result: Mapping[str, Any]) -> dict[str, Any]:
    _require(label in EXPECTED_SIZE_GEOMETRY, f"unexpected size label: {label}")
    expected_geometry = EXPECTED_SIZE_GEOMETRY[label]
    for field, expected in expected_geometry.items():
        _require(result.get(field) == expected, f"{label} geometry changed: {field}")
    _require(result.get("variant_ids") == list(VARIANT_IDS), f"{label} variants changed")
    _require(result.get("valid") is True, f"{label} primary validity did not pass")
    _require(
        result.get("validity")
        == {
            "c0_null_pass": True,
            "common_state_equal": True,
            "histories_valid": True,
            "lanes_valid": True,
        },
        f"{label} validity surface changed",
    )

    rows_by_lane = _mapping(result.get("causal_rows"), f"{label}.causal_rows")
    summaries = _mapping(result.get("causal_summary"), f"{label}.causal_summary")
    claimed_values = _mapping(result.get("values"), f"{label}.values")
    _require(set(rows_by_lane) == set(LANES), f"{label} row lanes changed")
    _require(set(summaries) == set(LANES), f"{label} summary lanes changed")
    _require(set(claimed_values) == set(LANES), f"{label} value lanes changed")

    recomputed_summaries: dict[str, dict[str, float]] = {}
    for lane in LANES:
        rows = rows_by_lane[lane]
        _require(isinstance(rows, list), f"{label}.{lane} rows must be a list")
        _require(len(rows) == len(VARIANT_IDS), f"{label}.{lane} row count changed")
        _require(
            [row.get("variant_id") for row in rows] == list(VARIANT_IDS),
            f"{label}.{lane} row variant IDs changed",
        )
        lane_channels: dict[str, list[float]] = {channel: [] for channel in CHANNELS}
        for index, row_value in enumerate(rows):
            row = _mapping(row_value, f"{label}.{lane}.row[{index}]")
            _require(row.get("valid") is True, f"{label}.{lane} contains invalid row")
            _require(
                row.get("common_state_equal") is True,
                f"{label}.{lane} common state differs",
            )
            divergences = _mapping(
                row.get("divergences"), f"{label}.{lane}.row[{index}].divergences"
            )
            _require(
                set(divergences) == set(CHANNELS),
                f"{label}.{lane} divergence channels changed",
            )
            for channel in CHANNELS:
                lane_channels[channel].append(
                    _finite_float(
                        divergences[channel],
                        f"{label}.{lane}.row[{index}].{channel}",
                    )
                )

        medians = {
            channel: float(statistics.median(lane_channels[channel]))
            for channel in CHANNELS
        }
        summary = _mapping(summaries[lane], f"{label}.{lane}.summary")
        _require(summary.get("valid") is True, f"{label}.{lane} summary is invalid")
        _require(
            summary.get("common_state_equal") is True,
            f"{label}.{lane} summary common state differs",
        )
        summary_medians = _mapping(
            summary.get("median_divergence"),
            f"{label}.{lane}.summary.median_divergence",
        )
        _require(
            set(summary_medians) == set(CHANNELS),
            f"{label}.{lane} summary channels changed",
        )
        for channel in CHANNELS:
            claimed_median = _finite_float(
                summary_medians[channel], f"{label}.{lane}.summary.{channel}"
            )
            _require(
                claimed_median == medians[channel],
                f"{label}.{lane}.{channel} median does not match retained rows",
            )
        recomputed_summaries[lane] = medians

    values = {
        lane: _finite_float(claimed_values[lane], f"{label}.values.{lane}")
        for lane in LANES
    }
    for lane in LANES:
        _require(
            values[lane] == recomputed_summaries[lane]["psi"],
            f"{label}.{lane} value does not match retained psi rows",
        )
    _require(values == EXPECTED_VALUES[label], f"{label} retained values changed")

    c0_channels_claimed = _mapping(
        result.get("c0_channel_divergences"),
        f"{label}.c0_channel_divergences",
    )
    _require(
        set(c0_channels_claimed) == set(CHANNELS),
        f"{label} C0 channels changed",
    )
    c0_channels = {
        channel: _finite_float(
            c0_channels_claimed[channel], f"{label}.c0_channel_divergences.{channel}"
        )
        for channel in CHANNELS
    }
    _require(
        c0_channels == recomputed_summaries["C0"],
        f"{label} C0 channels do not match retained rows",
    )
    return {
        "valid": True,
        "values": values,
        "c0_channel_divergences": c0_channels,
    }


def full_history_floor(d_null: float) -> float:
    return max(CAUSAL_FULL_ABS_FLOOR, 10.0 * d_null)


def single_channel_floor(d_null: float) -> float:
    return max(CAUSAL_SINGLE_ABS_FLOOR, 5.0 * d_null)


def zeroing_reduction(full_value: float, zeroed_value: float) -> float:
    if full_value <= 0.0:
        return 0.0
    return 1.0 - zeroed_value / full_value


def categorical_signature(result: Mapping[str, Any]) -> dict[str, bool]:
    values = _mapping(result.get("values"), "recomputed values")
    c0_channels = _mapping(
        result.get("c0_channel_divergences"), "recomputed C0 channels"
    )
    d_null = float(values["C0"])
    return {
        "C0": all(float(c0_channels[channel]) <= CAUSAL_NULL_MAX for channel in CHANNELS),
        "C1": float(values["C1"]) >= full_history_floor(d_null),
        "C2": float(values["C2"]) >= single_channel_floor(d_null),
        "C3": float(values["C3"]) >= single_channel_floor(d_null),
    }


def classify_resolution_pair(
    reference: Mapping[str, Any],
    prospective: Mapping[str, Any],
) -> dict[str, Any]:
    signatures = {
        "96": categorical_signature(reference),
        "128": categorical_signature(prospective),
    }
    signatures_match = signatures["96"] == signatures["128"]
    ratios: dict[str, float | None] = {}
    ratios_pass = True
    for lane in ("C1", "C2", "C3"):
        if signatures["96"][lane] and signatures["128"][lane]:
            ratio = float(prospective["values"][lane]) / float(
                reference["values"][lane]
            )
            ratios[lane] = ratio
            ratios_pass = ratios_pass and SCALE_RATIO_MIN <= ratio <= SCALE_RATIO_MAX
        else:
            ratios[lane] = None

    reference_valid = bool(reference.get("valid")) and signatures["96"]["C0"]
    prospective_valid = bool(prospective.get("valid")) and signatures["128"]["C0"]
    resolution_stability_pass = (
        reference_valid
        and prospective_valid
        and signatures_match
        and ratios_pass
    )
    reductions = {
        "96": zeroing_reduction(
            float(reference["values"]["C1"]), float(reference["values"]["C2"])
        ),
        "128": zeroing_reduction(
            float(prospective["values"]["C1"]),
            float(prospective["values"]["C2"]),
        ),
    }

    if not reference_valid or not prospective_valid:
        outcome = "rs1_inconclusive_or_confounded"
    elif not signatures_match or not ratios_pass:
        outcome = "rs1_resolution_sensitive_unresolved"
    elif not signatures["96"]["C3"] and not signatures["128"]["C3"]:
        outcome = "rs1_primary_mu_only_unsupported_indication"
    elif all(
        signature["C0"] and signature["C1"] and signature["C3"]
        for signature in signatures.values()
    ) and all(
        reduction >= CAUSAL_ZEROING_REDUCTION_MIN
        for reduction in reductions.values()
    ):
        outcome = "rs1_primary_mu_candidate_reopened"
    else:
        outcome = "rs1_mixed_pattern_unresolved"

    floors = {
        size: {
            "C0_max": CAUSAL_NULL_MAX,
            "C1": full_history_floor(float(result["values"]["C0"])),
            "C2": single_channel_floor(float(result["values"]["C0"])),
            "C3": single_channel_floor(float(result["values"]["C0"])),
        }
        for size, result in (("96", reference), ("128", prospective))
    }
    return {
        "outcome": outcome,
        "resolution_stability_pass": resolution_stability_pass,
        "signatures_match": signatures_match,
        "signatures": signatures,
        "floors": floors,
        "ratios": ratios,
        "ratios_pass": ratios_pass,
        "mu_zeroing_reduction": reductions,
    }


def recompute_and_compare(payload: Mapping[str, Any]) -> dict[str, Any]:
    validate_protocol_and_sources(payload)
    size_results = _mapping(payload.get("size_results"), "size_results")
    _require(set(size_results) == {"96", "128"}, "retained size set changed")
    recomputed_sizes = {
        label: recompute_size_result(label, _mapping(size_results[label], label))
        for label in ("96", "128")
    }
    recomputed = classify_resolution_pair(
        recomputed_sizes["96"], recomputed_sizes["128"]
    )

    claimed = _mapping(payload.get("classification"), "classification")
    for field in (
        "outcome",
        "resolution_stability_pass",
        "signatures_match",
        "signatures",
        "ratios",
        "ratios_pass",
        "mu_zeroing_reduction",
    ):
        _require(
            claimed.get(field) == recomputed[field],
            f"primary classification field disagrees with checker: {field}",
        )
    _require(
        recomputed["outcome"] == EXPECTED_PRIMARY_OUTCOME,
        f"unexpected primary outcome: {recomputed['outcome']}",
    )
    return {
        "values": {
            size: recomputed_sizes[size]["values"] for size in ("96", "128")
        },
        **recomputed,
    }


def check_retained_primary(
    path: Path,
    *,
    root: Path = REPOSITORY_ROOT,
) -> dict[str, Any]:
    raw, payload = load_json_strict(path)
    input_identity = verify_primary_file_identity(path, raw, root=root)
    claimed_canonical = payload.get("canonical_payload_sha256_without_self")
    recomputed_canonical = canonical_payload_sha256_without_self(payload)
    _require(
        claimed_canonical == EXPECTED_PRIMARY_CANONICAL_SHA256,
        "primary claimed canonical payload SHA-256 changed",
    )
    _require(
        recomputed_canonical == EXPECTED_PRIMARY_CANONICAL_SHA256,
        "primary canonical payload SHA-256 did not reproduce",
    )
    recomputed = recompute_and_compare(payload)
    post_read_sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
    _require(
        post_read_sha256 == input_identity["checkout_sha256"],
        "retained primary changed during checker read",
    )

    return {
        "checker_id": CHECKER_ID,
        "protocol_id": PROTOCOL_ID,
        "scope": {
            "retained_output_only": True,
            "primary_runner_imported": False,
            "trajectory_execution": False,
            "additional_resolution": False,
            "threshold_or_outcome_change": False,
        },
        "input_identity": {
            **input_identity,
            "canonical_payload_sha256_without_self": recomputed_canonical,
            "unchanged_after_read": True,
        },
        "recomputed": recomputed,
        "agreement": {
            "source_identity": True,
            "payload_identity": True,
            "row_medians": True,
            "lane_values": True,
            "signatures": True,
            "floors": True,
            "ratios": True,
            "mu_zeroing_reduction": True,
            "outcome_map": True,
            "primary_outcome": EXPECTED_PRIMARY_OUTCOME,
            "checker_outcome": recomputed["outcome"],
            "passed": True,
        },
        "scientific_status": "unsupported_under_rs1_tested_conditions",
        "evidence_boundary": {
            "normalized_lattice_sensitivity_only": True,
            "continuum_convergence_established": False,
            "retained_q2_m1_primary_reclassified": False,
            "direct_q2_established": False,
            "empirically_connected": False,
            "physical_memory_field_established": False,
            "lina_capability_established": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Independently check the retained Q2-M1-RS1 primary JSON"
    )
    parser.add_argument(
        "primary",
        nargs="?",
        type=Path,
        default=REPOSITORY_ROOT / PRIMARY_RELATIVE_PATH,
    )
    arguments = parser.parse_args()
    result = check_retained_primary(arguments.primary)
    encoded_without_self = json.dumps(
        result,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    result["canonical_payload_sha256_without_self"] = hashlib.sha256(
        encoded_without_self
    ).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
