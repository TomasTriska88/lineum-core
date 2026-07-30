import ast
import subprocess
from pathlib import Path


CORE_ROOT = Path(__file__).resolve().parents[1]
COMMERCIAL_ROOTS = ("portal", "routing_backend")


def _tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=CORE_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]


def test_commercial_runtime_trees_are_not_tracked_in_core():
    tracked = _tracked_files()
    violations = [
        path
        for path in tracked
        if any(path == root or path.startswith(f"{root}/") for root in COMMERCIAL_ROOTS)
    ]

    assert not violations, (
        "Commercial runtime trees must live in the private lineum-dynamics repository:\n"
        + "\n".join(violations)
    )


def test_core_ci_does_not_reference_commercial_runtime_trees():
    violations = []
    for workflow in (CORE_ROOT / ".github" / "workflows").glob("*.yml"):
        content = workflow.read_text(encoding="utf-8").replace("\\", "/")
        for root in COMMERCIAL_ROOTS:
            if f"{root}/" in content or f"cd {root}" in content:
                violations.append(f"{workflow.relative_to(CORE_ROOT)} -> {root}")

    assert not violations, (
        "Core CI must be runnable from a clean public checkout without private Dynamics trees:\n"
        + "\n".join(violations)
    )


def test_core_tests_do_not_import_or_read_commercial_runtime_trees():
    violations = []
    for test_file in (CORE_ROOT / "tests").glob("test_*.py"):
        if test_file == Path(__file__).resolve():
            continue

        tree = ast.parse(test_file.read_text(encoding="utf-8"), filename=str(test_file))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots = [alias.name.split(".", 1)[0] for alias in node.names]
                for root in imported_roots:
                    if root in COMMERCIAL_ROOTS:
                        violations.append(f"{test_file.name}:{node.lineno} imports {root}")
            elif isinstance(node, ast.ImportFrom) and node.module:
                root = node.module.split(".", 1)[0]
                if root in COMMERCIAL_ROOTS:
                    violations.append(f"{test_file.name}:{node.lineno} imports {root}")
            elif isinstance(node, ast.Constant) and isinstance(node.value, str):
                value = node.value.replace("\\", "/")
                for root in COMMERCIAL_ROOTS:
                    if value == root or value.startswith(f"{root}/"):
                        violations.append(f"{test_file.name}:{node.lineno} reads {root}")

    assert not violations, (
        "Core tests must cover the public repository only; commercial tests belong in Dynamics:\n"
        + "\n".join(sorted(set(violations)))
    )


def test_readme_and_boundary_document_describe_the_public_private_split():
    readme = (CORE_ROOT / "README.md").read_text(encoding="utf-8")
    assert "`/portal`" not in readme
    assert "cd portal" not in readme

    boundary_path = CORE_ROOT / "docs" / "repository-boundaries.md"
    assert boundary_path.exists(), "The public/private repository boundary must be documented."
    boundary = boundary_path.read_text(encoding="utf-8").lower()
    assert "lineum-core" in boundary
    assert "lineum-dynamics" in boundary
    assert "public" in boundary
    assert "private" in boundary
    assert "dynamics -> core" in boundary


def test_core_agent_and_github_policies_do_not_route_to_private_paths():
    policy_files = [CORE_ROOT / ".agent" / "rules.md"]
    policy_files.extend((CORE_ROOT / ".agent" / "workflows").glob("*.md"))
    policy_files.extend(
        [
            CORE_ROOT / ".github" / "CODEOWNERS",
            CORE_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md",
        ]
    )

    violations = []
    for policy_file in policy_files:
        content = policy_file.read_text(encoding="utf-8").replace("\\", "/")
        for root in COMMERCIAL_ROOTS:
            if f"{root}/" in content or f"cd {root}" in content:
                violations.append(f"{policy_file.relative_to(CORE_ROOT)} -> {root}")

    assert not violations, (
        "Core contributor policies must not route work into private repository paths:\n"
        + "\n".join(violations)
    )


def test_public_executable_configuration_has_no_private_runtime_dependency():
    executable_files = [
        CORE_ROOT / ".gitignore",
        CORE_ROOT / "pytest.ini",
        CORE_ROOT / "package.json",
        CORE_ROOT / ".githooks" / "pre-commit",
        CORE_ROOT / "lab" / "package.json",
        CORE_ROOT / "lab" / "vite.config.js",
        CORE_ROOT / "lab" / "scripts" / "check-czech.js",
        CORE_ROOT / "lab" / "src" / "lib" / "components" / "ContactFooter.svelte",
        CORE_ROOT / "scripts" / "check-czech.mjs",
        CORE_ROOT / "scripts" / "release_check.py",
        CORE_ROOT / "tools" / "sync_version.py",
    ]
    executable_files.extend((CORE_ROOT / "tmp").glob("*.py"))

    violations = []
    for executable_file in executable_files:
        if not executable_file.exists():
            continue
        content = executable_file.read_text(encoding="utf-8").lower().replace("\\", "/")
        for root in COMMERCIAL_ROOTS:
            private_tokens = (
                f"{root}/",
                f"cd {root}",
                f"from {root}",
                f"import {root}",
                f"{root}.",
            )
            if any(token in content for token in private_tokens):
                violations.append(f"{executable_file.relative_to(CORE_ROOT)} -> {root}")

    assert not violations, (
        "Public executable configuration must not depend on private runtime trees:\n"
        + "\n".join(violations)
    )
