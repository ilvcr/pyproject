#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 22 Apr 2018 05:35:52 PM CST
# File Name: warpOperation.py
# Description:  操作warp, 统一操作
"""

import homography
import warp


#打开图像, 并将其扭曲
fromim = array(Image.open('sunset_tree.jpg'))
x, y = meshgrid(range(5),range(6))
x = (fromim.shape[1]/4) * x.flatten()
y = (fromim.shape[0]/5) * y.flatten()


#三角剖分
tri = warp.triangulate_points(x, y)


#打开图像和目标点
im = array(Image.open('turningtorso1.jpg'))
tp = loadtxt('turningtorso1_points.txt') # destination points


# 将点转换成齐次坐标
fp = vstack((y,x,ones((1,len(x)))))
tp = vstack((tp[:,1],tp[:,0],ones((1,len(tp)))))


# 扭曲三角形
im = warp.pw_affine(fromim,im,fp,tp,tri)


# 绘制图像
figure()
imshow(im)
warp.plot_mesh(tp[1],tp[0],tri)
axis('off')
show()
