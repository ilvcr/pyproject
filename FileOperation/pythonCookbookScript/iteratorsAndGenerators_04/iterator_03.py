#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 08:59:02 PM CST
# File Name: iterator_03.py
# Description:  实现一个以深度优先方式遍历树形节点的生成器
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
        '''
        depth_first() 首先返回自己本身并迭代每一个子节点并通过调用子节点的 depth_first() 方法 (使用 yield from 语句) 返回对应元素。
        '''
        yield self
        for c in self:
            yield from c.depth_first()

#Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

    #Output Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)
