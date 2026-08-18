from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "research" / "runners" / "lineum_b4_q2_mu_causal_reuse.py"
ACTIVE_MATH_PATH = ROOT / "lineum_core" / "math.py"


PATH_ISOLATED_PROBE = r"""
import json
from pathlib import Path
import runpy
import sys

root = Path(sys.argv[1]).resolve()
runner = Path(sys.argv[2]).resolve()
runner_directory = runner.parent.resolve()


def resolved_path(entry: str) -> Path:
    return Path(entry or ".").resolve()


sys.path[:] = [
    str(runner_directory),
    *[
        entry
        for entry in sys.path
        if resolved_path(entry) not in {root, runner_directory}
    ],
]

namespace = runpy.run_path(
    str(runner),
    run_name="lineum_b4_q2_m1_import_path_probe",
)
CoreConfig, ExecutionPolicy, step_core = namespace["core_bindings"]()

import lineum_core.math as core_math

print(
    json.dumps(
        {
            "repository_root": str(root),
            "sys_path_first": sys.path[0],
            "core_math_file": str(Path(core_math.__file__).resolve()),
            "core_config_module": CoreConfig.__module__,
            "execution_policy_module": ExecutionPolicy.__module__,
            "step_core_module": step_core.__module__,
            "run_name": namespace["__name__"],
            "scientific_main_invoked": namespace["__name__"] == "__main__",
        },
        sort_keys=True,
    )
)
"""


def test_path_isolated_runner_bootstraps_the_active_repository_core() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            "-I",
            "-c",
            PATH_ISOLATED_PROBE,
            str(ROOT),
            str(RUNNER_PATH),
        ],
        cwd=RUNNER_PATH.parent,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

    assert completed.returncode == 0, completed.stderr
    receipt = json.loads(completed.stdout)
    assert Path(receipt["repository_root"]).resolve() == ROOT
    assert Path(receipt["sys_path_first"]).resolve() == ROOT
    assert Path(receipt["core_math_file"]).resolve() == ACTIVE_MATH_PATH
    assert receipt["core_config_module"] == "lineum_core.math"
    assert receipt["execution_policy_module"] == "lineum_core.math"
    assert receipt["step_core_module"] == "lineum_core.math"
    assert receipt["run_name"] == "lineum_b4_q2_m1_import_path_probe"
    assert receipt["scientific_main_invoked"] is False
