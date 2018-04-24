#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 24 Apr 2018 11:11:51 AM CST
# File Name: classesAndObjects_22.py
# Description:  另外一个代理例子是实现代理模式
"""


#A proxy that uraps around another object, but exposes its public attributes

class Proxy(object):
    def __init__(self, obj):
        self._obj = obj


    #Delegate attributes lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)


    #Delegate attributes assignment
    def __setattr__(self, name, value):
        if name.startswith('-'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)


    #Delegate attributes deletion
    def __delattr__(self, name):
        if name.startswith('-'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


#使用这个代理类时只需要用它来包装下其他类
class Spam(object):
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)


#Create an instance
s = Spam(2)

#Create a proxy around it
p = Proxy(s)

#Access the proxy
print(p.x)
p.bar(3)
p.x = 37
