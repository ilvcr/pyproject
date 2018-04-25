#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 25 Apr 2018 07:17:03 PM CST
# File Name: panorama.py
# Description:  使用单应性矩阵 H（使用 RANSAC 健壮性估计得出），协调两幅图像，
                    创建水平全景图像。结果为一幅和 toim 具有相同高度的图像。 
                        padding 指定填充像素的数目， delta 指定额外的平移量
"""

def panorama(H, fromim, toim, padding=2400,delta=2400):
    '''
    使用单应性矩阵 H（使用 RANSAC 健壮性估计得出），协调两幅图像，创建水平全景图像。结果
    为一幅和 toim 具有相同高度的图像。 padding 指定填充像素的数目， delta 指定额外的平移量
    '''

    #检查图像是灰度图像，还是彩色图像
    is_color = len(fromim.shape) == 3

    #用于 geometric_transform() 的单应性变换
    def transf(p):
        p2 = dot(H, [p[0], p[1], 1])
        return (p2[0]/p2[2], p2[1]/p2[2])

    if H[1, 2] < 0:  #fromim 在右边
        print('warp - right')
        #变换fromim
        if is_color:
            #在目标图像的右边填充 0
            toim_t = hstack((toim, zeros((toim.shape[0], padding, 3))))
            fromim_t = zeros((toim.shape[0],toim.shape[1]+padding,toim.shape[2]))
            for col in range(3):
                fromim_t[:,:,col] = ndimage.geometric_transform(fromim[:,:,col], transf,(toim.shape[0],toim.shape[1]+padding))

        else:
            # 在目标图像的右边填充 0
            toim_t = hstack((toim,zeros((toim.shape[0],padding))))
            fromim_t = ndimage.geometric_transform(fromim,transf, (toim.shape[0],toim.shape[1]+padding))

    else:
        print('warp - left')
        # 为了补偿填充效果，在左边加入平移量
        H_delta = array([[1,0,0],[0,1,-delta],[0,0,1]])
        H = dot(H,H_delta)

        # fromim 变换
        if is_color:
            # 在目标图像的左边填充 0
            toim_t = hstack((zeros((toim.shape[0],padding,3)),toim))
            fromim_t = zeros((toim.shape[0],toim.shape[1]+padding,toim.shape[2]))
            for col in range(3):
                fromim_t[:,:,col] = ndimage.geometric_transform(fromim[:,:,col], transf,(toim.shape[0],toim.shape[1]+padding))
        else:
            # 在目标图像的左边填充 0
            toim_t = hstack((zeros((toim.shape[0],padding)),toim))
            fromim_t = ndimage.geometric_transform(fromim, transf,(toim.shape[0],toim.shape[1]+padding))


        # 协调后返回（将 fromim 放置在 toim 上）
        if is_color:
            # 所有非黑色像素
            alpha = ((fromim_t[:,:,0] * fromim_t[:,:,1] * fromim_t[:,:,2] ) > 0)
            for col in range(3):
                toim_t[:,:,col] = fromim_t[:,:,col]*alpha + toim_t[:,:,col]*(1-alpha)
        else:
            alpha = (fromim_t > 0)
            toim_t = fromim_t*alpha + toim_t*(1-alpha)


    return toim_t
