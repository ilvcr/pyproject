#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 27 Apr 2018 08:00:40 PM CST
# File Name: metaprogramming_07.py
# Description:  将装饰器定义为类的一部分
                    在类中定义装饰器，并将其作用在其他函数或方法上。
"""

from functools import wraps

class A(object):
    #Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper


    #Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper

#As an instance method
a = A()
@a.decorator1
def spam():
    pass

#As a class method
@A.decorator2
def grok():
    pass


class Person(object):
    #Creat a property instance
    first_name = property()

    #Apply decorator methods
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value
