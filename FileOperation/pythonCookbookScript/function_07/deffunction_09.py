#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 11:50:24 PM CST
# File Name: deffunction_09.py
# Description:  让一个函数接受任意数量的位置参数, 可以使用一个 * 参数
"""

def avg(first, *rest):
    return (first + sum(rest)) / (1.0 + len(rest))


#Sample use
print(avg(1, 2))
print(avg(1, 2, 3, 4))
