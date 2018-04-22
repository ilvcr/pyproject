#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 12 Apr 2018 05:24:31 PM CST
# File Name: json2csv.py
# Description:使用python读取JSON文件并将它转换成CSV文件，
                本程序利用一个名为enronEmailPy.json的JSON
                文件，输出一个对应的CSV版本结果文件enronEmailPy.csv，
                其中的标题行信息来自于JSON中的属性
"""
import json
import csv

with open('enronEmailPy.json', 'r') as f:
    dicts = json.load(f)

out = open('enronEmailPy.csv', 'w')
writer = csv.DictWriter(out, dicts[0].keys())
writer.writerheader()
writer.writerows(dicts)
out.close()
