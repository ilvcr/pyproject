#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: first_not_repeating_char.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 17:51:01 2019
# Description: 第一个只出现一次的字符
#************************************************************************#

class Solution(object):

    def first_not_repeating_char(self, s):

        if not s:
            return -1

        store = {}
        lis = list(s)

        for i in lis:
            if i not in store.keys():
                store[i] = 0
            store[i] += 1

        for i in lis:
            if store[i] == 1:
                return s.index(i)

        return -1


