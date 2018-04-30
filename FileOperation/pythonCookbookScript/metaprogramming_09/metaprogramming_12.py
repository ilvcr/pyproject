#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 28 Apr 2018 05:36:24 PM CST
# File Name: metaprogramming_12.py
# Description:  通过装饰器来给被包装函数增加参数
"""


from functools import wraps
import inspect

def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')


    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('calling',func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug', inspect.Parameter.KEYWORD_ONLY, default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)

    return wrapper


@optional_debug
def a(x):
    pass

@optional_debug
def b(x, y, z):
    pass

@optional_debug
def c(x, y):
    pass
