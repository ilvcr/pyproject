#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 22 Apr 2018 03:29:47 PM CST
# File Name: pw_affine.py
# Description:  从一幅图像中扭曲矩形图像块
                        fromim= 将要扭曲的图像
                        toim= 目标图像
                        fp= 齐次坐标表示下，扭曲前的点
                        tp= 齐次坐标表示下，扭曲后的点
                        tri= 三角剖分
"""


def pw_affine(fromim, toim, fp, tp, tri):
    '''从一幅图像中扭曲矩形图像块
                fromim= 将要扭曲的图像
                toim= 目标图像
                fp= 齐次坐标表示下，扭曲前的点
                tp= 齐次坐标表示下，扭曲后的点
                tri= 三角剖分
    '''

    im = toim.copy()

    #检查图像是灰度图像还是彩色图像
    is_color = len(fromim.shape) == 3

    #创建扭曲后的图像（如果需要对彩色图像的每个颜色通道进行迭代操作，那么有必要这样做）
    im_t = zeros(im.shape, 'uint8')

    for i in tri:
        #计算仿射变换
        H = homography.Haffine_from_point(tp[:, t], fp[:, t])

        if is_color:
            for col  in range(fromim.shape[2]):
                im_t[:, :, col] = ndimage.affine_transform(fromim[:, :, col], H[:2, :2], (H[1, 2]), im.shape[:2])
        else:
            im_t = ndimage.affine_transform(fromim, H[:2, :2], (H[0, 2],H[1, 2]), im.shape[:2])


        #三角形的alpha
        alpha = alpha_for_triangle(tp[:, t], im.shape[0], im.shape[1])


        #将三角形加入到图像中
        im[alpha>0] = im_t[alpha>0]

    return im


'''
首先检查该图像是灰度图像还是彩色图像。如果图像为彩色图像，则对每个颜色通道进行扭曲处理。
因为对于每个三角形来说，仿射变换是唯一确定的，所以这里使用 Haffine_from_points() 函数来处理。
'''
