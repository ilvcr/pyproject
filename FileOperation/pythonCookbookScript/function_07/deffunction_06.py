#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 04:51:50 PM CST
# File Name: deffunction_06.py
# Description:  和deffunction_05.py闭包类比较的一个普通类
"""

class Stack2(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)
