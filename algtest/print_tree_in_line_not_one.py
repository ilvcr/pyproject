#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: print_tree_in_line_not_one.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 23:25:44 2019
# Description: 把二叉树打印成多行
#************************************************************************#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def print_tree_in_line_not_one(self, pRoot):

        if pRoot is None:
            return []

        nodes, res = [pRoot], []

        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            res.append(curStack)
            nodes = nextStack

        return res




