#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: serialize_tree.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 23:18:20 2019
# Description: 序列化二叉树
#************************************************************************#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.flag = -1

    def serialize_tree(self, root):

        if not root:
            return '#'
        return str(root.val)+','
               +self.serialize_tree(root.left)
               +self.serialize_tree(root.right)

    def deserialize(self, s):

        self.flag += 1
        l = s.splot(',')

        if self.flag >= len(s):
            return None
        root = None

        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.deserialize(s)
            root.right = self.deserialize(s)

        return root



