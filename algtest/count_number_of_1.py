#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: count_number_of_1.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 13:37:05 2019
# Description: 统计二进制中1的个数
#************************************************************************#

class Solution(object):
    
    def count_number_of_1(self, n):

        count = 0

        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            count += 1
            n = (n-1) & n

        return count



