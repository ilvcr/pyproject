#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 28 Apr 2018 05:47:28 PM CST
# File Name: metaprogramming_13.py
# Description:  使用装饰器扩充类的功能
                    通过反省或者重写类定义的某部分来修改行为，但又不希望使用继承或元类的方式。

            重写了特殊方法__getattribute__ 的类装饰器打印日志
"""

def log_getattribute(cls):
    #Get the original implementation
    orig_getattribute = cls.__getattribute__

    #Make a new definition
    def new_getattribute(self, name):
        print('getting:', name)
        return orig_getattribute(self, name)


    #Attach to the class and return
    cls.__getattribute__ = new_getattribute
    return cls

#Example use
@log_getattribute
class A(object):
    def __init__(self, x):
        self.x = x
    def spam(self):
        pass


#类装饰器作为其他高级技术比如混入或元类的一种非常简洁的替代方案。
class LoggedGetattribute(object):
    def __getattribute__(self, name):
        print('getting:', name)
        return super().__getattribute__(name)

#Example
class A1(LoggedGetattribute):
    def __init__(self, x):
        self.x = x
    def spam(self):
        pass
