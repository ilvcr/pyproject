#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 19 Apr 2018 10:01:04 PM CST
# File Name: appendimages.py
# Description:  实现匹配点的可视化, 与harris一起使用
"""


from scipy.ndimage import filters
from pylab import *

def appendimages(im1, im2):
    '''返回将两幅图像并排拼接成的一幅新图像'''

    #选取具有最少行数的图像, 然后填充足够的空行
    rows1 = im1.shape[0]
    rows2 = im2.shape[0]

    if rows1 < row2:
        im1 = concatenate((im1,zeros((rows2-rows1,im1.shape[1]))),axis=0)

    elif rows1 > rows2:
        im2 = concatenate((im2,zeros((rows1-rows2,im2.shape[1]))),axis=0)
    #如果这些情况都没有，那么它们的行数相同，不需要进行填充

    return concatenate((im1, im2), axis=1)
