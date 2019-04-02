#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: numpytest06.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 16:29:38 2019
# Description: 
#************************************************************************#

import numpy as np
import random

names = np.array(['bob', 'joe', 'will', 'bob', 'will', 'joe', 'joe'])
print "\n"
print names
print "\n"
data = np.random.randn(7, 4)
print "\n"
print data
print "\n"
print names == 'bob'
print "\n"
print data[names == 'bob']
print "\n"
print names != 'bob'
print "\n"
mask = (names == 'bob') | (names == 'will')
print mask
print "\n"
print data[mask]
data[data < 0] = 0
print data
print "\n"
data[names != 'joe'] = 7
print data
print "\n"

print "\n"
