#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 22 Apr 2018 04:34:43 PM CST
# File Name: compute_rigid_transform.py
# Description: 计算用于将点对齐到参考点的旋转、尺度和平移量
"""

from scipy import linalg

def compute_rigid_transform(refpoints, points):
    '''计算用于将点对齐到参考点的旋转、尺度和平移量'''

    A = array([ [points[0], -points[1], 1, 0],
                [points[1], points[0], 0, 1],
                [points[2], -points[3], 1, 0],
                [points[3], points[2], 0, 1],
                [points[4], -points[5], 1, 0],
                [points[5], points[4], 0, 1]])

    y = array([ refpoints[0],
                refpoints[1],
                refpoints[2],
                refpoints[3],
                refpoints[4],
                refpoints[5]])


    # 计算最小化 ||Ax-y|| 的最小二乘解
    a, b, tx, ty = linalg.lstsq(A, y)[0]
    R = array([[a, -b], [b, a]])  #包括尺度的旋转矩阵


    return R, tx, ty


'''
函数compute_rigid_transform返回一个具有尺度的旋转矩阵，以及在 x 和 y 方向上的平移量。
为了扭曲图像，并保存对齐后的新图像，可以对每个颜色通道（这些图像都是彩色图像）应用 
ndimage.affine_transform() 函数操作。作为参考坐标系`:wq
可以使用任何三个点的坐标。
'''
