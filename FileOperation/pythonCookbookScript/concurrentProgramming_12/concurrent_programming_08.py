#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 06:30:09 PM CST
# File Name: concurrent_programming_08.py
# Description:  创建一个线程安全的优先级队列
"""

import heapq
import threading

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._count = ()
        self._cv = threading.Condition()

    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]
