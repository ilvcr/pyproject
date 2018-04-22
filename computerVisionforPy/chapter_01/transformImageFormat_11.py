#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 04:06:37 PM CST
# File Name: transformImageFormat_11.py
# Description:  对二值图像中的对象个数的计算
"""

from PIL import Image
from numpy import *
from scipy.ndimage import measurements, morphology

#载入图像, 然后使用阈值化操作, 以保证处理的图像为二值图像
im = array(Image.open('example.jpg').convert('L'))
im = 1 * (im < 128) #通过和 1相乘，脚本将布尔数组转换成二进制表示。

labels, nbr_objects = measurements.label(im)  #使用 label() 函数寻找单个的物体，
                                               #并且按其属于哪个对象将整数标签给像素赋值
print("Number of object:", nbr_objects)


#对象之间有一些小连接, 进行二进制开（binary open）操作, 可将其移除
im_open = morphology.binary_opening(im, ones((9, 5)), iterations=2)
'''
1-> binary_opening() 函数的第二个参数指定一个数组结构元素。
    该数组表示以一个像素为中心时，使用哪些相邻像素
2-> 参数iterations 决定执行该操作的次数
'''

labels_open, nbr_objects_open = measurements.label(im_open)
print("Number of objects:", nbr_objects_open)
