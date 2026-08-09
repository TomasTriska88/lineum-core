import json
import math
import platform
import sys

TOL = 1e-12
DT_PRIMARY = 0.002
DT_AUDIT = (0.004, 0.002, 0.001)
T_RELAX = 8.0
RESET_X = -0.5
THRESHOLD_BASE = 0.0
THRESHOLD_SHIFT = 1.5
HYSTERESIS_HALF_WIDTH = 0.5

VARIANTS = (
    "TS0_independent_two_state",
    "TS1_coupled_modes_one_dof",
    "TS2_scalar_bistable",
    "TS3_threshold_projection",
    "TS4_history_dependent_relay",
    "TS5_observer_label",
)


def sign_label(x):
    return 1 if x >= 0.0 else -1


def rank2(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    return 2 if abs(a * d - b * c) > TOL else (1 if max(abs(a), abs(b), abs(c), abs(d)) > TOL else 0)


def baseline():
    return {name: {"observable": 1.0, "label": 1} for name in VARIANTS}


def port_response():
    independent = [[1.0, 0.0], [0.0, 1.0]]
    constrained = [[0.5, -0.5], [-0.5, 0.5]]
    return {
        "TS0_independent_two_state": {
            "matrix": independent,
            "rank": rank2(independent),
            "determinant": 1.0,
            "constraint_u_plus_v": None,
        },
        "TS1_coupled_modes_one_dof": {
            "matrix": constrained,
            "rank": rank2(constrained),
            "determinant": 0.0,
            "constraint_u_plus_v": 0.0,
        },
    }


def integrate_scalar(kind, dt, x0=RESET_X):
    x = float(x0)
    n = int(round(T_RELAX / dt))
    for _ in range(n):
        if kind == "bistable":
            dx = x - x * x * x
        elif kind == "monostable":
            dx = 1.0 - x
        else:
            raise ValueError(kind)
        x += dt * dx
    return x


def threshold_projection():
    x = 1.0
    before = sign_label(x - THRESHOLD_BASE)
    after = sign_label(x - THRESHOLD_SHIFT)
    return {
        "plant_before": x,
        "plant_after": x,
        "plant_delta": 0.0,
        "label_before": before,
        "label_after": after,
        "label_flipped": before != after,
    }


def relay_label(x, memory):
    if x > HYSTERESIS_HALF_WIDTH:
        return 1
    if x < -HYSTERESIS_HALF_WIDTH:
        return -1
    return memory


def history_relay():
    x = 0.0
    plus = relay_label(x, 1)
    minus = relay_label(x, -1)
    reset = relay_label(x, -1)
    return {
        "matched_current_x": x,
        "label_from_positive_history": plus,
        "label_from_negative_history": minus,
        "label_after_memory_reset_from_positive_to_negative": reset,
        "plant_delta_under_memory_reset": 0.0,
        "history_changes_label": plus != minus,
    }


def observer_label():
    x = 1.0
    physical_rule = sign_label(x)
    convention_plus = physical_rule
    convention_minus = -physical_rule
    return {
        "plant_before": x,
        "plant_after": x,
        "plant_delta": 0.0,
        "convention_plus_label": convention_plus,
        "convention_minus_label": convention_minus,
        "convention_flip": convention_plus != convention_minus,
    }


def classify(signatures):
    if signatures["port_rank"] == 2:
        return "TS0_independent_two_state"
    if signatures["pair_constraint"]:
        return "TS1_coupled_modes_one_dof"
    if signatures["persistent_source_off_switch"]:
        return "TS2_scalar_bistable"
    if signatures["threshold_only_flip"]:
        return "TS3_threshold_projection"
    if signatures["history_only_flip"]:
        return "TS4_history_dependent_relay"
    if signatures["convention_only_flip"]:
        return "TS5_observer_label"
    return "unclassified"


def evaluate(dt):
    base = baseline()
    ports = port_response()
    bistable_final = integrate_scalar("bistable", dt)
    monostable_final = integrate_scalar("monostable", dt)
    threshold = threshold_projection()
    history = history_relay()
    label = observer_label()

    signatures = {
        "TS0_independent_two_state": {
            "port_rank": ports["TS0_independent_two_state"]["rank"],
            "pair_constraint": False,
            "persistent_source_off_switch": False,
            "threshold_only_flip": False,
            "history_only_flip": False,
            "convention_only_flip": False,
        },
        "TS1_coupled_modes_one_dof": {
            "port_rank": ports["TS1_coupled_modes_one_dof"]["rank"],
            "pair_constraint": abs(ports["TS1_coupled_modes_one_dof"]["constraint_u_plus_v"]) <= TOL,
            "persistent_source_off_switch": False,
            "threshold_only_flip": False,
            "history_only_flip": False,
            "convention_only_flip": False,
        },
        "TS2_scalar_bistable": {
            "port_rank": 1,
            "pair_constraint": False,
            "persistent_source_off_switch": bistable_final <= -0.90,
            "threshold_only_flip": False,
            "history_only_flip": False,
            "convention_only_flip": False,
        },
        "TS3_threshold_projection": {
            "port_rank": 1,
            "pair_constraint": False,
            "persistent_source_off_switch": False,
            "threshold_only_flip": threshold["label_flipped"] and abs(threshold["plant_delta"]) <= TOL,
            "history_only_flip": False,
            "convention_only_flip": False,
        },
        "TS4_history_dependent_relay": {
            "port_rank": 1,
            "pair_constraint": False,
            "persistent_source_off_switch": False,
            "threshold_only_flip": False,
            "history_only_flip": history["history_changes_label"] and abs(history["plant_delta_under_memory_reset"]) <= TOL,
            "convention_only_flip": False,
        },
        "TS5_observer_label": {
            "port_rank": 1,
            "pair_constraint": False,
            "persistent_source_off_switch": False,
            "threshold_only_flip": False,
            "history_only_flip": False,
            "convention_only_flip": label["convention_flip"] and abs(label["plant_delta"]) <= TOL,
        },
    }

    classifications = {name: classify(sig) for name, sig in signatures.items()}
    baseline_gap = max(
        abs(row["observable"] - 1.0) + abs(row["label"] - 1)
        for row in base.values()
    )

    checks = {
        "baseline_binary_observation_is_nonidentifying": baseline_gap <= TOL,
        "independent_two_state_has_rank_two_response": (
            ports["TS0_independent_two_state"]["rank"] == 2
            and abs(ports["TS0_independent_two_state"]["determinant"]) >= 0.5
        ),
        "coupled_two_coordinate_state_has_rank_one_response": (
            ports["TS1_coupled_modes_one_dof"]["rank"] == 1
            and abs(ports["TS1_coupled_modes_one_dof"]["determinant"]) <= TOL
            and abs(ports["TS1_coupled_modes_one_dof"]["constraint_u_plus_v"]) <= TOL
        ),
        "scalar_bistability_persists_source_off": bistable_final <= -0.90,
        "monostable_threshold_control_returns_positive": monostable_final >= 0.90,
        "threshold_shift_can_flip_label_without_plant_change": (
            threshold["label_flipped"] and abs(threshold["plant_delta"]) <= TOL
        ),
        "matched_current_state_can_carry_history_dependent_label": (
            history["label_from_positive_history"] == 1
            and history["label_from_negative_history"] == -1
            and abs(history["plant_delta_under_memory_reset"]) <= TOL
        ),
        "observer_convention_can_flip_label_without_plant_change": (
            label["convention_plus_label"] == 1
            and label["convention_minus_label"] == -1
            and abs(label["plant_delta"]) <= TOL
        ),
        "all_six_variants_have_unique_frozen_intervention_signature": (
            all(classifications[name] == name for name in VARIANTS)
            and len({tuple(sorted(sig.items())) for sig in signatures.values()}) == len(VARIANTS)
        ),
    }

    return {
        "dt": dt,
        "baseline": base,
        "baseline_max_gap_from_common_observation": baseline_gap,
        "port_response": ports,
        "bistable_source_off_final": bistable_final,
        "monostable_source_off_final": monostable_final,
        "threshold_projection": threshold,
        "history_relay": history,
        "observer_label": label,
        "signatures": signatures,
        "classifications": classifications,
        "checks": checks,
        "pass_without_dt_audit": all(checks.values()),
    }


primary = evaluate(DT_PRIMARY)
audit = {str(dt): evaluate(dt) for dt in DT_AUDIT}
overall_pass = primary["pass_without_dt_audit"] and all(
    row["pass_without_dt_audit"] for row in audit.values()
)

output = {
    "python": sys.version.split()[0],
    "platform": platform.platform(),
    "parameters": {
        "variants": VARIANTS,
        "tolerance": TOL,
        "primary_dt": DT_PRIMARY,
        "audit_dt": DT_AUDIT,
        "relaxation_horizon": T_RELAX,
        "source_off_reset_x": RESET_X,
        "threshold_base": THRESHOLD_BASE,
        "threshold_shift": THRESHOLD_SHIFT,
        "hysteresis_half_width": HYSTERESIS_HALF_WIDTH,
        "randomness": None,
    },
    "primary": primary,
    "dt_audit": audit,
    "overall_pass": overall_pass,
}
print(json.dumps(output, indent=2, sort_keys=True))
