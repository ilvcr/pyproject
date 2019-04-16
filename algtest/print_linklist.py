#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: print_linklist.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 12:17:38 2019
# Description: 从尾到头打印链表
#************************************************************************#

class ListNode(object):
    '''
        定义链表
    '''
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
        return 从尾部z到头部的列表值序列
    '''
    def print_list_from_tail_to_head(self, listNode):

        if not listNode:
            return []

        result = []

        while listNode:
            result.insert(0, listNode.val)
            listNode = listNode,next
        return result


'''
if __name__ == '__main__':

    #data = [1, 2, 3 ,4, 5]
    #ll = ListNode(data)


    result = Solution([1, 2, 3 ,4, 5])
    print result.print_list_from_tail_to_head(ll)
'''

