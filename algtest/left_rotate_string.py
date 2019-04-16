#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: left_rotate_string.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 21:44:54 2019
# Description: 左旋字符串
#************************************************************************#

class Solution(object):

    def left_rotate_string(self, s, n):

        if len(s) <= 0 or n < 0 or len(s) < n:
            return ''

        lis = list(s)

        self.reverse(lis)
        length = len(s)
        pivot = length - n
        frontlist = self.reverse(lis[:pivot])
        behindlist = self.reverse(lis[pivot:])

        res = ''.join(frontlist) + ''.join(behindlist)

        return res

    def reverse(self, lis):

        if not lis or len(lis) <= 0:
            return ''

        start = 0
        end = len(lis) - 1
        while start < end:
            lis[start], lis[end] = lis[end], lis[start]
            start += 1
            end -= 1

        return lis



