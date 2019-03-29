#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testfibonacci.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 12:44:47 2019
# Description: 
#************************************************************************#

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib = fibonacci()
print '-----------------------'
print fib.next()
print '-----------------------'
print fib.next()

print '-----------------------'
print fib.next()

print '-----------------------'
print fib.next()

print '-----------------------'
print fib.next()



print [fib.next() for i in range(20)]

print '-----------------------'




