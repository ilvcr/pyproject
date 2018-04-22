#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 11 Apr 2018 11:13:05 PM CST
# File Name: deencryptDocuments.py
# Description:文件解密
"""

filejia= open(r"FILEPATH\FILENAMEENCRYPTE","r")
filejie=open(r"FILEPATH\FILENAMEDEENCRYPTE","w")
ch=True
while ch:
    ch=filejia.read(1)
    if ch:#已读取到
        jiach= chr(ord(ch)-1) #加密的字符
        filejie.write(jiach)

filejia.close()
filejie.close()
