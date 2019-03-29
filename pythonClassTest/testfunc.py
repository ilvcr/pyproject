#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testfunc.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Mar 28 19:47:44 2019
# Description: 
#************************************************************************#


def f(a, b):
    a += b
    return a

x = 1
y = 2
fxy = f(x, y)

print "f(x, y) = {}".format(fxy) + "\n"

#print fxy

print "x, y = {}, {}".format(x, y) + "\n"

a = [1, 2]
b = [3, 4]
fab = f(a, b)

print "f(a, b) = {}".format(fab) + "\n"

print "a, b = {}, {}".format(a, b) +"\n"


t = (10, 20)
u = (30, 40)
ftu = f(t, u)

print "f(t, u) = {}".format(ftu) + "\n"

print "t, u = {}, {}".format(t, u) + "\n"



