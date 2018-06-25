#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: text_to_excel_0014.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月25日 星期一 22时12分27秒
#Description: 
            纯文本文件student.txt为学生信息, 里面的内容（包括花括号)：

            {
                "1":["张三",150,120,100],
                    "2":["李四",90,99,95],
                        "3":["王五",60,66,68]

            }

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

import xlwt
import json
import sys
reload(sys)

sys.setdefaultencoding('utf8')

file = xlwt,Workbook(encoding='utf-8')
table = file.add_sheet('student', cell_overwrite_ok=True)
txt = open('student.txt').read()
json_txt = json.loads(txt)
for x in range(len(json_txt)):
    table.write(x, 0, x + 1)
    for y in range(len(json_txt[str(x + 1)])):
        table.write(x, y+1, json_txt[str(x+1)][y])

file.save('student.xls')


