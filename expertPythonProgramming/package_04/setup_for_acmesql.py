#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 18 May 2018 12:43:42 PM CST
# File Name: setup_for_acmesql.py
# Description:  针对acme.sql包完整的setup.py
"""

import os
from setuptools import setup, find_packages

vision = '0.1.0'
README = os.path.join(os.path.dirname(__file__), 'README.txt')
long_description = open(README).read() + '\n\n'
setup(name='acme.sql',
    version=version,
    description=("A package that edals with SQL, from ACME inc"),
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        ("Topic :: Software Development :: Libraries :: Python Modules"),
        ],
    keywords='acme.sql',
    author='Tarek',
    author_email='tarek@ziade.org',
    url='http://ziade.org',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['acme'],
    install_requires=['pysqlite', 'SQLAchemy']
)



