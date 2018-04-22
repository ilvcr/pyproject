#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 07:39:50 PM CST
# File Name: fileoperation_10.py
# Description:  使用文件对象readinto()方法, 读取数据到一个可变数组中


                直接读取二进制数据到一个可变缓冲区中，而不需要做任何的中间复制操作。
                或者想原地修改数据并将它写回到一个文件中去。
"""

import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf
