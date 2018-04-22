#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 13 Apr 2018 02:34:00 PM CST
# File Name: fileoperation_02.py
# Description:根据给出的行号, 从文本文件中读取一行数据
"""

import linecache
theline = linecache.getline(thefilepath, desired_line_number)

'''
#对getline的重新封装
#使用显式循环, 提高linecache的搜索速度

def getline(thefilepath, desired_line_number):
    if desired_line_number < 1:
        return ''

    for current_line_number, line in enumerate(open(thefilepath, 'rU')):
        if current_line_number == desired_line_number - 1:
            return line
        return ''
'''
