#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 26 Apr 2018 02:18:40 PM CST
# File Name: classesAndObjects_37.py
# Description:  将类的名字修改为以下划线 ( ) 开头，提示用户别直接调用它。
                    第二种就是让这个类的 init () 方法抛出一个异常，让它不能被初始化
                        然后修改缓存管理器代码， 使用 Spam. new() 来创建实例， 而不是直接调用 Spam()构造函数
"""

import weakref


class CacheSpamManager2(object):
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()


    def get_spam(self, name):
        if name not in self._cache:
            temp = Spam3._new(name) #Modified creation
            self._cache[name] = temp

        else:
            temp = self._cache[name]

        return temp

class Spam3(object):
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantitate directly")

    #Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self
