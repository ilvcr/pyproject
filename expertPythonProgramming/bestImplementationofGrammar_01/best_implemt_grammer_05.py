#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 12:09:03 AM CST
# File Name: best_implemt_grammer_05.py
# Description:  将yield变成一个表达式，值通过名为send的新方法来传递
"""

def psychologist():
    print 'Please tell me your problem'

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
print free.next()

print free.send('I fell bad')  #send的工作机制与next一样，但yield将变成能够返回传入的值

print free.send("Why I shouldn't?")


