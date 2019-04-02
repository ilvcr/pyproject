#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: numpytest.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 15:48:44 2019
# Description: 
#************************************************************************#

import numpy as np

data1 = [0.96526, -0.246, -0.8856, 0.5639, 0.2379, 0.9104]

arr1 = np.array(data1)

print arr1

print "\n"

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

arr2 = np.array(data2)

print arr2

print "\n"


print "arr2.ndim : {}".format(arr2.ndim)
#print arr2.ndim
print "\n"
print "\n"
print "arr2.shape : {}".format(arr2.shape)
print "\n"
print "\n"

print "arr1.dype : {}".format(arr1.dtype)
print "\n"
print "\n"
print "arr2.dype : {}".format(arr2.dtype)
print "\n"
print "\n"
print "np.zeros(0) : {}".format(np.zeros(0))
print "\n"
print "\n"
print "np.zeros((3, 6)) : {}".format(np.zeros((3, 6)))
print "\n"
print "\n"
print "np.empty((2, 3, 2)) : {}".format(np.empty((2, 3, 2)))
print "\n"
print "\n"

print "\n"

print "\n"
