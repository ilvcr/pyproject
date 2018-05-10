#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 08 May 2018 06:50:44 PM CST
# File Name: concurrent_programming_04.py
# Description:  通过继承 Thread 类来实现线程
"""

from threading import Thread

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = 0

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(2)

c = CountdownThread(5)
c.start()

#通过 multiprocessing 模块在一个单独的进程中执行代码
import multiprocessing
c = CountdownThread(5)
p = multiprocessing.Process(target=c.run)
p.start()
