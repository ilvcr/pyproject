#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 27 Apr 2018 07:41:35 PM CST
# File Name: metaprogramming_05.py
# Description:  带可选参数的装饰器
                    写一个装饰器，既可以不传参数给它，比如 @decorator ，
                    也可以传递可选参数给它，比如 @decorator(x,y,z)
"""

from functools import wraps, partial
import logging

def logged(func=None, *,level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(loged, level=level, name=name,message=message)


    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)


    return wrapper


#Example use
@logged
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')
