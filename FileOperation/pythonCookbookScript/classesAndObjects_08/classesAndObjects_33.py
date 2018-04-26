#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 26 Apr 2018 01:46:56 PM CST
# File Name: classesAndObjects_33.py
# Description:  循环引用数据结构的内存管理
                    一个简单的循环引用数据结构例子就是一个树形结构，双亲节点有指针指向孩子节点，
                    孩子节点又返回来指向双亲节点。这种情况下可以考虑使用 weakref 库中的弱引用。
"""

import weakref

class Node(object):
    def __init__(self, value):
        self.value = value
        self._parent = Node
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)


    #property that manages the parent as a weak-reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)


    def add_child(self, child):
        self.children.append(child)
        child.parent = self



#class just to illustrate when deletion occur
class Data(object):
    def __del__(self):
        print("Data.__del__")


#Node class involving a cycle
class Node(object):
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
