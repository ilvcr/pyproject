#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 17 Apr 2018 06:07:26 PM CST
# File Name: fileoperation_05.py
# Description:  代码功能：
                        提醒用户输入一个(尚不存在的)文件名, 然后由用户输入该文件的
                        每一行, 最后将所有文本写入文本文件
"""

import os

ls = os.linesep

#get filename
while True:
    if os.path.exists(fname):
        print("ERROR: '%s' already exists" %fname)
    else:
        break

#get file content (text) lines
all = []
print("\nEnter lines ('.' by itself to quit).\n")

#loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' %(x, ls) for x in all])
fobj.close()
print 'DONE!'
