#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 19 Apr 2018 08:48:37 PM CST
# File Name: rdandwtBinaryArrayData.py
# Description:  将一个 Python 元组列表写入一个二进制文件，
                    并使用 struct 将每个元组编码为一个结构体。
"""

from struct import Struct

def write_records(records, formats, f):
    '''
    Write a sequence of tuples to a binary file of structures
    '''

    record_struct = Struct(formats)
    for r in records:
        f.write(record_struct.pack(*r))

#example
if __name__ == "__main__":
    records = [ (1, 2.3, 4.5),
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]

    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)
