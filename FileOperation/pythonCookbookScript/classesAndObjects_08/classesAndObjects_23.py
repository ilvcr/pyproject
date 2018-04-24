#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 24 Apr 2018 11:24:52 AM CST
# File Name: classesAndObjects_23.py
# Description:  代理类可作为继承的替代方案
"""

class A(object):
    def spam(self, x):
        print('A.spam', x)
    def foo(self):
        print('A.foo')



#普通继承
class B(A):
    def spam(self, x):
        print('B.spam')
        super().spam(x)
    def bar(self):
        print('B.bar')



#使用代理
class B(object):
    def __init__(self):
        self._a = A()
    def spam(self, x):
        print('B.spam', x)
        self._a.spam(x)
    def bar(self):
        print('B.bar')
    def __getattr__(self, name):
        return getattr(self._a, name) 
        '''getattr ()实际是一个后备方法，只有在属性不存在时才会调用。
        如果代理类实例本身有这个属性的话，那么不会触发这个方法的。'''



# getattr () 对于大部分以双下划线 ( ) 开始和结尾的属性并不适用。
class ListLike(object):
    '''__getattr__ 对于双下划线开始和结尾的方法是不能用的，需要一个个去重定义'''

    def __init__(self):
        self._item = []

    def __getattr__(self, name):
        return getattr(self._item, name)
