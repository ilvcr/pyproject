#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 23 Apr 2018 07:45:40 PM CST
# File Name: classesAndObjects_09.py
# Description:  描述器通常是那些使用到装饰器或元类的大型框架中的一个组件。
                    同时它们的使用也被隐藏在后面
                                高级的基于描述器的代码，并涉及到一个类装饰器
"""

#Descriptor for a type-checked attribute
class Typed(object):
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

#Class decorator that applies it to selected attribute
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.item():
            #Attach a typed descriptor tp the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorator


#Example use
@typeassert(name=str, shares=int, price=float)
class Stock(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
