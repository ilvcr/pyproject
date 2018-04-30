#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 02:07:22 AM CST
# File Name: metaprogramming_26.py
# Description:  在类被定义的时候就初始化一部分类的成员，而不是要等到实例被创建后
                    创建类似于 collections 模块中的命名元组的类
"""

import operator

class StructTuplemeta(Type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTuplemeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields)
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls, args)


#用来定义简单的基于元组的数据结构
class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


class Point(StructTuple):
    _fields = ['x', 'y']
