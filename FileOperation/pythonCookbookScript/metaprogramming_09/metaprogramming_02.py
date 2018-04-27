#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 27 Apr 2018 03:02:12 PM CST
# File Name: metaprogramming_02.py
# Description:  创建装饰器时保留函数元信息
                    写一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、
                    文档字符串、注解和参数签名都已丢失。


            任何时候定义装饰器，都应该使用 functools 库中的 @wraps 装饰器来注解底层包装函数
"""

import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time
    '''

    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        end = time.time()

        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n>0:
        n -= 1


print(countdown(1000000))
print(countdown.__name__)
print(countdown.__doc__)
#print(countdown.__annotations__)
