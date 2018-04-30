#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 28 Apr 2018 06:18:04 PM CST
# File Name: metaprogramming_16.py
# Description:  捕获类的属性定义顺序
                    自动记录一个类中属性和方法定义的顺序，然后可以利用它来做很多操作（比如序列化、映射到数据库等等）。
"""

#利用元类可以很容易的捕获类的定义信息。下面是一个例子，使用了一个 OrderedDict 来记录描述器的定义顺序

from collections import OrderedDict:

#A set of descriptors for various types
class Typed(object):
    _expected_type = type(None)
    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Expected ' + str(self._expected_type))
        instance.__dict__[self._name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str



#Metaclass that uses an OrderedDict for class body
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()


'''
在这个元类中执行类主体时描述器的定义顺序会被一个OrderedDict``捕获到，
生成的有序名称从字典中提取出来并放入类属性`` order 中。
'''
