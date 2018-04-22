#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 09:16:36 PM CST
# File Name: iterator_04.py
# Description：
                背景：Python 的迭代协议要求一个 iter () 方法返回一个特殊的迭代器对象，这个迭
                代器对象实现了 next () 方法并通过 StopIteration 异常标识迭代的完成。但是，
                实现这些通常会比较繁琐。

                代码功能：使用一个关联迭代器类重新实现depth_first()方法
"""

class Node(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        #Return myself if just atarted; created an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        #If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)

        #Advance to the next child and its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)
