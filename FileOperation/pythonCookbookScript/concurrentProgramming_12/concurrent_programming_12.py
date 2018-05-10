#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 06:55:48 PM CST
# File Name: concurrent_programming_12.py
# Description: 实现一个SharedCounter 类
"""

import threading

class SharedCounter(object):
    '''
    A counter object that can be shared by multiple threads.
    '''

    _lock = threading.RLock()

    def __init__(self, initial_value = 0):
        self._value = initial_value


    def incr(slef, delta=1):
        '''
        Increment the counter with locking
        '''
        with SharedCounter._lock:
            self._value += delta


    def decr(self, delta=1):
        '''
        Decrement the counter with locking
        '''
        with SharedCounter._lock:
            self.incr(-delta)


