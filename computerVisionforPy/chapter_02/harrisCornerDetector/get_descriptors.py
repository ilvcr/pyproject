#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 19 Apr 2018 09:39:48 PM CST
# File Name: get_descriptors.py
# Description:  将本函数与harris.py一起使用
"""

from scipy.ndimage import filters
from pylab import *

def get_descriptors(image, filtered_coords, wid=5):
    '''对于每个返回的点，返回点周围 2*wid+1 个像素的值（假设选取点的 min_distance > wid） '''

    desc = []
    for coords in filtered_coords:
        patch = image[coords[0]-wid:coords[0]+wid+1, coords[1]-wid:coords[1]+wid+1].flatten()
    desc.append(patch)

    return desc

