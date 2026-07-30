from pathlib import Path

from setuptools import find_packages, setup


ROOT = Path(__file__).resolve().parent
VERSION_FILE = ROOT / "lineum_core/_version.py"
VERSION_NAMESPACE = {}
exec(VERSION_FILE.read_text(encoding="utf-8"), VERSION_NAMESPACE)

setup(
    name="lineum-core",
    version=VERSION_NAMESPACE["__version__"],
    description="Application-neutral Lineum physics library",
    packages=find_packages(),
    include_package_data=True,
    package_data={"lineum_core.data": ["claims.json"]},
    python_requires=">=3.11",
    install_requires=["numpy>=1.24,<2.0.0"],
)
