#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: cleandatatest01.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 17:58:53 2019
# Description: 
#************************************************************************#


from pandas import Series, DataFrame
import pandas as pd
import numpy as np

df1 = DataFrame({'key' : ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1' : range(7)})
print "\n"
print df1
df2 = DataFrame({'key' : ['a', 'b', 'd'], 'data2' : range(3)})
print "\n"
print df2
print "\n"
print pd.merge(df1, df2)
print "\n"
print pd.merge(df1, df2, on='key')
print "\n"

print "\n"

print "\n"

print "\n"

print "\n"

print "\n"
