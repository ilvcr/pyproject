#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: find_numbers_with_sum.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 21:41:18 2019
# Description: 和为s的两个数字
#************************************************************************#

class Solution(object):

    def find_numbers_with_sum(self, array, tsum):

        if not array or not tsum:
            return []

        start = 0
        end = len(array) - 1
        while start < end:
            csum = array[start] + array[end]

            if csum < tsum:
                start += 1
            elif csum > tsum:
                end -= 1
            else:
                return [array[start], array[end]]

        return []




