#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 11 Apr 2018 11:10:04 PM CST
# File Name: encryptDocuments.py
# Description:文件加密
"""

file= open(r"FILEPATH\FILENAME","r")
filejia=open(r"FILEPATH\FILENAMEENCRYPT","w")
ch=True
while ch:
    ch=file.read(1)
    if ch:#已读取到
    jiach= chr(ord(ch)+1) #加密的字符
    filejia.write(jiach)


file.close()
filejia.close()

