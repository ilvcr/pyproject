#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: bisection.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月15日 星期日 19时51分24秒
# Description: 
#************************************************************************#

import math

def bisection(function, a, b):  #finds where the function become 0 in [a,b] using bolzano
    
    start = a
    end = b

    if function(a) == 0:  #one of the a or b is a root for the function
        return a
    elif function(b) == 0:
        return b
    elif function(a) * function(b) > 0:  
        #if none of these are root and they are both positive or negative,
        #then his algorithm can't find the root
        print "could't find root in [a,b]"
        return
    else:
        mid = (start + end) / 2
        while abs(start - mid) > 0.0000001:  # until we achieve precise equals to 10^-7
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = (start + end) / 2
        return mid

def f(x):
    return math.pow(x, 3) - 2*x -5


print bisection(f, 1, 100)


