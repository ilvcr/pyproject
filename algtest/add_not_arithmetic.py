#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: add_not_arithmetic.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 22:15:31 2019
# Description: 不用加减乘除做加法 
#************************************************************************#

class Solution(object):

    def add_not_arithmetic(self, num1, num2):

        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp & 0xFFFFFFFF

        return num1 if num1 >> 31 == 0 else num1 - 4294967296



