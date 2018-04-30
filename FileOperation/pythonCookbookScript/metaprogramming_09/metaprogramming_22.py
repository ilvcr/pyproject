#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 01:17:26 AM CST
# File Name: metaprogramming_22.py
# Description:  在类上强制使用编程规约
"""

#想监控类的定义，通常可以通过定义一个元类。
#一个基本元类通常是继承自type 并重定义它的__new__() 方法或者是__init__() 方法。

class MyMeta(types):
    def __new__(self, clsname, bases, clsdict):
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary
        return super().__new__(cls, clsname, bases, clsdict)


#另一种方法为定义__init__()方法
class MyMeta1(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary


#为了使用此元类通常要将其放到到一个顶级父类定义中，然后其他的类继承这个顶级父类
class Root(metaclass=MyMeta):
    pass

class A(Root):
    pass

class B(Root):
    pass
