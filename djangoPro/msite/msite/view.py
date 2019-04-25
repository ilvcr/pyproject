#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: view.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 25 12:02:16 2019
# Description: 
#************************************************************************#

from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello world!')

