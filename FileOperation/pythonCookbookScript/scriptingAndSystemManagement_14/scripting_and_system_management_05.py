#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 11 May 2018 02:57:18 PM CST
# File Name: scripting_and_system_management_05.py
# Description:  通过文件名查找文件

            需要写一个涉及到文件查找操作的脚本，比如对日志归档文件的重命名工具，
            不想在 Python 脚本中调用 shell，或者要实现一些 shell 不能做的功能。
"""

#查找文件， 可使用 os.walk() 函数，传一个顶级目录名给它。
#查找特定的文件名并答应所有符合条件的文件全路径

import os

def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


if __name__ == '__main__':
    findfile(sys.argv[1], sys.argv[2])
