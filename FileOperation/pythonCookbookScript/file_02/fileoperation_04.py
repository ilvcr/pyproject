#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 13 Apr 2018 04:25:23 PM CST
# File Name: fileoperation_04.py
# Description:本代码为在多行上面做简单的文本匹配, 并只返回在前N行中匹配成功的行
              collections.deque作用: 保留有限历史记录
"""

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

#Example use on a file
if __name__ == '__main__':
    with open(r'AFILEPATH') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
