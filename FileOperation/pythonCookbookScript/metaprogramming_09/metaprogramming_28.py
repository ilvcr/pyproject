#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 03:04:16 AM CST
# File Name: metaprogramming_28.py
# Description:  使用元类和注解的一种替代方案，可以通过描述器来实现类似的效果
"""

import types

class multimethod(self):
    def __init__(self, func):
        self._methods = {}
        self.__name = func.__name__
        self._default = func

    def match(self, *types):
        def register(func):
            ndefaults = len(func.__defaults__) if func.__defaults__ else 0
            for n in range(ndefaults+1):
                self._methods[types[:len(types) - n]] = func
            return self
        return register


    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            return self._default(*args)

    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


#使用上述描述器
class Spam(object):
    @multimethod
    def bar(self, *args):
        #Default method called if no match
        raise TypeError('No matching method for bar')


    @bar.match(int, int):
    def bar(self, x, y):
        print('Bar 1:', x, y)


    @bar.match(str, int)
    def bar(self, s, n = 0):
        print('Bar 2:', s, n)
