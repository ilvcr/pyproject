#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: numpytest04.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 16:16:26 2019
# Description: 
#************************************************************************#

import numpy as np

arr = np.arange(10)
print "\n"
print "\n"
print arr
print "\n"
print "\n"
print arr[5]
print "\n"
print "\n"
print arr[5:8]
print "\n"
print "\n"
arr[5:8] = 12
print arr
print "\n"
print "\n"
arr_slice = arr[5:8]
arr_slice[1] = 12345
print arr
print "\n"
print "\n"
arr_slice[:] = 64
print arr
print "\n"
print "\n"
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print arr2d[2]
print arr2d[0][2]
print arr2d[0, 2]
print "\n"
print "\n"
