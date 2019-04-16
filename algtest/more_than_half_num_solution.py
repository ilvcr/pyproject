#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: more_than_half_num_solution.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 17:05:40 2019
# Description: 数组中出现次数超过一半的数字
#************************************************************************#

class Solution(object):

    def more_than_half_num_solution(self, numbers):

        length = len(numbers)
        if not numbers:
            return 0
        result = numbers[0]
        times = 1

        for i in range(1, length):
            if times == 0:
                result = number[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1

        if not self.check_more_than_half(numbers, length, result):
            return 0

        return result

    def check_more_than_half(self, numbers, length, number):

        times = 0

        for i in range(length):
            if numbers[i] == number:
                times += 1

        if times*2 <= length:
            return False

        return True



