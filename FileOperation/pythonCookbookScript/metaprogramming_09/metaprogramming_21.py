#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 01:08:13 AM CST
# File Name: metaprogramming_21.py
# Description:  通过使用自定义元类来创建签名对象
"""

from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)


class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


#Example
class Stock(Structure):
    _fields = ['name', 'shares', 'price']


class Point(Structure):
    _fields = ['x', 'y']

