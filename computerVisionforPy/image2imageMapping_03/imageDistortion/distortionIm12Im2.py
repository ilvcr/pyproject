#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 22 Apr 2018 05:15:21 PM CST
# File Name: distortionIm12Im2.py
# Description:  仿射扭曲 im1 到 im2 的例子
"""

import warp

#仿射扭曲 im1 到 im2 的例子

im1 = array(Image.open('beatles.jpg').convert('L'))
im2 = array(Image.open('billboard_for_rent.jpg').convert('L'))


# 选定一些目标点
tp = array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])


im3 = warp.image_in_image(im1, im2, tp)

figure()
gray()
imshow(im3)
axis('equal')
axis('off')
show()

