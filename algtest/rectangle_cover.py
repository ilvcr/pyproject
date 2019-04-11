#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: rectangle_cover.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 13:32:41 2019
# Description: 矩形覆盖问题
#************************************************************************#


class Solution(object):
    '''
        矩形覆盖问题
        使用2 1的小矩形横或者竖着去覆盖更大的矩形、
        用nd个2 1的小矩形五重叠覆盖一个2*n的大矩形，总共有多少种方法
    '''
    def rectangle_cover(self, number):

        if number == 0:
            return 0
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number+1):
                tempArray[(i+1)%2] = tempArray[0] + tempArray[1]

        return tempArray[(number+1)%2]



