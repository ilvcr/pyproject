#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: numpytest05.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 16:24:16 2019
# Description: 
#************************************************************************#


import numpy as np

arr3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10 ,11, 12]]])
print "\n"
print arr3d
print "\n"
print arr3d[0]
print "\n"
old_values = arr3d[0].copy()
arr3d[0] = 42
print arr3d
print "\n"
arr3d[0] = old_values
print arr3d
print "\n"
#print arr3d[1, 0]
print "\n"
#print array([7, 8, 9])
print "\n"

print "\n"

print "\n"

print "\n"

print "\n"
