#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 22 Apr 2018 04:41:00 PM CST
# File Name: rigid_alignment.py
# Description:  严格对齐图像，并将其保存为新的图像
                    path 决定对齐后图像保存的位置
                        设置 plotflag=True， 以绘制图像
"""

from scipy import ndimage
from scipy.misc import imsave
import os


def rigid_alignment(faces, path, plotflag=False):
    '''
    严格对齐图像，并将其保存为新的图像
        path 决定对齐后图像保存的位置
            设置 plotflag=True， 以绘制图像
    '''

    #将第一幅图像中的点作为参考点
    refpoints = faces.values()[0]

    #使用仿射变换扭曲每幅图像
    for face in faces:
        points = faces[face]

    R, tx, ty = compute_rigid_transform(refpoints, points)

    T = array([[Rp[1][1], R[1][0]], [R[0][[1], R[0][0]]])

    im = array(Image.open(os.path.join(path, face)))
    im2 = zeros(im.shape, 'unit8')

    #对每个颜色通道进行扭曲
    for i in range(len(im.shape)):
        im2[:, :, i] = ndimage.affine_transform(im[:,:,i],linalg.inv(T),offset=[-ty,-tx])

    if plotflag:
        imshow(im2)
        show()

    #裁剪边界, 并保存对齐后的图像
    h, w = im2.shape[:2]
    border = (w+h) / 20

    #裁剪边界
    imsave(os.path.join(path, 'aligned/'+face),im2[border:h-border,border:w-border,:])
        #imsave() 函数来将对齐后的图像保存到 aligned 子文件夹中
