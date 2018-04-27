#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 27 Apr 2018 07:49:06 PM CST
# File Name: metaprogramming_06.py
# Description:  利用装饰器强制函数上的类型检查
                    使用装饰器技术来实现 @typeassert
"""


from inspect import signature
from functols import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        #If in optimized mode, disable type checking
        if not __debug__:
            return func



        #Map function argument names to suplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments


        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            #Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.item():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)
        return wrapper

    return decorate


def decorate(func):
    #If in optimized mode, disable type checking
    if not __debug__:
        return func

