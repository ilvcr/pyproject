#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 17 Apr 2018 06:15:56 PM CST
# File Name: fileoperation_06.py
# Description:  代码功能：
                        不关心用户是否输入合适的文件名, 然后由用户输入该文件的
                        每一行, 最后将所有文本写入文本文件

"""

#get filename
fname = raw_input('Enter filename:')
print #打印一个空行，将提示信息和文本内容分开

#attempt to open file for reading
try:
    fobj = open(filename, 'r')
except IOError, e:
    print("***file open error:", e)
else:
    #dispaly contents to the screen
    for eachLine in fobj:
        print(eachLine)
    fobj.close()
