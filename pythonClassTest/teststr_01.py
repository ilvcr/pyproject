#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: teststr_01.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr  5 21:17:04 2019
# Description: 
#************************************************************************#

#修改实例的字符串，定义__str__() 与__repr__() 方法

class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
print p
print 'p is {0!r}'.format(p)
print 'p is {0}'.format(p)


