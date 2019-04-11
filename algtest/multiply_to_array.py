#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: multiply_to_array.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 22:28:52 2019
# Description: 构建乘积数组
#************************************************************************#

class Solution(object):

    def multiply_to_array(self, A):

        if not A or len(A) <= 0:
            return 

        length = len(A)
        lis = [1] * length

        for i in range(1, length):
            lis[i] = lis[i-1] * A[i-1]

        temp = 1
        for i in range(length-2, -1, -1):
            temp = temp * A[i+1]
            lis[i] *= temp

        return lis




