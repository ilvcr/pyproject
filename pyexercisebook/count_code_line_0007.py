#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: count_code_line_0007.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月22日 星期五 17时11分25秒
#Description:  有个目录里是自己写过的程序，统计一下写过多少行代码。
                    包括空行和注释，但是要分别列出来。
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

import os
import re

def stat_code(dir_path):
    if not os.path.isdir(dir_path):
        return

    exp_re = re.compile(r'^#.*')
    file_list = os.listdir(dir_path)
    print '{}\t{}\t{}\t{}'.format('file', 'all_lines', 'space_lines', 'exp_lines')
    for file_in in file_list:
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == '.py':
            with open(file_path) as f:
                all_lines = 0
                space_lines = 0
                exp_lines = 0
                for line in f.readlines():
                    all_lines += 1
                    if line.strip() == '':
                        space_lines += 1
                        continue
                    exp = exp_re.findall(line.strip())
                    if exp:
                        exp_lines += 1
            print '{}\t{}\t{}\t{}'.format(file, all_lines, space_lines, exp_lines)

if __name__ == '__main__':
    stat_code('.')



