#!/usr/bin/env python

import setuptools
import os

setuptools.setup(
    name='emerald-beryl-pipeline',
    version='0.0.0',
    description='',
    long_description="",
    long_description_content_type="text/markdown",
    author='Benjamin Bloss',
    author_email='bb@emrld.no',
    url='https://github.com/emerald-geomodelling/emerald-monitor',
    packages=setuptools.find_packages(),
    install_requires=[
        "psutil",
        "time",
        "numpy",
        "pandas",
        "matplotlib",
        "threading"
    ])
