#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: stack_is_pop_order.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 14:58:23 2019
# Description: 栈的压入、弹出序列
#************************************************************************#

class Solution(object):
    '''
        栈的压入、弹出序列
    '''
    def stack_is_pop_order(self, pushV, popV):

        if pushV == [] or popV == []:
            return False

        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)

        if len(stack):
            return False
        else:
            return True



