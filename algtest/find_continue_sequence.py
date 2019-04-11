#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: find_continue_sequence.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 18:31:11 2019
# Description: 和为s的连续整数序列
#************************************************************************#

class Solution(object):

    def find_continue_sequence(self, tsum):

        small, big, res = 1, 2, []

        csum = small + big

        while small < big:
            if csum > tsum:
                csum -= small
                small += 1
            else:
                if csum == tsum:
                    res.append([i for i in range(small, big+1)])
                big += 1
                csum += big

        return res



