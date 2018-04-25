#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 25 Apr 2018 08:48:50 PM CST
# File Name: classesAndObjects_29.py
# Description:  通过字符串调用对象方法
                    有一个字符串形式的方法名称，想通过它调用某个对象的对应方法。


                        使用 getattr()
                            使用 operator.methodcaller()
"""

import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:}, {!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)
d = getattr(p, 'distance')(0, 0)


import operator
operator.methodcaller('distance', 0, 0)(p)
