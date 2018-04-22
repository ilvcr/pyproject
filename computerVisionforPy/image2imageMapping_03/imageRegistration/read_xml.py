#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 22 Apr 2018 05:01:43 PM CST
# File Name: read_xml.py
# Description:  读取 XML 文件，其中文件名为键，点的坐标为键值。然后配准所有的图像，将它们与第一幅图像对齐
"""

import imregistration


#载入控制点的位置
xmlFileName = 'jkface2008_small/jkfaces.xml'

points = imregistration.read_points_from_xml(xmlFileName)

#注册
imregistration.rigid_alignment(points, 'jkface2008_small/')
