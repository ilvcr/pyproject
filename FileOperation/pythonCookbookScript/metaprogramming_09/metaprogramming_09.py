#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 27 Apr 2018 11:35:58 PM CST
# File Name: metaprogramming_09.py
# Description:  一个使用闭包和 nonlocal 变量实现的装饰器
"""

import types
from functools import wraps

def profiled(func):
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)

    wrapper.ncalls = lambda: ncalls
    return wrapper

#Example
@profiled
def add(x, y):
    return x + y
