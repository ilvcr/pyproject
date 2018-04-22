#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 13 Apr 2018 02:47:44 PM CST
# File Name: fileoperation_03.py
# Description:计算一个文件有多少行
"""

#基准测试框架脚本
import time
import os

def timeo(fun, n =10):
    start = time.clock()
    for i in xrange(n):
        fun()
    stend = time.clock()
    thetime = stend - start
    return fun.__name__, thetime

def linecount_w():
    return int(os.popen('wc -1 nuc').read().split()[0])

def linecount_1():
    return len(open('nuc').readlines())

def linecount_2():
    count = -1
    for count, line in enumerate(open('nuc')):
        pass
    return count + 1

def linecount_3():
    count = 0
    thefile = open('nuc', 'rb')
    while True:
        buffer = thefile.read(65536)
        if not buffer:
            break
        count += buffer.count('\n')
    return count

for f in linecount_w, linecount_1, linecount_2, linecount_3:
    print(f.__name__, f())

for f in linecount_1, linecount_2, linecount_3:
    print("%s %.2f"%timeo(f))




'''
1-> 对于不大的文件, 将文件读取放入一个行列表中, 计算列表长度。
    假设文件路径由变量thefilepath指定:

count = len(open(thefilepath, 'rU').readlines())
'''

'''
2-> 对于非常大的文件, 运用循环技术的方法:

count = -1
for count, line in enumerate(open(thefilepath, 'rU)):
    pass
count += 1
'''

'''
3-> 如果行结束标记是"\n"

count = 0
thrfile = open(thefilepath, 'rb')
while True:
    buffer = thrfile.read(8129*1024)
    if not buffer:
        break
    count += buffer.count('\n')
thefile.close()
'''
