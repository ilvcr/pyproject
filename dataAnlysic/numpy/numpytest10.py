#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: numpytest10.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 17:06:16 2019
# Description: 
#************************************************************************#

import numpy as np

arr = np.arange(10)
np.save('some_array.npy', arr)

print np.load('some_array.npy')




