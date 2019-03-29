#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testcheese.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Mar 28 20:07:05 2019
# Description: 
#************************************************************************#


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese({})',format(self.kind)




