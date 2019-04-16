#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: teststr_02.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr  5 21:27:21 2019
# Description: 
#************************************************************************#

_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2012, 12, 21)
print format(d)
print '===================\n'
print format(d, 'mdy')
print '===================\n'
print 'The date is {:ymd}'.format(d)
print '===================\n'
print 'The date is {:mdy}'.format(d)
print '===================\n'

from datetime import date

d = date(2012, 12, 21)
print format(d)
print '===================\n'
print format(d, '%A, %B %d, %Y')
print '===================\n'
print 'The end is {:%d %b %Y}. Goodbye'.format(d)







