#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 02:19:58 PM CST
# File Name: best_implemt_grammer_11.py
# Description:  itertools模块的tee: 往返式的迭代器
"""

import itertools

def with_head(iterable, headsize=1):
    '''
    读取文件的表头可以运行一个处理之前提供的特殊性信息
    '''
    a, b = itertools.tee(iterable)
    return list(itertools.islice(a, headsize)), b

seq = [1, 2, 3, 4, 5]

print with_head(seq)

print with_head(seq, 4)


