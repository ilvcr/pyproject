#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 07:53:41 PM CST
# File Name: fileoperation_13.py
# Description:  获取文件系统目录下所有的文件列表
"""

#使用os.listdir()函数来获取某个目录文件中的文件列表
import os
names = os.listdir('somedir')  #返回目录中所有的文件列表,包括文件、子目录、符号链接

#带有过滤性质的函数式编程目录遍历
import os.path
#Get all regular files
names = [name for name in os.listdir('somedir') if os.path.isfile(os.path.join('somefile', name))]

#Get all dirs
dirnames = [name for name in os.listdir('somefile') if os.path.isdir(os.path.join('somefile', name))]

#字符串的startswith() 和endswith()方法可以过滤一个目录的内容
pyfiles = [name for name in os.listdir('somedir') if name.endswith('.py')]


#匹配文件名,glob或者fnmatch模块
import glob
pyfiles = glob.glob('somedir/*.py')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir') if fnmatch(name, '*.py')]




