#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 12 May 2018 10:20:51 PM CST
# File Name: test_debug_exception_09.py
# Description:  使用一个简单的装饰器，测试函数的性能
"""

#timethis.py

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{}:{}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


#使用装饰器
@timethis
def countdown(n):
    while n > 0:
        n -= 1


