#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 26 Apr 2018 02:13:58 PM CST
# File Name: classesAndObjects_36.py
# Description:  使用一个全局变量，并且工厂函数跟类放在一块。
                    可以通过将缓存代码放到一个单独的缓存管理器中
"""

import weakref

class CacheSpamManager(object):
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]

        return s


class Spam(object):
    manager = CacheSpamManager()

    def __init__(self, name):
        self.name = name

    def get_spam(name):
        return Spam.manager.get_spam(name)
