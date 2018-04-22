#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 19 Apr 2018 09:11:09 PM CST
# File Name: harris.py
# Description:  Harris 角点检测程序
"""

from scipy.ndimage import filters
from pylab import *


def computer_harris_response(im, sigma=3):
    '''在一幅灰度图像中, 对每个像素计算Harris角点检测器响应函数'''

    #计算导数
    imx = zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (0, 1), imx)
    imy = zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (1, 0), imy)

    #计算Harris矩阵的分量
    Wxx = filters.gaussian_filter(imx * imx, sigma)
    Wxy = filters.gaussian_filter(imx * imy, sigma)
    Wyy = filters.gaussian_filter(imy * imy, sigma)

    #计算特征值和迹
    Wdet = Wxx * Wyy - Wxy ** 2
    Wtr = Wxx + Wyy

    return Wdet / Wtr


def get_harris_points(harrisim, min_dist=10, threshold=0.1):
    '''从一幅Harris响应图像中返回角点. min_dist为分割角点和图像边界最少像素数目'''

    #寻找高于阈值的候选角点
    corner_threshold = harrisim.max() * threshold
    harrisim_t = (harrisim > corner_threshold) * 1

    #得到候选点的坐标
    coords = array(harrisim_t.nonzero()).T

    #以及他们的harris响应值
    candidate_values = [harrisim[c[0], c[1]] for c in coords]

    #对候选点按照Harris响应值进行排序
    index = argsort(candidate_values)

    #将可行点的位置保存到数组中
    allowed_locations = zeros(harrisim.shape)
    allowed_locations[min_dist:-min_dist, min_dist:-min_dist] = 1

    #按照min_dist原则,选择最佳Harris点
    filtered_coords = []
    for i in index:
        if allowed_locations[coords[i, 0], coords[i, 1]] == 1:
            filtered_coords.append(coords[i])
            allowed_locations[(coords[i, 0]-min_dist):(coords[i,0]+min_dist),
                            (coords[i,1]-min_dist):(coords[i,1]+min_dist)] = 0

    return filtered_coords


def plot_harris_points(image, filtered_coords):
    '''绘制图像中检测到的角点'''

    figure()
    gray()
    imshow(image)
    plot([p[1] for p in filtered_coords], [p[0] for p in filtered_coords], '*')
    axis('off')
    show()

'''
首先，打开该图像，转换成灰度图像。
然后，计算响应函数，基于响应值选择角点。
最后，在原始图像中覆盖绘制检测出的角点， 绘制出结果图像
'''

im = array(Image.open('example.jpg').convert('L'))
harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim,6)
harris.plot_harris_points(im, filtered_coords)
