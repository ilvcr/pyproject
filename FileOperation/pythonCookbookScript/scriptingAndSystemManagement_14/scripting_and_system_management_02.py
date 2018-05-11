#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 11 May 2018 02:30:55 PM CST
# File Name: scripting_and_system_management_02.py
# Description:  解析命令行选项, argparse 模块可被用来解析命令行选项
"""


#search.py

'''
Hypothetical command-line tool for searching a collection of files for one or more text patterns.
'''

import argparse

parser = argparse.ArgumentParser(description='Search some files')

parser.add_argument(dest='filename', metavar='filename', nargs='*')
#用来构造一个文件名列表


parser.add_argument('-p', '--pat', metavar='pattern', required=True, dest='patterns', action='append',help='text pattern to search for')
#允许某个参数重复出现多次，并将它们追加到一个列表中去。required 标志表示该参数至少要有一个。-p 和 --pat 表示两个参数名形式都可使用。


parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
#根据参数是否存在来设置一个 Boolean 标志


parser.add_argument('-o', dest='outfile', action='store', help='output file')
#接受一个单独值并将其存储为一个字符串


parser.add_argument('--speed', dest='speed', action='store', choices={'slow','fast'}, default='slow', help='search speed')
#接受一个值，但是会将其和可能的选择值做比较，以检测其合法性


args = parser.parse_args()

#Output the collected arguments
print(args.filename)

print(args.patterns)

print(args.verbose)

print(args.outfile)
