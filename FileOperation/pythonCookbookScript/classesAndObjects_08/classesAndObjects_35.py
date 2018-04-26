#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 26 Apr 2018 02:09:50 PM CST
# File Name: classesAndObjects_35.py
# Description:  希望相同参数创建的对象时单例的, 需要使用一个和类本身分开的工厂函数
                    在很多库中都有实际的例子，比如 logging 模块，使用相同的名称创建的 logger 实例永远只有一个
"""


#The class in queation

class Spam(object):
    def __init__(self, name):
        self.name = name


#Caching support
import weakref
_apam_cache = weakref.WeakValueDictionary()
def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s

    else:
        s = _spam_cache[name]

    return s
