#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 03:38:10 PM CST
# File Name: transformImageFormat_09.py
# Description:  用scipy.ndimage.filters模块来做滤波操作, 该模块使用
                    一维分离的方式来计算卷积
                    代码功能：
                                实现滤波操作
"""

from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('example.jpg'.convert('L')))
im2 = filters.gaussian_filter(im, 5)  #guassian_filter() 函数的最后一个参数表示标准差


'''
#随着 σ(标准差)的增加, 一幅图像被模糊的程度。 σ 越大，处理后的图像细节丢失越多,
#如果打算模糊一幅彩色图像，只需简单地对每一个颜色通道进行高斯模糊

im = array(Image.open('example.jpg'))
im2 = zeros(im.shape)
for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i], 5)
im2 = uint8(im2)  #并不总是需要将图像转换成 uint8 格式，只将像素值用八位来表示
#im2 = array(im2, 'uint8')

'''
