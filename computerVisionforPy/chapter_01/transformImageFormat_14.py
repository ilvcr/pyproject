#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 04:53:33 PM CST
# File Name: transformImageFormat_14.py
# Description: 得到实际图像中使用ROF模型去噪的效果,
                运用transformImageFormat_12里的denoise()函数

                ROF 去噪后的图像保留了边缘和图像的结构信息，同时模糊了“噪声”
"""

from PIL import Image
from pylab import *
import transformImageFormat_12

im = array(Image.open('example.jpg').convert('L'))
U, T = transformImageFormat_12.denoise(im, im)

figure()
gray()
imshow()
axis('equal')
axis('off')
show()
