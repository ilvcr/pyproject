#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: numpytest02.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 16:03:31 2019
# Description: 
#************************************************************************#

import numpy as np

arr1 = np.array([1, 2, 3], dtype=np.float64)

arr2 = np.array([1, 2, 3], dtype=np.int32)

print "\n"
print arr1.dtype
print "\n"
print arr2.dtype
print "\n"

arr = np.array([1, 2, 3, 4, 5])

print "\n"
print np.dtype

print "\n"
float_arr = arr.astype(np.float64)
print float_arr.dtype
print "\n"
print "\n"


numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
print numeric_strings.dtype
print "\n"







