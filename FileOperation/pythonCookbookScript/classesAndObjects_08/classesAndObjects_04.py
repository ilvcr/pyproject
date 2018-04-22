#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 21 Apr 2018 05:49:01 PM CST
# File Name: classesAndObjects_04.py
# Description:  给某个实例attribute增加除访问与修改之外的其他处理逻辑, 比如类型检查或合法性验证
                    定义一个property, 增加对一个属性简单的类型检查
"""

class Person(object):

    def __init__(self, first_name):
        self.first_name = first_name


    #Getter function
    @property
    def first_name(self):
        return self._first_name

    #Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    #Delete function(optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("cant't delete attribute")


#Example
a = Person('Guido')
print(a.first_name)

