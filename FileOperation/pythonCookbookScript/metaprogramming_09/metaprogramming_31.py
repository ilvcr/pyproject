#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 03:59:59 AM CST
# File Name: metaprogramming_31.py
# Description:  写一个上下文管理器，你需要定义一个类，里面包含一个enter () 和一个 exit () 方法
"""

import time

class timethis(object):
    def __init__(self, label):
        self.label = label


    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print('{}:{}'.format(self.label, end - self.start))
