#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 11:24:28 PM CST
# File Name: transformImageFormat_03.py
# Description:  Matplotlib应用到计算机视觉中
                代码功能: 用几个点和一条线绘制图像
                          代码首先绘制出原始图像，然后在 x 和 y 列表中给定点的 x 坐标和 y 坐标上
                          绘制出红色星状标记点，最后在两个列表表示的前两个点之间绘制一条线段（默
                          认为蓝色）。
"""

from PIL import Image
from pylab import *  #在 PyLab 库中，我们约定图像的左上角为坐标原点。

#读取图像到数组中,filename为文件名
im = array(Image.open('filename'))

#绘制图像
imshow(im)

#一些点
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

#使用红色形状标记绘制点
plot(x, y, 'r*')

#绘制连接前两个点的线
plot(x[:2], y[:2])

#坐标轴不显示
#axis('off')

#添加标题, 显示绘制的图像
title('Plotting: "filename"')
show()
