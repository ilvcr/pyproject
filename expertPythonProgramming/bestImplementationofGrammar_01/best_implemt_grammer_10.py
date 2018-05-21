#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 02:11:52 PM CST
# File Name: best_implemt_grammer_10.py
# Description:  itertools模块的islice: 窗口迭代器
"""

#islice将返回第一个运行在序列的子分组上的迭代器

import itertools

def starting_at_five():
    '''
    按行从标准输出中读取信息，并且输出从第5行开始的每个元素
    '''
    value = raw_input().strip()

    while value != '':
        for el in itertools.islice(value.split(), 4, None):
            yield el

        value = raw_input().strip()


n = 5

iter = starting_at_five()

while n > 0:
    print iter.next()
    n -= 1
