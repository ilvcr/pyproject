#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 17 Apr 2018 06:23:31 PM CST
# File Name: fileoperation_07.py
# Description:  代码功能：
                        创建一个文本文件, 写入少量数据,然后重命名,输出文件内容,
                        最后进行一些辅助性的操作,比如便利目录树和文件路径名处理
"""

#练习使用os和os.path模块中的功能

import os

for tmpdir in ('/tmp', r'c:\temp'): #以这两个文件目录为例
    if os.path.isdir(tmpdir):
        break

    else:
        print("no temp directory available")
        tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print("*** current temporary directory")
    print(cwd)

    print('*** currenting example directory...')
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print("*** new working directory:")
    print cwd
    print("*** original directory listing:")
    print(os.listdir(cwd))

    print("*** creating test file...")
    fobj = open('test', 'w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print("*** update directory listing:")
    print(os.listdir(cwd))

    print("*** rename 'test' to 'filetest.txt'")
    os.rename('test', 'filetest.txt')
    print("*** update directory listing:")
    print(os.listdir(cwd))

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print("*** full file pathname")
    print(path)
    print("*** (pathname, basename) ==")
    print(os.path.split(path))
    print("*** (filrname, extension) ===")
    print(os.path.splittext(os.path.basename(path)))

    print("*** displaying file contents:")
    fobj = open(path)
    for eachLine in fobj:
        print(eachLine)
    fobj.close()

    print("*** deleting test file")
    os.remove(path)
    print("*** updated directory listing:")
    print(os.listdir(cwd))
    os.chdir(os.pardir)
    print("*** deleting test directory")
    os.rmdir('example')
    print("*** DONE!")
