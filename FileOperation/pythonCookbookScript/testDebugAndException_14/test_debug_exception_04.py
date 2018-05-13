#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 12 May 2018 08:01:11 PM CST
# File Name: test_debug_exception_04.py
# Description:  补丁函数
"""

#example.py

from urllib.request import urlopen
import csv


def dowprices():
    u = urlopen('http://finance.yahoo.com/d/quotes.csv?s=@^DJI&f=sl1')
    lines = (line.decode('utf-8') for line in u)
    rows = (row for row in csv.reader(lines) if len(row) == 2)
    prices = {name: float(price) for name, price in rows}
    return prices


