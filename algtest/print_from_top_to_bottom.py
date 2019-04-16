#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: print_from_top_to_bottom.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 15:03:31 2019
# Description: 从上往下打印二叉树
#************************************************************************#


class Solution(object):
    '''
        从上往下打印二叉树
    '''
    def print_from_top_to_bottom(self, root):
        '''
            return 从上到下每个节点值列表, 例: [1, 2, 3]
        '''
        if root is None:
            return []

        queue = []
        result = []

        queue.append(root)

        while len(queue) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)

            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)

        return result



