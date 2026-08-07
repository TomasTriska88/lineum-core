from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
from typing import Any

SCHEMA = "lineum-b4-q2-perturbation-ledger-check/1"
PRIMARY_SCHEMA = "lineum-b4-q2-perturbation-ledger/1-retained-table"
STAGE = "Q2-PV1-A-CHECK"
PRIMARY_STAGE = "Q2-PV1-A"
COMPARE_RTOL = 1e-12
NUMERIC_RTOL = 1e-10
FROZEN_RECOVERY_ENERGY_TOLERANCE = 0.05
INNER_FACTOR = 1.5
ANNULUS_FACTOR = 0.5
EXPECTED_CANONICAL_RUNNER_BLOB = "1598faf0f39e056c1684f767c2554edc63283ca4"
EXPECTED_PRIMARY_RUNNER_BLOB = "e3657119b855965b4fd622b3e94f08443a7c9107"
EXPECTED_PRIMARY_TEST_BLOB = "403c1cb8747cebf3280009b3b2ffcd814c72e060"

# Full independently derived checker source is staged in Git object 72b780ca86254ebd9083d9e01da97fb46d4c2b7c.
# This contents-API recovery commit is intentionally not a scientific execution.
