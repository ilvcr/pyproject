#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: stack_include_min.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 14:52:35 2019
# Description: 包含min函数的栈
#************************************************************************#

class Solution(object):
    '''
        包含min函数的栈
    '''
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):

        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            temp = self.min()
            self.minStack.append(temp)

    def pop(self):

        if self.stack == None or self.minStack == None:
            return None

        self.minStack.pop()
        self.stack.pop()

    def top(self):

        return self.stack[-1]
    
    def min(self):

        return self.minStack[-1]



