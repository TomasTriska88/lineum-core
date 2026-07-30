import os
import sys
import subprocess
import venv
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

def test_setup_py_integrity():
    """
    Ensures that setup.py is syntactically valid and package metadata is correctly formatted.
    This runs 'python setup.py check' natively to catch basic configuration issues.
    """
    setup_file = ROOT / "setup.py"
    
    assert setup_file.exists(), "setup.py is missing from the repository root!"

    result = subprocess.run(
        [sys.executable, "setup.py", "check"],
        cwd=ROOT,
        capture_output=True,
        text=True
    )
    
    # Strict validation of the check output
    assert result.returncode == 0, f"setup.py execution failed:\n{result.stderr}\n{result.stdout}"


def _package_version() -> str:
    namespace = {}
    version_file = ROOT / "lineum_core" / "_version.py"
    exec(version_file.read_text(encoding="utf-8"), namespace)
    return namespace["__version__"]


def test_package_version_has_one_runtime_source():
    version = _package_version()
    setup_content = (ROOT / "setup.py").read_text(encoding="utf-8")

    assert version == "1.1.6"
    assert "lineum_core/_version.py" in setup_content.replace("\\", "/")
    assert 'version="1.1.6"' not in setup_content

    result = subprocess.run(
        [sys.executable, "setup.py", "--version"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == version


def test_package_builds_an_installable_versioned_wheel(tmp_path):
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "build",
            "--wheel",
            "--outdir",
            str(tmp_path),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    wheels = list(tmp_path.glob("*.whl"))
    assert [path.name for path in wheels] == [
        f"lineum_core-{_package_version()}-py3-none-any.whl"
    ]

    environment = tmp_path / "isolated"
    venv.EnvBuilder(with_pip=True).create(environment)
    python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    install = subprocess.run(
        [str(python), "-m", "pip", "install", "--no-deps", str(wheels[0])],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert install.returncode == 0, install.stderr

    imported = subprocess.run(
        [
            str(python),
            "-c",
            (
                "import lineum_core; "
                "from lineum_core.resources import load_claims; "
                "assert any(item['id'] == 'CL-CORE-001' for item in load_claims()); "
                "print(lineum_core.__version__)"
            ),
        ],
        cwd=environment,
        capture_output=True,
        text=True,
    )
    assert imported.returncode == 0, imported.stderr
    assert imported.stdout.strip() == _package_version()


def test_claim_registry_has_one_package_source():
    package_registry = ROOT / "lineum_core" / "data" / "claims.json"
    legacy_lab_copy = ROOT / "lab" / "src" / "lib" / "data" / "claims.json"
    lab_loader = (ROOT / "lab" / "src" / "lib" / "data" / "claims.js").read_text(
        encoding="utf-8"
    )

    assert package_registry.exists()
    assert not legacy_lab_copy.exists()
    assert "lineum_core/data/claims.json" in lab_loader.replace("\\", "/")


def test_tag_release_publishes_the_library_wheel():
    workflow = (ROOT / ".github" / "workflows" / "release_reference_pack.yml").read_text(
        encoding="utf-8"
    )

    assert "python -m build --wheel" in workflow
    assert "wheel_file=" in workflow
    assert "steps.prepare_library.outputs.wheel_file" in workflow
    assert "cd /tmp" in workflow


def test_python_ci_watches_library_packaging_contract_files():
    workflow = (ROOT / ".github" / "workflows" / "python_tests.yml").read_text(
        encoding="utf-8"
    )

    for contract_path in (
        "setup.py",
        "lineum_core/_version.py",
        "requirements-dev.txt",
    ):
        assert workflow.count(f"- '{contract_path}'") == 2
