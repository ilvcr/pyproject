#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: find_nums_appear_once_in_array.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 18:27:44 2019
# Description: 数组中只出现一次的数字
#************************************************************************#

class Solution(object):

    def find_nums_appear_once_in_array(self, array):
        '''
            return [a, b]  其中ab是出现依次的两个数字
        '''
        hashmap = {}

        for i in array:
            if str(i) in hashmap:
                hashmap[str(i)] += 1
            else:
                hashmap[str(i)] = 1

        result = []
        for k in hashmap.keys():
            if hashmap[k] == 1:
                result.append(int(k))
        
        return result




