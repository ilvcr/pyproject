#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 14 May 2018 11:57:11 PM CST
# File Name: best_implemt_grammer_03.py
# Description:  使用tokenize模块将在文本之外生成令牌，针对每个处理过的行返回一个迭代器
"""

import tokenize

reader = open('best_implemt_grammer_02.py').next

tokens = tokenize.generate_tokens(reader)

print tokens.next()
print tokens.next()
print tokens.next()
print tokens.next()
print tokens.next()
print tokens.next()


