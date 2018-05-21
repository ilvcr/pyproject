#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 14 May 2018 11:51:33 PM CST
# File Name: best_implemt_grammer_02.py
# Description:  生成器，Fibonaci数列用迭代器来实现
"""

def fibonacci():
    a, b = 0, 1

    while True:
        yield b
        a, b = b, a + b


fib = fibonacci()

result = [fib.next() for i in range(20)]

print result

'''
该函数返回一个特殊的迭代器即generator对象
'''
