#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: pandastest03.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 17:45:11 2019
# Description: 
#************************************************************************#


import numpy as np
from pandas import Series, DataFrame
import pandas as pd

data = {'state' : ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year' : [2000, 2001, 2002, 2001, 2001],
        'pop' : [1.5, 1.7, 3.6, 2.4, 2.9]}
print "\n"
print data
print "\n"
frame = DataFrame(data)
print frame
print "\n"
print DataFrame(data, columns=['year', 'state', 'pop'])
print "\n"
frame2 = DataFrame(data, columns=['years', 'state', 'pop', 'debt'],
                    index=['one', 'two', 'three', 'four', 'five'])
print frame2
print "\n"
print frame2.columns
print "\n"
print frame2['state']
print "\n"
print frame2.years
print "\n"
print frame2.ix['three']
print "\n"
frame2['debt'] = 16.5
print frame2
print "\n"
frame2['debt'] = np.arange(5.)
print frame2
print "\n"

print "\n"

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame['debt'] = val
print frame2
print "\n"

print "\n"

print "\n"

print "\n"
