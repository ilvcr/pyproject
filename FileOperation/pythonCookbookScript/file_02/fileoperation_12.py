#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 07:47:09 PM CST
# File Name: fileoperation_12.py
# Description:  使用mmap模块来内存映射文件.
                代码功能：
                        如何让打开一个文件并以一种便携方式内存映射这个文件
"""

import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_EDWR)
    return mmap.mmap(fd, size, access=access)
