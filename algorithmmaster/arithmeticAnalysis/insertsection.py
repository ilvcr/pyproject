#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: insertsection.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月15日 星期日 20时06分34秒
# Description: 
#************************************************************************#

import math

def insertsection(function, x0, x1):
    #function is the f we want to find its root and x0 and x1 are two random starting points
    x_n = x0
    x_n1 = x1

    while True:
        x_n2 = x_n1 - (function(x_n1) / ((function(x_n1) - function(x_n)) / (x_n1 - x_n)))

        if abs(x_n2 - x_n1) < 0.0001:
            return x_n2

    x_n = x_n1
    x_n1 = x_n2

def f(x):
    return math.pow(x, 3) - 2*x -5

print insertsection(f, 3, 3.5)



