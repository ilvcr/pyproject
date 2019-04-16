#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: first_appearing_onece_in_string.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 22:49:25 2019
# Description: 
#************************************************************************#

class Solution(object):

    def __init__(self):
        self.dict = {}
        self.lis = []

    def first_appearing_onece_in_string(self):
        '''
            return 对应的char
        '''
        while len(self.lis) > 0 and self.dict[self.lis[0]] == 2:
            self.lis.pop(0)
        if len(slef.lis) == 0:
            return '#'
        else:
            return self.lis[0]

    def insert(self, char):

        if char not in self.dic.keys():
            self.dic[char] = 1
            self.lis.append(char)
        elif self.dic[char]:
            self.dic[chae] = 2


