#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: get_ugly_number_solution.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 17:42:03 2019
# Description: 丑数
#************************************************************************#

class Solution(object):

    def get_ugly_number_solution(self, index):

        if not index:
            return 0

        ugly_number = [1]*index
        next_index = 1

        index2 = 0
        index3 = 0
        index5 = 0

        while next_index < index:
            minValue = min(ugly_number[index2]*2, ugly_number[index3]*3, 
                           ugly_number[index5]*5)

            while ugly_number[index2]*2 <= ugly_number[next_index]:
                index2 += 1

            while ugly_number[index3]*3 <= ugly_number[next_index]:
                index3 += 1

            while ugly_number[index5]*5 <= ugly_number[next_index]:
                index5 += 1

            next_index += 1

        return ugly_number[-1]


