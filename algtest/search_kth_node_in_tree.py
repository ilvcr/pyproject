#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: search_kth_node_in_tree.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 23:13:43 2019
# Description: 搜索二叉树的第k个节点
#************************************************************************#

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def search_kth_node_in_tree(self, pRoot, k):
        '''
            return  y对应节点的TreeNode
        '''
        if not pRoot or not k:
            return

        res = []

        def traverse(node):
            if len(res) >= k or not node:
                return
            traverse(node.left)
            res.append(node)
            traverse(node.right)

        traverse(pRoot)

        if len(res) < k:
            return

        return res[k-1]




