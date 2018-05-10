#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 11:26:19 PM CST
# File Name: concurrent_programming_28.py
# Description:  使用上下文管理器协议在交换机对象上增加一个 subscribe() 方法
"""

from contextlib import contextmanager
from collections import defaultdict

class Exchange(object):
    def __init__(self):
        self._subscribers = set()


    def attach(self, task):
        self._subscribers.add(task)


    def detach(self, task):
        self._subscribers.remove(task)


    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)

        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)


    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)


# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]
