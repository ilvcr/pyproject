#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 21 Apr 2018 04:47:00 PM CST
# File Name: classesAndObjects_01.py
# Description:  改变对象实例的打印或者显示输出, 让他们具有可读性

                        要改变一个实例的字符串表示, 重新定义__str__()和__repr__()方法
"""

class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
        '''
        __repr__()方法返回一个实例的代码表示形式
        '''

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)
        '''
        __str__()方法将实例转换为一个字符串, 使用str()或print()函数会输出这个字符串
        '''

#Example
p = Pair(3, 4)
print(p)
str(p)
