#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 17 Apr 2018 05:57:23 PM CST
# File Name: generators_03.py
# Description:  代码功能：
                        合并两个排序文件
"""

#filename1，filename2为合并前的两个文件名,merged_file 为合并后的文件名

with open('filename1', 'rt') as file1, open('filename2', 'rt') as file2, open('merged_file', 'wt') as outf:
    for line in heapq.merged(file1, file2):
        out.write(line)

'''
强调:
    heapq.merge() 需要所有输入序列必须是排过序的。特别的，它并不会预先读取所有数据到堆栈中或者预先排序，
    也不会对输入做任何的排序检测。它仅仅是检查所有序列的开始部分并返回最小的那个，
    这个过程一直会持续直到所有输入序列中的元素都被遍历完。
'''

