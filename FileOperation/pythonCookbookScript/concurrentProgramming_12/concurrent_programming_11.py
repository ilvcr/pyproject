#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 06:50:52 PM CST
# File Name: concurrent_programming_11.py
# Description:  显式获取和释放锁
"""

import threading

class ShareCounter(object):
    '''
    A counter object that can be shared by multiple threads.
    '''
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()


    def incr(self, delta=1):
        '''
        Increment the counter with locking
        '''
        self._value_lock.acquire()
        self._value += delta
        self._value_lock.release()


    def decr(self, delta=1):
        '''
        Decrement the counter with locking
        '''
        self._value_lock.acquire()
        self._value -= delta
        self._value_lock.release()


