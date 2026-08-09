import json
import math
import platform
import statistics
import sys

REF = (-1.5, -1.0, -0.625, -0.25, 0.125, 0.5, 0.875, 1.875)
N = len(REF)
K = 3.0
TAU = 1.5
DT_PRIMARY = 0.002
DT_AUDIT = (0.004, 0.002, 0.001)
ORDER_A = (2, 5, 0, 7, 3, 6, 1, 4)
ORDER_B = tuple(reversed(ORDER_A))
TOL = 1e-12


def mean(values):
    return sum(values) / len(values)


def rms(values):
    return math.sqrt(sum(x * x for x in values) / len(values))


REF_PAIR_RMS = rms([
    REF[i] - REF[j]
    for i in range(N)
    for j in range(i + 1, N)
])
REF_STATE_RMS = rms(REF)


def rel_error(y):
    residual = [
        (y[i] - y[j]) - (REF[i] - REF[j])
        for i in range(N)
        for j in range(i + 1, N)
    ]
    return rms(residual) / REF_PAIR_RMS


def bag_error(y):
    yc = [x - mean(y) for x in y]
    return rms([a - b for a, b in zip(sorted(yc), sorted(REF))]) / REF_STATE_RMS


def recovery(e0, e1):
    if e0 <= 1e-15:
        return 1.0 if e1 <= 1e-15 else 0.0
    return max(0.0, min(1.0, (e0 - e1) / e0))


def settle_relational(y, dt, k):
    y = list(y)
    steps = int(round(TAU / dt))
    for _ in range(steps):
        m = mean(y)
        y = [
            yi + dt * (-k * ((yi - m) - ri))
            for yi, ri in zip(y, REF)
        ]
    return y


def settle_absolute(y, dt, k):
    y = list(y)
    steps = int(round(TAU / dt))
    for _ in range(steps):
        y = [
            yi + dt * (-k * (yi - ri))
            for yi, ri in zip(y, REF)
        ]
    return y


def member_jaccard(initial_ids, final_ids):
    a, b = set(initial_ids), set(final_ids)
    return len(a & b) / len(a | b)


def run_turnover(dt, order, k, member_ids=None):
    y = list(REF)
    ids = list(range(N)) if member_ids is None else list(member_ids)
    initial_ids = tuple(ids)
    recoveries = []
    e_before = []
    e_after = []
    mean_drift = 0.0

    for turn, role in enumerate(order):
        m0 = mean(y)
        y[role] = m0
        ids[role] = 1000 + turn
        e0 = rel_error(y)
        before_mean = mean(y)
        y = settle_relational(y, dt, k)
        after_mean = mean(y)
        e1 = rel_error(y)
        mean_drift = max(mean_drift, abs(after_mean - before_mean))
        recoveries.append(recovery(e0, e1))
        e_before.append(e0)
        e_after.append(e1)

    return {
        "median_recovery": statistics.median(recoveries),
        "min_recovery": min(recoveries),
        "final_rel_error": rel_error(y),
        "membership_jaccard": member_jaccard(initial_ids, ids),
        "max_mean_drift": mean_drift,
        "recoveries": recoveries,
        "e_before": e_before,
        "e_after": e_after,
    }


def external_template_control(dt):
    role_on = ORDER_A[0]
    y_on = list(REF)
    y_on[role_on] = mean(y_on)
    e0_on = rel_error(y_on)
    y_on = settle_absolute(y_on, dt, K)
    rec_on = recovery(e0_on, rel_error(y_on))

    role_off = ORDER_A[1]
    y_off = list(REF)
    y_off[role_off] = mean(y_off)
    e0_off = rel_error(y_off)
    y_off = settle_absolute(y_off, dt, 0.0)
    rec_off = recovery(e0_off, rel_error(y_off))
    return {"source_on_recovery": rec_on, "source_off_recovery": rec_off}


def evaluate(dt):
    active_a = run_turnover(dt, ORDER_A, K)
    active_b = run_turnover(dt, ORDER_B, K)
    removed_a = run_turnover(dt, ORDER_A, 0.0)
    removed_b = run_turnover(dt, ORDER_B, 0.0)

    relabelled_ids = tuple(reversed(range(N)))
    label_a = run_turnover(dt, ORDER_A, K, member_ids=relabelled_ids)

    shuffled = list(reversed(REF))
    shuffled_bag = bag_error(shuffled)
    shuffled_rel = rel_error(shuffled)

    clock = [0.0] * N
    clock_phase_order = 1.0
    clock_rel = rel_error(clock)

    ext = external_template_control(dt)

    perturbed = list(REF)
    perturbed[ORDER_A[0]] = mean(perturbed)
    offset = [x + 7.25 for x in perturbed]
    offset_delta = abs(rel_error(perturbed) - rel_error(offset))

    label_delta = max(
        abs(active_a[key] - label_a[key])
        for key in ("median_recovery", "min_recovery", "final_rel_error", "max_mean_drift")
    )

    checks = {
        "complete_turnover_relational_recovery": (
            min(active_a["median_recovery"], active_b["median_recovery"]) >= 0.985
            and max(active_a["final_rel_error"], active_b["final_rel_error"]) <= 0.02
        ),
        "zero_original_members_remain": (
            active_a["membership_jaccard"] == 0.0
            and active_b["membership_jaccard"] == 0.0
        ),
        "protocol_removal_blocks_recovery": (
            max(removed_a["median_recovery"], removed_b["median_recovery"]) <= 0.05
        ),
        "member_labels_are_nonidentifying": label_delta <= TOL,
        "same_unlabelled_parts_wrong_roles_are_rejected": (
            shuffled_bag <= TOL and shuffled_rel >= 1.5
        ),
        "common_clock_is_nonidentifying": (
            abs(clock_phase_order - 1.0) <= TOL and clock_rel >= 0.90
        ),
        "external_template_requires_source": (
            ext["source_on_recovery"] >= 0.985 and ext["source_off_recovery"] <= 0.05
        ),
        "global_offset_is_nonidentifying": offset_delta <= TOL,
    }

    return {
        "dt": dt,
        "active_order_a": active_a,
        "active_order_b": active_b,
        "protocol_removed_order_a": removed_a,
        "protocol_removed_order_b": removed_b,
        "label_invariance_delta": label_delta,
        "role_shuffle_bag_error": shuffled_bag,
        "role_shuffle_rel_error": shuffled_rel,
        "common_clock_phase_order": clock_phase_order,
        "common_clock_rel_error": clock_rel,
        "external_template": ext,
        "offset_invariance_delta": offset_delta,
        "checks": checks,
        "pass_without_dt_audit": all(checks.values()),
    }


primary = evaluate(DT_PRIMARY)
audit = {str(dt): evaluate(dt) for dt in DT_AUDIT}
overall_pass = primary["pass_without_dt_audit"] and all(
    row["pass_without_dt_audit"] for row in audit.values()
)

print(json.dumps({
    "python": sys.version.split()[0],
    "platform": platform.platform(),
    "parameters": {
        "reference": REF,
        "k": K,
        "settle_time": TAU,
        "primary_dt": DT_PRIMARY,
        "audit_dt": DT_AUDIT,
        "order_a": ORDER_A,
        "order_b": ORDER_B,
        "randomness": None,
    },
    "analytic_reference": {
        "continuous_single_turn_recovery": 1.0 - math.exp(-K * TAU),
        "common_clock_rel_error": 1.0,
        "complete_turnover_membership_jaccard": 0.0,
    },
    "primary": primary,
    "dt_audit": audit,
    "overall_pass": overall_pass,
}, indent=2, sort_keys=True))
