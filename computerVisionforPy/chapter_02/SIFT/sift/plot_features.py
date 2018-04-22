#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 01:20:41 PM CST
# File Name: plot_features.py
# Description:  显示带有特征的图像
                    输入： im（数组图像）， locs（每个特征的行、列、尺度和朝向）
"""
from scipy.ndimage import filters
from pylab import *
from numpy import *
from PIL import Image

def plot_features(im, locs, circle=False):
        '''
        显示带有特征的图像
        输入： im（数组图像）， locs（每个特征的行、列、尺度和朝向）
        '''

        def draw_circle(c, r):
            '''绘制出圆圈，圆圈的半径为特征的尺度'''
            t = arange(0, 1.01, .01) * 2 * pi
            x = r * cos(t) + c[0]
            y = r * sin(t) + c[1]
            plot(x, y, 'b', linewidth=2)

            imshow(im)

        if circle:
            for p in locs:
                draw_circle(p[:2], p[2])
        else:
            plot(locs[:,0], locs[:,1],'ob')

        axis('off')
