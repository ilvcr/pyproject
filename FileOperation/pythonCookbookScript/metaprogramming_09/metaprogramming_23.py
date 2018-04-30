#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 01:24:51 AM CST
# File Name: metaprogramming_23.py
# Description:  定义一个元类会拒绝任何有混合大小写名字作为方法的类定义
"""

class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)


class Root(metaclass=NoMixedCaseMeta):
    pass

class A(Root):
    def foo_bar(self):
        pass

class B(Root):
    def fooBar(self): #TypeError
        pass


#定义一个元类用来检测重载方法，确保它的调用参数跟父类中原始方法有着相同的参数签名
from inspect import signature
import logging

class MatchSignaturesMeta(Type):

    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswitch('_') or not callable(value):
                continue

            #Get the previous defintion (if any) and compare the signature
            prev_dfn = signature(prev_dfn)
            val_sig = signature(value)
            if prev_sig != val_sig:
                logging,warning('Signature mismatch in %s. %s != %s', value.__qualname__, prev_sig, val_sig)

#Example
class Root(metaclass=MatchSignaturesMeta):
    pass

class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass


#Class with redefines methods, but slightly different signature
class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass
