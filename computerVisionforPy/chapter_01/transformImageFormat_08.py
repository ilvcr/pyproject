#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 03:12:38 PM CST
# File Name: transformImageFormat_08.py
# Description:  假定这些图像的名称保存在列表 imlist 中，
                跟之前的代码一起保存传在 pca.py 文件中，
                可以使用如下的脚本计算图像的主成分
"""

from PIL import Image
from numpy import *
from pylab import *
import pca

im = arrary(Image.open(imlist[0]))  #打开一幅图像, 获取其大小
m, n = im.shape[0:2]  #获取图像大小
imnbr = len(imlist)  #获取图像的数目

#创建矩阵, 保存所有压平后的图像数据
immatrix = array([array(Image.open(im)).flatten() for im in imlist], 'f')

#执行PCA操作
V, S, immean = pca.pca(immatrix)

#显式一些图像(均值图像和前7个模式)
figure()
gray()
subplot(2, 4, 1)
imshow(imean.reshape(m, n))
for i in range(7):
    subplot(2, 4, i+2)
    imshow(V[i].reshape(m, n))  #可以使用 reshape() 函数将图像需要从一维表示重新转换成二维图像

show()

