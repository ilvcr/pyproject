#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 24 Apr 2018 11:35:15 AM CST
# File Name: classesAndObjects_24.py
# Description:  手动实现方法代理
"""

class ListLike(object):
    '''__getattr__ 对于双下划线开始和结尾的方法是不能用的，需要一个个去重定义'''

    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)


    #Added special methods to support certain list operations
    def __len__(self):
        return len(self._items)
    def __getitem__(self, index):
        return self._item[index]
    def __setitem__(self, index, value):
        self._items[index] = value
    def __delitem__(self, index):
        del self._items[index]
