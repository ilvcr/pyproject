#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 08 May 2018 06:37:34 PM CST
# File Name: concurrent_programming_02.py
# Description:  把线程放入一个类中
"""

import time
class CountdownTask(object):
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print("T-minus", n)
            n -= 1
            time.sleep(2)


from threading import Thread
c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate()  # Signal termination
t.join()       # Wait for actual termination (if needed)

