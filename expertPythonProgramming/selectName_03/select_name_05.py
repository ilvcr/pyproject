#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 17 May 2018 12:51:33 PM CST
# File Name: select_name_05.py
# Description:  根据迭代设计构建参数，当附加一些参数时，应当尽可能有默认值以避免任何退化
"""

class BD(object):
    def _query(self, query, type):
        print 'done'

    def execute(self, query):
        self._query(query, 'EXECUTE')


print BD().execute('mu query')

import logging

class BD1(object):
    def _query(self, query, type, logger):
        logger('done')

    def execute(self, query, logger=logging.info):
        self._query(query, 'EXECUTE', logger)


print BD1().execute('my query')
print BD1().execute('my query', logging.warning)


