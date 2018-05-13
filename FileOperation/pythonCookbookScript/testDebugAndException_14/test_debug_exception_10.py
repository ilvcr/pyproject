#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 12 May 2018 10:34:05 PM CST
# File Name: test_debug_exception_10.py
# Description:  利用上下文管理器来测试代码的运行时间
"""

from contextlib import contextmanager
import time

@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))


#使用上下文管理器
with timeblock('counting'):
    n = 1000000
    while n > 0:
        n -= 1


