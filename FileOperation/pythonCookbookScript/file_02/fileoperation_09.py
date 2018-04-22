#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 07:33:59 PM CST
# File Name: fileoperation_09.py
# Description:  以文本形式读取压缩文件, 写入压缩文件
"""

#gzip compression
import gzip

#读取压缩文件
with gzip.open('somefile.gzip', 'rt') as f:
    text = f.read()

#bz2 compression
import bz2
with bz2.open('somefile.bz2','rt') as f:
    text = f.read()

#写入压缩文件
#gzip compression
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

#bz2 compression
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)
