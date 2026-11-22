"""Regression tests for the Git multi-route escalation gate."""

import unittest
from pathlib import Path

from scripts.agent_git_access_fallback import (
    NextAction,
    RouteEvidence,
    RouteStatus,
    select_next_action,
)


class TestRouteSelection(unittest.TestCase):
    def test_local_git_is_preferred_when_verified(self):
        self.assertEqual(
            select_next_action(RouteEvidence(local_git=RouteStatus.USABLE)),
            NextAction.USE_LOCAL_GIT,
        )

    def test_local_dns_failure_does_not_claim_global_github_outage(self):
        evidence = RouteEvidence(
            local_git=RouteStatus.INADEQUATE,
            github_connector=RouteStatus.USABLE,
        )
        self.assertEqual(select_next_action(evidence), NextAction.USE_GITHUB_CONNECTOR)

    def test_oversized_blob_falls_back_to_verified_prcek(self):
        evidence = RouteEvidence(
            local_git=RouteStatus.INADEQUATE,
            github_connector=RouteStatus.INADEQUATE,
            prcek_git=RouteStatus.USABLE,
            current_ha_manual_read=True,
            host_runner_authorized=True,
        )
        self.assertEqual(select_next_action(evidence), NextAction.USE_PRCEK_READ_ONLY)

    def test_bridge_manual_is_a_hard_gate(self):
        evidence = RouteEvidence(
            local_git=RouteStatus.INADEQUATE,
            github_connector=RouteStatus.INADEQUATE,
            prcek_git=RouteStatus.USABLE,
            host_runner_authorized=True,
        )
        self.assertEqual(select_next_action(evidence), NextAction.READ_HA_MANUAL)

    def test_no_host_execution_without_permission_check(self):
        evidence = RouteEvidence(
            local_git=RouteStatus.INADEQUATE,
            github_connector=RouteStatus.INADEQUATE,
            prcek_git=RouteStatus.USABLE,
            current_ha_manual_read=True,
        )
        self.assertEqual(
            select_next_action(evidence), NextAction.VERIFY_HOST_RUNNER_PERMISSION
        )

    def test_unverified_prcek_route_must_be_checked(self):
        evidence = RouteEvidence(
            local_git=RouteStatus.INADEQUATE,
            github_connector=RouteStatus.INADEQUATE,
        )
        self.assertEqual(select_next_action(evidence), NextAction.VERIFY_PRCEK_ROUTE)

    def test_only_all_confirmed_inadequate_routes_allow_blocker_claim(self):
        evidence = RouteEvidence(
            local_git=RouteStatus.INADEQUATE,
            github_connector=RouteStatus.INADEQUATE,
            prcek_git=RouteStatus.INADEQUATE,
        )
        self.assertEqual(
            select_next_action(evidence), NextAction.REPORT_VERIFIED_BLOCKER
        )

    def test_unverified_local_route_requires_fresh_probe(self):
        self.assertEqual(
            select_next_action(RouteEvidence()), NextAction.VERIFY_LOCAL_GIT
        )

    def test_binding_repository_policy_names_the_actual_access_route(self):
        rules = (
            Path(__file__).resolve().parents[1] / ".agent" / "rules.md"
        ).read_text(encoding="utf-8")
        expected = (
            "Mandatory Multi-Route Git Access Fallback Gate",
            "github.com DNS failure",
            "GitHub connector",
            "Prcek",
            "Home Assistant",
            "HA_COMMANDS",
            "HA_RESPONSES",
            "service_response.returncode=0",
            "same repository and ref",
            "Do not claim a global GitHub outage",
            "never send private content",
            "scripts/agent_git_access_fallback.py",
            "without claiming completion",
        )
        for term in expected:
            with self.subTest(term=term):
                self.assertIn(term, rules)


if __name__ == "__main__":
    unittest.main()
