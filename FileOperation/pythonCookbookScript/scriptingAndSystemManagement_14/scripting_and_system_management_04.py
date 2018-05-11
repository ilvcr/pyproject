#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 11 May 2018 02:49:51 PM CST
# File Name: scripting_and_system_management_04.py
# Description:  不调用 shell 命令复制或者移动文件和目录
"""

#shutil 模块有很多便捷的函数可以复制文件和目录

import shutil

#copy src to dst.(cp src dst)
shutil.copy(src, dst)

#copy file, but preserver metadata (cp -p src dst)
shutil.copy2(src, dst)

#copy directory tree (cp -R src dst)
shutil.copytree(src, dst)

#move src to dst (mv src dst)
shutil.move(src, dst)


#如果想保留被复制目录中的符号链接
shutil.copytree(src, dst, symlinks=True)


#copytree() 可以让你在复制过程中选择性的忽略某些文件或目录。可以提供一个忽略函数，
#接受一个目录名和文件名列表作为输入，返回一个忽略的名称列表。
def ignore_pyc_files(dirname, filenames):
    return [name in filenames if name.endswith('.pyc')]

shutil.copytree(src, dst, ignore=ignore_pyc_files)


