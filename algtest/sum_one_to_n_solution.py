#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: sum_one_to_n_solution.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 22:11:11 2019
# Description: 求1+2+3+4+..........+n
#************************************************************************#

class Solution(object):

    def sum_one_to_n_solution_01(self, n):
        return self.sumN(n)

    def sum0(self, n):
        return 0

    def sumN(self, n):
        fun = {False:self.sum0, True:self.sumN}
        return n+fun[not not n](n-1)

    def sum_one_to_n_solution_02(self, n):
        return n and self.sum_solution(n-1)+n



