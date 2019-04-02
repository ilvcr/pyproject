#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: pandastest01.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 17:23:32 2019
# Description: 
#************************************************************************#

import pandas as pd
from pandas import Series, DataFrame

obj = Series([4, 7, -5, 3])
print obj
print "\n"
print obj.values
print "\n"
print "\n"
print obj.index
print "\n"
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print obj2
print "\n"
print obj2.index
print "\n"
print obj2['a']
print "\n"
obj2['d'] = 6
print "\n"
print obj2[['c', 'a', 'd']]
print "\n"
print obj2
print "\n"
print obj2[obj2 > 0]
print "\n"
print 'b' in obj2
print "\n"
print 'e' in obj2
print "\n"
