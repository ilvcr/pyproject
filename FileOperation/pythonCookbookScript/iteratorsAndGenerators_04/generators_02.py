#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 17 Apr 2018 05:50:57 PM CST
# File Name: generators_02.py
# Description:  代码功能：
                        将一个多层嵌套的序列展开成一个单层列表
"""

#yield from 实现
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            '''
            isinstance(x, Iterable) 检查某个元素是否是可迭代的.如果是，
            yield from 就会返回所有子例程的值.最终返回结果就是一个没有嵌套的简单序列
            '''
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]

for x in flatten(items):
    print(x)

