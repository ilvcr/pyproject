#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: numpytest07.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 16:47:13 2019
# Description: 
#************************************************************************#

import numpy as np

arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print "\n"
print arr
print "\n"
print arr[[4, 3, 0, 6]]
print "\n"

arr1 = np.arange(32).reshape((8, 4))
print arr1
print "\n"
print arr1.T
print "\n"
arr2 = np.random.randn(6, 3)
print arr2
print "\n"
arr3 = np.arange(16).reshape((2, 2, 4))
print arr3
print "\n"
print arr3.transpose((1, 0, 2))
print "\n"
