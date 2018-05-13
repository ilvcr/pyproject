#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 11 May 2018 03:19:00 PM CST
# File Name: scripting_and_system_management_09.py
# Description:  实现一个计时器, 记录程序执行多个任务所花费的时间
"""

#time 模块包含很多函数来执行跟时间有关的函数。在此基础之上构造一个更高级的接口来模拟一个计时器

import time

class Timer(object):
    '''
    这个类定义了一个可以被用户根据需要启动、停止和重置的计时器。
    会在elapsed 属性中记录整个消耗时间。
    '''

    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None


    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()


    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0


    @property
    def running(self):
        return self._start is not None


    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()


#A Sample Use
def countdown(n):
    while n > 0:
        n -= 1


#Use 1: Explicit start/stop
t = Timer()
t.start()
countdown(10000000)
t.stop()
print(t.elapsed)


# Use 2: As a context manager
with t:
    countdown(10000000)

print(t.elapsed)

with Timer() as t2:
    countdown(10000000)
print(t2.elapsed)


