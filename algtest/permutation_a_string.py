#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: permutation_a_string.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 16:56:23 2019
# Description: 字符串的排列
#************************************************************************#

class Solution(object):

    def permutation_a_string(self, ss):

        if not ss:
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(0, len(charList)):
            if i > 0 and charList[i] == charList[i-1]:
                continue

            temp = self.permutation_a_string(''.join(charList[:i])+''.join(charList[i+1:]))
            
            for j in temp:
                pStr.append(charList[i] + j)

        return pStr


a = Solution()
ss = "fahfdadkgaukhfaodfhajdfkalhafjnlf"
print a.permutation_a_string(ss)


