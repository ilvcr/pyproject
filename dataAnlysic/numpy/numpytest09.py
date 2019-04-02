#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: numpytest09.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 16:56:54 2019
# Description: 
#************************************************************************#

import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01)
print "\n"
print points
print "\n"
xs, ys = np.meshgrid(points, points)
print ys
print "\n"
z = np.sqrt(xs ** 2 + ys ** 2)
print "\n"
print z
print "\n"
print plt.imshow(z, cmap=plt.cm.gray)
print "\n"
print plt.colorbar()
print "\n"
print plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
print "\n"

print "\n"

print "\n"

print "\n"

print "\n"

print "\n"
