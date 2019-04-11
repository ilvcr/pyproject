#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: fibonacci_series.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 13:17:48 2019
# Description:  斐波纳契数列
#************************************************************************#

class Solution(object):
    '''
        斐波那契数列
    '''
    def fibonacci_series(self, n):

        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]

result = Solution()
print result.fibonacci_series(20)


