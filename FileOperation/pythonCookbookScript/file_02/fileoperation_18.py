#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 08:54:20 PM CST
# File Name: fileoperation_18.py
# Description: 一个在内部定义一个线程但仍然可以序列化和反序列化的类
"""

import time
import threading

class Countdown(object):
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate_(self, n):
        self.__init__(n)
