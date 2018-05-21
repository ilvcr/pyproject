#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 16 May 2018 11:42:16 PM CST
# File Name: best_implemt_class_09.py
# Description:  属性Property
"""

class MyClass(object):
    def __init__(self):
        self._my_secret_thing = 1

    def _i_get(self):
        return self._my_secret_thing

    def _i_set(self, value):
        self._my_secret_thing = value

    def _i_delete(slef):
        print 'neh!'

    my_thing = property(_i_get, _i_set, _i_delete, 'the thing')


instance_of = MyClass()

print instance_of.my_thing

instance_of.my_thing = 3
print instance_of.my_thing

del instance_of.my_thing

print help(instance_of)


