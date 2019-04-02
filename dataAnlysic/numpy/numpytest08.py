#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: numpytest08.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 16:53:40 2019
# Description: 
#************************************************************************#

import numpy as np

arr = np.arange(10)
print "\n"
print arr
print "\n"
print np.sqrt(arr)
print "\n"
print np.exp(arr)
print "\n"
x = np.random.randn(8)
y = np.random.randn(8)
print "\n"
print x
print "\n"
print y
print "\n"
print np.maximum(x, y)
print "\n"

arr = np.random.randn(7) * 5
print np.modf(arr)

print "\n"
