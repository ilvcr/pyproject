#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 03:48:19 PM CST
# File Name: transformImageFormat_10.py
# Description:  使用scipy.ndimage.filters 模块的标准卷积操作来实现导数滤波
"""

from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('example.jpg').convert('L'))

#Sobel导数滤波器
'''
使用 Sobel 滤波器来计算 x 和 y 的方向导数，以及梯度大小。
sobel() 函数的第二个参数表示选择 x 或者 y 方向导数，第三个参数保存输出的变量。
'''
imx = zeros(im.shape)
filters.sobel(im, 1, imx)

imy = zeros(im.shape)
filters.sobel(im, 0, imy)

magnitude = sqrt(imx**2 + imy**2)
