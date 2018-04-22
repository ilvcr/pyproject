#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 07:43:46 PM CST
# File Name: fileoperation_11.py
# Description:  读取一个由相同大小的记录组成的二进制文件
"""

record_size = 32  #Size of each record (adjust value)

buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break

        #Next  Usethe contents of buf
