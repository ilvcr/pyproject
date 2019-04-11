#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: get_least_number_solution.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 17:16:23 2019
# Description: 最小的k个数
#************************************************************************#

class Solution(object):

    def get_least_number_solution(self, tinput, k):

        if not tinput or k > len(tinput):
            return []

        tinput = self.quick_sort(tinput)
        return tinput[:k]

    def quick_sort(self, lst):
        
        if not lst:
            return []
        pivot = lst[0]
        left = self.quick_sort([x for x in lst[1:] if x < pivot])
        right = self.quick_sort([x for x in lst[1:] if x >= pivot])

        return left + [pivot] + right



