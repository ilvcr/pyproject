#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: tree_mirror_root.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 14:37:09 2019
# Description: 二叉树的镜像
#************************************************************************#

class Solution(object):
    '''
        返回镜像树的根节点
    '''
    def tree_mirror_root(self, root):

        if root == None:
            return
        if root.left == None and root.right == None:
            return root

        ptemp = root.left
        root.left = root.right
        root.right = ptemp

        self.tree_mirror_root(root.left)
        self.tree_mirror_root(root.right)


