#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 28 Apr 2018 05:56:03 PM CST
# File Name: metaprogramming_14.py
# Description:  使用元类控制实例的创建
                    改变实例创建方式来实现单例、缓存或其他类似的特性
"""

#定义了一个类就能像函数一样的调用它来创建实例
class Spam(object):
    def __init__(self, name):
        self.name = name

a = Spam('Guido')
b = Spam('Diana')


#定义一个元类并自己实现 call () 方法
class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

#Example
class Spam1(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam1.grok')


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


#Example
class Spam2(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam2')
