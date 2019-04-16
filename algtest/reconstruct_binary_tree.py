#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: reconstruct_binary_tree.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 12:35:17 2019
# Description:  重建二叉树
#************************************************************************#

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
        return 构造的TreeNode根节点
    '''
    def reconstruct_binary_tree(self, pre, tin):

        if not pre and not tin:
            return None

        root = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None

        i = tin.index(pre[0])

        root.left = self.reconstruct_binary_tree(pre[1: i+1], tin[:i])
        root.right = self.reconstruct_binary_tree(pre[i+1: ], tin[i+1:])

        return root



