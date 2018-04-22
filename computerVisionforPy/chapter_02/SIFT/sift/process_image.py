#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 01:02:22 PM CST
# File Name: process_image.py
# Description:  处理一幅图像，然后将结果保存在文件中
"""

from scipy.ndimage import filters
from pylab import *

def process_image(imagename, resultname, params="--edge-thresh --peak-thresh 5"):
    '''处理一幅图像，然后将结果保存在文件中'''

    if imagename[-3:] !='pgm':
        #创建一个pgm文件
        im = Image.open(imagename).convert('L')
        im.save('tmp.pgm')
        imagename = 'tmp.pgm'

    cmmd = str("sift"+imagename+" --output="+resultname+" "+params)

    os.system(cmmd)

    print("process", imagename, "to", resultname)
