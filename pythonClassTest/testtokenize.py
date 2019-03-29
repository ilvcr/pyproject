#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testtokenize.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 12:48:41 2019
# Description: 
#************************************************************************#


import tokenize

reader = open('testfunc.py').next

tokens = tokenize.generate_tokens(reader)

print '---------------------------------'
print tokens.next()
print '---------------------------------'

print tokens.next()
print '---------------------------------'

print tokens.next()
print '---------------------------------'

print tokens.next()
print '---------------------------------'

print tokens.next()
print '---------------------------------'

print tokens.next()
print '---------------------------------'






