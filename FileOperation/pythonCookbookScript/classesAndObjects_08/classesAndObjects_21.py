#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 24 Apr 2018 10:50:10 AM CST
# File Name: classesAndObjects_21.py
# Description:  属性的代理访问
                    将某个实例的属性访问代理到内部另一个实例中去，目的可能是作为继承的一个替代方法或者实现代理模式


                        代理是一种编程模式，它将某个操作转移给另外一个对象来实现
"""

class A(object):
    def spam(self, x):
        pass

    def foo(self):
        pass


class B1(object):
    '''简单的代理'''

    def __init__(self):
        self._a = A()


    def spam(self, x):
        #Delegate to the internal self._a instance
        return self._a.spam()

    def foo(self):
        #Delegate to the internal self._a instance
        return self._a.foo()

    def bar(self):
        pass


class B2(object):
    '''使用 __getattr__ 的代理，代理方法比较多时候'''

    def __init__(self):
        self._a = A()

    def bar(self):
        pass


    #Expose all of the methods defined on class A
    def __getattr__(self, name):
        '''这个方法在访问的 attribute 不存在的时候被调用
        the __getattr__() method is actually a fallback method
        that only gets called when an attribute is not found'''
        return getattr(self._a, name)
