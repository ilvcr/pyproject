#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 11:33:25 PM CST
# File Name: transformImageFormat_04.py
# Description:  绘制图像的轮廓和直方图

"""

from PIL import Image
from pylab import *

#读取图像到数组中,filename为文件名
im = array(Image.open("filename").convert('L'))
'''绘制轮廓需要对每个坐标 [x, y] 的像素值施加同一个阈值，所以首先需要将图像灰度化'''

#新建一个图像
figure()

#不使用颜色信息
gray()

#在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis(''off)

'''
图像的直方图用来表征该图像像素值的分布情况。用一定数目的小区间（bin）来指定表征像素值的范围，
每个小区间会得到落入该小区间表示范围的像素数目。灰度图像的直方图可以使用 hist() 函数绘制

hist()函数的第二个参数指定小区间的数目。需要注意的是，因为 hist() 只接受一维数组作为输入，
所以我们在绘制图像直方图之前，必须先对图像进行压平处理。flatten()方法将任意数组按照行优先准则转换成一维数组。
'''
figure()
hist(im.flatten(), 128)
show()
