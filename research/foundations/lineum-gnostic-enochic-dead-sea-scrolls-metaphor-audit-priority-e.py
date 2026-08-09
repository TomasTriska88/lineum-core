import json
import platform
import sys

TOL = 1e-12
LEVELS = ("snapshot", "finite_history", "relational", "source_aware", "generative")


def make_case(name, x_prev, x_now, relation, source_gain, intervention, a, calibration=None):
    return {
        "name": name,
        "x_prev": float(x_prev),
        "x_now": float(x_now),
        "relation": float(relation),
        "source_gain": float(source_gain),
        "intervention": float(intervention),
        "a": float(a),
        "calibration": calibration,
    }


def future(case):
    v_now = case["x_now"] - case["x_prev"]
    v_next = (
        case["a"] * v_now
        + case["relation"]
        + case["source_gain"] * case["intervention"]
    )
    return case["x_now"] + v_next


def infer_a(calibration, clip_cap=None):
    xm1, x0, x1, relation, source_gain, intervention = calibration
    if clip_cap is not None:
        def clip(x):
            return max(-clip_cap, min(clip_cap, x))
        xm1, x0, x1 = clip(xm1), clip(x0), clip(x1)
    v0 = x0 - xm1
    v1 = x1 - x0
    if abs(v0) <= TOL:
        raise ValueError("calibration velocity must be nonzero")
    return (v1 - relation - source_gain * intervention) / v0


def observer_key(case, level, clip_cap=None):
    idx = LEVELS.index(level)
    key = [case["x_now"]]
    if idx >= 1:
        key = [case["x_prev"], case["x_now"]]
    if idx >= 2:
        key.append(case["relation"])
    if idx >= 3:
        key.extend([case["source_gain"], case["intervention"]])
    if idx >= 4:
        if case["calibration"] is None:
            raise ValueError("generative observer requires calibration record")
        key.append(infer_a(case["calibration"], clip_cap=clip_cap))
    return tuple(key)


def same_key(a, b, level, clip_cap=None):
    ka = observer_key(a, level, clip_cap=clip_cap)
    kb = observer_key(b, level, clip_cap=clip_cap)
    return len(ka) == len(kb) and all(abs(x-y) <= TOL for x, y in zip(ka, kb))


def minimal_resolving_level(a, b, clip_cap=None):
    for level in LEVELS:
        if not same_key(a, b, level, clip_cap=clip_cap):
            return level
    return None


def calibration_for(a):
    # Calibration uses a unit incoming velocity, no relation, and no source pulse.
    # The held-out challenge later uses a source pulse of opposite context.
    xm1 = 0.0
    x0 = 1.0
    relation = 0.0
    source_gain = 0.0
    intervention = 0.0
    v0 = x0 - xm1
    v1 = a * v0 + relation + source_gain * intervention
    x1 = x0 + v1
    return (xm1, x0, x1, relation, source_gain, intervention)


PAIRS = {
    "H_history": (
        make_case("H_plus", -1.0, 0.0, 0.0, 0.0, 0.0, 1.0, calibration_for(1.0)),
        make_case("H_minus", 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, calibration_for(1.0)),
    ),
    "R_relation": (
        make_case("R_plus", 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, calibration_for(1.0)),
        make_case("R_minus", 0.0, 0.0, -1.0, 0.0, 0.0, 1.0, calibration_for(1.0)),
    ),
    "S_source": (
        make_case("S_on", 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, calibration_for(1.0)),
        make_case("S_off", 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, calibration_for(1.0)),
    ),
    "G_generative": (
        make_case("G_pos", -1.0, 0.0, 0.0, 1.0, 0.25, 0.5, calibration_for(0.5)),
        make_case("G_neg", -1.0, 0.0, 0.0, 1.0, 0.25, -0.5, calibration_for(-0.5)),
    ),
}

EXPECTED_MIN = {
    "H_history": "finite_history",
    "R_relation": "relational",
    "S_source": "source_aware",
    "G_generative": "generative",
}


def pair_result(name, pair):
    a, b = pair
    fa, fb = future(a), future(b)
    return {
        "future": [fa, fb],
        "future_gap": abs(fa-fb),
        "collision_by_level": {level: same_key(a, b, level) for level in LEVELS},
        "minimal_resolving_level": minimal_resolving_level(a, b),
        "unavoidable_worst_case_error_lower_bound_when_colliding": abs(fa-fb) / 2.0,
    }


def generative_prediction(case, calibration=None, clip_cap=None):
    cal = case["calibration"] if calibration is None else calibration
    a_hat = infer_a(cal, clip_cap=clip_cap)
    v_now = case["x_now"] - case["x_prev"]
    v_next = (
        a_hat * v_now
        + case["relation"]
        + case["source_gain"] * case["intervention"]
    )
    return case["x_now"] + v_next, a_hat


def reverse_calibration(cal):
    xm1, x0, x1, relation, source_gain, intervention = cal
    return (x1, x0, xm1, relation, source_gain, intervention)


def translated_case(case, offset):
    cal = case["calibration"]
    if cal is not None:
        xm1, x0, x1, relation, source_gain, intervention = cal
        cal = (
            xm1 + offset,
            x0 + offset,
            x1 + offset,
            relation,
            source_gain,
            intervention,
        )
    return make_case(
        case["name"] + "_translated",
        case["x_prev"] + offset,
        case["x_now"] + offset,
        case["relation"],
        case["source_gain"],
        case["intervention"],
        case["a"],
        cal,
    )


