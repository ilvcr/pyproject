#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 12 May 2018 07:37:00 PM CST
# File Name: test_debug_exception_01.py
# Description:  测试stdout输出
"""

#mymodule.py

def urlprint(protocol, host, domain):
    url = '{}://{}.{}'format(protocol, host, domain)
    print(url)


#默认情况下内置的print函数会将输出发送到 sys.stdout
