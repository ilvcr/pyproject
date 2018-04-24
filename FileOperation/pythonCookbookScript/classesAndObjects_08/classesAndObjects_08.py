#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 23 Apr 2018 07:39:59 PM CST
# File Name: classesAndObjects_08.py
# Description:  想创建一个新的拥有一些额外功能的实例属性类型，比如类型检查。
                    想创建一个全新的实例属性，
                        可以通过一个描述器类的形式来定义它的功能。
"""

#Descriptor attribute for an integer type-checked attribute
class Integer(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]
