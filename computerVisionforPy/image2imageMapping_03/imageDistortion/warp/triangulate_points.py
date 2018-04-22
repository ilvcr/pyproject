#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 22 Apr 2018 03:26:33 PM CST
# File Name: triangulate_points.py
# Description:  二维点的 Delaunay 三角剖分
"""

import matplotlib.delaunay as md

def triangulate_points(x, y):
    '''二维点的 Delaunay 三角剖分'''

    centers, edges, tri, neighbors = md.delaunay(x, y)

    return tri


'''
狄洛克三角剖分选择一些三角形，使三角剖分中所有三角形的最小角度最大 。
函数 delaunay() 有 4 个输出，其中我们仅需要三角形列表信息（第三个输出）

函数输出的是一个数组，该数组的每一行包含对应数组 x 和 y 中每个三角形三个点的切片。
'''
