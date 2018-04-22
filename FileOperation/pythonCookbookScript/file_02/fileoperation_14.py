#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 08:09:53 PM CST
# File Name: fileoperation_14.py
# Description:  获取文件大小\修改时间等元信息
"""

#Example od getting a directory listing

import os
import os.path
import glob

pyfiles = glob.glob('*.py')

#Get file size and modification dates
name_sz_data = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]

for name, size, mtime in name_sz_date:
    print(name, size, mtime)

#Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
