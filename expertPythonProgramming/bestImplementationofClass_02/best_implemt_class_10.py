#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 16 May 2018 11:47:44 PM CST
# File Name: best_implemt_class_10.py
# Description:  元编程
"""

#特殊方法_new_是一个元构造程序，每当一个对象必须被factory类实例化时就将调用它

class MyClass(object):
    def __new__(cls):
        print '__new__ called'
        return object.__new__(cls)  #default factory


    def __init__(self):
        print '__init__ called'
        self.a = 1


instance = MyClass()

print instance


