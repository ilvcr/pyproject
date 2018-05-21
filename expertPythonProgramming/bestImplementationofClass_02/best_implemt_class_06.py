#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 16 May 2018 03:09:24 PM CST
# File Name: best_implemt_class_06.py
# Description:  船建一个数据符，并通过一个实例来实现它
"""

class UpperString(object):
    def __init__(self):
        self._value = ''

    def __get__(self, instance, klass):
        return self._value

    def __set__(self, instance, value):
        self._value = value.upper()


class MyClass(object):
    attribute = UpperString()


instance_of = MyClass()
print instance_of.attribute

instance_of.attribute = 'my value'
print instance_of.attribute

instance_of.__dict__ = {}

instance_of.new_att = 1
print instance_of.__dict__


