#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 03:17:18 AM CST
# File Name: metaprogramming_29.py
# Description:  避免重复的属性方法
"""

#简单的类的属性由属性方法包装
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be a string')
        self._name = value


    @property
    def age(self):
        return self._age


    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('age must be an int')
        self._age = value


def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)


    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}',format(name, expected_type))
        setattr(self, storage_name, value)

    return prop


#Example use
class Person(object):
    name = typed_property('name', str)
    age = typed_property('age', int)


    def __init__(self, name, age):
        self.name = name
        self.age = age





from functools import partial

String = partial(typed_property, expected_type=str)
Integer = partial(typed_property, expected_type=int)

#Examole
class Person(object):
    name = String('name')
    age = Integer('age')


    def __init__(self, name, age):
        self.name = name
        self.age = age
