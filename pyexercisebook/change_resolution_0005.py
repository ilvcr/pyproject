#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: change_resolution_0005.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月22日 星期五 16时48分48秒
#Description:   有一个目录装了很多照片，把其的尺寸变成都不大于 iPhone5
                    分辨率的大小。
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

from PIL import Image
import os

path = 'source/picture05/pics'
resultPath = 'source/picture05/result'

if not os.path.isdir(resultPath):
    os.mkdir(resultPath)

for picName in os.listdir(path):
    picPath = os.path.join(path, picName)
    print picPath
    with Image.open(picPath) as im:
        w, h = imsize
        n = w / 1366 if (w / 1366) >= (h / 640) else h / 640
        im.thumbnail(w / n, h / n)
        im.save(resultPath+'/finish_'+picName.split('.')[0]+'.jpg', 'jpeg')


