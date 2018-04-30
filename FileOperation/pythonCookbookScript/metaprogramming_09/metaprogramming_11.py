#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 28 Apr 2018 05:32:12 PM CST
# File Name: metaprogramming_11.py
# Description:  装饰器为被包装函数增加参数
                    使用关键字参数来给被包装函数增加额外参数
"""

from functools import wraps

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling:', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@optional_debug
def spam(a, b, c):
    print(a, b, c)


