#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testRLock.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 13:42:22 2019
# Description: 
#************************************************************************#


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
def thread_safe():
    pass















