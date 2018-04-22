#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 17 Apr 2018 05:25:58 PM CST
# File Name: generators_01.py
# Description:  问题：
                    想以数据管道 (类似 Unix 管道) 的方式迭代处理数据。比如有个大量的数据
                    需要处理，但是不能将它们一次性放入内存中。
                代码功能：
                    为了处理日志文件文件，可以定义一个由多个执行特定任务独立任务的简单生成器函
                    数组成的容器的脚本。
"""

import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    '''
    Find all filename in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.ealk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

def gen_opener(filenames):
    '''
    Open a sequence of filename one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence od iterators together into a single sequence
    '''
    for it in iterators:
        yield from it # yield from将yield 操作代理到父生成器上去语句yield from it简单的返回生成器 it 所产生的所有值

def gen_grep(pattern, ;ines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


'''
查找包含单词python的所有日志行
'''
lognames = gen_find('access-log', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)



'''
‘’‘
计算出传输字节数并计算总和
’‘’
lognames = gen_find('access-log', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
bytes = (int(x) for x in bytecolumn if x != '-')
print('Total', sum(bytes))
'''
