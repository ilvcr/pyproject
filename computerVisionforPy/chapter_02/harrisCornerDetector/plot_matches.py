#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 19 Apr 2018 10:06:49 PM CST
# File Name: plot_matches.py
# Description:  与harris.py一起使用
"""

from scipy.ndimage import filters
from pylab import *

def plot_matches(im1, im2, locs1, locs2, matchscores, show_below=True):
    '''显示一幅带有连接匹配之间连线的图片
       输入： im1， im2（数组图像）， locs1， locs2（特征位置）， matchscores（match() 的输出），
       show_below（如果图像应该显示在匹配的下方）
    '''

    im3 = appendimages(im1, im2)

    if show_below:
        im3 = vstack((im3, im3))

    imshow(im3)

    cols1 = im1.shape[1]
    for i, m in enumerate(matchscores):
        if m > 0:
            plot([locs1[i][1],locs2[m][1]+cols1],[locs1[i][0],locs2[m][0]],'c')
    axis('off')
