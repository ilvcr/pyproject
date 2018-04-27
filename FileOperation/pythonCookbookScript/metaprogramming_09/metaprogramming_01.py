#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 27 Apr 2018 02:54:38 PM CST
# File Name: metaprogramming_01.py
# Description:  在函数上添加包装器
                    在函数上添加一个包装器，增加额外的操作处理 (比如日志、计时等)。

            使用额外的代码包装一个函数，可以定义一个装饰器函数
"""

import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper      #闭包


#Example
@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

print(countdown(1000000))

