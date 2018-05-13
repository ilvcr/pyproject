#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 12 May 2018 07:52:22 PM CST
# File Name: test_debug_exception_03.py
# Description:  在单元测试中给对象打补丁

"""

#将patch()当作一个装饰器, 上下文管理器或者单独使用
'''
unittest.mock.patch()函数用来给对象补丁
'''

from unittest.mock import patch
import example


#装饰器
@patch('example.func')
def test(x, mock_func):
    example.func(x)     #Uses patched example.func
    mock_func.assert_called_with(x)

#上下文管理器
with patch('example.func') as mock_func:
    example.func(x)
    mock_func.assert_called_with(x)


#手动打补丁
p = patch('example.func')
mock_func = p.start()
example.func(x)
mock_func.assert_called_with(x)
p.stop()


