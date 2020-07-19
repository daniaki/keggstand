#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "beautifulsoup4>=4.8",
    "lxml>=4.4",
    "pandas>=1.0",
    "requests>=2.20",
    "tqdm>=4.48.0",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = ["pytest>=3", "mock>=4"]

setup(
    author="Daniel Esposito",
    author_email="danielce90@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="KEGG API client and parsers for pathway protein-protein interactions",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="keggstand",
    name="keggstand",
    packages=find_packages(include=["keggstand", "keggstand.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/daniaki/keggstand",
    version="0.0.7",
    zip_safe=False,
)
