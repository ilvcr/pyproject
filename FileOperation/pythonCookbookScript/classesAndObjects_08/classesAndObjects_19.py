#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 24 Apr 2018 09:57:06 AM CST
# File Name: classesAndObjects_19.py
# Description:  实现自定义容器, 比如列表和字典
                    collections 定义了很多抽象基类, 对自定义容器类非常有用

                    支持迭代:
                                让类继承 collections.Iterable
                                注：需要实现 collections.Iterable 所有的抽象方法
"""

import collections

#示例：继承Sequence 抽象类，并且实现元素按照顺序存储
class SortedItem(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    #Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)


    #Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)  # bisect是一个在排序列表中插入元素的高效方式。可以保证元素插入后还保持顺序。



items = SortedItem([5, 1, 3])
print(list(items))
print(items[0], items[-1])
items.add(2)
print(list(items))
