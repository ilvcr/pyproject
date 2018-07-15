#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: NewtonRaphsonMethod.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月15日 星期日 20时29分04秒
# Description:  Implementing Newton Raphson method in python 
#************************************************************************#


from sympy import diff
from decimal import Decimal
from math import sin, cos, exp

def NewtonRaphson(function, a):
    #Finds root from the point 'a' onwards by Newton-Raphson method
    while True:
        x = a
        c = Decimal(a) - (Decimal(eval(function)) / Decimal(eval(str(diff(function)))))

        x = c
        a = c
        # This number dictates the accuracy of the answer
        if abs(eval(function)) < 10**-15:
            return c


#Let's Execute
if __name__ == '__main__':
    #Find root of trignometric fucntion
    #Find value of  pi
    print 'sin(x) = 0', NewtonRaphson('sin(x)', 2)

    #Find root of polynomial
    print ('x**2 - 5*x +2 = 0', NewtonRaphson('x**2 - 5*x +2', 0.4))
            
    #Find Square Root of 5
    print ('x**2 - 5 = 0', NewtonRaphson('x**2 - 5', 0.1))

    #Exponential Roots
    print ('exp(x) - 1 = 0', NewtonRaphson('exp(x) - 1', 0))



