#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 17 May 2018 12:27:50 PM CST
# File Name: select_name_01.py
# Description:  python命名
"""

SQL_USER = 'tarek'
SQL_PASSWORD = 'secret'
SQL_URI = 'postgres://{}:{}@localhost/db'.format(SQL_USER, SQL_PASSWORD)

MAX_THREADS = 4

print '\n' + SQL_URI + '\n'


OPTIONS = {}

def register_option(name):
    return OPTIONS.setdefault(name, 1 << len(OPTIONS))

def has_option(options, name):
    return bool(options & name)

#定义选项
BLUE = register_option('BULE')
RED = register_option('RED')
WHITE = register_option('WHITE')

SET = BLUE | RED

print has_option(SET, BLUE)
print has_option(SET, WHITE)


