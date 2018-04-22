#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 02:37:26 PM CST
# File Name: visualConnectionImageForThumbnail.py
# Description:  将每幅图像尺度化为缩略图形式，缩略图的最大边为 100 像素
"""

import pydot
from PIL import Image

threshold = 2  #创建关联需要的最小匹配数目

g = pydot.Dot(graph_type='graph')  #不使用默认的有向图
for i in range(nbr_images):
    for j in range(i+1, nbr_images):
        if matchscore[i, j] > threshold:
            #图像对中的第一幅图像
            im = Image.open(imlist[i])
            im.thumbnail((100, 100))
            filename = str(i) + '.png'
            im.save(filename) #需要一定大小的临时文件
            g.add_node(pydot.Node(str(i), fontcolor='transparent', shape='rectangle',image=path+filename))


            #图像对中的第二幅图像
            im = Image.open(imlist[j])
            im.thumbnail((100, 100))
            filename = str(j) + '.png'
            im.save(filename) #需要一定大小的临时文件
            g.add_node(pydot.Node(str(j), fontcolor='transparent', shape='rectangle',image=path+filename))


            g.add_edge(pydot.Edge(str(i), str(j)))


    g.write_png('whitehouse.png')


