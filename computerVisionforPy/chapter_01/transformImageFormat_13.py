#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 04:47:12 PM CST
# File Name: transformImageFormat_13.py
# Description:  使用transformImageFormat_12.py里面的denoise()函数
"""

from numpy import *
from numpy import random
from scipy.ndimage import filters
import transformImageFormat_12

#使用噪声创建合成图像
im = zeros((500, 500))
im[100:400, 100:400] = 128
im[200:300, 200:300] = 255
im = im + 30 * random.standard_normal((500, 500))

U, T = transformImageFormat_12.denoise(im, im)
G = filters.gaussian_filter(im, 10)

#保存生成结果
from scipy.misc import imsave
imsave('example_rof.pdf', U)
imsave('example_gaussian.pdf', G)
