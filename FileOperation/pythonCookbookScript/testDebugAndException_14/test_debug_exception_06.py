#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 12 May 2018 08:42:35 PM CST
# File Name: test_debug_exception_06.py
# Description:  在单元测试中测试异常情况
"""

#测试某个函数抛出的ValueError异常
import unittest

#A sample function to illustrate
def parse_int(s):
    return int(s)


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')



#测试异常的具体值
import errno

class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)

        else:
            self.fall('IOError not raised')

#手动进行异常检测
class TestConversion1(unittest.TestCase):
    def test_bad_int(self):
        try:
            r = parse_int('N/A')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
