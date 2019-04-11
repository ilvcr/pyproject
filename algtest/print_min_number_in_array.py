#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: print_min_number_in_array.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 17:37:46 2019
# Description: 把数组排成最小的数
#************************************************************************#

class Solution(object):

    def print_min_number_in_array(self, number):

        if not number:
            return ''

        str_num = [str(m) for m in number]

        for i in range(len(number)-1):
            for j in range(i+1, len(number)):
                if str_num[i] + str_num[j] > str_num[j] + str_num[i]:
                    str_num[i], str_num[j] = str_num[j], str_num[i]

        return ''.jion(str_num)




