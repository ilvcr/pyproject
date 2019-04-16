#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: find_greatest_sum_of_sub_array.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 17:27:44 2019
# Description: 连续数组的最大和
#************************************************************************#

class Solution(object):

    def find_greatest_sum_of_sub_array(self, array):

        if not array:
            return 0

        cur_sum = 0
        max_sum = array[0]

        for i in range(len(array)):
            if cur_sum <= 0:
                cur_sum = array[i]
            else:
                cur_sum += array[i]

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum



