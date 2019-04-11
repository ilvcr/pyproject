#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: frog_jump_floor.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 13:27:02 2019
# Description: 青蛙跳台阶
#************************************************************************#

class Solution(object):
    '''
        青蛙跳台阶
    '''
    def frog_jump_floor(self, number):

        tempArray = [1, 2]

        if number >= 3:
            for i in range(3, number+1):
                tempArray[(i+1)%2] = tempArray[0] + tempArray[1]

        return tempArray[(number+1)%2]

    def frog_jump_floor_plus(self, number):
        '''
            青蛙可以跳1级、2级台阶、n级台阶
        '''

        ans = 1
        if number >= 2:
            for i in range(number-1):
                ans = ans * 2

        return ans


