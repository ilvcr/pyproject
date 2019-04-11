#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: use_stack_relize_queue.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 12:50:43 2019
# Description: 使用两个栈实现队列
#************************************************************************#

class Solution(object):
    '''
        通过栈实现队列
    '''
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):

        self.stack1.append(node)
    
    def pop(self):

        if len(self.stack1) == 0 and len(self.stack2) == 0:
            
            return
        elif len(self.stack2) == 0:
            
            while len(self.stack1) > 0:
                
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


