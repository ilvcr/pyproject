#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 11 Apr 2018 11:04:10 PM CST
# File Name: folderProgramming.py
# Description:
"""

import os
os.mkdir(r"/home/No1File/No2File/No3File/test")#创建文件夹,必须一层一层的创建

os.rmdir(r"/home/No1File/No2File/No3File/test")#删除空文件夹

os.remove(r"/home/No1File/No2File/No3File/test")#删除文件

os.rename(r"/home/No1File/No2File/No3File/test/1.txt",r"/home/No1File/No2File/No3File/test/a.txt")#重命名文件

os.rename(r"/home/No1File/No2File/No3File/test/1",r"/home/No1File/No2File/No3File/test/x")#重命名文件夹

mylist=os.listdir(r"/home/No1File/No2File/No3File/test")
print(mylist)#列举文件夹下所有文件与文件夹
print(os.path.isfile(r"/home/No1File/No2File/No3File/test/a.txt"))#判断是文件
print(os.path.isdir(r"/home/No1File/No2File/No3File/test/x"))#判断是否文件夹
