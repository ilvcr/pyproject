#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 17 May 2018 12:42:51 PM CST
# File Name: select_name_03.py
# Description:  python中的特殊方法
"""

class weirdint(int):
    def __add__(self, other):
        return int.__add__(self, other) + 1

    def __repr__(self):
        return '<weirdo {}>'.format(self)

    #共有API

    def do_this(self):
        print 'this'

    def do_that(self):
        print 'that'


class BadHabits(object):
    def __my_method__(self):
        print 'ok'


