#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 23 Apr 2018 11:09:07 PM CST
# File Name: classesAndObjects_12.py
# Description:  简化数据结构的初始化
                    在一个基类中写一个公用的 __init__ () 函数
"""


import math

class Structure1(object):
    #Class variable that specifies expect fields

    _fields = []


    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} argument'.format(len(self._fields)))

        #Set the argument
        for name, value in zip(self._fields, args):
            setattr(self, name, value)



#Example class definetions
class Stock(Structure1):
    _fields = ['name', 'sharps', 'price']


class Point(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2
