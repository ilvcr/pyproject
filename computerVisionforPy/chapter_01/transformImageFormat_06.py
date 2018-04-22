#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 11:46:21 PM CST
# File Name: transformImageFormat_06.py
# Description:  图像平均
                代码功能：
                        该函数包括一些基本的异常处理技巧，可以自动跳过不能打开的图像。还可以使用 mean() 函数计算平均图像。 
                        mean() 函数需要将所有的图像堆积到一个数组中；也就是说，如果有很多图像，该处理方式需要占用很多内存。
"""

def compute_average(imlist):
    '''计算图像列表的平均图像'''

    '''打开第一幅图象, 将其存储在浮点型数组中'''
    averageim = array(Image.open(imlist[0]),'f')  #imlist为文件中的图像列表

    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print(imname + '...skipped')
    averageim /= len(imlist)

    #返回unit8类型的平均图像
    return array(averageim, 'unit8')


'''
图像平均操作是减少图像噪声的一种简单方式，通常用于艺术特效。
可以简单地从图像列表中计算出一幅平均图像。
假设所有的图像具有相同的大小，我们可以将这些图像简单地相加，
然后除以图像的数目，来计算平均图像。
'''
