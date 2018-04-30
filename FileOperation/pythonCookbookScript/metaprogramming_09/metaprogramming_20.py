#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 01:00:08 AM CST
# File Name: metaprogramming_20.py
# Description:  *args 和 **kwargs 的强制参数签名
                    有一个函数或方法它使用 *args 和 **kwargs 作为参数

"""

'''
在基类中先定义了一个非常通用的 init () 方法，
然后我们强制所有的子类必须提供一个特定的参数签名。
'''
#强制函数签名

from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)


class Structure(object):
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


#Example use
class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')
