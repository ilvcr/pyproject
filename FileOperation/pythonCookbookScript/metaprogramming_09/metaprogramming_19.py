#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 12:44:56 AM CST
# File Name: metaprogramming_19.py
# Description:  定义有可选参数的元类
                    使用metaclass关键字参数来指定特定的元类如抽象基类
"""

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass


    @abstractmethod
    def write(self, data):
        pass


class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    pass

#为了使元类支持这些关键字参数, 须确保在__prepare__(),__new__()和__init__() 方法中都使用强制关键字参数
class MyMeta(type):
    #OPtional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        #Custom processing
        pass
        return super().__prepare__(name, bases)

    #Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        #Custom processing
        pass
        return super().__new__(cls, name, bases, ns)


    #Required
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        #Custom processing
        pass
        super().__init__(name, bases, ns)

