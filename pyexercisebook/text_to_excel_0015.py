#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: text_to_excel_0015.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月25日 星期一 22时20分08秒
#Description: 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）：
            {
                "1" : "上海",
                    "2" : "北京",
                        "3" : "成都"

            }

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

import xlwt
import json
import sys
reload(sys)

sys.setdefaultencoding('utf8')

file = xlwt.Working(encoding='utf-8')
table = file.add_sheet('city', cell_overwrite_ok=True)
txt = open('city.txt').read()
json_txt = json.loads(txt)
for x in range(len(json_txt)):
    table.write(x, 0, x+1)
    table.write(x, 1, json_txt[str(x+1)])
file.save('city.xls')


