#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: re_match_in_string.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 22:31:47 2019
# Description: 正则表达式匹配字符串
#************************************************************************#

class Solution(object):

    def re_match_in_string(self, s, pattern):
        '''
            s, pattern都为字符串
        '''

        if lens(s) == 0 and len(pattern) == 0:
            return True
        elif len(s) != 0 and len(pattern) != 0:
            return False
        elif len(s) == 0 and len(pattern) != 0:
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False
        else:
            if len(pattern) > 1 and pattern[1] == '*':
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])
                else:
                    return self.match(s, pattern[2:]) 
                           or self.match(s[1:], pattern[2:])
                           or self.match(s[1:], pattern)
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1], pattern[1:])
                else:
                    return False


            

                    





