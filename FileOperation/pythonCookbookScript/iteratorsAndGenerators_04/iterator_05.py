#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 09:29:36 PM CST
# File Name: iterator_05.py
# Description:
                代码功能: 在自定义类上实现__reversed__()方法来实现反向迭代
"""

class Countdown(object):
    def __init__(self, start):
        self.start = start

    #Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    #Reversed iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)

for rr in Countdown(30):
    print(rr)
