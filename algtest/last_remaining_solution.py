#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: last_remaining_solution.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 22:08:36 2019
# Description: 孩子门的游戏圆圈中最后剩下的数
#************************************************************************#


class Solution(object):
    
    def last_remaining_solution(self, n, m):

        if n < 1 or m < 1:
            return -1

        con = range(n)
        start = 0
        end = -1
        while con:
            k = (start + m - 1) % n
            end = con.pop(k)
            n -= 1
            start = k

        return end



