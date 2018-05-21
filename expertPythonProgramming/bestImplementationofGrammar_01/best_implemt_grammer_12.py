#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 02:24:54 PM CST
# File Name: best_implemt_grammer_12.py
# Description:  staticmethod,classmethod装饰器的使用
"""

class WhatFor(object):
    @classmethod
    def it(cls):
        print 'work with {}'.format(cls)

    @staticmethod
    def uncommon():
        print 'I could be a global function'


this_is = WhatFor()

print this_is.it()

print this_is.uncommon()


