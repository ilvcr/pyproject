#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: number_of_1_between_and_N_solution.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 17:32:17 2019
# Description: 统计1出现的次数
#************************************************************************#

class Solution(object):

    def number_of_1_between_and_N_solution(self, n):

        count = 0
        for i in range(1, n+1):
            while i:
                if i%10 == 1:
                    count += 1
                i = i/10

        return count

    def number_of_1_between_and_N_solution_math(self, n):
        
        count, m = 0, 1
        while m <= n:
            count += (n//m + 8) // 10*m + (n // m%10 == 1) * (n%m + 1)
            m *= 10

        return count



