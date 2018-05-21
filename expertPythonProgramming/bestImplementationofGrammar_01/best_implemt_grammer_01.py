#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 14 May 2018 11:46:47 PM CST
# File Name: best_implemt_grammer_01.py
# Description:  创建定制的类，编写一个next方法的类，提供返回迭代器的__iter__特殊方法
"""

class MyIterator(object):
    def __init__(self, step):
        self.step = step

    def next(self):
        """Returns the next element"""
        if self.step == 0:
            raise StopIteration

        self.step -= 1

        return self.step

    def __iter__(self):
        """Returns the iterator itself"""
        return self


for el in MyIterator(4):
    print el
