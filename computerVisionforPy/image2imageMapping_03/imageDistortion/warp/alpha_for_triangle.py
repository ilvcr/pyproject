#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 22 Apr 2018 03:21:46 PM CST
# File Name: alpha_for_triangle.py
# Description:  对于带有由 points 定义角点的三角形，创建大小为 (m, n)的alpha图（在归一化的齐次坐标意义下）
"""

def alpha_for_triangle(point, m, n):
    '''
    对于带有由 points 定义角点的三角形，创建大小为 (m, n)的alpha图
    （在归一化的齐次坐标意义下）
    '''

    alpha = zeros((m, n))

    for i in range(min(points[0]), max(point[0])):
        for j in range(min(point[1]), max(point[1])):
            x = linalg.solve(point, [i, j, 1])
            if min(x) > 0:  #所有系数都大于0
                alpha[i, j] = 1

    return alpha
