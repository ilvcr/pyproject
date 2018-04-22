#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 13 Apr 2018 04:34:32 PM CST
# File Name: datastaAlg_01.py
# Description:利用heapq实现一个简单的优先级队列
"""

import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = ()

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item)) #队列包含了一个 (-priority, index, item) 的元组。
                                                                    #优先级为负数的目的是使得元素按照优先级从高到低排序。
                                                                    #这个跟普通的按优先级从低到高排序的堆排序恰巧相反。
        self._index += 1 #index 变量的作用是保证同等优先级元素的正确排序。
                         #通过保存一个不断增加的index 下标变量，可以确保元素按照它们插入的顺序排序。
                         #而且， index 变量也在相同优先级元素比较的时候起到重要作用。

    def pop(self):
        return heapq.heappop(self._queue)[-1] #heappop() 函数总是返回”最小的” 的元素，这就是保证队列 pop 操作返回正确元素的关键。

'''
上述代码使用方法:

class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
q.pop()
q.pop()
q.pop()
'''
