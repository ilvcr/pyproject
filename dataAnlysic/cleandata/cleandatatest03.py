#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: cleandatatest03.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 18:18:54 2019
# Description: 
#************************************************************************#


val = 'a,b,   guido'
print "\n"
print val.split(',')
pieces = [x.strip() for x in val.split(',')]
print "\n"
print pieces
print "\n"
first, second, third = pieces
print first + '::' + second + '::' + third
print "\n"
print '::'.join(pieces)
print "\n"
print 'guido' in val

print "\n"
import re
text = "foo   bar\t  baz \tqux"
print "\n"
print text
print "\n"
print re.split('\s+', text)
print "\n"
regex = re.compile('\s+')
print regex.split(text)
print "\n"
print regex.findall(text)
print "\n"






