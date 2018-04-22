#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 12 Apr 2018 05:13:17 PM CST
# File Name: csv2json.py
# Description:使用Pyhon来写一个程序读取行信息并把它们转换成JSON格式
"""
'''
假设CSV文件名为enronEmail.csv并且内容如下(前三行)
name, email_id
"Lysa Akin", lysa.akin@enron.com
"Phillip Allen", k..allen@enron.com
"Harry Arrora", harry.arrora@enron.com
'''

import json
import csv

#读取csv文件
with open("enronEmail.csv") as file:
    file_csv = csv.DictReader(file)
    output = '['
    #处理每一个目录
    for row in file_csv:
        #两个实体间加入逗号
        output += json.dumps(row) + ','
    output = output.rstrip(',') + ']'

#把文件写入磁盘中
f.open('enronEmailPy.json', 'w')#enronEmailPy为处理后的文件
f.write(output)
f.close()