PAIR_RESULTS = {name: pair_result(name, pair) for name, pair in PAIRS.items()}

g_pair = PAIRS["G_generative"]
g_preds = []
g_reversed_errors = []
g_a_errors = []
for case in g_pair:
    pred, a_hat = generative_prediction(case)
    g_preds.append({"name": case["name"], "prediction": pred, "truth": future(case), "a_hat": a_hat})
    g_a_errors.append(abs(a_hat-case["a"]))
    rpred, _ = generative_prediction(case, calibration=reverse_calibration(case["calibration"]))
    g_reversed_errors.append(abs(rpred-future(case)))

CLIP_CAP = 1.25
clip_pair = (
    make_case("C_a15", -1.0, 0.0, 0.0, 0.0, 0.0, 1.5, calibration_for(1.5)),
    make_case("C_a20", -1.0, 0.0, 0.0, 0.0, 0.0, 2.0, calibration_for(2.0)),
)
clip_true = [future(c) for c in clip_pair]
clip_hats = [infer_a(c["calibration"], clip_cap=CLIP_CAP) for c in clip_pair]
clip_collision = same_key(clip_pair[0], clip_pair[1], "generative", clip_cap=CLIP_CAP)
clip_gap = abs(clip_true[0]-clip_true[1])

OFFSET = 7.25
translated_g = tuple(translated_case(c, OFFSET) for c in g_pair)
translation_gap_delta = abs(
    abs(future(translated_g[0])-future(translated_g[1]))
    - PAIR_RESULTS["G_generative"]["future_gap"]
)
translation_a_delta = max(
    abs(infer_a(translated_g[i]["calibration"]) - infer_a(g_pair[i]["calibration"]))
    for i in range(2)
)
translation_prediction_shift_error = max(
    abs(
        generative_prediction(translated_g[i])[0]
        - (generative_prediction(g_pair[i])[0] + OFFSET)
    )
    for i in range(2)
)

checks = {
    "history_resolves_snapshot_collision": (
        PAIR_RESULTS["H_history"]["collision_by_level"]["snapshot"]
        and PAIR_RESULTS["H_history"]["future_gap"] >= 1.5
        and PAIR_RESULTS["H_history"]["minimal_resolving_level"] == "finite_history"
    ),
    "relation_resolves_history_collision": (
        PAIR_RESULTS["R_relation"]["collision_by_level"]["finite_history"]
        and PAIR_RESULTS["R_relation"]["future_gap"] >= 1.5
        and PAIR_RESULTS["R_relation"]["minimal_resolving_level"] == "relational"
    ),
    "source_resolves_relational_collision": (
        PAIR_RESULTS["S_source"]["collision_by_level"]["relational"]
        and PAIR_RESULTS["S_source"]["future_gap"] >= 0.5
        and PAIR_RESULTS["S_source"]["minimal_resolving_level"] == "source_aware"
    ),
    "generative_model_resolves_source_aware_collision": (
        PAIR_RESULTS["G_generative"]["collision_by_level"]["source_aware"]
        and PAIR_RESULTS["G_generative"]["future_gap"] >= 0.9
        and PAIR_RESULTS["G_generative"]["minimal_resolving_level"] == "generative"
        and max(g_a_errors) <= TOL
        and max(abs(row["prediction"]-row["truth"]) for row in g_preds) <= TOL
    ),
    "temporal_order_matters_for_model_reconstruction": min(g_reversed_errors) >= 1.0,
    "noninjective_clipping_remains_nonidentifying": (
        clip_collision
        and abs(clip_hats[0]-clip_hats[1]) <= TOL
        and clip_gap >= 0.4
        and clip_gap/2.0 >= 0.2
    ),
    "global_translation_is_nonidentifying": (
        translation_gap_delta <= TOL
        and translation_a_delta <= TOL
        and translation_prediction_shift_error <= TOL
    ),
    "nested_minimal_levels_match_preregistration": all(
        PAIR_RESULTS[name]["minimal_resolving_level"] == expected
        for name, expected in EXPECTED_MIN.items()
    ),
}

output = {
    "python": sys.version.split()[0],
    "platform": platform.platform(),
    "parameters": {
        "levels": LEVELS,
        "tolerance": TOL,
        "held_out_generative_intervention": 0.25,
        "clipping_control_cap": CLIP_CAP,
        "translation_offset": OFFSET,
        "randomness": None,
    },
    "plant": {
        "v_now": "x_now - x_prev",
        "v_next": "a*v_now + relation + source_gain*intervention",
        "x_next": "x_now + v_next",
    },
    "pair_results": PAIR_RESULTS,
    "generative_predictions": g_preds,
    "generative_a_max_error": max(g_a_errors),
    "reversed_calibration_prediction_errors": g_reversed_errors,
    "clipping_control": {
        "true_futures": clip_true,
        "future_gap": clip_gap,
        "clipped_a_hats": clip_hats,
        "generative_key_collision": clip_collision,
        "deterministic_predictor_minimax_error_lower_bound": clip_gap / 2.0,
    },
    "translation_audit": {
        "future_gap_delta": translation_gap_delta,
        "a_hat_delta": translation_a_delta,
        "prediction_shift_error": translation_prediction_shift_error,
    },
    "checks": checks,
    "overall_pass": all(checks.values()),
}
print(json.dumps(output, indent=2, sort_keys=True))
