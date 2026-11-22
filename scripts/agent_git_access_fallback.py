"""Read-only route selection after a Git access problem.

This module does not connect to any service or execute a command. The caller
must establish each route's current state from authoritative observations.
"""

from dataclasses import dataclass
from enum import Enum


class RouteStatus(str, Enum):
    UNVERIFIED = "unverified"
    USABLE = "usable"
    INADEQUATE = "inadequate"


class NextAction(str, Enum):
    VERIFY_LOCAL_GIT = "verify_local_git"
    USE_LOCAL_GIT = "use_local_git"
    VERIFY_GITHUB_CONNECTOR = "verify_github_connector"
    USE_GITHUB_CONNECTOR = "use_github_connector"
    VERIFY_PRCEK_ROUTE = "verify_prcek_route"
    READ_HA_MANUAL = "read_ha_manual"
    VERIFY_HOST_RUNNER_PERMISSION = "verify_host_runner_permission"
    USE_PRCEK_READ_ONLY = "use_prcek_read_only"
    REPORT_VERIFIED_BLOCKER = "report_verified_blocker"


@dataclass(frozen=True)
class RouteEvidence:
    local_git: RouteStatus = RouteStatus.UNVERIFIED
    github_connector: RouteStatus = RouteStatus.UNVERIFIED
    prcek_git: RouteStatus = RouteStatus.UNVERIFIED
    current_ha_manual_read: bool = False
    host_runner_authorized: bool = False


def select_next_action(evidence: RouteEvidence) -> NextAction:
    """Fail open to the next *verification*, never to an unverified claim.

    ``INADEQUATE`` includes a route that connects but cannot perform the
    specific required operation, e.g. a connector unable to read a large blob.
    ``USE_PRCEK_READ_ONLY`` authorizes no writes or service changes by itself.
    """
    if evidence.local_git is RouteStatus.UNVERIFIED:
        return NextAction.VERIFY_LOCAL_GIT
    if evidence.local_git is RouteStatus.USABLE:
        return NextAction.USE_LOCAL_GIT
    if evidence.github_connector is RouteStatus.UNVERIFIED:
        return NextAction.VERIFY_GITHUB_CONNECTOR
    if evidence.github_connector is RouteStatus.USABLE:
        return NextAction.USE_GITHUB_CONNECTOR
    if evidence.prcek_git is RouteStatus.UNVERIFIED:
        return NextAction.VERIFY_PRCEK_ROUTE
    if evidence.prcek_git is RouteStatus.USABLE:
        if not evidence.current_ha_manual_read:
            return NextAction.READ_HA_MANUAL
        if not evidence.host_runner_authorized:
            return NextAction.VERIFY_HOST_RUNNER_PERMISSION
        return NextAction.USE_PRCEK_READ_ONLY
    return NextAction.REPORT_VERIFIED_BLOCKER
