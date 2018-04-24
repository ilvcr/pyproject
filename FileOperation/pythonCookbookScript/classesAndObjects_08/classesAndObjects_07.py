#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 23 Apr 2018 07:30:46 PM CST
# File Name: classesAndObjects_07.py
# Description:  用来扩展一个描述器
                    简单的子类化 setter 和 deleter 方法
"""


#A description

class String(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value


#A class with a descriptor
class Person(object):
    name = String('name')

    def __init__(self, name):
        self.name = name


#Extending a descriptor with a property
class SubPerson(Person):
    @property
    def name(self):
        print('Geting name')
        return super().name


    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)
