# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logging-loki",
    version="0.0.1-alpha.1",
    description="Python logging handler for Grafana Loki.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Lunaticsky",
    author_email="tqla314@gmail.com",
    url="https://github.com/greyzmeem/python-logging-loki",
    packages=setuptools.find_packages(exclude=("tests",)),
    python_requires=">=3.6",
    install_requires=["rfc3339>=6.1", "requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
