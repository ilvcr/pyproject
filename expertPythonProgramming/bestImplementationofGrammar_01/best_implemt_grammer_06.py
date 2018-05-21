#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : 2018年05月15日 星期一 13时30分28秒
# File Name: best_implemt_grammer_06.py
# Description:  list use
"""

#1
numbers = range(10)
size = len(numbers)

evens = []

i = 0
while i < size:
    if i %2 == 0:
        evens.append(i)
    i += 1

print evens

print('*******************************')
#2

t = [i for i in range(10) if i % 2 == 0]
print t


