#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 01:29:42 PM CST
# File Name: featureLocationImageofSIFT.py
# Description:
"""

from scipy.ndimage import filters
from pylab import *
from numpy import *
from PIL import Image


imname = 'example.jpg'
im1 = array(Image.open(imname).convert('L'))
sift.process_image(imname,'example.sift')
l1,d1 = sift.read_features_from_file('example.sift')


figure()
gray()
sift.plot_features(im1,l1,circle=True)
show()
