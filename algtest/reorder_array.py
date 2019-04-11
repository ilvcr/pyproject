#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: reorder_array.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 14:01:02 2019
# Description: 调整数组顺序是奇数位于偶数前面
#************************************************************************#

class Solution(object):
    '''
        调整数组顺序是奇数位于偶数前面
    '''
    def reorder_array(self, array):

        return sorted(array, key=lambda c:c%2, reverse=True)

arr = [1, 3, 4, 2, 4 , 5, 6 ,78 ,345, 243]
a = Solution()
print a.reorder_array(arr)



