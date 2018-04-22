#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 21 Apr 2018 06:12:09 PM CST
# File Name: classesAndObjects_06.py
# Description:  Properties是一种定义动态计算attribute的方法
                    这种类型的额attribute不会被实际存储, 在需要的时候计算出来
"""

import math

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def diameter(self):
        return self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.radius)
print(c.area)
print(c.perimeter)
