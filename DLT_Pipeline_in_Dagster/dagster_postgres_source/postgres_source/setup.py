from setuptools import find_packages, setup

setup(
    name="postgres_source",
    packages=find_packages(exclude=["postgres_source_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
