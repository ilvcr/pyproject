#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testnewsibleton.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Sat Mar 30 09:08:18 2019
# Description: 
#************************************************************************#

#Use __new__ ====> Singleton

class Singleton(object):
    def __new__(self, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class Myclass(Singleton):
    a = 1



#Use import
class My_Singleton(object):
    def foo(self):
        pass
my_singleton = My_Singleton()

from mysingle import my_singleton
my_singleton.foo()


#Use zhuangshiqi

def singleton(cls, *args, **kw):
    instance = {}
    def getinstance():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return getinstance

@singleton
class MyClass(object):









