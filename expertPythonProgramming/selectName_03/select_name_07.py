#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 17 May 2018 01:05:09 PM CST
# File Name: select_name_07.py
# Description:  *args的使用
"""

def sum(*args): #可行
    total = 0
    for arg in args:
        total += arg
    return total


def sum(sequence):
    total = 0
    for arg in args:
        total += arg
    return total


def make_sentence(**kwargs):
    noun = kwargs.get('noun', 'Bill')
    verb = kwargs.get('verb', 'is')
    adj = kwargs.get('adjective', 'happy')
    return '{} {} {}'.format(noun, verb, adj)

def make_sentence_1(noun='Bill', verb='is', adjective='happy'):
    return '{} {} {}'.foramt(noun, verb, adjective)


def log_request_1(request):
    print request.get('HTTP_REFERER', 'No referer')


def log_request_2(request):
    print request.get('HTTP_REFERER', 'No referer')
    print request.get('HTTP_HOST', 'No host')


import logging
def log(**context):
    logging.info('Context is: \n{}\n'.format(str(context)))



