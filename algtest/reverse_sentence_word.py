#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: reverse_sentence_word.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 21:51:36 2019
# Description: 翻转单词顺序列
#************************************************************************#


class Solution(object):
    def reverse_sentence_word(self, s):

        if not s or len(s) <= 0:
            return ''

        lis = list(s)
        lis = self.reverse(lis)
        start = 0
        end = 0
        res = ''
        lisTmp = []

        while end < len(s):
            if end == len(s) - 1:
                lisTmp.append(self.reverse(lis[start:]))
                break
            if lis[start] == '':
                start += 1
                end += 1
                lisTmp.append(' ')
            elif lis[end] == ' ':
                lisTmp.append(self.reverse(lis[start:end]))
                start = end
            else:
                end += 1

        for i in lisTmp:
            res += ''.join(i)

        return res

    def reverse(self, lis):
        if not lis or len(lis) <= 0:
            return ''
        start = 0
        end = len(lis) - 1
        while start < end:
            lis[start], lis[end] = lis[end], lis[start]
            start += 1
            end -= 1

        return lis

