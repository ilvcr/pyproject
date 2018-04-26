#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 26 Apr 2018 01:57:51 PM CST
# File Name: classesAndObjects_34.py
# Description:  让类支持比较操作
                    构建一些房子，然后给它们增加一些房间，最后通过房子大小来比较它们
"""

'''
装饰器 functools.total ordering 就是用来简化这个处理的。使用它来装饰一个来，
只需定义一个 eq () 方法，外加其他方法 ( lt , le , gt , or ge ) 中的一个即可。
然后装饰器会自动填充其它比较方法。
'''

from functools import total_ordering

class Room(object):
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width


@total_ordering
class House(object):
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{} square foot {}'.format(self.name, self.living_space_footage, self.style)

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage



class House1(object):
    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    #Method created bu @total_ordering
    __le__ = lambda self, other: self < other or self == other
    __gt__ = lambda self, other: not (self < other or self == other)
    __ge__ = lambda self, other: not (self < other)
    __ne__ = lambda self, other: not self == other
