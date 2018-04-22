#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 11:11:51 PM CST
# File Name: transformImageFormat_02.py
# Description:  imtools
                代码功能：
                        创建一个包含文件夹中所有图像的文件名列表,
                        用来储存一些经常使用的图像操作。
"""

import os

def get_imlist(path):
    """返回目录中所有JPG图像的文件名列表"""
    return [os.path.join(path, f) for f in os.listdir(path) if f.endwith('.jpg')]
