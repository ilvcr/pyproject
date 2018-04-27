#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 27 Apr 2018 11:41:44 PM CST
# File Name: metaprogramming_10.py
# Description:  为类和静态方法提供装饰器
                    给类或静态方法提供装饰器确保装饰器在 @classmethod 或@staticmethod 之前。
"""

import time
from functools import wraps

#A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r
    return wrapper


# Class illustrating application of the decorator to different kinds of methods
class Spam(object):
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmwthod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1


    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1
