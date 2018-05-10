#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 11:10:08 PM CST
# File Name: concurrent_programming_24.py
# Description:   actor 允许在一个工作者中运行任意的函数，并通过一个特殊的 Result 对象返回结果
"""

from threading import Event

class Result(object):
    def __init__(self):
        self._evt = Event()
        self._result = None


    def set_result(self, value):
        self._result = value

        self._evt.set()


    def result(self):
        self._evt.wait()
        return self._result



class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r


    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))



#Example use
worker = Worker()
worker.start()
r = worker.submit(pow, 2, 3)
print(r.result())


