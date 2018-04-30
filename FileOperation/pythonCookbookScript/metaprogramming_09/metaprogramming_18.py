#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 29 Apr 2018 12:11:39 AM CST
# File Name: metaprogramming_18.py
# Description:  防止重复的定义
"""

from collections import OrderedDict

class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname):
        self.clsname = clsname
        super().__init__()
    def __setitem__(self, name, value):
        if name in self:
            raise TypeError('{} already defined in {}'.format(name, self.clsname))
        super().__setitem__(name, value)


class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        d['_order'] = [name for name in clsdict if name[0] != '_']
        return type.__new__(cls, clsname, bases, d)


        @classmethod
        def __prepare__(cls, clsname, bases):
            return NoDupOrderedDict(clsname)


class A(metaclass=OrderedMeta):
    def spam(self):
        pass
    def spam(self):
        pass
