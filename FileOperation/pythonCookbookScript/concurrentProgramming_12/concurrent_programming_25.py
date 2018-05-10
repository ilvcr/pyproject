#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 11:16:50 PM CST
# File Name: concurrent_programming_25.py
# Description:  交换机实现
"""

from collections import defaultdict

class Exchange(object):
    def __init__(self):
        self._subscribers = set()


    def attach(self, task):
        self._subscribers.add(task)


    def detach(self, task):
        self._subscribers.remove(task)


    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# Dictionary of all created exchanges
_exchange = defaultdict(Exchange)


# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchange[name]


