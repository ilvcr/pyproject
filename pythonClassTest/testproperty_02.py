#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testproperty_02.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr  5 21:59:27 2019
# Description: 
#************************************************************************#

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(4.0)
print c.radius

print c.area

print c.perimeter






