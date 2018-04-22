#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 22 Apr 2018 03:10:57 PM CST
# File Name: image_in_image.py
# Description:  函数的输入参数为两幅图像和一个坐标。
                    该坐标为将第一幅图像放置到第二幅图像中的角点坐标
"""


def image_in_image(im1, im2, tp):
    '''
    使用仿射变换将 im1 放置在 im2 上，使 im1 图像的角和 tp 尽可能的靠近
    tp 是齐次表示的，并且是按照从左上角逆时针计算的
    '''

    #扭曲的点
    m, n = im1.shape[:2]
    fp = array([[0, m, m, 0], [0, 0, n , n], [1, 1, 1, 1]])

    #计算仿射变化, 并且将其应用于图像im1
    H = homography.Haffine_from_points(tp, fp)
    im1_t = ndimage.affine_transform(im1, H[:2, :2], (H[0, 2], H[1, 2]), im2.shape[:2])

    alpha = (im1_t > 0)

    return (1 - alpha) * im2 + alpha * im1_t



'''
函数 Haffine_from_points() 会返回给定对应点对的最优仿射变换。
'''
