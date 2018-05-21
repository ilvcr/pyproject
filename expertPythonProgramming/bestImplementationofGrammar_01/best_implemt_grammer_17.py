#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 03:21:14 PM CST
# File Name: best_implemt_grammer_17.py
# Description:  上下文提供者
"""

from threading import RLock
lock = RLock()

def synchronized(function):
    def _synchronized(*args, **kwargs):
        lock.acquire()
        try:
            return function(*args, **kwargs)
        finally:
            lock.release()

        return _synchronized


@locker
def thread_safe():   #make sure it licks the resource
    pass


