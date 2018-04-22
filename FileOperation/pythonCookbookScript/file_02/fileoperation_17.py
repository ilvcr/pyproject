#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 08:49:56 PM CST
# File Name: fileoperation_17.py
# Description:  在程序执行时创建一个临时文件或目录, 在使用完之后自动销毁
"""

from tempfile import TemporaryFile:

with TemporaryFile('w+t') as f:
    #Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    #Seek back tk beginning and read the data
    f.seek(0)
    data = f.read()

#TemporaryFile is destoryed
