#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 08 May 2018 02:16:51 PM CST
# File Name: network_and_web_30.py
# Description:  通过网络连接发送和接受连续数据的大型数组，并尽量减少数据的复制操作
"""

#利用 memoryviews 来发送和接受大数组
#zerocopy.py

def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]

def recv_into(arr, source):
    view = memoyview(arr).cast('B')
    while len(view):
        nrecv = source.recv_into(view)
        view = view[nrecv:]

