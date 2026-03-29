import os
from setuptools import setup, find_packages

def read_requirements():
    req_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_file):
        with open(req_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name='lineum_core',
    version='1.0.0',
    description='Core physics engine and generative algorithms for Lineum and OEA',
    author='Tomáš Tříska',
    # Registers the package directory structure, specifically the core "lineum_core/"
    packages=find_packages(include=['lineum_core', 'lineum_core.*']),
    # Registers top-level modules at the root, e.g. "import lineum" via "lineum.py"
    py_modules=['lineum'],
    install_requires=read_requirements(),
    python_requires='>=3.8',
)
