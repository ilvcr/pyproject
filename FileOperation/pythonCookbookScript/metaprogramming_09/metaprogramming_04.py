#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 27 Apr 2018 07:22:23 PM CST
# File Name: metaprogramming_04.py
# Description:  可自定义属性的装饰器
                    写一个装饰器来包装一个函数，并且允许用户提供参数在运行时控制装饰器行为。


            引入一个访问函数，使用 nolocal 来修改内部变量。然后这个访问函数被作为一个属性赋值给包装函数。
"""

from functools import wraps, partial
import logging

#Utility decorator to attach a function as an attribute of obj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging level,
    name is the logger name, and message is the log message.
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

        #Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg


        return wrapper


    return decorate


#Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@loged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


#装饰器以相反的方向排放
@logged(logging.DEBUG)
@timethis
def countdown(n):
    while n > 0:
        n -= 1


#使用 lambda 表达式代码来让访问函数的返回不同的设定值
@attach_wrapper(wrapper)
def get_level():
    return level

#Alternative
wrapper.get_level = lambda: level


@wraps(func)
def wrapper(*args, **kwargs):
    wrapper.log.log(wrapper.level, wrapper.logmsg)
    return func(*args, **kwargs)

#Attach adjustable attribute
wrapper.level = level
wrapper.logmsg = logmsg
wrapper.log = log

