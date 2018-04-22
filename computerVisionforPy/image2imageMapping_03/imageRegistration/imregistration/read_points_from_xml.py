#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 22 Apr 2018 04:28:19 PM CST
# File Name: read_points_from_xml.py
# Description:  读取用于人脸对齐的控制点
"""

from xml.dom import minidom

def read_points_from_xml(xmlFileName):
    '''读取用于人脸对齐的控制点'''

    xmldoc = minidom.parse(xmlFileName)
    facelist = xmldoc.getElementsByName('face')
    faces = {}

    for xmlFace in facelist:
        fileName = xmlFace.attributes['file'].value
        xf = int(xmlFace.attributes['xf'].value)
        yf = int(xmlFace.attributes['yf'].value)
        xs = int(xmlFace.attributes['xs'].value)
        ys = int(xmlFace.attributes['ys'].value)
        xm = int(xmlFace.attributes['xm'].value)
        ym = int(xmlFace.attributes['ym'].value)
        faces[fileName] = array([xf, yf, xs, ys, xm, ym])

    return faces


'''
标记点会在 Python 中以字典的形式返回，字典的键值为图像的文件名。
格式为：图像中左眼（人脸右侧）的坐标为 xf 和 yf，右眼的坐标为 xs 和 ys，嘴的坐标为 xm 和 ym。
为了计算相似变换中的参数，我们可以使用最小二乘解来解决。
'''

