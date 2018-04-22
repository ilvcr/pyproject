#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 13 Apr 2018 02:18:04 PM CST
# File Name: fileoperation_01.py
# Description: 将文件中的某个字符串改成另一个
               字符串替换最简单的办法 ：replace

               本代码的功能为从一个特定的文件(或标准输入)读取数据, 然后写入一个指定的文件
               (或标准输出)
"""

import os
import sys

nargs = len(sys.argv)

if not 3 <= nargs <= 5:
    print("usage:%s search_text replace_text [infile [outfile]]" %(os.path.basename(sys.argv[0])))

else:
    stext = sys.argv[1]
    rtext = sys.argv[2]
    input_file = sys.stdin
    output_file = sys.stdout
    if nargs > 3:
        input_file = open(sys.argv[3])
    if nargv > 4:
        output_file = open(sys.argv[4], 'w')

    for s in input_file:
        output_file.write(s.replace(stext, rtext))
    #代替循环
    #output_file.write(input_file.read().replace(stext, rtext))

    output_file.close(
    input_file.close()
