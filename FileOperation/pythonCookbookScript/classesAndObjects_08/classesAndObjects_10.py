#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 23 Apr 2018 07:58:14 PM CST
# File Name: classesAndObjects_10.py
# Description:  想将一个只读属性定义成一个 property，
                    并且只在访问的时候才会计算结果。
                            但是一旦被访问后希望结果值被缓存起来，不用每次都去计算。



                定义一个延迟属性的一种高效方法是通过使用一个描述器类


                使用延迟计算属性

                缺陷是计算出的值被创建后是可以被修改
"""

class lazyproprety(object):
    def __init__(self, func):
        self.func = func


    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value



#Example use

import math

class Cricle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazyproprety
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproprety
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

