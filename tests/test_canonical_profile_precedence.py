"""Regression tests for canonical audit profile selection."""

from tools.whitepaper_contract import select_profile_result


def _profile_result(name: str, status: str, check_count: int) -> dict:
    return {
        "profile": name,
        "status": status,
        "checks": [{"status": status} for _ in range(check_count)],
    }


def test_one_step_canonical_failure_is_not_hidden_by_baseline_pass() -> None:
    baseline = _profile_result("baseline", "PASS", 5)
    canonical = _profile_result("canonical", "FAIL", 12)

    selected = select_profile_result([baseline, canonical])

    assert selected["profile"] == "canonical"
    assert selected["status"] == "FAIL"


def test_wave_core_pass_cannot_hide_canonical_failure() -> None:
    baseline = _profile_result("baseline", "PASS", 5)
    canonical = _profile_result("canonical", "FAIL", 12)
    wave_core = _profile_result("wave_core", "PASS", 13)

    selected = select_profile_result([baseline, canonical, wave_core])

    assert selected["profile"] == "canonical"
    assert selected["status"] == "FAIL"


def test_canonical_pass_remains_authoritative() -> None:
    baseline = _profile_result("baseline", "PASS", 5)
    canonical = _profile_result("canonical", "PASS", 12)
    wave_core = _profile_result("wave_core", "FAIL", 13)

    selected = select_profile_result([baseline, canonical, wave_core])

    assert selected["profile"] == "canonical"
    assert selected["status"] == "PASS"


def test_noncanonical_run_preserves_best_passing_profile() -> None:
    baseline = _profile_result("baseline", "PASS", 5)
    wave_core = _profile_result("wave_core", "PASS", 13)

    selected = select_profile_result([baseline, wave_core])

    assert selected["profile"] == "wave_core"
    assert selected["status"] == "PASS"


def test_noncanonical_run_falls_back_to_most_comprehensive_failure() -> None:
    baseline = _profile_result("baseline", "FAIL", 5)
    wave_core = _profile_result("wave_core", "FAIL", 13)

    selected = select_profile_result([baseline, wave_core])

    assert selected["profile"] == "wave_core"
    assert selected["status"] == "FAIL"
}
