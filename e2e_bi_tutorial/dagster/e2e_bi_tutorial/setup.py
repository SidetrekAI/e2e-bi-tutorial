from setuptools import find_packages, setup

setup(
    name="e2e_bi_tutorial",
    packages=find_packages(exclude=["e2e_bi_tutorial_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
