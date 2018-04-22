#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 19 Apr 2018 08:54:53 PM CST
# File Name: rdandwtBinaryArrayData_expand.py
# Description:      用很多种方法来读取这个文件并返回一个元组列表
                        1->以块的形式增量读取文件
                        2->将整个文件一次性读取到一个字节字符串中，然后在分片解析
"""

#1->以块的形式增量读取文件
from struct import Struct

def read_records(formats, f):
    record_struct = Struct(formats)
    chunks = iter(lambda:f.read(record_struct.size), b'')
    return (record_struct.unpack(chunks) for chunk in chunks)

#Example
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            #Process rec
            ...


#2->将整个文件一次性读取到一个字节字符串中，然后在分片解析
from struct import Struct

def unpack_records(formats, data):
    record_struct = Struct(formats)
    return (record_struct.unpack_from(data, offset) 
            for offset in range(0, len(data)), read_records.size)

#Example
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        data = f.read()
    for rec in unpack_records('<idd', data):
        #Process rec
        ...

