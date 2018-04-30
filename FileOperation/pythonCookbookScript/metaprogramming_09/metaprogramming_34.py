#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 12:48:20 PM CST
# File Name: metaprogramming_34.py
# Description:  拆解 Python 字节码
"""

#生成器函数可以将原始字节码序列转换成 opcodes 和参数

import opcode

def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i+1]*256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue

        else:
            oparg = None

        yield (op, oparg)


#使用方法
for op, oparg in generate_opcodes(countdown.__code__.co_code):
    print(op, opcode.opname[op], oparg)
