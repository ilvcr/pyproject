#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: duplicate_in_array.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 22:24:38 2019
# Description: 数组中重复的数字
#************************************************************************#

class Solution(object):

    def duplicate_in_array(self, numbers, duplicate):
        '''
            找到任意重复的一个值并赋值到duplicate[0]
            return  True/False
        '''

        if not numbers or len(numbers) < 0:
            return False

        for i in numbers:
            if i < 0 or i > len(numbers) - 1:
                return False

        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplicate[0] = numbers[i]
                    return True
                else:
                    idx = numbers[i]
                    numbers[i], numbers[idx] = numbers[idx], numbers[i]

        return False




