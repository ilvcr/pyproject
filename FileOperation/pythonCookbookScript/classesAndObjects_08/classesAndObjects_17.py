#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 24 Apr 2018 09:09:05 AM CST
# File Name: classesAndObjects_17.py
# Description:  根据类来实际定义的各种不同的数据类型;
                    然后使用这些自定义数据类型定义一个类
"""


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


#然后使用这些自定义数据类型自定义一个类
class Stock(object):

    #Specify constrains
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')


    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price



#使用类装饰器简化上面代码
#Class decorator to apply constraints
def chexk_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Desceiptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key,value(key))
        return cls

    return decorate

#Example
@chexk_attributes(name=SizedString(size=8), shares=UnsignedInteger, price=UnsignedFloat)
class Stock1(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price



#使用类元类简化上面代码
#A metaclass that applies checking
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        #Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Desceiptor):
                value.name = key

        return type.__new__(cls, clsname, bases, methods)

#Example
class Stock2(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()


    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
