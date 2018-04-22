#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 06:25:42 PM CST
# File Name: iterator_01.py
# Description:  代码功能:手动读取一个文件中的所有行
                            '/etc/passwd'为函数路径
"""

def manual_iter():
    with open('/etc/passwd') as f:

        try:
            while True:
                line = next(f)
                print(line, end='')

        except StopIteration:  #StopIteration 用来指示迭代的结尾
            pass


'''
#手动使用 next() 函数，可以通过返回一个指定值来标记结尾,比如None
with open('/etc/passwd') as f:
    while True:
        line = next(f)
        if line is None:
            break
        print(line, end='')
'''
