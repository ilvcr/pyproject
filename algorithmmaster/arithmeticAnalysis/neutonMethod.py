#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: neutonMethod.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月15日 星期日 20时23分55秒
# Description: 
#************************************************************************#

def newton(function, function1, startingInt):
    #function is the f(x) and function1 is the f'(x)
    x_n = startingInt

    while True:
        x_n1 = x_n - function(x_n) / function1(x_n)
        if abs(x_n - x_n1) < 0.00001:
            return x_n1
    x_n = x_n1


def f(x):
    return (x**3) - 2*x - 5

def f1(x):
    return 3 * (x**2) - 2

print newton(f, f1, 3)


