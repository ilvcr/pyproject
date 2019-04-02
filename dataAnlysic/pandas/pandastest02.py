#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: pandastest02.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 17:32:40 2019
# Description: 
#************************************************************************#


import pandas as pd
from pandas import Series, DataFrame

sdata = {'Ohio' : 35000, 'Texas' : 71000, 'Oregon' : 16000, 'Utah' : 5000}
print "\n"
print sdata
print "\n"
obj3 = Series(sdata)
print obj3
print "\n"
states = ['California', 'Ohio', 'Oregon', 'Texas']
print states
print "\n"
obj4 = Series(sdata, index=states)
print obj4
print "\n"
print pd.isnull(obj4)
print "\n"
print pd.notnull(obj4)
print "\n"
print obj4.isnull()
print "\n"
print obj3
print "\n"
print obj4
print "\n"
print obj3 + obj4
print "\n"
obj4.name = 'population'
obj4.index.name = 'state'
print obj4
print "\n"
obj4.index = ['bob', 'steve', 'jeff', 'ryan']
print obj4
print "\n"
