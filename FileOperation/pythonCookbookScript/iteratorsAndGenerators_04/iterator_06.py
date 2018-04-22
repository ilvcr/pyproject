#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 17 Apr 2018 05:12:25 PM CST
# File Name: iterator_06.py
# Description:  代码功能：
                        简单将生成器实现为一个类, 然后把生成器放到__iter__()方法中去, 然后把生成器
                        暴露外部状态给用户
"""

from collection import deque

class linehistory(object):
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=hislen)

    def __iter__():
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


#A Example__filenamw为文件名
if __name__ == '__main__':
    with open('filename') as f:
        lines = linehistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')
