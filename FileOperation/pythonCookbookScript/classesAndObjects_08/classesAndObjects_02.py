#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 21 Apr 2018 05:23:12 PM CST
# File Name: classesAndObjects_02.py
# Description:  通过format()函数和字符串方法使得一个对象能支持自定义的格式

                    为了自定义字符串, 需要在类上面定义__format__()方法
"""

_formats ={
    'ymd' : '{d.year}-{d.month}-{d.day}}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }


class Data(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'

        fmt = _formats[code]
        return fmt.format(d=self)

d = Data(2012, 12, 21)
#print(format(d))
print("----------------------")
print(format(d, 'mdy'))
#print("----------------------")
#print('The data is {:ymd}'.format(d))
#print('The data is {:mdy}'.format(d))


