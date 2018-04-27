#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 27 Apr 2018 11:29:47 PM CST
# File Name: metaprogramming_08.py
# Description:  将装饰器定义为类
                    使用一个装饰器去包装函数，但是希望返回一个可调用的实例


                        将装饰器定义成一个实例，需要确保它实现了 call () 和 get () 方法

            代码定义了一个类，它在其他函数上放置一个简单的记录层：
"""

import types
from functools import wraps

class Profiled(object):
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)


    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Spam(object):
    @Profiled
    def bar(self, x):
        print(self, x)
