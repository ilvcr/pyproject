#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 21 Apr 2018 12:06:34 AM CST
# File Name: deffunction_10.py
# Description:  函数的某些参数强制使用关键字传递参数示例

                    在接受任意多个位置参数的函数中指定关键字参数
"""


def mininum(*values, clip=None):
    m = min(values)

    if clip is not None:
        m = clip if clip > m else m

    return m


print(mininum(1, 5, 2, -5, 10))
print(mininum(1, 5, 2, -5, 10, clip=0))
