#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 11 May 2018 02:18:24 PM CST
# File Name: scripting_and_system_management_01.py
# Description:  Python 内置的 fileinput 模块让重定向/管道/文件接受输入变得简单
"""

from __future__ import print_function
import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, "")



'''
$ ls j ./filein.py # Prints a directory listing to stdout.
$ ./filein.py /etc/passwd # Reads /etc/passwd to stdout.
$ ./filein.py < /etc/passwd # Reads /etc/passwd to stdout.
'''
