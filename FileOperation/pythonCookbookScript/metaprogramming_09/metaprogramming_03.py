#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 27 Apr 2018 03:12:27 PM CST
# File Name: metaprogramming_03.py
# Description:  带参数的装饰器
                    写一个装饰器，给函数添加日志功能，当时允许用户指定日志的级别和其他的选项。
"""

from functools import wraps
import logging

def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logginglevel,
    name is the logger name, and message is thelog message.
    If name and message aren't specified,they default to the function's module and name.
    '''

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate

#Example
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print("Spam!")

'''
最外层的函数 logged()接受参数并将它们作用在内部的装饰器函数上面。
内层的函数 decorate() 接受一个函数作为参数，然后在函数上面放置一个包装器。

关键点是包装器是可以使用传递给 logged() 的参数的。
'''
