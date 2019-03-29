#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testfunc_02.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 12:58:21 2019
# Description: 
#************************************************************************#

def psychologist():
    print 'PLS tell me your problems'
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print "Don't ask yourself too much questions"
            elif 'good' in answer:
                print "A that's good, go on"
            elif 'bad' in answer:
                print "Don't be so negative"

free = psychologist()
print '======================================'
print free.next()
print '======================================'
print free.send('I feel bad')
print '======================================'
print free.send("Why I shouldn't?")
print '======================================'
print free.send("ok then i should find what is good for me.")
print '======================================'

print '======================================'

print '======================================'



