#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 11:02:00 PM CST
# File Name: transformImageFormat_01.py
# Description:
                从文件名列表(filelist)中读取所有的图像文件, 并转换成JPEG格式
"""

from PIL import Image
import os

for infile in filelist:
    outfile = os.path.splitext(infile)[0] + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)#PIL的open()函数用于创建PIL图像对象,save()方法用于保存图像到具有指定文件名的文件。
        except IOError:
            print("cannot convert", infile)


'''
#1->
from PIL import Image
pil_im = Image.open("filename")
#上述代码的返回值 pil_im 是一个 PIL 图像对象

#2->
pil_im_convert = Image.open("filename").convert('L')
#图像的颜色转换可以使用 convert() 方法来实现

#3->
pil_im_thumbnail.thumbnail((128, 128))#创建最长边为 128 像素的缩略图
#thumbnail() 方法接受一个元组参数（该参数指定生成缩略图的大小）,然后将图像转换成符合元组参数指定大小的缩略图。

#4->
box = (100, 100, 400, 400)
region = pil_im.crop(box)#使用 crop() 方法可以从一幅图像中裁剪指定区域
#该区域使用四元组来指定。四元组的坐标依次是（左，上，右，下）。 

#5->
region = region.transpose(Image.ROTAT_180)
pil_im.paste(region, box)#旋转region区域，然后使用paste() 方法将该区域放回去.

#6->
out = pil_im.resize(128, 128)#resize() 方法用来调整图像的尺寸
out = pil_im.rotate(45)#rotate()方法用来使用逆时针方式表示旋转角度(45°)
'''
