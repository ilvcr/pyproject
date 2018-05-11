#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 11 May 2018 03:02:15 PM CST
# File Name: scripting_and_system_management_06.py
# Description:  打印所有最近被修改过的文件
"""

import os
import time

def modified_within(top, seconds):
    now = time.time()
    for path, dirs files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath)
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print(fullpath)



if __name__ == '__main__':
    import os
    if len(sys.argv) != 3:
        print('Usage: {} dir seconds'.format(sys.argv[0]))
        raise SystemExit(1)


    modified_within(sys.argv[1], float(sys.argv[2]))
