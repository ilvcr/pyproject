#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 11:40:33 PM CST
# File Name: transformImageFormat_05.py
# Description:  交互式标注
                代码功能：
                        首先绘制一幅图像，然后等待用户在绘图窗口的图像区域点击三次。
                        程序将这些点击的坐标 [x, y] 自动保存在 x 列表里。
"""

from PIL import Image
from pylab import *

im = array(Image.open('filename'))
imshow(im)

print("Please click 3 point")

x = ginput(3)  #pylab库中的ginput函数可以实现交互式标注
print('you clicked:', x)
show()
