#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 21 Apr 2018 06:03:29 PM CST
# File Name: classesAndObjects_05.py
# Description:  在已存在的get和set方法的基础上定义property
"""


class Person(object):

    def __init__(self, first_name):
        self.set_first_name(first_name)

    #Getter function
    def get_first_name(self):
        return self._first_name

    #Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    #Deleter function(Optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    #Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)


