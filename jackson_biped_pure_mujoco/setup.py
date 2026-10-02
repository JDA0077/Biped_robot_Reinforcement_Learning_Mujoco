# Copyright (c) 2026, Jackson Bipedal Research Project.
# Pure MuJoCo Package Setup.

from setuptools import setup, find_packages

setup(
    name="jackson_biped",
    version="2.0.0",
    packages=find_packages(),
    author="Jackson Bipedal Research Team",
    description="Pure MuJoCo Locomotion Framework for Jackson Bipedal Robot",
    license="BSD-3-Clause",
    install_requires=[
        "mujoco>=3.0.0",
        "gymnasium>=0.29.0",
        "torch>=2.0.0",
        "numpy>=1.22.0",
    ],
    python_requires=">=3.10",
)
