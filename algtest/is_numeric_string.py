#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: is_numeric_string.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 22:41:04 2019
# Description: 表示数值的字符串
#************************************************************************#

class Solution(object):

    def is_numeric_string(slef, s):
        '''
            s为字符串
        '''
        if len(s) <= 0:
            return False
        
        #分别标记出是否出现过特殊的正负号、小数点、e，
        has_sign = False
        has_point = False
        has_e = False

        for i in range(len(s)):
            #e
            if s[i] == 'E' or s[i] == 'e':
                if has_e:
                    return False
                else:
                    has_e = True
                    if i == len(s) - 1:
                        return False
            #正负号
            elif s[i] == '+' or s[i] == '-':
                if has_sign:
                    if s[i-1] != 'e' and s[i-1] != 'E':
                        return False
                else:
                    has_sign = True
                    if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                        return False
            #小数点
            elif s[i] == '.':
                if has_point or has_e:
                    return False
                else:
                    has_point = True
                    if i > 0 and (s[i-1] == 'e' or s[i-1] == 'E'):
                        return False
            else:
                if s[i] < '0' or s[i] > '9':
                    return False

        return True

                




