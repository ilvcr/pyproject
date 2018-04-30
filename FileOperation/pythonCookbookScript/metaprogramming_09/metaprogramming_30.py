#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 03:50:35 AM CST
# File Name: metaprogramming_30.py
# Description:  定义上下文管理器的简单方法
                    实现一个新的上下文管理器的最简单的方法就是使用 contexlib 模块中的@contextmanager 装饰器
"""


#实现代码块计时功能的上下文管理器例子
import time
from contextlib import contextmanager

@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}:{}'.format(label, end - start))


#Example use
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working
