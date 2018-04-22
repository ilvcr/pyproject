#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
 Author       : Yoghourt.Lee->lvcr
 Last modified: 2018-04-04 16:03
 Email        : liyaoliu@foxmail.com or ilvcr@outlook.com
 Filename     : util.py
 Description  :
'''

def lines(file):
    """
    生成器,在文本最后加一空行
    """
    for line in file: yield line
    yield '\n'

def blocks(file):
    """
    生成器,生成单独的文本块
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
