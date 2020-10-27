#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

NAME = 'draco'
DESCRIPTION = 'Detection and recognition of celestial objects'
URL = 'https://github.com/ynbella/draco'
EMAIL = 'me@example.com'
AUTHOR = 'Jared Bell, Youness Bella, Fonte Clanton'
REQUIRES_PYTHON = '>=3.8.6'
VERSION = '0.0.1'

try:
    with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
        LONG_DESCRIPTION = '\n' + f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

try:
    with io.open(os.path.join(here, 'LICENSE'), encoding='utf-8') as f:
        LICENSE = '\n' + f.read()
except FileNotFoundError:
    LICENSE = "No license found."

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["docs", "tests", "*.tests", "*.tests.*", "tests.*"]),
)