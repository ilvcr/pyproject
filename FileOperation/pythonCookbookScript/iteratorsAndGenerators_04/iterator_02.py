#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 08:49:14 PM CST
# File Name: iterator_02.py
# Description:  定义一个__iter()__方法, 将迭代操作代理到容器内部的对象上,
                __iter()__方法只是简单地将迭代请求传递给内部的_children属性
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

#Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    #Outputs Node(1), Node(2)
    for ch in root:
        print(ch)

'''
Python 的迭代器协议需要 iter () 方法返回一个实现了 next () 方法的迭代器对象。

iter(s)只是简单的通过调用s.iter()方法来返回对应的迭代器对象,
跟len(s)调用s.len()原理一样。
'''
