#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: reverse_linklist.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 14:14:17 2019
# Description: 反转链表
#************************************************************************#

class Solution(object):
    '''
        反转链表
    '''
    def reverse_linklist(self, pHead):

        pReverseHead = None
        pNode = pHead
        pPrev = None

        while pNode != None:
            pNext = pNode.next
            if pNext == None:
                pReverseHead = pNode

            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext

        return pReverseHead


